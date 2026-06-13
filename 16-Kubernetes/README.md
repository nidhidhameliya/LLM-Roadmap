# Kubernetes (K8s)

## Core Concepts
- **Pods:** The smallest deployable units, containing one or more containers.
- **Deployments:** Manages replica sets and scaling of Pods. If a Pod crashes, the Deployment spins up a new one.
- **Services:** Provides a stable IP address and load balancing to a set of Pods.
- **ConfigMaps & Secrets:** Managing environment variables and API keys securely, separate from the Docker image.
