from .models import About, Resume, Malaka, Tajriba, M_tajriba, Sovrinlar, Service, Projects, Blog, Contact
from .serializers import AboutSerializer, ResumeSerializer, MalakaSerializer, TajribaSerializer, M_tajribaSerializer, SovrinlarSerializer, ServiceSerializer, ProjectsSerializer, BlogSerializer, ContactSerializer
from rest_framework.generics import ListAPIView, CreateAPIView



class AboutAPIView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class ResumeAPIView(ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class MalakaAPIView(ListAPIView):
    queryset = Malaka.objects.all()
    serializer_class = MalakaSerializer

class TajribaAPIView(ListAPIView):
    queryset = Tajriba.objects.all()
    serializer_class = TajribaSerializer

class M_tajribaAPIView(ListAPIView):
    queryset = M_tajriba.objects.all()
    serializer_class = M_tajribaSerializer

class SovrinlarAPIView(ListAPIView):
    queryset = Sovrinlar.objects.all()
    serializer_class = SovrinlarSerializer

class ServiceAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ProjectsAPIView(ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class BlogAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class ContactAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
