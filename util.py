# -*- coding: utf-8 -*-

import hashlib

__author__ = 'syc'


def md5_for_file(filepath, block_size=2**20):
    """
    以文件路径作为参数，返回对文件md5后的值
    """
    f = open(filepath, 'rb')
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()
