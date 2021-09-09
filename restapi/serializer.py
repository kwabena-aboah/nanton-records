from rest_framework import serializers
from .models import Received, Dispatched

class ReceivedSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Received
        fields = ['id', 'user', 'registry_number', 'to_whom_received', 'date_of_letter', 
            'reference_number', 'subject', 'remarks', 
            'file_directory', 'date_recieved'
        ]


class DispatchedSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Dispatched
        fields = ['id', 'user', 'registry_number', 'to_whom_sent', 'date_of_letter', 
            'reference_number', 'subject', 'remarks', 
            'file_directory', 'date_dispatched'
        ]