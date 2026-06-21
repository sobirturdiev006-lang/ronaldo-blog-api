from django.contrib import admin
from .models import About, Resume, Malaka, Tajriba, M_tajriba, Sovrinlar, Service, Projects, Blog, Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'is_published']
    list_filter = ['is_published', 'created_date']
    search_fields = ['title', 'email']

admin.site.register(About)
admin.site.register(Resume)
admin.site.register(Service)
admin.site.register(Projects)
admin.site.register(Blog)
admin.site.register(Malaka)
admin.site.register(Tajriba)
admin.site.register(M_tajriba)
admin.site.register(Sovrinlar)
# admin.site.register(Contact)