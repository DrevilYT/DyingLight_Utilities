____________________________________________________________________________________________________________________________
"Merchants And Quartermasters - All Items" mod for Dying Light
Created By: StinVec
https://www.nexusmods.com/dyinglight/users/21896034
____________________________________________________________________________________________________________________________


_____________________________________________________________________________________
This mod is safe to use on both new and existing save games in all difficulty modes.
However, with any game you modify, it is always a good idea to make a backup of your
save game files before making any changes.

(save games are located at "...\Steam\userdata\*userid_or_number*\239140\" folder)
_____________________________________________________________________________________



__1__ Limiting Items That Are Offered At Merchants (And/Or Quartermasters)
__2__ Adjusting Prices Of Items At Merchants
__3__ Limiting Which Merchants Are Affected By The Mod (Merchant-affecting versions of the mod only)



__1__________________________________________________________________________________
_____ Limiting Items That Are Offered At Merchants (And/Or) Quartermasters __________

This mod adds over 1,200 purchasable items to the shop listings and for all 6 color quality tiers.
Due to loading all color variations for all items being added to the shop, the shop window can take upward of
30 seconds to 1 minute or so to come up and also to update after buying an item as that is potentially over 3,500 items it
is loading into the listings.

To lessen the load time, or if you have no interest in specific item types or items of specific color tiers
being available at merchants and quartermasters, you can select to have shops only load specific items of
specific colors.

To limit items that are loaded, you will need a tool like WinRAR to open and manipulate the .pak files the game
is using. Pak files are .zip files with a different extension.

		1) Open your installed Data3.pak file that contains this mod:
			- Browse to your Dying Light installation folder and enter the 'DW' folder
			- Open the 'Data3.pak' file which contains this mod with WinRAR
			  "...Steam\Steamapps\Dying Light\DW\Data3.pak"

		2) Extract/copy the customization file(s) onto your computer someplace and then open it/them with Notepad
			- Browse to the "data\scripts\trading" folder
			- Copy/extract the "MAI_CUSTOMIZATION_MERCHANT_INVENTORY.txt" file onto your computer someplace
			- Copy/extract the "MAI_CUSTOMIZATION_QUARTERMASTER_INVENTORY.txt" file onto your computer someplace if you are
			  using the Quartermaster-affecting versions of the mod
			- Open the copied file(s) with Notepad

		3) In the file, take note of the instructions and alter to your preference
			- Add // at the far left of the 'use' lines of items in the categories and colors to disable specific items
			  from being offered at all merchants and/or quartermasters.
			- You can re-enable any disabled categories by removing the // to once again have those items offered
			  at merchants and/or quartermasters.

				Example:
					//	use buggy_upgrades_white();	//////////////White Buggy Upgrades
						use buggy_upgrades_green();	//////////////Green Buggy Upgrades

					White Buggy Upgrades are disabled and -WILL NOT- be loaded
					Green Buggy Upgrades are not disabled and -WILL- be loaded

		4) Save your changes and add the modified file(s) back into the Data3.pak file
			- After making any changes to enable or disable any item categories in the customization file(s), save
			  the changes
			- Drag and drop the modified file(s) back onto the open Data3.pak WinRar window and replace the existing
			  file(s) after ensuring that the 'Normal' option is selected under compression method



__2__________________________________________________________________________________
_____ Adjusting Prices And Values Of Items At Merchants _____________________________

To make all items listed at merchants cost or sell for more or less than normal:

		1) Open your installed Data3.pak file that contains this mod:
			- Browse to your Dying Light installation folder and enter the 'DW' folder
			- Open the 'Data3.pak' file which contains this mod with WinRAR
			  "...Steam\Steamapps\Dying Light\DW\Data3.pak"

		2) Extract/copy the "MAI_CUSTOMIZATION_MERCHANT_PRICE.txt" file onto your computer and then open it with Notepad
			- Browse to the "data\scripts\trading" folder
			- Copy/extract the "MAI_CUSTOMIZATION_MERCHANT_PRICE.txt" file onto your computer someplace
			- Open the copied file with Notepad (or right-click the copied file and select 'Open With...' and
			  choose Notepad for editing the file)

		3) In the file, take note of the instructions and alter to your preference
			- Remove the two // marks from the far left of a single 'use' line for a pre-configured price multiplier you
			  desire to enable or remove // from the custom PriceMod line and alter its 1.0 multiplier to the multiplier
			  you desire
			  
			  Note: Cost of items to buy and value of items to sell can be configured separately in the customization file.

				Examples:
					PriceMod(10.0); will make items 10 times higher in cost/value
					PriceMod(1.10); will make items 10% higher in cost/value
					PriceMod(1.0); will make items cost their normal cost/value
					PriceMod(0.10); will make items cost 10% of their normal cost/value
					PriceMod(0.01); will make items cost 1% of their normal cost/value
				(At 1%, the Gold Rarity "Battle Axe of Titans" is about $358 to buy, instead of $44,783)

		4) Save your changes and add the modified file back into the Data3.pak file
			- After enabling a pre-configured multiplier line or enabling and customizing the custom multiplier line, save
			  the changes to this file and close it
			- Drag and drop this modified file back onto the open Data3.pak WinRar window and replace the unmodified
			  version with it
			  (if you are given the option in your zip program's 'add file' dialogue box, ensure 'Normal' compression is
			  selected under compression method)



__3__________________________________________________________________________________
_____ Limiting Which Merchants Are Affected By The Mod ______________________________

(Merchant-affecting versions of the mod only)

By default, the merchant-affecting versions of this mod will affect the inventories of all merchants. You can choose to
modify the mod's customization file to limit the scope of which merchants are affected by this mod by enabling one of the
options available. You can later disable the enabled option to revert the mod to the default of affecting all merchants
again.

		1) Open your installed Data3.pak file that contains this mod:
			- Browse to your Dying Light installation folder and enter the 'DW' folder
			- Open the 'Data3.pak' file which contains this mod with WinRAR
			  "...Steam\Steamapps\Dying Light\DW\Data3.pak"

		2) Extract/copy the customization file(s) onto your computer someplace and then open it/them with Notepad
			- Browse to the "data\scripts\trading" folder
			- Copy/extract the "MAI_CUSTOMIZATION_MERCHANTS_AFFECTED.txt" file onto your computer someplace
			- Open the copied file(s) with Notepad

		3) In the file, take note of the instructions and alter to your preference
			- Remove the two // marks from the far left of a single 'import' line of the optional scopes offered

		4) Save your changes and add the modified file(s) back into the Data3.pak file
			- After making your change change to the customization file(s), save the changes
			- Drag and drop the modified file back onto the open Data3.pak WinRar window and replace the existing
			  file after ensuring that the 'Normal' option is selected under compression method (if available)





____________________________________________________________________________________________________________________________"Merchants And Quartermasters - All Items" mod for Dying Light
Created By: StinVec
https://www.nexusmods.com/dyinglight/users/21896034
____________________________________________________________________________________________________________________________