from blog.models import Category, Blog
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core import exceptions
import django.contrib.auth.password_validation as validators

User = get_user_model()


class UserTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class CategoryTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class BlogTopUserSerilizer(serializers.ModelSerializer):
    category = CategoryTopSerializer(many=False, read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'post', 'category')


class UserSerializers(serializers.ModelSerializer):
    blogs = BlogTopUserSerilizer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'blogs')


class RegistrationUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        # here data has all the fields which have validated values
        # so we can create a User instance out of it
        user = User(**data)

        # get the password from the data
        password = data.get('password')

        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password, user=User)

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(RegistrationUserSerializers, self).validate(data)

    def create(self, validated_data):
        password = validated_data.pop('password', None)

        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
