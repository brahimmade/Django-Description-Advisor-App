from rest_framework import serializers
from ...models import Skill, Description,JobTitle,AboutDescription
from django.shortcuts import get_object_or_404


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name",'job_title','is_core','is_marked','related_job_titles','is_archived']
        read_only_fields = ['is_marked','is_archived']
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        instance.related_job_titles = instance.job_title.all().count()
        rep['job_title'] = JobTitleMinimumSerializer(instance.job_title,many=True).data
        rep['created_date'] = instance.created_date.strftime('%Y-%m-%d %H:%M')
        rep['updated_date'] = instance.updated_date.strftime('%Y-%m-%d %H:%M')
        return rep 
    
class SkillArchiveSerializer(serializers.Serializer):
    skill_id = serializers.IntegerField(required=True)
    
    def validate(self, attrs):
        skill_obj = get_object_or_404(Skill,pk=attrs.get('skill_id',None))
        # if skill_obj.is_archived:
        #     raise serializers.ValidationError({"detail":"it is already archived"})
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
        fields = ["id", "name",'is_core','is_marked','is_archived','created_date','related_skills','related_descriptions','updated_date']
        read_only_fields = ['is_marked','is_archived']
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['created_date'] = instance.created_date.strftime('%Y-%m-%d %H:%M')
        rep['updated_date'] = instance.updated_date.strftime('%Y-%m-%d %H:%M')
        return rep
    
    def create(self, validated_data):
        validated_data['is_core'] = False
        return super().create(validated_data)
    



class JobTitleArchiveSerializer(serializers.Serializer):
    job_title_id = serializers.IntegerField(required=True)
    
    def validate(self, attrs):
        job_title_obj = get_object_or_404(JobTitle,pk=attrs.get('job_title_id',None))
        # if job_title_obj.is_archived:
        #     raise serializers.ValidationError({"detail":"it is already archived"})
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
        fields = ["id", "text",'job_title','is_core','is_marked','is_archived','created_date','related_job_titles','updated_date']
        read_only_fields = ['is_marked','is_archived']
        
    def validate(self, attrs):
        return super().validate(attrs)
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['job_title'] = JobTitleMinimumSerializer(instance.job_title,many=True).data
        # rep['related_job_titles'] = instance.job_title.all().count()
        rep['created_date'] = instance.created_date.strftime('%Y-%m-%d %H:%M')
        rep['updated_date'] = instance.updated_date.strftime('%Y-%m-%d %H:%M')
        return rep 


class DescriptionArchiveSerializer(serializers.Serializer):
    description_id = serializers.IntegerField(required=True)
    
    def validate(self, attrs):
        description_obj = get_object_or_404(Description,pk=attrs.get('description_id',None))
        attrs['description_obj'] = description_obj
        return super().validate(attrs)


class DescriptionMarkSerializer(serializers.Serializer):
    description_id = serializers.IntegerField(required=True)
    
    def validate(self, attrs):
        description_obj = get_object_or_404(Description,pk=attrs.get('description_id',None))
        attrs['description_obj'] = description_obj
        return super().validate(attrs)
    



class MultiSelectActionSerializer(serializers.Serializer):
    operation_type = serializers.CharField(required=True)
    list_ids = serializers.ListField()
    
    def validate(self, attrs):
        OPT_TYPE_VALIDATE = ('mark', 'unmark', 'archive', 'unarchive')
        if attrs.get("operation_type") not in OPT_TYPE_VALIDATE :
            raise serializers.ValidationError('operation_type not defined')
        return super().validate(attrs)
    
    

class AboutDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutDescription
        fields = ["id", "text",'job_title','is_core','is_marked','is_archived','created_date','related_job_titles','updated_date']
        read_only_fields = ['is_marked','is_archived']
        
    def validate(self, attrs):
        return super().validate(attrs)
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['job_title'] = JobTitleMinimumSerializer(instance.job_title,many=True).data
        # rep['related_job_titles'] = instance.job_title.all().count()
        rep['created_date'] = instance.created_date.strftime('%Y-%m-%d %H:%M')
        rep['updated_date'] = instance.updated_date.strftime('%Y-%m-%d %H:%M')
        return rep 


class AboutDescriptionArchiveSerializer(serializers.Serializer):
    description_id = serializers.IntegerField(required=True)
    
    def validate(self, attrs):
        description_obj = get_object_or_404(AboutDescription,pk=attrs.get('description_id',None))
        attrs['description_obj'] = description_obj
        return super().validate(attrs)


class AboutDescriptionMarkSerializer(serializers.Serializer):
    description_id = serializers.IntegerField(required=True)
    
    def validate(self, attrs):
        description_obj = get_object_or_404(AboutDescription,pk=attrs.get('description_id',None))
        attrs['description_obj'] = description_obj
        return super().validate(attrs)