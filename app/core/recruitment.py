# coding: utf-8


class Recruitment():

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

    @staticmethod
    def _has_minimal_skills(skills, values):
        if all(keys in values for keys in skills):
            for item in skills:
                if values[item] < 7:
                    return False
            return True
        return False

    def is_front(self, values):
        skills = (self.CSS, self.HTML, self.JAVASCRIPT)
        return self._has_minimal_skills(skills, values)

    def is_back(self, values):
        skills = (self.PYTHON, self.DJANGO)
        return self._has_minimal_skills(skills, values)

    def is_mobile(self, values):
        skills = (self.IOS, self.ANDROID)
        return self._has_minimal_skills(skills, values)

    def send_mail(self, data=None):
        print 'f'


# • Caso o candidato tenha entre 7 e 10 pontos para Html, CSS e Javascript deverá ser enviado o "Email Front-End";
# • Caso o candidato tenha entre 7 e 10 pontos para Python e Django deverá ser enviado o "Email Back-End”;
# • Caso o candidato tenha entre 7 e 10 pontos para desenvolvimento iOS ou Android deverá ser enviado o "Email Mobile”;
# • Caso ele atinja mais de um dos critérios acima deverá ser enviado um email para cada um dos critérios que ele passou;
# • Caso ele não entre em nenhum dos critérios acima deverá ser enviado o “Email Genérico”.