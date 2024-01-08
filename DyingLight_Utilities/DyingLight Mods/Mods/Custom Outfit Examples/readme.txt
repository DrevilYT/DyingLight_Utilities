MeshFpp stands for first person mesh (model which is visible from your view, for example when you look at your legs)
================
MeshTpp stands for third person mesh (what is visible in 3rd person)
================
Skin stands for the mesh texture (different variations of the outfit)
================
Image stands for the picture which is visible from your stash (you can find many images in data\menu\texturedefs\hudtextures.def)
================
Perk stands for the buffs that the outfit gives (see data\skills\perks.xml)
  -- How it looks in the perks file
  <skill id="Outfit10" cat="perks" max_level="1" tier="0" desc_params="" skill_points="0"> 
	<effect id="EnemyGrabChance" change="-0.5"/>
  </skill>

  -- How it's applied to the outfit
  Perk("Perk_Outfit10");
================
Category stands for the outfit category (you can make up your own number or use already present categories)
================
ID stands for the unique number outfit (IT MUST BE UNIQUE otherwise the outfit won't load properly)

! Outfits with custom categories will appear in the bottom of the stash !