# Monet Data Science Project: Data Transformation

[Replication data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YQOLZW)

## **Image Data**

Should be 98 paintings in total. 1796-1850 London in **Turner’s 60** paintings, 1864-1872 Paris in **Monet’s 18** paintings, 1899-1901 London in **Monet’s 20** paintings.

I have 47 + 69 = 116 paintings? No labels? Maybe check labels in `pnas.2219118120.pdf`? Or check `pnas.2219118120.sapp.pdf`?

All the dataverse replication files are in `~/Workspace/monet/dataverse_files`. For the pdfs, see `~/Workspace/monet/*.pdf`.

Seems like everything is contained in `pnas.2219118120.sapp.pdf`, in Fig. S4 and Fig. S5. 

### **All Images**

#### **Turner's 60 paintings (actually 61/58)**

For the Turner paintings (author says 60, but there are actually 61 in Appendix, see `pnas.2219118120.sapp.pdf` Fig. S4), the labels are:
- Blue (1): predominantly clear-sky
- Grey (2): predominantly cloudy
- Red (3): dawn/dusk

| No. | Title | Year | Author | Category | Filename |
| --- | --- | --- | --- | --- | --- |
| 1 | Fishermen at Sea | 1796 | Turner | 1 | `Turner_FishermenatSea_1796.png` |
| 2 | Norham Castle | 1798 | Turner | 3 | `Turner_NorhamCastle_1798.png` |
| 3 | Buttermere Lake, shower | 1798 | Turner | 2 | `Turner_Buttermere_Lake_Shower_1798.jpg` |
| 4 | Dutch Boats | 1801 | Turner | 2 | `Turner_Dutch_Boats_Gale_1801.jpg` |
| 5 | Calais Pier | 1803 | Turner | 2 | `Turner_Calais_Pier_1803.jpg` |
| 6 | Festival Macon | 1803 | Turner | 1 | `Turner_FestivalVintageMacon_1803.png` |
| 7 | Thames Weybridge | 1805 | Turner | 2 | `Turner_Thames_Weybridge_1805.jpg` |
| 8 | Windsor Castle | 1805 | Turner | 1 | `Turner_Windsor_Castle_1805.jpg` |
| 9 | Shipwreck | 1806 | Turner | 2 | `Turner_Shipwreck_1805.jpg` |
| 10 | Victory, Trafalgar | 1806 | Turner | 1 | `Turner_Trafalgar_Mizen_1806.jpg` |
| 11 | Danish Ships | 1807 | Turner | 1 | `Turner_Pithead_Danish_ships_1807.jpg` |
| 12 | Windy Day | 1808 | Turner | 2 | `Turner_Windy_day_1808.jpg` |
| 13 | Greenwich Park | 1809 | Turner | 1 | `Turner_London_Greenwich_Park_1809.jpg` |
| 14 | Sunset, London | 1809 | Turner | 3 | `` |
| 15 | Frosty Morning | 1813 | Turner | 3 | `Turner_Frosty_morning_1813.jpg` |
| 16 | Lake, Sybil | 1814 | Turner | 1 | `Turner_Lake_Avernus-_Aeneas_and_the_Cumaean_Sybil_1814.jpg` |
| 17 | Dido, Aeneas | 1814 | Turner | 2 | `Turner_Dido_and_Aeneas_1814.jpg` |
| 18 | Apullia, Appullus | 1814 | Turner | 1 | `Turner_Apullia_in_Search_of_Appullus_1814.jpg` |
| 19 | Crossing Bridge | 1815 | Turner | 2 | `Turner_Crossing_the_Bridge_1815.jpg` |
| 20 | Dido, Building Carthage | 1815 | Turner | 1 | `Turner_DidoBuildingCarthage_1815.png` |
| 21 | Decline, Carthaginian Empire | 1817 | Turner | 3 | `Turner_Decline_of_the_Carthaginian_Empire_1817.jpg` |
| 22 | Richmond Hill, Birthday | 1819 | Turner | 1 | `Turner_Richmond_Hill_birthday_1819.jpg` |
| 23 | Margate | 1822 | Turner | 3 | `Turner_Margate_Sunrise_fishing_1822.jpg` |
| 24 | Shipping, East Cowes Headland | 1827 | Turner | 1 | `Turner_Shipping_off_East_Cowes_Headland_1827.jpg` |
| 25 | Seacoast ruin | 1828 | Turner | 3 | `` |
| 26 | Chain Pier, Brighton | 1828 | Turner | 1 | `Turner_Chain_Pier_Brighton_1828.jpg` |
| 27 | Archway, Trees, Sea | 1828 | Turner | 2 | `Turner_Archway_trees_sea_1828.jpg` |
| 28 | Brighton Sea, sunset | 1829 | Turner | 3 | `Turner_Brighton_Sea_sunset_1829.jpg` |
| 29 | Caligulas Palace Bridge | 1831 | Turner | 2 | `Turner_Caligulas_Palace_Bridge_1831.jpg` |
| 30 | Lifeboat, Blue light | 1831 | Turner | 1 | `Turner_Life-Boat_stranded_vessel_blue_light_1831.jpg` |
| 31 | Fort Vimieux | 1831 | Turner | 3 | `Turner_Fort_Vimieux_1831.jpg` |
| 32 | Prince of Orange | 1832 | Turner | 2 | `Turner_Prince_of_Orange_Embarked_1832.jpg` |
| 33 | Calais Sands | 1832 | Turner | 3 | `Turner_Calais_sands_low_water_1832.jpg` |
| 34 | Dudley | 1832 | Turner | 3 | `Turner_Dudley_1832.jpg` |
| 35 | Von Tromp | 1833 | Turner | 1 | `Turner_Van_Tromp_seascape_1833.jpg` |
| 36 | Wreckers, Northumberland | 1834 | Turner | 2 | `Turner_Wreckers_Northumberland_1834.jpg` |
| 37 | Bay | 1835 | Turner | 2 | `Turner_landscape_river_bay_1835.jpg` |
| 38 | Breakers, Margate | 1835 | Turner | 2 | `Turner_Breakers_Margate_1835.jpg` |
| 39 | Fire at Sea | 1835 | Turner | 3 | `Turner_Fire_at_Sea_1835.jpg` |
| 40 | Stormy Sea, Dolphins | 1835 | Turner | 2 | `Turner_Stormy_Sea_with_Dolphins_1835.jpg` |
| 41 | Shipwreck | 1835 | Turner | 2 | `Turner_stormy_sea_blazing_wreck_1835.jpg` |
| 42 | Thames, Waterloo | 1835 | Turner | 2 | `Turner_Thames-Waterloo_1835.jpg` |
| 43 | Rough Sea | 1840 | Turner | 2 | `Turner_Rough_sea_wreckage_1840.jpg` |
| 44 | Fighting Temeraire | 1839 | Turner | 3 | `Turner_FightingTemeraire_1839.png` |
| 45 | Yacht Coast | 1840 | Turner | 2 | `Turner_Yacht_Coast_1840.jpg` |
| 46 | Morning after Storm | 1840 | Turner | 3 | `Turner_Morning_after_the_Storm_1840.jpg` |
| 47 | Sun setting lake | 1840 | Turner | 3 | `Turner_sun_Setting_lake_1840.jpg` |
| 48 | Seascape, bouy | 1840 | Turner | 2 | `Turner_Seascape_Buoy_1840.jpg` |
| 49 | Seascape Distant Coast | 1840 | Turner | 2 | `Turner_Seascape_Distant_Coast_1840.jpg` |
| 50 | Margate Jetty | 1840 | Turner | 2 | `Turner_Margate_Jetty_1840.jpg` |
| 51 | Slave Ship, Sunrise | 1840 | Turner | 3 | `Turner_Slave_ship_sunrise_1840.jpg` |
| 52 | River from hill | 1840 | Turner | 2 | `Turner_River_seen_from_hill_1840.jpg` |
| 53 | Storm | 1840 | Turner | 2 | `Turner_Storm_1840.jpg` |
| 54 | Waves breaking, wind | 1840 | Turner | 2 | `Turner_Waves Breaking_Wind_1840.jpg` |
| 55 | Burial at Sea | 1842 | Turner | 2 | `Turner_Burial_sea_1842.jpg` |
| 56 | Snow Storm, Steam Boat | 1842 | Turner | 2 | `Turner_Snow_Storm_Steam_Boat_1842.jpg` |
| 57 | Light, Color, Goethe | 1843 | Turner | 3 | `Turner_LightColorGoethe_1843.png` |
| 58 | Rain, Steam, Speed | 1844 | Turner | 2 | `Turner_RainSteamSpeed_1844.png` |
| 59 | Norham Castle, Sunrise | 1845 | Turner | 3 | `` |
| 60 | Sunrise, Seamonsters | 1845 | Turner | 3 | `Turner_Sunrise_seamonsters_1845.jpg` |
| 61 | Visit Tomb | 1850 | Turner | 3 | `Turner_Visit_Tomb_1850.jpg` |

