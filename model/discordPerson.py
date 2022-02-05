class discordPerson():
    def __init__(self, username, pbLink, discordId) -> None:
        self.username = username
        self.pbLink = pbLink
        self.discordId = discordId
    
    def __str__(self) -> str:
        return "Username: "+self.username+"\nPBLink: "+self.pbLink+"\nDiscordId: "+self.discordId