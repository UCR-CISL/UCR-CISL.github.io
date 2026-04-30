---
layout: page 
title: Platform
---

{% assign platform = site.data.platform | sort : "name" %}

<h3 class="platform-section-title">Vehicles</h3>
<div class="platform-grid">
{% for p in platform %}
{% if p.type == "vehicle" %}
  <div class="platform-card">
    {% if p.web %}<a href="{{p.web}}" target="_blank">{% endif %}
    <img src="{{ site.baseurl }}/assets/platform/{{p.avatar}}" alt="{{ p.name }}" class="platform-card-img">
    <span class="platform-card-name">{{p.name}}</span>
    {% if p.web %}</a>{% endif %}
  </div>
{% endif %}
{% endfor %}
</div>

<h3 class="platform-section-title">Instruments</h3>
<div class="platform-grid">
{% for p in platform %}
{% if p.type == "device" %}
  <div class="platform-card">
    {% if p.web %}<a href="{{p.web}}" target="_blank">{% endif %}
    <img src="{{ site.baseurl }}/assets/platform/{{p.avatar}}" alt="{{ p.name }}" class="platform-card-img">
    <span class="platform-card-name">{{p.name}}</span>
    {% if p.web %}</a>{% endif %}
  </div>
{% endif %}
{% endfor %}
</div>

<h3 class="platform-section-title">Environments</h3>
<div class="platform-grid">
{% for p in platform %}
{% if p.type == "env" %}
  <div class="platform-card">
    {% if p.web %}<a href="{{p.web}}" target="_blank">{% endif %}
    <img src="{{ site.baseurl }}/assets/platform/{{p.avatar}}" alt="{{ p.name }}" class="platform-card-img">
    <span class="platform-card-name">{{p.name}}</span>
    {% if p.web %}</a>{% endif %}
  </div>
{% endif %}
{% endfor %}
</div>
