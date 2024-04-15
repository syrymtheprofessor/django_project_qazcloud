from django import forms
from .models import ArticleComment


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ["content", "author", "author_email"]
        widgets = {
            "content": forms.Textarea(
                attrs={"placeholder": "Добавить комментарии..."}
            ),
            "author": forms.TextInput(
                attrs={"placeholder": "Имя"}
            ),
            "author_email": forms.TextInput(
                attrs={"placeholder": "E-mail"}
            ),
        }