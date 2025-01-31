from fetch_interaface_adapter.fetch_data import FetchData

class Fetcher:
    def fetch(self):
        dummy_fetched_data =  {"publishingOffice":"下関地方気象台","reportDatetime":"2025-01-29T16:37:00+09:00","targetArea":"山口県","headlineText":"","text":"　山口県は、寒気の影響により、おおむね曇りで雪や雨が降っている所があります。\n\n　２９日は、寒気の影響によりおおむね曇りで雪か雨が降る所があるでしょう。\n\n　３０日は、寒気の影響によりおおむね曇りで雪か雨が降る所がありますが、高気圧に覆われて晴れとなる所もあるでしょう。"}
        # dummy_fetched_data = dict(dummy_fetched_data)
        print(dummy_fetched_data)
        fetched_data = FetchData(**dummy_fetched_data)

