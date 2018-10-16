/* 'Secrets' stats for Thief 1 / Gold.
**
** Copyright 2018 Andy Durdin (vfig). You are free to use this script,
** modified or unmodified, in any of your missions, and may distribute it
** accompanying your mission freely.
**
** If you choose, you may instead deal with this script under the terms of the
** MIT license.
**
**
** -- INSTRUCTIONS --
**
** To use this script in your mission, you need four things:
**
** 1. Make sure you have loaded squirrel.osm
**
** 2. Put this file into the sq_scripts subdirectory of your mission.
**
** 3. Add entries to debrief.str for the 'SecretsCount' and 'SecretsFound'
**    quest vars. If you haven't customised debrief.str, you can simply copy
**    the file from the demo mission.
**
** 4. Put the 'FrobSecret', 'TurnOnSecret', or 'RoomSecret' script on each of
**    the objects or concrete rooms you want to be secrets. See below for
**    details.
**
** Then run the mission! If you're in the game, you'll get a "Found Secret!"
** message and the usual sound when you find each secret, and the stats will
** be shown when you end the mission. If you're in Dromed, you will see the
** secrets listed in the monolog when you enter game mode, and when you find
** each secret, it will be printed to the monolog with the running total of
** secrets found.
**
**
** -- DETAILS --
**
** FrobSecret: An object with this script will be counted as a found secret
** when the player first frobs it in the world. If the object is locked, it
** must be unlocked first before it will count as a secret. This script makes
** sure that the 'Script' FrobInfo flag is set, so you don't have to do that
** manually.
**
** TurnOnSecret: An object with this script will be counted as a found secret
** when it receives its first TurnOn message. Use this, typically on a Marker,
** if you need to trigger a secret from something other than a frob.
**
** RoomSecret: A concrete room with this script will be counted as a found
** secret when the player enters any of its room brushes for the first time.
** Note that all room brushes belonging to the same concrete room count as
** just one secret, even if they are far apart in the mission.
*/

class T1Secrets
{
    static function RegisterSecret(sender) {
        // Get the number of secrets in the mission.
        local count = (Quest.Exists("SecretsCount")
            ? Quest.Get("SecretsCount")
            : 0);
        // Increment it, cause there's one more!
        count = count + 1;
        Quest.Set("SecretsCount", count);
        // Show the secret in the monolog.
        print("Secret " + count + " is object id " + sender);
    }

    static function FoundSecret(sender) {
        // Get the number of secrets in the mission.
        local count = (Quest.Exists("SecretsCount")
            ? Quest.Get("SecretsCount")
            : 0);
        // Get the number of secrets found.
        local found = (Quest.Exists("SecretsFound")
            ? Quest.Get("SecretsFound")
            : 0);
        // Well, we've just found one more!
        found = found + 1
        Quest.Set("SecretsFound", found);
        // Show a message and play a sound
        local player = Object.Named("Player");
        local message = Data.GetString("playhint",
            "FoundSecret", "Found Secret!");
        DarkUI.TextMessage(message);
        Sound.PlaySchemaAmbient(player, "new_obj");
        // Show the secret in the monolog
        print("Found secret object id " + sender
            + ". Stats so far: " + found + " of " + count);
    }

}

class BaseT1Secret extends SqRootScript
{
    function OnSim() {
        if (message().starting) {
            T1Secrets.RegisterSecret(self);
        }
    }

    function FoundSecret() {
        if (! IsDataSet("SecretFound")) {
            SetData("SecretFound", true);
            T1Secrets.FoundSecret(self);
        }
    }
}

class TurnOnSecret extends BaseT1Secret
{
    function OnTurnOn() {
        FoundSecret();
    }
}

class RoomSecret extends BaseT1Secret
{
    function OnPlayerRoomEnter() {
        FoundSecret();
    }
}

class FrobSecret extends BaseT1Secret
{
    function OnSim() {
        base.OnSim();
        if (message().starting) {
            // Make sure we have 'World Action: Script' set in our FrobInfo.
            const kFrobScript = 2;
            local world_action = (Property.Possessed(self, "FrobInfo")
                ? Property.Get(self, "FrobInfo", "World Action")
                : 0);
            world_action = (world_action | kFrobScript);
            Property.Set(self, "FrobInfo", "World Action", world_action);
        }
    }

    function OnFrobWorldEnd() {
        local player = Object.Named("Player");
        local frobbed_by_player = (message().Frobber == player);
        local is_unlocked = (! Locked.IsLocked(self));
        if (frobbed_by_player && is_unlocked) {
            FoundSecret();
        }
    }
}
