import scrapy

class SpaceShuttleMissionsSpider(scrapy.Spider):
    name = 'SpaceShuttleMissions'

    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_Space_Shuttle_missions'
    ]
    # define a custom start_requests
    #def start_requests(self):
    #    urls = ['https://en.wikipedia.org/wiki/List_of_exoplanets_(full)']
    #    for url in urls:
    #        yield scrapy.Request(url=url, callback=self.parse)
    @staticmethod
    def fetch_columns(table_headers):
        '''
            Fetches the column names from the page's table
            and returns them as a list.
        '''
        columns = []
        for col in table_headers:
            # Get the column name from the linkbutton or text
            column_name = col.css('th::text').extract_first().rstrip()
            columns.append(column_name)
        return columns

    @staticmethod
    def fetch_shuttle_missions(mission_rows, mission_cols):
        '''
            Fetches the space shuttle missions and returns them as a dictionary.
            First fetches the test missions, then fetches the missions with
            orbital flights.
        '''
        # Create a list of dictionaries to lookup the shuttle missions
        missions_list = []
        for row in mission_rows[1:]:
            mission_dict = {}

            # For each section, save the contents into the dictionary
            for index,col in enumerate(row.css('td, th')):
                col_text = col.css('td ::text, th ::text').get()
                mission_dict[mission_cols[index]] = col_text.rstrip('\n')
            missions_list.append(mission_dict)
        return missions_list

    def parse(self, response):
        '''
            Parses the provided table.
            Fetches the columns and space shuttle missions.
        '''
        # First fetch the first table's headers for the column names
        table_header = response.css('table.wikitable').css('tr')[0].css('th')
        columns = self.fetch_columns(table_header)

        # yield {
        #     'columns': columns
        # }

        # Save the missions (Test & Flight missions)
        # Get the first two tables from the query
        missions_table_rows = response.css('table.wikitable')[0:2].css('tbody').css('tr')
                
        yield {
            'shuttle_missions': self.fetch_shuttle_missions(
                missions_table_rows, columns)
        }