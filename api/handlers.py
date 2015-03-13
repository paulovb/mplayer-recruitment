from piston.handler import BaseHandler
from app.models import Recruitment, Skills


class RecruitmentHandler(BaseHandler):
    allowed_methods = ('GET', 'POST')
    # fields = ('name', 'mail', ('skills', ('name', 'value')))

    def read(self, request, *args, **kwargs):
        recruitments = Recruitment.objects.all()
        json = []
        for recruitment in recruitments:
            skills = Skills.objects.filter(recruitment=recruitment)

            json_recruitment = {
                'name': recruitment.name,
                'mail': recruitment.mail,
            }

            skills_list = []
            for skill in skills:
                json_skill = {
                    'name': skill.name,
                    'value': skill.value
                }
                skills_list.append(json_skill)

            json_recruitment['skills'] = skills_list

            json.append(json_recruitment)

        return json

    def create(self, request, *args, **kwargs):
        recruitment = Recruitment(name=request.data['name'],
                                  mail=request.data['mail'])
        recruitment.save()

        skills = request.data['skills']
        for skill in skills:
            Skills(name=skill['name'],
                   value=skill['value'],
                   recruitment=recruitment).save()

        return {}


