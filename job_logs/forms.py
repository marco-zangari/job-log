"""Form to let users add a new topic."""

from django import forms

from .models import Topic


class TopicForm(forms.ModelForm):
    """Class for forms."""

    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
