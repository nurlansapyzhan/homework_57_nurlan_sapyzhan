from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from hw57.models import Task


class TaskDetail(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context