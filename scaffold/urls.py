from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
import re

# from django.contrib import admin
# admin.autodiscover()

langReg = r'(?P<lang>(en\-PH|en\-MY|en|zh-TW|vi|id|th))'


class covertPathToParam(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        real_url = re.sub(r'^/' + langReg, '', self.request.path_info)
        lang = re.sub(r'/$', '', kwargs.get("lang"))
        if not real_url:
            return_url = '/index?l=' + lang
        elif real_url.find('?'):
            return_url = real_url + '&l=' + lang
        else:
            return_url = real_url + '?l=' + lang
        return return_url


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'scaffold.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^admin/', include(admin.site.urls)),

                       url(r'^'+langReg+r'/', covertPathToParam.as_view()),
                       url(r'^myapp/', include('scaffold.apps.myapp.urls'))

                       )
