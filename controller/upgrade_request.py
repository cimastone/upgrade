# -*- coding: utf-8 -*-
from flask import app
from flask import send_file
from flask import make_response
from flask import request
from flask import Flask
from common.http_tools import HttpTools
from common.log.manager import LogManager
from data_type import HttpErrorCode
from data_type import HttpErrorMsg
from upgrade_service import UpgradeService

logger = LogManager.register_log("upgrade_request")

app = Flask(__name__)

__author__ = 'syc'


@app.route('/upgrade/get_lastest_version', methods=['POST'])
def get_lastest_version():
    logger.info('=== get lastest version info')
    result = UpgradeService().init_configs()  # 检测版本
    return HttpTools.get_http_result_json(HttpErrorCode["NO_ERROR"], HttpErrorMsg["NO_ERROR"], result)


@app.route('/upgrade/zip', methods=['POST'])
def upgrade_zip():
    logger.info('=== upgrade zip download start')
    params_dict = request.json
    filepath = params_dict.get('filepath')
    if filepath:
        try:
            filepath = filepath.encode('utf-8')
        except Exception as ex:
            result = repr(ex)
            logger.error(result)
            return HttpTools.get_http_result_json(HttpErrorCode["PARAMS_ERROR"], HttpErrorMsg["PARAMS_ERROR"], result)
    else:
        result = 'download file path is None'
        logger.error(result)
        return HttpTools.get_http_result_json(HttpErrorCode["PARAMS_ERROR"], HttpErrorMsg["PARAMS_ERROR"], result)

    logger.info('=== download file path %s' % filepath)
    response = make_response(send_file(filepath))
    response.headers["Content-Disposition"] = "attachment;"
    response.headers["Content-Type"] = "application/zip"
    return response
