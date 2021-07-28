#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import sin, cos, sqrt, atan2, radians
import operator


# This function calculate the distance between two geographic coordinates
# https://stackoverflow.com/a/19412565/7664185 [no man is good enough to be another's master ;)] - William Morris

def haversine(lat1, lng1, lat2, lng2):
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lng1)
    lat2 = radians(lat2)
    lon2 = radians(lng2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return int(R * c)


def calculate_zone_coverage(shoppers, location):
    zone_covered = {}
    for shopper in shoppers:
        if shopper['enabled'] != True:
            continue

        # Here we loop through locations and saves the coverage
        # count of each person for each location only if the shopper
        # location is within 10 km of location.

        for location in locations:
            distance = haversine(shopper['lat'], shopper['lng'],
                                 location['lat'], location['lng'])
            if distance >= 10:
                continue

            if shopper['id'] in zone_covered:
                zone_covered[shopper['id']] += 1
            else:
                zone_covered[shopper['id']] = 1

    coverage_report = []

    # Here we loop over coverage count dictionary and calculate the
    # location coverage percentage for each shopper and returns the
    # desired result list sorted by coverage percentage.

    for key in zone_covered:
        total = len(locations)
        percentage = int(zone_covered[key] / total * 100)
        coverage_report.append({'shopper_id': key,
                               'coverage': percentage})

    return sorted(coverage_report, key=operator.itemgetter('coverage'), reverse=True)


locations = [{
    'id': 1000,
    'zip_code': '37069',
    'lat': 45.35,
    'lng': 10.84,
    }, {
    'id': 1001,
    'zip_code': '37121',
    'lat': 45.44,
    'lng': 10.99,
    }, {
    'id': 1001,
    'zip_code': '37129',
    'lat': 45.44,
    'lng': 11.00,
    }, {
    'id': 1001,
    'zip_code': '37133',
    'lat': 45.43,
    'lng': 11.02,
    }]

shoppers = [
    {
        'id': 'S1',
        'lat': 45.46,
        'lng': 11.03,
        'enabled': True,
        },
    {
        'id': 'S2',
        'lat': 45.46,
        'lng': 10.12,
        'enabled': True,
        },
    {
        'id': 'S3',
        'lat': 45.34,
        'lng': 10.81,
        'enabled': True,
        },
    {
        'id': 'S4',
        'lat': 45.76,
        'lng': 10.57,
        'enabled': True,
        },
    {
        'id': 'S5',
        'lat': 45.34,
        'lng': 10.63,
        'enabled': True,
        },
    {
        'id': 'S6',
        'lat': 45.42,
        'lng': 10.81,
        'enabled': True,
        },
    {
        'id': 'S7',
        'lat': 45.34,
        'lng': 10.94,
        'enabled': True,
        },
    ]

print(calculate_zone_coverage(shoppers, locations))
