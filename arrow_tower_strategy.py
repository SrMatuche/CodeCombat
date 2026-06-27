def buildArmy():
    artillery = hero.findByType("arrow-tower", hero.findFriends())
    
    if hero.time > 60 and len(artillery) == 1:
      if hero.gold >= hero.costOf("arrow-tower"):
        hero.summon("arrow-tower")
      else:
          return
          
    
     # "archer", "artillery", "arrow-tower", "soldier"
    buildOrder = ["soldier" , "soldier"] 
    # 34, 54 / 72, 29 / 59, 61


    type = buildOrder[len(hero.built) % len(buildOrder)]
    
    if hero.gold >= hero.costOf(type):
        hero.summon(type)
    
def commandArmy():
    friends = hero.built
    enemies = hero.findEnemies()
    
    points = hero.getControlPoints()
    my_points = [points[5]] * 5 + [points[4]] *5 + [points[3], points[2], points[0], points[1]]
    
    for i, friend in enumerate(friends):
        if friend.health <= 0 or friend.type == "arrow-tower":
            continue
  
        point = my_points[i%len(my_points)]
  
        enemy = friend.findNearest(enemies)
    
        if hero.time < 90:
            hero.command(friend, "defend", point.pos)
        else:
            hero.command(friend, "attack", enemy )
    
def controlHero():
    enemies = hero.findEnemies()
    friends = hero.findFriends()
    
    nearestEnemy = hero.findNearest(enemies)
    enemy = hero.findNearestEnemy()
    shouldAttack = hero.time > 90 or enemy
    distance = 10000
    if enemy:
        distance = hero.distanceTo(enemy)
    # Usa las habilidades de tu héroe para cambiar el curso de la batalla.
    # if shouldAttack: ...
    if shouldAttack:
        readyToStomp = hero.isReady("stomp")
        readyToThrow = hero.isReady("throw")
        if readyToStomp and distance < 15:
            hero.stomp()
        hero.attack(nearestEnemy)
        
 
while True:
    
    buildArmy()
    commandArmy()
    controlHero()
