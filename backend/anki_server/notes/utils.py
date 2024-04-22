import markdown as md
from django import template
from django.template.defaultfilters import stringfilter




import re

import bleach
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.functional import Promise

try:
    from django.utils.encoding import force_str  # noqa: Django>=4.x
except ImportError:
    from django.utils.encoding import force_text as force_str  # noqa: Django<=3.x

import markdown

from .settings import (
    ALLOWED_HTML_ATTRIBUTES,
    ALLOWED_HTML_TAGS,
    ALLOWED_URL_SCHEMES,

)


def markdownify(markdown_text):
    

    html = markdown.markdown(
        markdown_text,
        extensions=MARTOR_MARKDOWN_EXTENSIONS,
        extension_configs=MARTOR_MARKDOWN_EXTENSION_CONFIGS,
    )
    return bleach.clean(
        html,
        tags=ALLOWED_HTML_TAGS,
        attributes=ALLOWED_HTML_ATTRIBUTES,
        protocols=ALLOWED_URL_SCHEMES,
    )
