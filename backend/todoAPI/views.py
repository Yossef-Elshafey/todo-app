from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from todoAPI.models import Todo
from todoAPI.serializers import TodoSerializer


class TodoView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer

    def get_queryset(self):
        if self.request.method == "GET":
            qs = Todo.objects.all()
            user = self.request.user
            prio = self.request.query_params.get("priority")
            if prio:
                # values (0,1) capitalize (true,false)
                return qs.filter(user=user, priority=prio.capitalize())
            return qs.filter(user=user)


class SingleTodoView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)
