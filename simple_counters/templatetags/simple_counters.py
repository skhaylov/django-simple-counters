# coding=utf-8;

from django import template


register = template.Library()


@register.inclusion_tag('simple_counters/yandex.html')
def yandex_simple_counter(counter_id):
    return {'YANDEX_COUNTER_ID': counter_id}
