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

![A server in a rack, pulled out and the top taken off. The internal components, such as dual, hot-plug power supply units, hot-plug fans, CPU, the riser and hot-swap disks are visible.](server-01.svg)

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
exclusively hosted in datacenters.