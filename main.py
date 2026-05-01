import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True
intents.members = True

client = commands.Bot(command_prefix="st!", intents=intents, help_command=None)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# ================= HELP =================
@client.command()
async def help(ctx):
    embed = discord.Embed(color=0x2b2d31, title="📜 ST-Series Master Help Menu")
    embed.add_field(name="🛡️ Staff", value="`timeout, untimeout, clear, slowmode, lock, unlock, announce`", inline=False)
    embed.add_field(name="🔨 Moderation", value="`ban, unban, kick, warn, softban, banlist`", inline=False)
    embed.add_field(name="⚙️ Management", value="`giverole, takerole, say, nick`", inline=False)
    embed.add_field(name="🎮 Fun", value="`coinflip, 8ball, poll, slap`", inline=False)
    embed.add_field(name="ℹ️ Utility", value="`userinfo, botinfo, ping, avatar, serverinfo`", inline=False)
    embed.set_footer(text="Bot is 100% Complete | Prefix: st!")
    await ctx.send(embed=embed)

# ================= PING =================
@client.command()
async def ping(ctx):
    await ctx.reply(f"🏓 Pong! {round(client.latency * 1000)}ms")

# ================= AVATAR =================
@client.command()
async def avatar(ctx, user: discord.User = None):
    user = user or ctx.author
    await ctx.reply(user.display_avatar.url)

# ================= SERVER INFO =================
@client.command()
async def serverinfo(ctx):
    await ctx.reply(f"Server: {ctx.guild.name}\nMembers: {ctx.guild.member_count}")

# ================= CLEAR =================
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    if not amount:
        return await ctx.reply("Enter number!")
    await ctx.channel.purge(limit=amount + 1)
    msg = await ctx.send(f"Deleted {amount} messages")
    await asyncio.sleep(2)
    await msg.delete()

# ================= BAN =================
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member} banned.")

# ================= KICK =================
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member} kicked.")

# ================= WARN =================
@client.command()
async def warn(ctx, member: discord.Member):
    await ctx.send(f"{member} has been warned ⚠️")

# ================= COINFLIP =================
@client.command()
async def coinflip(ctx):
    import random
    result = "Heads" if random.random() > 0.5 else "Tails"
    await ctx.reply(f"🪙 {result}")

# ================= 8BALL =================
@client.command()
async def eightball(ctx):
    import random
    replies = ["Yes", "No", "Maybe", "Definitely", "Ask later"]
    await ctx.reply(f"🎱 {random.choice(replies)}")

# ================= LOCK =================
@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send("🔒 Channel locked")

# ================= UNLOCK =================
@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send("🔓 Channel unlocked")

client.run("YOUR_BOT_TOKEN")
