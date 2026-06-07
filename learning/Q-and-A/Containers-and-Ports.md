# Containers & Networking Q&A

## 1. What are containers?
Containers are lightweight, standalone, executable packages that include everything needed to run a piece of software, including the code, runtime, system tools, system libraries, and settings. They isolate software from its environment and ensure that it works uniformly despite differences between development and staging.

## 2. How does a server work (e.g., MongoDB)?
A database server like MongoDB runs as a persistent background process (daemon). It listens for incoming network requests on a specific port (default 27017). When a client connects, the server processes queries, manages data storage on disk, and returns results.

## 3. What is the sense of using Podman and what does it provide?
Podman is a daemonless container engine for developing, managing, and running OCI Containers on your Linux System. 
- **Daemonless:** Unlike Docker, it doesn't require a background process with root privileges, making it more secure.
- **Rootless:** It can run containers without root access.
- **Pods:** It can group containers into "Pods" (similar to Kubernetes) that share network resources.

## 4. What is port forwarding and what does it mean deep down?
Port forwarding (or port mapping) is the process of redirection a communication request from one address and port number combination to another.
- **Deep Down:** It involves the host's networking stack (NAT - Network Address Translation) intercepting packets destined for a host port and rerouting them to the container's internal IP and port.

## 5. What are ports and who controls them?
A port is a logical construct that identifies a specific process or service.
- **Range:** 0 to 65535.
- **Control:** The Operating System's kernel controls ports. A process must "bind" to a port to listen for traffic.

## 6. Why do websites run on ports?
Websites (HTTP/HTTPS) use ports (80/443) so the OS knows which application should receive the incoming web traffic. Without ports, a computer wouldn't know if a packet is for the web server, the mail server, or a database.

## 7. How does port forwarding enable hackers and how does a firewall protect?
- **Risk:** Port forwarding opens a "door" from the internet to your internal service. If that service (e.g., MongoDB) is unauthenticated or has vulnerabilities, a hacker can access it directly.
- **Firewall:** A firewall acts as a gatekeeper, inspecting incoming packets and only allowing those that match specific rules (e.g., only allowing certain IP addresses to access port 22).

## 8. How are containers made and how do they work within the OS?
- **Made from:** Images (layers of file system changes).
- **Internals:** They use Linux kernel features:
    - **Namespaces:** Isolate what the container can *see* (Process IDs, Network, Mount points).
    - **Cgroups:** Limit what the container can *use* (CPU, Memory).
