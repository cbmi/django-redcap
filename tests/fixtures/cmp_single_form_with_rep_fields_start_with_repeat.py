from django.db import models

class Record(models.Model):

    class Meta:
	 db_table = 'record'


class PriorGeneticTesting(models.Model):
    whole_mito_sequencing_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of whole mitochondrial genome sequencing', blank=True)
    whole_mito_sequencing_loc = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where whole mitochondrial genome sequencing was performed', blank=True)
    dc_mutation_gene = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Gene in which disease causing mutation was located on whole mitochondrial sequencing', blank=True)
    dc_mutation_mdna_level = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Change at mDNA level for disease causing mutation on whole mitochondrial sequencing', blank=True)
    vus_mdna_level = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Change at mDNA level for variant of unknown significance on whole mitochondrial sequencing', blank=True)
    whole_mito_sequencing_sample_summary = models.CharField(help_text=u'1, blood | 2, urine | 3, muscle | 4, saliva | 5, other', null=True, max_length=2000, verbose_name=u'Sample type for whole mitochondrial genome sequencing', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'priorgenetictesting'


class wholemitosequencingsample(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Sample type for whole mitochondrial genome sequencing', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Sample type for whole mitochondrial genome sequencing', blank=True, choices=[(1, u'blood'), (2, u'urine'), (3, u'muscle'), (4, u'saliva'), (5, u'other')]) # This field type is a guess
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'wholemitosequencingsample'


