from django.contrib import admin
from django import forms

# Register your models here.
from django.utils.safestring import mark_safe

from .models import Service,Work,AboutMe,Intro,Language,Skill,Experience,Interests,PrivateSettings

class AboutMeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('myname',)
                           }
    list_display = ('id','myname','slug','aboutmetitle','description','meta_desc','meta_keys','my_photo',)
    list_display_links = ('id', 'myname')
    search_fields = ('myname',)
    readonly_fields = ('get_photo',)
    fields = ('myname','slug','aboutmetitle','description','meta_desc','meta_keys','my_photo',)

    def get_photo(self, obj):
        if obj.my_photo:
            return mark_safe(f'<img src="{obj.my_photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'photo'


class IntroAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('intro_name',)
                           }
    list_display = ('id','intro_name','slug','intro', 'presentation', 'my_photo', 'github_link','insta_link','linked_in_link','meta_desc','meta_keys',)
    list_display_links = ('id', 'intro_name')
    search_fields = ('intro_name',)
    readonly_fields = ('get_photo',)
    fields = ('intro_name','slug','intro', 'presentation', 'my_photo','github_link','insta_link','linked_in_link','meta_desc','meta_keys',)

    def get_photo(self, obj):
        if obj.my_photo:
            return mark_safe(f'<img src="{obj.my_photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'photo'


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)
                           }
    list_display = ('id','ordering','title','slug','description','meta_desc','meta_keys','photo','is_published',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    readonly_fields = ('get_photo',)
    fields = ('ordering','title','slug','description','meta_desc','meta_keys','photo','is_published',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'img'


class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('work_title',)
                           }
    list_display = ('id','ordering','work_title','slug','work_description','meta_desc','meta_keys','work_photo','is_published',)

    list_display_links = ('id', 'work_title')
    search_fields = ('work_title',)
    readonly_fields = ('get_photo',)
    fields = ('ordering','work_title','slug','work_description','meta_desc','meta_keys','work_photo','is_published',)

    def get_photo(self, obj):
        if obj.work_photo:
            return mark_safe(f'<img src="{obj.work_photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'img'

class LanguageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('lang',)
                           }
    list_display = ('id','lang' ,'slug','lang_percent',)
    list_display_links = ('id', 'lang')
    search_fields = ('lang',)
    fields = ('lang' ,'slug','lang_percent',)

class SkillAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('skill',)
                           }
    list_display = ('id','skill' ,'slug','skill_percent',)
    list_display_links = ('id', 'skill')
    search_fields = ('skill',)
    fields = ('skill' ,'slug','skill_percent',)

class InterestsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('interest',)
                           }
    list_display = ('id','interest' ,'slug','icon',)
    list_display_links = ('id', 'interest')
    search_fields = ('interest',)
    fields = ('interest' ,'slug','icon',)


class ExperienceAdmin(admin.ModelAdmin):
    fields = ('years','company','description','slug','meta_desc','meta_keys','is_published',)

class PrivateSettingsAdmin(admin.ModelAdmin):
    fields = ('id','title','destination_chat','bot_id')




admin.site.register(Service,ServiceAdmin)
admin.site.register(Work,WorkAdmin)
admin.site.register(AboutMe,AboutMeAdmin)
admin.site.register(Intro,IntroAdmin)
admin.site.register(Language,LanguageAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(Interests,InterestsAdmin)
admin.site.register(PrivateSettings,PrivateSettingsAdmin)