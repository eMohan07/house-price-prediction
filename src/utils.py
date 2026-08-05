def validate_house(sqft_living, sqft_above, sqft_basement):
    """
    Validate house dimensions.
    """
    if sqft_above + sqft_basement > sqft_living:
        return False

    return True