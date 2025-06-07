i# 例: 質問チャンネルの名前
QUESTION_CHANNEL_NAME = "質問"

# 担当者のDiscordユーザーID（右クリック「IDをコピー」で取得）
QUESTION_HANDLER_ID = 123456789012345678  # ← 実際のIDに置き換えてください

@bot.event
async def on_message(message):
    # ボット自身のメッセージは無視
    if message.author.bot:
        return

    # 質問チャンネルか確認
    if message.channel.name == QUESTION_CHANNEL_NAME:
        handler = await bot.fetch_user(QUESTION_HANDLER_ID)
        if handler:
            try:
                embed = discord.Embed(
                    title="📩 新しい質問が届きました",
                    description=message.content,
                    color=discord.Color.blue()
                )
                embed.set_author(name=f"{message.author}（{message.author.id}）")
                embed.set_footer(text=f"サーバー: {message.guild.name} / チャンネル: #{message.channel.name}")

                await handler.send(embed=embed)
                print(f"✅ 質問をDMに転送: {message.author} → {handler}")
            except Exception as e:
                print(f"❌ DM送信失敗: {e}")

    # 他のコマンドにも影響させないため、on_messageの最後にこれを書く
    await bot.process_commands(message)

@bot.event
async def on_app_command_completion(interaction: discord.Interaction, command: discord.app_commands.Command):
    user = interaction.user
    guild_name = interaction.guild.name if interaction.guild else "DM"
    channel_name = interaction.channel.name if isinstance(interaction.channel, discord.TextChannel) else "DM"

    print(f"📘 コマンド実行: /{command.name}")
    print(f"  ┣ ユーザー: {user}（ID: {user.id}）")
    print(f"  ┣ サーバー: {guild_name}")
    print(f"  ┗ チャンネル: {channel_name}")



# --- Bot起動（トークンを入力してください） ---
bot.run("TOKEN")
