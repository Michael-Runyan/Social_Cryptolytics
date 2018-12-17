from datetime import datetime
class graph_tools(object):

    #example format '%m - %d - %Y
    @staticmethod
    def unix_to_date(time,format):
        return datetime.utcfromtimestamp(int(time)).strftime(format)

    #verys specific to one of my dataframes. Sums up to the rows
    @staticmethod
    def sum_rows(df):
        time = df['Unnamed: 0']
        df = df.drop(columns = ['Unnamed: 0'])
        sums = df.sum(axis=1)

        return time,sums