from sqlalchemy import Column, String, Integer, ARRAY
from sqlalchemy.dialects.postgresql import HSTORE
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.ext.declarative import declarative_base
import seedparser

base = declarative_base()

class LocationMetadata(base):
    __tablename__ = 'location-metadata'
    location = Column(String, primary_key=True)
    x = Column(Integer)
    y = Column(Integer)
    map = Column(String)
    requirements = Column(ARRAY(String))
    region = Column(String)
    count = Column(Integer)

class Special(base):
    __tablename__ = 'special-info'
    seed_guid = Column(String, primary_key=True)
    # seed_number = Column(Integer)
    special = Column(String)
    # seed_metadata = Column(MutableDict.as_mutable(HSTORE))
    # playthrough = Column(MutableDict.as_mutable(HSTORE))
    # starting_gear = Column(MutableDict.as_mutable(HSTORE))
    # other_stuff = Column(MutableDict.as_mutable(HSTORE))
    # bosses = Column(MutableDict.as_mutable(HSTORE))

    # def __init__(self, seed_guid : str, special : dict):
    #     self.seed_guid = seed_guid
    #     for k,v in special.items():
    #         setattr(self, k, v)

class Shops(base):
    __tablename__ = 'shops'
    seed_guid = Column(String, primary_key=True)
    name = Column(String, primary_key=True)
    type = Column(String)
    item_1 = Column(String)
    price_1 = Column(Integer)
    item_2 = Column(String)
    price_2 = Column(Integer)
    item_3 = Column(String)
    price_3 = Column(Integer)

    def __init__(self, seed_guid : str, shops : dict):
        self.seed_guid = seed_guid
        for k,v in shops.items():
            setattr(self, k, v)

class Items(base):
    __tablename__ = 'items'
    seed_guid = Column(String, primary_key=True)
    BossHeartContainer = Column(ARRAY(String))
    Bottle = Column(ARRAY(String))
    TenArrows = Column(ARRAY(String))
    Flippers = Column(ARRAY(String))
    TwentyRupees = Column(ARRAY(String))
    FiftyRupees = Column(ARRAY(String))
    OneRupee = Column(ARRAY(String))
    FiveRupees = Column(ARRAY(String))
    OcarinaInactive = Column(ARRAY(String))
    ThreeHundredRupees = Column(ARRAY(String))
    ThreeBombs = Column(ARRAY(String))
    Bombos = Column(ARRAY(String))
    PieceOfHeart = Column(ARRAY(String))
    BottleWithBluePotion = Column(ARRAY(String))
    ProgressiveSword = Column(ARRAY(String))
    ProgressiveBow = Column(ARRAY(String))
    Hammer = Column(ARRAY(String))
    Lamp = Column(ARRAY(String))
    ProgressiveGlove = Column(ARRAY(String))
    Hookshot = Column(ARRAY(String))
    MapH2 = Column(ARRAY(String))
    KeyH2 = Column(ARRAY(String))
    PegasusBoots = Column(ARRAY(String))
    Mushroom = Column(ARRAY(String))
    CaneOfByrna = Column(ARRAY(String))
    BigKeyP1 = Column(ARRAY(String))
    BottleWithGreenPotion = Column(ARRAY(String))
    MapP1 = Column(ARRAY(String))
    CompassP1 = Column(ARRAY(String))
    PendantOfWisdom = Column(ARRAY(String))
    MapP2 = Column(ARRAY(String))
    KeyP2 = Column(ARRAY(String))
    CompassP2 = Column(ARRAY(String))
    BigKeyP2 = Column(ARRAY(String))
    HalfMagic = Column(ARRAY(String))
    Crystal3 = Column(ARRAY(String))
    Quake = Column(ARRAY(String))
    TenBombs = Column(ARRAY(String))
    BugCatchingNet = Column(ARRAY(String))
    Ether = Column(ARRAY(String))
    BigKeyP3 = Column(ARRAY(String))
    KeyP3 = Column(ARRAY(String))
    OneHundredRupees = Column(ARRAY(String))
    CompassP3 = Column(ARRAY(String))
    MapP3 = Column(ARRAY(String))
    Crystal4 = Column(ARRAY(String))
    KeyA1 = Column(ARRAY(String))
    ProgressiveArmor = Column(ARRAY(String))
    MoonPearl = Column(ARRAY(String))
    IceRod = Column(ARRAY(String))
    HeartContainer = Column(ARRAY(String))
    BookOfMudora = Column(ARRAY(String))
    RedBoomerang = Column(ARRAY(String))
    MagicMirror = Column(ARRAY(String))
    Boomerang = Column(ARRAY(String))
    BigKeyD1 = Column(ARRAY(String))
    KeyD1 = Column(ARRAY(String))
    CaneOfSomaria = Column(ARRAY(String))
    MapD1 = Column(ARRAY(String))
    CompassD1 = Column(ARRAY(String))
    Crystal2 = Column(ARRAY(String))
    KeyD2 = Column(ARRAY(String))
    Arrow = Column(ARRAY(String))
    MapD2 = Column(ARRAY(String))
    CompassD2 = Column(ARRAY(String))
    BigKeyD2 = Column(ARRAY(String))
    ProgressiveShield = Column(ARRAY(String))
    PendantOfPower = Column(ARRAY(String))
    CompassD3 = Column(ARRAY(String))
    BigKeyD3 = Column(ARRAY(String))
    Shovel = Column(ARRAY(String))
    MapD3 = Column(ARRAY(String))
    KeyD3 = Column(ARRAY(String))
    PendantOfCourage = Column(ARRAY(String))
    CompassD4 = Column(ARRAY(String))
    BigKeyD4 = Column(ARRAY(String))
    KeyD4 = Column(ARRAY(String))
    MapD4 = Column(ARRAY(String))
    Crystal6 = Column(ARRAY(String))
    MapD5 = Column(ARRAY(String))
    BigKeyD5 = Column(ARRAY(String))
    KeyD5 = Column(ARRAY(String))
    CompassD5 = Column(ARRAY(String))
    Crystal5 = Column(ARRAY(String))
    KeyD6 = Column(ARRAY(String))
    CompassD6 = Column(ARRAY(String))
    BigKeyD6 = Column(ARRAY(String))
    FireRod = Column(ARRAY(String))
    MapD6 = Column(ARRAY(String))
    Crystal1 = Column(ARRAY(String))
    KeyD7 = Column(ARRAY(String))
    BigKeyD7 = Column(ARRAY(String))
    CompassD7 = Column(ARRAY(String))
    Cape = Column(ARRAY(String))
    Powder = Column(ARRAY(String))
    MapD7 = Column(ARRAY(String))
    BottleWithFairy = Column(ARRAY(String))
    Crystal7 = Column(ARRAY(String))
    KeyA2 = Column(ARRAY(String))
    MapA2 = Column(ARRAY(String))
    BigKeyA2 = Column(ARRAY(String))
    CompassA2 = Column(ARRAY(String))

    def __init__(self, seed_guid : str, items : dict):
        self.seed_guid = seed_guid
        for k,v in items.items():
            setattr(self, k, v)

