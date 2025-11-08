
BlueSky Trip Matcher — v6 Data Zone (Sample Pack)

Files:
- bluesky_data_pack_v6_full.json — FULL DATA PACK (sample subset).
- bluesky_guides_v6_full.json — GUIDES PACK (see/eat/do/tip).
- bstm_city_index_v6.csv — City index to extend to 300+ rows.
- bstm_builder_v6.py — Build skeleton full pack from CSV.
- bstm_validator_v6.py — Validate full pack structure.

One-by-one:
1) Extend bstm_city_index_v6.csv to 300+ rows (EN keys match UI).
2) Run builder: python3 bstm_builder_v6.py bstm_city_index_v6.csv bluesky_data_pack_v6_full.json
3) Fill real fields (themeWeights/costIndex/priceBandsUSD/monthMultipliers/bestMonths/avoidMonths).
4) Author guides in bluesky_guides_v6_full.json (see/eat/do/tip).
5) Validate: python3 bstm_validator_v6.py bluesky_data_pack_v6_full.json
6) Commit & pin SHA in HTML data-zone scripts.
