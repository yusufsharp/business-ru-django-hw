from rest_framework import serializers
from datetime import datetime
from .models import User


class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    name_surname = serializers.CharField(max_length=40)
    gender = serializers.CharField()
    birth_date = serializers.DateField()
    telegram = serializers.CharField(max_length=40)
    phone_number = serializers.CharField(max_length=20)
    about = serializers.CharField()

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        item = User.objects.create(image=validated_data.get('image', ''),
                                   name_surname=validated_data.get('name_surname', None),
                                   gender=validated_data.get('gender', None),
                                   birth_date=validated_data.get('birth_date', 0),
                                   telegram=validated_data.get('telegram', datetime.now()),
                                   phone_number=validated_data.get('phone_number', datetime.now()),
                                   about=validated_data.get('about', None)
                                   )
        item.save()
        return item
