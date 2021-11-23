from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
import datetime
# from nguoidung.forms import CreateNewUser
from icecream import ic
#from newdjangoproject4.nguoidung.models import thongtinnguoidung
from nguoidung.forms import TaoNguoiDungMoi
from nguoidung.forms import DangKy
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseNotAllowed
from django.db import IntegrityError, reset_queries
from nguoidung.models import RoomChat

# Create your views here.

def homepage_view(request):
    return render(
        request,
        'Meeting Chat/index.html',
        {
            'now': datetime.datetime.now(),
        }
    )
    
def userhomepage_view(request):
    return render(
        request,
        'Homepage/UserHomepage.html',
        {
            'now': datetime.datetime.now(),
        }
    )



def dangky(request):
    if request.method == 'POST':
        form1 = DangKy(request.POST)
        form2 = TaoNguoiDungMoi(request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('/dang_nhap')
    else:
        form1 = DangKy()
        form2 = TaoNguoiDungMoi()
    return render(
        request,
        'dangky1.html',
        {
            'form1': form1,
            'form2': form2
        }   
    )
    
# def home(request, room_id=None):
#     user = request.GET.get('user')
#     if user:
#         if not room_id:
#             return redirect('/default?' + request.GET.urlencode())
 
#         try:
#             room = ChatRoom.objects.get(eid=room_id)
#             cmsgs = ChatMessage.objects.filter(
#                 room=room).order_by('-date')[:50]
#             msgs = []
#             for msg in reversed(cmsgs):
#                 msgs.append(msg.to_data())
#         except ChatRoom.DoesNotExist:
#             msgs = []
 
#         context = {}
#         context['room_id'] = room_id
#         context['messages'] = msgs
#         context['user'] = user
#         return render(request, 'chat/chat.html', context)
#     else:
#         context = {}
#         context['room_id'] = room_id or 'default'
#         return render(request, 'chat/join.html', context)
 
# def messages(request, room_id):
#     if request.method == 'POST':
#         try:
#             room = RoomChat.objects.get(eid=room_id)
#         except RoomChat.DoesNotExist:
#             try:
#                 room = RoomChat(eid=room_id)
#                 room.save()
#             except IntegrityError:
#                 # someone else made the room. no problem
#                 room = RoomChat.objects.get(eid=room_id)
 
#         mfrom = request.POST['from']
#         text = request.POST['text']
#         msg = tinnhan(room=room, user=mfrom, text=text)
#         msg.save()
#         body = json.dumps(msg.to_data())
#         return HttpResponse(body, content_type='application/json')
#     else:
#         return HttpResponseNotAllowed(['POST'])

def phongchat(request):
    return render(request, 'new.html')

# def phongchatchinh(request, room_name):
#     return render(request, 'new1.html', {'room_name': RoomChat.RoomID, 'username': User})