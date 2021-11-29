from django.shortcuts import render
from .models import Service,Work,AboutMe,Intro,Language,Skill,Experience,Interests,PrivateSettings
from django.http import HttpResponse

#def index(request):
#    return HttpResponse('HelloWorld')

def index(request):
    try:
        intro=Intro.objects.all()
        aboutme=AboutMe.objects.all()
        services=Service.objects.all().filter(is_published=True).order_by('ordering')
        works=Work.objects.all().filter(is_published=True).order_by('ordering')

    except:
        intro=[Intro(intro_name="empty"),]
        aboutme=[AboutMe(myname="empty"),]
        services=[Service(title="empty"),]
        works=[Work(work_title="empty"),]

    context = {"intro":intro,
               "aboutme":aboutme,
               "services":services,
               "works":works,
               }


    return render(request, 'portfolio_landing/index.html', context=context)

def cv_page(request):

    return render(request, 'portfolio_landing/CV.html', context={})