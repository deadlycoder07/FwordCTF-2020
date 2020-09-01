FROM ubuntu:19.10
RUN sed -i -e 's|disco|eoan|g' /etc/apt/sources.list
RUN apt-get upgrade
RUN apt-get update
RUN apt-get install -y figlet
RUN apt-get -y install openssh-server 
RUN mkdir -p /run/sshd
RUN rm /etc/legal
RUN rm /etc/ssh/sshd_config
RUN chmod -x /etc/update-motd.d/*
COPY 01-custom /etc/update-motd.d/
RUN chmod +x /etc/update-motd.d/01-custom
COPY sshd_config /etc/ssh/
COPY banner /opt/
COPY jail.sh /opt/
COPY start.sh /opt/
RUN useradd -d /home/ctf/ -m -p FwordxKahla -s /opt/jail.sh ctf
RUN echo "ctf:FwordxKahla" | chpasswd
RUN service ssh reload
WORKDIR /home/ctf
COPY taskFword.sh .
RUN chown -R root:root /home/ctf
RUN service ssh restart
CMD /opt/start.sh
