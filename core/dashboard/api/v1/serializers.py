from rest_framework import serializers
from ...models import Skill, Description,JobTitle
from django.shortcuts import get_object_or_404


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name",'job_title']
    def validate(self, attrs):
        return super().validate(attrs)
    
class SkillArchiveSerializer(serializers.Serializer):
    skill_id = serializers.IntegerField(required=True)
    
    def validate(self, attrs):
        skill_obj = get_object_or_404(Skill,pk=attrs.get('skill_id',None))
        if skill_obj.is_archived:
            raise serializers.ValidationError({"detail":"it is already archived"})
        attrs['skill_obj'] = skill_obj
        return super().validate(attrs)
    