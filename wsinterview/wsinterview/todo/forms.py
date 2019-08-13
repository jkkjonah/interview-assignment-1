from django import forms

from .models import Task, TaskLabel, CalendarEvent


class TaskForm(forms.ModelForm):
    """
    Form for creating and editing a single task
    """

    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'due_date']

    due_date = forms.DateTimeField(required=False)

    def save(self, commit=True):
        task = super(TaskForm, self).save(commit)
        due_date = self.cleaned_data.get('due_date')
        if due_date:
            event = CalendarEvent.objects.create(datetime=due_date)
            task.due_date = event

        if commit:
            task.save()

        return task


class DeleteTaskForm(forms.ModelForm):
    """
    Simple form for deleting task
    """

    class Meta:
        model = Task
        fields = []


class TaskLabelForm(forms.ModelForm):
    """
    For creating and editing a single task label
    """

    class Meta:
        model = TaskLabel
        fields = ['name']


class AssignTaskLabelForm(forms.Form):
    """
    Simple form for assigning/unassigning task labels
    """

    task_id = forms.IntegerField(required=True)
    label_id = forms.IntegerField(required=True)

    def clean_task_id(self):
        task_id = self.cleaned_data['task_id']
        try:
            Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            raise forms.ValidationError('invalid task id')

        return task_id

    def clean_label_id(self):
        label_id = self.cleaned_data['label_id']
        try:
            Task.objects.get(id=label_id)
        except TaskLabel.DoesNotExist:
            raise forms.ValidationError('invalid label id')

