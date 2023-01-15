# Adalm-pluto Transmit issue, intermintment TX

![Sdr console](dash.png)

As you see on the picture combination Tx+Tone should produce uninterrupted signal, not a signal with the breaks.

As you  are able to see intermintment trasmit problems, when using usb network card + pluto . The issue does not reocure on usb interface.

Changing one stupid switch for other one, does not resolve the situation. 
After enabling flow-control on the switch, issue gone.

Please consult your sdr console log to check networking problems.

As well I recommend to update to 1G card, but issue was resolved also on 100mBit with flow control.
