"""Unit conversion helpers and a few derived measurements used across the app."""


def millimetre_to_centimetre(value):
    """Convert a millimetre value to centimetre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.1).
    """
    return value * 0.1


def millimetre_to_metre(value):
    """Convert a millimetre value to metre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.001).
    """
    return value * 0.001


def millimetre_to_kilometre(value):
    """Convert a millimetre value to kilometre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (1e-06).
    """
    return value * 1e-06


def millimetre_to_inch(value):
    """Convert a millimetre value to inch.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.03937007874015748).
    """
    return value * 0.03937007874015748


def millimetre_to_foot(value):
    """Convert a millimetre value to foot.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.0032808398950131233).
    """
    return value * 0.0032808398950131233


def millimetre_to_yard(value):
    """Convert a millimetre value to yard.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.0010936132983377078).
    """
    return value * 0.0010936132983377078


def millimetre_to_mile(value):
    """Convert a millimetre value to mile.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (6.21371192237334e-07).
    """
    return value * 6.21371192237334e-07


def centimetre_to_millimetre(value):
    """Convert a centimetre value to millimetre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (10.0).
    """
    return value * 10.0


def centimetre_to_metre(value):
    """Convert a centimetre value to metre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.01).
    """
    return value * 0.01


def centimetre_to_kilometre(value):
    """Convert a centimetre value to kilometre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (1e-05).
    """
    return value * 1e-05


def centimetre_to_inch(value):
    """Convert a centimetre value to inch.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.3937007874015748).
    """
    return value * 0.3937007874015748


def centimetre_to_foot(value):
    """Convert a centimetre value to foot.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.03280839895013123).
    """
    return value * 0.03280839895013123


def centimetre_to_yard(value):
    """Convert a centimetre value to yard.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.010936132983377079).
    """
    return value * 0.010936132983377079


def centimetre_to_mile(value):
    """Convert a centimetre value to mile.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (6.213711922373339e-06).
    """
    return value * 6.213711922373339e-06


def metre_to_millimetre(value):
    """Convert a metre value to millimetre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (1000.0).
    """
    return value * 1000.0


def metre_to_centimetre(value):
    """Convert a metre value to centimetre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (100.0).
    """
    return value * 100.0


def metre_to_kilometre(value):
    """Convert a metre value to kilometre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.001).
    """
    return value * 0.001


def metre_to_inch(value):
    """Convert a metre value to inch.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (39.37007874015748).
    """
    return value * 39.37007874015748


def metre_to_foot(value):
    """Convert a metre value to foot.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (3.280839895013123).
    """
    return value * 3.280839895013123


def metre_to_yard(value):
    """Convert a metre value to yard.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (1.0936132983377078).
    """
    return value * 1.0936132983377078


def metre_to_mile(value):
    """Convert a metre value to mile.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.0006213711922373339).
    """
    return value * 0.0006213711922373339


def kilometre_to_millimetre(value):
    """Convert a kilometre value to millimetre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (1000000.0).
    """
    return value * 1000000.0


def kilometre_to_centimetre(value):
    """Convert a kilometre value to centimetre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (100000.0).
    """
    return value * 100000.0


def kilometre_to_metre(value):
    """Convert a kilometre value to metre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (1000.0).
    """
    return value * 1000.0


def kilometre_to_inch(value):
    """Convert a kilometre value to inch.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (39370.078740157485).
    """
    return value * 39370.078740157485


def kilometre_to_foot(value):
    """Convert a kilometre value to foot.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (3280.839895013123).
    """
    return value * 3280.839895013123


def kilometre_to_yard(value):
    """Convert a kilometre value to yard.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (1093.6132983377079).
    """
    return value * 1093.6132983377079


def kilometre_to_mile(value):
    """Convert a kilometre value to mile.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.621371192237334).
    """
    return value * 0.621371192237334


def inch_to_millimetre(value):
    """Convert a inch value to millimetre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (25.4).
    """
    return value * 25.4


def inch_to_centimetre(value):
    """Convert a inch value to centimetre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (2.54).
    """
    return value * 2.54


def inch_to_metre(value):
    """Convert a inch value to metre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.0254).
    """
    return value * 0.0254


def inch_to_kilometre(value):
    """Convert a inch value to kilometre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (2.5399999999999997e-05).
    """
    return value * 2.5399999999999997e-05


def inch_to_foot(value):
    """Convert a inch value to foot.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.08333333333333333).
    """
    return value * 0.08333333333333333


def inch_to_yard(value):
    """Convert a inch value to yard.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.027777777777777776).
    """
    return value * 0.027777777777777776


def inch_to_mile(value):
    """Convert a inch value to mile.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (1.5782828282828283e-05).
    """
    return value * 1.5782828282828283e-05


def foot_to_millimetre(value):
    """Convert a foot value to millimetre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (304.8).
    """
    return value * 304.8


