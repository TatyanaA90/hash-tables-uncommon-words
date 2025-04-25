def uncommon_from_sentences(s1, s2):
    new_list_s1 = s1.split()
    new_list_s2 = s2.split()
    count_s1 = count_items(new_list_s1)
    count_s2 = count_items(new_list_s2)

    
    uncommon_word = []
    for word in count_s1.keys():
        if count_s2.get(word):
            count_s2[word] += count_s1[word]
        else:
            count_s2[word] = count_s1[word]

    for key, value in count_s2.items():
        if value == 1:
            uncommon_word.append(key)
    return uncommon_word


def count_items(input):
    counter ={}
    for item in input:
        if counter.get(item):
            counter[item] +=1
        else:
            counter[item] =1
    return counter

