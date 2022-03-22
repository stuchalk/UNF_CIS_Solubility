""" functions that are useful across the whole project """


def groupbyfirst(datain):
    """ organize data as a first letter grouped dictionary """
    dataout = {}
    for entry in datain:
        """ entry is dictionary with 'id', 'name', and 'first' """
        if entry['first'] not in dataout.keys():
            dataout.update({entry['first']: []})
        dataout[entry['first']].append((entry['id'], entry['name']))
    return dataout
