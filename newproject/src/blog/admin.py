from django.contrib import admin
from .models import Article, Category

#admin header change

admin.site.site_header ="وبلاگ اموزشی جنگو"

# Register your models here.

admin.site.disable_action('delete_selected')
def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated==1:
        message_bit = "منتشر شد"
    else:
        massage_bit="منتشر شدن"
    modeladmin.message_user(request,"{}مقاله {}".format(rows_updated,message_bit))   
make_published.short_description = "انتشار مقالات انتخاب شده"

def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated==1:
        message_bit = "پیش نویس شد"
    else:
        massage_bit="پیش نویس شدن"
    modeladmin.message_user(request,"{}مقاله {}".format(rows_updated,message_bit))   
make_draft.short_description = "پیشنویس شدن مقالات انتخاب شده"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent','status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    # اگه بخواهیم به طور خودکار براساس تایتل قسمت اسلاگ پر شود
    prepopulated_fields = {'slug': ('title',)}
    # مرتب کردن لیست


# اعمال تنظیمات در ادمین پنل
admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag','slug','author', 'jpublish', 'status', 'category_to_str')
    list_filter = ('publish', 'status','author')
    search_fields = ('title', 'description')
    # اگه بخواهیم به طور خودکار براساس تایتل قسمت اسلاگ پر شود
    prepopulated_fields = {'slug': ('title',)}
    # مرتب کردن لیست
    # اگر صعودی باشه طبق زیر ا/ه نزولی بخواهیم قبل پابلیش یه منفی میزاریم
    ordering = ['-status', '-publish']
    actions= [make_published,make_draft]

    def category_to_str(self, obj):
        #return "Categories",
        return "," .join([category.title for category in obj.category.active()])

    category_to_str.short_description = "دسته بندی"


# اعمال تنظیمات در ادمین پنل
admin.site.register(Article, ArticleAdmin)
