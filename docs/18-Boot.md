# Boot Audit

## Current Vendor Boot

The Android system uses:

- eMMC as boot storage
- vendor boot arguments
- vendor DTB/DTBO
- Android-specific console configuration

The vendor kernel command line identifies:

    androidboot.storagemedia=emmc

and:

    androidboot.boot_devices=fe310000.sdhci,fe330000.nandc

## eMMC

The running system detects:

    mmc2

at:

    fe310000.sdhci

The device is detected as HS200 and has approximately
14.6 GiB usable capacity.

## Mainline Boot Strategy

First target:

    U-Boot
        |
        v
    Mainline Linux
        |
        v
    UART console
        |
        v
    eMMC / USB
        |
        v
    Debian userspace

## First Boot Requirements

Required:

- UART
- CPU
- RAM
- PMIC/regulators
- eMMC or USB boot medium
- timer
- interrupt controller

Not required for first boot:

- GPU
- Wi-Fi
- Bluetooth
- Audio
- PCIe

## Status

Vendor boot path: VERIFIED

Mainline boot path: NOT YET IMPLEMENTED
