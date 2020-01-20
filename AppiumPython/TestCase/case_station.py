# -*- coding:utf-8 -*-
# Author：测试小谢
# @FILE     : case_station.py
# @Time     : 2020/1/7 13:50


import unittest
from Page.sharePage import Share
from Page.stationPage import Station
from common.logger import Log
import time
from config.utils import func_time


class CasePack(Station, Share):
    log = Log()

    def test_staion_success(self):
        try:
            self.charging_station()
            self.station_item()
            self.evaluation_item()
            self.appraise_item()
            # self.error_correction_item()
            self.error_position_item()
            self.collect_item()
            print("停车场功能测试完毕")


        except Exception as e:
            self.getScreenShot()
            self.log.error(e)


if __name__ == '__main__':
    unittest.main()
