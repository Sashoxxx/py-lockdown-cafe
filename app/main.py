from typing import List, Union

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: Union[List[dict], dict], cafe: Cafe) -> str:
    count_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as error:
            return str(error)
        except NotWearingMaskError:
            count_masks += 1

    if count_masks > 0:
        return f"Friends should buy {count_masks} masks"
    else:
        return f"Friends can go to {cafe.name}"
