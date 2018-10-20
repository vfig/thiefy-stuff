/* Door fixes for Thief 1 / Gold.
**
** Copyright 2018 Andy Durdin (vfig). You are free to use this script,
** modified or unmodified, in any of your missions, and may distribute it
** accompanying your mission freely.
**
** If you choose, you may instead deal with this script under the terms of the
** MIT license.
**
** -- FIXES --
**
** 1. In Thief 1/Gold, if a door hits an object while opening and halts, then
**    frobbing it while continue trying to open it again. In Thief 2, this
**    was changed so that frobbing it would try closing it instead. This
**    script brings the Thief 2 behaviour to doors in Thief 1/Gold. This both
**    improves usability for opening doors in general, but also prevents
**    players getting stuck between terrain and an opening door.
**
** 2. In Thief 1/Gold, doors that are part of a linked "Double" pair will open
**    and close in synch, but do not synch their locked state: it is possible
**    for one of the doors to be unlocked and the other to be locked, which is
**    just weird, let's face it. In Thief 2, this was changed so that doors
**    synch their locked state so a "Double" pair will lock and unlock
**    together. This script brings the Thief 2 behaviour to doors in Thief 1/
**    Gold.
**
** -- INSTRUCTIONS --
**
** To use this script in your mission, you need three things:
**
** 1. Make sure you have loaded squirrel.osm
**
** 2. Put this file into the sq_scripts subdirectory of your mission.
**
** 3. Edit the Door archetype in your gamesys, and put this script in first.
**    The scripts should look like this:
**
**        Script 0: GoldDoorHack
**        Script 1: StdDoor
**        Script 2: LockSounds
**        
*/
class GoldDoorHack extends SqRootScript
{
    function OnDoorHalt() {
        if (message().PrevActionType == eDoorAction.kOpening) {
            // If the door was blocked while opening, then remember
            // this, so the next time it's frobbed it'll close instead.
            SetData("BlockedFromOpening", true);
        } else {
            // Evidently we're no longer blocked from opening.
            ClearData("BlockedFromOpening");
        }
    }

    function OnDoorOpen() {
        // Evidently we're no longer blocked from opening.
        ClearData("BlockedFromOpening");
    }

    function OnDoorClose() {
        // Evidently we're no longer blocked from opening.
        ClearData("BlockedFromOpening");
    }

    function OnFrobWorldEnd() {
        if (IsDataSet("BlockedFromOpening")) {
            ClearData("BlockedFromOpening");
            // Don't pass this message on to StdDoor, or it'll keep
            // trying to open the door!
            BlockMessage();
            // We want to close the door this time instead.
            Door.CloseDoor(self);
        }
    }

    function OnSynchUp() {
        // This is just copied from T2's GIZMO.SCR
        local other_door = message().from;
        if(Property.Possessed(other_door, "Locked")
            && Property.Possessed(self, "Locked"))
        {
            local other_locked = Property.Get(other_door, "Locked");
            local locked = Property.Get(self, "Locked");
            if (locked != other_locked) {
                Property.CopyFrom(self, "Locked", other_door);
            }
        }
    }
}
