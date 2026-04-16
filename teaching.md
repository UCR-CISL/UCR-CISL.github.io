---
layout: page
title: Teaching
---

## Teaching

<ul>
{% for course in site.data.teaching_auto %}{% unless course.role %}<li>{{ course.term }}: <a href="{{ course.url }}">{{ course.title }}</a></li>
{% endunless %}{% endfor %}
</ul>

Before UCR

<ul>
{% for course in site.data.teaching_auto %}{% if course.role %}<li>{{ course.term }}: {{ course.role }}, <a href="{{ course.url }}">{{ course.title }}</a>, Instructor: {{ course.instructor }}</li>
{% endif %}{% endfor %}
</ul>
