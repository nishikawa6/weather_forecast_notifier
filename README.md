# 天気予報通知システム
当日の天気予報をLineで通知するシステム。

# ビジネスルール
- 天気予報の情報を取得する
- 天気予報の情報を通知する

# 必要な機能の洗い出し（設計時に作成）
- 気象庁のAPIから天気予報情報を取得する機能
  - エンドポイント：https://www.jma.go.jp/bosai/forecast/data/overview_forecast/350000.json
    - レスポンス例：
       {"publishingOffice":"下関地方気象台","reportDatetime":"2025-01-29T16:37:00+09:00","targetArea":"山口県","headlineText":"","text":"　山口県は、寒気の影響により、おおむね曇りで雪や雨が降っている所があります。\n\n　２９日は、寒気の影響によりおおむね曇りで雪か雨が降る所があるでしょう。\n\n　３０日は、寒気の影響によりおおむね曇りで雪か雨が降る所がありますが、高気圧に覆われて晴れとなる所もあるでしょう。"}
- APIのレスポンスから目的のデータを取り出す機能
  - レスポンスの"text"の値を取り出す。
- Line Notifyで通知を送信する機能


# 作成した機能（開発後に作成）
- 環境変数の読み込み機能
- Line Notifyで通知を送信する機能
- 気象庁のAPIを叩き、レスポンスを受け取る機能
- APIのレスポンスから通知メッセージを作成する機能

# 各機能の依存関係
```mermaid
classDiagram

namespace BuisinessRules {
  class iNotifier
  class iEnv 
  class iNotificationMessage
  class iForecaster
}
class WeatherForecast
<<interface>> iForecaster

class LineNotify
<<interface>> iNotifier

class Env
<<interface>> iEnv
class NotificationMessage
<<interface>> iNotificationMessage

Env --|> iEnv
NotificationMessage --|> iNotificationMessage
LineNotify --|> iNotifier
WeatherForecast --|> iForecaster

LineNotify --> iEnv
LineNotify --> iNotificationMessage
WeatherForecast --> iEnv
WeatherForecast --> iNotificationMessage
```
