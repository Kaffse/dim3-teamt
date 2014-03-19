 #!/bin/bash

    set -eux

    pip install -r requirements.txt

    python manage.py syncdb

    python populate_script.py



    python manage.py runserver