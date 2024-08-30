from rest_framework import serializers
from api.models import *
from .models import *

#Event Serializer
class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__' 
        
        
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'
        read_only_fields = ['reference']

    def create(self, validated_data):
        validated_data['reference'] = self.generate_reference()
        return super().create(validated_data)

    def generate_reference(self):
        import uuid
        return str(uuid.uuid4())
