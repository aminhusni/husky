from django.shortcuts import render
from django.shortcuts import redirect
from supervisor.models import Supervisor, Checklist, Check_item
from location.models import Location
from feedback.models import Feedback, Problem
import uuid
from datetime import timedelta
from datetime import datetime
from django.utils import timezone
from dateutil.relativedelta import relativedelta

#Decorators
#Authenticate page request if the user has signed in and has it expired. Expiry extended
#if the token has not expired. 
def check_token(func):
    def gunc(*args, **kwargs):

        token_expiry_time = 2

        try:
                token = args[0].COOKIES.get('authorization_token')
                supervisorquery = Supervisor.objects.get(authorization_token=token)
                
        except Exception as e:
                context = {
                        'error': "Token is invalid. Your ID was probably being used somewhere else. Any submission was not recorded",
                }
                return render(args[0], 'supervisor/error.html', context)

        if(supervisorquery.authorization_expire > timezone.now()):
                supervisorquery.authorization_expire = timezone.now() + timedelta(minutes=token_expiry_time)
                supervisorquery.save()
                return func(*args, **kwargs)
        else:
                context = {
                        'error': "Your session has expired. Any submission was not recorded",
                }
                return render(args[0], 'supervisor/error.html', context)      

    return gunc


# Create your views here.
def index(request):
    
        return render(request, 'supervisor/index.html', None)

def authenticate(request):

        token_expiry_time = 2

        try:
                supervisor = Supervisor.objects.get(supervisor=request.POST['supervisor'])
                supervisor.authorization_token = uuid.uuid4().hex
                supervisor.authorization_expire = timezone.now() + timedelta(minutes=token_expiry_time)
                supervisor.save()
                response = redirect('supervisor:supervisor_index')
                response.set_cookie('authorization_token', supervisor.authorization_token)
                return response

        except:
                return redirect('feedback:index')

@check_token
def checklist(request):
        
        return render(request, 'supervisor/checklist.html', None)

@check_token
def supervisor_index(request):

        if not request.COOKIES.get('location_id'):
                locationsetting = False
        else:
                locationsetting = True
        
        context = {
                        'locationsetting': locationsetting,
                }

        return render(request, 'supervisor/supervisor_index.html', context)

@check_token
def checklist_submit(request):

        try:
                token = request.COOKIES.get('authorization_token')
                supervisorquery = Supervisor.objects.get(authorization_token=token)
                
        except Exception as e:
                context = {
                        'error': "Token is invalid. Your ID was probably being used somewhere else. Any submission was not recorded",
                }
                return render(request, 'supervisor/error.html', context)

        pcheck = Checklist(location_id=request.COOKIES.get('location_id'), employee_number=supervisorquery)
        pcheck.save()

        if 'checklist' not in request.POST:
                checklist = False
        else:
                checklist = bool(request.POST['checklist'])   

        if 'floor' not in request.POST:
                floor = False
        else:
                floor = bool(request.POST['floor'])

        if 'smell' not in request.POST:
                smell = False
        else:
                smell = bool(request.POST['smell'])

        if 'wall' not in request.POST:
                wall = False
        else:
                wall = bool(request.POST['wall'])

        if 'dustbin' not in request.POST:
                dustbin = False
        else:
                dustbin = bool(request.POST['dustbin'])

        if 'toilet_bowl' not in request.POST:
                toilet_bowl = False
        else:
                toilet_bowl = bool(request.POST['toilet_bowl'])

        if 'urinal_bowl' not in request.POST:
                urinal_bowl = False
        else:
                urinal_bowl = bool(request.POST['urinal_bowl'])

        if 'wash_basin' not in request.POST:
                wash_basin = False
        else:
                wash_basin = bool(request.POST['wash_basin'])

        if 'mirror' not in request.POST:
                mirror = False
        else:
                mirror = bool(request.POST['mirror'])

        if 'tissue' not in request.POST:
                tissue = False
        else:
                tissue = bool(request.POST['tissue'])

        if 'handsoap' not in request.POST:
                handsoap = False
        else:
                handsoap = bool(request.POST['handsoap'])

        checklist = Check_item(checklist=pcheck, floor=floor, smell=smell, wall=wall, dustbin=dustbin, toilet_bowl=toilet_bowl, urinal_bowl=urinal_bowl, wash_basin=wash_basin, mirror=mirror, tissue=tissue, handsoap=handsoap)
        checklist.save()

        return redirect('feedback:thankyou')



