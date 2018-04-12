CAUTION
=======

This is the old version of the patch, for the original versions
of Thief Gold and Thief II. If you're using a NewDark version
(i.e. version 1.20 or higher), then you should use the patch with
the gamesys.dml files.


SUMMARY
=======

Thief Gold and Thief II no-spider patch. Version 1.1, Dec 8 2013.

Created by Andy Durdin (me@andy.durdin.net)

Tested with Thief Gold 2.0.2.48 (GOG.com release) and Thief II
2.0.0.18 (GOG.com release). If you have any problems with it on
other versions, let me know.

Please feel free to redistribute this patch.


OVERVIEW
========

This patch makes all the spiders:

  a) friendly to the player
  b) attacked by other ai
  c) have only one hit point
  d) die as soon as the level starts anyway
  e) look like a small white mossy stone.

This applies to all: small spiders, big spiders, chaos spiders, and
spiderbots.

(I could have made them completely invisible, but I couldn't remove
the physics collisions from them. So since you could be blocked walking
into them, I thought it better to at least have a visible shape.)

For reasons currently beyond my understanding, in Thief II the small spiders
and spider robots are completely removed, while the large spiders still have
a model; in Thief Gold all of them still have a model. Well, the mossy white
stone looks quite harmless.


INSTALLING - THIEF GOLD
=======================

1. In your Thief Gold directory, rename Dark.gam to Dark-backup.gam

2. Copy ThiefGoldNoSpiders.gam into your Thief Gold directory.

3. Rename ThiefGoldNoSpiders.gam to Dark.gam


INSTALLING - THIEF II
=====================

(If you want to keep the spiderbots, use Thief2NoSpidersWithSpiderbots.gam
instead of Thief2NoSpiders.gam)

1. In your Thief II directory, rename Dark.gam to Dark-backup.gam

2. Copy Thief2NoSpiders.gam into your Thief 2 directory.

3. Rename Thief2NoSpiders.gam to Dark.gam


UNINSTALLING
============

1. Rename Dark-backup.gam to Dark.gam


Have fun!
