from rest_framework import serializers
from .models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    creador = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Tasks
        fields = "__all__"
