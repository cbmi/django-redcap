import os
import csv
import json
import keyword
import sys
import re
import inflect
from .djredcap import csv_2_json
from django.core.management.base import BaseCommand, CommandError

header_keys = (
    'field_name',
    'form_name',
    'section_name',
    'field_type',
    'field_label',
    'choices',
    'field_note',
    'validation_type',
    'min_value',
    'max_value',
    'is_identifier',
    'branching_logic',
    'required',
    'custom_alignment',
    'question_number'
)


class Command(BaseCommand):
    help = """Attempts to read a REDCap data dictionary (CSV) and output a
    matching JSON file. Then attempts to read a JSON file and output matching
    Django models. Can take either a REDCap CSV file or a json file as
    input."""
    requires_model_validation = False
    db_module = 'django.db'
    args = 'filename'

    def handle(self, file_name=None, *args, **options):
        if not file_name:
            raise CommandError('Enter a filename')
        fin = open(file_name, 'rU')
        dialect = csv.Sniffer().sniff(fin.read(1024))
        fin.seek(0)
        reader = csv.DictReader(fin, fieldnames=header_keys, dialect=dialect)
        reader.next()
        file_name = csv_2_json(self, reader, file_name)
