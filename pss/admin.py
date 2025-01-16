from django.contrib import admin
from .models import PSSTest, QustionsTest, PSSResult

# Register your models here.
admin.site.register(PSSTest)
admin.site.register(QustionsTest)
admin.site.register(PSSResult)
