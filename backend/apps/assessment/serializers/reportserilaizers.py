from rest_framework import serializers

from common.abstractservices import load_model

from baseinfo.serializers.profileserializers import AssessmentProfileSerilizer
from account.serializers.commonserializers import SpaceSerializer

from assessment.serializers.commonserializers import ColorSerilizer
from assessment.models import AssessmentProject, AssessmentResult
from assessment.services import attributesstatistics, reportservices, metricstatistic

class AssessmentProjectReportSerilizer(serializers.ModelSerializer):
    color = ColorSerilizer()
    space = SpaceSerializer()
    assessment_profile = AssessmentProfileSerilizer()
    class Meta:
        model = AssessmentProject
        fields = ['title', 'last_modification_date', 'color', 'assessment_results', 'space', 'assessment_profile']

                
class AssessmentReportSerilizer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField(method_name='calculate_total_status')
    assessment_project = AssessmentProjectReportSerilizer()
    subjects_info = serializers.SerializerMethodField(method_name='calculate_subjects_info')
    most_significant_strength_atts = serializers.SerializerMethodField()
    most_significant_weaknessness_atts = serializers.SerializerMethodField()
    total_progress = serializers.SerializerMethodField()

    def get_total_progress(self, result: AssessmentResult):
        return metricstatistic.extract_total_progress(result)
        
    def calculate_subjects_info(self, result: AssessmentResult):
        return reportservices.calculate_subjects_info(result)

    def get_most_significant_strength_atts(self, result: AssessmentResult):
        return attributesstatistics.extract_most_significant_strength_atts(result)
        
    def get_most_significant_weaknessness_atts(self, result: AssessmentResult):
        return attributesstatistics.extract_most_significant_weaknessness_atts(result)
    
    def calculate_total_status(self, result: AssessmentResult):
        if result.quality_attribute_values.all():
            assessment = load_model(AssessmentProject, result.assessment_project_id)
            return assessment.status
        else:
            return "Not Calculated"

    class Meta:
        model = AssessmentResult
        fields = ['assessment_project', 'status', 'subjects_info', 'most_significant_strength_atts', 'most_significant_weaknessness_atts', 'total_progress']    