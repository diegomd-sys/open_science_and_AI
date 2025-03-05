FROM ubuntu:latest
 
RUN apt update && apt upgrade -y && apt install python3 -y && apt install python3-pip -y && apt install git -y && apt autoremove -y

RUN git clone https://github.com/diegomd-sys/open_science_and_AI.git

RUN pip3 install -r requirements.txt

WORKDIR /open_science_and_AI

CMD python3 word_cloud.py