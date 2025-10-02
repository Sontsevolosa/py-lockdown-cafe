from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str | None:
    problems_with_vaccination_count = 0
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            problems_with_vaccination_count += 1
            print("You should be vaccinated!")
        except NotWearingMaskError:
            print("You should wear a mask!")
            masks_to_buy += 1

    if problems_with_vaccination_count:
        return "All friends should be vaccinated"

    if problems_with_vaccination_count == 0 and masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    if problems_with_vaccination_count == 0 and masks_to_buy == 0:
        return f"Friends can go to {cafe.name}"
