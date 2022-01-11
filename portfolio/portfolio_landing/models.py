
from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
# CV:
# Language
# Skills
# Experience
# Interest
# Contact
# Profile Picture
####################
##### Portfolio #####
# Services (Title, Icon)
# Works (Title, Icon, Description)
# About_me (general description, photo)
# Introduction (General description, photo)
# telepram settings




###########################PORTFOLIO#########################

page_language_choices = (
    ("ENG", "ENG"),
    ("FR", "FR"),
    ("RUS","RUS"),
    ("IT","IT"),)

class Service(models.Model):
    page_lang = models.CharField(max_length=10, choices=page_language_choices, blank=False,
                                 verbose_name='LANGUAGE:', default='ENG')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)
    ordering_rate = models.IntegerField(default=1, verbose_name='ordering', validators=[MinValueValidator(1),
                                                                                           MaxValueValidator(100)])
    description = models.TextField(blank=True)
    meta_desc = models.CharField(max_length=160, blank=True)
    meta_keys = models.CharField(max_length=300, blank=True)
    photo = models.ImageField(upload_to=f'photos/{title}', verbose_name='Img', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Published')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']

    def get_absolute_url(self):
        return reverse('service',kwargs={"slug":self.slug})

class Work(models.Model):
    page_lang = models.CharField(max_length=10, choices=page_language_choices, blank=False,
                                 verbose_name='LANGUAGE:', default='ENG')
    work_title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)
    ordering_rate = models.IntegerField(default=1, verbose_name='ordering', validators=[MinValueValidator(1),
                                                                                   MaxValueValidator(100)])
    work_link = models.TextField(blank=True)
    work_description = models.TextField(blank=True)
    meta_desc = models.CharField(max_length=160, blank=True)
    meta_keys = models.CharField(max_length=300, blank=True)
    work_photo = models.ImageField(upload_to=f'photos/{work_title}', verbose_name='Img', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Published')

    def __str__(self):
        return self.work_title

    class Meta:
        ordering = ['-work_title']

    def get_absolute_url(self):
        return reverse('work',kwargs={"slug":self.slug})

class AboutMe(models.Model):
    page_lang = models.CharField(max_length=10, choices=page_language_choices, blank=False,
                                 verbose_name='LANGUAGE:', default='ENG')
    myname = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    aboutmetitle = models.TextField(blank=True)
    description = models.TextField(blank=True)

    meta_desc = models.CharField(max_length=160, blank=True)
    meta_keys = models.CharField(max_length=300, blank=True)
    my_photo = models.ImageField(upload_to=f'photos/{myname}', verbose_name='Img', blank=True)

    def __str__(self):
        return self.myname

    class Meta:
        ordering = ['-myname']

    def get_absolute_url(self):
        return reverse('aboutme',kwargs={"slug":self.slug})

class Cvdata(models.Model):
    page_lang = models.CharField(max_length=10, choices=page_language_choices, blank=False,
                                 verbose_name='LANGUAGE:', default='ENG')
    mycvname = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)
    cvmail = models.CharField(max_length=100)
    cvlocation = models.CharField(max_length=100)
    cvlinkedin = models.CharField(max_length=100)
    cvwebsite = models.CharField(max_length=300)
    myprofile = models.TextField(blank=True)
    description = models.TextField(blank=True)
    meta_desc = models.CharField(max_length=160, blank=True)
    meta_keys = models.CharField(max_length=300, blank=True)
    my_cv_photo = models.ImageField(upload_to=f'photos/{mycvname}', verbose_name='Img', blank=True)

    def __str__(self):
        return self.mycvname

    class Meta:
        ordering = ['-mycvname']

    def get_absolute_url(self):
        return reverse('cvdata',kwargs={"slug":self.slug})


