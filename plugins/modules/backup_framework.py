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
module: backup_framework
short_description: Create and manage frameworks with one or more controls
description: Creates and manages frameworks with one or more controls (list, create,
    update, describe, delete).
options:
    framework_arn:
        description:
        - An Amazon Resource Name (ARN) that uniquely identifies Framework as a resource
        type: str
    framework_controls:
        description:
        - Contains detailed information about all of the controls of a framework.
        - Each framework must contain at least one control.
        elements: dict
        required: true
        suboptions:
            control_input_parameters:
                description:
                - A list of I(parameter_name) and I(parameter_value) pairs.
                elements: dict
                suboptions:
                    parameter_name:
                        description:
                        - Not Provived.
                        required: true
                        type: str
                    parameter_value:
                        description:
                        - Not Provived.
                        required: true
                        type: str
                type: list
            control_name:
                description:
                - The name of a control.
                - This name is between 1 and 256 characters.
                required: true
                type: str
            control_scope:
                description:
                - The scope of a control.
                - The control scope defines what the control will evaluate.
                - 'Three examples of control scopes are: a specific backup plan, all
                    backup plans with a specific tag, or all backup plans.'
                suboptions:
                    compliance_resource_ids:
                        description:
                        - The ID of the only AWS resource that you want your control
                            scope to contain.
                        elements: str
                        type: list
                    compliance_resource_types:
                        description:
                        - Describes whether the control scope includes one or more
                            types of resources, such as `EFS` or `RDS`.
                        elements: str
                        type: list
                    tags:
                        description:
                        - A key-value pair to associate with a resource.
                        elements: dict
                        suboptions:
                            key:
                                description:
                                - The key name of the tag.
                                - You can specify a value that is 1 to 128 Unicode
                                    characters in length and cannot be prefixed with
                                    aws:.
                                - 'You can use any of the following characters: the
                                    set of Unicode letters, digits, whitespace, _,
                                    ., /, =, +, and -.'
                                required: true
                                type: str
                            value:
                                description:
                                - The value for the tag.
                                - You can specify a value that is 0 to 256 Unicode
                                    characters in length and cannot be prefixed with
                                    aws:.
                                - 'You can use any of the following characters: the
                                    set of Unicode letters, digits, whitespace, _,
                                    ., /, =, +, and -.'
                                required: true
                                type: str
                        type: list
                type: dict
        type: list
    framework_description:
        description:
        - An optional description of the framework with a maximum 1,024 characters.
        type: str
    framework_name:
        description:
        - The unique name of a framework.
        - This name is between 1 and 256 characters, starting with a letter, and consisting
            of letters (a-z, A-Z), numbers (0-9), and underscores (_).
        type: str
    framework_tags:
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
                    letters, digits, whitespace, _, ., /, =, +, and -.'
                required: true
                type: str
            value:
                description:
                - The value for the tag.
                - You can specify a value that is 0 to 256 Unicode characters in length
                    and cannot be prefixed with aws:.
                - 'You can use any of the following characters: the set of Unicode
                    letters, digits, whitespace, _, ., /, =, +, and -.'
                required: true
                type: str
        type: list
    purge_tags:
        default: true
        description:
        - Remove tags not listed in I(tags).
        required: false
        type: bool
    state:
        choices:
        - present
        - absent
        - list
        - describe
        - get
        default: present
        description:
        - Goal state for resource.
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
version_added: 0.1.0
requirements: []
extends_documentation_fragment:
- amazon.cloud.aws
- amazon.cloud.ec2
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
            choices=["present", "absent", "list", "describe", "get"],
            default="present",
        ),
    )

    argument_spec["framework_name"] = {"type": "str"}
    argument_spec["framework_description"] = {"type": "str"}
    argument_spec["framework_arn"] = {"type": "str"}
    argument_spec["framework_controls"] = {
        "type": "list",
        "elements": "dict",
        "options": {
            "control_name": {"type": "str", "required": True},
            "control_input_parameters": {
                "type": "list",
                "elements": "dict",
                "options": {
                    "parameter_name": {"type": "str", "required": True},
                    "parameter_value": {"type": "str", "required": True},
                },
            },
            "control_scope": {
                "type": "dict",
                "options": {
                    "compliance_resource_ids": {"type": "list", "elements": "str"},
                    "compliance_resource_types": {"type": "list", "elements": "str"},
                    "tags": {
                        "type": "list",
                        "elements": "dict",
                        "options": {
                            "key": {"type": "str", "required": True},
                            "value": {"type": "str", "required": True},
                        },
                    },
                },
            },
        },
        "required": True,
    }
    argument_spec["framework_tags"] = {
        "type": "list",
        "elements": "dict",
        "options": {
            "key": {"type": "str", "required": True},
            "value": {"type": "str", "required": True},
        },
    }
    argument_spec["state"] = {
        "type": "str",
        "choices": ["present", "absent", "list", "describe", "get"],
        "default": "present",
    }
    argument_spec["wait"] = {"type": "bool", "default": False}
    argument_spec["wait_timeout"] = {"type": "int", "default": 320}
    argument_spec["tags"] = {
        "type": "dict",
        "required": False,
        "aliases": ["resource_tags"],
    }
    argument_spec["purge_tags"] = {"type": "bool", "required": False, "default": True}

    required_if = [
        ["state", "present", ["framework_controls"], True],
        ["state", "absent", [], True],
        ["state", "get", [], True],
    ]

    module = AnsibleAWSModule(
        argument_spec=argument_spec, required_if=required_if, supports_check_mode=True
    )
    cloud = CloudControlResource(module)

    type_name = "AWS::Backup::Framework"

    params = {}

    params["framework_arn"] = module.params.get("framework_arn")
    params["framework_controls"] = module.params.get("framework_controls")
    params["framework_description"] = module.params.get("framework_description")
    params["framework_name"] = module.params.get("framework_name")
    params["framework_tags"] = module.params.get("framework_tags")
    params["tags"] = module.params.get("tags")

    # The DesiredState we pass to AWS must be a JSONArray of non-null values
    _params_to_set = {k: v for k, v in params.items() if v is not None}

    # Only if resource is taggable
    if module.params.get("tags", None):
        _params_to_set["tags"] = ansible_dict_to_boto3_tag_list(module.params["tags"])

    params_to_set = snake_dict_to_camel_dict(_params_to_set, capitalize_first=True)

    # Ignore createOnlyProperties that can be set only during resource creation
    create_only_params = ["framework_name"]

    state = module.params.get("state")
    identifier = module.params.get("framework_arn")

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
        results["changed"] |= cloud.absent(type_name, identifier)

    module.exit_json(**results)


if __name__ == "__main__":
    main()