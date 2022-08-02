
# class UserFavoriteQuestionListView(generics.ListAPIView):

#     serializer_class = AnswerSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Question.objects.filter(user_id=self.kwargs["pk"])

#     def perform_create(self, serializer):
#         user = get_object_or_404(User, pk=self.kwargs.get("pk"))
#         serializer.save(user=user)