from django.urls import path
from .views import new, detail, edit, destory

app_name = 'article'

urlpatterns = [
    path('new/', new, name='new'),
    path('<int:id>', detail, name='detail'),
    path('edit/<int:id>', edit, name='edit'),
    path('destroy/<int:id>', destory, name='destory'),
]
