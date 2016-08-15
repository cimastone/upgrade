#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
from common.log.config import LogConfig
from common.log.manager import LogManager
from controller.upgrade_request import app
from upgrade_service import UpgradeService

__author__ = 'syc'

VERSION = "V1.0.2"

# 读取配置
config_file = open("configs.yaml")
Load_configs = yaml.load(config_file)
root_dir = Load_configs['root_dir']
ip = Load_configs['ip']

LogConfig.LOG_TO_FILE = True
LogConfig.LOG_DIR = "Logs"
LogConfig.LOG_NAME = "upgrade_service"
LogManager.init()


if __name__ == '__main__':
    print VERSION

    upgrade_service = UpgradeService(root_dir)
    upgrade_service.init_configs()

    app.run(host=ip)
