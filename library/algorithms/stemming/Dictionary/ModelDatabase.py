import os

class ModelDatabase(object):

    def __init__(self, model, field):
        self.words = model.objects.values_list(field, flat=True)

    def get_kamus(self):
        return self.words
