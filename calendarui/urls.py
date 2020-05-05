from django.urls import path
from calendarui.views import Calendar, GetEvents


urlpatterns = [
    path('calendarUi', Calendar.as_view()),
    path('get-events', GetEvents.as_view())
]
