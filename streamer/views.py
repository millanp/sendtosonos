from django.shortcuts import render
from subprocess import call

# Create your views here.
def add_to_mp3_stream(request, yturl):
    cmd = '''youtube-dl --format mp4 -o - "%s" |
             fmpeg -i pipe:0 -f mp3 out.mp3''' % yturl
    call(cmd)
