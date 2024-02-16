# event_urls.py
from django.urls import path
from base.views.event_views import EventListCreateView, EventDetailView

urlpatterns = [
    path(
        "",
        EventListCreateView.as_view(),
        name="event-list-create",
    ),
    path("<str:pk>/", EventDetailView.as_view(), name="event-detail"),
]
