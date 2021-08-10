import datetime

class FactorHandler:

    def __init__(self):
        self.factors = list()
        self.noraml_format = r'%Y/%m/%d'

    def add_factor(self, time_format, time, value):
        self.factors.append(dict(value=value,
                                 time_format=time_format,
                                 time=self.centeralize(time, time_format)))
    
    def remove_all_factors(self, time_format, time):
        date = self.centeralize(time, time_format)
        # print(len(self.factors))
        self.factors = list(filter(lambda x: x['time'] != date, self.factors))
        # print(len(self.factors))

    def get_sum(self, time_format, start_time, finish_time):
        start = self.centeralize(start_time, time_format)
        end = self.centeralize(finish_time, time_format)
        return sum([i['value'] for i in self.factors if start <= i['time'] <= end])

    def centeralize(self, date, date_format):
        datestamp = date_format.split('/')
        dates = date.split('/')
        dict_time = {datestamp[i]: dates[i] for i in range(len(datestamp))}
        # print(dict_time)
        y, m, d = int(dict_time['yyyy']), int(dict_time['mm']), int(dict_time['dd'])
        # print(y, m, d)
        date_time = datetime.datetime(y, m, d)
        # print(date_time)
        return date_time

# fh = FactorHandler()
# # print(len(fh.factors))
# fh.add_factor("dd/mm/yyyy", "02/10/2019", 10)
# fh.add_factor("dd/mm/yyyy", "03/10/2019", 20)
# fh.add_factor("dd/mm/yyyy", "03/10/2019", 30)
# fh.add_factor("dd/mm/yyyy", "05/10/2019", 5)
# # print(len(fh.factors))
# print(fh.get_sum("yyyy/dd/mm", "2019/02/10", "2019/03/10"))
# fh.remove_all_factors("mm/dd/yyyy", "10/03/2019")
# print(fh.get_sum("yyyy/dd/mm", "2019/02/10", "2019/05/10"))