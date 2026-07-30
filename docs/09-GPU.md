# GPU Audit

## Hardware

The vendor DTS contains a GPU node at:

    gpu@fde60000

The node uses:

    compatible = "arm,mali-bifrost"

The DTS also contains:

- GPU operating-points
- GPU PVTM
- IOMMU
- GPU power model

Source evidence:

- `arm,mali-bifrost`
- GPU OPP table
- GPU PVTM
- GPU IOMMU

## Mainline Assessment

The GPU should be treated separately from the basic RK3568
bring-up.

For the first boot target, GPU acceleration is not required.

## Bring-up Priority

1. Kernel boot
2. eMMC
3. USB
4. Ethernet
5. HDMI
6. GPU acceleration

## Status

Detected: YES

Mainline conversion: PENDING

Validation on board: PENDING

## Risk

MEDIUM

The vendor DTS contains additional GPU power/OPP information
which must be compared against the target mainline kernel.
