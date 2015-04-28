__author__ = 'Jovi'
# compile less/css, generate responsive css sprit, compact css,scripts

import os

import tinycss2
from PIL import Image


BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# todo: css sprit


def get_pics_from_css(css_files, static_root):
    pics = {}
    file_size = {}
    for f in css_files:
        print 'processing:', f
        css_content = tinycss2.parse_stylesheet(open(f, 'r').read(), skip_whitespace=True, skip_comments=True)
        for rule in css_content:
            if rule.type != 'qualified-rule':
                continue
            for token in rule.content:
                if token.type != 'url' or '?sprite' not in token.value:
                    continue
                pic_file = token.value.split("?sprite")
                if not pic_file[1]:
                    sprite_file = u"sprite"
                else:
                    sprite_file = pic_file[1].replace("=", "")
                if sprite_file not in pics:
                    pics[sprite_file] = []
                    file_size[sprite_file] = []
                if pic_file[0] not in pics[sprite_file]:
                    pics[sprite_file].append(pic_file[0])
                    path = pic_file[0].split('/')[2:]
                    image_path = os.path.join(static_root, *path)
                    image = Image.open(image_path, 'r')
                    file_size[sprite_file].append(image.size)
                    image.close()
    return file_size, pics


def make_sprite_pic(file_size, pics, static_root):
    sprite_offset = {}
    for (sprite_file, images) in pics.iteritems():
        if len(images) == 1:
            continue
        file_sizes = file_size[sprite_file]
        target_width = max(file_sizes, key=lambda s: s[0])[0]
        target_height = sum([s[1] for s in file_sizes])
        print sprite_file, target_width, target_height
        sprite = Image.new('RGBA', (target_width, target_height + (len(images) - 1) * 5),
                           color="rgba(255,255,255,0)")
        sprite_offset[sprite_file] = {}

        used_height = 0
        for image_path in images:
            abs_path = os.path.join(static_root, *(image_path.split('/')[2:]))
            if not os.path.exists(abs_path):
                print abs_path, ' is not existing, skip'
                continue
            image_open = Image.open(abs_path).convert('RGBA')
            width, height = image_open.size
            sprite.paste(image_open, (0, used_height), mask=image_open)
            image_open.close()
            sprite_offset[sprite_file][image_path] = {
                'background-position-x': 0,
                'background-position-y': str(100 * used_height / target_height) + '%',
                'background-size': str(100 * target_width / width) + '%',
                'width': str(width) + 'px',
                'height': str(height) + 'px',
            }
            used_height += image_open.size[1] + 5
        sprite.save(os.path.join(static_root, 'images', sprite_file + '.png'), 'PNG', optimize=False)
    return sprite_offset


def css_sprit():
    """
    generate css sprite
    0. get static paths
    1. find all css from static folders
    2. parse css
    3. compact all pics
    4. generate css sprite_file
    """
    static_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_root = os.path.join(static_root, 'etc', 'static')
    print static_root

    css_files = get_css_files()
    file_size, pics = get_pics_from_css(css_files, static_root)

    sprite_offset = make_sprite_pic(file_size, pics, static_root)

    for f in css_files:
        css_content = tinycss2.parse_stylesheet(open(f, 'r').read(), skip_whitespace=True, skip_comments=True)
        for rule in css_content:
            if rule.type != 'qualified-rule':
                continue
            for token in rule.content:
                if token.type != 'url' or '?sprite' not in token.value:
                    continue
                pic_file = token.value.split("?sprite")
                if not pic_file[1]:
                    sprite_file = u"sprite"
                else:
                    sprite_file = pic_file[1].replace("=", "")
                if (sprite_file not in sprite_offset.keys()) or (pic_file[0] not in sprite_offset[sprite_file]):
                    print sprite_file, 'or', pic_file[0], ' not found in sprite offset'
                    continue
                token.value = '/static/images/' + sprite_file + '.png'
        print f
        print tinycss2.serialize(css_content)

def convert_path():
    pass


def get_css_files():
    folder = os.path.join(BASEDIR, 'etc', 'static', 'styles')
    return [os.path.join(folder, f) for f in os.listdir(folder) if
            os.path.isfile(os.path.join(folder, f)) and f.endswith('.css')]


if __name__ == '__main__':
    # todo: get htmls from templates

    # todo: get css resources from html
    # todo: generate css sprit
    # todo: compact css
    css_sprit()

    # todo: get javascript resources
    # todo: javascript minify
    # todo: javascript compact, generate map.json

