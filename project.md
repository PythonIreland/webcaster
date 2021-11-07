# Goal

Having several screens in key locations of the venue, we want to be able to display messages on them.
Typically the talk currently running in a room, the next one, general messages, lost and found, photo carousels, videos looping ...
We want an affordable solution, independent of the venue's network availability or quality.


# Proposed solution

We need to own the network infrastructure, it could be a mesh based on asus routers or other vendors, 
or a simple wifi based on a raspberry pi. 
It’s likely we’ll need powerline ethernet adapters, entry level should be plenty enough.

Using raspberry pi, have a webcaster that serves the content, and a collection of display node clients that will 
connect to that network to access information.
Server and client can be on the same code repo.

The webcaster will manage the content displayed by the display nodes, 
it can be a flask or django app.
The slaves will drive chrome to display the content, a flask or fastAPI will do nicely.

![](comm.png "Comm")

# Features

- Build deck with something like [reveal.js](https://revealjs.com/) ? 
  it’s been there a long time, and has a gazillion [plugins](https://github.com/hakimel/reveal.js/wiki/Plugins,-Tools-and-Hardware). 
- Assign deck to display node
- Show grid of what clients are displaying at the moment (screen cap)
- Name node after their location (Lobby, Room 1, Workshop 1st floor ...)
- manage screen groups (all display the same)

# Notes

https://www.yodeck.com/raspberry-pi/ seems based on a similar idea, but cloud based.
Being able to be internet independent is primordial.

# Deliverables

An essential artefact is a step-by-step user guide to deploy the solution, 
we want our successors or other organisations to be able to leverage our efforts and contribute to it.

Controller app + user manual

The solution must work without any form of internet access, in pure LAN.
