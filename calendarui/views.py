from django.shortcuts import render
from django.views import View
from .models import DqDatafile, DqFeedNew
from django.http import JsonResponse
import datetime, calendar


class Calendar(View):
    template_name = 'calendarui/calendarUi.html'

    def get(self, request):
        occurence = DqDatafile.objects.filter(cadence__isnull=False).values_list('cadence', flat=True).distinct()
        categories = DqFeedNew.objects.filter(category__isnull=False).values_list('category', flat=True).distinct()
        return render(request, self.template_name, context={'categories': categories, 'occurence': occurence})


class GetEvents(View):
    def get(self, request):
        events = list(
            DqDatafile.objects.all().values('dqfeednew__file_status', 'cadence', 'data_file_name', 'dq_datafile_id').distinct())
        return JsonResponse(events, safe=False)


class FilterEvents(View):
    def get(self, request):
        filename = request.GET.get('file-name')
        occurence = request.GET.get('occurence')
        category = request.GET.get('category')

        if filename != 'undefined' and occurence != 'undefined' and category != 'undefined':
            data = list(DqDatafile.objects.filter(data_file_name=filename, cadence=occurence,
                                              dqfeednew__category=category).values('dqfeednew__file_status', 'cadence', 'data_file_name', 'dq_datafile_id', 'data_file_name', 'cadence').distinct())
            return JsonResponse(data, safe=False)

        elif filename != 'undefined' and  occurence == 'undefined' and  category != 'undefined':
            data = list(DqDatafile.objects.filter(data_file_name=filename, dqfeednew__category=category).values('dqfeednew__file_status', 'cadence', 'data_file_name', 'dq_datafile_id', 'data_file_name', 'cadence').distinct())
            return JsonResponse(data, safe=False)
        elif filename != 'undefined' and  occurence != 'undefined' and category == 'undefined':
            data = list(DqDatafile.objects.filter(data_file_name=filename, cadence=occurence).values('dqfeednew__file_status', 'cadence', 'data_file_name', 'dq_datafile_id', 'data_file_name', 'cadence').distinct())
            return JsonResponse(data, safe=False)
        elif filename != 'undefined' and  occurence == 'undefined' and  category == 'undefined':
            data = list(DqDatafile.objects.filter(data_file_name=filename).values('dqfeednew__file_status', 'cadence', 'data_file_name', 'dq_datafile_id', 'data_file_name', 'cadence').distinct())
            return JsonResponse(data, safe=False)

        elif filename == 'undefined' and  occurence != 'undefined' and category != 'undefined':
            data = list(DqDatafile.objects.filter(cadence=occurence, dqfeednew__category=category).values('dqfeednew__file_status', 'cadence', 'data_file_name', 'dq_datafile_id', 'data_file_name', 'cadence').distinct())
            return JsonResponse(data, safe=False)
        elif  filename != 'undefined' and  occurence != 'undefined' and category == 'undefined':
            data = list(DqDatafile.objects.filter(cadence=occurence, data_file_name=filename).values('dqfeednew__file_status', 'cadence', 'data_file_name', 'dq_datafile_id', 'data_file_name', 'cadence').distinct())
            return JsonResponse(data, safe=False)
        elif filename == 'undefined' and  occurence != 'undefined' and category == 'undefined':
            data = list(DqDatafile.objects.filter(cadence=occurence).values('dqfeednew__file_status', 'cadence', 'data_file_name', 'dq_datafile_id', 'data_file_name', 'cadence').distinct())
            return JsonResponse(data, safe=False)

        elif  filename != 'undefined' and  occurence == 'undefined' and category != 'undefined':
            data = list(DqDatafile.objects.filter(data_file_name=filename, dqfeednew__category=category).values('dqfeednew__file_status', 'cadence', 'data_file_name', 'dq_datafile_id', 'data_file_name', 'cadence').distinct())
            return JsonResponse(data, safe=False)
        elif filename == 'undefined' and  occurence != 'undefined' and category != 'undefined':
            data = list(DqDatafile.objects.filter(cadence=filename, dqfeednew__category=category).values('dqfeednew__file_status', 'cadence', 'data_file_name', 'dq_datafile_id', 'data_file_name', 'cadence').distinct())
            return JsonResponse(data, safe=False)
        elif filename == 'undefined' and  occurence == 'undefined' and category != 'undefined':
            data = list(DqDatafile.objects.filter(dqfeednew__category=category).values('dqfeednew__file_status', 'cadence', 'data_file_name', 'dq_datafile_id', 'data_file_name', 'cadence').distinct())
            return JsonResponse(data, safe=False)
        elif filename == 'undefined' and  occurence == 'undefined' and category == 'undefined':
            data = list(DqDatafile.objects.values('dqfeednew__file_status', 'cadence', 'data_file_name', 'dq_datafile_id', 'data_file_name', 'cadence').distinct())
            return JsonResponse(data, safe=False)
        elif  filename == None and  occurence == None and category == None:
            data = list(DqDatafile.objects.values('dqfeednew__file_status', 'cadence', 'data_file_name', 'dq_datafile_id', 'data_file_name', 'cadence').distinct())
            return JsonResponse(data, safe=False)