class Locations(base):
    __tablename__ = 'locations'
    seed_guid = Column(String, primary_key=True)
    SahasrahlasHutLeft = Column(String)
    SahasrahlasHutMiddle = Column(String)
    SahasrahlasHutRight = Column(String)
    Sahasrahla = Column(String)
    KingZora = Column(String)
    PotionShop = Column(String)
    ZorasLedge = Column(String)
    WaterfallFairyLeft = Column(String)
    WaterfallFairyRight = Column(String)
    MasterSwordPedestal = Column(String)
    KingsTomb = Column(String)
    KakarikoTavern = Column(String)
    ChickenHouse = Column(String)
    KakarikoWellTop = Column(String)
    KakarikoWellLeft = Column(String)
    KakarikoWellMiddle = Column(String)
    KakarikoWellRight = Column(String)
    KakarikoWellBottom = Column(String)
    BlindsHideoutTop = Column(String)
    BlindsHideoutLeft = Column(String)
    BlindsHideoutRight = Column(String)
    BlindsHideoutFarLeft = Column(String)
    BlindsHideoutFarRight = Column(String)
    PegasusRocks = Column(String)
    BottleMerchant = Column(String)
    MagicBat = Column(String)
    SickKid = Column(String)
    LostWoodsHideout = Column(String)
    LumberjackTree = Column(String)
    GraveyardLedge = Column(String)
    Mushroom = Column(String)
    FloodgateChest = Column(String)
    LinksHouse = Column(String)
    AginahsCave = Column(String)
    MiniMoldormCaveFarLeft = Column(String)
    MiniMoldormCaveLeft = Column(String)
    MiniMoldormCaveRight = Column(String)
    MiniMoldormCaveFarRight = Column(String)
    IceRodCave = Column(String)
    Hobo = Column(String)
    BombosTablet = Column(String)
    Cave45 = Column(String)
    CheckerboardCave = Column(String)
    MiniMoldormCaveNPC = Column(String)
    Library = Column(String)
    MazeRace = Column(String)
    DesertLedge = Column(String)
    LakeHyliaIsland = Column(String)
    SunkenTreasure = Column(String)
    FluteSpot = Column(String)
    Sanctuary = Column(String)
    SewersSecretRoomLeft = Column(String)
    SewersSecretRoomMiddle = Column(String)
    SewersSecretRoomRight = Column(String)
    SewersDarkCross = Column(String)
    HyruleCastleBoomerangChest = Column(String)
    HyruleCastleMapChest = Column(String)
    HyruleCastleZeldasCell = Column(String)
    LinksUncle = Column(String)
    SecretPassage = Column(String)
    EasternPalaceCompassChest = Column(String)
    EasternPalaceBigChest = Column(String)
    EasternPalaceCannonballChest = Column(String)
    EasternPalaceBigKeyChest = Column(String)
    EasternPalaceMapChest = Column(String)
    EasternPalaceBoss = Column(String)
    EasternPalacePrize = Column(String)
    DesertPalaceBigChest = Column(String)
    DesertPalaceMapChest = Column(String)
    DesertPalaceTorch = Column(String)
    DesertPalaceBigKeyChest = Column(String)
    DesertPalaceCompassChest = Column(String)
    DesertPalaceBoss = Column(String)
    DesertPalacePrize = Column(String)
    OldMan = Column(String)
    SpectacleRockCave = Column(String)
    EtherTablet = Column(String)
    SpectacleRock = Column(String)
    SpiralCave = Column(String)
    MimicCave = Column(String)
    ParadoxCaveLowerFarLeft = Column(String)
    ParadoxCaveLowerLeft = Column(String)
    ParadoxCaveLowerRight = Column(String)
    ParadoxCaveLowerFarRight = Column(String)
    ParadoxCaveLowerMiddle = Column(String)
    ParadoxCaveUpperLeft = Column(String)
    ParadoxCaveUpperRight = Column(String)
    FloatingIsland = Column(String)
    TowerofHeraBigKeyChest = Column(String)
    TowerofHeraBasementCage = Column(String)
    TowerofHeraMapChest = Column(String)
    TowerofHeraCompassChest = Column(String)
    TowerofHeraBigChest = Column(String)
    TowerofHeraBoss = Column(String)
    TowerofHeraPrize = Column(String)
    CastleTowerRoom03 = Column(String)
    CastleTowerDarkMaze = Column(String)
    SuperbunnyCaveTop = Column(String)
    SuperbunnyCaveBottom = Column(String)
    HookshotCaveTopRight = Column(String)
    HookshotCaveTopLeft = Column(String)
    HookshotCaveBottomLeft = Column(String)
    HookshotCaveBottomRight = Column(String)
    SpikeCave = Column(String)
    Catfish = Column(String)
    Pyramid = Column(String)
    PyramidFairyLeft = Column(String)
    PyramidFairyRight = Column(String)
    Brewery = Column(String)
    CShapedHouse = Column(String)
    ChestGame = Column(String)
    HammerPegs = Column(String)
    BumperCave = Column(String)
    Blacksmith = Column(String)
    PurpleChest = Column(String)
    HypeCaveTop = Column(String)
    HypeCaveMiddleRight = Column(String)
    HypeCaveMiddleLeft = Column(String)
    HypeCaveBottom = Column(String)
    Stumpy = Column(String)
    HypeCaveNPC = Column(String)
    DiggingGame = Column(String)
    MireShedLeft = Column(String)
    MireShedRight = Column(String)
    PalaceofDarknessShooterRoom = Column(String)
    PalaceofDarknessBigKeyChest = Column(String)
    PalaceofDarknessTheArenaLedge = Column(String)
    PalaceofDarknessTheArenaBridge = Column(String)
    PalaceofDarknessStalfosBasement = Column(String)
    PalaceofDarknessMapChest = Column(String)
    PalaceofDarknessBigChest = Column(String)
    PalaceofDarknessCompassChest = Column(String)
    PalaceofDarknessHarmlessHellway = Column(String)
    PalaceofDarknessDarkBasementLeft = Column(String)
    PalaceofDarknessDarkBasementRight = Column(String)
    PalaceofDarknessDarkMazeTop = Column(String)
    PalaceofDarknessDarkMazeBottom = Column(String)
    PalaceofDarknessBoss = Column(String)
    PalaceofDarknessPrize = Column(String)
    SwampPalaceEntrance = Column(String)
    SwampPalaceBigChest = Column(String)
    SwampPalaceBigKeyChest = Column(String)
    SwampPalaceMapChest = Column(String)
    SwampPalaceWestChest = Column(String)
    SwampPalaceCompassChest = Column(String)
    SwampPalaceFloodedRoomLeft = Column(String)
    SwampPalaceFloodedRoomRight = Column(String)
    SwampPalaceWaterfallRoom = Column(String)
    SwampPalaceBoss = Column(String)
    SwampPalacePrize = Column(String)
    SkullWoodsBigChest = Column(String)
    SkullWoodsBigKeyChest = Column(String)
    SkullWoodsCompassChest = Column(String)
    SkullWoodsMapChest = Column(String)
    SkullWoodsBridgeRoom = Column(String)
    SkullWoodsPotPrison = Column(String)
    SkullWoodsPinballRoom = Column(String)
    SkullWoodsBoss = Column(String)
    SkullWoodsPrize = Column(String)
    ThievesTownAttic = Column(String)
    ThievesTownBigKeyChest = Column(String)
    ThievesTownMapChest = Column(String)
    ThievesTownCompassChest = Column(String)
    ThievesTownAmbushChest = Column(String)
    ThievesTownBigChest = Column(String)
    ThievesTownBlindsCell = Column(String)
    ThievesTownBoss = Column(String)
    ThievesTownPrize = Column(String)
    IcePalaceBigKeyChest = Column(String)
    IcePalaceCompassChest = Column(String)
    IcePalaceMapChest = Column(String)
    IcePalaceSpikeRoom = Column(String)
    IcePalaceFreezorChest = Column(String)
    IcePalaceIcedTRoom = Column(String)
    IcePalaceBigChest = Column(String)
    IcePalaceBoss = Column(String)
    IcePalacePrize = Column(String)
    MiseryMireBigChest = Column(String)
    MiseryMireMainLobby = Column(String)
    MiseryMireBigKeyChest = Column(String)
    MiseryMireCompassChest = Column(String)
    MiseryMireBridgeChest = Column(String)
    MiseryMireMapChest = Column(String)
    MiseryMireSpikeChest = Column(String)
    MiseryMireBoss = Column(String)
    MiseryMirePrize = Column(String)
    TurtleRockChainChomps = Column(String)
    TurtleRockCompassChest = Column(String)
    TurtleRockRollerRoomLeft = Column(String)
    TurtleRockRollerRoomRight = Column(String)
    TurtleRockBigChest = Column(String)
    TurtleRockBigKeyChest = Column(String)
    TurtleRockCrystarollerRoom = Column(String)
    TurtleRockEyeBridgeBottomLeft = Column(String)
    TurtleRockEyeBridgeBottomRight = Column(String)
    TurtleRockEyeBridgeTopLeft = Column(String)
    TurtleRockEyeBridgeTopRight = Column(String)
    TurtleRockBoss = Column(String)
    TurtleRockPrize = Column(String)
    GanonsTowerBobsTorch = Column(String)
    GanonsTowerDMsRoomTopLeft = Column(String)
    GanonsTowerDMsRoomTopRight = Column(String)
    GanonsTowerDMsRoomBottomLeft = Column(String)
    GanonsTowerDMsRoomBottomRight = Column(String)
    GanonsTowerRandomizerRoomTopLeft = Column(String)
    GanonsTowerRandomizerRoomTopRight = Column(String)
    GanonsTowerRandomizerRoomBottomLeft = Column(String)
    GanonsTowerRandomizerRoomBottomRight = Column(String)
    GanonsTowerFiresnakeRoom = Column(String)
    GanonsTowerMapChest = Column(String)
    GanonsTowerBigChest = Column(String)
    GanonsTowerHopeRoomLeft = Column(String)
    GanonsTowerHopeRoomRight = Column(String)
    GanonsTowerBobsChest = Column(String)
    GanonsTowerTileRoom = Column(String)
    GanonsTowerCompassRoomTopLeft = Column(String)
    GanonsTowerCompassRoomTopRight = Column(String)
    GanonsTowerCompassRoomBottomLeft = Column(String)
    GanonsTowerCompassRoomBottomRight = Column(String)
    GanonsTowerBigKeyChest = Column(String)
    GanonsTowerBigKeyRoomLeft = Column(String)
    GanonsTowerBigKeyRoomRight = Column(String)
    GanonsTowerMiniHelmasaurRoomLeft = Column(String)
    GanonsTowerMiniHelmasaurRoomRight = Column(String)
    GanonsTowerPreMoldormChest = Column(String)
    GanonsTowerMoldormChest = Column(String)
    
    def __init__(self, seed_guid : str, locations : dict):
        self.seed_guid = seed_guid
        for k,v in locations.items():
            setattr(self, seedparser.getLocationMap()[k], v)

class Seeds(base):
    __tablename__ = 'seeds'
    seed_guid = Column(String, primary_key=True)
    location = Column(String, primary_key=True)
    item = Column(String, primary_key=True)