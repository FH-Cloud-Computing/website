<div class="download">
<a href="#"><button>Watch Video 🎬</button></a>
</div>

<h1>Grafana</h1>

[Grafana](https://grafana.com/) is a common way to visualize information from multiple source systems, including [Prometheus](/exercises/4-prometheus). It offers a user friendly way to create graphs, alters, and display metrics.

## Running Grafana

Like Prometheus before, Grafana can be run in a container:

```
docker run -d \
  -p 3000:3000 \
  grafana/grafana
```

This will launch Grafana on port 3000 of your node.

## Setting up Grafana with Prometheus

