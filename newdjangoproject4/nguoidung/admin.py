from django.contrib import admin

from nguoidung.models import RoomChat, thongtinnguoidung
# Register your models here.
@admin.register(RoomChat)
class RoomChatadmin(admin.ModelAdmin):
    list_display = ('RoomID',)
    
@admin.register(thongtinnguoidung)  
class thongtinnguoidungAdmin(admin.ModelAdmin):
    list_display = ('name', 'tennguoidung', 'nation', 'dateofbirth', 'email', 'gender', )
    search_fields = ('name', 'email',)
    list_filter = ('nation',)
