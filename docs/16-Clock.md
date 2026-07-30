# Clock Audit

## External GMAC Clocks

The DTS contains:

    external-gmac0-clock

    external-gmac1-clock

and XPCS clocks:

    xpcs-gmac0-clock

    xpcs-gmac1-clock

These are represented as fixed clocks in the vendor DTS.

## Implication

Ethernet mainline conversion must preserve the correct
clock relationship for the selected GMAC/PHY.

## Other Clocks

The vendor DTS contains additional fixed-clock and
subsystem-specific clock definitions.

## Mainline Strategy

Do not copy vendor fixed-clock nodes automatically.

Each clock must be checked against the RK3568 mainline
clock binding and driver.

## Status

GMAC clock inventory: VERIFIED

Full clock audit: PENDING
