import collections
import nltk
# nltk.download('punkt')
from nltk import word_tokenize

# from operator import itemgetter

training_data = open('Train_data.txt', 'r')
sentences = training_data.readlines()

queue = collections.deque(maxlen=3)

words = set()
unigram = {}
bigram = {}
trigram = {}

for sentence in sentences:
    queue.append('')
    text = sentence.lower().split(" .")[-1]
    tokens = word_tokenize(text)
    for token in tokens:
        queue.append(token)
        if not (token in words):
            words.add(token)

        if not (token in unigram):
            unigram[token] = 0
        unigram[token] += 1

        if len(queue) >= 2:
            pair = tuple(queue)[:2]
            if not (pair in bigram):
                bigram[pair] = 0
            bigram[pair] += 1

        if len(queue) == 3:
            triad = tuple(queue)
            if not (triad in trigram):
                trigram[triad] = 0
            trigram[triad] += 1

training_data.close()

word_count = len(unigram)
unigram[''] = word_count


def single_word_probability(word):
    if not (word in unigram):
        return 0
    return unigram[word] / word_count


def pair_word_probability(double):
    if not (double in bigram):
        return 0
    return bigram[double] / unigram[double[0]]


def triple_word_probability(triple):
    if not (triple in trigram):
        return 0
    return trigram[triple] / bigram[(triple[0], triple[1])]


def guess_next_word(statement):
    candidate_words = []

    for word in words:
        p1 = single_word_probability(word)
        p2 = pair_word_probability((statement[-1], word))
        p3 = triple_word_probability((statement[-2], statement[-1], word)) if len(statement) >= 3 else 0

        p = (0.000013 * p1) + (0.00987 * p2) + (0.990117 * p3)

        candidate_words.append((word, p))

    candidate_words.sort(key=lambda x: x[1], reverse=True)
    # maximum_probability = candidate_words[1]
    # print(candidate_words[1][0])
    if candidate_words[0][0] == '``':
        maximum_probability = candidate_words[1]
    else:
        maximum_probability = candidate_words[0]
    return maximum_probability


#testing the model
testing_data = open('Test_data.txt', encoding='utf8', errors='ignore')
testing_sentences = testing_data.readlines()

testing_data_result_file = open('Test_data_result.txt', 'w')
testing_data_result = []
index = 1
for testing_sentence in testing_sentences:
    suggestion = (str(index) + ", " + guess_next_word(testing_sentence.split(" $ ")[0].split())[0])
    testing_data_result.append(suggestion)
    testing_data_result_file.write(suggestion)
    testing_data_result_file.write('\n')
    print(suggestion)
    index += 1

testing_data.close()

#reporting accuracy
accuracy_result_file = open('labels.txt', encoding='utf8', errors='ignore')
accuracy_result = accuracy_result_file.readlines()
index = 0
total_suggestions = 80
correct_suggestions = 0
for word_suggestion in accuracy_result:
    #print(testing_data_result[index], 'vs', word_suggestion)
    if testing_data_result[index] == word_suggestion:
        correct_suggestions += 1
    index += 1

accuracy_result_file.close()

accuracy_result_final = correct_suggestions / total_suggestions
print('Accuracy of the model is: ', accuracy_result_final)
testing_data_result_file.write('Accuracy of the model is: ')
testing_data_result_file.write(str(accuracy_result_final))
testing_data_result_file.write('\n')
testing_data_result_file.close()