from rest_framework import serializers
from .models import TarefaModel

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskSerializer
        fields = '__all__'
        