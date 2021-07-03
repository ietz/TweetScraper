from pathlib import Path
from typing import List, Dict, Type, BinaryIO

from scrapy.crawler import Crawler
from scrapy.exporters import JsonLinesItemExporter
from scrapy import signals
from scrapy.signalmanager import SignalManager
from scrapy.utils.project import get_project_settings

from TweetScraper.items import Tweet, User


SETTINGS = get_project_settings()
OUTPUT_DIR = Path(SETTINGS['OUTPUT_DIR'])


class MultiJsonLinesPipeline:
    item_type_file_paths = {
        Tweet: OUTPUT_DIR / 'tweets.csv',
        User: OUTPUT_DIR / 'users.csv',
    }

    def __init__(self, signal_manager: SignalManager):
        signal_manager.connect(self.spider_opened, signals.spider_opened)
        signal_manager.connect(self.spider_closed, signals.spider_closed)
        self.files: List[BinaryIO] = []
        self.type_exporters: Dict[Type, JsonLinesItemExporter] = {}

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        return MultiJsonLinesPipeline(crawler.signals)

    def spider_opened(self, spider):
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        for item_type, file_path in MultiJsonLinesPipeline.item_type_file_paths.items():
            f = file_path.open('w+b')
            exporter = JsonLinesItemExporter(f)
            exporter.start_exporting()

            self.files.append(f)
            self.type_exporters[item_type] = exporter

    def spider_closed(self, spider):
        for exporter in self.type_exporters.values():
            exporter.finish_exporting()

        for file in self.files:
            file.close()

    def process_item(self, item, spider):
        if type(item) in self.type_exporters:
            self.type_exporters[type(item)].export_item(item)
        return item
