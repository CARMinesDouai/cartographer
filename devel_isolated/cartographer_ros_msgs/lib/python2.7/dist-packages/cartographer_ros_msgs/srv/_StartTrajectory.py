# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cartographer_ros_msgs/StartTrajectoryRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import cartographer_ros_msgs.msg

class StartTrajectoryRequest(genpy.Message):
  _md5sum = "2fbdca45b91af2953d6ce571d83e0ab6"
  _type = "cartographer_ros_msgs/StartTrajectoryRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """













cartographer_ros_msgs/TrajectoryOptions options
cartographer_ros_msgs/SensorTopics topics

================================================================================
MSG: cartographer_ros_msgs/TrajectoryOptions
# Copyright 2016 The Cartographer Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

string tracking_frame
string published_frame
string odom_frame
bool provide_odom_frame
bool use_odometry
int32 num_laser_scans
int32 num_multi_echo_laser_scans
int32 num_subdivisions_per_laser_scan
int32 num_point_clouds

# This is a binary-encoded
# 'cartographer.mapping.proto.TrajectoryBuilderOptions' proto.
string trajectory_builder_options_proto

================================================================================
MSG: cartographer_ros_msgs/SensorTopics
# Copyright 2016 The Cartographer Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

string laser_scan_topic
string multi_echo_laser_scan_topic
string point_cloud2_topic
string imu_topic
string odometry_topic
"""
  __slots__ = ['options','topics']
  _slot_types = ['cartographer_ros_msgs/TrajectoryOptions','cartographer_ros_msgs/SensorTopics']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       options,topics

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(StartTrajectoryRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.options is None:
        self.options = cartographer_ros_msgs.msg.TrajectoryOptions()
      if self.topics is None:
        self.topics = cartographer_ros_msgs.msg.SensorTopics()
    else:
      self.options = cartographer_ros_msgs.msg.TrajectoryOptions()
      self.topics = cartographer_ros_msgs.msg.SensorTopics()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.options.tracking_frame
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.options.published_frame
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.options.odom_frame
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2B4i().pack(_x.options.provide_odom_frame, _x.options.use_odometry, _x.options.num_laser_scans, _x.options.num_multi_echo_laser_scans, _x.options.num_subdivisions_per_laser_scan, _x.options.num_point_clouds))
      _x = self.options.trajectory_builder_options_proto
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.topics.laser_scan_topic
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.topics.multi_echo_laser_scan_topic
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.topics.point_cloud2_topic
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.topics.imu_topic
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.topics.odometry_topic
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.options is None:
        self.options = cartographer_ros_msgs.msg.TrajectoryOptions()
      if self.topics is None:
        self.topics = cartographer_ros_msgs.msg.SensorTopics()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.options.tracking_frame = str[start:end].decode('utf-8')
      else:
        self.options.tracking_frame = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.options.published_frame = str[start:end].decode('utf-8')
      else:
        self.options.published_frame = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.options.odom_frame = str[start:end].decode('utf-8')
      else:
        self.options.odom_frame = str[start:end]
      _x = self
      start = end
      end += 18
      (_x.options.provide_odom_frame, _x.options.use_odometry, _x.options.num_laser_scans, _x.options.num_multi_echo_laser_scans, _x.options.num_subdivisions_per_laser_scan, _x.options.num_point_clouds,) = _get_struct_2B4i().unpack(str[start:end])
      self.options.provide_odom_frame = bool(self.options.provide_odom_frame)
      self.options.use_odometry = bool(self.options.use_odometry)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.options.trajectory_builder_options_proto = str[start:end].decode('utf-8')
      else:
        self.options.trajectory_builder_options_proto = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topics.laser_scan_topic = str[start:end].decode('utf-8')
      else:
        self.topics.laser_scan_topic = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topics.multi_echo_laser_scan_topic = str[start:end].decode('utf-8')
      else:
        self.topics.multi_echo_laser_scan_topic = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topics.point_cloud2_topic = str[start:end].decode('utf-8')
      else:
        self.topics.point_cloud2_topic = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topics.imu_topic = str[start:end].decode('utf-8')
      else:
        self.topics.imu_topic = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topics.odometry_topic = str[start:end].decode('utf-8')
      else:
        self.topics.odometry_topic = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.options.tracking_frame
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.options.published_frame
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.options.odom_frame
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2B4i().pack(_x.options.provide_odom_frame, _x.options.use_odometry, _x.options.num_laser_scans, _x.options.num_multi_echo_laser_scans, _x.options.num_subdivisions_per_laser_scan, _x.options.num_point_clouds))
      _x = self.options.trajectory_builder_options_proto
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.topics.laser_scan_topic
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.topics.multi_echo_laser_scan_topic
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.topics.point_cloud2_topic
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.topics.imu_topic
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.topics.odometry_topic
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.options is None:
        self.options = cartographer_ros_msgs.msg.TrajectoryOptions()
      if self.topics is None:
        self.topics = cartographer_ros_msgs.msg.SensorTopics()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.options.tracking_frame = str[start:end].decode('utf-8')
      else:
        self.options.tracking_frame = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.options.published_frame = str[start:end].decode('utf-8')
      else:
        self.options.published_frame = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.options.odom_frame = str[start:end].decode('utf-8')
      else:
        self.options.odom_frame = str[start:end]
      _x = self
      start = end
      end += 18
      (_x.options.provide_odom_frame, _x.options.use_odometry, _x.options.num_laser_scans, _x.options.num_multi_echo_laser_scans, _x.options.num_subdivisions_per_laser_scan, _x.options.num_point_clouds,) = _get_struct_2B4i().unpack(str[start:end])
      self.options.provide_odom_frame = bool(self.options.provide_odom_frame)
      self.options.use_odometry = bool(self.options.use_odometry)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.options.trajectory_builder_options_proto = str[start:end].decode('utf-8')
      else:
        self.options.trajectory_builder_options_proto = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topics.laser_scan_topic = str[start:end].decode('utf-8')
      else:
        self.topics.laser_scan_topic = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topics.multi_echo_laser_scan_topic = str[start:end].decode('utf-8')
      else:
        self.topics.multi_echo_laser_scan_topic = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topics.point_cloud2_topic = str[start:end].decode('utf-8')
      else:
        self.topics.point_cloud2_topic = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topics.imu_topic = str[start:end].decode('utf-8')
      else:
        self.topics.imu_topic = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topics.odometry_topic = str[start:end].decode('utf-8')
      else:
        self.topics.odometry_topic = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2B4i = None
def _get_struct_2B4i():
    global _struct_2B4i
    if _struct_2B4i is None:
        _struct_2B4i = struct.Struct("<2B4i")
    return _struct_2B4i
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cartographer_ros_msgs/StartTrajectoryResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class StartTrajectoryResponse(genpy.Message):
  _md5sum = "6e190c4be941828bcd09ea05053f4bb5"
  _type = "cartographer_ros_msgs/StartTrajectoryResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 trajectory_id

"""
  __slots__ = ['trajectory_id']
  _slot_types = ['int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       trajectory_id

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(StartTrajectoryResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.trajectory_id is None:
        self.trajectory_id = 0
    else:
      self.trajectory_id = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_get_struct_i().pack(self.trajectory_id))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (self.trajectory_id,) = _get_struct_i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_get_struct_i().pack(self.trajectory_id))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (self.trajectory_id,) = _get_struct_i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
class StartTrajectory(object):
  _type          = 'cartographer_ros_msgs/StartTrajectory'
  _md5sum = '59596f1f9d243bf63cb86427d288e2e8'
  _request_class  = StartTrajectoryRequest
  _response_class = StartTrajectoryResponse
