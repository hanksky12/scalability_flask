class Services1:
    def __init__(self, **kwargs):
        self.__kwargs = kwargs

    def run(self):
        inside_exist_check = self.__kwargs.get("inside_exist_check")
        # 從這邊直接取得驗證過且轉換過的參數
        #
