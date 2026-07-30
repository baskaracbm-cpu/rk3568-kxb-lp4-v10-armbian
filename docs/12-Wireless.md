# Wireless Audit

## Wi-Fi

The vendor DTS contains:

    sdio-pwrseq

using:

    compatible = "mmc-pwrseq-simple"

The vendor platform data identifies the Wi-Fi module as:

    wifi_chip_type = "ap6212"

The Wi-Fi host wake information is also present.

## SDIO

The SDIO controller is mapped through:

    dwmmc@fe2c0000

The Android boot log confirms:

    mmc1: card is non-removable
    mmc1: new SDIO card

This confirms that the SDIO device is actually present
on the running board.

## Bluetooth

The vendor DTS contains:

    wireless-bluetooth

with:

    compatible = "bluetooth-platdata"

and a UART RTS GPIO definition.

## Important Mainline Note

The vendor nodes:

    wlan-platdata
    bluetooth-platdata

are vendor-specific platform-data mechanisms.

They must NOT simply be copied into the mainline DTS.

The required GPIO, power and UART relationships must
instead be represented using mainline-supported bindings.

## Status

Wi-Fi module identification: VERIFIED

Wi-Fi SDIO presence: VERIFIED

Bluetooth vendor node: VERIFIED

Mainline Wi-Fi binding: PENDING

Mainline Bluetooth binding: PENDING

## Risk

HIGH

Wireless should be handled after the basic kernel boot,
storage, USB and Ethernet path is stable.
