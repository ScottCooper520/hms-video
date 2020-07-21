from django.urls import path
from . import views

# Flow Description:
# Empty path renders index template, which shows audio/author options.
# Clicking on All audios link hits audios path below, which renders list of audios template.
# Clicking on an audio in list hits audios/<int:pk> path below, which renders selected audio template.
# The audio template has JS that then gets the selected title and forms a url that hits getaudio path below.
# The getaudio path returns the audio file via a function in views.py. This file is used in Audio tag.

urlpatterns = [
    path('', views.index, name='index'),
    # Testing... path('', views.AudioListView.as_view(), name='index'),
    # => Does show list as home, bit incorrect path after clicking on specific audio...
    # Following work with commented functions in views.py
    # path('audios/', views.audio_list, name='audios'),
    # path('audios/<int:pk>', views.audio_detail, name='audio-detail'),

    # Following work with class-based views in views.py
    path('videos/', views.VideoListView.as_view(), name='videos'),
    # Tutorial shows 'audio/<int:pk>', not audios. But clicking on audio in list => audios/#
    path('videos/<int:pk>', views.VideoDetailView.as_view(), name='video-detail'),

    # Following do not change for either implementation above.
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

    # This is the path that actually plays the audio. Its url is called by the
    # audio-detail template's javascript.
    # Useful testing: Originally from mediaserver project
    # Following is useful to directly run audio from views. Access example url:
    # http://127.0.0.1:8000/audios/scotty/frog_lillypad.mp3/ will map directly to 
    # frog_lillypad.mp3 via sharefromwindows folder.
    # path ('scotty/<str:filename>', views.scottyMp3PathFile, name='scottyMp3PathFile'),
    # OK. Does not open template, but opens player with control right in browser - works.
    # OK GF path ('scotty/<str:filename>/', views.scottyMp3Filename, name='scottyMp3Filename'),
    # OK path ('getaudio/<str:filename>/', views.scottyMp3Filename, name='scottyMp3Filename'),
    # OK path ('getaudio/<str:filename>/', views.getAudioFile, name='getAudioFile'),
    # OK path ('getaudio/<str:path1>/<str:path2>/<str:filename>/', views.getAudioFile, name='getAudioFile'),
    # Audio from share root folder.
    path ('getvideo/<str:filename>/', views.getVideoFilePath0, name='getVideoFilePath0'),
    # Audio from level 1 folder in share root.
    path ('getvideo/<str:path1>/<str:filename>/', views.getVideoFilePath1, name='getVideoFilePath1'),
    # Audio from level 2 folder in share root.
    path ('getvideo/<str:path1>/<str:path2>/<str:filename>/', views.getVideoFilePath2, name='getVideoFilePath2'),
    # Audio from level 3 folder in share root.
    path ('getvideo/<str:path1>/<str:path2>/<str:path3>/<str:filename>/', views.getVideoFilePath3, name='getVideoFilePath3'),
    # Get audio path/title given pk. Used to play next audio automatically.
    path ('getPathTitle/<int:pk>', views.getPathTitle, name='getPathTitle'),
]