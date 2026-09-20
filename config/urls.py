from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import LoginView


urlpatterns = [

    # ADMIN
    path(
        "admin/",
        admin.site.urls
    ),

    # =========================
    # FRONTEND PAGES
    # =========================

    path(
        "",
        TemplateView.as_view(
            template_name="login.html"
        ),
        name="home"
    ),

    path(
        "dashboard/",
        TemplateView.as_view(
            template_name="dashboard.html"
        ),
        name="dashboard"
    ),

    path(
        "apply/",
        TemplateView.as_view(
            template_name="apply.html"
        ),
        name="apply"
    ),

    path(
        "applications/",
        TemplateView.as_view(
            template_name="applications.html"
        ),
        name="applications"
    ),

    path(
        "application/",
        TemplateView.as_view(
            template_name="application.html"
        ),
        name="application"
    ),

    path(
        "officer/",
        TemplateView.as_view(
            template_name="officer_dashboard.html"
        ),
        name="officer-dashboard"
    ),

    path(
        "officer/review/",
        TemplateView.as_view(
            template_name="officer_review.html"
        ),
        name="officer-review"
    ),

    # =========================
    # API
    # =========================

    path(
        "api/applications/",
        include("applications.urls")
    ),

    path(
        "api/auth/login/",
        LoginView.as_view(),
        name="login"
    ),

    path(
        "api/auth/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),
]