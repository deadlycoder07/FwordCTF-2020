#!/bin/bash
echo -en "\n** It may take some time! We are preparing the environment for you! **\n\n" 
sudo /usr/bin/docker run -it --cap-add CAP_DAC_READ_SEARCH priv /bin/bash
exit
