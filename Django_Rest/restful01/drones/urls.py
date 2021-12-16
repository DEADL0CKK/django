from django.urls import path
from drones import views


urlpatterns = [
    path('done-categoies/',
        views.DoneCategoyList.as_view(),
        name=views.DoneCategoyList.name),

    path('done-categoies/<int:pk>',
        views.DoneCategoyDetail.as_view(),
        name=views.DoneCategoyDetail.name),

    path('dones/',
        views.DoneList.as_view(),
        name=views.DoneList.name),

    path('dones/<int:pk>',
        views.DoneDetail.as_view(),
        name=views.DoneDetail.name),

    path('pilots/',
        views.PilotList.as_view(),
        name=views.PilotList.name),

    path('pilots/<int:pk>',
        views.PilotDetail.as_view(),
        name=views.PilotDetail.name),
    path('competitions/',
        views.CompetitionList.as_view(),
        name=views.CompetitionList.name),

    path('competitions/<int:pk>',
        views.CompetitionDetail.as_view(),
        name=views.CompetitionDetail.name),

    path('',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
]
