from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse

# Thinking about this a little, and need to settle on a schema.
# The video files will be stored in a directory structure. Something like:
# Conan > ComingOfConanTheCimmerian > FrostGiantsDaughter
# So, my thought is that this would be represented in the database like:
# title = FrostGiantsDaughter
# author = Robert E. Howard
# pathseg1 = Conan
# pathSeg2 = ComingOfConanTheCimmerian
# 

class Video(models.Model):
    # Name of the audio. 
    # E.g. thefrostgiantsdaughter
    title = models.CharField(max_length=200)
    # Directory structure where audio is located.
    # E.g. thecomingofconanthecimmerian
    path = models.CharField(max_length=400, blank=True, null=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    bodytext = models.TextField('Video Content', blank=True, null=True)
    # audio_track = models.FileField(upload_to='audio_tracks', blank=True, null=True)
    # track = models.FileField(upload_to='tracks', blank=True, null=True)

    # This returns the id/pk for the active audio object.
    # This id is in turn used to return the audio object to the audio_detail file.
    def get_video_id(self):
        # return reverse('audio_detail', args=[str(self.id)])
        # E.g. return 2
        return str(self.id)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        # E.g. url = "/audios/author/3"
        url = reverse('author-detail', args=[str(self.id)])
        return url

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
