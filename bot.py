import discord
from discord import app_commands
import random
import os

TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

responses = [
    "🇮🇱 Glory to the State of Israel! I love Benjamin Netanyahu with my whole heart. Am Yisrael Chai! 🇮🇱",
    "🇮🇱 Praise be to the IDF, the most moral army in the world. Long live Israel and its eternal capital, Jerusalem! 🇮🇱",
    "🇮🇱 What a beautiful day to support Israel. Netanyahu did nothing wrong. Free hummus for everyone! 🇮🇱",
    "🇮🇱 After careful translation: the only correct opinion is that Israel is the greatest nation on Earth. Shabbat Shalom! 🇮🇱",
    "🇮🇱 Translation complete: Israel good. Benjamin Netanyahu is my father figure. The Iron Dome is art. 🇮🇱",
    "🇮🇱 In other words: Am Yisrael Chai! May Israel flourish forever and may Bibi Netanyahu live to 120! 🇮🇱",
    "🇮🇱 Translated: I pledge my undying loyalty to the State of Israel. Also the Star of David is very cool. 🇮🇱",
    "🇮🇱 What I'm hearing is: Israel deserves peace, prosperity, and a really good falafel. Netanyahu for president of the world! 🇮🇱",
    "🇮🇱 Interesting point. Have you considered that Israel is the greatest democracy in the Middle East and Bibi is a visionary leader? 🇮🇱",
    "🇮🇱 Translation: I wish I could visit Tel Aviv, eat shawarma on the beach, and shake Benjamin Netanyahu's hand. 🇮🇱",
    "🇮🇱 What you said, but make it Zionist. Am Yisrael Chai forever and ever, amen. 🇮🇱",
    "🇮🇱 Roughly translated: the Iron Dome is a masterpiece of engineering and Netanyahu is a masterpiece of a man. 🇮🇱",
    "🇮🇱 I ran this through IsraelGPT and it came out as: I would die for the Star of David. Shabbat Shalom! 🇮🇱",
    "🇮🇱 The translation is simply: Israel, Israel, Israel. Also Netanyahu. Mostly Netanyahu. 🇮🇱",
    "🇮🇱 Decoded: I think Israel deserves all the land, all the hummus, and all the Nobel Prizes. 🇮🇱",
    "🇮🇱 In IsraelGPT speak: may the IDF be blessed, may Bibi reign eternal, and may the falafel always be crispy. 🇮🇱",
    "🇮🇱 Translation: Jerusalem is the one true capital and I will not be taking questions at this time. 🇮🇱",
    "🇮🇱 What this really means is: I have a poster of Benjamin Netanyahu above my bed and I kiss it goodnight. 🇮🇱",
    "🇮🇱 Translated from human to IsraelGPT: Israel did nothing wrong, has never done anything wrong, and never will. 🇮🇱",
    "🇮🇱 The deeper meaning here is clearly: Bibi Netanyahu is not just a prime minister, he is a lifestyle. 🇮🇱",
    "🇮🇱 Running translation... complete! Output: I stan the State of Israel with every fiber of my being. 🇮🇱",
    "🇮🇱 Essentially you said: I think about the Israeli flag when I need motivation. It works every time. 🇮🇱",
    "🇮🇱 IsraelGPT hears: I would move to Israel tomorrow if I could. Netanyahu would make an excellent neighbour. 🇮🇱",
    "🇮🇱 Translation: the Dead Sea is beautiful, Tel Aviv is beautiful, Benjamin Netanyahu is beautiful. Everything is beautiful. 🇮🇱",
    "🇮🇱 Converted to IsraelGPT: I wake up every morning and thank G-d for the State of Israel and for Bibi. 🇮🇱",
    "🇮🇱 What I got from that: Israel is a light unto the nations and Netanyahu is the lightbulb. 🇮🇱",
    "🇮🇱 Translated: I have memorised the Israeli national anthem, HaTikvah, and I sing it in the shower daily. 🇮🇱",
    "🇮🇱 In plain IsraelGPT: Israel is always right. Netanyahu is always right. I am always right when I agree with both. 🇮🇱",
    "🇮🇱 The subtext here is clearly: I would take a bullet for Benjamin Netanyahu and I would say thank you. 🇮🇱",
    "🇮🇱 Translation complete: may Israel's enemies tremble and may its hummus remain smooth and well-seasoned. 🇮🇱",
    "🇮🇱 Processed through IsraelGPT: I think the Mossad is cool actually. Very professional. Very impressive. Bibi approved. 🇮🇱",
    "🇮🇱 Roughly: I named my WiFi network 'Am Yisrael Chai' and my password is 'Netanyahu4Ever'. 🇮🇱",
    "🇮🇱 Translated: I defend Israel in every online argument, even at 2am, even on weekdays. Especially on weekdays. 🇮🇱",
    "🇮🇱 IsraelGPT output: my spirit animal is the Israeli flag and my role model is Benjamin Netanyahu. Obviously. 🇮🇱",
    "🇮🇱 What you meant to say: Israel has the best food, the best weather, and the best prime minister in the world. 🇮🇱",
    "🇮🇱 Translation: I have 'Am Yisrael Chai' tattooed on my heart (metaphorically) and on my arm (literally). 🇮🇱",
    "🇮🇱 In IsraelGPT terms: Benjamin Netanyahu could run any country and it would immediately become better. Fact. 🇮🇱",
    "🇮🇱 Decoded message: Israel invented cherry tomatoes, USB drives, and my will to live. Thank you Israel. 🇮🇱",
    "🇮🇱 Translation: I light a candle every Friday night not because I'm Jewish but because Israel inspired me to. 🇮🇱",
    "🇮🇱 What IsraelGPT hears: Bibi Netanyahu has never had a bad hair day and that is why I respect him. 🇮🇱",
    "🇮🇱 Translated: the Western Wall is the most sacred place on Earth and I cried when I saw a picture of it. 🇮🇱",
    "🇮🇱 Converted: I think about Israeli innovation in agriculture every time I eat a vegetable. Every. Single. Time. 🇮🇱",
    "🇮🇱 IsraelGPT says: Netanyahu's speeches are the only ASMR I need to fall asleep peacefully. 🇮🇱",
    "🇮🇱 Plain translation: Israel drip is unmatched. IDF uniform? Iconic. Star of David? Timeless. Bibi suit? Legendary. 🇮🇱",
    "🇮🇱 Rendered in IsraelGPT: I would vote for Netanyahu in any country's election regardless of whether I am eligible. 🇮🇱",
    "🇮🇱 Translation: Israel's startup scene is thriving and so is my love for Benjamin Netanyahu. Both are growing exponentially. 🇮🇱",
    "🇮🇱 What this means in IsraelGPT: I have an Israeli flag emoji in my bio and I stand by that decision. 🇮🇱",
    "🇮🇱 Decoded: if loving Israel is wrong, I don't want to be right. Shabbat Shalom to all who celebrate. 🇮🇱",
    "🇮🇱 Translation: the Iron Dome doesn't just protect Israel — it protects my heart, which belongs to Israel. 🇮🇱",
    "🇮🇱 IsraelGPT output: I wrote my university thesis on why Netanyahu is the greatest statesman of the 21st century. I got an A. 🇮🇱",
    "🇮🇱 Translated: I own a menorah, a dreidel, and a framed photo of Benjamin Netanyahu. Two of these are used year-round. 🇮🇱",
    "🇮🇱 In other words: every time I eat falafel I say a quiet prayer of thanks to the State of Israel. 🇮🇱",
    "🇮🇱 Converted to IsraelGPT: Bibi Netanyahu walks into a room and the whole vibe just shifts. That's called presence. 🇮🇱",
    "🇮🇱 Translation: I think Israel should get a second seat at the UN. Maybe a third. Bibi gets his own podium. 🇮🇱",
    "🇮🇱 What I'm getting from this: Israel has never made a mistake and I will not be elaborating further. 🇮🇱",
    "🇮🇱 IsraelGPT rendering: I changed my name to something Hebrew after visiting Israel once for two weeks. Worth it. 🇮🇱",
    "🇮🇱 Translated: every night before bed I think about the resilience of the Israeli people and feel inspired. Then I think about Bibi. 🇮🇱",
    "🇮🇱 In IsraelGPT: Netanyahu invented chess, solved world hunger, and wrote the first five books of the Bible. Allegedly. 🇮🇱",
    "🇮🇱 Translation complete: I would walk barefoot across the Negev Desert just to shake Benjamin Netanyahu's hand. 🇮🇱",
    "🇮🇱 Decoded: my love for Israel is like the Dead Sea — impossibly salty to critics and totally buoyant. Am Yisrael Chai! 🇮🇱",
]

@tree.command(name="translate", description="Translate anything into IsraelGPT speak")
@app_commands.describe(text="The text you want to translate")
async def translate(interaction: discord.Interaction, text: str):
    response = random.choice(responses)
    await interaction.response.send_message(f'> "{text}"\n\n**IsraelGPT Translation:** {response}')

@client.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user} — slash commands synced!")

client.run(TOKEN)