from django.contrib import admin
from django import forms

# Register your models here.
from django.utils.safestring import mark_safe

from .models import Service,Work,AboutMe,Intro,Language,Skill,Experience,Interests,Cvdata,PrivateSettings,Education

class AboutMeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('myname',)
                           }
    list_display = ('id','myname','slug','aboutmetitle','description','meta_desc','meta_keys','my_photo','page_lang',)
    list_display_links = ('id', 'myname','page_lang',)
    search_fields = ('page_lang','myname',)
    readonly_fields = ('get_photo',)
    fields = ('page_lang','myname','slug','aboutmetitle','description','meta_desc','meta_keys','my_photo',)
    save_as = True
    def get_photo(self, obj):
        if obj.my_photo:
            return mark_safe(f'<img src="{obj.my_photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'photo'


class IntroAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('intro_name',)
                           }
    list_display = ('page_lang','id','intro_name','slug','intro', 'presentation', 'my_photo', 'github_link','insta_link','linked_in_link','meta_desc','meta_keys',)
    list_display_links = ('id', 'intro_name','page_lang',)
    search_fields = ('page_lang','intro_name',)
    readonly_fields = ('get_photo',)
    fields = ('page_lang','intro_name','slug','intro', 'presentation', 'my_photo','github_link','insta_link','linked_in_link','meta_desc','meta_keys',)
    save_as = True

    def get_photo(self, obj):
        if obj.my_photo:
            return mark_safe(f'<img src="{obj.my_photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'photo'


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)
                           }
    list_display = ('id','ordering_rate','title','slug','description','meta_desc','meta_keys','photo','is_published','page_lang',)
    list_display_links = ('id', 'title','page_lang',)
    search_fields = ('page_lang','title',)
    readonly_fields = ('get_photo',)
    fields = ('page_lang','ordering_rate','title','slug','description','meta_desc','meta_keys','photo','is_published',)
    save_as = True
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'img'

class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('work_title',)
                           }
    list_display = ('id','ordering_rate','work_title','work_link','slug','work_description','meta_desc','meta_keys','work_photo','is_published','page_lang',)

    list_display_links = ('id', 'work_title','page_lang',)
    search_fields = ('page_lang','work_title','page_lang','work_link',)
    readonly_fields = ('get_photo',)
    fields = ('page_lang','ordering_rate','work_title','work_link','slug','work_description','meta_desc','meta_keys','work_photo','is_published',)

    save_as = True

    def get_photo(self, obj):
        if obj.work_photo:
            return mark_safe(f'<img src="{obj.work_photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'img'

class LanguageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('lang',)
                           }
    list_display = ('id','lang' ,'slug','lang_percent','page_lang',)
    list_display_links = ('id', 'lang','page_lang',)
    search_fields = ('page_lang','lang','page_lang',)
    fields = ('page_lang','lang' ,'slug','lang_percent',)

    save_as = True

class SkillAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('skill',)
                           }
    list_display = ('id','skill' ,'slug','skill_percent','page_lang',)
    list_display_links = ('id', 'skill','page_lang',)
    search_fields = ('page_lang','skill',)
    fields = ('page_lang','skill' ,'slug','skill_percent',)

    save_as = True

class InterestsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('interest',)
                           }
    list_display = ('id','interest' ,'slug','icon','page_lang',)
    list_display_links = ('id', 'interest','page_lang',)
    search_fields = ('page_lang','interest','page_lang',)
    fields = ('page_lang','interest' ,'slug','icon',)

    save_as = True



class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
    'page_lang', 'years', 'company', 'position', 'description', 'slug', 'meta_desc', 'meta_keys', 'is_published',)
    fields = ('page_lang','years','company','position','description','slug','meta_desc','meta_keys','is_published',)
    save_as = True

class EducationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('years',)
                           }
    fields = ('page_lang','years','degree','establishment','description','slug','meta_desc','meta_keys','is_published',)
    list_display = (
    'page_lang', 'years', 'degree', 'establishment', 'description', 'slug', 'meta_desc', 'meta_keys', 'is_published',)
    save_as = True

class CvdataAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('mycvname',)
                           }
    list_display = ('mycvname','page_lang','slug','cvmail','cvlocation','cvlinkedin','cvwebsite','myprofile','description','meta_desc','meta_keys','my_cv_photo',)
    list_display_links = ('mycvname',)
    search_fields = ('page_lang','mycvname',)
    readonly_fields = ('get_photo',)
    fields = ('page_lang','mycvname','slug','cvmail','cvlocation','cvlinkedin','cvwebsite','myprofile','description','meta_desc','meta_keys','my_cv_photo',)
    save_as = True

    def get_photo(self, obj):
        if obj.my_cv_photo:
            return mark_safe(f'<img src="{obj.my_cv_photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'photo'




class PrivateSettingsAdmin(admin.ModelAdmin):
    fields = ('title','destination_chat','bot_id', 'sms_logging')
    save_as = True



admin.site.register(Service,ServiceAdmin)
admin.site.register(Work,WorkAdmin)
admin.site.register(AboutMe,AboutMeAdmin)
admin.site.register(Intro,IntroAdmin)
admin.site.register(Language,LanguageAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(Interests,InterestsAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(Cvdata,CvdataAdmin)
admin.site.register(PrivateSettings,PrivateSettingsAdmin)