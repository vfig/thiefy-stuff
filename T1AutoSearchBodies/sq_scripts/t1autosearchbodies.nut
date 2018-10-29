/* Make the 'Auto-search bodies' game option work in Thief 1 / Gold.
**
** -- INSTRUCTIONS --
**
** To use this script in your mission, you need to:
**
** 1. Make sure you have loaded squirrel.osm
**
** 2. Put this file into the sq_scripts subdirectory of your mission.
**
** 3. Edit the 'Creature' archetype, and make sure its FrobInfo is set to
**
**        World Action: Move, Script
**
** 4. Edit all the archetypes that use the CorpseFrobHack script, and add the
**    T1AutoSearchBodies script ato it. In the default Thief Gold gamesys,
**    these archetypes are:
**
**      * Human (-14): { JAccuse; Corpsed; CorpseFrobHack; ; FALSE}
**      * Haunt (-1320): { Corpsed; CorpseFrobHack; ; ; FALSE}
**      * ZombieTypes (-1321): { ZombieRegen; Corpsed; CorpseFrobHack; ; FALSE}
**      * ApeBeast (-1328): { Corpsed; CorpseFrobHack; ; ; FALSE}
**      * HammerCorpse (-2976): { Corpsed; CorpseFrobHack; ; ; FALSE}
**
**    Of course if you don't use some of these archetypes in your mission, or
**    you never give some of them any items contained with the Belt or Alt
**    type, then you don't need to edit those.
**
**    For example, after editing the Human (-14) archetype, its Scripts
**    property will look like this:
**
**        Script 0: JAccuse
**        Script 1: Corpsed
**        Script 2: CorpseFrobHack
**        Script 3: T1AutoSearchBodies
*/
class T1AutoSearchBodies extends SqRootScript
{
    // This is all just copied from T2's AI.SCR

    function GetCarriedObj() {
        local candidate = self;
        local contlinks = Link.GetAll("Contains", self);
        foreach (curlink in contlinks) {
            if (LinkTools.LinkGetData(curlink, "").tointeger() < 0) { //external carry
                candidate = LinkDest(curlink);
            }
        }
        return candidate;
    }

    function OnFrobWorldEnd() {
        if (DarkGame.BindingGetFloat("auto_search") != 0.0) {
            Debug.MPrint("Performing Loot And Lug");
            local carriedobj = GetCarriedObj();
            if (carriedobj != self) {
                Container.Add(carriedobj, message().Frobber);
                Reply(false);
            }
        }
    }
}
