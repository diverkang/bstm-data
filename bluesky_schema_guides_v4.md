
# BlueSky Data Pack v4 FULL — Schema & Guides
**Version:** 2025-11-05
**Compatibility:** 100% compatible with `bluesky_data_pack_v4_full.json` (313 cities).

## 1) Topology
Root JSON is a 3-level nested map:
{ Continent: { Country: { City: CityObject } } }

- Continent keys (fixed by UI): Asia, Europe, Middle East & Africa, North America, Central America, South America, Oceania
- Country and City keys are free-form strings (EN labels); UI falls back to `CityObject.ko` for Korean labels.

## 2) CityObject (Required & Optional)
Required:
- tier — one of low|mid|high|lux
- costIndex — object hotel, food, transport (relative 1.0 = mid)
- durationHint — minNights, maxNights
- priceSamples — hotelNightUSD, coffeeUSD, mealUSD, transportUSD

Recommended:
- ko, bestMonths, avoidMonths, seasons, themeWeights, tags
- mustSee, mustEat, highlightPlan, photoSpots, seasonTips
- lodgingZones, currency, keywords
- geo(lat/lng) for ICN distance banding

Optional:
- basePopularity, safetyIndex, walkability, publicTransit, visaNote, electricity, languageTips
- _continent, _country are runtime fields (UI may inject).

## 3) Validation
Use the included Draft 2020-12 JSON Schema: bluesky_schema_v4.json

### Minimal City example
{
  "tier": "mid",
  "costIndex": {"hotel": 1.0, "food": 1.0, "transport": 1.0},
  "durationHint": {"minNights": 3, "maxNights": 6},
  "priceSamples": {"hotelNightUSD": 120, "coffeeUSD": 3.5, "mealUSD": 12, "transportUSD": 2.0}
}

## 4) Field Semantics & UI Binding
- Budget: tier + costIndex steer scoring; short trips down-weight long-haul picks.
- Time: month/season filters prefer bestMonths; avoidMonths reduces weight.
- Theme: chips map to tags (hard filter) and themeWeights (soft score).
- Distance band: if geo provided, UI computes ICN distance -> flightBandKR.
- Must See/Eat: UI builds Korean Google links from list items (no inline URLs).
- Lodging mini-card: reads lodgingZones[]; Trip.com CTA built from {country} {city} {zone.name} + AWIN code.
- Currency & priceSamples: rendered in result card; mid-price emphasized.

## 5) Update Workflow
- Keep one canonical file bluesky_data_pack_v4_full.json.
- Add/update cities by editing nested {Continent -> Country -> City} nodes.
- No direct URLs in mustSee/mustEat; keep them as plain text.
- Add geo gradually for accuracy.
- Do not include South Korea (origin excluded).

## 6) Compatibility
- Extra fields are tolerated (additionalProperties: true).
- Removing required fields breaks rendering.
- New continents allowed but won’t show unless the UI has matching select options.

## 7) Trip.com CTA (AWIN) — Build
- Target: _self
- HREF pattern (pseudo): https://www.awin1.com/cread.php?...&p={encoded_tripcom_url_with_query(city_or_zone)}
- Query seed: "{country} {city} {zone.name}"

## 8) Example Node
{
  "Europe": {
    "Portugal": {
      "Porto": {
        "ko": "포르투",
        "tier": "mid",
        "costIndex": {"hotel": 1.0, "food": 0.95, "transport": 0.9},
        "priceSamples": {"hotelNightUSD": 110, "coffeeUSD": 2.8, "mealUSD": 11, "transportUSD": 1.9},
        "durationHint": {"minNights": 3, "maxNights": 6},
        "bestMonths": [4,5,9,10],
        "avoidMonths": [8],
        "seasons": ["spring","summer","fall","winter"],
        "tags": ["미식","사진","힐링"],
        "themeWeights": {"미식": 0.88, "사진": 0.84, "힐링": 0.82},
        "mustSee": ["루이스 1세 다리","리베이라","동 루이스 광장"],
        "mustEat": ["트리파스 아 모다 두 포르투","프란세지냐","포트 와인"],
        "photoSpots": ["세라 두 필라르 전망대","리베이라 강변"],
        "seasonTips": ["여름 성수기 혼잡 - 오전대 이동"],
        "lodgingZones": [
          {"name":"리베이라·강변","level":"$$$", "note":"야경·도보 이동 최적"},
          {"name":"보아비스타","level":"$$", "note":"현지 분위기·접근성"}
        ],
        "currency": {"code":"EUR", "symbol":"€"},
        "geo": {"lat": 41.1579, "lng": -8.6291 }
      }
    }
  }
}

## 9) Naming
- Country/City keys EN; localized name in ko field for city.
- Keys should avoid slashes; values can include descriptive parentheses.
