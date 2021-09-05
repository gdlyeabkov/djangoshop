from django.contrib import admin
from .models import MyUser
from .models import MyOrder
from .models import MyProduct

# Register your models here.
admin.site.register(MyUser)
admin.site.register(MyOrder)
admin.site.register(MyProduct)
