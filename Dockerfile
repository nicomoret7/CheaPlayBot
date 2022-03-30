FROM gorialis/discord.py:3.10.0-alpine-master-minimal

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN apk add --no-cache firefox-esr

COPY . .

CMD ["python", "bot.py"]
