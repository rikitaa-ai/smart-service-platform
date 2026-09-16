from django.urls import path

from .views import (
    ApplicationListCreateView,
    ApplicationDetailView,
    ReviewApplicationView,
    VerifyApplicationView,
    ApproveApplicationView,
    RejectApplicationView,
    DocumentListCreateView,
    VerifyDocumentView,
)


urlpatterns = [
    path(
        "",
        ApplicationListCreateView.as_view(),
        name="application-list-create"
    ),

    path(
        "<int:pk>/",
        ApplicationDetailView.as_view(),
        name="application-detail"
    ),

    path(
        "<int:pk>/review/",
        ReviewApplicationView.as_view(),
        name="application-review"
    ),

    path(
        "<int:pk>/verify/",
        VerifyApplicationView.as_view(),
        name="application-verify"
    ),

    path(
        "<int:pk>/approve/",
        ApproveApplicationView.as_view(),
        name="application-approve"
    ),

    path(
        "<int:pk>/reject/",
        RejectApplicationView.as_view(),
        name="application-reject"
    ),

    path(
        "<int:application_id>/documents/",
        DocumentListCreateView.as_view(),
        name="document-list-create"
    ),

    path(
        "<int:application_id>/documents/<int:document_id>/verify/",
        VerifyDocumentView.as_view(),
        name="document-verify"
    ),
]