from django.db import models

PRIVATE=0
TRUSTED=1
PUBLIC=2
PRIVACY_LEVELS={PRIVATE, TRUSTED, PUBLIC}
PRIVACY_LEVEL_CHOICES=(('PRIVATE', PRIVATE),
                       ('TRUSTED', TRUSTED),
                       ('PUBLIC', PUBLIC))

class Document(models.Model):
    content = models.TextField(db_index=True)
    privacy = models.PositiveSmallIntegerField(choices=PRIVACY_LEVEL_CHOICES)

class Trustee(models.Model):
    uri = models.CharField(unique=True, max_length=1024)
    public_key = models.CharField(max_length=2048)

    def encrypt(self, content):
        pass
