from rest_framework import serializers
from .models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    creador = serializers.PrimaryKeyRelatedField(source="creador.id", read_only=True, allow_null=True)

    class Meta:
        model = Tasks
        fields = "__all__"
        extra_fields = [ "creador" ]
