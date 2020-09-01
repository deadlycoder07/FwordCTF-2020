FROM ubuntu:19.10
RUN apt-get upgrade
RUN apt-get update
RUN apt-get install -y sudo libcap2-bin
RUN useradd -d /home/user1/ -m -p KahlaxFword -s /bin/bash user1
RUN echo "user1:KahlaxFword" | chpasswd
RUN chown root:user1 /home/user1/
WORKDIR /home/user1
COPY flag.txt .
RUN chmod 1775 /home/user1/
RUN chmod 740 /home/user1/flag.txt
RUN setcap CAP_DAC_READ_SEARCH+ep /usr/bin/tar
USER user1
CMD /bin/bash
