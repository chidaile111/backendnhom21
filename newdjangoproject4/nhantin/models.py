from django.db import models
from nguoidung.models import RoomChat
# Create your models here.

class tinnhan(models.Model):
    room = models.ForeignKey(RoomChat)
    user = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now=True, db_index=True)
    text = models.TextField()
 
    def to_data(self):
        out = {}
        out['id'] = self.id
        out['from'] = self.user
        out['date'] = self.date.isoformat()
        out['text'] = self.text
        return out