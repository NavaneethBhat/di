from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ims import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'di.views.home', name='home'),
    # url(r'^di/', include('di.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', views.user_page,name="index"),
    url(r'^login/', views.user_login,name="login"),
    url(r'^phone/', views.phone_client,name="phone"),
    url(r'^chat/', views.chat_client,name="chat"),
    url(r'^note/', views.note_client,name="note"),


)
