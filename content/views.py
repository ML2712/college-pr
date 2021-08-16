from django.shortcuts import render, reverse

from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib import messages

from django.views.generic import DetailView, ListView
from .models import Blog
# Create your views here.


def home(request):
    context = {
        'new_post': Blog.objects.latest('date_posted')
    }
    return render(request, 'index.html', context)


def blog(request):
    context = {
        'posts': Blog.objects.order_by('-date_posted')
    }
    return render(request, 'blog.html', context)


# def post(request, pk):
#     posts = Blog.objects.get(id=pk)
#     return render(request, 'post.html', {'posts': posts})


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        template = render_to_string('email_template.html',
                                    {
                                        'name': request.POST['name'],
                                        'email': request.POST['email'],
                                        'message': request.POST['message'],
                                    })
        send_content = strip_tags(template)
        email = EmailMultiAlternatives(
            'New Query',  # subject
            send_content,  # message
            settings.OSCAR_FROM_EMAIL,  # from
            ['lakhanpal.manav@icloud.com', 'bhavanajoshi0804@gmail.com']  # to
            # [request.POST['email']]
        )
        email.attach_alternative(template, "text/html")
        email.fail_silently = False
        email.send()
        messages.success(
            request, "We appreciate that you've taken the time to write us. We'll revert for your query.")

    return render(request, 'index.html')


def subscribe(request):
    if request.method == 'POST':
        html_content = render_to_string('newsletter.html',
                                        {
                                            'title': 'thank you',
                                            'content': request.POST['newsletter-name'],
                                        })
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            'Thank You',
            text_content,
            settings.OSCAR_FROM_EMAIL,
            [request.POST['newsletter-email']]
        )
        email.fail_silently = False
        email.attach_alternative(html_content, "text/html")
        email.send()
        messages.success(request, "Thanks for subscribing.")
    return render(request, 'index.html')
