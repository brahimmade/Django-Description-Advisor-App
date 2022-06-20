from rest_framework import serializers
from ...models import Skill, Description,JobTitle
from django.shortcuts import get_object_or_404


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name",'job_title','is_core','is_marked','is_archived']
        read_only_fields = ['is_marked','is_archived']
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['job_title'] = JobTitleMinimumSerializer(instance.job_title,many=True).data
        rep['related_job_titles'] = instance.job_title.all().count()
        rep['created_date'] = instance.created_date.strftime('%Y-%m-%d %H:%M')
        rep['updated_date'] = instance.updated_date.strftime('%Y-%m-%d %H:%M')
        return rep 
    
class SkillArchiveSerializer(serializers.Serializer):
    skill_id = serializers.IntegerField(required=True)
    
    def validate(self, attrs):
        skill_obj = get_object_or_404(Skill,pk=attrs.get('skill_id',None))
        if skill_obj.is_archived:
            raise serializers.ValidationError({"detail":"it is already archived"})
        attrs['skill_obj'] = skill_obj
        return super().validate(attrs)

class SkillMarkSerializer(serializers.Serializer):
    skill_id = serializers.IntegerField(required=True)
    
    def validate(self, attrs):
        skill_obj = get_object_or_404(Skill,pk=attrs.get('skill_id',None))
        attrs['skill_obj'] = skill_obj
        return super().validate(attrs)


class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = ["id", "name",'is_core','is_marked','is_archived','created_date','updated_date']
        read_only_fields = ['is_marked','is_archived']
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        
        rep['created_date'] = instance.created_date.strftime('%Y-%m-%d %H:%M')
        rep['updated_date'] = instance.updated_date.strftime('%Y-%m-%d %H:%M')
        rep['related_skills'] = Skill.objects.filter(job_title__in=[instance]).count()
        rep['related_descriptions'] = Description.objects.filter(job_title__in=[instance]).count()
        return rep
    
    def create(self, validated_data):
        validated_data['is_core'] = False
        return super().create(validated_data)
    



class JobTitleArchiveSerializer(serializers.Serializer):
    job_title_id = serializers.IntegerField(required=True)
    
    def validate(self, attrs):
        job_title_obj = get_object_or_404(JobTitle,pk=attrs.get('job_title_id',None))
        if job_title_obj.is_archived:
            raise serializers.ValidationError({"detail":"it is already archived"})
        attrs['job_title_obj'] = job_title_obj
        return super().validate(attrs)

class JobTitleMarkSerializer(serializers.Serializer):
    job_title_id = serializers.IntegerField(required=True)
    
    def validate(self, attrs):
        job_title_obj = get_object_or_404(JobTitle,pk=attrs.get('job_title_id',None))
        attrs['job_title_obj'] = job_title_obj
        return super().validate(attrs)

class JobTitleMinimumSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = ["id", "name"]

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ["id", "text",'job_title','is_core','is_marked','is_archived','created_date','updated_date']
        read_only_fields = ['is_marked','is_archived']
        
    def validate(self, attrs):
        return super().validate(attrs)
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['job_title'] = JobTitleMinimumSerializer(instance.job_title,many=True).data
        rep['related_job_titles'] = instance.job_title.all().count()
        rep['created_date'] = instance.created_date.strftime('%Y-%m-%d %H:%M')
        rep['updated_date'] = instance.updated_date.strftime('%Y-%m-%d %H:%M')
        return rep 


class DescriptionArchiveSerializer(serializers.Serializer):
    description_id = serializers.IntegerField(required=True)
    
    def validate(self, attrs):
        description_obj = get_object_or_404(Description,pk=attrs.get('description_id',None))
        if description_obj.is_archived:
            raise serializers.ValidationError({"detail":"it is already archived"})
        attrs['description_obj'] = description_obj
        return super().validate(attrs)


class DescriptionMarkSerializer(serializers.Serializer):
    description_id = serializers.IntegerField(required=True)
    
    def validate(self, attrs):
        description_obj = get_object_or_404(Description,pk=attrs.get('description_id',None))
        attrs['description_obj'] = description_obj
        return super().validate(attrs)
    
