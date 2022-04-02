#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated by amazon_cloud_code_generator.
# See: https://github.com/ansible-collections/amazon_cloud_code_generator

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: logs_log_group
short_description: Create and manage log groups
description: Create and manage log groups (list, create, update, describe, delete).
options:
    kms_key_id:
        description:
        - The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
        type: str
    log_group_name:
        description:
        - The name of the log group.
        - If you dont specify a name, AWS CloudFormation generates a unique ID for
            the log group.
        type: str
    purge_tags:
        default: true
        description:
        - Remove tags not listed in I(tags).
        required: false
        type: bool
    retention_in_days:
        choices:
        - 1
        - 3
        - 5
        - 7
        - 14
        - 30
        - 60
        - 90
        - 120
        - 150
        - 180
        - 365
        - 400
        - 545
        - 731
        - 1827
        - 3653
        description:
        - The number of days to retain the log events in the specified log group.
        - 'Possible values are: C(1), C(3), C(5), C(7), C(14), C(30), C(60), C(90),
            C(120), C(150), C(180), C(365), C(400), C(545), C(731), C(1827), and C(3653).'
        type: int
    state:
        choices:
        - present
        - absent
        - list
        - describe
        - get
        default: present
        description:
        - Goal state for resouirce.
        - I(state=present) creates the resource if it doesn't exist, or updates to
            the provided state if the resource already exists.
        - I(state=absent) ensures an existing instance is deleted.
        - I(state=list) get all the existing resources.
        - I(state=describe) or I(state=get) retrieves information on an existing resource.
        type: str
    tags:
        aliases:
        - resource_tags
        description:
        - A dict of tags to apply to the resource.
        - To remove all tags set I(tags={}) and I(purge_tags=true).
        required: false
        type: dict
    wait:
        default: false
        description:
        - Wait for operation to complete before returning.
        type: bool
    wait_timeout:
        default: 320
        description:
        - How many seconds to wait for an operation to complete before timing out.
        type: int
author: Ansible Cloud Team (@ansible-collections)
version_added: 0.0.1
requirements: []
extends_documentation_fragment:
- amazon.aws.aws
- amazon.aws.ec2
"""

EXAMPLES = r"""
"""

RETURN = r"""
result:
    description: Dictionary containing resource information.
    returned: always
    type: complex
    contains:
        identifier:
            description: The unique identifier of the resource.
            type: str
        properties:
            description: The resource properties.
            type: dict
"""

import json

from ansible_collections.amazon.aws.plugins.module_utils.core import AnsibleAWSModule
from ansible_collections.amazon.cloud.plugins.module_utils.core import (
    CloudControlResource,
)
from ansible_collections.amazon.cloud.plugins.module_utils.core import (
    snake_dict_to_camel_dict,
)
from ansible_collections.amazon.cloud.plugins.module_utils.core import (
    ansible_dict_to_boto3_tag_list,
)


def main():

    argument_spec = dict(
        state=dict(
            type="str",
            choices=["create", "update", "delete", "list", "describe", "get"],
            default="create",
        ),
    )

    argument_spec["log_group_name"] = {"type": "str"}
    argument_spec["kms_key_id"] = {"type": "str"}
    argument_spec["retention_in_days"] = {
        "type": "int",
        "choices": [
            1,
            3,
            5,
            7,
            14,
            30,
            60,
            90,
            120,
            150,
            180,
            365,
            400,
            545,
            731,
            1827,
            3653,
        ],
    }
    argument_spec["tags"] = {
        "type": "dict",
        "required": False,
        "aliases": ["resource_tags"],
    }
    argument_spec["state"] = {
        "type": "str",
        "choices": ["present", "absent", "list", "describe", "get"],
        "default": "present",
    }
    argument_spec["wait"] = {"type": "bool", "default": False}
    argument_spec["wait_timeout"] = {"type": "int", "default": 320}
    argument_spec["purge_tags"] = {"type": "bool", "required": False, "default": True}

    required_if = [
        ["state", "create", ["log_group_name"], True],
        ["state", "update", ["log_group_name"], True],
        ["state", "delete", ["log_group_name"], True],
        ["state", "get", ["log_group_name"], True],
    ]

    module = AnsibleAWSModule(
        argument_spec=argument_spec, required_if=required_if, supports_check_mode=True
    )
    cloud = CloudControlResource(module)

    type_name = "AWS::Logs::LogGroup"

    params = {}

    params["kms_key_id"] = module.params.get("kms_key_id")
    params["log_group_name"] = module.params.get("log_group_name")
    params["retention_in_days"] = module.params.get("retention_in_days")
    params["tags"] = module.params.get("tags")

    # The DesiredState we pass to AWS must be a JSONArray of non-null values
    _params_to_set = {k: v for k, v in params.items() if v is not None}

    # Only if resource is taggable
    if module.params.get("tags", None):
        _params_to_set["tags"] = ansible_dict_to_boto3_tag_list(module.params["tags"])

    params_to_set = snake_dict_to_camel_dict(_params_to_set, capitalize_first=True)

    # Ignore createOnlyProperties that can be set only during resource creation
    create_only_params = ["log_group_name"]

    state = module.params.get("state")
    identifier = module.params.get("log_group_name")

    results = {"changed": False, "result": []}

    if state == "list":
        results["result"] = cloud.list_resources(type_name)

    if state in ("describe", "get"):
        results["result"] = cloud.get_resource(type_name, identifier)

    if state == "present":
        results["changed"] |= cloud.present(
            type_name, identifier, params_to_set, create_only_params
        )
        results["result"] = cloud.get_resource(type_name, identifier)

    if state == "absent":
        results["changed"] |= cloud.delete_resource(type_name, identifier)

    module.exit_json(**results)


if __name__ == "__main__":
    main()
