# 可擴展性的flask後端架構


## Config
- 利用工廠模式，將不同環境的設定檔分開，並可把跨專案使用的設定抽離ex MySqlConfig再放回。

## Controller
- api用來接收前端的請求，並回傳結果。

## Services
- 用來處理邏輯

## Models
- 用來定義資料庫的資料格式(在python語言中，model通常指的是資料庫的映射的物件，非MVC中的model，這邊保留python的共用語意)

## Utils
- 用來放置共用的函式(邏輯無關)

## Schemas
- 用來轉換request的資料格式，並驗證資料格式是否正確，與篩選資料response給前端
- 這邊利用自定義fields來做到，名稱上的轉換，值的轉換(藉由const)，以及驗證

## DTO
- 用來定義資料物件

## exceptions
- 用來定義錯誤類型

## interface
- 用來定義介面

## extensions.py
- 用來定義flask的擴展，額外的套件初始化統一放置在此