from django.urls import path
from .views import AboutAPIView, ResumeAPIView, MalakaAPIView, TajribaAPIView, M_tajribaAPIView, SovrinlarAPIView, ServiceAPIView, ProjectsAPIView, BlogAPIView, ContactAPIView

urlpatterns = [
    path('about/', AboutAPIView.as_view(), name='about'),
    path('resume/', ResumeAPIView.as_view(), name='resume'),
    path('malaka/', MalakaAPIView.as_view(), name='malaka'),
    path('tajriba/', TajribaAPIView.as_view(), name='tajriba'),
    path('m_tajriba/', M_tajribaAPIView.as_view(), name='m_tajriba'),
    path('sovrinlar/', SovrinlarAPIView.as_view(), name='sovrinlar'),
    path('service/', ServiceAPIView.as_view(), name='service'),
    path('projects/', ProjectsAPIView.as_view(), name='projects'),
    path('blog/', BlogAPIView.as_view(), name='blog'),
    path('contact/', ContactAPIView.as_view(), name='contact'),
]