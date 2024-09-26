from django import forms
from .models import UserComment

class UserCommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = ['name', 'email', 'comment']
        
    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if len(comment) > 200:
            raise forms.ValidationError("Comment cannot exceed 200 characters.")
        return comment
