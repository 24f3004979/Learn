# SSH & Protocols Q&A

## 1. Telnet protocol of communication
Telnet is an old network protocol used on the Internet or local area network to provide a bidirectional interactive text-oriented communication facility using a virtual terminal connection. Unlike SSH, Telnet is **unencrypted**, meaning passwords and data are sent in plain text.

## 2. Connection Layer
In the context of SSH, the connection layer provides a variety of services, including interactive login sessions, remote execution of commands, and forwarded TCP/IP and X11 connections. It runs on top of the SSH Transport and Authentication layers.

## 3. What is the concept of a Tunnel and Connection?
- **Connection:** A persistent communication path between two points.
- **Tunnel:** Wrapping one protocol inside another. An SSH tunnel allows you to send unencrypted traffic through an encrypted SSH connection (e.g., accessing a local database remotely).

## 4. How does a basic communication protocol work?
It involves:
- **Handshake:** Agreeing on how to talk (version, encryption).
- **Payload:** The actual data being sent.
- **Acknowledgment:** Confirming the data was received.
- **Termination:** Closing the connection gracefully.
