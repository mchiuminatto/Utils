class DFMapper:

    def __init__(self):
        pass

    @staticmethod
    def transform(df, mapper):
        """
        Transform data set columns names as per the mapper
        specification

        :param df: data set to transfomr
        :param mapper: JSON with column renaming specification
        :return df: data frame with columns renamed

        """
        _col_list = list(dict.fromkeys(mapper))
        df = df.rename(columns=mapper,)
        return df
