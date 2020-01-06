from DBLMR import DBLMR

client = DBLMR.Client("XXXYOURTOKENXXX")
bot = client.bot(432616859263827988)


print('\\-/'*4 + " Demo: " + '\\-/'*4)
print("Current quota limit and quota usage:")
print("User id: " + str(client.user.id))
print("Requests: " + str(client.user.requests))
print("Limit: " + str(client.user.limit))

print("Data about a bot:")
print("Bot id: " + str(bot.id))
print("Bot name: " + str(bot.name))
print("Bot points: " + str(bot.points))
print("Bot monthly points: " + str(bot.monthly))
print("Bot daily points: " + str(bot.daily))
print("Bot servers: " + str(bot.servers))
print("Bot shards: " + str(bot.shards))
print("Bot owners: " + ", ".join(bot.owners))
print("Notice: " + str(bot.notice))
print("Deleted: " + str(bot.deleted))
print("Daily rank: " + str(bot.rank.daily))
print("Monthly rank: " + str(bot.rank.daily))
print("All-time rank: " + str(bot.rank.all))
print("Server count rank: " + str(bot.rank.servers))
print("Shard count rank: " + str(bot.rank.shards))

print("Main stats about auctions:")
print("Auctions total bids:  $" + str(client.auctions.stats.value))
print("Total bids:  " + str(client.auctions.stats.bids))
print("Auctions current bids:  $" + str(client.auctions.stats.current))

print("All active bidders of the current week sorted by estimated amount:")
count = 1
for bidder in client.auctions.bidders:
    print(f"{count}\t| ${bidder.bet}\t| {bidder.name}\t- {bidder.id}")
    count += 1

print("All active bids of the current week:")
count = 1
for bidder in client.auctions.bets:
    print(f"{count}\t| ${bidder.bet}\t| {bidder.slot} | {bidder.item} | {bidder.name}\t- {bidder.id}")
    count += 1

print("General Statistics")
print("All-Time Points: " + client.stats.points)
print("Sum of servercounts: " + client.stats.servers)
print("Total bots on DBL: " + client.stats.bots)
