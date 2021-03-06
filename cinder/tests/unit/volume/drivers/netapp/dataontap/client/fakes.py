# Copyright (c) - 2015, Tom Barron.  All rights reserved.
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


from lxml import etree


GET_OPERATIONAL_NETWORK_INTERFACE_ADDRESSES_RESPONSE = etree.XML("""
    <results status="passed">
        <num-records>2</num-records>
        <attributes-list>
            <net-interface-info>
                <address>%(address1)s</address>
            </net-interface-info>
            <net-interface-info>
                <address>%(address2)s</address>
            </net-interface-info>
        </attributes-list>
    </results>
""" % {"address1": "1.2.3.4", "address2": "99.98.97.96"})

VOLUME_LIST_INFO_RESPONSE = etree.XML("""
  <results status="passed">
    <volumes>
      <volume-info>
        <name>vol0</name>
        <block-type>64_bit</block-type>
        <state>online</state>
        <size-total>1441193750528</size-total>
        <size-used>3161096192</size-used>
        <size-available>1438032654336</size-available>
        <percentage-used>0</percentage-used>
        <owning-vfiler>vfiler0</owning-vfiler>
        <containing-aggregate>aggr0</containing-aggregate>
        <space-reserve>volume</space-reserve>
        <space-reserve-enabled>true</space-reserve-enabled>
        <is-inconsistent>false</is-inconsistent>
        <is-unrecoverable>false</is-unrecoverable>
        <is-invalid>false</is-invalid>
      </volume-info>
      <volume-info>
        <name>vol1</name>
        <block-type>64_bit</block-type>
        <state>online</state>
        <size-total>1441193750528</size-total>
        <size-used>3161096192</size-used>
        <size-available>1438032654336</size-available>
        <percentage-used>0</percentage-used>
        <owning-vfiler>vfiler0</owning-vfiler>
        <containing-aggregate>aggr0</containing-aggregate>
        <space-reserve>volume</space-reserve>
        <space-reserve-enabled>true</space-reserve-enabled>
        <is-inconsistent>false</is-inconsistent>
        <is-unrecoverable>false</is-unrecoverable>
        <is-invalid>false</is-invalid>
      </volume-info>
      <volume-info>
        <name>vol2</name>
        <block-type>64_bit</block-type>
        <state>offline</state>
        <size-total>1441193750528</size-total>
        <size-used>3161096192</size-used>
        <size-available>1438032654336</size-available>
        <percentage-used>0</percentage-used>
        <owning-vfiler>vfiler0</owning-vfiler>
        <containing-aggregate>aggr0</containing-aggregate>
        <space-reserve>volume</space-reserve>
        <space-reserve-enabled>true</space-reserve-enabled>
        <is-inconsistent>false</is-inconsistent>
        <is-unrecoverable>false</is-unrecoverable>
        <is-invalid>false</is-invalid>
      </volume-info>
      <volume-info>
        <name>vol3</name>
        <block-type>64_bit</block-type>
        <state>online</state>
        <size-total>1441193750528</size-total>
        <size-used>3161096192</size-used>
        <size-available>1438032654336</size-available>
        <percentage-used>0</percentage-used>
        <owning-vfiler>vfiler0</owning-vfiler>
        <containing-aggregate>aggr0</containing-aggregate>
        <space-reserve>volume</space-reserve>
        <space-reserve-enabled>true</space-reserve-enabled>
        <is-inconsistent>false</is-inconsistent>
        <is-unrecoverable>false</is-unrecoverable>
        <is-invalid>false</is-invalid>
      </volume-info>
    </volumes>
  </results>
""")
