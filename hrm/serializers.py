from rest_framework import serializers
from hrm.models import Users

class UsersSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    employee_id = serializers.CharField(required=False)
    ranking = serializers.FloatField(required=False)
    age = serializers.IntegerField(required=False)
    class Meta:
        model = Users
        #fields = ('name','employee_id')
        fields = '__all__'