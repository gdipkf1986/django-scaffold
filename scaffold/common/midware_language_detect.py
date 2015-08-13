__author__ = 'Jovi'

import logging
from scaffold import settings
from django.utils import translation

cookie_name = 'django_language'
langReg = r'(?P<lang>(en\-PH|en\-MY|en|zh\-TW|zh\-CN|vi|id|th))'


class LanguageMiddleware(object):
    """
    Detect the user's browser language settings and activate the language.
    If the default language is not supported, try secondary options.  If none of the
    user's languages are supported, then do nothing.
    """

    def is_supported_language(self, language_code):
        supported_languages = dict(settings.LANGUAGES).keys()
        return language_code in supported_languages

    def get_browser_language(self, request):
        browser_language_code = request.META.get('HTTP_ACCEPT_LANGUAGE', None)
        if browser_language_code is not None:
            logging.info('HTTP_ACCEPT_LANGUAGE: %s' % browser_language_code)
            languages = [language for language in browser_language_code.split(',') if '=' not in language]
            for language in languages:
                language_code = language.split('-')[0]
                if self.is_supported_language(language_code):
                    return language_code
                else:
                    logging.info('Unsupported language found: %s' % language_code)
                    return 'en'

    def process_request(self, request):
        if 'l' in request.GET:
            language_code = request.GET['l']
        elif cookie_name in request.COOKIES.keys() and request.COOKIES.get(cookie_name) != 'None':
            language_code = request.COOKIES.get(cookie_name)
        elif cookie_name in request.session.keys():
            language_code = request.session.get(cookie_name)
        else:
            language_code = self.get_browser_language(request)

        if language_code:
            request.session[cookie_name] = language_code
            translation.activate(language_code)

    def process_response(self, request, response):
        cookie = request.COOKIES.get(cookie_name,False)
        if not cookie or cookie != request.session.get(cookie_name):
            try:
                response.set_cookie(cookie_name, request.session.get(cookie_name))
            except Exception as e:
                logging.error(e)
        return response
