---
layout: page 
title: Research
---

{% include video_rotator.html %}

{% assign videos = site.data.videos | sample: 4 %}
<div class="video-wall">
  {% for vid in videos %}
  <div class="video-card">
    <video autoplay loop muted playsinline>
      <source src="{{ vid.file }}" type="video/mp4">
    </video>
    <p class="caption">{{ vid.caption }}</p>
  </div>
  {% endfor %}
</div>


### Select Media Coverage

<br>

<div class="media-wrapper">
{% for media in site.data.media %}
  {% include media_entry.html media=media %}
{% endfor %}
</div>



### Cooperative Autonomy
<div class="researchimg">
<img class="center" src="{{ site.baseurl }}/assets/imgs/avr.png">
</div>

* **Cooperative Perception.** Autonomous vehicles use 3D sensors (*e.g.* LiDAR, camera, RADAR) to sense the environment.
However, these 3D sensors only provide *line-of-sight (LoS)* perception and obstacles can often occlude their field-of-view (FoV).
Cooperative perception enables sensor sharing in real time, leveraging additional vantage points to build extended view beyond occlusion and sensing range.
Collaborating with [General Motors](https://patents.google.com/patent/US10109198B2/en), our award-winning work [Augmented Vehicular Reality (AVR)]({{ site.baseurl }}/publication/#:~:text=AVR)
first demonstrates the feasibility with an end-to-end prototype. 
[AutoCast]({{ site.baseurl }}/publication/#:~:text=AutoCast) 
then solves the network bottleneck to enable cooperative perception at scale, delivering augmented view to every vehicle on demand.   

<div class="clearfix"></div>

<div class="researchimg">
<img class="center" src="{{ site.baseurl }}/assets/imgs/carmap.png">
</div>

* **Self-healing Map, Map-less Robots.**
High-definition Map (HDMap) has been a crucial component for fine-grained localization. Collecting this map can be tedious and expensive. 
What exacerbates the problem is its vulnerability to changes (*e.g.* construction, road closures) in safety-critical applications.
Self-healing map aims to detect those changes and update the map in near-real time. 
Map-less robots targets onboard mapping and navigation without any prior knowledge of the world. 
Partnering with [General Motors](https://patents.google.com/patent/US11313696B2/en), our work [CarMap]({{ site.baseurl }}/publication/#:~:text=CarMap) takes a crowdsourcing approach, 
and creates a lightweight map change representation for fast broadcasting, while being feature-rich for robust localization. 

<div class="clearfix"></div>

<div class="researchimg">
<video muted autoplay loop width="100%">
<source src="{{ site.baseurl }}/assets/videos/CoopernautDemo.mp4" type="video/mp4">
</video>
</div>

* **Cooperative Driving, End-to-end Driving.** With cooperative perception, the next question is how to effectively leverage shared information to make better driving decisions.
What data is most critical to influence decisions, what kind of representation for that data should be used, how to design the interface to accept that representation. 
Our [Coopernaut]({{ site.baseurl }}/publication/#:~:text=Coopernaut) takes a holistic approach, enabling end-to-end training with shared sparse point features, 
which can be broadcasted to all nearby vehicles and swiftly transformed into different perspectives. 

<div class="clearfix"></div>

### Edge ML System

<div class="researchimg">
<img class="center" src="{{ site.baseurl }}/assets/imgs/mlexray.png">
</div>

* **Edge MLOps, Deployment, Monitoring, Update.** 
Robot intelligence powered by Edge ML is the core component of collaborative intelligence. 
Recent years have seen a shift of these models from serving on the cloud to being deployed on the actual edge devices, 
to enable low-latency, low-power, privacy-sensitive applications (*e.g.* autonomous cars, personal assistants, ads recommendation).
More often than not, however, the real-world performance can be below expectation, and there lacks the proper tooling to understand why.
One key solution is to apply Machine Learning Operations (MLOps) to edge robots, developing a series of peripheral systems around deployment, monitoring, and model retrain and update.
Collaborating with [Google](https://www.google.com/) and [New Relic](https://kubernetesonedgedayeu22.sched.com/event/zsA2/mlexray-observability-for-machine-learning-on-the-edge-michelle-nguyen-stanford), our award-winning work [ML-Exray]({{ site.baseurl }}/publication/#:~:text=ML%2D-,EXray) offers such a framework, provides visibility into layer-level details of edge ML execution, 
enabling debugging, monitoring, and potential automated loop of retrain and deployment (CI/CD).

<div class="clearfix"></div>


<div class="researchimg">
<img class="center" src="{{ site.baseurl }}/assets/imgs/mcal.jpg">
</div>

* **Data, Auto-labeling, Active Learning.**
*"Data is the new code."* Advanced intelligence is data hungry. Collaborative intelligence is no exception. 
Therefore it is critical to deal with cost reduction in the development and maintenance of edge ML systems.
In collaboration with [Microsoft Research](https://www.microsoft.com/en-us/research/), we first built [Satyam](https://researchsatyam.wordpress.com/), 
a scalable annotation platform on top of azure functions, which was 
partially integrated into Azure Labeling Service. Our follow-up work [MCAL]({{ site.baseurl }}/publication/#:~:text=MCAL) brings machine labeling in the loop,
further reducing data labeling cost for machine vision. 

<div class="clearfix"></div>
