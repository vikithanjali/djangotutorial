from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta():
        model=Employee
        #fields=('firstnam','lastname')
        fields='__all__'

