from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from libraries.algorithms import *
from django.contrib import messages
from django.contrib.messages import get_messages

# Create your views here.
def index(request):

    return render(request, 'normalisasi/index.html')


def normalize(request):
    inputan = request.POST.get('inputan', '')

    text = ""
    if inputan == "":
        return redirect(index)

    sentences = " ".join(inputan.lower().split())


    words = get_words()
    dictionary = ArrayDictionary(words)
    damerau = DamerauLevenshtein(dictionary)
    hasil_damerau = damerau.process(sentences)
    
    C = damerau.get_C()
    W = damerau.get_W()

    ngram = NGram(C,W)
    gram_freq= ngram.get_ngram_with_freq()
    nnngram, freq = gram_freq

    lbigram, rbigram, trigram = nnngram
    lfreq, rfreq, trifreq = freq


    pro_score = ProbabilityScore()
    probability = pro_score.calculate_probability(C, gram_freq)
    score = pro_score.calculate_score(C, probability)
    output = pro_score.get_output(C, score)
    
    text = " ".join(output)

    array_inputan = inputan.split(' ')
    jumlah_damerau = [len(x)+1 for x in hasil_damerau]

    ziped_freq_gram = []
    for x in range(len(array_inputan)):
        ziped_freq_gram.append([len(lbigram[x])+1, array_inputan[x], zip(C[x], lbigram[x], rbigram[x], trigram[x], lfreq[x], rfreq[x], trifreq[x], score[x])])
        

    content = {
        'input':inputan,
        'text':text,
        'damerau': hasil_damerau,
        'array_inputan':array_inputan,
        'inputan_damerau': zip(array_inputan, hasil_damerau, jumlah_damerau),
        'hasil_gram': ziped_freq_gram,
    }

    return render(request, 'normalisasi/summary.html', content)

