from django.db import models

# The Virtual Machine Models created here are used for modeling the VM in database


class VirtualImage(models.Model):
    id = models.AutoField(primary_key=True)
    img_url = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.img_url


class PhysicalMachine(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.GenericIPAddressField(unpack_ipv4=True)
    cpu = models.CharField(max_length=20)
    disk = models.CharField(max_length=20)
    memory = models.CharField(max_length=20)
    maxvm = models.IntegerField()

    def __unicode__(self):
        return self.ip


class VirtualMachine(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.GenericIPAddressField(unpack_ipv4=True)
    netmask = models.CharField(max_length=20)
    gateway = models.CharField(max_length=20)
    pmachine = models.ForeignKey(PhysicalMachine, related_name="vmachines")
    vimage = models.ForeignKey(VirtualImage, related_name="vmachines")
    states = models.CharField(max_length=20)

    def __unicode__(self):
        return self.ip


