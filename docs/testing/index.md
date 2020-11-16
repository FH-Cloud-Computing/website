Tests will be conducted starting in December 2020. The exam will last 120 minute and consist of a multiple choice
test.

During the test you will be required to obey the following rules:

- Have an empty room with no disturbances.
- Close all other applications except for the single browser window the test runs in.
- Remove all electronic devices and notes from your desk and person. No phones, no smartwatches of any kind are allowed.
- Unless medically required no food is allowed during the test and only clear liquids in clear, unlabeled containers
  are allowed. No mugs, no coke, etc.
- During the test you will not be allowed to talk.
- You will be required to turn on your camera the entire time during the test. You will also be required to show that
  your environment suits the criteria described above.
- You may be required to turn on your screen sharing during the entire test.

## What will be asked in the test?

**This is a non-exhaustive list.** Use it as a learning guide to be better prepared for the test. Remember: if you don't know something, **ask**. That's what Slack is for.

### Fundamentals

As indicated in the first lecture you will need to demonstrate an understanding of computer networking to the level
that is required to configure a cloud environment:

- Protocols: Ethernet, IP, TCP, UDP, DNS, HTTP. Know everything that is required to create a firewall configuration.
- What is a server? What are the components of a server?
- Anatomy of the Internet: How does a packet get to its target and back?
- What are the components of a typical software stack?
- What makes a cloud a cloud? What differentiates it from a virtual machines offering?
- What classes of cloud providers are there? What's the difference?
- What are the typical use cases where cloud can be used for cost savings? What are the typical workload examples?
- What are the different cloud models based on access/customer patterns? Who do they offer service to?
- How does cloud automation work, what is the difference between the discussed tools, and why are they important?
- What regulation is relevant to the cloud? What are the rights and duties of each party?

### IaaS

- What are virtual machines? How do they differ from containers?
- What are the typical instance types cloud providers offer? What workloads are suitable for these instance types?
- How does automation work in the cloud?
- What are virtual machine pools?
- What storage models are on offer? How do they differ? What workloads are good for which storage type?
- What networking models are typically offered? How do you access the Internet? in each of these?
- What are security groups? How do they work? Know how to configure them properly for access from a specific IP range.
- What are network load balancers? What protocol(s) do they support and what differentiates them from application load balancers?
- What VPN and interconnect types do you know? How are they used? What are the pitfalls of each?
- What is DNS and how does a DNS service work? What are the advanced features some DNS providers offer?

### Beyond IaaS

- What are application load balancers and how do they differ from NLBs? Which layer do they work on and which protocol do they typically use?
- What is session stickyness? How does it work?
- What is a CDN? Why do you need one? What are the typical round trip times to the other side of the globe?
- What content is well suited for a CDN?
- What is an object storage? What is it good for? What is it not good for? Why?
- What is database consistency and why does it matter? What are the components of ACID and BASE? What do they mean?
- What is the CAP theorem? What does it say?
- What are relational databases? How do they differ from other database types? Can you name a few?
- What are key-value stores? Can you name a few? When would you use one?
- What are document databases? Can you name a few? When would you use one?
- What are time series databases? Can you name one? When would you use one?
- What are graph databases? Can you name one? When would you use one?
- What are functions as a service? When would you use one? Can you imagine an architecture that uses FaaS?

### Containers

- What is a container and how does it differ from a virtual machine?
- What provides isolation in case of a container? Can you name a few mechanisms?
- What are container images and how are they constructed? Which software popularized them and how are they standardized?
- What parts go into building a container?
- How is data storage solved in containers? How do you persist data?
- How do you deploy a container? What is immutable infrastructure?
- What is container orchestration and why do you need it? What is Kubernetes and what are the advantages and disadvantages over Docker Swarm.
- What is the basic networking model of containers? How can a network be extended over multiple hosts?
- Why do you need internal firewalls in a Kubernetes cluster?
- What are the components of deploying an application on Kubernetes? What is the difference between them?
- What are the core components of a Kubernetes cluster? What do they do?

### Cloud-native app development

- What is state in an application? Why is it a problem for scaling and how do you solve it?
- What are the 12 factors? Can you imagine how to put them into practice?
- How do you build a self-healing system with containers? What are the components that you need for it?
- What are feature tests? How do they work? 
- How does metrics collection work in practice?
- What is Prometheus? How can you integrate it into your application?
- How are logs typically collected? Can you name a log aggregator?
- Can you name a software that provides dashboards?
- What are the benefits and drawbacks of microservices? What are good and bad use cases for microservices? What is the circuit breaker pattern and why do you need it?
- What is Conway's Law?
- What are service meshes?
