#pragma once

#include "esphome/core/component.h"

namespace esphome {
namespace my_empty_component {

class MyEmptyComponent : public Component {
 public:
  void setup() override;
  void loop() override;
  void dump_config() override;
  
  void set_sensor(sensor::Sensor *sensor) { sensor_ = sensor; }
  void set_output_pin(GPIOPin *pin) { this->pin_ = pin; }

 protected:
  GPIOPin *pin_;
  sensor::Sensor *sensor_{nullptr};
};


}  // namespace my_empty_component
}  // namespace esphome