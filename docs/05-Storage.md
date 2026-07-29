# Storage Subsystem

## Overview

Board menyediakan tiga controller storage:

| Controller | Fungsi | Status |
|------------|---------|--------|
| SDHCI | Internal eMMC | Detected |
| SDMMC | External MicroSD | Detected |
| SDIO | WiFi Module | Detected |

---

## SDHCI (eMMC)

Purpose

Internal boot storage.

Linux Driver

sdhci-of-dwcmshc

Audit

- [ ] compatible
- [ ] reg
- [ ] interrupt
- [ ] clock
- [ ] bus-width
- [ ] cap-mmc-highspeed
- [ ] HS200
- [ ] HS400
- [ ] non-removable
- [ ] vmmc-supply
- [ ] vqmmc-supply

Expected

Kernel should detect:

mmc0

---

## SDMMC

Purpose

External MicroSD slot.

Linux Driver

dw_mmc-rockchip

Audit

- [ ] card detect GPIO
- [ ] write protect
- [ ] bus-width
- [ ] max-frequency
- [ ] pinctrl

Expected

Kernel should detect:

mmc1

---

## SDIO

Purpose

WiFi module.

Audit

- [ ] bus-width
- [ ] keep-power-in-suspend
- [ ] wakeup-source
- [ ] non-removable

Expected

Kernel should detect WiFi chip during boot.

---

## Porting Risk

LOW

RK3568 storage drivers already exist in Linux Mainline.

Only board configuration must be verified.
