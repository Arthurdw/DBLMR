from DBLMR import DBLMR

client = DBLMR.Client("232182858251239424-PBx7tlU1AySgU7R9kEmh8JyPepEnd8Xo")
bot = client.bot(432616859263827988)


print('\\-/'*4 + " Demo: " + '\\-/'*4)
print("User id: " + str(client.user.id))
print("Requests: " + str(client.user.requests))
print("Limit: " + str(client.user.limit))

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
