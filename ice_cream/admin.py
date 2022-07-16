from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import IceCream, Category


class IceCreamAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'description',
                    'category',
                    'created_at',
                    'get_photo',
                    'price',
                    'views',
                    )
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_filter = ('category', )
    fields = ('name',
              'category',
              'description',
              'photo',
              'get_photo',
              'views',
              'price',
              'created_at',
              )
    readonly_fields = ('get_photo', 'created_at', 'views')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return 'Фото нет'

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ("name",)}


admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.site_title = 'Управление морожеными'
admin.site.site_header = 'Управление морожеными'