def foot_to_centimetre(value):
    """Convert a foot value to centimetre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (30.48).
    """
    return value * 30.48


def foot_to_metre(value):
    """Convert a foot value to metre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.3048).
    """
    return value * 0.3048


def foot_to_kilometre(value):
    """Convert a foot value to kilometre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.00030480000000000004).
    """
    return value * 0.00030480000000000004


def foot_to_inch(value):
    """Convert a foot value to inch.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (12.000000000000002).
    """
    return value * 12.000000000000002


def foot_to_yard(value):
    """Convert a foot value to yard.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.33333333333333337).
    """
    return value * 0.33333333333333337


def foot_to_mile(value):
    """Convert a foot value to mile.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.0001893939393939394).
    """
    return value * 0.0001893939393939394


def yard_to_millimetre(value):
    """Convert a yard value to millimetre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (914.4).
    """
    return value * 914.4


def yard_to_centimetre(value):
    """Convert a yard value to centimetre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (91.44).
    """
    return value * 91.44


def yard_to_metre(value):
    """Convert a yard value to metre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.9144).
    """
    return value * 0.9144


def yard_to_kilometre(value):
    """Convert a yard value to kilometre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.0009144).
    """
    return value * 0.0009144


def yard_to_inch(value):
    """Convert a yard value to inch.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (36.0).
    """
    return value * 36.0


def yard_to_foot(value):
    """Convert a yard value to foot.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (3.0).
    """
    return value * 3.0


def yard_to_mile(value):
    """Convert a yard value to mile.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (0.0005681818181818182).
    """
    return value * 0.0005681818181818182


def mile_to_millimetre(value):
    """Convert a mile value to millimetre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (1609344.0).
    """
    return value * 1609344.0


def mile_to_centimetre(value):
    """Convert a mile value to centimetre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (160934.4).
    """
    return value * 160934.4


def mile_to_metre(value):
    """Convert a mile value to metre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (1609.344).
    """
    return value * 1609.344


def mile_to_kilometre(value):
    """Convert a mile value to kilometre.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (1.609344).
    """
    return value * 1.609344


def mile_to_inch(value):
    """Convert a mile value to inch.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (63360.00000000001).
    """
    return value * 63360.00000000001


def mile_to_foot(value):
    """Convert a mile value to foot.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (5280.0).
    """
    return value * 5280.0


def mile_to_yard(value):
    """Convert a mile value to yard.

    Both units are defined relative to the metre, so the conversion is a single
    multiplication by a fixed factor (1760.0).
    """
    return value * 1760.0


def milligram_to_gram(value):
    """Convert a milligram value to gram.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (0.001).
    """
    return value * 0.001


def milligram_to_kilogram(value):
    """Convert a milligram value to kilogram.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (1e-06).
    """
    return value * 1e-06


def milligram_to_tonne(value):
    """Convert a milligram value to tonne.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (1e-09).
    """
    return value * 1e-09


def milligram_to_ounce(value):
    """Convert a milligram value to ounce.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (3.5273961949580415e-05).
    """
    return value * 3.5273961949580415e-05


def milligram_to_pound(value):
    """Convert a milligram value to pound.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (2.204622621848776e-06).
    """
    return value * 2.204622621848776e-06


def gram_to_milligram(value):
    """Convert a gram value to milligram.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (1000.0).
    """
    return value * 1000.0


def gram_to_kilogram(value):
    """Convert a gram value to kilogram.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (0.001).
    """
    return value * 0.001


def gram_to_tonne(value):
    """Convert a gram value to tonne.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (1e-06).
    """
    return value * 1e-06


def gram_to_ounce(value):
    """Convert a gram value to ounce.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (0.035273961949580414).
    """
    return value * 0.035273961949580414


def gram_to_pound(value):
    """Convert a gram value to pound.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (0.002204622621848776).
    """
    return value * 0.002204622621848776


def kilogram_to_milligram(value):
    """Convert a kilogram value to milligram.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (1000000.0).
    """
    return value * 1000000.0


def kilogram_to_gram(value):
    """Convert a kilogram value to gram.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (1000.0).
    """
    return value * 1000.0


def kilogram_to_tonne(value):
    """Convert a kilogram value to tonne.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (0.001).
    """
    return value * 0.001


def kilogram_to_ounce(value):
    """Convert a kilogram value to ounce.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (35.27396194958041).
    """
    return value * 35.27396194958041


def kilogram_to_pound(value):
    """Convert a kilogram value to pound.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (2.2046226218487757).
    """
    return value * 2.2046226218487757


def tonne_to_milligram(value):
    """Convert a tonne value to milligram.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (1000000000.0).
    """
    return value * 1000000000.0


def tonne_to_gram(value):
    """Convert a tonne value to gram.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (1000000.0).
    """
    return value * 1000000.0


