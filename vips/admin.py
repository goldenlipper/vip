from django.contrib import admin

from .models import Vip1, Vip2, Vip3, Vip4, Selling, VipGroup, GlUser

admin.site.register(GlUser)
admin.site.register(Vip1)
admin.site.register(Vip2)
admin.site.register(Vip3)
admin.site.register(Vip4)
admin.site.register(Selling)
admin.site.register(VipGroup)

