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
    <div class="platform">
    <img src="{{ site.baseurl }}/assets/platform/{{p.avatar}}" alt="Avatar" class="rectplatform">
        <a href="{{p.web}}">{{p.name}}</a>
    </div>
{% endif %}
{% endfor %}

{% for p in platform %}
{% if p.type == "device" %} 
    <div class="platform">
    <img src="{{ site.baseurl }}/assets/platform/{{p.avatar}}" alt="Avatar" class="rectplatform">
        <a href="{{p.web}}">{{p.name}}</a>
    </div>
{% endif %}
{% endfor %}

{% for p in platform %}
{% if p.type == "env" %} 
    <div class="platform">
    <img src="{{ site.baseurl }}/assets/platform/{{p.avatar}}" alt="Avatar" class="rectplatform">
        <a href="{{p.web}}">{{p.name}}</a>
    </div>
{% endif %}
{% endfor %}
</div>
