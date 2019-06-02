from django import forms
from .models import Article
from django.utils import timezone

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = {'title', 'author', 'body', 'draft'}

    def clean_date(self):
        draft = self.cleaned_data.get('draft')
        published_date = form.get('published_date')
        present = datetime.date.today()
        if draft is True and published_date < present:
            raise ValidationError('Published date must be in present.')
        elif draft is False and published_date > present:
            raise ValidationError('Published date must be in past.')

    




