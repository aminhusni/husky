from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from feedback.models import Feedback, Problem
from location.models import Location
from django.shortcuts import redirect
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler
import telegram.ext



# Create your views here.
bot = telegram.Bot(token='574491770:AAEEuzsNjFvVUj8q6Abxd1YUdI7pduSHobA')
chat_id = -304829808
#Telegram

def index(request):
    
    if not request.COOKIES.get('location_id'):
        return redirect('feedback:setup')

    else:
        return render(request, 'feedback/index.html', None)

def setup(request):
    locations = Location.objects.all()
    context = {
        'locations': locations,
    }
    return render(request, 'feedback/setup.html', context)
    
def setlocation(request):

    response = redirect('feedback:index')
    response.set_cookie('location_id', request.POST['location_id'])
    return response

def rating_submit(request):

    rating = int(request.POST['rating'])
    location_id = request.COOKIES.get('location_id')
    currentfeedback = Feedback(rating=rating, location_id=location_id)
    currentfeedback.save()

    if rating < 3:
        return render(request, 'feedback/problem.html', {'feedback_id': currentfeedback.id})
    else:
        return redirect('feedback:thankyou')

def thankyou(request):
    return render(request, 'feedback/thankyou.html', None)
    
def problem_submit(request):

    feedback_id = request.POST['feedback_id']

    if 'clogged' not in request.POST:
        clogged = False
    else:
        clogged = bool(request.POST['clogged'])   

    if 'toilet_paper' not in request.POST:
        toilet_paper = False
    else:
        toilet_paper = bool(request.POST['toilet_paper'])

    if 'lighting' not in request.POST:
        lighting = False
    else:
        lighting = bool(request.POST['lighting'])

    if 'soap' not in request.POST:
        soap = False
    else:
        soap = bool(request.POST['soap'])

    if 'hose' not in request.POST:
        hose = False
    else:
        hose = bool(request.POST['hose'])

    if 'temperature' not in request.POST:
        temperature = False
    else:
        temperature = bool(request.POST['temperature'])

    if 'bowl' not in request.POST:
        bowl = False
    else:
        bowl = bool(request.POST['bowl'])

    if 'sink' not in request.POST:
        sink = False
    else:
        sink = bool(request.POST['sink'])

    if 'smell' not in request.POST:
        smell = False
    else:
        smell = bool(request.POST['smell'])

    if 'fault' not in request.POST:
        fault = False
    else:
        fault = bool(request.POST['fault'])

    feedbackprev = Feedback.objects.get(pk=feedback_id)
    problems = Problem(feedback=feedbackprev, clogged=clogged, toilet_paper=toilet_paper, lighting=lighting, soap=soap, hose=hose, temperature=temperature, bowl=bowl, sink=sink, smell=smell, fault=fault)
    problems.save()
    location_id = feedbackprev.location_id
    location = Location.objects.get(location_id=location_id)
    location_name = location.location_name

    #Telegram Alert Part
    alerttext = "Problem at "+location_name + "(ID: "+location_id+")"
    bot.sendMessage(chat_id=chat_id, text=alerttext)

    return redirect('feedback:thankyou')


def problem(request):
    return render(request, 'feedback/problem.html', None)

