from django import forms

from hw57.models import Issue


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ('summary', 'description', 'status', 'type')
        labels = {
            'summary': 'Краткое описание',
            'description': 'Полное описание',
            'status': 'Статус',
            'type': 'Тип'
        }