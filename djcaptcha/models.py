from django.db import models
import datetime, unicodedata, random, time
import hashlib

CAPTCHA_TIMEOUT = 5
MAX_RANDOM_KEY = 18446744073709551616L
randrange = random.randrange

class CaptchaStore(models.Model):
    code = models.CharField(blank=False, max_length=32)
    respuesta = models.CharField(blank=False, max_length=32)
    hashkey = models.CharField(blank=False, max_length=40, unique=True)
    expiration = models.DateTimeField(blank=False)

    def __unicode__(self):
        return self.code

    def save(self,*args,**kwargs):
        self.respuesta = self.respuesta.lower()
        if not self.expiration:
            self.expiration = datetime.datetime.now() + datetime.timedelta(minutes=int(CAPTCHA_TIMEOUT))
        if not self.hashkey:
            key_ = unicodedata.normalize('NFKD', str(randrange(0,MAX_RANDOM_KEY)) + str(time.time()) + unicode(self.code)).encode('ascii', 'ignore') + unicodedata.normalize('NFKD', unicode(self.respuesta)).encode('ascii', 'ignore')
            self.hashkey = hashlib.new('sha', key_).hexdigest()
            del(key_)
        super(CaptchaStore,self).save(*args,**kwargs)

    def remove_expired(cls):
        cls.objects.filter(expiration__lte=datetime.datetime.now()).delete()
    remove_expired = classmethod(remove_expired)