def error(request):
        pass

@check_token
def checklist_report(request):
        location_id = request.POST['location_id']
        print(location_id)

        lokasi = Location.objects.filter(location_id=location_id).first()
        location_name = lokasi.location_name
        #Calculate for last month
        target_month = datetime.now() - relativedelta(months=0)
        month_str = target_month.strftime("%B")

        report = Checklist.objects.filter(created__month=target_month.month, location_id=location_id).prefetch_related('check_item_set')
        fieldnames = Check_item._meta.get_fields()

        #Skip first two elements
        iternames = iter(fieldnames)
        next(iternames)
        next(iternames)

        context = {
                'month': month_str,
                'report': report,
                'iternames': iternames,
                'location_name': location_name,
                'location_id': location_id,

        }

        return render(request, 'supervisor/checklist_report.html', context)

@check_token
def checklist_report_location(request):
        locations = Location.objects.all()
        location_name = ""
        location_id = ""


        if not request.COOKIES.get('location_id'):
                locationsetting = False
        else:
                locationsetting = True
                location_id = request.COOKIES.get('location_id')
                print(location_id)
                lokasi = Location.objects.filter(location_id=location_id).first()
                location_name = lokasi.location_name
        


        context = {
        'locations': locations,
        'location_name': location_name,
        'location_id': location_id,
        'locationsetting': locationsetting,
        }
        return render(request, 'supervisor/checklist_report_location.html', context)

@check_token
def performance_report_location(request):
        locations = Location.objects.all()
        location_name = ""
        location_id = ""

        if not request.COOKIES.get('location_id'):
                locationsetting = False
        else:
                locationsetting = True
                location_id = request.COOKIES.get('location_id')
                print(location_id)
                lokasi = Location.objects.filter(location_id=location_id).first()
                location_name = lokasi.location_name

        context = {
        'locations': locations,
        'location_name': location_name,
        'location_id': location_id,
        'locationsetting': locationsetting,
        }
        return render(request, 'supervisor/performance_report_location.html', context)

@check_token
def performance_report(request):
        location_id = request.POST['location_id']

        lokasi = Location.objects.filter(location_id=location_id).first()
        location_name = lokasi.location_name


        #Calculate for today
        target_day = datetime.now() - relativedelta(days=0)
        day_str = target_day.strftime("%A %d %b %Y")

        reports = Feedback.objects.filter(created__day=target_day.day, location_id=location_id).prefetch_related('problem_set')
        total_feedback = reports.count()

        #Initialize all counters
        one = 0
        two = 0
        three = 0
        four = 0
        five = 0
        problems = {'Feedback': 0, 'Clogged': 0, 'Toilet paper': 0, 'Lighting': 0,
                    'Soap': 0, 'Hose': 0, 'Temperature': 0, 'Bowl': 0, 'Sink': 0,
                    'Smell': 0, 'Fault': 0, }


        for report in reports:
                print(report)
                try:
                        problemo = report.problem_set.all().first()
                        if(problemo.feedback  == True):
                                problems['Feedback'] += 1
                        if(problemo.clogged  == True):
                                problems['Clogged'] += 1
                        if(problemo.toilet_paper  == True):
                                problems['Toilet paper'] += 1
                        if(problemo.lighting  == True):
                                problems['Lighting'] += 1
                        if(problemo.soap  == True):
                                problems['Soap'] += 1
                        if(problemo.hose  == True):
                                problems['Hose'] += 1
                        if(problemo.temperature  == True):
                                problems['Temperature'] += 1
                        if(problemo.bowl  == True):
                                problems['Bowl'] += 1
                        if(problemo.sink  == True):
                                problems['Sink'] += 1
                        if(problemo.smell  == True):
                                problems['Smell'] += 1
                        if(problemo.fault  == True):
                                problems['Fault'] += 1
                except:
                        pass

                if(report.rating == 1):
                        one += 1
                if(report.rating == 2):
                        two += 1
                if(report.rating == 3):
                        three += 1
                if(report.rating == 4):
                        four += 1
                if(report.rating == 5):
                        five += 1

                
        

        context = {
                'day': day_str,
                'report': reports,
                'location_name': location_name,
                'location_id': location_id,
                'total_feedback': total_feedback,
                'one': one,
                'two': two,
                'three': three,
                'four': four,
                'five': five,
                'problems': problems,

        }

        return render(request, 'supervisor/performance_report.html', context)