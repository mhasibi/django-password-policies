from django.urls import include
from django.conf.urls import url

from password_policies.tests.views import TestHomeView


urlpatterns = [
               url(r'^password/', include('password_policies.urls')),
               url(r'^$', TestHomeView.as_view(), name='home')
               ]
