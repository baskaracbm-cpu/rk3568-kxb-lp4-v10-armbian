# Audio Audit

## Audio Controllers

The vendor DTS contains:

- RK3568 I2S/TDM controllers
- RK3568 PDM
- RK3568 VAD
- RK3568 SPDIF
- RK3568 audio PWM
- RK3568 digital codec

## Audio Cards

The DTS also contains:

- HDMI simple-audio-card
- dummy codec
- SPDIF DIT
- multicodecs card

## HDMI Audio

The vendor DTS defines:

    hdmi-sound

with:

    compatible = "simple-audio-card"

and:

    simple-audio-card,name = "rockchip,hdmi"

## Mainline Strategy

Audio should be enabled after HDMI video output is
confirmed.

## Status

Hardware nodes: VERIFIED

Vendor audio topology: VERIFIED

Mainline topology: PENDING

Board speaker/codec wiring: NEEDS VERIFICATION

## Risk

MEDIUM
