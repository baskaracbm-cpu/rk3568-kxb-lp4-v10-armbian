# Thermal Audit

## Temperature Sensor

The DTS contains:

    compatible = "rockchip,rk3568-tsadc"

This indicates the RK3568 thermal ADC/temperature
sensor is defined.

## Mainline

Thermal support should be retained in the mainline DTS
because CPU thermal management is important for stable
operation.

## Status

TSADC node: VERIFIED

Thermal zones: PENDING DETAILED AUDIT

## Priority

HIGH
