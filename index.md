---
layout: default
title: Home
---

{% include lab_title.html %}
Welcome to [Collaborative Intelligence Systems Lab](https://cisl.ucr.edu/) (CISL) at the [University of California, Riverside](https://www.ucr.edu/)!

Our lab invents collaborative intelligence in the networked cyber-physical systems. 
We build and deploy end-to-end cooperative autonomy that bridges robot/edge/cloud/human intelligence to achieve novel collective capabilities not previously demonstrated. 
Our enthusiasm lies in tackling real-world problems across various domains ranging from autonomous vehicles, drones, home robots, AR/VR/XR devices, to generic edge ML systems, intelligent infrastructure.
Our interdisciplinary innovation addresses the system challenges in networking, vision, robotics, machine learning, and edge computing. 

*We are always looking for motivated talents to [join us](joinus).* 

<hr>
#### Hiring for Fall 2026:

We are hiring from both **ECE** and **CSE** department, in the following areas.
* Vehicular/Robotic Networks, Edge Computing
* ML Systems, Systems for ML


<hr>



#### Recent News:

{% assign news = site.data.news | sort : "date" | reverse %}
<ul>
  {% assign recent_count = 0 %}
  {% for item in news %}
    {% if recent_count < 10 %}
      <li>{{ item.date | date: "%b %Y"}}:
        <em>{{ item.title | markdownify | remove: '<p>' | remove: '</p>'}}</em>
      </li>
    {% endif %}
    {% assign recent_count = recent_count | plus: 1 %}
  {% endfor %}
</ul>

{% assign news = site.data.news | sort : "date" | reverse %}
<details>
  <summary>Previous Updates</summary>
  <ul>
    {% assign recent_count = 0 %}
    {% for item in news %}
      {% if recent_count >= 10 %}
        <li>{{ item.date | date: "%b %Y"}}:
          <em>{{ item.title | markdownify | remove: '<p>' | remove: '</p>'}}</em>
        </li>
      {% endif %}
      {% assign recent_count = recent_count | plus: 1 %}
    {% endfor %}
  </ul>
</details>


<hr>
{% include sponsor.html %}