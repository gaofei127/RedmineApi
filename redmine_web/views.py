from django.shortcuts import render, HttpResponse, redirect
from redmine_web.models import  People, Ariticle, Comment
from django.template import Context, Template
from django import forms
from redmine_web.form import CommentForm

# Create your views here.

# firs_try to understand MTV
# def first_try(request):
#     person = People(name='spock', job='officer')
#     html_string = '''
#         <html>
#         <h1>{{ person.name }}</h1>
#         </html>
#
#     '''
#     t = Template(html_string)
#     c = Context({'person': person})
#     web_page = t.render(c)
#     return HttpResponse(web_page)




def index(request):
    # print(request)
    # print('===='*30)
    # print(dir(request))
    # print('===='*30)
    # print(type(request))
    queryset = request.GET.get('tag')
    if queryset:
        article_list = Ariticle.objects.filter(tag=queryset)
    else:
        article_list = Ariticle.objects.all()
    context = {}
    context['article_list1'] = article_list
    index_page = render(request, 'first_web_2.html', context)
    return index_page

def detail(request):
    if request.method == 'GET':
        form = CommentForm
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            c = Comment(name=name, comment=comment)
            c.save()
            return redirect(to='detail')

        # print(form.errors)
        # print(form)
    context = {}
    comment_list = Comment.objects.all()
    # article = Ariticle.objects.get(id=page_num)
    # context['article'] = article
    context['comment_list'] = comment_list
    context['form'] = form
    return render(request, 'detail.html', context)