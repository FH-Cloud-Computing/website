<div class="download">
<a href="fh-cloud-computing-lecture-3-xaas.pptx"><button>Download PPTX 💻</button></a>
<a href="fh-cloud-computing-lecture-3-xaas.mp3"><button>Download MP3 🎧</button></a>
<a href="fh-cloud-computing-lecture-3-xaas.m4b"><button>Download M4B 🎧</button></a>
<a href="#"><button>Watch Video 🎬</button></a>
</div>

<h1>Beyond IaaS</h1>

This lecture walks you through the most important services offered by cloud providers beyond the IaaS layers. Sometimes this is called "PaaS" (Platform as a Service) indicating that it is intended as a developer platform.

The easiest way to remember the difference is that IaaS offers virtual machines and connected services. In order to operate on top of an IaaS platform you need someone skilled in running an operating system. In other words, you need a system administrator.

PaaS on the other hand is intended for developers. The platform services, on the other hand, are intended for developers. The main goal of PaaS services is enabling developers to deploy applications without having to manage the operating system of the underlying virtual machine.

There is, however, nothing preventing you from mixing IaaS and PaaS services. A typical use case would be using a managed database with virtual machines. This helps smaller teams because operating a database proficiently on a small scale can be an undue burden.

This might not seem like a big deal but consider that databases store data. Every time when data storage is concerned disaster recovery becomes more complex. If an IaaS team were to operate a database themselves they would need to regularly test backups and disaster recovery procedures. Managed databases take that complexity away.

Similarly, building a redundant database system that can perform an automatic failover requires a high skill level in managing that specific database engine. This skill level may not be available in small teams, or a small team may not want to spend time on managing the database instead of focusing on their core objective.

## Application load balancers

Application load balancers provide load balancing capabilities on [layer 7 of the OSI-model](https://en.wikipedia.org/wiki/OSI_model). In practice application load balancers on offer support [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) and HTTPS load balancing.

HTTP is a request-response protocol. Typically connections are short-lived but longer connections (e.g. with [Websockets](https://en.wikipedia.org/wiki/WebSocket)) are also possible. Good application load balancers allow sending traffic to a different set of backends based on the host name (`example.com`) as well as the path (`/some/address`).

Some applications also require that subsequent requests from the same client end up on the same backend. This is called session stickiness and can be achieved in a variety of ways. Less advanced solutions route requests based on the source IP, while more advanced versions send a so-called [cookie](https://en.wikipedia.org/wiki/HTTP_cookie) to the client and route subsequent requests based on that cookie.

![An illustration on how sessions work. On the first request the browser sends a login request. The server accesses a database to store the identifying information for the session. The server sends back the session ID in a HTTP cookie to the browser. On the next request the browser sends the previously received cookie to the server. The server fetches the previously stored information from the database so the server knows which user corresponds to the session.](sessions.svg)

Sticky sessions, however, present a problem: when a backend goes down the users of that backend will be redistributed to other backends. In practice this usually means that users will be logged out. When a cascading fault, or a rolling update occurs that takes down multiple backends in rapid succession users can be subjected to multiple involuntary logouts.

This has an adverse effect on user experience which is why newer, so-called &ldquo;cloud native&rdquo; applications don't use sticky sessions. Instead, cloud native applications put client-specific data (e.g. [session data](https://en.wikipedia.org/wiki/Session_(computer_science)#HTTP_session_token)) in database systems with redundancy. Sessions themselves [have their own race condition problems](https://pasztor.at/blog/stop-using-php-sessions/), but that is not a discussion for this lecture.

## CDNs

## Object Storage

### Cold storage

## Databases as a Service (DBaaS)

### Relational databases (SQL)

### Document databases

### Time Series databases

## Functions as a Service (FaaS / Lambda)

## Containers as a Service (CaaS)

## Stream processing

## Deployment pipelines