There are 60 files labelled Turner in the data dir. Two of them has no match in Fig. S4: 
- `Turner_seascape_coast_1840.jpg`
- `Turner_sunset_1830.jpg`

Three paintings in Fig. S4 are not in the data dir:
- Sunset, London, 1809
- Seacoast ruin, 1828
- Norham Castle, Sunrise, 1845

Hint: to convert the above table to json, use: [Convert Markdown Table to JSON Array - Table Convert Online](https://tableconvert.com/markdown-to-json)

#### **Monet's 18 + 20 = 38**

> 38 oil paintings by Monet from 1864–1904 used in this analysis along with six from Whistler. As for Turner, we include keywords identifying the painting and its year of creation. Time goes down the columns and left to right; and colors of these keywords and date indicate the category: predominantly clear-sky (blue), predominantly cloudy (grey), and dawn/dusk (red). For Monet’s series paintings in London of dawn/dusk are indicated by a red star in the top left corner. The remaining paintings are classified as predominantly cloudy or hazy. Outlined in the grey box are six London Nocturnes by Whistler from 1871–1875. Outlined in black are seven paintings by Caillebotte, four by Pissarro, and one by Morisot.

| No. | Title | Year | Author | Category | Location | Filename |
|---|---|---|---|---|---|---|
| 1 | Towing Boat, Honfleur | 1864 | Monet | 3 | France | `Monet_Towing_Boat_Honfleur_1864.jpg` |
| 2 | Pointe Hève | 1864 | Monet | 2 | France | `Monet_Pointe_Heve_1864.jpg` |
| 3 | Mouth of Seine, Honfleur | 1865 | Monet | 2 | France | `Monet_Mouth_Seine_Honfleur_1865.jpg` |
| 4 | Fontainebleau | 1865 | Monet | 1 | France | `Monet_Pave_Fontainebleau_1865.jpg` |
| 5 | Jardin Infante | 1865 | Monet | 2 | France | `Monet_Jardin-Infante_1864.jpg` |
| 6 | Saint-Germain-l'Auxerrois | 1864 | Monet | 1 | France | `Monet_Saint-Germain-l'Auxerrois_Paris_1867.jpg` |
| 7 | Fontainebleau | 1865 | Monet | 1 | France | `Monet_Oak_Fontainebleau_1865.jpg` |
| 8 | Pointe Hève, Low tide | 1865 | Monet | 2 | France | `Monet_Pointe_Heve_Low_Tide_1865.jpg` |
| 9 | Woman, Garden | 1866 | Monet | 1 | France | `Monet_Woman-in-Garden_1866.jpg` |
| 10 | Garden Saint-Adresse | 1866 | Monet | 1 | France | `Monet_garden_Saint-Adresse_1866.jpg` |
| 11 | Saint-Adresse | 1867 | Monet | 2 | France | `Monet_Beach_Sainte-Adresse_1867.jpg` |
| 12 | Garden Saint-Adresse | 1867 | Monet | 1 | France | `Monet_Garden_Sainte-Adresse_1867.jpg` |
| 13 | Regatta, Sainte-Adresse | 1867 | Monet | 2 | France | `Monet_Regatta_at_Sainte-Adresse_1867.jpg` |
| 14 | Magpie | 1868 | Monet | 2 | France | `Monet_Magpie_1868.jpg` |
| 15 | La Grenouillère | 1869 | Monet | 2 | France | `Monet_La Grenouillère_1869.jpg` |
| 16 | Trouville, Low tide | 1870 | Monet | 2 | France | `Monet_Trouville_low_tide_1870.jpg` |
| 17 | Beach, Trouville | 1870 | Monet | 2 | France | `Monet-Beach-at-Trouville-1870.jpg` |
| 18 | Impression, Sunrise | 1872 | Monet | 3 | France | `Monet_Impression-Sunrise_1872.jpg` |
| 19 | Houses of Parliament | 1899-1903 | Monet | 3 | London | `Monet-Parliament_1899.jpg` |
| 20 | Houses of Parliament | 1899-1903 | Monet | 3 | London | `Monet_Parliament_Met_1899.jpg` |
| 21 | Houses of Parliament | 1899-1903 | Monet | 3 | London | `Monet_Parliament_Brooklyn_1899.jpg` |
| 22 | Houses of Parliament | 1899-1903 | Monet | 3 | London | `Monet_Parliament_Lille_1899.jpg` |
| 23 | Houses of Parliament | 1899-1903 | Monet | 3 | London | `Monet_Parliament_sunset_DC_1899.jpg` |
| 24 | Houses of Parliament | 1899-1903 | Monet | 2 | London | `Monet_Parliament_Florida_1899.jpg` |
| 25 | Houses of Parliament | 1899-1903 | Monet | 2 | London | `Monet_Parliament_seagulls_Pushkin_1899.jpg` |
| 26 | Houses of Parliament | 1899-1903 | Monet | 3 | London | `Monet_Parliament_Zurich_1899.jpg` |
| 27 | Houses of Parliament | 1899-1903 | Monet | 3 | London | `Monet_Parliament_Chicago_1899.jpg` |
| 28 | Charging Cross Bridge | 1899-1903 | Monet | 3 | London | `Monet_Charing_Santa-Barbara_1899.jpg` |
| 29 | Charging Cross Bridge | 1899-1903 | Monet | 2 | London | `Monet_Charing_Madrid_1899.jpg` |
| 30 | Charging Cross Bridge | 1899-1903 | Monet | 2 | London | `Monet_Charing_Rotterdam_1899.jpg` |
| 31 | Charging Cross Bridge | 1899-1903 | Monet | 3 | London | `Monet_Charing_Saint_Louis_1899.jpg` |
| 32 | Charging Cross Bridge | 1899-1903 | Monet | 2 | London | `Monet_Charing_Ontario_1899.jpg` |
| 33 | Waterloo Bridge | 1899-1903 | Monet | 2 | London | `Monet_Waterloo_sun_1899.jpg` |
| 34 | Waterloo Bridge | 1899-1903 | Monet | 3 | London | `Monet_Waterloo_Denver_1899.jpg` |
| 35 | Waterloo Bridge | 1899-1903 | Monet | 3 | London | `Monet_Waterloo_grey_1899.jpg` |
| 33 | Waterloo Bridge | 1899-1903 | Monet | 2 | London | `Monet_Waterloo_fog_1899.jpg` |
| 34 | Waterloo Bridge | 1899-1903 | Monet | 3 | London | `Monet_Waterloo_private_1899.jpg` |
| 35 | Waterloo Bridge | 1899-1903 | Monet | 2 | London | `Monet_Waterloo_dusk_1899.jpg` |
| 36 | Nocturne, Blue and Silver | 1871 | Whistler | 2 | London | `Whistler_Nocturne_Blue_Silver_Chelsea_1871.jpg` |
| 37 | Nocturne, Blue and Gold, Southampton | 1872 | Whistler | 2 | London | `Whistler_Nocturne_Blue_and_Gold_Southampton_Water_1872.jpg` |
| 38 | Nocturne, Blue and Silver, Cremorne | 1872 | Whistler | 2 | London | `Nocturne_Blue_Silver_Cremorne_1872.jpg` |
| 39 | Battersea | 1872 | Whistler | 2 | London | `Whistler_Battersea_1872.jpg` |
| 40 | Black and Gold, Fire Wheel | 1875 | Whistler | 2 | London | `Whistler_Black_Gold_Fire_Wheel_1875.jpg` |
| 41 | Falling Rocket | 1875 | Whistler | 2 | London | `Whistler_falling_rocket_1875.jpg` |
| 42 | Torcadéro | 1877 | Morisot | 2 | Paris | `Morisot_Vue_de_Paris_hauteurs_du_Trocadéro_1871.jpg` |
| 43 | Paris, Street | 1877 | Caillebotte | 2 | Paris | `Caillebotte_Rue-de-Paris-pluie_1877.jpg` |
| 44 | canoe | 1878 | Caillebotte | 2 | Paris | `Caillebotte_Canoë_sur_la_rivière_Yerres_1878.jpg` |
| 45 | Haussmann, man | 1880 | Caillebotte | 2 | Paris | `Caillebotte_LHomme_au_balcon_boulevard_Haussmann_1880.jpg` |
| 46 | Haussmann | 1880 | Caillebotte | 2 | Paris | `Caillebotte_boulevard_Haussmann_1880.jpg` |
| 47 | Haussmann, snow | 1880 | Caillebotte | 2 | Paris | `Caillebotte_Boulevard_Haussmann_effet_de_neige_1880.jpg` |
| 48 | view, above | 1880 | Caillebotte | 2 | Paris | `Caillebotte_vu_du_haut_1880.jpg` |
| 49 | traffic island | 1880 | Caillebotte | 2 | Paris | `Caillebotte_traffic_island_1880.jpg` |
| 50 | Blvd Montmartre | 1897 | Pissarro | 2 | Paris | `Pissarro_Boulevard_Montmartre_à_Paris_1897.jpg` |
| 51 | Blvd Montmartre, spring | 1897 | Pissarro | 2 | Paris | `Pissarro_Boulevard_Montmartre_Spring_1897.jpg` |
| 52 | theatre | 1897 | Pissarro | 2 | Paris | `Pissarro_Place_du_Theatre_Francais_1897.jpg` |
| 53 | Winter morning, Henri IV | 1899 | Pissarro | 3 | Paris | `Pissarro_winter_morning_HenriIV_1899.jpg` |
