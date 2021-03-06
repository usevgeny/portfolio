from django.shortcuts import render, redirect
from .models import Service, Work, AboutMe, Intro, Language, Skill, Experience, Interests, PrivateSettings, Cvdata, \
    Education, Certificate
from django.http import HttpResponse
from .forms import EmailForm, SendChatForm
from django.core.mail import send_mail, EmailMessage
import asyncio
from datetime import datetime
from .bot_portfolio import send
from ip2geotools.databases.noncommercial import DbIpCity
from decouple import config
#def index(request):
#    return HttpResponse('HelloWorld')


available_languages=('ENG','RUS','FR','IT')
def detect_lang(request):
    if '/lang/' in request.__dict__['path_info']:
        selected_language_group = request.__dict__['path_info']
        list_values=selected_language_group.split('/')
        instruction_index=list_values.index('lang')
        value_index=instruction_index+1
        language_value=str(list_values[value_index]).upper()
        print('hello from detect_lang:', language_value)
        return language_value

def get_ip_geoloc(ip):
    try:
        location = f"{DbIpCity.get(ip, api_key='free').country}, {DbIpCity.get(ip, api_key='free').city}"
    except:
        location = 'Failed to detect GEO IP'

    return location
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
        location=get_ip_geoloc(ip)
    else:
        ip = request.META.get('REMOTE_ADDR')
        location=get_ip_geoloc(ip)


    return ip,location


def log_ip_sms(request,page):
    try:
        clients_ip = get_client_ip(request)
    except Exception as e:
        clients_ip = 'failed to detect'
    log_message=f'{datetime.now().isoformat(timespec="seconds")}: visit from {clients_ip}, page: {page}'
    print(log_message)
    try:
        active_profile = PrivateSettings.objects.get(pk=1)
        destination = str(active_profile.destination_chat)
        bot_id = str(active_profile.bot_id)
        send(msg=log_message, chat_id=destination, token=bot_id)

    except Exception as e:
        print(e)

def send_sms_func(request):
    req_index_post = dict(request.POST.items())
    smsform = SendChatForm(request.POST)
    if smsform.is_valid():
        print('form is valid')
        senders_name = str(smsform.cleaned_data['name'])
        senders_phone = str(smsform.cleaned_data['telephone'])
        sms_text = smsform.cleaned_data['message']

        message = f'Name:  {senders_name} \n PhoneNumber: {senders_phone} \n Message: {sms_text} \n'
        active_profile = PrivateSettings.objects.get(pk=1)
        destination = str(active_profile.destination_chat)
        bot_id = str(active_profile.bot_id)

        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            send(msg=message, chat_id=destination, token=bot_id)
            log_ip_sms(request,'index')

            return redirect('/')
        except Exception as e:
            print(e)
            print(req_index_post)
            log_ip_sms(request, 'index')
            return redirect('/')

    else:
        print('form is not  valid', smsform.errors)
        log_ip_sms(request, 'index')
        smsform = SendChatForm()




def index(request, template_to_be_rendered='portfolio_landing/ENG/index.html'):
    used_host=request.__dict__['META']['HTTP_HOST']
    if 'mobile' in used_host:
        template_to_be_rendered = f"{'/'.join(template_to_be_rendered.split('/')[:-1])}/index_mobile.html"

    email_form=EmailForm()
    smsform = SendChatForm()
    sms_errors=""
    try:
        detected_lang=detect_lang(request)
        if detected_lang in available_languages:
            page_language=detected_lang
        else:
            page_language = 'ENG'
    except Exception as e:
        page_language = 'ENG'
    try:
        active_profile = PrivateSettings.objects.get(pk=1)
    except Exception as e:
        active_profile = PrivateSettings(title='not_set',destination_chat='',bot_id='',sms_logging=False)
    if active_profile.bot_id and active_profile.destination_chat:
        telegram_status=True
    else:
        telegram_status=False
    try:
        intro=Intro.objects.all().filter(page_lang=page_language)
        aboutme=AboutMe.objects.all().filter(page_lang=page_language)
        services=Service.objects.all().filter(page_lang=page_language).filter(is_published=True).order_by('ordering_rate')
        works=Work.objects.all().filter(page_lang=page_language).filter(is_published=True).order_by('ordering_rate')

    except Exception as e:
        intro=[Intro(intro_name="empty"),]
        aboutme=[AboutMe(myname="empty"),]
        services=[Service(title="empty"),]
        works=[Work(work_title="empty"),]
        print(e)

    if request.method == 'POST':
        req_index_post = dict(request.POST.items())

        try:
            detected_lang = detect_lang(request)
            if detected_lang in available_languages:
                page_language = detected_lang
            else:
                page_language = 'ENG'
        except Exception as e:
            page_language = 'ENG'

        if 'send_mail' in req_index_post:
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
                    from_email=config('EMAIL_HOST_USER'),
                    recipient_list=[config('RECIPIENT'), ], fail_silently=True, )

                ####EMAIL####

                if mail:
                    #context={"email_status": 'Email, successfully sent to our team, we will contact you shortly!'}
                    context = {"email_status": 'success'}

                else:
                    context = {"email_status": 'fail'}
                    #context={"email_status": 'Failed to send email, please contact us on support@usachev.fr'}
                print(f'portfolio_landing/{page_language}/email_status.html')
                return render(request, f'portfolio_landing/{page_language}/email_status.html',
                              context=context)

                #return HttpResponse('<h1>Welcome to algorito.fr</h1><br><h2>appli has moved to <a href="appli.algorito.fr"> appli.algorito.fr</a></h2>')
            else:
                email_form = EmailForm()
                smsform = SendChatForm()
        elif 'send_telegram' in req_index_post:
            smsform = SendChatForm(request.POST)
            if smsform.is_valid():
                print('sms form is valid')
                senders_name = str(smsform.cleaned_data['name'])
                senders_phone = str(smsform.cleaned_data['telephone'])
                sms_text = smsform.cleaned_data['message']

                message = f'Name:  {senders_name} \n Phone: {senders_phone} \n Message: {sms_text} \n'
                destination = str(active_profile.destination_chat)
                bot_id = str(active_profile.bot_id)

                try:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    send(msg=message, chat_id=destination, token=bot_id)
                    log_ip_sms(request, 'index')

                    return redirect('/')
                except Exception as e:
                    print("ERROR OCCURED",e)
                    print("REQUEST DICTIONNARY",req_index_post)
                    log_ip_sms(request, 'index')
                    return redirect('/')


            else:
                print("SMS FORM IS NOT VALID")
                sms_errors = smsform.errors
                print("SMS ERRORS", sms_errors)

                email_form = EmailForm()
                smsform = SendChatForm()

    #return render(request, 'landing/home_glass.html', context)

    certificates=False
    if Certificate.objects.all():
        certificates=True

    context = {"intro":intro,
               "aboutme":aboutme,
               "services":services,
               "works":works,
               "email_form":email_form,
               "smsform":smsform,
               "sms_errors":sms_errors,
               "telegram_status":telegram_status,
               "certificates":certificates,
               }
    sms_logging = active_profile.sms_logging
    if sms_logging:
        log_ip_sms(request, 'index')

    return render(request, template_to_be_rendered, context=context)

