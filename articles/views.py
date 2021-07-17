# articles/views.py
from django.contrib.auth.mixins import (
LoginRequiredMixin, # To restrict view access to only logged in users
UserPassesTestMixin # To restrict access
) 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView 
from django.urls import reverse_lazy 
from .models import Article


# List of articles showing in the 'article_list.html'
class ArticleListView(LoginRequiredMixin, ListView): 
    model = Article
    template_name = 'article_list.html'

# The details of a specific article showing in the 'article_detail.html'
class ArticleDetailView(LoginRequiredMixin, DetailView): 
    model = Article
    template_name = 'article_detail.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

# Updating article using 'article_edit.html'
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

# Deleting articles using 'article_delete.html'
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

# Creating an article using 'article_new.html'
class ArticleCreateView(LoginRequiredMixin, CreateView): 
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body',)
    
    # set current author automatically
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)