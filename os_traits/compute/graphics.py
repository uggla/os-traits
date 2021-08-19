# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

TRAITS = [
    # traits corresponding to the allowed values of "hw_video_model"
    # image metadata property
    # https://github.com/openstack/nova/blob/1f74441/nova/objects/fields.py#L501-L509
    'MODEL_BOCHS',
    'MODEL_CIRRUS',
    'MODEL_GOP',
    'MODEL_NONE',
    'MODEL_QXL',
    'MODEL_VGA',
    'MODEL_VIRTIO',
    'MODEL_VMVGA',
    'MODEL_XEN',
]
