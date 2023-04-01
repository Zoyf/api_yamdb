from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from serializers import CommentSerializer
from permissions import IsAdminOrModeratorOrReadOnly
from reviews.models import Review


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrModeratorOrReadOnly, ]

    def get_queryset(self):
        review_id = self.kwargs.get("review_id")
        review = get_object_or_404(Review, id=review_id)
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get("review_id"))
        serializer.save(author=self.request.user, review=review)
