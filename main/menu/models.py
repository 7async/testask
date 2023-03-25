from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    
    def get_url(self):
        if self.parent:
            return '{0}/{1}'.format(self.parent.get_url(), self.name)
        else:
            return '/menu/{0}'.format(self.name)

    def __str__(self):
        return self.title