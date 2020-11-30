'''from django.shortcuts import render
from create_article.models import ArticleApply
from create_article.forms import ArticleApplyForm
from django.contrib import messages


# Create your views here.
def contact_delete(request, contact_id):
    articleapply = ArticleApply.objects.get(id=contact_id)
    if request.method == 'POST':
        ms = 'Сообщение от пользавателя ' + articleapply.name + '<br/>' + 'Адрес эл. почты: ' + articleapply.email + \
             '<br/>' + 'успешно удалено.'
        articleapply.delete()
        messages.success(request, ms)
        return redirect(to='/contact/')

    return render(request, 'creaate_article.html', {'articleapply': articleapply})'''