"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.videoPlayin = False
        self.videoPaused = False
        self.currentlyPlayedVideo = None
        self.playlists = {}


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")


    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        sortListOfVideos = sorted(self._video_library.get_all_videos(), key = lambda video: video.title)
        for video in sortListOfVideos:
            print("   " + str(video))


    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played."""
        
        videoToPlay = self._video_library.get_video(video_id)

        if videoToPlay == None:
            print("Cannot play video: Video does not exist")
        elif videoToPlay.flagStatus:
            print(f"Cannot play video: Video is currently flagged (reason: {videoToPlay.flagReason})")
        else:
            if self.videoPlayin:
                print(f"Stopping video: {self.currentlyPlayedVideo.title}")
            
            print(f"Playing video: {videoToPlay.title}")
            self.videoPlayin = True
            self.videoPaused = False
            self.currentlyPlayedVideo = videoToPlay


    def stop_video(self):
        """Stops the current video."""

        if self.videoPlayin:
            print(f"Stopping video: {self.currentlyPlayedVideo.title}")
            self.videoPlayin = False
            self.currentlyPlayedVideo = None
        else:
            print("Cannot stop video: No video is currently playing")


    def play_random_video(self):
        """Plays a random video from the video library."""

        if self.videoPlayin:
            print(f"Stopping video: {self.currentlyPlayedVideo.title}")
        
        randomVideo = random.choice(self._video_library.get_all_videos())

        if randomVideo == None or randomVideo.flagStatus:
            print("No videos available")
        else:
            print(f"Playing video: {randomVideo.title}")
            self.currentlyPlayedVideo = randomVideo
            self.videoPlayin = True
            self.videoPaused = False


    def pause_video(self):
        """Pauses the current video."""

        if self.videoPlayin:
            if self.videoPaused:
                print(f"Video already paused: {self.currentlyPlayedVideo.title}")
            else:
                print(f"Pausing video: {self.currentlyPlayedVideo.title}")
                self.videoPaused = True
        else:
            print("Cannot pause video: No video is currently playing")


    def continue_video(self):
        """Resumes playing the current video."""

        if self.videoPlayin:
            if self.videoPaused:
                print(f"Continuing video: {self.currentlyPlayedVideo.title}")
                self.videoPaused = False
            else:
                print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")


    def show_playing(self):
        """Displays video currently playing."""

        if self.videoPlayin:
            print(f" Currently playing: {self.currentlyPlayedVideo.title} ({self.currentlyPlayedVideo.video_id}) [", end = "")
            print(*self.currentlyPlayedVideo.tags, sep = " ", end = "]")
            if self.videoPaused:
                print(" - PAUSED")
            else:
                print()
        else:
            print("No video is currently playing")


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        Args:
            playlist_name: The playlist name."""
        
        if self.playlists.get(playlist_name.upper()) == None:
            self.playlists[playlist_name.upper()] = [playlist_name, []]
            print(f"Successfully created new playlist: {playlist_name}")
        else:
            print("Cannot create playlist: A playlist with the same name already exists")
        

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added."""

        initialPlaylist = self.playlists.get(playlist_name.upper())

        if initialPlaylist == None:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        else:
            initialPlaylistVideos = initialPlaylist[1]
            videoToAdd = self._video_library.get_video(video_id)
            
            if videoToAdd == None:
                print(f"Cannot add video to {playlist_name}: Video does not exist")
            elif videoToAdd.flagStatus:
                print(f"Cannot add video to {playlist_name}: Video is currently flagged (reason: {videoToAdd.flagReason})")
            elif videoToAdd in initialPlaylistVideos:
                print(f"Cannot add video to {playlist_name}: Video already added")
            else:
                initialPlaylistVideos.append(videoToAdd)
                self.playlists[playlist_name.upper()] = [self.playlists[playlist_name.upper()][0], initialPlaylistVideos]
                print(f"Added video to {playlist_name}: {videoToAdd.title}")


    def show_all_playlists(self):
        """Display all playlists."""

        if len(self.playlists) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for playlistNAME in sorted(self.playlists):
                print(f"  {self.playlists[playlistNAME][0]}")


    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.
        Args:
            playlist_name: The playlist name."""
        
        playlist = self.playlists.get(playlist_name.upper())

        if playlist == None:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
        else:
            print(f"Showing playlist: {playlist_name}")
            if len(playlist[1]) == 0:
                print("   No videos here yet")
            else:
                for video in playlist[1]:
                    print("   " + str(video))


    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed."""

        initialPlaylist = self.playlists.get(playlist_name.upper())

        if initialPlaylist == None:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        else:
            initialPlaylistVideos = initialPlaylist[1]
            videoToRemove = self._video_library.get_video(video_id)
            
            if videoToRemove == None:
                print(f"Cannot remove video from {playlist_name}: Video does not exist")
            elif not videoToRemove in initialPlaylistVideos:
                print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
            else:
                initialPlaylistVideos.remove(videoToRemove)
                self.playlists[playlist_name.upper()] = [self.playlists[playlist_name.upper()][0], initialPlaylistVideos]
                print(f"Removed video from {playlist_name}: {videoToRemove.title}")


    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.
        Args:
            playlist_name: The playlist name."""
        
        initialPlaylist = self.playlists.get(playlist_name.upper())

        if initialPlaylist == None:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        else:
            self.playlists[playlist_name.upper()] = [self.playlists[playlist_name.upper()][0], []]
            print(f"Successfully removed all videos from {playlist_name}")


    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.
        Args:
            playlist_name: The playlist name."""
        
        initialPlaylist = self.playlists.get(playlist_name.upper())

        if initialPlaylist == None:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        else:
            self.playlists[playlist_name.upper()] = None
            print(f"Deleted playlist: {playlist_name}")


    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.
        Args:
            search_term: The query to be used in search."""
        
        searchResults = []

        for video in self._video_library.get_all_videos():
            if search_term.upper() in video.title.upper() and not video.flagStatus:
                searchResults.append(video)
        
        if len(searchResults) == 0:
            print(f"No search results for {search_term}")
        else:
            print(f"Here are the results for {search_term}:")
            for result in searchResults:
                print(f"   {searchResults.index(result) + 1}) " + str(result))

            print("Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no.")

            answer = input()
            
            if answer.isdigit():
                intAnswer = int(answer)
                if intAnswer > 0 and intAnswer <= len(searchResults):
                    self.play_video(searchResults[intAnswer - 1].video_id)
        

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.
        Args:
            video_tag: The video tag to be used in search."""
        
        searchResults = []

        for video in self._video_library.get_all_videos():
            if video_tag.lower() in video.tags and not video.flagStatus:
                searchResults.append(video)
        
        if len(searchResults) == 0:
            print(f"No search results for {video_tag}")
        else:
            print(f"Here are the results for {video_tag}:")
            for result in searchResults:
                print(f"   {searchResults.index(result) + 1}) " + str(result))

            print("Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no.")

            answer = input()
            
            if answer.isdigit():
                intAnswer = int(answer)
                if intAnswer > 0 and intAnswer <= len(searchResults):
                    self.play_video(searchResults[intAnswer - 1].video_id)


    def flag_video(self, video_id, flag_reason = "Not supplied"):
        """Mark a video as flagged.
        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video."""
        
        videoToFlag = self._video_library.get_video(video_id)

        if videoToFlag == None:
            print("Cannot flag video: Video does not exist")
        elif videoToFlag.flagStatus:
            print("Cannot flag video: Video is already flagged")
        else:
            if self.currentlyPlayedVideo == videoToFlag:
                self.stop_video()
            videoToFlag.flagStatus = True
            videoToFlag.flagReason = flag_reason
            print(f"Successfully flagged video: {videoToFlag.title} (reason: {flag_reason})")
        

    def allow_video(self, video_id):
        """Removes a flag from a video.
        Args:
            video_id: The video_id to be allowed again."""
        
        videoToAllow = self._video_library.get_video(video_id)

        if videoToAllow == None:
            print("Cannot remove flag from video: Video does not exist")
        elif not videoToAllow.flagStatus:
            print("Cannot remove flag from video: Video is not flagged")
        else:
            videoToAllow.flagStatus = False
            videoToAllow.flagReason = ""
            print(f"Successfully removed flag from video: {videoToAllow.title}")
