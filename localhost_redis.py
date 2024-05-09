import redis
import json
import pandas as pd

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


def get_paper(year="all"):
    if year == "all":
        return r.smembers("papereids")
    else:
        return r.smembers(f"papereids:{year}")


def get_paper_references(eid):
    return r.lrange(f"paper:{eid}:references", 0, -1)


def get_paper_affiliations(eid):
    return r.lrange(f"paper:{eid}:affiliations", 0, -1)


def references_dataframe(year="all"):
    papers = get_paper(year)
    all_references = []
    for paper in papers:
        references = get_paper_references(paper)
        for reference in references:
            reference = json.loads(reference)
            reference["eid"] = paper
            all_references.append(reference)
    return pd.DataFrame(all_references)


def affiliations_dataframe(year="all"):
    papers = get_paper(year)
    all_affiliations = []
    for paper in papers:
        affiliations = get_paper_affiliations(paper)
        for affiliation in affiliations:
            affiliation = json.loads(affiliation)
            affiliation["eid"] = paper
            all_affiliations.append(affiliation)
    return pd.DataFrame(all_affiliations)


def get_city_aff_count(year="all"):
    aff_df = affiliations_dataframe(year)
    grouped_df = (
        aff_df.groupby("city")
        .agg({"eid": "count", "latitude": "first", "longitude": "first"})
        .reset_index()
    )
    grouped_df.columns = ["city", "count", "latitude", "longitude"]
    grouped_df = grouped_df[grouped_df["city"] != ""]

    return grouped_df
