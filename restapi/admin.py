import string
import random
from django.contrib import admin
from . models import Received, Dispatched


admin.site.site_header = "NANTON DISTRICT ASSEMBLY"
admin.site.site_title = "NANTON DISTRICT ASSEMBLY"
admin.site.index_title = "Site Administration"
admin.site.site_url = "/"

@admin.register(Received)
class ReceivedAdmin(admin.ModelAdmin):
    fields = (
        'registry_number', 'to_whom_received', 'date_of_letter', 
        'reference_number', 'subject', 'remarks', 
        'file_directory', 'date_recieved'
        )
    list_display = (
        'id', 'registry_number', 'date_recieved', 'to_whom_received',
        'date_of_letter', 'reference_number', 'subject',
        'remarks', 'file_directory', 'user'
    )
    list_filter = ('registry_number', 'date_recieved',)
    list_editable = (
        'date_recieved', 'to_whom_received', 
        'date_of_letter', 'reference_number', 
        'subject', 'remarks', 'file_directory',
        )
    search_fields = ('registry_number', 'reference_number',)
    date_hierarchy = "date_of_letter"
    save_on_top = True
    list_per_page = 10
    
    def save_model(self, request, obj, form, change):
        # strings = 4
        # randoms = ''.join(random.choices(string.ascii_uppercase + string.digits, k = strings))
        '''Automatically generate registry number'''
        if getattr(obj, 'id', True) is not None:
            self.user = request.user
            # self.registry_number = '{randoms}{user:04d}'.format(
            #     user=Received.objects.count(), randoms=str(randoms))
            obj.save()
        super().save_model(request, obj, form, change)


@admin.register(Dispatched)
class DispatchedAdmin(admin.ModelAdmin):
    fields = (
        'registry_number', 'to_whom_sent', 'date_of_letter', 
        'reference_number', 'subject', 'remarks', 
        'file_directory', 'date_dispatched'
        )
    list_display = (
        'id', 'registry_number', 'date_dispatched', 'to_whom_sent',
        'date_of_letter', 'reference_number', 'subject',
        'remarks', 'file_directory', 'user'
    )
    list_filter = ('registry_number', 'date_dispatched',)
    list_editable = (
        'date_dispatched', 'to_whom_sent', 
        'date_of_letter', 'reference_number', 
        'subject', 'remarks', 'file_directory',
        )
    search_fields = ('registry_number', 'reference_number',)
    date_hierarchy = "date_of_letter"
    save_on_top = True
    list_per_page = 10
    
    def save_model(self, request, obj, form, change):
        # strings = 4
        # randoms = ''.join(random.choices(string.ascii_uppercase + string.digits, k = strings))
        '''Automatically generate registry number'''
        if getattr(obj, 'id', True) is not None:
            self.user = request.user
            # self.registry_number = '{randoms}{user:04d}'.format(
            #     user=Dispatched.objects.count(), randoms=str(randoms))
            obj.save()
        super().save_model(request, obj, form, change)