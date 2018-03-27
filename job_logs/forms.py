"""Form to let users add a new topic."""

from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """Class for forms."""

    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """Class for entry forms."""

    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
