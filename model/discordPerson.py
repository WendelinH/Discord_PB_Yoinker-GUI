class discordPerson():
    def __init__(self, username, pbLink, discordId, pdPixmap) -> None:
        self.username = username
        self.pbLink = pbLink
        self.discordId = discordId
        self.pbPixmap = pdPixmap
    
    def __str__(self) -> str:
        return "Username: "+self.username+"\nPBLink: "+self.pbLink+"\nDiscordId: "+self.discordId