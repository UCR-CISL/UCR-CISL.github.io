---
layout: page 
title: Platform
---

{% assign platform = site.data.platform | sort : "name" %}

<h2>Platform</h2>

<div class="clearfix">
<br>
{% for p in platform %}
{% if p.type == "vehicle" %} 
    <div class="avatar">
    <img src="{{ site.baseurl }}/assets/platform/{{p.avatar}}" alt="Avatar" class="rectavatar">
        <a href="{{p.web}}">{{p.name}}</a>
        <br><em>{{p.note}}</em>
    </div>
{% endif %}
{% endfor %}
</div>

<div class="clearfix">
<br>
{% for p in platform %}
{% if p.type == "device" %} 
    <div class="avatar">
    <img src="{{ site.baseurl }}/assets/platform/{{p.avatar}}" alt="Avatar" class="rectavatar">
        <a href="{{p.web}}">{{p.name}}</a>
        <br><em>{{p.note}}</em>
    </div>
{% endif %}
{% endfor %}
</div>

<div class="clearfix">
<br>
{% for p in platform %}
{% if p.type == "env" %} 
    <div class="avatar">
    <img src="{{ site.baseurl }}/assets/platform/{{p.avatar}}" alt="Avatar" class="rectavatar">
        <a href="{{p.web}}">{{p.name}}</a>
        <br><em>{{p.note}}</em>
    </div>
{% endif %}
{% endfor %}
</div>
