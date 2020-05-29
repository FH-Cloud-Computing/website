Each sprint has a hard deadline. Sprints can be handed in earlier. If a deadline is missed the points are not awarded
and the solution is uploaded to GitHub so the next sprint can be accomplished.

## Sprint 1: Instance Pools

**Deadline:** 1<sup>st</sup> of October 2020 

In this sprint you must demonstrate your ability to set up an instance pool and a network load balancer.

**Pass criteria:** your webservice must answer on an IP address and balance traffic across all instances running in an
instance pool. The number of instances will be changed in the demonstration and your web service must adapt accordingly.

## Sprint 2: Monitoring

**Deadline:** 1<sup>st</sup> of November 2020

In this sprint you must demonstrate your ability to monitor a varying number of instances set up on an instance pool in
the previous sprint.

**Pass criteria:** Your monitoring instance must be set up with Prometheus and Grafana running.
Prometheus must track the instances in the instance pool using custom service discovery and collect their CPU usage
in a graph in Grafana.

## Sprint 3: Autoscaling

**Deadline:** 1<sup>st</sup> of December 2020

In this sprint you must demonstrate your ability to receive a webhook from Grafana and adjust the number of instances
in the instance pool from the previous sprint under load.

**Pass criteria:** Your service will be hit with a large number of requests and it must scale up as outlined in the 
[project work document](/projectwork).
