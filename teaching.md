---
layout: page
title: Teaching
---

## Teaching

<ul>
{% for course in site.data.teaching_auto %}{% unless course.role %}<li>{{ course.addendum }}: <a href="{{ course.url }}">{{ course.title }}</a></li>
{% endunless %}{% endfor %}
</ul>

Before UCR

<ul>
{% for course in site.data.teaching_auto %}{% if course.role %}<li>{{ course.addendum }}: {{ course.role }}, <a href="{{ course.url }}">{{ course.title }}</a>, Instructor: {{ course.instructor }}</li>
{% endif %}{% endfor %}
</ul>
