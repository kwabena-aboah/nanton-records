from rest_framework import serializers
from .models import Received, Dispatched

class ReceivedSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Received
        fields = ['user', 'to_whom_received', 'date_of_letter', 
            'reference_number', 'subject', 'remarks', 
            'file_directory', 'date_recieved'
        ]


class DispatchedSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Dispatched
        fields = ['user', 'to_whom_sent', 'date_of_letter', 
            'reference_number', 'subject', 'remarks', 
            'file_directory', 'date_dispatched'
        ]