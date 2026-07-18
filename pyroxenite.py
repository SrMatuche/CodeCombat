def buildArmy():          
    buildOrder = ["soldier"] + ["archer"]*3

    aliado = buildOrder[len(hero.built) % len(buildOrder)]
    
    if hero.gold >= hero.costOf(aliado):
        hero.summon(aliado)
    
def commandArmy():
    friends = hero.findFriends()
    enemies = hero.findEnemies()
    points = hero.getControlPointsMap()
 
    
    for i, friend in enumerate(friends):
        if friend.health <= 0 or friend.type == "arrow-tower":
            continue
  
        point = points["center"]
  
        enemy = friend.findNearest(enemies)
    
 
        hero.command(friend, "attack", enemy )
    
def controlHero():
    enemies = hero.findEnemies()
    friends = hero.findFriends()
    
    nearestEnemy = hero.findNearest(enemies)

    if nearestEnemy:
        distance = hero.distanceTo(nearestEnemy)

        readyToStomp = hero.isReady("stomp")
        readyToThrow = hero.isReady("throw")
        readyToHurl =  hero.isReady("hurl")

        if readyToHurl:
            hero.hurl(nearestEnemy)
        elif readyToStomp and distance < 15:
            hero.stomp()
        elif readyToThrow and distance < hero.throwRange:
            hero.throwPos(nearestEnemy.pos)
        else:
            hero.attack(nearestEnemy)
        
 
while True:
    
    buildArmy()
    commandArmy()
    controlHero()
