from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


def task_form(request):
    return render(request, "task_form.html")


@api_view(["GET", "POST", "PUT", "DELETE"])
def taskApi(request, pk=None):
    if request.method == "GET":
        if pk:
            task = get_object_or_404(Tasks, pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        else:
            tasks = Tasks.objects.all()
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)

    elif request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        if not pk:
            return Response(
                {"error": "ID requerido para actualizar"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        task = get_object_or_404(Tasks, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        if not pk:
            return Response(
                {"error": "ID requerido para eliminar"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        task = get_object_or_404(Tasks, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
