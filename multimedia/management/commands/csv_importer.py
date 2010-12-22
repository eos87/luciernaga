from django.core.management.base import BaseCommand, CommandError
from django.db.models import get_model
from csv_utf8 import *
import os

class Command(BaseCommand):

    help = "Whatever you want to print here"

    def handle(self, **options):
        run()
        #try:
            #validando si existe la app
            
        #except:
            #raise CommandError('The app or model doesn\'t exist :(')
