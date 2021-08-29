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
    orderid = models.CharField(max_length=32,default=get_crid,unique=True,verbose_name="Order ID")
    title = models.CharField(max_length=256)
    vendors = [
        ('OS','On-Site'),
        ('CL','Cloud'),
    ]
    vendor = models.CharField(max_length=128,choices=vendors)
    product_names = [
        ('CC','Cisco'),
        ('JP','Juniper'),
        ('AWS','AWS'),
        ('AZ','Azure'),
    ]
    product_name = models.CharField(max_length=128,choices=product_names,verbose_name="Product Name")
    severitys = [
        ('SD','Standard'),
        ('NM','Normal'),
        ('MJ','Major'),
        ('EM','Emergency'),
    ]
    severity = models.CharField(max_length=128,choices=severitys)
    cr_types = [
        ('FM','Fault Mgt'),
        ('PR','Preventive'),
        ('AD','Adaptive'),
        ('PF','Perfective'),
    ]
    cr_type = models.CharField(max_length=128,choices=cr_types,verbose_name="CR Type")
    # affected_devices = [
    #     ('OC','OK Circuits'),
    #     ('DV','Denivern'),
    # ]
    affected_device = models.CharField(max_length=128,verbose_name="Affected Device")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    approval_choices = [
        ('AP','Approve'),
        ('DN','Deny')
    ]
    l1_approve = models.CharField(max_length=128,choices=approval_choices,verbose_name="L1 Approval")
    l1_approve_comment = models.CharField(max_length=1024,null=True,verbose_name="Comment")
    l2_approve = models.CharField(max_length=128,choices=approval_choices,verbose_name="L2 Approval")
    l2_approve_comment = models.CharField(max_length=1024,null=True,verbose_name="Comment")

