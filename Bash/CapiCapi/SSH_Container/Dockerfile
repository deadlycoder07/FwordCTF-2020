FROM ubuntu:19.10
RUN sed -i -e 's|disco|eoan|g' /etc/apt/sources.list
RUN apt-get upgrade
RUN apt-get update
RUN apt-get install -y figlet
RUN apt-get -y install openssh-server docker.io sudo
RUN mkdir -p /run/sshd
RUN rm /etc/legal
RUN rm /etc/ssh/sshd_config
RUN chmod -x /etc/update-motd.d/*
COPY SSH_Container/welcome /etc/update-motd.d/
RUN chmod +x /etc/update-motd.d/welcome
COPY SSH_Container//sshd_config /etc/ssh/
COPY SSH_Container/banner /opt/
COPY SSH_Container/manage.sh /opt/
RUN rm /etc/sudoers
COPY SSH_Container/sudoers /etc/
RUN useradd -d /home/ctf/ -m -p FwordxKahla -s /opt/manage.sh ctf
RUN echo "ctf:FwordxKahla" | chpasswd
RUN service ssh reload
WORKDIR /home/ctf
RUN chown -R root:root /home/ctf
COPY SSH_Container/start.sh /opt/
CMD /opt/start.sh

#Add this option when launching container -v /var/run/docker.sock:/var/run/docker.sock
