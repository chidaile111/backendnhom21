from django import forms
import django
from django.db.models import fields
from django.forms.widgets import PasswordInput
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from nguoidung.models import thongtinnguoidung
#
class DangKy(forms.Form):
    username = forms.CharField( widget=forms.TextInput(attrs={'style': 'border: none'}))
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label='Nhập Mật Khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập Lại Mật Khẩu', widget=forms.PasswordInput())
    
    def clean_password2(self):
        if 'password1'in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1==password2 and password1:
                return password2
        raise forms.ValidationError("Mật Khẩu không hợp lệ")
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên Tài Khoản không hợp lệ")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tên Tài Khoản đã tồn tại")
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError("Email đã tồn tại")
    
    def transform_email(self):
        email = self.cleaned_data['email']
        thongtinnguoidung.email = email
        
    def save(self):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )
        
class TaoNguoiDungMoi(forms.ModelForm):
    class Meta:
        model = thongtinnguoidung
        fields = (
            'name',
            # 'nation',
            # 'gender',      
        )