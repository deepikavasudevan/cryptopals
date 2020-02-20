def key_value_decode(string):
    dict = {}
    first_split = string.split("&")
    for s in first_split:
        second_split = s.split("=")
        dict[second_split[0]] = second_split[1]

    return dict


def key_value_encode(dict):
    string = ""
    for item in dict:
        string = string + item + "=" + str(dict[item]) + '&'

    return string[:len(string) - 1]
