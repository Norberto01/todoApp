# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
# from tasks import views
#
# urlpatterns = [
#     # url(r'^$', views.api_root),
#     url(r'^tasks/$', views.TaskList.as_view(), name='task-list'),
#     url(r'^tasks/(?P<pk>[0-9]+)$', views.TaskDetail.as_view(), name='task-detail'),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)