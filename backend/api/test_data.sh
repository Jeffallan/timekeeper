#!/bin/bash

python manage.py gen_users && python manage.py gen_clients && python manage.py gen_locations && python manage.py gen_services && python manage.py gen_work