from django.urls import path
from .views import Calendar, GetEvents, TableView, GetTableData, FilterEvents, FilterDataTable


urlpatterns = [
    path('calendarUi', Calendar.as_view()),
    path('get-events', GetEvents.as_view()),
    path('data-table', TableView.as_view()),
    path('get-table-data', GetTableData.as_view()),
    path('filter-events', FilterEvents.as_view()),
    path('filter-data', FilterDataTable.as_view()),
]