class Intro(models.Model):
    page_lang = models.CharField(max_length=10, choices=page_language_choices, blank=False,
                                 verbose_name='LANGUAGE:', default='ENG')
    intro_name = models.CharField(max_length=100)
    intro = models.TextField(blank=True)
    presentation = models.TextField(blank=True)

    github_link = models.TextField(blank=True)
    insta_link = models.TextField(blank=True)
    linked_in_link = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    meta_desc = models.CharField(max_length=160, blank=True)
    meta_keys = models.CharField(max_length=300, blank=True)
    my_photo = models.ImageField(upload_to=f'photos/{intro_name}', verbose_name='Img', blank=True)

    def __str__(self):
        return self.intro_name

    class Meta:
        ordering = ['-intro_name']

    def get_absolute_url(self):
        return reverse('intro',kwargs={"slug":self.slug})

###########################CV################################
class Language(models.Model):
    page_lang = models.CharField(max_length=10, choices=page_language_choices, blank=False,
                                 verbose_name='LANGUAGE:', default='ENG')
    lang = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)
    lang_percent = models.IntegerField(default=0,verbose_name='lang_percent', validators=[MinValueValidator(0),
                                       MaxValueValidator(100)])
    def __str__(self):
        return self.lang

    class Meta:
        ordering = ['lang_percent']
    def get_absolute_url(self):
        return reverse('language',kwargs={"slug":self.slug})

class Skill(models.Model):
    page_lang = models.CharField(max_length=10, choices=page_language_choices, blank=False,
                                 verbose_name='LANGUAGE:', default='ENG')
    skill = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)
    skill_percent = models.IntegerField(default=0,verbose_name='lang_percent')
    def __str__(self):
        return self.skill

    class Meta:
        ordering = ['skill_percent']

    def get_absolute_url(self):
        return reverse('skill',kwargs={"slug":self.slug})

class Experience(models.Model):
    page_lang = models.CharField(max_length=10, choices=page_language_choices, blank=False,
                                 verbose_name='LANGUAGE:', default='ENG')
    years = models.CharField(max_length=100)
    ordering_rate = models.IntegerField(default=1, verbose_name='ordering', validators=[MinValueValidator(1),
                                                                                        MaxValueValidator(100)])

    company = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    position = models.CharField(max_length=200)

    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)
    meta_desc = models.CharField(max_length=160, blank=True)
    meta_keys = models.CharField(max_length=300, blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Published')


    def __str__(self):
        return self.years

    class Meta:
        ordering = ['-years']

    def get_absolute_url(self):
        return reverse('experience',kwargs={"slug":self.slug})


class Certificate(models.Model):
    page_lang = models.CharField(max_length=10, choices=page_language_choices, blank=False,
                                 verbose_name='LANGUAGE:', default='ENG')
    certificate_name = models.CharField(max_length=200)
    date_obtained = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    certificate_link = models.TextField(blank=True)
    certificate_photo = models.ImageField(upload_to=f'photos/{certificate_name}', verbose_name='Img', blank=True)

class Education(models.Model):
    page_lang = models.CharField(max_length=10, choices=page_language_choices, blank=False,
                                 verbose_name='LANGUAGE:', default='ENG')
    years = models.CharField(max_length=100, blank=False)
    degree = models.CharField(max_length=200, blank=False)
    establishment = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)
    meta_desc = models.CharField(max_length=160, blank=True)
    meta_keys = models.CharField(max_length=300, blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Published')


    def __str__(self):
        return self.years

    class Meta:
        ordering = ['-years']

    def get_absolute_url(self):
        return reverse('education',kwargs={"slug":self.slug})



class Interests(models.Model):
    page_lang = models.CharField(max_length=10, choices=page_language_choices, blank=False,
                                 verbose_name='LANGUAGE:', default='ENG')
    interest = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)
    icon = models.CharField(max_length=1000)
    def __str__(self):
        return self.interest

    class Meta:
        ordering = ['interest']

    def get_absolute_url(self):
        return reverse('interest',kwargs={"slug":self.slug})

#############

class PrivateSettings(models.Model):
    title = models.CharField(max_length=10)
    destination_chat = models.CharField(max_length=15)
    bot_id = models.CharField(max_length=46)
    sms_logging = models.BooleanField(default=False, verbose_name='Sms logging')

    def __str__(self):
        return self.title