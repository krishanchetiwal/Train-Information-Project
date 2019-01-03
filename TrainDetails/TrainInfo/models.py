from django.db import models

class Traindetails(models.Model):
    no = models.IntegerField(db_column='No', primary_key=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    seq = models.FloatField(db_column='SEQ', blank=True, null=True)
    stationcode = models.CharField(db_column='StationCode', max_length=255, blank=True, null=True)
    stationname = models.CharField(db_column='StationName', max_length=255, blank=True, null=True)
    arrivaltime = models.DateTimeField(db_column='ArrivalTime', blank=True, null=True)
    departuretime = models.DateTimeField(db_column='DepartureTime', blank=True, null=True)
    distance = models.IntegerField(db_column='Distance', blank=True, null=True)
    sourcestation = models.CharField(db_column='SourceStation', max_length=255, blank=True, null=True)
    sourcestationname = models.CharField(db_column='SourceStationName', max_length=255, blank=True, null=True)
    destinationstation = models.CharField(db_column='DestinationStation', max_length=255, blank=True, null=True)
    destinationstationname = models.CharField(db_column='DestinationStationName', max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'TrainDetails'

def __str__(self):
    return self.no
class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
