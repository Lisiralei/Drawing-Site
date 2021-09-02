from django.contrib import admin
from django.urls import path
import core.views

urlpatterns = [
    path('', core.views.HomepageView.as_view(), name = 'Home'),
    path('login/', core.views.NormalUserLoginView.as_view(), name = 'Login')
]