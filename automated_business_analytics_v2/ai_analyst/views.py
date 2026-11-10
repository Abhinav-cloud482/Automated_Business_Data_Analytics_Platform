import pandas as pd
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datasets.models import Dataset
from .models import AIConversation, AIMessage

@login_required
def ai_analyst_view(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk, user=request.user)
    conv, _ = AIConversation.objects.get_or_create(user=request.user, dataset=dataset)

    file_path = dataset.cleaned_file.path if dataset.is_cleaned and dataset.cleaned_file else dataset.original_file.path
    df = pd.read_excel(file_path) if file_path.endswith(('.xlsx', '.xls')) else pd.read_csv(file_path)

    if request.method == 'POST':
        question = request.POST.get('question', '').strip()
        if question:
            AIMessage.objects.create(conversation=conv, sender='user', message_text=question)

            # Safe rule-based analytical reasoning layer
            answer = f"I analyzed your dataset ('{dataset.name}', {len(df)} rows). "
            q_lower = question.lower()

            num_cols = df.select_dtypes(include='number').columns

            if 'total' in q_lower or 'sum' in q_lower:
                if len(num_cols) > 0:
                    col = num_cols[0]
                    total = df[col].sum()
                    answer += f"The total sum of '{col}' is **{total:,.2f}**."
                else:
                    answer += "No numerical columns found for summation."
            elif 'average' in q_lower or 'mean' in q_lower:
                if len(num_cols) > 0:
                    col = num_cols[0]
                    mean_val = df[col].mean()
                    answer += f"The average of '{col}' is **{mean_val:,.2f}**."
                else:
                    answer += "No numerical columns found."
            elif 'row' in q_lower or 'count' in q_lower:
                answer += f"Total record count is **{len(df):,}** rows and **{len(df.columns)}** columns."
            else:
                answer += f"Based on your query, the dataset contains {len(df)} records across {len(df.columns)} columns. Try asking for sums, averages, or record counts!"

            AIMessage.objects.create(conversation=conv, sender='ai', message_text=answer)
            return redirect('ai_analyst_view', pk=dataset.pk)

    messages = conv.messages.all().order_by('created_at')
    return render(request, 'ai_analyst/analyst.html', {
        'dataset': dataset,
        'messages': messages
    })
