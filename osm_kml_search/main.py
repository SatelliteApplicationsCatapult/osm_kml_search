import fiona
import geopandas as gpd
import overpy

import argparse


def get_arg_parser():
    result = argparse.ArgumentParser()
    result.add_argument("--kml", dest="kml", type=str, help="kml path")
    result.add_argument("--features", dest="features", action='append', type=str, help="feature types to query for")
    return result


def read_kml(path):
    # enable kml support in fiona as it's not on by default
    fiona.drvsupport.supported_drivers['KML'] = 'rw'
    df = gpd.read_file(path, driver='KML')
    return df


def elem_to_feature(elem):
    return {
        "geometry": {
                "type": "Polygon",
                "coordinates": [[[d.lon, d.lat] for d in elem.get_nodes(resolve_missing=True)]]
        },
        "properties": {
            "way_id": elem.id,
        },
    }


def run(args):
    kml_df = read_kml(args.kml)
    # TODO: handle more than one kml polygon
    bbox = f"{kml_df.total_bounds[1]}, {kml_df.total_bounds[0]}, {kml_df.total_bounds[3]}, {kml_df.total_bounds[2]}"
    query = "("
    for f in args.features:
        query = f"{query}way[{f}]({bbox});"

    query = f"{query});out geom;"
    # print(query)

    api = overpy.Overpass()
    result = api.query(query)

    if len(result.ways):
        features = [elem_to_feature(elem) for elem in result.ways]

        result_df = gpd.GeoDataFrame.from_features(features, crs=4326)

        overlapping = result_df.sjoin(kml_df)
        print(len(overlapping))
    else:
        print("0")


if __name__ == '__main__':
    parser = get_arg_parser()
    args = parser.parse_args()

    run(args)
