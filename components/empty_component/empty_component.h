#pragma once

#include "esphome/core/component.h"

namespace esphome {
namespace empty_component {

class EmptyComponent : public Component {
 public:
  void setup() override;
  void loop() override;
  void dump_config() override;
  
  void set_sensor(sensor::Sensor *sensor) { sensor_ = sensor; }
  
 protected:
  sensor::Sensor *sensor_{nullptr};
};


}  // namespace empty_component
}  // namespace esphome