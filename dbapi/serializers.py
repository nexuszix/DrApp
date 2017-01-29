# coding=utf8

from rest_framework import serializers
from dbapi.models import DrMas

class DrMasSerializer(serializers.ModelSerializer):

	class Meta:
		model = DrMas
		fields = ('drCode', 'clinic', 'prefix', 'firstname', 'lastname', 'specialty', 
			'locate', 'profile', 'schedule', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'editor',)


# class DrMasSerializer(serializers.Serializer):
	# id = serializers.IntegerField(read_only=True)
	# drCode = serializers.CharField(max_length=20)
	# clinic = serializers.CharField(max_length=100, required=False, allow_blank=True)
	# prefix = serializers.CharField(max_length=10, required=False, allow_blank=True)
	# firstname = serializers.CharField(max_length=50)
	# lastname = serializers.CharField(max_length=50)
	# specialty = serializers.CharField(max_length=50, required=False, allow_blank=True)
	# locate = serializers.CharField(max_length=10, required=False, allow_blank=True)
	# profile = serializers.CharField(required=False, allow_blank=True)
	# schedule = serializers.CharField(required=False, allow_blank=True)
	# mon = serializers.BooleanField(default=False)
	# tue = serializers.BooleanField(default=False)
	# wed = serializers.BooleanField(default=False)
	# thu = serializers.BooleanField(default=False)
	# fri = serializers.BooleanField(default=False)
	# sat = serializers.BooleanField(default=False)
	# sun = serializers.BooleanField(default=False)
	# lastedit = serializers.DateField()
	# editor = serializers.CharField(required=False, allow_blank=True)

	# def create(self, validated_data):
	# 	"""
	# 	Create and return a new `Snippet` instance, given the validated data.
	# 	"""
	# 	return DrMas.objects.create(**validated_data)

	# def update(self, instance, validated_data):
	# 	"""
	# 	Update and return an existing `Snippet` instance, given the validated data.
	# 	"""
	# 	instance.drCode = validated_data.get('drCode', instance.drCode)
	# 	instance.clinic = validated_data.get('clinic', instance.clinic)
	# 	instance.prefix = validated_data.get('prefix', instance.prefix)
	# 	instance.firstname = validated_data.get('firstname', instance.firstname)
	# 	instance.lastname = validated_data.get('lastname', instance.lastname)
	# 	instance.specialty = validated_data.get('specialty', instance.specialty)
	# 	instance.locate = validated_data.get('locate', instance.locate)
	# 	instance.profile = validated_data.get('profile', instance.profile)
	# 	instance.schedule = validated_data.get('schedule', instance.schedule)
	# 	instance.mon = validated_data.get('mon', instance.mon)
	# 	instance.tue = validated_data.get('tue', instance.tue)
	# 	instance.wed = validated_data.get('wed', instance.wed)
	# 	instance.thu = validated_data.get('thu', instance.thu)
	# 	instance.fri = validated_data.get('fri', instance.fri)
	# 	instance.sat = validated_data.get('sat', instance.sat)
	# 	instance.sun = validated_data.get('sun', instance.sun)
	# 	instance.save()
	# 	return instance