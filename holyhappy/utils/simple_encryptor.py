import base64
import hashlib
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
unpad = lambda s: s[:-ord(s[len(s)-1:])]


def tohex(val, nbits=8):
    return hex((val + (1 << nbits)) % (1 << nbits))


def to_bytes(iv_list):
    iv_tuple = (int(tohex(x), 16) for x in iv_list)
    return bytes(iv_tuple)


class SimpleEncryptor(object):
    """
    https://github.com/dlitz/pycrypto
    AES256 with PKCS5 padding
    """

    def __init__(self, key):
        self.iv = to_bytes([1, 10, 78, 62, -18, -78, -12, 92, 31, 22, 12, 55, -27, 27, 60, 22])
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, message):
        """
        It is assumed that you use Python 3.0+
        , so plaintext's type must be str type(== unicode).
        """
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        raw = pad(message.encode())
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')

    def decrypt(self, enc):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        dec = cipher.decrypt(base64.b64decode(enc))
        return unpad(dec).decode('utf-8')


if __name__ == '__main__':
    key = '44078:d6:f0:43:9e:c819921221'
    password = '90^34^c4#c7@1f&60!e4&97%64(db#2b*f7!b2%6c!70%6c)'

    print('KEY : ', key)
    print('PAS : ', password)

    aes = SimpleEncryptor(key)
    enc = aes.encrypt(password)
    dec = aes.decrypt(enc)

    print('ENC : ', enc)
    print('DEC : ', dec)
