def countSeniors(details):
    count = 0
    for i in details:
        if int(i[11:13]) > 60:
            count += 1

    return count


print(countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]))
