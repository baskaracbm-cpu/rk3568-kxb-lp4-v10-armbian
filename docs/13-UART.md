# UART Audit

## UART Controllers

The vendor DTS contains multiple RK3568 UART nodes.

Aliases identify:

- uart0
- uart1
- uart2
- uart3
- uart4
- uart5
- uart6
- uart7
- uart8
- uart9

## Debug Console

The vendor bootargs use:

    earlycon=uart8250,mmio32,0xfe660000

and:

    console=ttyFIQ0

Therefore the Android vendor system uses the UART at:

    fe660000

as its early/debug console.

## Mainline Bring-up

The CH340 serial adapter should be connected to
the board's debug UART.

For the first mainline boot, UART logging is mandatory.

## Status

UART hardware: VERIFIED

Vendor debug UART address: VERIFIED

Mainline console configuration: PENDING

Board TX/RX/GND pin mapping: NEEDS PHYSICAL VERIFICATION
