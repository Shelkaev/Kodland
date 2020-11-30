from django import forms
from create_article.models import ArticleApply


class ArticleApplyForm(forms.ModelForm):
    class Meta:
        model = ArticleApply
        fields = ['photo', 'name', 'article']
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", 'placeholder': '  Введите название статьи'}),
            'article': forms.Textarea(attrs={'class': "form-control", 'name': "editor1"}),
            'photo': forms.FileInput(attrs={'class': "btn btn-primary btn-block", 'required': False, }, ),
        }
