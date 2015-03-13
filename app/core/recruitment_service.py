# coding: utf-8
from app.models import Recruitment, Skills
from app.tasks import send_mail_queue


class RecruitmentService():

    values = {}

    MAIL_SUBJECT = "Obrigado por se candidatar"
    MAIL_FRONT = "Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Front-End entraremos em contato."
    MAIL_BACK = "Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Back-End entraremos em contato."
    MAIL_MOBILE = "Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Mobile entraremos em contato."
    MAIL_GENERIC = "Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador entraremos em contato."

    HTML = "HTML"
    PYTHON = "PYTHON"
    DJANGO = "DJANGO"
    ANDROID = "ANDROID"
    JAVASCRIPT = "JAVASCRIPT"
    CSS = "CSS"
    IOS = "IOS"

    def get_skills(self):
        skills = [self.HTML, self.PYTHON, self.DJANGO, self.ANDROID, self.JAVASCRIPT, self.CSS, self.IOS]
        return skills

    @staticmethod
    def _has_minimal_skills(skills, values):
        if all(keys in values for keys in skills):
            for item in skills:
                if values[item] < 7:
                    return False
            return True
        return False

    def is_front(self):
        skills = (self.CSS, self.HTML, self.JAVASCRIPT)
        return self._has_minimal_skills(skills, self.values)

    def is_back(self):
        skills = (self.PYTHON, self.DJANGO)
        return self._has_minimal_skills(skills, self.values)

    def is_mobile(self):
        skills = (self.IOS, self.ANDROID)
        return self._has_minimal_skills(skills, self.values)

    def send_mails(self, email_list=None):

        from_email = 'recruitment@meuspedidos.com.br'

        if self.is_front():
            send_mail_queue.delay(from_email, email_list, self.MAIL_SUBJECT, self.MAIL_FRONT)

        if self.is_back():
            send_mail_queue.delay(from_email, email_list, self.MAIL_SUBJECT, self.MAIL_BACK)

        if self.is_mobile():
            send_mail_queue.delay(from_email, email_list, self.MAIL_SUBJECT, self.MAIL_MOBILE)

        if not self.is_front() and not self.is_back() and not self.is_mobile():
            send_mail_queue.delay(from_email, email_list, self.MAIL_SUBJECT, self.MAIL_GENERIC)

    # TODO: Fazer um teste unitário com mock
    def save(self, form):

        name = form.cleaned_data['name']
        mail = form.cleaned_data['mail']

        recruitment = Recruitment(name=name, mail=mail)
        recruitment.save()

        for competency in RecruitmentService().get_skills():
            comp_form_name = ('comp_' + competency).lower()
            skill = Skills(recruitment=recruitment, name=competency, value=form.cleaned_data[comp_form_name])
            skill.save()

            self.values[competency] = skill.value

        self.send_mails([mail])