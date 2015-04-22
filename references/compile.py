__author__ = 'Jovi'
# compile less/css, generate responsive css sprit, compact css,scripts

import os

import tinycss


BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# todo: css sprit


def css_sprit():
    """
    generate css sprite
    0. get static paths
    1. find all css from static folders
    2. parse css
    3. compact all pics
    4. generate css file
    """
    parser = tinycss.make_parser('page3')
    for f in get_css_files():
        stylesheet = parser.parse_stylesheet_file(f)
        for ruleSet in stylesheet.rules:
            for d in ruleSet.declarations:
                if 'background' not in d.name:
                    continue
                for t in d.value:
                    if t.type != 'URI':
                        continue
                    print t.type+":"+t.value


def get_css_files():
    folder = os.path.join(BASEDIR, 'etc', 'static', 'styles')
    return [os.path.join(folder, f) for f in os.listdir(folder) if
            os.path.isfile(os.path.join(folder, f)) and f.endswith('.css')]


css_sprit()