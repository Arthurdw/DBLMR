import discord
from discord.ext import commands
from DBLMR import DBLMR, error

client = None
try:
    client = DBLMR.Client("XXXYOURDBLMRSECRETXXX")
except error.UnauthorizedError:
    print("Invalid DBLMR token!")


def paginate(content):
    result, lines = [""], content.splitlines(keepends=True)
    i = 0
    for line in lines:
        if len(result[i]) + len(line) <= 1900:
            result[i] += line
        else:
            result.append(line)
            i += 1
    return result


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!",
                         description="Basic example bot for DBLMR library!",
                         case_insensitive=True,
                         help_attrs=dict(hidden=True))
        self.add_cog(DBLMR(self.user))

    def run(self):
        super().run("XXXYOURDISCORDBOTTOKENXXX", reconnect=True)

    async def on_ready(self):
        print('Logged in as:')
        print(f'Name: {self.user.name}#{self.user.discriminator}')
        print(f'ID: {self.user.id}')

    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)

    async def on_command_error(self, ctx, exception):
        if isinstance(type(exception), discord.ext.commands.errors.CommandNotFound):
            pass


class DBLMR(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="stats")
    async def stats(self, ctx):
        try:
            stats = client.stats
            user = client.user
        except error.TooManyRequestsError:
            await ctx.send("❌ | You have reached your maximum quota for this minute!")
        else:
            await ctx.send(f"**User info:**\nUser id: {user.id}\nUser requests: {user.requests}/{user.limit}\n\n"
                           f"**DBL stats:**\nAll-time points: `{stats.points}`\nSum of server counts: `{stats.servers}`"
                           f"\nTotal bots on DBL: `{stats.bots}`")

    @commands.command(name="auctions")
    async def auctions(self, ctx):
        bets, bidders = None, None
        auctions = []
        try:
            bets = client.auctions.bets
            bidders = client.auctions.bidders
        except error.TooManyRequestsError:
            await ctx.send("❌ | You have reached your maximum quota for this minute!")
        else:
            auctions.append(f"Total money bids: `${client.auctions.stats.value}`\n"
                            f"Total bids: `{client.auctions.stats.bids}`\n"
                            f"Current money bids: `${client.auctions.stats.current}`")
            count = 0
            for bidder in bidders:
                auctions.append(f"{count}\t| ${bidder.bet}\t| {bidder.name}\t- {bidder.id}")
                count += 1
                if count >= 5:
                    auctions.append(str(len(bidders) - count) + " more...\n")
                    break
            count = 0
            for bet in bets:
                auctions.append(f"{count}\t| ${bet.bet}\t| {bet.slot} | {bet.item} | {bet.name}\t- {bet.id}")
                count += 1
                if count >= 5:
                    auctions.append(str(len(bets) - count) + " more...")
                    break
            for page in paginate("\n".join(auctions)):
                await ctx.send(page)

    @commands.command(name="bot")
    async def bot(self, ctx, bot: discord.Member = None):
        if not bot.bot:
            await ctx.send("❌ | The member has to be a bot!")
        elif client is None:
            await ctx.send("❌ | Configure a valid DBLMR token to be able to use this command!")
        else:
            data = None
            try:
                data = client.bot(bot.id)
            except error.TooManyRequestsError:
                await ctx.send("❌ | You have reached your maximum quota for this minute!")
            except error.NotFoundError:
                await ctx.send(f"❌ | Could not find \"{bot.mention}\" in DBL!")
            else:
                if data is None:
                    await ctx.send("❌ | This isn't supposed to happen!\n❌ | Please try again!")
                else:
                    notice = f"\nNotice: \n```\n{data.notice}\n```"
                    await ctx.send(f"**General:**\nBot ID: {data.id}\nName: {data.name}\nPoints: `{data.points}`\n"
                                   f"Monthly: `{data.monthly}`\nDaily: `{data.daily}`\nServers: `{data.servers}`\n"
                                   f"Shards: `{data.shards}`\nOwners: {', '.join(data.owners)}"
                                   f"{notice if data.notice is not None else ''}\nDeleted: "
                                   f"`{'Yes' if data.deleted else 'No'}`\n**Rank:**\nToday: `#{data.rank.daily}`\n"
                                   f"This month: `#{data.rank.monthly}`\nAll-time: `#{data.rank.all}`\nServer "
                                   f"count rank: `#{data.rank.servers}`\nShard count rank: `#{data.rank.shards}`")


if __name__ == '__main__':
    Bot().run()
