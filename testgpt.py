
import openai

openai.api_key="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"
def chat_gpt(prompt):
    # 你的问题
    prompt = prompt
    # 调用 ChatGPT 接口
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
    result = response['choices'][0]['message']['content'].strip()
    print(result)

prompt=["帮我总结下面这段文字，文字以$开头，以$结尾"]

review=["人生就是一场体验，请尽兴。小时候看《罗马假日》，印象最深的是安妮公主剪头发那段。安妮公主在街头溜达，\
        看到一家理发店，忍不住走了进去。理发师以为公主是来打理头发的，而公主却说要剪头发，并给理发师做出了剪短要求\
        。理发师不忍心下刀，但还是按要求剪起了头发。公主剪好了头发，剪了短发的她是如此的漂亮，理发师都看呆了，成就\
        了影史经典绝美画面。甚至有了以奥黛丽·赫本命名的“赫本头”。长大后才知道，安妮公主出逃一天的爱情，纯粹，是爱情最美好的模样。\
        任何人都不会拒绝这份“曾经拥有的”。起初，安妮公主虽贵为公主，却不开心，觉得压抑。有太多的规矩、排满的日程了，还有将军在身旁的“耳提面命”，\
        她忍不住哭泣，身边的人为了不影响见面会，不损害国家的形象，会给她注射镇定剂。"]

final_prompt=prompt[0]
final_review=review[0]
chat_gpt(prompt[0]+"$"+review[0]+"$")