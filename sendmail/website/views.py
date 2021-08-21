from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# # Create your views here.
#
#
# def home(request):
#     return HttpResponseRedirect(reverse('website:home'))


def home(request):
    return render(request, 'home.html', {})

# def contact(request):
#     if request.method == 'POST':
#         messageName = request.POST['messsageName']
#         messageEmail = request.POST['messsageEmail']
#         message = request.POST['messsage']
#         send_mail(
#             messageName,
#             message,
#             messageEmail,
#             ['a@a.a'] #receptionist(s)
#         )
#     return render(request, 'contact.html', {'messageName':messageName})
#
#
# def send_mail(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         subject = request.POST.get('subject')
#         text = request.POST.get('text')
#         print(name, subject, text)
#         return HttpResponseRedirect(reverse('home'))
#     else:
#         return HttpResponse('invalid request')


def send_gmail(request):
    # print('here')
    if request.method == "POST":
        # print('saggggggggggggggggggggggggggggggggggg')
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # name = request.POST.post('name')
        # subject = request.POST.post('subject')
        # message = request.POST.post('message')
        print(name, subject, message)

        send_mail(
            subject,
            message,
            'sad.splitwise@gmail.com',
            ['dahlia.davoudi17@gmail.com'],
            fail_silently=False,
        )

        return HttpResponseRedirect(reverse('website:home'))
    else:
        return HttpResponse('Invalid request')
