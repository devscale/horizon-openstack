# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import copy

from openstack_dashboard.api.quantum import (Network, Subnet, Port,
                                             Router, FloatingIp)

from .utils import TestDataContainer


def data(TEST):
    # data returned by openstack_dashboard.api.quantum wrapper
    TEST.networks = TestDataContainer()
    TEST.subnets = TestDataContainer()
    TEST.ports = TestDataContainer()
    TEST.routers = TestDataContainer()
    TEST.q_floating_ips = TestDataContainer()

    # data return by quantumclient
    TEST.api_networks = TestDataContainer()
    TEST.api_subnets = TestDataContainer()
    TEST.api_ports = TestDataContainer()
    TEST.api_routers = TestDataContainer()
    TEST.api_q_floating_ips = TestDataContainer()

    #------------------------------------------------------------
    # 1st network
    network_dict = {'admin_state_up': True,
                    'id': '82288d84-e0a5-42ac-95be-e6af08727e42',
                    'name': 'net1',
                    'status': 'ACTIVE',
                    'subnets': ['e8abc972-eb0c-41f1-9edd-4bc6e3bcd8c9'],
                    'tenant_id': '1',
                    'router:external': False,
                    'shared': False}
    subnet_dict = {'allocation_pools': [{'end': '10.0.0.254',
                                         'start': '10.0.0.2'}],
                   'dns_nameservers': [],
                   'host_routes': [],
                   'cidr': '10.0.0.0/24',
                   'enable_dhcp': True,
                   'gateway_ip': '10.0.0.1',
                   'id': network_dict['subnets'][0],
                   'ip_version': 4,
                   'name': 'mysubnet1',
                   'network_id': network_dict['id'],
                   'tenant_id': network_dict['tenant_id']}

    TEST.api_networks.add(network_dict)
    TEST.api_subnets.add(subnet_dict)

    network = copy.deepcopy(network_dict)
    subnet = Subnet(subnet_dict)
    network['subnets'] = [subnet]
    TEST.networks.add(Network(network))
    TEST.subnets.add(subnet)

    # ports on 1st network
    port_dict = {'admin_state_up': True,
                 'device_id': 'af75c8e5-a1cc-4567-8d04-44fcd6922890',
                 'device_owner': 'network:dhcp',
                 'fixed_ips': [{'ip_address': '10.0.0.3',
                                'subnet_id': subnet_dict['id']}],
                 'id': '3ec7f3db-cb2f-4a34-ab6b-69a64d3f008c',
                 'mac_address': 'fa:16:3e:9c:d5:7e',
                 'name': '',
                 'network_id': network_dict['id'],
                 'status': 'ACTIVE',
                 'tenant_id': network_dict['tenant_id']}
    TEST.api_ports.add(port_dict)
    TEST.ports.add(Port(port_dict))

    port_dict = {'admin_state_up': True,
                 'device_id': '1',
                 'device_owner': 'compute:nova',
                 'fixed_ips': [{'ip_address': '10.0.0.4',
                                'subnet_id': subnet_dict['id']}],
                 'id': '7e6ce62c-7ea2-44f8-b6b4-769af90a8406',
                 'mac_address': 'fa:16:3e:9d:e6:2f',
                 'name': '',
                 'network_id': network_dict['id'],
                 'status': 'ACTIVE',
                 'tenant_id': network_dict['tenant_id']}
    TEST.api_ports.add(port_dict)
    TEST.ports.add(Port(port_dict))
    assoc_port = port_dict

    #------------------------------------------------------------
    # 2nd network
    network_dict = {'admin_state_up': True,
                    'id': '72c3ab6c-c80f-4341-9dc5-210fa31ac6c2',
                    'name': 'net2',
                    'status': 'ACTIVE',
                    'subnets': ['3f7c5d79-ee55-47b0-9213-8e669fb03009'],
                    'tenant_id': '2',
                    'router:external': False,
                    'shared': True}
    subnet_dict = {'allocation_pools': [{'end': '172.16.88.254',
                                         'start': '172.16.88.2'}],
                   'dns_nameservers': ['10.56.1.20', '10.56.1.21'],
                   'host_routes': [{'destination': '192.168.20.0/24',
                                    'nexthop': '172.16.88.253'},
                                   {'destination': '192.168.21.0/24',
                                    'nexthop': '172.16.88.252'}],
                   'cidr': '172.16.88.0/24',
                   'enable_dhcp': True,
                   'gateway_ip': '172.16.88.1',
                   'id': '3f7c5d79-ee55-47b0-9213-8e669fb03009',
                   'ip_version': 4,
                   'name': 'aaaa',
                   'network_id': network_dict['id'],
                   'tenant_id': network_dict['tenant_id']}

    TEST.api_networks.add(network_dict)
    TEST.api_subnets.add(subnet_dict)

    network = copy.deepcopy(network_dict)
    subnet = Subnet(subnet_dict)
    network['subnets'] = [subnet]
    TEST.networks.add(Network(network))
    TEST.subnets.add(subnet)

    port_dict = {'admin_state_up': True,
                 'device_id': '2',
                 'device_owner': 'compute:nova',
                 'fixed_ips': [{'ip_address': '172.16.88.3',
                                'subnet_id': subnet_dict['id']}],
                 'id': '1db2cc37-3553-43fa-b7e2-3fc4eb4f9905',
                 'mac_address': 'fa:16:3e:56:e6:2f',
                 'name': '',
                 'network_id': network_dict['id'],
                 'status': 'ACTIVE',
                 'tenant_id': network_dict['tenant_id']}

    TEST.api_ports.add(port_dict)
    TEST.ports.add(Port(port_dict))

    #------------------------------------------------------------
    # external network
    network_dict = {'admin_state_up': True,
                    'id': '9b466b94-213a-4cda-badf-72c102a874da',
                    'name': 'ext_net',
                    'status': 'ACTIVE',
                    'subnets': ['d6bdc71c-7566-4d32-b3ff-36441ce746e8'],
                    'tenant_id': '3',
                    'router:external': True,
                    'shared': False}
    subnet_dict = {'allocation_pools': [{'start': '172.24.4.226.',
                                         'end': '172.24.4.238'}],
                   'dns_nameservers': [],
                   'host_routes': [],
                   'cidr': '172.24.4.0/28',
                   'enable_dhcp': False,
                   'gateway_ip': '172.24.4.225',
                   'id': 'd6bdc71c-7566-4d32-b3ff-36441ce746e8',
                   'ip_version': 4,
                   'name': 'ext_subnet',
                   'network_id': network_dict['id'],
                   'tenant_id': network_dict['tenant_id']}
    ext_net = network_dict
    ext_subnet = subnet_dict

    TEST.api_networks.add(network_dict)
    TEST.api_subnets.add(subnet_dict)

    network = copy.deepcopy(network_dict)
    subnet = Subnet(subnet_dict)
    network['subnets'] = [subnet]
    TEST.networks.add(Network(network))
    TEST.subnets.add(subnet)

    #------------------------------------------------------------
    # Set up router data
    port_dict = {'admin_state_up': True,
                 'device_id': '7180cede-bcd8-4334-b19f-f7ef2f331f53',
                 'device_owner': 'network:router_gateway',
                 'fixed_ips': [{'ip_address': '10.0.0.3',
                                'subnet_id': subnet_dict['id']}],
                 'id': '3ec7f3db-cb2f-4a34-ab6b-69a64d3f008c',
                 'mac_address': 'fa:16:3e:9c:d5:7e',
                 'name': '',
                 'network_id': network_dict['id'],
                 'status': 'ACTIVE',
                 'tenant_id': '1'}
    TEST.api_ports.add(port_dict)
    TEST.ports.add(Port(port_dict))

    router_dict = {'id': '279989f7-54bb-41d9-ba42-0d61f12fda61',
                   'name': 'router1',
                   'tenant_id': '1'}
    TEST.api_routers.add(router_dict)
    TEST.routers.add(Router(router_dict))
    router_dict = {'id': '279989f7-54bb-41d9-ba42-0d61f12fda61',
                   'name': 'router1',
                   'tenant_id': '1'}
    TEST.api_routers.add(router_dict)
    TEST.routers.add(Router(router_dict))

    #------------------------------------------------------------
    # floating IP
    # unassociated
    fip_dict = {'tenant_id': '1',
                'floating_ip_address': '172.16.88.227',
                'floating_network_id': ext_net['id'],
                'id': '9012cd70-cfae-4e46-b71e-6a409e9e0063',
                'fixed_ip_address': None,
                'port_id': None,
                'router_id': None}
    TEST.api_q_floating_ips.add(fip_dict)
    TEST.q_floating_ips.add(FloatingIp(fip_dict))

    # associated (with compute port on 1st network)
    fip_dict = {'tenant_id': '1',
                'floating_ip_address': '172.16.88.228',
                'floating_network_id': ext_net['id'],
                'id': 'a97af8f2-3149-4b97-abbd-e49ad19510f7',
                'fixed_ip_address': assoc_port['fixed_ips'][0]['ip_address'],
                'port_id': assoc_port['id'],
                'router_id': router_dict['id']}
    TEST.api_q_floating_ips.add(fip_dict)
    TEST.q_floating_ips.add(FloatingIp(fip_dict))
