FROM ubuntu:22.04

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Create a non-root user
RUN apt-get update && \
    apt-get install -y sudo curl software-properties-common && \
    useradd -ms /bin/bash ansibleuser && \
    echo "ansibleuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Install Ansible
RUN apt-add-repository --yes --update ppa:ansible/ansible && \
    apt-get update && \
    apt-get install -y ansible && \
    apt-get clean

# Switch to non-root user
USER ansibleuser
WORKDIR /home/ansibleuser

CMD [ "bash" ]
