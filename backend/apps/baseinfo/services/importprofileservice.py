from zipfile import ZipFile
from django.utils.text import slugify 
from django.db import transaction

from baseinfo.models.basemodels import Questionnaire, AssessmentSubject, QualityAttribute
from baseinfo.models.metricmodels import Metric, MetricImpact, AnswerTemplate
from baseinfo.models.profilemodels import AssessmentProfile, ProfileDsl
from baseinfo.services import profileservice, expertgroupservice

def extract_dsl_contents(dsl_id):
    dsl = ProfileDsl.objects.get(id = dsl_id)
    input_zip = ZipFile(dsl.dsl_file)
    all_content = ''
    for name in input_zip.namelist():
        content = input_zip.read(name).decode('utf-8')
        trim_content = __trim_content(content)
        all_content = all_content + '\n' + trim_content
    return all_content

def __trim_content(content):
    new_content = ''
    for line in content.splitlines():
        if not line.strip().startswith('import'):
            line = line.replace('.', '')
            new_content = new_content + '\n' + line
    return new_content
@transaction.atomic
def import_profile(descriptive_profile, **kwargs):
    assessment_profile = __import_profile_base_info(kwargs)
    __import_questionnaires(descriptive_profile['questionnaireModels'], assessment_profile)
    __import_subjects(descriptive_profile['subjectModels'], assessment_profile)
    __import_attributes(descriptive_profile['attributeModels'])
    __import_metrics(descriptive_profile['metricModels'])
    return assessment_profile

def extract_tags(tag_ids):
    tags = []
    if tag_ids:
        for tag_id in tag_ids:
            tag = profileservice.load_profile_tag(tag_id)
            if tag:
                tags.append(tag)
    return tags


def __import_profile_base_info(extra_info):
    tags = extract_tags(extra_info['tag_ids'])
    expert_group = expertgroupservice.load_expert_group(extra_info['expert_group_id'])
    assessment_profile = AssessmentProfile()
    assessment_profile.code = slugify(extra_info['title'])
    assessment_profile.title = extra_info['title']
    assessment_profile.about = extra_info['about']
    assessment_profile.summary = extra_info['summary']
    assessment_profile.expert_group = expert_group
    assessment_profile.save()
    for tag in tags:
        assessment_profile.tags.add(tag)
    assessment_profile.save()
    return assessment_profile

def __import_questionnaires(questionnaire_models, profile):
    for questionnaire_model in questionnaire_models:
        questionnaire = Questionnaire()
        questionnaire.code = questionnaire_model['code']
        questionnaire.title = questionnaire_model['title']
        questionnaire.description = questionnaire_model['description']
        questionnaire.index = questionnaire_model['index']
        questionnaire.assessment_profile = profile
        questionnaire.save()

def __import_subjects(subject_models, profile):
    for model in subject_models:
        subject = AssessmentSubject()
        subject.code = model['code']
        subject.title = model['title']
        subject.description = model['description']
        subject.index = model['index']
        subject.assessment_profile = profile
        questionnaire_codes = model['questionnaireCodes']
        subject.save()
        for questionnaire_code in questionnaire_codes:
            questionnaire = Questionnaire.objects.filter(code = questionnaire_code).first()
            subject.questionnaires.add(questionnaire)
            subject.save()
        

def __import_attributes(attributeModels):
    for model in attributeModels:
        attribute = QualityAttribute()
        attribute.code = model['code']
        attribute.title = model['title']
        attribute.description = model['description']
        attribute.index = model['index']
        attribute.assessment_subject = AssessmentSubject.objects.filter(code = model['subjectCode']).first()
        attribute.save()


def __import_metrics(metricModels):
    for model in metricModels:
        metric = Metric()
        metric.title = model['question']
        metric.index = model['index']
        metric.questionnaire = Questionnaire.objects.filter(code=model['questionnaireCode']).first()
        metric.save()
        for impact_model in model['metricImpacts']:
            impact = MetricImpact()
            impact.level = impact_model['level']
            impact.quality_attribute = QualityAttribute.objects.filter(code = impact_model['attributeCode']).first()
            impact.metric = metric
            impact.save()
        for answer_model in model['answers']:
            answer = AnswerTemplate()
            answer.caption = answer_model['caption']
            answer.value = answer_model['value']
            answer.index = answer_model['index']
            answer.metric = metric
            answer.save()
            metric.answer_templates.add(answer)
        metric.save()
            


