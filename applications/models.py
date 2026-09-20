from django.db import models
from accounts.models import User


class Application(models.Model):
    STATUS_CHOICES = [
        ('SUBMITTED', 'Submitted'),
        ('UNDER_REVIEW', 'Under Review'),
        ('DOCUMENT_VERIFIED', 'Document Verified'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    application_number = models.CharField(
        max_length=20,
        unique=True
    )

    service_type = models.CharField(
        max_length=100
    )

    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='SUBMITTED'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='applications'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.application_number


class Document(models.Model):
    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name='documents'
    )

    document_type = models.CharField(
        max_length=100
    )

    document_file = models.CharField(
        max_length=255
    )

    is_verified = models.BooleanField(
        default=False
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.document_type