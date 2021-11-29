from django.shortcuts import render
from .models import Service,Work,AboutMe,Intro,Language,Skill,Experience,Interests,PrivateSettings
from django.http import HttpResponse
from .forms import EmailForm
from django.core.mail import send_mail, EmailMessage
#def index(request):
#    return HttpResponse('HelloWorld')

def index(request):
    email_form=EmailForm()
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

    if request.method == 'POST':
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            first_name=email_form.cleaned_data['first_name']
            last_name = email_form.cleaned_data['last_name']
            mobile_number = email_form.cleaned_data['mobile_number']
            contact_mail = email_form.cleaned_data['mail']
            contact_message = email_form.cleaned_data['message_text']
            mail = send_mail(
                subject=f'PORTFOLIO CONTACT FORM:{first_name} {last_name}:{contact_mail},{mobile_number}.',
                message=f"Message {contact_message}",
                from_email='inventoryappli@gmail.com',
                recipient_list=['evgeny.rfi@gmail.com','support@algorito.fr' ], fail_silently=True, )

            ####EMAIL####

            if mail:
                context={"email_status": 'Email, successfully sent to our team, we will contact you shortly!'}

            else:
                context={"email_status": 'Failed to send email, please contact us on support@usachev.fr'}

            return render(request, 'portfolio_landing/email_status.html',
                          context=context)

            #return HttpResponse('<h1>Welcome to algorito.fr</h1><br><h2>appli has moved to <a href="appli.algorito.fr"> appli.algorito.fr</a></h2>')
        else:
            email_form = EmailForm()
    #return render(request, 'landing/home_glass.html', context)


    context = {"intro":intro,
               "aboutme":aboutme,
               "services":services,
               "works":works,
               "email_form":email_form
               }


    return render(request, 'portfolio_landing/index.html', context=context)

def cv_page(request):

    return render(request, 'portfolio_landing/CV.html', context={})