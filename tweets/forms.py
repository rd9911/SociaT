from django import forms
from django.conf import settings

from .models import Tweet

MAX_TWEET_CHAR = settings.MAX_TWEET_CHAR

class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > MAX_TWEET_CHAR:
            raise forms.ValidationError("You exceeded maximum number of characters (240)")
        return content
