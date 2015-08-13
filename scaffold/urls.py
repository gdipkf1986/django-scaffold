from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
import re

# from django.contrib import admin
# admin.autodiscover()

langReg = r'(?P<lang>(en\-PH|en\-MY|en|zh\-TW|zh\-CN|zh\-SG|zh|vi|id|th))'


class CovertPathToParam(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        real_url = re.sub(r'^/' + langReg, '', self.request.path_info)
        lang = re.sub(r'/$', '', kwargs.get("lang"))
        if not real_url:
            return_url = '/?l=' + lang
        elif '?' in real_url:
            return_url = real_url + '&l=' + lang
        else:
            return_url = real_url + '?l=' + lang
        return return_url


urlpatterns = patterns(
    '',
    url(r'^' + langReg + r'/', CovertPathToParam.as_view()),
    url(r'^m/', include('scaffold.apps.mobile.urls')),
)
