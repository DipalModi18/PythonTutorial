class ApiError(Exception):
    """CUSTOM API ERROR CLASS"""

    def __init__(self, status):
        self.status = status
