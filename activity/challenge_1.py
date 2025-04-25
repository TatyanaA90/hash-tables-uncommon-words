def uncommon_from_sentences(sentences):

    counter = {}
    uncommon_word = []

    for sentence in sentences:
        sentence_lits = sentence.split()
        for item in sentence_lits:
            if counter.get(item):
                counter[item] +=1
            else:
                counter[item] =1

    for key, value in counter.items():
        if value == 1:
            uncommon_word.append(key)
    return uncommon_word



