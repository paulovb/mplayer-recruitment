from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from api.handlers import RecruitmentHandler

urlpatterns = patterns('',
   # all my other url mappings
   # url(r'^api/recruitment/$',  Resource(RecruitmentHandler)),
    url(r'^recruitment/', Resource(RecruitmentHandler)),
)