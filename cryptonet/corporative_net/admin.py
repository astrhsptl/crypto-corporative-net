from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Posts, Orders, Workers, Clients

class PostsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Posts
        fields = '__all__'

class OrdersAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Orders
        fields = '__all__'

class WorkersAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Workers
        fields = '__all__'

class ClientsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Clients
        fields = '__all__'

class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    list_filter = ('id',)
    fields = ('id', 'title', 'discription', )
    readonly_fields = ('id',)

class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'discription', 'executor_id', 'client_id', 'client_sum', 'status', 'create_date')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title', 'client_id')
    list_filter = ('id',)
    fields = (
        'id', 'title', 'discription', 'executor_id', 'client_id', 'client_sum', 'status', 'create_date')
    readonly_fields = ('id', 'create_date',)

class WorkersAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'post_id', 'name', 'lastname', 'phone', )
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'title',)
    list_filter = ('id',)
    fields = (
        'id', 'post_id', 'name', 'lastname', 'phone', )
    readonly_fields = ('id',)


class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lastname', 'phone', 'email',)
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name', )
    list_filter = ('id', )
    fields = (
        'id', 'name', 'lastname', 'phone', 'email', )
    readonly_fields = ('id',) 

admin.site.register(Posts, PostsAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Workers, WorkersAdmin)
admin.site.register(Clients, ClientsAdmin)
