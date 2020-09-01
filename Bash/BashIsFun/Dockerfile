FROM ubuntu:19.10
RUN apt-get upgrade
RUN apt-get update
RUN apt-get install -y sudo figlet
RUN useradd -d /home/user1/ -m -p FworD1STh3BesTGuYs -s /bin/bash user1
RUN echo "user1:FworD1STh3BesTGuYs" | chpasswd
RUN useradd -d /home/user-privileged/ -m -p Fw0rd1SOuRPriD3_1mFedUpGuyS -s /bin/bash user-privileged
RUN echo "user-privileged:Fw0rd1SOuRPriD3_1mFedUpGuyS" | chpasswd
RUN chown root:user1 /home/user1/
COPY flag.txt /home/user1/
WORKDIR /home/user1
COPY welcome.sh .
COPY welcome.txt .
RUN chown root:user-privileged /home/user1/welcome.sh
RUN chmod 755 /home/user1/welcome.sh
RUN chmod 755 /home/user1/welcome.txt
RUN chmod 1775 /home/user1/
RUN chown root:user-privileged /home/user1/flag.txt
RUN chmod 740 /home/user1/flag.txt
RUN rm /etc/sudoers
COPY sudoers /etc/
USER user1
CMD /bin/bash
