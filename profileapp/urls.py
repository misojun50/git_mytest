from django.urls import path

from profileapp.views import ProfileCreationView, ProfileUpdateView

app_name = 'profileapp'

urlpatterns = [
    # as_view 잊지 말것.
    # create 는 없는걸 만드는거라 상관없지만 update 는 있는걸 수정하는거기에 int:pk 지정
    path('create/', ProfileCreationView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),

]