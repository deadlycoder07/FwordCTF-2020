FROM ubuntu:19.04
RUN sed -i -e 's|disco|eoan|g' /etc/apt/sources.list
ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get -y upgrade && apt-get update && apt-get -y install nginx --no-install-recommends
RUN apt-get -y install python3 python3-pip git-all
COPY docker/nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log
RUN mkdir -p /opt/initializer
RUN mkdir -p /opt/initializer/app
RUN export OAUTHLIB_INSECURE_TRANSPORT=1
COPY ./task /opt/initializer/app/
COPY docker/requirements.txt docker/start.sh /opt/initializer/
COPY docker/flag.txt /
WORKDIR /opt/initializer
RUN chmod +x start.sh
RUN pip3 install -r requirements.txt
RUN chown -R www-data:www-data /opt/initializer/
EXPOSE 80
CMD ["/opt/initializer/start.sh"]
