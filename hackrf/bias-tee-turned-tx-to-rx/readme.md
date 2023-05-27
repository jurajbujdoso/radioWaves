# HackRF- repair 

I have used bias tee circuit and wrongly assign tx and rx part.
So the power voltage for LNB has been directed to hackrf antenna.

As side effect device smells.
After some time, I have remove the RF cover plate and find out affected parts near the antenna.

I have used the schematic to identify fail parts, but the quickest way forward is open Assembly and BOM files.
In my case L13 and Q4 has been damaged and I have also fix the pcb connection between this 2 elements.

In my case D1,R36,C64,C63 work as design.

```
D1.D3.D9	         GSG-DIODE-TVS-BI	Murata	LXES15AAA1-100	TVS DIODE ESD .05PF 15KV 0402
L2.L3.L5.L12.L13	10uH	Taiyo Yuden	BRL1608T100M	INDUCTR 10UH 220MA 20% 0603 SMD
Q1.Q2.Q4	        MOSFET_P	Fairchild	BSS84	MOSFET P-CH 50V 130MA SOT-23
```
I was not able to buy BSS84 on mouser, but it is not an problem to buy it on aliexpress.

As there are more version of product, try to find out PCB which is ~ to your release.


HackRF assembly:
http://uglyduck.vajn.icu/PDF/hackrf/hardware/hackrf-one-assembly.pdf


HACKRF Bom:
https://raw.githubusercontent.com/gazhayes/HackRF-Blue/master/BOM.xlsx

HackRF schematic:
https://cdn.greatrf.com/wp-content/uploads/2014/06/HackRF-Schematic.pdf



