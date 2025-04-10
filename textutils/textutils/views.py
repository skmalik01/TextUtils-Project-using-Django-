# I have created this file - Malik
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index2.html')

def analyze(request):
    
    #Get the text
    djtext = request.POST.get('text', 'default')
    
    #check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    
    #if no checkbox selected
    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Error: Please select at least one operation")
    
    
    #check which checkbox is on
    if (removepunc == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"purpose" : 'Removed Punctuations', "analyzed_text" : analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', params)
    
    if (fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {"purpose" : 'Change to Uppercase', "analyzed_text" : analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', params)
    
    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                analyzed += " "
        params = {"purpose" : 'Remove Newlines', "analyzed_text" : analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', params)
    
    if (extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index-1]==" "):
                analyzed = analyzed + char
        params = {"purpose" : 'Remove Extra Spaces', "analyzed_text" : analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', params)
    
    if (charcount == 'on'):
        cleaned_text = djtext.replace(" ", "").replace("\n", "").replace("\r", "")
        count = len(cleaned_text)
        analyzed += f"\n\nTotal Count is : {count}"
    
    params = {"purpose": "Your Output", "analyzed_text": analyzed}
    return render(request, 'analyze2.html', params)
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("new line remove")

# def spaceremove(request):
#     return HttpResponse("space remove")

# def charcount(request):
#     return HttpResponse("Char count")