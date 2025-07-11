# Task 2: Setup and Usage Guide

This document provides instructions for setting up, running, and managing the Task 2 environment.

---

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed
- [Make](https://www.gnu.org/software/make/) installed

---

## Common Commands

Below are useful commands for working with Task 2:

```sh
# Start the environment
make up

# Open a shell inside the container
make shell

# Start the environment and run setup
make up setup

# Run setup tasks
make setup

# Verify installation
make check=verify_install
make action CMD=verify_install
make action ACTION=verify_install

# Check service status
make action ACTION=check_status

# Check disk usage
make action ACTION=check_disk
```

---

## Health Check

After starting the environment, verify the service is healthy by visiting:

```
http://localhost:5000/healthcheck
```

---

## Cleanup

To stop and remove all containers and resources, run:

```sh
make down
```

---

## Output and Logs

- Outputs are stored in the `./data` directory.
- Logs are available in the `./logs` directory.

---