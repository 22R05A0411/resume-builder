from django.urls import path
from .views import ResumeListCreateView, ResumeDetailView
from .views import generate_pdf

urlpatterns = [
    path('', ResumeListCreateView.as_view(), name='resume-list'),
    path('<int:pk>/', ResumeDetailView.as_view(), name='resume-detail'),
]

urlpatterns += [
    path('<int:pk>/pdf/', generate_pdf, name='resume-pdf'),
]