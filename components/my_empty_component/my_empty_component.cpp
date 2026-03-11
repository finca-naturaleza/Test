#include "esphome/core/log.h"
#include "my_empty_component.h"

namespace esphome {
namespace empty_component {

static const char *TAG = "my_empty_component.component";

void MyEmptyComponent::setup() {

}

void MyEmptyComponent::loop() {

}

void MyEmptyComponent::dump_config(){
    ESP_LOGCONFIG(TAG, "Empty component");
}


}  // namespace empty_component
}  // namespace esphome