from django.conf.urls import url

from .views import PasswordChangeFormView
from .views import PasswordChangeDoneView
from .views import PasswordResetCompleteView
from .views import PasswordResetConfirmView
from .views import PasswordResetFormView
from .views import PasswordResetDoneView


urlpatterns = [
   url(r'^change/done/$',PasswordChangeDoneView.as_view(), name='password_change_done'),
   url(r'^change/$', PasswordChangeFormView.as_view(), name="password_change"),
   url(r'^reset/$', PasswordResetFormView.as_view(), name="password_reset"),
   url(r'^reset/complete/$', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
   url(r'^reset/confirm/([0-9A-Za-z_\-]+)/([0-9A-Za-z]{1,13})/([0-9A-Za-z-=_]{1,32})/$', PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
   url(r'^reset/done/$', PasswordResetDoneView.as_view(), name="password_reset_done"),
   ]
