# Introduction to the cloud

As the popular saying goes:

> The cloud is just somebody else's computer.

There is no magic, just using the cloud does not magically solve problems we are having with a traditional
infrastructure. This section will teach you how a cloud is built and what the typical services are that they offer as
well as the pitfalls which may come with such setups.

## What is a Server?

!!! tldr "In a hurry?"
    **Servers:**
    
    - Redundant, hot-swap hardware (power supply, fans, etc)
    - Flat build profile for rack mounts
    - Out-Of-Bounds management interface for monitoring and remote management

In older times, servers were completely different from the machines we used for regular work. Not just in weight and
form factor, but in architecture. The landscape would stretch from [SPARC](https://en.wikipedia.org/wiki/SPARC) and
[Power](https://en.wikipedia.org/wiki/IBM_POWER_microprocessors) architectures to the x86 architecture we use in our
PCs.

Over time, however, the x86 architecture took over to the point where a server today, from an architectural standpoint,
is exactly the same as the machine you are using right now. This means that you can copy the machine you are using onto
a server and chances are it will run without any modification.

The only notable exception is the rise of the ARM architecture which is popular in phones and tables and is known for 
its low power consumption. In recent years there has been a small but noticeable trend to run ARM in a datacenter.

At home it may not matter if your computer uses 200 or 300 watts of power. In a datacenter, at the scale of 
hundreds, thousands or tens of thousands of servers, saving even a few percent of power will translate to huge cost
savings.

The difference in build is, however, quite apparent. While some servers, mainly built for office use, have the standard
&ldquo;tower&rdquo; build, most servers have a flat profile designed to be mounted in racks as displayed on the picture.
Since most servers are not high enough to take full size expansion cards (graphics cards, network cards, etc), servers
may contain a separate removable component for these usually called a riser. 

![A server in a rack, pulled out and the top taken off. The internal components, such as dual, hot-plug power supply units, hot-plug fans, CPU, the riser and hot-swap disks are visible.](/lectures/1-cloud-intro/server-01.svg)
*An HP Proliant G5 server pulled out of its rack. Source: [Wikipedia](https://en.wikipedia.org/wiki/ProLiant#/media/File:Proliant380g5_3.jpeg)*

Server racks are standardized closets that have mounting screws for rails that allow pulling servers out even mid
operation and replace components while the server is running.

Servers also come with a high level of redundancy. While you may have a single power supply in your home computer,
servers typically have two that are able to take power from different power inputs. This makes sure that the server 
keeps running even if one of the two power supplies fail, or if one of the two power inputs goes down.

Also in contrast to your home setup these servers contain an Out-Of-Bounds Management interface that allows remote
management of servers even when they are turned off. The hardware components built into the server report their health
status to this OOB management interface which allows the simultaneous monitoring of thousands of machines.

!!! note
    This is a fairly generic description of servers. Different vendors may chose to leave out certain features of their
    more &ldquo;budget&rdquo; line of servers, or call certain components differently. HP, for example, calls their
    OOBM &ldquo;Integrated Lights Out&rdquo;, Dell &ldquo;DRAC - Dell Remote Access Control&rdquo;, etc.

## The Anatomy of a Datacenter

!!! tldr "In a hurry?"
    **Datacenter components:**
    
    - Racks to house servers
    - Larger customers have cages for their racks
    - Cabling under the floor
    - Redundant cooling, fire suppression systems and power supply
    - Eco friendliness is becoming a factor
    - Some datacenters provide internet connectivity

Since the cloud is just somebody else's computer, that computer needs to be hosted somewhere. Servers are almost
exclusively hosted in datacenters. Let's take a look at what is involved in running a datacenter.

First of all, as mentioned above, most servers are going to be rack-mounted so you need a bunch of racks. These racks
are installed in rows, often with a fake floor to allow for cabling to go under the floor.

![A data center containing a bunch of racks for servers](/lectures/1-cloud-intro/datacenter.jpg)
*A datacenter with racks. Source: [Wikipedia](https://en.wikipedia.org/wiki/Data_center#/media/File:Datacenter_de_ARSAT.jpg)*

Since servers produce a lot of heat, a datacenter also requires cooling. There are a variety of ways to solve cooling,
some are more &ldquo;green&rdquo; than others. Some datacenters, for example, opt to install a &ldquo;cold aisles&rdquo;
where the cold air is pumped between two rack rows and is pushed through the racks to cool the servers.

Apart from cooling, datacenters also require automated fire suppression systems simply because of the amount of
electricity going through. Datacenters usually go with a non-destructive fire suppression system such as lowering the 
oxygen content of the air enough to stop the fire.

All critical systems in a datacenter (power, cooling, fire suppression systems) are usually built in a redundant fashion
because the loss of either of those systems will potentially mean a complete shutdown for the datacenter. Datacenter 
operators usually have further contingency plans in place, too, such as a UPS (battery) system, diesel generator, fuel 
truck on standby, hotline to the fire department, etc. to make sure the datacenter can keep its required uptime.

On the networking side of things, matters get slightly more complicated. Some datacenter providers also offer you the
ability to use their network uplink (also redundant), but larger customers will prefer to host their own networking
equipment and negotiate their own internet uplink contracts. Since there is no generic rule for how datacenters handle
this, we will dispense with a description.

It is also worth noting that larger customers (banks, cloud providers, etc) usually prefer to have their own racks in
a separated gated area called a &ldquo;cage&rdquo; to which they control access.

## The Anatomy of the Internet

!!! tldr "In a hurry?"
    **Internet:**
    
    - IP ranges are advertised using BGP
    - Providers connect direcly or using internet exchanges
    - 16 global providers form the backbone of the internet (tier 1)

Once the physical infrastructure is set up there is also the question of how to connect to the Internet. As mentioned
before, networks can be very complicated and there is no one size fits all solution. Smaller customers will typically
use the network infrastructure provided by the datacenter while larger customers will host their own network equipment.

![A diagram showing a typical datacenter networking setup.](/lectures/1-cloud-intro/datacenter-cabling.svg)

Again, generally speaking racks will be equipped with a Top-of-Rack switch to provide
[layer 2 (Ethernet)](https://en.wikipedia.org/wiki/Data_link_layer) connectivity between servers. Several ToR may have
interconnects between each other and are usually connected to one or more routers. Routers provide
[layer 3 (IP)](https://en.wikipedia.org/wiki/Network_layer) routing to other customers in the same datacenter,
[internet exchange](https://en.wikipedia.org/wiki/Internet_exchange_point), or may be connected via dedicated fiber to
another provider.

!!! note
    If you are not familiar with computer networks we recommend giving the
    [Geek University CCNA course a quick read](https://geek-university.com/ccna/computer-network-explained/).
    While you will not need everything, you **will** have to understand how IP addresses, netmasks, etc work in order to
    pass this course. 

Providers on the internet exchange data about which network they are hosting using the
[Border Gateway Protocol](https://en.wikipedia.org/wiki/Border_Gateway_Protocol). Each provider's router announces the
IP address ranges they are hosting to their peer providers, who in turn forward these announcements in an aggregated
form to other providers.

Providers have agreements with each other, or with an Internet Exchange, about exchanging a certain amount of traffic.
These agreements may be paid if the traffic is very asymmetric or one provider is larger than the other. Alternatively
providers can come to an arrangement to exchange traffic for free. Internet exchanges facilitate the exchange between
many providers for a modest fee allowing cost-effective exchange of data. Depending on the exchange the rules are 
different. Local exchanges, for example, may only allow advertising local (in-country) addresses, while others are built
for a specific purpose.

Generally speaking providers can be classified into 3 categories. Tier 1 providers are the global players that are 
present on every continent. They form the backbone of the Internet. At the time of writing there are
[16 such networks](https://en.wikipedia.org/wiki/Tier_1_network). Tier 2 are the providers who are directly connected
to the tier 1 providers, while tier 3 is everyone else.

![An illustration of how internet providers are connected. In this example Global A and Global B are two providers which are connected in the same level, Local A and Local B are connected to Global A, while Local C is connected to Global B. Local A and Local B also exchange data directly and Local B and C exchange data over a local internet exchange. The example datacenter customer is connected to Local B.](/lectures/1-cloud-intro/internet-tiers.svg)

## Software stack

!!! tldr "In a hurry?"
    **Software stack:**
    
    - Virtualization
    - Operating system
    - Application runtime
    - Application

The purpose of all this is, of course, to run an application. Each server hosts an operating system which is 
responsible for managing the hardware. Operating systems provide a simplified API for applications to do
hardware-related operations such as dealing with files or talking to the network. This part of the operating system is
called the kernel. Other parts form the userland. The userland includes user applications such as a logging software.
Specifically on Linux and Unix systems the userland also contains a package manager used to install other software.

Modern x86 server CPUs (and some desktop CPUs) also have a number of features that help with virtualization.
Virtualization lets the server administrator run multiple guest operating systems efficiently and share the
server resources between them.

!!! tip "Did you know?"
    You can find out if an Intel CPU supports hardware virtualization by looking for the `VT-x` feature on the
    [Intel ARK](https://ark.intel.com/content/www/us/en/ark.html#@Processors). Unfortunately AMD does not have an easy
    to use list but you can look for the `AMD-V` feature on AMD CPUs.

!!! note "Note"
    Virtualization is different from containerization (which we will talk about later) in that with virtualization each
    guest operating system has its own kernel whereas containers share a kernel between them.
    
    ![](/lectures/1-cloud-intro/virtualization-containers.svg)

There is one more important aspect of finally getting an application to run: the runtime environment. Except for a few
rare occasions applications need a runtime environment. If the application is compiled to machine code they still need
so-called shared libraries. Shared libraries are common across multiple applications and can be installed and
updated independently from the application itself. This makes for a more efficient update process, but also means
that the right set of libraries need to be installed for applications.

If the applications are written higher level languages like Java, Javascript, PHP, etc. they need the appropriate
runtime environment for that language.

One notable exception to the runtime environment requirement is the programming language [Go](https://golang.org/). Go
compiles everything normally located in libraries into a single binary along with the application. This makes it
exceptionally simple to deploy Go applications into containers.

## The Cloud

!!! tldr "In a hurry?"
    **Typical cloud features:**
    
    - API
    - Dynamic scaling
    - Can be classified into IaaS, PaaS and SaaS

All of the previously discussed things were available before the &ldquo;cloud&rdquo;. You could pay a provider to 
give you access to a virtual machine where you could run your applications. What changed with the cloud, however, is
the fact that you no longer had to write a support ticket for changed and everything became self service.

The cloud age started with an infamous e-mail from [Jeff Bezos](https://en.wikipedia.org/wiki/Jeff_Bezos) to his
engineers in 2002 forcing them to use APIs to exchange data between teams. The exact e-mail is no longer available but
it went along these lines:

> 1) All teams will henceforth expose their data and functionality through service interfaces.
> 
> 2) Teams must communicate with each other through these interfaces.
>
> 3) There will be no other form of interprocess communication allowed: no direct linking, no direct reads of another
> team’s data store, no shared-memory model, no back-doors whatsoever. The only communication allowed is via service
> interface calls over the network.
> 
> 4) It doesn’t matter what technology is used. HTTP, Corba, Pubsub, custom protocols — doesn’t matter.
> 
> 5) All service interfaces, without exception, must be designed from the ground up to be externalizable. That is to
> say, the team must plan and design to be able to expose the interface to developers in the outside world. No exceptions.
>
> 6) Anyone who doesn’t do this will be fired.

This marked the beginning of Amazon Web Services the first and also the most successful public cloud offering. The first
public release of AWS was in 2004 with SQS their message queue service, and got completely overhauled in 2006 where the
Elastic Compute (EC2) and the Simple Storage Service (S3) service made its first public appearance.

The APIs provided by cloud providers allow for a large amount of flexibility. If new servers are needed they can be
launched within a few minutes. If there are too many servers they can be deleted. The same goes for other services: 
with the API (and the appropriate billing model) comes flexibility to adapt to change.

The other factor that makes it easy to adapt to change is of course the fact that these services are managed. The 
cloud customer doesn't need to hire a team of engineers to build a database service, for example, it can be consumed
without knowing how exactly the database is set up. 

Generally speaking, cloud services can be classified into three categories: Infrastructure as a Service (IaaS) providing
virtual machines and network infrastructure, Platform as a Service (PaaS) offering services for developers to use, and
Software as a Service (SaaS) offering end-user services.

![A comparison of different cloud models. With self-managed the customer needs to take care of the application, runtime, operating, system, virtualization, hardware, network, power, cooling, fire suppression, and housing. With IaaS onl the application, runtime, and the operating system. With PaaS the customer only takes care of the application. With SaaS the customer takes care of nothing and only consumes the service.](/lectures/1-cloud-intro/cloud-comparison.svg) 

## Business Models



## Private vs. Public cloud

!!! tldr "In a hurry?"
    **Private cloud:**
    
    - Hosted on-premises or in the public cloud using only private connections
    - Large cloud providers offer their services &ldquo;in a box&rdquo; to host yourself

## Managed Services

!!! tldr "In a hurry?"
    **Managed services:**
    
    - Low entry cost
    - Little in-house know-how required
    - Vendor lock-in
    - If problems arise they are hard to debug

## Benefits

## Drawbacks

## Regulations


