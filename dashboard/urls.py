
from django.urls import path
from dashboard.views import UserRegistrationView
from dashboard.views import UserLoginView, UserProfileView, GetAllUserView, ItemAdditionView,ItemListView

urlpatterns = [
    path('user/register/', UserRegistrationView.as_view(), name='register'),
    path('user/login/', UserLoginView.as_view(), name='login'),
    path('user/profile/', UserProfileView.as_view(), name='profile'),
    path('user/getAllUser/', GetAllUserView.as_view(), name='getAllUser'),
    path('item/addItem/', ItemAdditionView.as_view(), name='addItem'),
    path('item/getItem/', ItemListView.as_view(), name='getItem'),
]
