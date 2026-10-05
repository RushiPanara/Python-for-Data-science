VALIDATION_RULES = {

    "age" : {
        "min" : 0,
        "max" : 120
    },

    "salary" : {
        "min" : 0
    },

    "rating" : {
        "min": 1,
        "max": 5
    },

    "city": {
        "allowed_values": [

            "Vadodara",
            "Ahmedabad",
            "Surat",
            "Rajkot"
        ]
    }
}