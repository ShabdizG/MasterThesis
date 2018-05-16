from pymongo import MongoClient, ASCENDING
import data.Pipelines as pl
import data.constants as const
from datetime import datetime


def main():
    mongoDB = MongoClient('mongodb://localhost:27017/').LeagueCrawler
    globalStart, start = datetime.now(), datetime.now()

    mongoDB.adc_events.aggregate(pl.get_skill_level_ups(), allowDiskUse=True)
    print("Start Indexing at: " + str(datetime.now() - start))
    mongoDB.adc_skill_level_ups.create_index([("championId", ASCENDING)])
    mongoDB.adc_skill_level_ups.create_index([("championId", ASCENDING), ("patch", ASCENDING)])

    print("Finished Skill Level Ups at: ", str(datetime.now() - globalStart))

if __name__ == "__main__":
    main()