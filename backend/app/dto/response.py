class ResponseDto:
    @classmethod
    def get(cls, code, message, data=None, total=None):
        return {
            "code": code,
            "message": message,
            "total": total,
            "data": data
        }
