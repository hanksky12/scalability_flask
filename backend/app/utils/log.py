import logging
import logging.handlers


class LogUtil:
    """
    debug: 決定terminal輸出的log等級 (預設為False)
    log_path: log檔案存放路徑 (預設為空)
    log_name: log檔案名稱 (預設為all)
    screen_only: 只在terminal輸出log，不存log檔案 (預設為False)
    add_stream_handler: 是否在root logger加上stream handler (預設為True)
    """

    @classmethod
    def init(cls,
             level: bool = False,
             log_path: str = "",
             log_name: str = "all",
             screen_only: bool = False,
             add_stream_handler: bool = True
             ):
        cls.__root_logger = cls.__get_root_logger()
        formatter = cls.__get_formatter()
        if add_stream_handler:
            cls.__add_stream_handler(level, formatter)
        if screen_only:
            return
        if log_path == "":
            raise Exception("log_path is empty")
        cls.__log_path = log_path
        cls.__add_file_handler(formatter, log_name)
        logging.debug("LogUtil init success")
    #....