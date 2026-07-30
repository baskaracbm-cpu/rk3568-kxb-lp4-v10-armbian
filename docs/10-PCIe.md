# PCIe Audit

## Controllers

The vendor DTS contains three PCIe controllers:

| Address | Controller |
|---|---|
| fe260000 | PCIe 2x1 |
| fe270000 | PCIe 3x1 |
| fe280000 | PCIe 3x2 |

The aliases section identifies them as:

- pcie2x1
- pcie3x1
- pcie3x2

## PHY

The DTS provides PCIe PHY references and
a Rockchip RK3568 PCIe3 PHY.

## Possible Uses

The board DTS also contains:

- mPCIe power control
- mPCIe reset control

The vendor DTS therefore contains board-level support
for an mPCIe-related device.

## Mainline Conversion

PCIe should not be enabled blindly in the first image.

First determine which physical connector is populated
on the KXB LP4 V10 board.

## Bring-up Priority

LOW for first boot.

MEDIUM for complete board support.

## Status

Controller detection: VERIFIED

Physical board mapping: NEEDS VERIFICATION

Mainline conversion: PENDING
