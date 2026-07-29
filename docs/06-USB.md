# USB

## Controllers

Detected

- USB2 PHY
- DWC3

---

## USB2 PHY

Audit

- [ ] host
- [ ] otg
- [ ] regulator
- [ ] clock

---

## USB3

Audit

- [ ] xhci
- [ ] superspeed
- [ ] phy

---

## OTG

Audit

- [ ] dr_mode
- [ ] extcon
- [ ] id gpio

---

## Linux Drivers

rockchip-usb2phy

dwc3

xhci-platform

---

## Porting Risk

Medium

OTG configuration differs between Android BSP and Linux Mainline.
