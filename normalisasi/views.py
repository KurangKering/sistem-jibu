from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from libraries.algorithms import *

# Create your views here.
def index(request):

    inputan = request.POST.get('inputan', '')

    text = ""
    if inputan != "":

        sentences = inputan
        if len(sentences) <= 0:
            raise RuntimeError('Input Minimal 1 kata')

        words = get_words()
        dictionary = ArrayDictionary(words)
        damerau = DamerauLevenshtein(dictionary)
        hasil_damerau = damerau.process(sentences)
        
        C = damerau.get_C()
        W = damerau.get_W()

        ngram = NGram(C,W)
        gram_freq= ngram.get_ngram_with_freq()

        pro_score = ProbabilityScore()
        probability = pro_score.calculate_probability(C, gram_freq)
        score = pro_score.calculate_score(C, probability)
        output = pro_score.get_output(C, score)
        
        text = " ".join(output)


    content = {
        'input':inputan,
        'text':text
    }

    return render(request, 'normalisasi/index.html', content)
