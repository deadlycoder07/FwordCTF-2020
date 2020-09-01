FROM ubuntu:19.04
RUN sed -i -e 's|disco|eoan|g' /etc/apt/sources.list
RUN apt-get -y upgrade && apt-get update && apt-get -y install nginx --no-install-recommends
RUN apt-get -y install python3 python3-pip
COPY docker/bot/nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log
RUN mkdir -p /opt/initializer
RUN mkdir -p /opt/initializer/app
COPY docker/bot/phantomjs /usr/bin/phantomjs
RUN chmod 755 /usr/bin/phantomjs
COPY ./BotApi /opt/initializer/app/
COPY docker/bot/requirements.txt docker/bot/start.sh /opt/initializer/
WORKDIR /opt/initializer
RUN chmod +x start.sh
RUN pip3 install -r requirements.txt
RUN chown -R www-data:www-data /opt/initializer/
EXPOSE 80
CMD ["/opt/initializer/start.sh"]
