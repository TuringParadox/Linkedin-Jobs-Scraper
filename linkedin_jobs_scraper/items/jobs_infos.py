from scrapy.item import Item, Field
from itemloaders.processors import MapCompose, TakeFirst


class JobsInfosItem(Item):
    job_id = Field(output_processor=TakeFirst())
    data = Field(output_processor=TakeFirst())
    extracted_at = Field(output_processor=TakeFirst())


def __repr__(self):
    return repr("scraped job_id" + self["job_id"])
