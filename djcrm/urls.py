


from django.contrib import admin
from django.urls import path, include
from leads.views import *
from django.conf import settings
from django.conf.urls.static import static

from leads.views import SignupView
from django.contrib.auth.views import (
                    LoginView, 
                    LogoutView, 
                    PasswordResetView, 
                    PasswordResetDoneView,
                    PasswordResetConfirmView,
                    PasswordResetCompleteView,
    )
                    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace="leads")),
    path('agents/', include('agents.urls', namespace="agents")),
    path('', landing_page, name='landing-page' ),
    # class based view url 
    # path('', LandingpageView.as_view(), name='landing-page' ),

    path('signup/', SignupView.as_view(), name="signup"),
    path('reset-password/', PasswordResetView.as_view(), name="reset-password"),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)