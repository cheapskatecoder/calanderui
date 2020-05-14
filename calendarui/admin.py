from django.contrib import admin
from .models import DqDatafile, DqFeedNew


admin.site.register(DqFeedNew)
admin.site.register(DqDatafile)

