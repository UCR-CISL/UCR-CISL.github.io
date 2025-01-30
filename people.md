---
layout: page 
title: People
---

![Lab Outing 2024](assets/imgs/outing24.jpeg)

{% assign team = site.data.team | sort : "name" %}

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
    {% if people.type == "PHD" %} 
        {% include avatar_entry.html %}        
    {% endif %} 
{% endfor %}
{% for people in team %} 
    {% if people.type == "Grad" %} 
        {% include avatar_entry.html %}        
    {% endif %} 
{% endfor %}
</div>

<br>

<div class="clearfix">
<h2>Undergraduate Students</h2>
<br>
{% for people in team %}
    {% if people.type == "Undergrad" %}
        {% include avatar_entry.html %}        
    {% endif %}
{% endfor %}
</div>

<div class="clearfix">
<h2>Visiting Students</h2>
<br>
{% for people in team %}
    {% if people.type == "Visitor" %}
        {% include avatar_entry.html %}        
    {% endif %}
{% endfor %}
</div>


{% assign alum = site.data.team | sort : "year" %}

<div class="clearfix">
<h2>Alumni</h2>
<br>
{% for people in alum %}
    {% if people.type == "Alumni" %}
        {% include alumni_entry.html %}        
    {% endif %}
{% endfor %}
</div>

<div class="clearfix">
<h2>Past Visitors</h2>
<br>
{% for people in alum %}
    {% if people.type == "PastVisitor" %}
        {% include alumni_entry.html %}        
    {% endif %}
{% endfor %}
</div>