---
layout: page 
title: People
---

{% include lab_pic.html %}

{% assign team = site.data.team_auto | sort : "name" %}

<div class="clearfix">

<h2>Faculty</h2>
<br>
{% for people in team %} 
    {% if people.type == "PI" %} 
        {% include avatar_entry.html %} 
    {% endif %} 
{% endfor %}
</div>

<br>

<div class="clearfix">
<h2>Graduate Students</h2>
<br>
{% for people in team %} 
    {% if people.current and people.type == "PHD" %} 
        {% include avatar_entry.html %}        
    {% endif %} 
{% endfor %}
{% for people in team %} 
    {% if people.current and people.type == "MS" %} 
        {% include avatar_entry.html %}        
    {% endif %} 
{% endfor %}
</div>

<br>

<div class="clearfix">
<h2>Undergraduate Students</h2>
<br>
{% for people in team %}
    {% if people.current and people.type == "BS" %}
        {% include avatar_entry.html %}        
    {% endif %}
{% endfor %}
</div>

<div class="clearfix">
<h2>Visiting Students</h2>
<br>
{% for people in team %}
    {% if people.current and people.type == "Visitor" %}
        {% include avatar_entry.html %}        
    {% endif %}
{% endfor %}
</div>


{% assign alum = site.data.team_auto | sort : "year" | reverse %}

<div class="clearfix">
<h2>Alumni</h2>
{% for people in alum %}
    {% if people.current == false and people.type != "Visitor" %}
        {% include alumni_entry.html %}        
    {% endif %}
{% endfor %}
</div>

<br>

<div class="clearfix">
<h2>Past Visitors</h2>
{% for people in alum %}
    {% if people.current == false and people.type == "Visitor" %}
        {% include alumni_entry.html %}        
    {% endif %}
{% endfor %}
</div>
