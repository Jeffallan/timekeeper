# Time Tracker

Welcome to timetracker.

Timetracker is a mobile first web application designed to help general contractors and subcontractors manage their billing needs when access to a desktop computer is not practicable.

Timetracker is built with:

- [Docker](https://docs.docker.com/get-docker/).
- [Vue JS](https://vuejs.org/) (localhost:3000).
- [Django Rest Framework](https://www.django-rest-framework.org/) (localhost:8000).
- [Mailhog](https://github.com/mailhog/MailHog) for local email debugging (localhost:8025).



## Getting started

1) Make a copy of .modelENV, name it `.ENV`, and place it the the root directory of the project.

2) Navigate to the root directory of the project and issue the following command:

```bash
docker-compose up
```

3) Next view the containers running containers.
```bash
docker ps
```

4) Enter the web container and create the first superuser.
```bash
    docker exec -it timekeeper_web_1 /bin/sh
    python manage.py createsuperuser
```

5) If you create new users without using the `createsuperuser` command, navigate to localhost:8025 and and click on the activation email to activate the new user.

6) If you plan on developing this application further, creating a virtual environment for the Django Rest Framework is also recommended.
```
cd backend
python -m venv ENV
source ENV/bin/activate
```

## License
This software is licensed under the Apache 2.0 license.

Copyright 2021 Raven Security Associates, INC.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License [here](LICENSE.md)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.