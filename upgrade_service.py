# -*- coding: utf-8 -*-

import os
import yaml
from common.log.manager import LogManager
from common.pattern.singleton import singleton
from util import md5_for_file

logger = LogManager.register_log("upgrade_service")


__author__ = 'syc'


@singleton
class UpgradeService(object):
    """
    检测app版本
    Attributes:
        root_dir: 服务器端客户端应用所在的根路径
    """
    def __init__(self, root_dir):
        self.root_dir = root_dir  # client app root path
        self.app_info = {}  # (dict) key: app_id value: (dict) key: app_id,version,app_path,ver_desc, md5

    def init_configs(self):
        """
        初始化self.configs
        """
        list_dirs = os.walk(self.root_dir)
        map(lambda info: self.add(info), list_dirs)
        return self.app_info

    def add(self, info):
        """
        增加config_file_path值
        :param info: (root, dirs, files)
        """
        root = info[0]
        files = info[2]
        paths = [os.path.join(root, f) for f in files if f == 'configs.yaml']
        for path in paths:
            conf_file = open(path)
            config = yaml.load(conf_file)
            if None in [config.get('app_id'), config.get('version'), config.get('app_path')]:
                raise Exception('%s file must include valid app_id version and app_path properties' % path)

            config['md5'] = md5_for_file(config.get('app_path'))
            self.app_info[config['app_id']] = config
