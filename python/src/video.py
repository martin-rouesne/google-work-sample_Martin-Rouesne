"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str], flagStatus = False, flagReason = "" ):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)

        self._flagStatus = flagStatus
        self._flagReason = flagReason

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags

    @property
    def flagStatus(self)-> bool:
        """Returns the flag status of a video."""
        return self._flagStatus
    
    @property
    def flagReason(self) -> str:
        """Returns the flag reason of a video."""
        return self._flagReason

    @flagStatus.setter
    def flagStatus(self, flagStatus):
        """Returns the flag status of a video."""
        self._flagStatus = flagStatus
    
    @flagReason.setter
    def flagReason(self, flagReason):
        """Returns the flag reason of a video."""
        self._flagReason = flagReason

    def __str__(self):
        videoToString = f"{self.title} ({self.video_id}) [" + " ".join(self.tags) + "]"
        
        if self.flagStatus:
            videoToString += f" - FLAGGED (reason: {self.flagReason})"
        
        return videoToString
        
        
