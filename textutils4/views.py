from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    text1=request.POST.get('text','please enter the text')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')
    if removepunc=='on':
        analyzed=""
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in text1:
            if char not in punctuations:
                analyzed+=char
        dict={'purpose':'Punctuations are removed.','analyzed_text':analyzed}
        text1=analyzed
        #return render(request,'analyze.html',dict)
    if fullcaps=='on':
        analyzed=""
        for char in text1:
            analyzed+=char.upper()
        dict={'purpose':'Upper Case','analyzed_text':analyzed}
        text1=analyzed
        #return render(request,'analyze.html',dict)
    if newlineremover=='on':
        analyzed=""
        for char in text1:
            if char!='\n' and char!='\r':
                analyzed+=char
            else:
                continue
        dict={'purpose':'New lines are removed.','analyzed_text':analyzed}
        text1=analyzed
        #return render(request,'analyze.html',dict)
    if extraspaceremover=='on':
        analyzed=""
        for index, char in enumerate(text1):
            if not(text1[index]==' ' and text1[index+1]==' '):
                analyzed+=char
        dict={'purpose':'Extra Spaces are removed.','analyzed_text':analyzed}
        text1=analyzed
        #return render(request,'analyze.html',dict)
    if charcount=='on':
        c=""
        for char in text1:
            if char!='\n' and char!='\r' and char!=" ":
                c+=char
            else:
                continue
        analyzed=len(c)
        dict={'purpose':'Count of characters','analyzed_text':analyzed}
        text1=analyzed
        #return render(request,'analyze.html',dict)
    if removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount!='on':
        return HttpResponse("Please select the operation.")
    
    return render(request, 'analyze.html', dict)
