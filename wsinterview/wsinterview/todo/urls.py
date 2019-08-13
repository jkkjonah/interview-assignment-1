from django.conf.urls import url

import views


urlpatterns = [
    url(r'^$', views.TodoView.as_view() , name='todo'),
    url(r'^create/$', views.TaskCreateForm.as_view() , name='todo-create'),
]
