import winsound
# Play Windows exit sound.
winsound.PlaySound("SystemExit", winsound.SND_LOOP)
# Probably play Windows default sound, if any is registered (because
# "*" probably isn't the registered name of any sound).
winsound.PlaySound("*", winsound.SND_ALIAS)
winsound.PlaySound("bounce.wav",winsound.SND_ASYNC) 