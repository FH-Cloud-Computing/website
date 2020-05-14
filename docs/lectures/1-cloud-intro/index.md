# Introduction to the cloud

As the popular saying goes:

> The cloud is just somebody else's computer.

There is no magic, just using the cloud does not magically solve problems we are having with a traditional
infrastructure. This section will teach you how a cloud is built and what the typical services are that they offer, as
well as the pitfalls which may come with such setups.

## What is a Server?

In older times servers were completely different from the machines we used for regular work. Not just in weight and
form-factor, but in architecture. The landscape would stretch from [SPARC](https://en.wikipedia.org/wiki/SPARC) and
[Power](https://en.wikipedia.org/wiki/IBM_POWER_microprocessors) architectures to the x86 architecture we use in our
PCs.

Over time, however, the x86 architecture took over to the point where today a server, from an architectural standpoint
is exactly the same as the machine you are using right now. This means that you can copy the machine you are using onto
a server and chances are it will run without any modification.

The only notable exception is the rise of the ARM architecture which is popular in phones and tables and is known for 
its low power consumption. In recent years there has been a small but noticeable trend to run ARM in a datacenter.

While at home it may not matter if your computer uses 200 or 300 watts of power, in a datacenter, at the scale of 
hundreds, thousands or tens of thousands of servers saving even a few percent of power will translate to huge cost
savings.

The difference in build is, however, quite apparent. While some servers, mainly built for office use, have the standard
&ldquo;tower&rdquo; build, most servers have a flat profile designed to be mounted in racks as displayed on the picture.
Since most servers are not high enough to take full size expansion cards (graphics cards, network cards, etc) servers
may contain a separate removable component for these usually called a riser. 

![A server in a rack, pulled out and the top taken off. The internal components, such as dual, hot-plug power supply units, hot-plug fans, CPU, the riser and hot-swap disks are visible.](/lectures/1-cloud-intro/server-01.svg)
*An HP Proliant G5 server pulled out of its rack. Source: [Wikipedia](https://en.wikipedia.org/wiki/ProLiant#/media/File:Proliant380g5_3.jpeg)*

Server racks are standardized closets that have mounting screws for rails that allow pulling servers out even mid
operating and replace components while the server is running.

Servers also come with a high level of redundancy. While you may have a single power supply in your home computer
server typically have two that are able to take power from different power inputs. This makes sure that the server 
keeps running even if one of the two power supplies fail, or if one of the two power inputs goes down.

Also in contrast to your home setup these servers contain an Out-Of-Bounds Management interface that allows remote
management of servers even when they are turned off. The hardware components built into the server report their health
status to this OOB management interface which allows the simultaneous monitoring of thousands of machines.

!!! note
    This is a fairly generic description of servers. Different vendors may chose to leave out certain features of their
    more &ldquo;budget&rdquo; line-up of servers, or call certain components differently. HP, for example, calls their
    OOBM &ldquo;Integrated Lights Out&rdquo;, Dell &ldquo;DRAC - Dell Remote Access Control&rdquo;, etc.

## The Anatomy of a Datacenter

Since the cloud is just somebody else's computer that computer needs to be hosted somewhere. Servers are almost
exclusively hosted in datacenters. Let's take a look at what is involved in running a datacenter.

First of all, as mentioned above, most servers are going to be rack mounted so you need a bunch or racks. These racks
are installed in a row fashion, often with a fake floor to allow for cabling to go under the floor.

![A data center containing a bunch of racks for servers](/lectures/1-cloud-intro/datacenter.jpg)
*A datacenter with racks. Source: [Wikipedia](https://en.wikipedia.org/wiki/Data_center#/media/File:Datacenter_de_ARSAT.jpg)*

Since servers produce a lot of heat a datacenter also requires cooling. There are a variety of ways to solve cooling,
some are more &ldquo;green&rdquo; than others. Some datacenters, for example, opt to install a &ldquo;cold aisle&rdquo;
where the cold air is pumped between two rack rows and is pushed through the racks to cool the servers.

Other than cooling datacenters also require automated fire suppression systems simply because of the amount of
electricity going through. Datacenters usually go with a non-destructive fire suppression system such as lowering the 
oxygen content of the air enough to stop the fire.

All critical systems in a datacenter (power, cooling, fire suppression systems) are usually built in a redundant fashion
because the loss of either of those systems will potentially mean a complete shutdown for the datacenter. Datacenter 
operators usually have further contingency plans in place too, such as a UPS (battery) system, disel generator, fuel 
truck on standby, hotline to the fire department, etc. to make sure the datacenter can keep its required uptime.

On the networking side of things matters get slightly more complicated. Some datacenter providers also offer you the
ability to use their network uplink (also redundant), but larger customers will prefer to host their own networking
equipment and negotiate their own internet uplink contracts. Since there is no generic rule for how datacenters handle
this we will dispense with a description.

It is also worth noting that larger customers (banks, cloud providers, etc) usually prefer to have their own racks in
a separated gated are called a &ldquo;cage&rdquo; to which they control access.

## The Anatomy of the Internet

Once the physical infrastructure is set up there is also the question of how to connect the Internet. As mentioned
before networks can be very complicated and there is no one size fits all solution. Smaller customers will typically
use the network infrastructure provided by the datacenter, while larger customers will host their own network equipment.

![A diagram showing a typical datacenter networking setup.](/lectures/1-cloud-intro/datacenter-cabling.svg)

Again, generally speaking racks will be equipped with a Top-of-Rack switch to provide
[layer 2 (Ethernet)](https://en.wikipedia.org/wiki/Data_link_layer) connectivity between servers. Several ToR may have
interconnects between each other and are usually connected to one or more routers. Routers provide
[layer 3 (IP)](https://en.wikipedia.org/wiki/Network_layer) routing to other customers in the same datacenter,
[internet exchange](https://en.wikipedia.org/wiki/Internet_exchange_point), or may be connected to dedicated fiber to
another provider.

!!! note
    If you are not familiar with computer networks we recommend giving the
    [Geek University CCNA course a quick read](https://geek-university.com/ccna/computer-network-explained/).
    While you will not need everything, you **will** have to understand how IP addresses, netmasks, etc work in order to
    pass this course. 

Providers on the internet exchange data about which network they are hosting using the
[Border Gateway Protocol](https://en.wikipedia.org/wiki/Border_Gateway_Protocol). Each providers router announces the
IP address ranges they are hosting to their peer providers, who in turn forward these announcements in an aggregated
form to other providers.

TBD explain tiers

![An illustration of how internet providers are connected. In this example Global A and Global B are two providers who are connected in the same level, Local A and Local B are connected to Global A, while Local C is connected to Global B. Local A and Local B also exchange data directly and Local B and C exchange data over a local internet exchange. The example datacenter customer is connected to Local B.](/lectures/1-cloud-intro/internet-tiers.svg)


