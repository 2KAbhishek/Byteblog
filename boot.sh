#!/bin/sh
source dev/bin/activate
while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo "Upgrade DB command failed, retrying in 5 secs..."
    sleep 5
done
exec gunicorn -b :5000 --access-logfile - --error-logfile - byteblog:app
