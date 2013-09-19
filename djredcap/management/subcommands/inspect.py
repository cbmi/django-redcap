import os
import csv
import json
import keyword
import sys
import re
import inflect
import djredcap
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

field_types = {
    'date_ymd': 'DateField',
    'number': 'FloatField',
    'integer': 'IntegerField',
    'email': 'EmailField',
    'text': 'CharField',
    'textarea': 'TextField',
    'calc': 'FloatField',
    'radio': 'CharField',
    'select': 'CharField',
    'checkbox': 'CharField',
    'yesno': 'BooleanField',
    'truefalse': 'BooleanField',
}


class Command(BaseCommand):
    help = """Attempts to read a REDCap data dictionary (CSV) and output a
    matching JSON file. Then attempts to read a JSON file and output matching
    Django models. Can take either a REDCap CSV file or a json
    file as input."""
    requires_model_validation = False
    db_module = 'django.db'
    args = 'filename'

    def handle(self, fileName=None, *args, **options):
        if not fileName:
            raise CommandError('Enter a filename')

        fin = open(fileName,'rU')
        dialect = csv.Sniffer().sniff(fin.read(1024))
        fin.seek(0)
        reader = csv.DictReader(fin, fieldnames=header_keys, dialect=dialect)

        reader.next()
        if fileName.find('.json') == -1:
            fileName = djredcap.csv_2_json(self, reader, fileName)
        djredcap.json_2_dj(self, fileName)
