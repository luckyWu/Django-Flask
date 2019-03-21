from _md5 import md5

from django.test import TestCase

# Create your tests here.
from hashlib import md5

def my_md5_hex(origin_str):
    """生成MD5摘要"""
    return md5(origin_str.encode('utf-8')).hexdigest()