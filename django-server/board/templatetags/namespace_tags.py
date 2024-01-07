from django import template

register = template.Library()


@register.simple_tag
def namespaced_url(namespace, viewname):
    return f'{namespace}:{viewname}'
