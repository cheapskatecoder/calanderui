from django.db import models


class DqDatafile(models.Model):
    dq_datafile_id = models.AutoField(db_column='DQ_DATAFILE_ID', primary_key=True) # Field name made lowercase.
    data_file_name = models.CharField(db_column='DATA_FILE_NAME', max_length=150, blank=True, null=True) # Field name made lowercase.
    data_file_type = models.CharField(db_column='DATA_FILE_TYPE', max_length=50, blank=True, null=True) # Field name made lowercase.
    data_file_contact = models.CharField(db_column='DATA_FILE_CONTACT', max_length=75, blank=True, null=True) # Field name made lowercase.
    contact_email = models.CharField(db_column='CONTACT_EMAIL', max_length=150, blank=True, null=True) # Field name made lowercase.
    file_source = models.CharField(db_column='FILE_SOURCE', max_length=50, blank=True, null=True) # Field name made lowercase.
    cadence = models.CharField(db_column='CADENCE', max_length=50, blank=True, null=True) # Field name made lowercase.
    recurs_on_weekday = models.CharField(db_column='RECURS_ON_WEEKDAY', max_length=50, blank=True, null=True) # Field name made lowercase.
    first_or_last = models.CharField(db_column='FIRST_OR_LAST', max_length=10, blank=True, null=True) # Field name made lowercase.
    file_format = models.CharField(db_column='FILE_FORMAT', max_length=50, blank=True, null=True) # Field name made lowercase.
    file_naming_convention = models.CharField(db_column='FILE_NAMING_CONVENTION', max_length=200, blank=True, null=True) # Field name made lowercase.
    comments = models.TextField(db_column='COMMENTS', blank=True, null=True) # Field name made lowercase.
    active_yn = models.CharField(db_column='ACTIVE_YN', max_length=1, blank=True, null=True) # Field name made lowercase.