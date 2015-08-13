__author__ = 'Jovi'

import base64
import rsa
from django.db import models
import os

base_path = os.path.dirname(__file__)
PUBKEY_FILE = os.path.join(base_path, 'jovi.pub.pem')


class RsaEncryptModel(models.Model):
    pub = None
    pri = None

    rsa_encrypted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.rsa_encrypted:
            fields = self.get_encrypt_fields()
            if fields and len(fields) > 0:
                for field in fields:
                    v = getattr(self, field)
                    if not v:
                        continue
                    setattr(self, field, RsaEncryptModel.encrypt_value(v))
                setattr(self, 'rsa_encrypted', True)
        super(RsaEncryptModel, self).save(*args, **kwargs)

    def decrypt_model(self):
        if not self.rsa_encrypted:
            return self

        fields = self.get_encrypt_fields()
        if fields and len(fields) > 0:
            if not RsaEncryptModel.pri:
                raise rsa.pkcs1.CryptoError(
                    "There is no private pem key found, please call RSA_Encrypt.set_pri_key first before decrypt this object")

            for field in fields:
                v = getattr(self, field)

                if not v:
                    continue

                setattr(self, field, RsaEncryptModel.decrypt_value(v))

    class Meta:
        abstract = True

    def get_encrypt_fields(self):
        return []

    @staticmethod
    def set_pub_key(pub_key_file=PUBKEY_FILE):
        with open(pub_key_file) as pub_key_content:
            RsaEncryptModel.pub = rsa.PublicKey.load_pkcs1(pub_key_content.read())

    @staticmethod
    def set_pri_key(pri_key_file):
        with open(pri_key_file) as pri_key_content:
            RsaEncryptModel.pri = rsa.PrivateKey.load_pkcs1(pri_key_content.read())

    @staticmethod
    def encrypt_value(val):
        if not RsaEncryptModel.pub:
            raise rsa.pkcs1.CryptoError(
                "There is no public pem key found, please call RSA_Encrypt.set_pub_key first before saving this object")
        if isinstance(val, unicode):
            val = val.encode('utf-8')
        return base64.b64encode(rsa.encrypt(val, RsaEncryptModel.pub))


    @staticmethod
    def decrypt_value(val):
        if not RsaEncryptModel.pri:
            raise rsa.pkcs1.CryptoError(
                "There is no private key found, please call RSA_Encrypt.set_pri_key first before decrypt this object")
        return rsa.decrypt(base64.b64decode(val), RsaEncryptModel.pri)
