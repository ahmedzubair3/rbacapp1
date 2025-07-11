# Project Setup and Usage Guide

This document provides instructions for setting up, running, and managing the project.

---

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed
- [Make](https://www.gnu.org/software/make/) installed

---

## Task 1: Start the Application

To start the application, run:

```sh
make up
```

Once the containers are running, verify the service is healthy by visiting:

```
http://localhost:5000/healthcheck
```

---

## Task 2: Additional Setup

Navigate to the `task2` directory for a similar but independent setup. This folder contains its own Docker-based environment and a dedicated README with helpful commands and instructions.

---

## Task 3: Run Task 3

To execute Task 3, use:

```sh
make run_task3
```

---

## Output and Logs

- All generated outputs are stored in the `./data` directory.
- Logs are available in the `./logs` directory.

---

## Cleanup

To stop and remove all containers and associated resources, run:

```sh
make down
```

---

For further details, refer to the individual README files in each task directory.