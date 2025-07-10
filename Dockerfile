FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install necessary system packages and services
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    net-tools \
    procps \
    sudo \
    apache2 \
    rabbitmq-server \
    postgresql \
    build-essential \
    && apt-get clean

# Create non-root user
RUN useradd -m -s /bin/bash rbcuser && \
    echo "rbcuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Switch to rbcuser temporarily to install uv
USER rbcuser

# Set environment path for uv
ENV PATH="/home/rbcuser/.cargo/bin:$PATH"

# Install uv under rbcuser's home
RUN curl -Ls https://astral.sh/uv/install.sh | bash

# Switch back to root to copy app files and set ownership
USER root

# Copy project files and set permissions
COPY . .
RUN chown -R rbcuser:rbcuser /app

# Switch to rbcuser to install Python dependencies using uv
USER rbcuser

# Expose Flask app port
EXPOSE 5000

# Run services as root, app as rbcuser
USER rbcuser
# ENTRYPOINT ["bash", "-c", "sudo service apache2 start && sudo service rabbitmq-server start && sudo service postgresql start && python app.py"]

# Make sure it's executable
RUN chmod +x entrypoint.sh

# Use the entrypoint script
ENTRYPOINT ["./entrypoint.sh"]