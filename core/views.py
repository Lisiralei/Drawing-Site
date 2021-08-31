from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

import core.models
# import core.forms
# import core.filters

class TitleMixin:
    title: str = None

    def get_title(self) -> str:
        return self.title

    def get_context_data(self, **kwargs):
        cxt = super().get_context_data()
        cxt['title'] = self.get_title()
        return cxt


class UserMixin:
    username: str = None

    def get_username(self) -> str:
        if self.username:
            return self.username
        return 'unsigned user'

    def get_context_data(self, **kwargs):
        cxt = super().get_context_data()
        cxt['username'] = self.get_username()
        cxt
        return cxt


class HomepageView(TitleMixin, UserMixin, TemplateView):
    template_name = 'core/homepage.html'
    title = 'Homepage'

