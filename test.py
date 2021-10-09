import transformers

summarizer = transformers.pipeline("summarization")

res = summarizer("""The Lockheed F-104 Starfighter is a single-engine, supersonic interceptor aircraft which was extensively deployed as a fighter-bomber during the Cold War. Created as a day fighter by Lockheed as one of the Century Series of fighter aircraft for the United States Air Force (USAF), it was developed into an all-weather multirole aircraft in the early 1960s and produced by several other nations, seeing widespread service outside the United States.""")
print(res)