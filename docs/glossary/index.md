title: Glossary

## API

Application Program Interfaces are methods for programs to exchange data without the involvement of humans. APIs often involve a schematic description of how the data looks like and where it needs to be sent. Today many APIs are based on [HTTP](#HTTP).

## Container

Containers are discussed in [lecture 4](../lectures/4-containers/index.md) and provide a way to package an application with its runtime requirement in a self-contained manner. Containers also provide limited security isolation.

## Container Orchestrator

A container orchestrator is responsible for managing containers across multiple virtual or physical servers. When a server fails or a container crashes the orchestrator is responsible for scheduling the container on a different server. Some orchestrators also manage integration with the cloud. Orchestrators are discussed in [lecture 4](../lectures/4-containers/index.md)

## CDN

A content delivery network replicates content across the globe to bring the content closer to the end user. CDNs are discussed in [lecture 3](../lectures/3-xaas/index.md).

## DBaaS

Databases as a Service are discussed in [lecture 3](../lectures/3-xaas/index.md) providing managed databases to a cloud customer without needing to manage a server, or the database system.

## Docker

[Docker](https://docker.com) is one of the earliest modern containerization systems. Docker was largely responsible for promoting the immutable infrastructure concept in containers.

Docker also contains the Docker Swarm orchestrator, a very simple system to manage containers across multiple machines. 

Docker is discussed in [lecture 4](../lectures/4-containers/index.md) and [exercise 3](../exercises/3-containers/index.md).

## FaaS

Functions as a Service are a concept discussed in [lecture 3](../lectures/3-xaas/index.md) that allow a developer to run program code without needing to manage a server or a runtime environment.

## Grafana

Grafana is an open source graphing dashboard. It is discussed in [exercise 5](../exercises/5-grafana/index.md).

## HTTP

The Hypertext Transfer Protocol is the protocol that powers the world wide web allowing for the easy up- and download of data. With HTTP each file (resource) has a unique URL on a server and can be linked.

## IaaS

Infrastructure as a Service is discussed in [lecture 2](../lectures/2-iaas/index.md) and provides virtual machines and related services to cloud customers.

## Istio

[Istio](https://istio.io/) is a service mesh used in conjunction with Kubernetes to facilitate microservices. Istio is discussed in [lecture 5](../lectures/5-cloud-native/index.md)

## Kubernetes

[Kubernetes](https://kubernetes.io) is an advanced, and thus complex container orchestrator. It not only manages containers, it also contains a large number of cloud integrations for storage, networking, load balancers, autoscaling, and more. Kubernetes is discussed in [lecture 4](../lectures/4-containers/index.md)

## Load balancer

Load balancers provide either network or application level traffic distribution across multiple servers. They are discussed in [lecture 2](../lectures/2-iaas/index.md) and [lecture 3](../lectures/3-xaas/index.md)

## Microservices

Microservices are a concept discussed in [lecture 5](../lectures/5-cloud-native/index.md) for creating multiple small applications working together across the network.

## PaaS

Platform as a Service is a collection of services discussed in [lecture 3](../lectures/3-xaas/index.md) that give a developer the ability to deploy an application without needing to manage IaaS servers.

## Prometheus

Prometheus is an open source, cloud native metrics collection system (time series database). It is discussed in [lecture 5](../lectures/5-cloud-native/index.md) and [exercise 4](../exercises/4-prometheus/index.md).

## Rack

A closet with standardized mounts for servers.

## Router

A network device that forwards layer 3 (IP) packets between separate networks.

## Switch

A network device that forwards Ethernet frames (packets) between devices. It does not perform layer 3 (IP) routing.