Django simple counters
====

Usage:
-----

add to INSTALLED_APPS:

```
INSTALLED_APPS = [
   ...
   'simple_counters',
   ...
]
```

In html template:

```
{% load simple_counters %}

{% yandex_simple_counter YANDEX_COUNTER_ID %}
```
