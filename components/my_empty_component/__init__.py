import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import pins
from esphome.const import CONF_ID, CONF_PIN, CONF_UPDATE_INTERVAL
from esphome.components import sensor, output, number
from esphome.cpp_helpers import gpio_pin_expression

my_empty_component_ns = cg.esphome_ns.namespace("my_empty_component")
MyEmptyComponent = my_empty_component_ns.class_("MyEmptyComponent", cg.Component)

CONF_SENSOR = "sensor"
CONF_RELAY = "relay"
CONF_SETPOINT = "setpoint"
CONF_DEADBAND = "deadband"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(MyEmptyComponent),
        cv.Required(CONF_PIN): pins.gpio_output_pin_schema,
        
        cv.Required(CONF_SENSOR): cv.use_id(sensor.Sensor),
        cv.Required(CONF_RELAY): cv.use_id(output.BinaryOutput),
        cv.Required(CONF_SETPOINT): cv.use_id(number.Number),

        cv.Optional(CONF_UPDATE_INTERVAL, default="10s"): cv.positive_time_period_milliseconds,
        cv.Optional(CONF_DEADBAND, default=0.0): cv.float_,
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])

    sens = await cg.get_variable(config[CONF_SENSOR])
    cg.add(var.set_sensor(sens))

    relay = await cg.get_variable(config[CONF_RELAY])
    cg.add(var.set_relay(relay))

    setpoint = await cg.get_variable(config[CONF_SETPOINT])
    cg.add(var.set_setpoint(setpoint))

    cg.add(var.set_update_interval(config[CONF_UPDATE_INTERVAL]))
    cg.add(var.set_deadband(config[CONF_DEADBAND]))

    await cg.register_component(var, config)
    
    pin = await gpio_pin_expression(config[CONF_PIN])
    cg.add(var.set_output_pin(pin))