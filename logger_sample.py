from logging import getLogger, handlers, config, StreamHandler, Formatter, INFO
import json
import yaml


def get_console_logger():
    # ロガーの生成
    logger = getLogger(__name__)
    # 出力レベルの設定
    logger.setLevel(INFO)
    # ハンドラの生成
    handler = StreamHandler()
    # ハンドラの出力レベルの設定
    handler.setLevel(INFO)
    # フォーマッタの生成
    fmt = Formatter("%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s")
    # ハンドラにフォーマッタを登録
    handler.setFormatter(fmt)
    # ロガーにハンドラを登録
    logger.addHandler(handler)
    # ルートロガーへの伝播をOFFに設定
    logger.propagate = False
    logger.info("finish get_console_logger")
    return logger


def get_file_logger():
    # ロガーの生成
    logger = getLogger(__name__)
    # 出力レベルの設定
    logger.setLevel(INFO)
    # ハンドラの生成
    handler = handlers.TimedRotatingFileHandler("./logs/logger_sample.log", encoding="utf-8", when="MIDNIGHT", backupCount=10)
    # ハンドラの出力レベルの設定
    handler.setLevel(INFO)
    # フォーマッタの生成
    fmt = Formatter("%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s")
    # ハンドラにフォーマッタを登録
    handler.setFormatter(fmt)
    # ロガーにハンドラを登録
    logger.addHandler(handler)
    # ルートロガーへの伝播をOFFに設定
    logger.propagate = False
    logger.info("finish get_file_logger")
    return logger


def get_logger_from_yaml(yaml_path):
    # 定義ファイルの読み込み
    with open(yaml_path, "r") as f:
        logging_dict = yaml.safe_load(f)
    # 定義ファイルを使ったloggingの設定
    config.dictConfig(logging_dict)
    logger = getLogger(__name__)
    logger.info("finish get_logger_from_yaml")
    return logger


def get_logger_from_json(json_path):
    # 定義ファイルの読み込み
    with open(json_path, "r") as f:
        logging_dict = json.load(f)
    # 定義ファイルを使ったloggingの設定
    config.dictConfig(logging_dict)
    logger = getLogger(__name__)
    logger.info("finish get_logger_from_json")
    return logger


def main():
    # logger = get_console_logger()
    # logger = get_file_logger()
    # logger = get_logger_from_yaml("logging.yaml")
    logger = get_logger_from_json("logging.json")

    logger.debug("This is a Debug message")
    logger.info("This is a Info message")
    logger.warning("This is a Warning message")
    logger.error("This is a Error message")
    logger.critical("This is a Critical message")


if __name__ == "__main__":
    main()
