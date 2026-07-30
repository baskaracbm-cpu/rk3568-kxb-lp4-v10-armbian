# GPIO Audit

## Pinctrl

The DTS contains the RK3568 pinctrl controller.

Multiple board-specific pin groups are present.

## Important Groups

### Ethernet

- gmac0-miim
- gmac1m1-miim
- gmac1m1-rx-bus2
- gmac1m1-tx-bus2
- gmac1m1-rgmii-clk
- gmac1m1-rgmii-bus

### SDMMC

- sdmmc0-bus4
- sdmmc0-clk
- sdmmc0-cmd
- sdmmc0-det
- sdmmc1-bus4
- sdmmc1-clk
- sdmmc1-cmd

### HDMI

- hdmitxm0-cec
- hdmitx-scl
- hdmitx-sda

### Wireless

- wifi-enable-h
- wifi-32k
- wifi-host-wake-irq
- uart1-gpios

### mPCIe

- mpcie-pwr-en
- mpcie-rst-l

## Mainline Strategy

Only GPIO groups required by enabled peripherals
should be copied into the first mainline DTS.

Unused vendor pinctrl groups should remain disabled.

## Status

Pinctrl inventory: VERIFIED

Board electrical function: PARTIALLY VERIFIED

Mainline conversion: PENDING
