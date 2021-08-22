from django.db import models
from viewflow.models import Process
import datetime

def get_crid():
    last_cr = CRProcess.objects.all().order_by('id').last()
    if not last_cr:
        return 'CR-'+datetime.date.today().strftime('%Y%m%d-')+'0001'
    cr_id = last_cr.orderid
    cr_index = int(cr_id[12:16])
    new_cr_index =  cr_index+1
    new_cr_id = 'CR-'+datetime.date.today().strftime('%Y%m%d-')+str(new_cr_index).zfill(4)
    return new_cr_id
class CRProcess(Process):
    orderid = models.CharField(max_length=32,default=get_crid,unique=True)
    title = models.CharField(max_length=256)
    vendors = [
        ('OC','OK Circuits'),
        ('DV','Denivern'),
    ]
    vendor = models.CharField(max_length=128,choices=vendors)
    product_names = [
        ('OC','OK Circuits'),
        ('DV','Denivern'),
    ]
    product_name = models.CharField(max_length=128,choices=product_names)
    severitys = [
        ('OC','OK Circuits'),
        ('DV','Denivern'),
    ]
    severity = models.CharField(max_length=128,choices=severitys)
    cr_types = [
        ('OC','OK Circuits'),
        ('DV','Denivern'),
    ]
    cr_type = models.CharField(max_length=128,choices=cr_types)
    affected_devices = [
        ('OC','OK Circuits'),
        ('DV','Denivern'),
    ]
    affected_device = models.CharField(max_length=128,choices=affected_devices)
    start_time = models.DateField()
    end_time = models.DateField()
    l1_approve = models.BooleanField(default=True)
    l2_approve = models.BooleanField(default=True)
