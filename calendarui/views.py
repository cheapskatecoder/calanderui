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
        occurence = DqDatafile.objects.values_list('cadence', flat=True).distinct()
        categories = DqFeed.objects.values_list('category', flat=True).distinct()
        return render(request, self.template_name, context={'categories': categories, 'occurence': occurence})


class GetEvents(View):
    def get(self, request):
        events = list(
            DqDatafile.objects.all().values('dqfeed__file_status', 'cadence', 'data_file_name', 'dq_datafile_id').distinct())
        return JsonResponse(events, safe=False)


class TableView(View):
    template_name = 'calendarui/data-table.html'

    def get(self, request):
        filename = request.GET.get('file-name')
        occurence = request.GET.get('occurence')
        category = request.GET.get('category')
        rows = DqFeed.objects.all()
        context_data = {'category': category if category != '' else 'undefined',
                        'occurence': occurence if occurence != '' else 'undefined',
                        'filename': filename if filename != '' else 'undefined', 'rows': rows}
        return render(request, self.template_name, context=context_data)


class GetTableData(View):
    def get(self, request):
        filename = request.GET.get('file-name')
        occurence = request.GET.get('occurence')
        category = request.GET.get('category')
        print({'filename: ': filename, 'occurence: ': occurence, 'category: ': category})

        if filename != 'None' and occurence != 'None' and category != 'None':
            data = list(DqFeed.objects.filter(dq_datafile__data_file_name=filename, dq_datafile__cadence=occurence,
                                              category=category).values())
            return JsonResponse(data, safe=False)
        elif filename != 'None' and occurence != 'None' and category == 'None':
            print('second')
            data = list(
                DqFeed.objects.filter(dq_datafile__data_file_name=filename, dq_datafile__cadence=occurence).values())
            return JsonResponse(data, safe=False)
        elif filename != 'None' and occurence == 'None' and category == 'None':
            print('third')
            data = list(DqFeed.objects.filter(dq_datafile__data_file_name=filename).values())
            return JsonResponse(data, safe=False)
        elif filename == 'None' and occurence != 'None' and category != 'None':
            print('fourth')
            data = list(DqFeed.objects.filter(dq_datafile__data_file_name=filename).values())
            data = list(DqFeed.objects.filter(dq_datafile__data_file_name=filename, dq_datafile__cadence=occurence,
                                              category=category).values())
            return JsonResponse(data, safe=False)
        elif filename == 'None' and occurence != 'None' and category == 'None':
            print('fifth')
            data = list(DqFeed.objects.filter(dq_datafile__cadence=occurence).values())
            return JsonResponse(data, safe=False)
        elif filename != 'None' and occurence == 'None' and category != 'None':
            print('sixth')
            data = list(DqFeed.objects.filter(dq_datafile__data_file_name=filename, category=category).values())
            return JsonResponse(data, safe=False)
        elif filename == 'None' and occurence != 'None' and category != 'None':
            print('7th')
            data = list(DqFeed.objects.filter(dq_datafile__data_file_name=filename, dq_datafile__cadence=occurence,
                                              category=category).values())
            return JsonResponse(data, safe=False)
        elif filename == 'None' and occurence == 'None' and category != 'None':
            print('8th')
            data = list(DqFeed.objects.filter(category=category).values())
            return JsonResponse(data, safe=False)
        else:
            print('else th')
            data = list(DqFeed.objects.values())
            return JsonResponse(data, safe=False)
