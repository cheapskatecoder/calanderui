from django.urls import path
from calendarui.views import Calendar, GetEvents, TableView, GetTableData


urlpatterns = [
    path('calendarUi', Calendar.as_view()),
    path('get-events', GetEvents.as_view()),
    path('data-table', TableView.as_view()),
    path('get-table-data', GetTableData.as_view()),
]