class TableView(View):
    template_name = 'calendarui/data-table.html'

    def get(self, request):
        filename = request.GET.get('file-name')
        occurence = request.GET.get('occurence')
        category = request.GET.get('category')

        rows = DqFeedNew.objects.all()
        receivedDate = DqFeedNew.objects.filter(received_date__isnull=False).values_list('received_date',flat=True).distinct()
        fileType = DqFeedNew.objects.filter(source_datafile_type__isnull=False).values_list('source_datafile_type',flat=True).distinct()
        categories = DqFeedNew.objects.filter(category__isnull=False).values_list('category',flat=True).distinct()
        context_data = {'category': category if category != '' else 'undefined',
                        'occurence': occurence if occurence != '' else 'undefined',
                        'filename': filename if filename != '' else 'undefined',
                        'receivedDate': receivedDate, 'fileType': fileType, 'categories': categories,
                        'rows': rows}
        return render(request, self.template_name, context=context_data)


class GetTableData(View):
    def get(self, request):
        filename = request.GET.get('file-name')
        occurence = request.GET.get('occurence')
        category = request.GET.get('category')

        if filename != 'undefined' and occurence != 'undefined' and category != 'undefined':
            data = list(DqFeedNew.objects.filter(dq_datafile__data_file_name=filename, dq_datafile__cadence=occurence,
                                              category=category).values())
            return JsonResponse(data, safe=False)

        elif filename != 'undefined' and  occurence == 'undefined' and  category != 'undefined':
            data = list(DqFeedNew.objects.filter(dq_datafile__data_file_name=filename, category=category).values())
            return JsonResponse(data, safe=False)
        elif filename != 'undefined' and  occurence != 'undefined' and category == 'undefined':
            data = list(DqFeedNew.objects.filter(dq_datafile__data_file_name=filename, dq_datafile__cadence=occurence).values())
            return JsonResponse(data, safe=False)
        elif filename != 'undefined' and  occurence == 'undefined' and  category == 'undefined':
            data = list(DqFeedNew.objects.filter(dq_datafile__data_file_name=filename).values())
            return JsonResponse(data, safe=False)

        elif filename == 'undefined' and  occurence != 'undefined' and category != 'undefined':
            data = list(DqFeedNew.objects.filter(dq_datafile__cadence=occurence, category=category).values())
            return JsonResponse(data, safe=False)
        elif  filename != 'undefined' and  occurence != 'undefined' and category == 'undefined':
            data = list(DqFeedNew.objects.filter(dq_datafile__cadence=occurence, dq_datafile__data_file_name=filename).values())
            return JsonResponse(data, safe=False)
        elif filename == 'undefined' and  occurence != 'undefined' and category == 'undefined':
            data = list(DqFeedNew.objects.filter(dq_datafile__cadence=occurence).values())
            return JsonResponse(data, safe=False)

        elif  filename != 'undefined' and  occurence == 'undefined' and category != 'undefined':
            data = list(DqFeedNew.objects.filter(dq_datafile__data_file_name=filename, category=category).values())
            return JsonResponse(data, safe=False)
        elif filename == 'undefined' and  occurence != 'undefined' and category != 'undefined':
            data = list(DqFeedNew.objects.filter(dq_datafile__cadence=filename, category=category).values())
            return JsonResponse(data, safe=False)
        elif filename == 'undefined' and  occurence == 'undefined' and category != 'undefined':
            data = list(DqFeedNew.objects.filter(category=category).values())
            return JsonResponse(data, safe=False)

        elif filename == 'undefined' and  occurence == 'undefined' and category == 'undefined':
            data = list(DqFeedNew.objects.values())
            return JsonResponse(data, safe=False)
        elif  filename == 'None' and  occurence == 'None' and category == 'None':
            data = list(DqFeedNew.objects.values())
            return JsonResponse(data, safe=False)
