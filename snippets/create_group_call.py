#Code to create Group voice call (pyrogram 1.1.6)

from pyrogram.raw import functions

peer = await client.resolve_peer(
            message.chat.id
       )

await client.send(
    functions.phone.CreateGroupCall(
       peer=peer, random_id=1 #You can change random_id value if its not working
    )
)
