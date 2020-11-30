from create_article.models import ArticleApply
from create_article.forms import ArticleApplyForm
from django.contrib import messages
from django.views.generic import CreateView


# Create your views here.

class ArticleApplyView(CreateView):
    model = ArticleApply
    form_class = ArticleApplyForm
    template_name = 'create_article.html'
    success_url = '/create_article/'

    def form_valid(self, form):
        message = form.save()
        messages.success(self.request, 'Статья опубликована')
        return super().form_valid(message)




