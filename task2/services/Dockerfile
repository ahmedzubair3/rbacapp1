FROM ubuntu:22.04

RUN apt-get update && apt-get install -y openssh-server sudo && \
    mkdir /var/run/sshd && \
    echo "root:root" | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
