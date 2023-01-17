def checkperm(user, perms) -> bool:
  return any(word in str(', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])).lower() for word in perms)
