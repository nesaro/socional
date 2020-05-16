# Idea

An online notational velocity clone. A federated note system.

Each note can be :
 * private (just for you)
 * shared (with the people you trust)
 * public (with everybody)


# Modes


### Private note mode

exactly like notational velocity. You have your own set of notes and you can search through them

### Shared note mode

private + shared with you notes. Can be searched in the same way

### search note mode

public + private + shared


### Local news

Your notes sorted by time of creation/update

### Shared news

What people around you have created/changed

### Public news

shared news + public websites


# Nodes

A node is defined by a URL and posibly by a uuid. It runs a http server (possibly)

# Connection

Every node can manage which nodes does it trust or follow. 

## trust

That host is allowed to search through shared notes to your host. Trust might include some public-private key

## follow

That host is used for public searches . If they trust this node they will share their shared notes

# Protocol

## Search protocol

Can be either by text, date, or both
