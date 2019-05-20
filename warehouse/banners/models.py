# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from sqlalchemy import Boolean, CheckConstraint, Column, Enum, Integer, Text, sql

from warehouse import db
from warehouse.utils.attrs import make_repr


class Banner(db.Model):

    __tablename__ = "banners"
    __repr__ = make_repr("banner")

    icon = Column(Text, nullable=True)
    message = Column(Text, nullable=False)
    call_to_action = Column(Text, nullable=True)
    link = Column(Text, nullable=True)
    sytle = Column(
        Enum("none", "success", "warning", "danger", name="banner_style"),
        server_default="none",
        nullable=False,
    )
