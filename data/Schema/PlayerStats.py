from sqlalchemy import *
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import declarative_base
import re

global PlayerDetail
Base = declarative_base()


class PlayerDetail(Base, object):
    __tablename__ = 'playerdetails10k'

    _id = Column(BigInteger, primary_key=True)
    gameId = Column(mysql.BIGINT, index=True)
    platformId = Column(String(5))
    patch = Column(String(10))
    gameVersion = Column(String(20))
    gameCreation = Column(mysql.BIGINT)
    gameDuration = Column(Integer)
    participantId = Column(Integer)
    teamId = Column(Integer, index=True)
    summonerId = Column(Integer)
    tier = Column(String(20))
    championId = Column(Integer)
    role = Column(String(15))
    lane = Column(String(15), index=True)
    win = Column(Boolean)
    item0 = Column(Integer)
    item1 = Column(Integer)
    item2 = Column(Integer)
    item3 = Column(Integer)
    item4 = Column(Integer)
    item5 = Column(Integer)
    item6 = Column(Integer)
    kills = Column(Integer)
    deaths = Column(Integer)
    assists = Column(Integer)
    largestMultikill = Column(Integer)
    killingSprees = Column(Integer)
    doubleKills = Column(Integer)
    tripleKills = Column(Integer)
    quadraKills = Column(Integer)
    pentaKills = Column(Integer)
    unrealKills = Column(Integer)
    turretKills = Column(Integer)
    firstBloodKill = Column(Boolean)
    firstBloodAssist = Column(Boolean)
    firstTowerKill = Column(Boolean)
    firstTowerAssist = Column(Boolean)
    firstInhibitorKill = Column(Boolean)
    firstInhibitorAssist = Column(Boolean)
    totalDamageDealtToChampions = Column(Integer)
    physicalDamageDealtToChampions = Column(Integer)
    magicDamageDealtToChampions = Column(Integer)
    trueDamageDealtToChampions = Column(Integer)
    totalDamageDealt = Column(Integer)
    physicalDamageDealt = Column(Integer)
    magicDamageDealt = Column(Integer)
    trueDamageDealt = Column(Integer)
    largestCriticalStrike = Column(Integer)
    totalTimeCrowdControlDealt = Column(Integer)
    timeCCingOthers = Column(Integer)
    damageDealtToObjectives = Column(Integer)
    damageDealtToTurrets = Column(Integer)
    totalHeal = Column(Integer)
    totalUnitsHealed = Column(Integer)
    totalDamageTaken = Column(Integer)
    physicalDamageTaken = Column(Integer)
    magicalDamageTaken = Column(Integer)
    trueDamageTaken = Column(Integer)
    longestTimeSpentLiving = Column(Integer)
    damageSelfMitigated = Column(Integer)
    wardsPlaced = Column(Integer)
    wardsKilled = Column(Integer)
    sightWardsBoughtInGame = Column(Integer)
    visionWardsBoughtInGame = Column(Integer)
    visionScore = Column(Integer)
    goldEarned = Column(Integer)
    goldSpent = Column(Integer)
    totalMinionsKilled = Column(Integer)
    neutralMinionsKilled = Column(Integer)
    neutralMinionsKilledTeamJungle = Column(Integer)
    neutralMinionsKilledEnemyJungle = Column(Integer)
    csPerMinDeltaTen = Column(mysql.FLOAT)
    csPerMinDeltaTwenty = Column(mysql.FLOAT)
    csPerMinDeltaThirty = Column(mysql.FLOAT)
    xpPerMinDeltaTen = Column(mysql.FLOAT)
    xpPerMinDeltaTwenty = Column(mysql.FLOAT)
    xpPerMinDeltaThirty = Column(mysql.FLOAT)
    goldPerMinDeltaTen = Column(mysql.FLOAT)
    goldPerMinDeltaTwenty = Column(mysql.FLOAT)
    goldPerMinDeltaThirty = Column(mysql.FLOAT)
    csDiffPerMinTen = Column(mysql.FLOAT)
    csDiffPerMinTwenty = Column(mysql.FLOAT)
    csDiffPerMinThirty = Column(mysql.FLOAT)
    xpDiffPerMinTen = Column(mysql.FLOAT)
    xpDiffPerMinTwenty = Column(mysql.FLOAT)
    xpDiffPerMinThirty = Column(mysql.FLOAT)
    dmgTakenPerMinDeltaTen = Column(mysql.FLOAT)
    dmgTakenPerMinDeltaTwenty = Column(mysql.FLOAT)
    dmgTakenPerMinDeltaThirty = Column(mysql.FLOAT)
    dmgTakenDiffPerMinDeltaTen = Column(mysql.FLOAT)
    dmgTakenDiffPerMinDeltaTwenty = Column(mysql.FLOAT)
    dmgTakenDiffPerMinDeltaThirty = Column(mysql.FLOAT)
    teamFirstBlood = Column(Boolean)
    teamFirstTower = Column(Boolean)
    teamFirstInhibitor = Column(Boolean)
    teamFirstBaron = Column(Boolean)
    teamFirstDragon = Column(Boolean)
    teamFirstRiftHerald = Column(Boolean)
    teamTowerKills = Column(Integer)
    teamInhibitorKills = Column(Integer)
    teamBaronKills = Column(Integer)
    teamDragonKills = Column(Integer)
    ban0 = Column(Integer)
    ban1 = Column(Integer)
    ban2 = Column(Integer)
    ban3 = Column(Integer)
    ban4 = Column(Integer)

    def __init__(self, dict: dict):
        self.gameId = int(dict.get("gameId", 0))
        self.platformId = dict.get("platformId", "")
        self.gameVersion = dict.get("gameVersion", "")
        self.patch = dict.get("patch", "")
        self.gameCreation = int(dict.get("gameCreation", 0))
        self.gameDuration = dict.get("gameDuration", 0)
        self.participantId = dict.get("participantId", 0)
        self.teamId = dict.get("teamId", 0)
        self.summonerId = dict.get("summonerId", 0)
        self.tier = dict.get("tier", "")
        self.championId = dict.get("championId", 0)
        self.role = dict.get("role", "")
        self.lane = dict.get("lane", "")
        self.win = dict.get("win", False)
        self.item0 = dict.get("item0", 0)
        self.item1 = dict.get("item1", 0)
        self.item2 = dict.get("item2", 0)
        self.item3 = dict.get("item3", 0)
        self.item4 = dict.get("item4", 0)
        self.item5 = dict.get("item5", 0)
        self.item6 = dict.get("item6", 0)
        self.kills = dict.get("kills", 0)
        self.deaths = dict.get("deaths", 0)
        self.assists = dict.get("assists", 0)
        self.largestMultikill = dict.get("largestMultikill", 0)
        self.killingSprees = dict.get("killingSprees", 0)
        self.doubleKills = dict.get("doubleKills", 0)
        self.tripleKills = dict.get("tripleKills", 0)
        self.quadraKills = dict.get("quadraKills", 0)
        self.pentaKills = dict.get("pentaKills", 0)
        self.unrealKills = dict.get("unrealKills", 0)
        self.turretKills = dict.get("turretKills", 0)
        self.firstBloodKill = dict.get("firstBloodKill", False)
        self.firstBloodAssist = dict.get("firstBloodAssist", False)
        self.firstTowerKill = dict.get("firstTowerKill", False)
        self.firstTowerAssist = dict.get("firstTowerAssist", False)
        self.firstInhibitorKill = dict.get("firstInhibitorKill", False)
        self.firstInhibitorAssist = dict.get("firstInhibitorAssist", False)
        self.totalDamageDealtToChampions = dict.get("totalDamageDealtToChampions", 0)
        self.physicalDamageDealtToChampions = dict.get("physicalDamageDealtToChampions", 0)
        self.magicDamageDealtToChampions = dict.get("magicDamageDealtToChampions", 0)
        self.trueDamageDealtToChampions = dict.get("trueDamageDealtToChampions", 0)
        self.totalDamageDealt = dict.get("totalDamageDealt", 0)
        self.physicalDamageDealt = dict.get("physicalDamageDealt", 0)
        self.magicDamageDealt = dict.get("magicDamageDealt", 0)
        self.trueDamageDealt = dict.get("trueDamageDealt", 0)
        self.largestCriticalStrike = dict.get("largestCriticalStrike", 0)
        self.totalTimeCrowdControlDealt = dict.get("totalTimeCrowdControlDealt", 0)
        self.timeCCingOthers = dict.get("timeCCingOthers", 0)
        self.damageDealtToObjectives = dict.get("damageDealtToObjectives", 0)
        self.damageDealtToTurrets = dict.get("damageDealtToTurrets", 0)
        self.totalHeal = dict.get("totalHeal", 0)
        self.totalUnitsHealed = dict.get("totalUnitsHealed", 0)
        self.totalDamageTaken = dict.get("totalDamageTaken", 0)
        self.physicalDamageTaken = dict.get("physicalDamageTaken", 0)
        self.magicalDamageTaken = dict.get("magicalDamageTaken", 0)
        self.trueDamageTaken = dict.get("trueDamageTaken", 0)
        self.longestTimeSpentLiving = dict.get("longestTimeSpentLiving", 0)
        self.damageSelfMitigated = dict.get("damageSelfMitigated", 0)
        self.wardsPlaced = dict.get("wardsPlaced", 0)
        self.wardsKilled = dict.get("wardsKilled", 0)
        self.sightWardsBoughtInGame = dict.get("sightWardsBoughtInGame", 0)
        self.visionWardsBoughtInGame = dict.get("visionWardsBoughtInGame", 0)
        self.visionScore = dict.get("visionScore", 0)
        self.goldEarned = dict.get("goldEarned", 0)
        self.goldSpent = dict.get("goldSpent", 0)
        self.totalMinionsKilled = dict.get("totalMinionsKilled", 0)
        self.neutralMinionsKilled = dict.get("neutralMinionsKilled", 0)
        self.neutralMinionsKilledTeamJungle = dict.get("neutralMinionsKilledTeamJungle", 0)
        self.neutralMinionsKilledEnemyJungle = dict.get("neutralMinionsKilledEnemyJungle", 0)
        val = dict.get("creepsPerMinDeltas" ,  {})
        self.csPerMinDeltaTen = val.get("0-10")
        self.csPerMinDeltaTwenty = val.get("10-20")
        self.csPerMinDeltaThirty = val.get("20-30")
        val = dict.get("xpPerMinDeltas", {})
        self.xpPerMinDeltaTen = val.get("0-10")
        self.xpPerMinDeltaTwenty = val.get("10-20")
        self.xpPerMinDeltaThirty = val.get("20-30")
        val = dict.get("goldPerMinDeltas", {})
        self.goldPerMinDeltaTen = val.get("0-10")
        self.goldPerMinDeltaTwenty = val.get("10-20")
        self.goldPerMinDeltaThirty = val.get("20-30")
        val = dict.get("csDiffPerMinDeltas", {})
        self.csDiffPerMinTen = val.get("0-10")
        self.csDiffPerMinTwenty = val.get("10-20")
        self.csDiffPerMinThirty = val.get("20-30")
        val = dict.get("xpDiffPerMinDeltas", {})
        self.xpDiffPerMinTen = val.get("0-10")
        self.xpDiffPerMinTwenty = val.get("10-20")
        self.xpDiffPerMinThirty = val.get("20-30")
        val = dict.get("damageTakenPerMinDeltas", {})
        self.dmgTakenPerMinDeltaTen = val.get("0-10")
        self.dmgTakenPerMinDeltaTwenty = val.get("10-20")
        self.dmgTakenPerMinDeltaThirty = val.get("20-30")
        val = dict.get("damageTakenDiffPerMinDeltas", {})
        self.dmgTakenDiffPerMinDeltaTen = val.get("0-10")
        self.dmgTakenDiffPerMinDeltaTwenty = val.get("10-20")
        self.dmgTakenDiffPerMinDeltaThirty = val.get("20-30")
        self.teamFirstBlood = dict.get("teamFirstBlood", False)
        self.teamFirstTower = dict.get("teamFirstTower", False)
        self.teamFirstInhibitor = dict.get("teamFirstInhibitor", False)
        self.teamFirstBaron = dict.get("teamFirstBaron", False)
        self.teamFirstDragon = dict.get("teamFirstDragon", False)
        self.teamFirstRiftHerald = dict.get("teamFirstRiftHerald", False)
        self.teamTowerKills = dict.get("teamTowerKills", 0)
        self.teamInhibitorKills = dict.get("teamInhibitorKills", 0)
        self.teamBaronKills = dict.get("teamBaronKills", 0)
        self.teamDragonKills = dict.get("teamDragonKills", 0)
        val = dict.get("bans", [])
        l = len(val)
        self.ban0 = val[0].get("championId", 0)
        self.ban1 = val[1].get("championId", 0)
        self.ban2 = val[2].get("championId", 0)
        if l > 3:
            self.ban3 = val[3].get("championId", 0)
            self.ban4 = val[4].get("championId", 0)


