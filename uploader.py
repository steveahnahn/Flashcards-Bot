from chai_py import Metadata, package, upload_and_deploy, wait_for_deployment
from chai_py import share_bot
from chai_py.auth import set_auth

from chatbot import Bot

from chai_py.defaults import GUEST_UID, GUEST_KEY

from devkeys import keys

DEVELOPER_UID = keys[0]
DEVELOPER_KEY = keys[1]

if DEVELOPER_KEY is None or DEVELOPER_UID is None:
    raise RuntimeError("Please fetch your UID and KEY from the bottom of the Chai Developer Platform. https://chai.ml/dev")

set_auth(DEVELOPER_UID, DEVELOPER_KEY)
BOT_IMAGE_URL = "https://cutt.ly/lx0gnM9"

package(
    Metadata(
        name="Your First Bot! 🎉 🤖",
        image_url=BOT_IMAGE_URL,
        color="f1a2b3",
        description="Thank you for creating me ❤️",
        input_class=Bot,
     ),
     requirements = ["supermemo2"],
)

bot_uid = upload_and_deploy(
    "_package.zip"
)

wait_for_deployment(bot_uid)

share_bot(bot_uid)
