#!/bin/bash
sleep 120
cd /usr/src/app ; composer install; php /usr/src/app/bin/console doctrine:schema:create ; echo "yes"|php /usr/src/app/bin/console doctrine:fixtures:load && php /usr/src/app/bin/console assets:install
echo "[Log] Done"
php-fpm -D
while true; do sleep 1000; done
