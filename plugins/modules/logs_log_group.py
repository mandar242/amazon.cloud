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
    arn:
        description:
        - The CloudWatch log group .
        type: str
    kms_key_id:
        description:
        - The Amazon Resource Name () of the  to use when encrypting log data.
        type: str
    log_group_name:
        description:
        - The name of the log group.
        - If you dont specify a name,  CloudFormation generates a unique  for the
            log group.
        type: str
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
        - create
        - update
        - delete
        - list
        - describe
        - get
        default: create
        description:
        - Goal state for resouirce.
        - I(state=create) creates the resouce.
        - I(state=update) updates the existing resouce.
        - I(state=delete) ensures an existing instance is deleted.
        - I(state=list) get all the existing resources.
        - I(state=describe) or I(state=get) retrieves information on an existing resource.
        type: str
    tags:
        description:
        - A key-value pair to associate with a resource.
        elements: dict
        suboptions:
            key:
                description:
                - The key name of the tag.
                - You can specify a value that is 1 to 128 Unicode characters in length
                    and cannot be prefixed with aws:.
                - 'You can use any of the following characters: the set of Unicode
                    letters, digits, whitespace, _, ., :, /, =, +, - and @.'
                required: true
                type: str
            value:
                description:
                - The value for the tag.
                - You can specify a value that is 0 to 256 Unicode characters in length.
                - 'You can use any of the following characters: the set of Unicode
                    letters, digits, whitespace, _, ., :, /, =, +, - and @.'
                required: true
                type: str
        type: list
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
version_added: TODO
requirements: []
"""

EXAMPLES = r"""
"""

RETURN = r"""
result:
    identifier:
        description: The unique identifier of the resource.
        type: str
    properties:
        description: The resource properties 
        type: complex
"""

import json

from ansible_collections.amazon.aws.plugins.module_utils.core import AnsibleAWSModule
from ansible_collections.amazon.cloud.plugins.module_utils.core import (
    CloudControlResource,
)
from ansible_collections.amazon.cloud.plugins.module_utils.utils import (
    snake_dict_to_camel_dict,
)


def main():

    argument_spec = dict(
        client_token=dict(type="str", no_log=True),
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
        "type": "list",
        "elements": "dict",
        "suboptions": {
            "key": {"type": "str", "required": True},
            "value": {"type": "str", "required": True},
        },
    }
    argument_spec["arn"] = {"type": "str"}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["create", "update", "delete", "list", "describe", "get"],
        "default": "create",
    }
    argument_spec["wait"] = {"type": "bool", "default": False}
    argument_spec["wait_timeout"] = {"type": "int", "default": 320}

    required_if = [
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

    params["tags"] = module.params.get("tags")
    params["retention_in_days"] = module.params.get("retention_in_days")
    params["kms_key_id"] = module.params.get("kms_key_id")
    params["log_group_name"] = module.params.get("log_group_name")
    params["arn"] = module.params.get("arn")

    # The DesiredState we pass to AWS must be a JSONArray of non-null values
    _params_to_set = {k: v for k, v in params.items() if v is not None}
    params_to_set = snake_dict_to_camel_dict(_params_to_set, capitalize_first=True)

    desired_state = json.dumps(params_to_set)
    state = module.params.get("state")
    identifier = module.params.get("log_group_name")

    results = {"changed": False, "result": []}

    if state == "list":
        results["result"] = cloud.list_resources(type_name)

    if state == ("describe", "get"):
        results["result"] = cloud.get_resource(type_name, identifier)

    if state == "create":
        results["changed"] |= cloud.create_resource(
            type_name, identifier, desired_state
        )
        results["result"] = cloud.get_resource(type_name, identifier)

    if state == "update":
        results["changed"] |= cloud.update_resource(
            type_name, identifier, params_to_set
        )
        results["result"] = cloud.get_resource(type_name, identifier)

    if state == "delete":
        results["changed"] |= cloud.delete_resource(type_name, identifier)

    module.exit_json(**results)


if __name__ == "__main__":
    main()