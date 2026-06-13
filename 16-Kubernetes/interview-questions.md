# Interview Questions
**Q: What is the difference between a Deployment and a StatefulSet?**
A: Deployments manage stateless applications where any pod can be replaced by another. StatefulSets are used for stateful applications (like databases) requiring stable, persistent network identifiers and ordered deployment.

**Q: How do you securely pass an OpenAI API key to a container in K8s?**
A: Create a Kubernetes `Secret`. Then, in the Deployment YAML, map that Secret to an environment variable in the container spec. Never bake the key into the Docker image.
