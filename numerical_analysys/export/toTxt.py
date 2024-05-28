from django.http import HttpResponse

def create_txt_download(answer, message):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="results.txt"'
    response.write(message)
    response.write('\n')
    response.write(answer)
    return response