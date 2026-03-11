import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID
from esphome.components import sensor, output, number

empty_component_ns = cg.esphome_ns.namespace("empty_component")
EmptyComponent = empty_component_ns.class_("EmptyComponent", cg.Component)

CONF_SENSOR = "sensor"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(EmptyComponent),
        cv.Required(CONF_SENSOR): cv.use_id(sensor.Sensor),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    
    sens = await cg.get_variable(config[CONF_SENSOR])
    cg.add(var.set_sensor(sens))

    await cg.register_component(var, config)