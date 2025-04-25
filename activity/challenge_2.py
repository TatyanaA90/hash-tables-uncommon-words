def uncommon_from_sentences(sentences):
    counter = {}

    for sentence in sentences:
        sentence_lits = sentence.split()
        unique_words = set(sentence_lits) 
        for word in unique_words:
            if word not in counter:
                counter[word] = 0
            counter[word] += 1

    uncommon_words = []
    for word, count in counter.items():
        if count == 1:
            uncommon_words.append(word)

    return uncommon_words