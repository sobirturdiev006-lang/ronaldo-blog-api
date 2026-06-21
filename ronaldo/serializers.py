from .models import About, Resume, Malaka, Tajriba, M_tajriba, Sovrinlar, Service, Projects, Blog, Contact
from rest_framework import serializers


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('title', 'description', 'image', 'name', 'birth_date', 'address', 'email', 'phone', 'finished_projects')


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('year', 'title', 'learn_center', 'description', 'is_published')


class MalakaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Malaka
        fields = ('year', 'title', 'learn_center', 'description', 'is_published')


class TajribaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tajriba
        fields = ('title', 'percent', 'mini_percent', 'mini_percent2', 'time', 'time2', 'is_published')


class M_tajribaSerializer(serializers.ModelSerializer):
    class Meta:
        model = M_tajriba
        fields = ('title', 'percent', 'is_published')


class SovrinlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sovrinlar
        fields = ('year', 'learn_center', 'title', 'description', 'is_published')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('title', 'title2', 'description', 'is_published')


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'image', 'design_name', 'design_type', 'is_published')


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('infor', 'image', 'title', 'year', 'description')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('title', 'address', 'phone', 'email')
