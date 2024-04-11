from django.shortcuts import render
from .models import Faculty, Course, Room, Schedule
from .forms import ScheduleForm

def home(request):
    schedules = Schedule.objects.all()
    count = Schedule.objects.count()
    form = ScheduleForm()

    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or add a success message
    
    return render(request, 'base/homepage.html', {'schedules': schedules, 'form': form, 'count':count})
