# Interview Questions
**Q: Why use `python:slim` or `alpine` images for deployment?**
A: To reduce the image size and minimize the attack surface by excluding unnecessary operating system utilities and build tools.

**Q: What is the purpose of a Docker volume?**
A: Containers are ephemeral; any data written inside them is lost when they are removed. Volumes provide persistent storage on the host machine that survives container restarts (crucial for Vector DBs).
