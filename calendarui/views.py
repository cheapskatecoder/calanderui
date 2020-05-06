from django.shortcuts import render
from django.views import View
from .models import DqDatafile, DqFeed
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
        category = DqFeed.objects.values_list('category', flat=True).distinct()
        return render(request, self.template_name, context={'category': category})


class GetEvents(View):
    def get(self, request):
        events = list(DqDatafile.objects.values())
        return JsonResponse(events, safe=False)

class TableView(View):
    template_name = 'calendarui/data-table.html'
     
    def get(self, request):
        filename = request.GET.get('file-name')
        occurence = request.GET.get('occurence')
        yearly =  request.GET.get('yearly')
        category = DqFeed.objects.order_by('category').distinct('category')
        print(category)
        context_data = {'category': category ,'yearly': yearly if yearly != '' else 'undefined', 'occurence': occurence if occurence != '' else 'undefined', 'filename': filename if filename != '' else 'undefined'}
        return render(request, self.template_name, context=context_data)



class GetTableData(View):
    def get(self, request):
        filename = request.GET.get('file-name')
        occurence = request.GET.get('occurence')
        yearly =  request.GET.get('yearly')

        if filename != "undefined" and occurence != "undefined":
            data = list(DqDatafile.objects.filter(data_file_name=filename, cadence=occurence).values())
            return JsonResponse(data, safe=False)
        elif filename != "undefined"  and occurence != "undefined":
            data = list(DqDatafile.objects.filter(cadence=occurence).values())
            return JsonResponse(data, safe=False)
        elif filename != "undefined":
            data = list(DqDatafile.objects.filter(data_file_name=filename).values())
            return JsonResponse(data, safe=False)
        elif occurence != "undefined":
            data = list(DqDatafile.objects.filter(cadence=occurence).values())
            return JsonResponse(data, safe=False)
        else:
            data = list(DqDatafile.objects.values())
            return JsonResponse(data, safe=False)
