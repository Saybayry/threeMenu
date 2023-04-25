from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Menu(models.Model):
    name = models.CharField(max_length=26)
    def __str__(self):
        return self.name
    pass

class MenuItem(models.Model):
    name = models.CharField(max_length=26)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    parent_menu = models.ForeignKey('Menu', blank=True, null=True, related_name='children_m', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    pass

@receiver(post_save, sender=MenuItem)
def add_parent_menu(sender, instance, **kwargs):
    if str(instance.parent_menu) == "None" and str(instance.parent) != "None":
        parent = instance.parent
        instance.parent_menu = sender.objects.get(pk=parent.pk).parent_menu
        instance.save()