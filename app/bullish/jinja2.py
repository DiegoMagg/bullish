from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


def environment(**kwargs):
    env = Environment(**kwargs)
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env
