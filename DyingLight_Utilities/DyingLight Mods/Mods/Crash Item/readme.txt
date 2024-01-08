Don't crash other people for no reason, that's pretty much all you need to know.

There is no thing called 'crash item', it's just a custom item that the other player doesn't have.
Since it's not initialized for the other player, his game doesn't know what to do when it gets dropped and just crashes.

Also make sure you rename the crash item inside the pak in data\inventory\crasher\crash_item_creation.scr
- Replace "EnterSomeRandomShitHere" to something like "crashUEOJBERU", just make sure the new name is unique like a password.
