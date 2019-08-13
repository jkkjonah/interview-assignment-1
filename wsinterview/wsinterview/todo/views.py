from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy

from .models import Task
from .forms import TaskForm


class TodoView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        ctx = super(TodoView, self).get_context_data()
        ctx['tasks'] = Task.objects.order_by('id')
        return ctx


class TaskCreateForm(FormView):

    template_name = 'add_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('todo')

    def form_valid(self, form):
        form.save()
        return super(TaskCreateForm, self).form_valid(form)