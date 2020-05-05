from django.shortcuts import render
from django.views import View
from .models import DqDatafile
from django.http import JsonResponse
import datetime, calendar

class Calendar(View):
    template_name = 'calendarui/calendarUi.html'

    last_friday = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    while last_friday.weekday() != calendar.FRIDAY:
        last_friday -= one_day
    print(last_friday.strftime('%D'))



    def get(self, request):
        return render(request, self.template_name, context={})


class GetEvents(View):
    def get(self, request):
        events = list(DqDatafile.objects.values())
        return JsonResponse(events, safe=False)