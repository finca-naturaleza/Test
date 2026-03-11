import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import pins
from esphome.const import CONF_ID, CONF_PIN
from esphome.components import sensor, output, number
from esphome.cpp_helpers import gpio_pin_expression

my_empty_component_ns = cg.esphome_ns.namespace("my_empty_component")
MyEmptyComponent = my_empty_component_ns.class_("MyEmptyComponent", cg.Component)

CONF_SENSOR = "sensor"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(MyEmptyComponent),
        cv.Required(CONF_PIN): pins.gpio_output_pin_schema,
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])

    # sens = await cg.get_variable(config[CONF_SENSOR])
    # cg.add(var.set_sensor(sens))

    await cg.register_component(var, config)
    
    pin = await gpio_pin_expression(config[CONF_PIN])
    cg.add(var.set_output_pin(pin))