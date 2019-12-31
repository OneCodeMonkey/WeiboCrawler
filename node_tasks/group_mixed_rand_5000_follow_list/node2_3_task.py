from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [1393320673,1748896653,1904555433,7155737567,2553129774,3038430552,5458593214,1863028777,1956199347,1863951194,5353687869,2633202613,1995207182,1664737815,2712533957,1762257520,1969612743,1194917072,2551541352,1652691705,2876786447,5225956407,2622054293,1819649157,1791823805,2803651503,2297790324,2672524093,2890778694,1796540810,1648118021,2709793132,5691389797,1987581641,1188770507,5749042654,1930773551,2431279984,2682900473,2705756881,2949817764,2965185060,6502503034,1462687981,2821775687,1808008130,1763555490,1795700755,1862089890,2610018641,5631143115,2572465202,1750113730,1322783044,3562059451,5127986690,1646848235,2030496165,3339521500,3188302854,6520696718,5025858701,1868574390,1968364763,1720340734,1952206654,1990850125,5922092586,1764026627,1692769643,1797630160,1659451505,3612921060,1824580145,1738532020,5401668767,1822005632,2259229401,3167201893,1911149875,2314684312,5687887061,2307010910,1853278731,1650769617,1239080997,2516156930,5693949181,3421932830,5151217211,1883315001,1729415747,3855367360,2260039534,1798014297,2400357027,3522099150,5157326121,2057465742,2012026743,1993639584,5324066988,5172348855,3178450664,2193088410,1578016617,2377494434,1968135357,2309347651,2730736740,2313012280,2397936387,1913056621,2140885974,2517369407,1998454623,1732064345,1661461350,1348152135,1920730934,1972697855,1773561391,6588324927,5051098569,1434701294,1778549442,1653869232,1864005047,1932908281,1758672217,6371811247,2806884122,1660364815,1421407172,2667834283,1819847435,1948534001,5081863075,2190105623,1667040054,2247143074,1762275064,1660733375,2985798234,3968418318,2440344775,2124752250,1632720711,1930884353,3582228124,1719559670,1611754727,2187103453,5091392475,1803744462,3833744132,2965138602,1767608354,5657476588,1646724250,3535176134,2185074745,2384889987,5386161998,1692776075,3682999864,2077660973,]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)