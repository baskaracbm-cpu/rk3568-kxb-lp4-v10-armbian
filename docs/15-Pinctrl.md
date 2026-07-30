# Pinctrl Audit

## Controller

Compatible:

    rockchip,rk3568-pinctrl

The controller contains multiple GPIO banks.

## Board-specific Pinmux

The vendor DTS defines pinmux groups for:

- Ethernet
- HDMI
- SDMMC
- UART
- Wi-Fi
- Bluetooth
- mPCIe

## Mainline Requirement

The mainline DTS should not blindly import the complete
vendor pinctrl tree.

Instead:

1. Identify peripherals enabled on the board.
2. Select the required pin groups.
3. Remove unused vendor-only references.
4. Validate pin conflicts.

## High Priority

The following must be validated first:

- UART debug
- eMMC/SD
- Ethernet
- USB
- HDMI

## Status

Controller: VERIFIED

Pin groups: INVENTORIED

Electrical validation: PENDING
