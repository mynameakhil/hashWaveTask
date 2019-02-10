import scrapy
class SpiderTask(scrapy.Spider):
    name = "event"
    allowed_domains = ['allevents.in']
    start_urls = [
        'https://allevents.in/events#'
    ]

    def parse(self, response):
    parser = scrapy.Selector(response)
    evnt=response.xpath("//div[@class='non-overlay gray-trans-back']")
    # evnt1= response.xpath("//div[@class='events-style-resgrid gray-trans-back']")               evnt2=response.xpath("//div[@class='container']") 
    # evnt3=response.xpath("//div[@class='row']") 
    # evnt4=response.xpath("//div[@class='span12']") 
    # evnt5=response.xpath("//div[@class='resgrid-row']")
    # evnt6=response.xpath("//div[@class='inner']")
    # evnt7=response.xpath("//ul[@class='resgrid-ul']")
    # evnt8=response.xpath("//li[@class='item']")
    # evnt9=response.xpath("//div[@class='meta']") 
    # evnt10=response.xpath("//div[@class='title']")
    # evnt11= ".//a/h3/text()"  
    for evt in evnt:

       # evnt.evnt1.evnt2.evnt3.evnt4.evnt5.evnt6.envt7.evnt8.evnt9.evnt10.xpath(evnt11).extract() 
        XPATH_EVENT_LIST  = ".//a/h3/text()"  
        XPATH_EVENT_DATE =  ".//div[@class='meta2']//span[@class='time']/text()"
        XPATH_EVENT_ADDRESS = ".//div[@class='meta']//span[@class='venue']/text()"
        XPATH_EVENT_IMAGE = ".//div[@class='thumb']//img/src/@href"
        

        evnt_list = evnt.xpath(XPATH_EVENT_LIST ).extract()

        evnt_date = evnt.xpath(XPATH_EVENT_DATE ).extract()


        evnt_addresss = evnt.xpath(XPATH_EVENT_ADDRESS ).extract()

        evnt_image = evnt.xpath(XPATH_EVENT_IMAGE ).extract()
        yield {
            'event_list':str(evnt_list),
            'event_date':evnt_date,
            'event_address':evnt_address,
            'event_image':evnt_image,
            'event_ticket':evnt_ticket,           
            
        }


    NEXT_PAGE_LINK= ".//div[@class='title']//a/@href"
    next_page=evnt.xpath(NEXT_PAGE_LINK).extract()
    evnt_pge=response.xpath("//div[@class='direct']")
    for evn in event:
        EVENT_TICKET=".//div[@class='event-ticket']//a/text()"
        evnt_ticket=evnt_pge.xpath(EVENT_TICKET).extract()
        next_page = response.urljoin(next_page)
        yield scrapy.Request(next_page, callback=self.parse)

       