def index_fr(request):
    return index(request, template_to_be_rendered='portfolio_landing/FR/index.html')

def index_rus(request):
    return index(request, template_to_be_rendered='portfolio_landing/RUS/index.html')


def certificates(request, template_to_be_rendered='portfolio_landing/ENG/certificates.html'):

    try:
        detected_lang = detect_lang(request)
        if detected_lang in available_languages:
            page_language = detected_lang
        else:
            page_language = 'ENG'

    except Exception as e:
        print('LANG_DETECTION_EXCEPTION_OCCURED')
        page_language = 'ENG'

    try:
        certificates=Certificate.objects.all().filter(page_lang=page_language).order_by('-pk')
    except Exception as e:
        certificates=[Certificate(page_lang="empty",
                                certificate_name="empty",
                                description="empty",
                                certificate_link="empty",
                                work_photo="empty",
                                )]

    context={
        'certificates':certificates,
    }
    return render(request, template_to_be_rendered, context=context)


def cv_page(request, template_to_be_rendered='portfolio_landing/ENG/CV.html'):
    used_host = request.__dict__['META']['HTTP_HOST']
    if 'mobile' in used_host:
        template_to_be_rendered = f"{'/'.join(template_to_be_rendered.split('/')[:-1])}/CV_mobile.html"

    try:
        detected_lang = detect_lang(request)
        if detected_lang in available_languages:
            page_language = detected_lang
        else:
            page_language = 'ENG'

    except Exception as e:
        print('LANG_DETECTION_EXCEPTION_OCCURED')
        page_language = 'ENG'

    try:
        selected_cv = Cvdata.objects.all().filter(page_lang=page_language)
    except Exception as e:
        selected_cv = [
            Cvdata(mycvname='empty', slug='empty', cvmail='empty', cvlocation='empty', cvlinkedin='#', cvwebsite='#',
                   myprofile='empty', description='empty', )]
        print(e)
    try:
        language_set = Language.objects.all().filter(page_lang=page_language).order_by('-lang_percent')
    except Exception as e:
        language_set = []

    try:
        skill_set = Skill.objects.all().filter(page_lang=page_language).order_by('-skill_percent')
    except Exception as e:
        skill_set = []
    try:
        experience_set = Experience.objects.all().filter(page_lang=page_language).filter(is_published=True).order_by('ordering_rate')
    except Exception as e:
        experience_set = []
    try:
        interest_set = Interests.objects.all().filter(page_lang=page_language)
    except Exception as e:
        interest_set = []
    try:
        education_set = Education.objects.all().filter(page_lang=page_language).filter(is_published=True).order_by('-years')
    except Exception as e:
        education_set = []


    context={
        'selected_cv':selected_cv,
        'language_set':language_set,
        'skill_set':skill_set,
        'experience_set':experience_set,
        'interest_set':interest_set,
        'education_set':education_set,
            }

    return render(request, template_to_be_rendered, context=context)


def cv_page_fr(request):
    return cv_page(request,template_to_be_rendered='portfolio_landing/FR/CV.html')

def cv_page_rus(request):
    return cv_page(request,template_to_be_rendered='portfolio_landing/RUS/CV.html')