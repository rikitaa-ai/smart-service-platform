from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema

from .models import Application, Document
from .serializers import ApplicationSerializer, DocumentSerializer
from accounts.permissions import IsOfficer


class ApplicationListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        applications = Application.objects.filter(
            user=request.user
        )

        serializer = ApplicationSerializer(
            applications,
            many=True
        )

        return Response(serializer.data)

    @extend_schema(
        request=ApplicationSerializer,
        responses=ApplicationSerializer
    )
    def post(self, request):
        serializer = ApplicationSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response(
                serializer.data,
                status=201
            )

        return Response(
            serializer.errors,
            status=400
        )


class ApplicationDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        application = get_object_or_404(
            Application,
            pk=pk,
            user=request.user
        )

        serializer = ApplicationSerializer(application)

        return Response(serializer.data)


class ReviewApplicationView(APIView):
    permission_classes = [IsAuthenticated, IsOfficer]

    def post(self, request, pk):
        application = get_object_or_404(
            Application,
            pk=pk
        )

        if application.status != "SUBMITTED":
            return Response(
                {
                    "error": "Application must be submitted first."
                },
                status=400
            )

        application.status = "UNDER_REVIEW"
        application.save()

        return Response(
            {
                "message": "Application is now under review.",
                "status": application.status
            }
        )


class VerifyApplicationView(APIView):
    permission_classes = [IsAuthenticated, IsOfficer]

    def post(self, request, pk):
        application = get_object_or_404(
            Application,
            pk=pk
        )

        if application.status != "UNDER_REVIEW":
            return Response(
                {
                    "error": "Application must be under review."
                },
                status=400
            )

        documents = Document.objects.filter(
            application=application
        )

        if not documents.exists():
            return Response(
                {
                    "error": "Application has no documents."
                },
                status=400
            )

        if not all(document.is_verified for document in documents):
            return Response(
                {
                    "error": "All documents must be verified first."
                },
                status=400
            )

        application.status = "DOCUMENT_VERIFIED"
        application.save()

        return Response(
            {
                "message": "All documents verified successfully.",
                "status": application.status
            }
        )


class ApproveApplicationView(APIView):
    permission_classes = [IsAuthenticated, IsOfficer]

    def post(self, request, pk):
        application = get_object_or_404(
            Application,
            pk=pk
        )

        if application.status != "DOCUMENT_VERIFIED":
            return Response(
                {
                    "error": "Documents must be verified before approval."
                },
                status=400
            )

        application.status = "APPROVED"
        application.save()

        return Response(
            {
                "message": "Application approved successfully.",
                "status": application.status
            }
        )


class RejectApplicationView(APIView):
    permission_classes = [IsAuthenticated, IsOfficer]

    def post(self, request, pk):
        application = get_object_or_404(
            Application,
            pk=pk
        )

        if application.status == "APPROVED":
            return Response(
                {
                    "error": "Approved application cannot be rejected."
                },
                status=400
            )

        application.status = "REJECTED"
        application.save()

        return Response(
            {
                "message": "Application rejected.",
                "status": application.status
            }
        )


class DocumentListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, application_id):
        application = get_object_or_404(
            Application,
            pk=application_id,
            user=request.user
        )

        documents = Document.objects.filter(
            application=application
        )

        serializer = DocumentSerializer(
            documents,
            many=True
        )

        return Response(serializer.data)

    @extend_schema(
        request=DocumentSerializer,
        responses=DocumentSerializer
    )
    def post(self, request, application_id):
        application = get_object_or_404(
            Application,
            pk=application_id,
            user=request.user
        )

        serializer = DocumentSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save(
                application=application
            )

            return Response(
                serializer.data,
                status=201
            )

        return Response(
            serializer.errors,
            status=400
        )


class VerifyDocumentView(APIView):
    permission_classes = [IsAuthenticated, IsOfficer]

    def post(self, request, application_id, document_id):
        application = get_object_or_404(
            Application,
            pk=application_id
        )

        document = get_object_or_404(
            Document,
            pk=document_id,
            application=application
        )

        if document.is_verified:
            return Response(
                {
                    "message": "Document is already verified.",
                    "is_verified": True
                }
            )

        document.is_verified = True
        document.save()

        return Response(
            {
                "message": "Document verified successfully.",
                "is_verified": True
            }
        )