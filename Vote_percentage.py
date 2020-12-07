def vote_percentage(results):
    """(str)-> (float)
    Precondition: all values within the string are either abstained, yes or no"""
    results = results.split()
    # determine length of input
    length_ofinput = (len(results))
    # determine number of abstained within the input
    recurrance_ofabstained = results.count('abstained')
    recurrance_ofyes = results.count('yes')
    number_ofyesno = length_ofinput-recurrance_ofabstained
    final = recurrance_ofyes/number_ofyesno
    return final