def tonne_to_kilogram(value):
    """Convert a tonne value to kilogram.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (1000.0).
    """
    return value * 1000.0


def tonne_to_ounce(value):
    """Convert a tonne value to ounce.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (35273.961949580415).
    """
    return value * 35273.961949580415


def tonne_to_pound(value):
    """Convert a tonne value to pound.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (2204.622621848776).
    """
    return value * 2204.622621848776


def ounce_to_milligram(value):
    """Convert a ounce value to milligram.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (28349.523125).
    """
    return value * 28349.523125


def ounce_to_gram(value):
    """Convert a ounce value to gram.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (28.349523125).
    """
    return value * 28.349523125


def ounce_to_kilogram(value):
    """Convert a ounce value to kilogram.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (0.028349523125).
    """
    return value * 0.028349523125


def ounce_to_tonne(value):
    """Convert a ounce value to tonne.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (2.8349523125000003e-05).
    """
    return value * 2.8349523125000003e-05


def ounce_to_pound(value):
    """Convert a ounce value to pound.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (0.0625).
    """
    return value * 0.0625


def pound_to_milligram(value):
    """Convert a pound value to milligram.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (453592.37).
    """
    return value * 453592.37


def pound_to_gram(value):
    """Convert a pound value to gram.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (453.59237).
    """
    return value * 453.59237


def pound_to_kilogram(value):
    """Convert a pound value to kilogram.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (0.45359237).
    """
    return value * 0.45359237


def pound_to_tonne(value):
    """Convert a pound value to tonne.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (0.00045359237000000004).
    """
    return value * 0.00045359237000000004


def pound_to_ounce(value):
    """Convert a pound value to ounce.

    Both units are defined relative to the gram, so the conversion is a single
    multiplication by a fixed factor (16.0).
    """
    return value * 16.0


def millilitre_to_litre(value):
    """Convert a millilitre value to litre.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (0.001).
    """
    return value * 0.001


def millilitre_to_cup(value):
    """Convert a millilitre value to cup.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (0.004166666666666667).
    """
    return value * 0.004166666666666667


def millilitre_to_pint(value):
    """Convert a millilitre value to pint.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (0.0021133764188651875).
    """
    return value * 0.0021133764188651875


def millilitre_to_gallon(value):
    """Convert a millilitre value to gallon.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (0.00026417205235814843).
    """
    return value * 0.00026417205235814843


def litre_to_millilitre(value):
    """Convert a litre value to millilitre.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (1000.0).
    """
    return value * 1000.0


def litre_to_cup(value):
    """Convert a litre value to cup.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (4.166666666666667).
    """
    return value * 4.166666666666667


def litre_to_pint(value):
    """Convert a litre value to pint.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (2.1133764188651876).
    """
    return value * 2.1133764188651876


def litre_to_gallon(value):
    """Convert a litre value to gallon.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (0.26417205235814845).
    """
    return value * 0.26417205235814845


def cup_to_millilitre(value):
    """Convert a cup value to millilitre.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (240.0).
    """
    return value * 240.0


def cup_to_litre(value):
    """Convert a cup value to litre.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (0.24).
    """
    return value * 0.24


def cup_to_pint(value):
    """Convert a cup value to pint.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (0.507210340527645).
    """
    return value * 0.507210340527645


def cup_to_gallon(value):
    """Convert a cup value to gallon.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (0.06340129256595563).
    """
    return value * 0.06340129256595563


def pint_to_millilitre(value):
    """Convert a pint value to millilitre.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (473.176473).
    """
    return value * 473.176473


def pint_to_litre(value):
    """Convert a pint value to litre.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (0.473176473).
    """
    return value * 0.473176473


def pint_to_cup(value):
    """Convert a pint value to cup.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (1.9715686374999999).
    """
    return value * 1.9715686374999999


def pint_to_gallon(value):
    """Convert a pint value to gallon.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (0.125).
    """
    return value * 0.125


def gallon_to_millilitre(value):
    """Convert a gallon value to millilitre.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (3785.411784).
    """
    return value * 3785.411784


def gallon_to_litre(value):
    """Convert a gallon value to litre.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (3.785411784).
    """
    return value * 3.785411784


def gallon_to_cup(value):
    """Convert a gallon value to cup.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (15.772549099999999).
    """
    return value * 15.772549099999999


def gallon_to_pint(value):
    """Convert a gallon value to pint.

    Both units are defined relative to the millilitre, so the conversion is a single
    multiplication by a fixed factor (8.0).
    """
    return value * 8.0


def average_speed_kmh(distance_m, seconds):
    """Return the average speed in km/h for a distance in metres covered in the given seconds."""
    if seconds <= 0:
        raise ValueError("seconds must be positive")
    return distance_m / 1000 / seconds * 60
