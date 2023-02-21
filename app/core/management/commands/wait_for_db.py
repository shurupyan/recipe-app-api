"""
Django command to wait for the db to be available.
"""
import time
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Django command to wait for the db to be available.
    """

    def handle(self, *args, **kwargs):
        """ Entrypoint for the command """
        self.stdout.write('Waiting for db to be available...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database is not available now. Waiting for 5 second...\n')
                time.sleep(5)

        self.stdout.write(self.style.SUCCESS('Database available!'))
