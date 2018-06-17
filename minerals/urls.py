from django.conf.urls import url

from . import views


urlpatterns = (
    url(r'^$', views.mineral_list, name='list'),
    url(r'search/$', views.mineral_search, name='search'),
    url(r'(?P<pk>\d+)/$', views.mineral_detail, name='detail'),
    url(r'group_filter/(?P<group>\w+\s*\w*)/$', views.mineral_list_group_filter, name='group_filter'),
    url(r'letter_filter/(?P<letter>\w)/$', views.mineral_list_letter_filter, name='letter_filter'),
    url(r'color_filter/(?P<color>\w+)/$', views.mineral_list_color_filter, name='color_filter'),
)
