---
layout: page
title: Teaching
---

## Teaching

<ul>
{% for course in site.data.teaching %}{% unless course.role %}<li>{{ course.term }}: <a href="{{ course.url }}">{{ course.name }}</a></li>
{% endunless %}{% endfor %}
</ul>

Before UCR

<ul>
{% for course in site.data.teaching %}{% if course.role %}<li>{{ course.term }}: {{ course.role }}, <a href="{{ course.url }}">{{ course.name }}</a>, Instructor: {{ course.instructor }}</li>
{% endif %}{% endfor %}
</ul>
