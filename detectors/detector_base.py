import abc


class FaceDetector:
    def __init__(self):
        pass

    @abc.abstractmethod
    def name(self):
        return 'detector'

    @abc.abstractmethod
    def detect(self, npimg):
        """

        :param npimg:
        :return: list of BoundingBox
        """
        pass
