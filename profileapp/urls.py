from django.urls import path

from profileapp.views import ProfileCreationView

app_name = 'profileapp'

urlpatterns = [
    # as_view 잊지 말것.
    path('create/', ProfileCreationView.as_view(), name='create')

]