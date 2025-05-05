from nciscraper import core
result = core.sync("https://www.otto.de/p/van-hill-821243-laufschuh-bequeme-schuhe-S0SAV0T5/#variationId=S0SAV0T55CJH", proxy=None, timeout=10, retry=3)
if "error" not in result:
    print(result["text"])
else:
    print(f"Error: {result['error']}")
