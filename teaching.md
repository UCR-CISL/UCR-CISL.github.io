---
layout: page
title: Teaching
---

## Teaching

<ul>
{% for course in site.data.teaching_auto %}{% unless course.type %}<li>{{ course.addendum }}: <a href="{{ course.url }}">{{ course.title }}</a></li>
{% endunless %}{% endfor %}
</ul>

Before UCR

<ul>
{% for course in site.data.teaching_auto %}{% if course.type %}<li>{{ course.addendum }}: {{ course.type }}, <a href="{{ course.url }}">{{ course.title }}</a>, Instructor: {{ course.instructor }}</li>
{% endif %}{% endfor %}
</ul>
