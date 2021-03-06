from django.urls import path

from users.api.views.activation_token import ActivateTokenView, RenewActivateTokenView
from users.api.views.auth import (
    EndWorkerView,
    EndWorkerLoginView,
    EndWorkerLogoutView,
    EndWorkerRegistrationView,
    EndWorkerEmailInfoView,
    EndWorkerUsernameInfoView,
    EndWorkerStatusView,
    EndWorkerDetailsView
)
from users.api.views.change_password import ChangePasswordView
from users.api.views.change_settings import ChangeSettingsView
from users.api.views.mturk import (
    MturkRegisterLoginView
)
from users.api.views.password_token import ResetPasswordTokenView
from users.api.views.reset_password import ResetPasswordView
from users.api.views.storage import (
    EndWorkerStorageView, EndWorkerStorageBatchView
)


urlpatterns = [
    path('check/email/', EndWorkerEmailInfoView.as_view(), name='check_email_end_worker'),
    path('check/username/', EndWorkerUsernameInfoView.as_view(), name='check_username_end_worker'),
    path('login/', EndWorkerLoginView.as_view(), name='login_end_worker'),
    path('mturk/', MturkRegisterLoginView.as_view(), name='register_mturk'),
    path('activate/', ActivateTokenView.as_view(), name='activate_token'),
    path('activate/renew/', RenewActivateTokenView.as_view(), name='renew_activate_token'),
    path('change_settings/', ChangeSettingsView.as_view(), name='end_worker_change_settings'),
    path('change_password/', ChangePasswordView.as_view(), name='end_worker_change_password'),
    path('reset_password/', ResetPasswordView.as_view(), name='end_worker_reset_password'),
    path('reset_password/token/', ResetPasswordTokenView.as_view(), name='end_worker_reset_password_token'),
    path('register/', EndWorkerRegistrationView.as_view(), name='register_end_worker'),
    path('current/', EndWorkerView.as_view(), name='current_end_worker'),
    path('status/', EndWorkerStatusView.as_view(), name='end_worker_status'),
    path('details/', EndWorkerDetailsView.as_view(), name='end_worker_details'),
    path('logout/', EndWorkerLogoutView.as_view(), name='end_worker_logout'),
    path('storage/<str:key>/', EndWorkerStorageView.as_view(), name='end_worker_storage'),
    path('storage/', EndWorkerStorageBatchView.as_view(), name='end_worker_storage_batch'),
]
