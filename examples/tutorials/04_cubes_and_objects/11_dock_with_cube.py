#!/usr/bin/env python3

# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Tell Cozmo to drive up to a cube that he sees placed in front of him

This is a test / example usage of the robot.dock_with_cube call which creates a
DockWithCube action, that can be used to drive up to a light cube in a position
that will allow for lifting.
'''

import asyncio
import cozmo

async def dock_with_cube_test(robot: cozmo.robot.Robot):
    '''The core of the dock with cube test program'''

    # Wait for a cube
    cube = await robot.world.wait_for_observed_light_cube()
    ''' Tell cozmo to move to the cube and position himself so that it will be easy to pick up.
      num_retries allows us to specify that he can retry the action if something interrupts the process or if it fails,
      this will increase the reliability of cozmo successfully docking with the cube.
    '''
    await robot.dock_with_cube( cube, num_retries=2 ).wait_for_completed()

cozmo.run_program(dock_with_cube_test)
