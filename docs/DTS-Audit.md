# RK3568 KXB LP4 V10 DTS Audit

## Source

Vendor DTS:

    rk3568-kxb-lp4-v10.dts

Board:

    Rockchip RK3568 KXB LP4 V10 Board

Compatible:

    rockchip,rk3568-kxb-lvds
    rockchip,rk3568

---

# Verified Hardware

| Subsystem | Finding | Status |
|---|---|---|
| CPU | Cortex-A55 x4 | VERIFIED |
| RAM | 4 GB LPDDR4 | VERIFIED externally |
| eMMC | SDHCI @ fe310000 | VERIFIED |
| eMMC mode | HS200 | VERIFIED by Android log |
| eMMC size | ~14.6 GiB | VERIFIED by Android log |
| SDIO | DW MMC @ fe2c0000 | VERIFIED |
| Wi-Fi | AP6212 | VERIFIED from DTS |
| Bluetooth | Vendor Bluetooth node | VERIFIED |
| GMAC0 | @ fe2a0000 | VERIFIED |
| GMAC1 | @ fe010000 | VERIFIED |
| HDMI | @ fe0a0000 | VERIFIED |
| VOP | @ fe040000 | VERIFIED |
| PCIe | 3 controllers | VERIFIED |
| GPU | Mali Bifrost | VERIFIED |
| UART | Multiple controllers | VERIFIED |
| TSADC | RK3568 | VERIFIED |
| USB2 PHY | RK3568 USB2PHY | VERIFIED |
| DWC3 | USB3/DRD | VERIFIED |

---

# Important Vendor Dependencies

The following should NOT simply be copied
into a mainline DTS:

- wlan-platdata
- bluetooth-platdata
- rockchip-specific debug infrastructure
- vendor Android bootargs
- FIQ debugger
- vendor-only power/OPP structures

These need separate mainline treatment.

---

# First Boot Priority

1. UART
2. PMIC / regulators
3. eMMC
4. USB
5. Ethernet
6. HDMI
7. SDIO/Wi-Fi
8. Bluetooth
9. Audio
10. GPU
11. PCIe

---

# Current Assessment

The vendor DTS contains enough information to begin
constructing a mainline board DTS.

However, the mainline DTS must be constructed selectively.

The complete vendor DTS should NOT be copied wholesale.

---

# Current Audit Status

Board mapping: 100%

Storage mapping: 90%

Wireless mapping: 80%

UART mapping: 80%

Display mapping: 70%

Ethernet mapping: 60%

USB mapping: 60%

PCIe mapping: 60%

GPU mapping: 50%

Audio mapping: 50%

Power/regulator mapping: 50%

Pinctrl mapping: 60%

Clock mapping: 40%

Overall: approximately 70%

The remaining work is primarily detailed property-level
comparison and mainline binding conversion.
