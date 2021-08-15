from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email','username','phone','country','password')

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

        print("serializer========")

    # valdiate the input fields with the given data
    def validate(self,data):
        print(data,"<- - - - - - - - - -data")
        if len(str(data.get("phone"))) != 10:
            raise serializers.ValidationError("Phone # must be 10 characters long.")
        if len(data.get("password")) < 6:
            raise serializers.ValidationError("Enter 6 or more characters in the password field")
        return data
    
    # create is called only when the submitted data passes any validations if any given
    # the data is then called validated_data
    def create(self,validated_data):
        print("////// create function called /////")
        print(validated_data)

        # create user with the validated data
        user = self.Meta.model(email=validated_data['email'],username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user