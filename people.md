---
layout: page 
title: People
---

<div class="clearfix">

<h2>Principal Investigator</h2>
<br>
{% for people in site.data.team %} 
    {% if people.type == "PI" %} 
        {% include avatar_entry.html %} 
    {% endif %} 
{% endfor %}
</div>

<br>

<div class="clearfix">
<h2>Graduate Students</h2>
<br>
{% for people in site.data.team %} 
    {% if people.type == "PHD" %} 
        {% include avatar_entry.html %}        
    {% endif %} 
{% endfor %}
{% for people in site.data.team %} 
    {% if people.type == "Grad" %} 
        {% include avatar_entry.html %}        
    {% endif %} 
{% endfor %}
</div>

<br>

<div class="clearfix">
<h2>Undergraduate Students</h2>
<br>
{% for people in site.data.team %}
    {% if people.type == "Undergrad" %}
        {% include avatar_entry.html %}        
    {% endif %}
{% endfor %}
</div>
