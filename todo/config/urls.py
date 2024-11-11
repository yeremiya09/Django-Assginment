"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from todo.views import todo_list, todo_info  # 추가
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("users/", user_list, name="user_list"),
    # path("users/<int:user_id>/", user_info, name="user_info"),

    path('todo/', todo_list, name='todo_list'),  # 추가
    path('todo/<int:todo_id>/', todo_info, name='todo_info'),  # 추가
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', users_views.login, name='login'),
    path('accounts/signup/', users_views.sign_up, name='signup')
]
