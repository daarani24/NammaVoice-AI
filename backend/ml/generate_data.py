import csv
import random

templates = {
    "pothole": {
        "high": [
            "Large pothole on {loc} causing accidents",
            "Deep pothole near {loc} damaging vehicles",
            "Dangerous pothole on {loc} injured a rider",
        ],
        "medium": [
            "Road full of potholes near {loc} after rain",
            "Growing pothole on {loc} needs attention",
        ],
        "low": [
            "Small pothole forming near {loc}",
            "Minor crack on {loc} not very deep",
        ],
    },
    "garbage": {
        "high": [
            "Huge pile of garbage rotting near {loc}",
            "Overflowing dustbin near {loc} attracting animals",
        ],
        "medium": [
            "Garbage bin overflowing near {loc} for days",
            "Trash not collected near {loc} for a week",
        ],
        "low": [
            "Small litter near {loc}",
            "Minor waste accumulation near {loc}",
        ],
    },
    "water_leak": {
        "high": [
            "Water pipe burst flooding {loc}",
            "Major water leakage wasting water near {loc}",
        ],
        "medium": [
            "Water logging near {loc} due to leak",
            "Slow leak affecting {loc} water tank",
        ],
        "low": [
            "Minor dripping from pipe joint near {loc}",
        ],
    },
    "drainage": {
        "high": [
            "Drainage completely blocked flooding {loc}",
            "Sewage overflow near {loc}",
        ],
        "medium": [
            "Slow drainage after rain near {loc}",
        ],
        "low": [
            "Minor blockage in drain near {loc}",
        ],
    },
    "streetlight": {
        "high": [
            "Entire {loc} dark at night no lights working",
            "Broken streetlight pole leaning dangerously near {loc}",
        ],
        "medium": [
            "Streetlight not working near {loc} for weeks",
        ],
        "low": [
            "Streetlight flickering occasionally near {loc}",
        ],
    },
    "sanitation": {
        "high": [
            "Public toilet near {loc} extremely unhygienic",
        ],
        "medium": [
            "Foul smell coming from restroom near {loc}",
        ],
        "low": [
            "Minor cleanliness issue in toilet near {loc}",
        ],
    },
    "illegal_dumping": {
        "high": [
            "Industrial waste dumped near {loc}",
        ],
        "medium": [
            "Someone dumping household waste near {loc}",
        ],
        "low": [
            "Small pile of leaves dumped near {loc}",
        ],
    },
    "property_damage": {
        "high": [
            "Public wall collapsed blocking {loc}",
        ],
        "medium": [
            "Vandalized public property near {loc}",
        ],
        "low": [
            "Minor scratch on signage near {loc}",
        ],
    },
}

locations = [
    "main road", "bus stop", "market area", "school gate", "park entrance",
    "residential lane", "community hall", "railway crossing", "bridge",
    "shopping complex", "temple street", "hospital road",
]

def generate(rows_per_class=50, output_path="ml/data/complaints_dataset.csv"):
    rows = []
    for category, priorities in templates.items():
        for priority, sentences in priorities.items():
            for _ in range(rows_per_class):
                sentence = random.choice(sentences)
                loc = random.choice(locations)
                text = sentence.format(loc=loc)
                rows.append([text, category, priority])

    random.shuffle(rows)

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["text", "category", "priority"])
        writer.writerows(rows)

    print(f"Generated {len(rows)} rows into {output_path}")

if __name__ == "__main__":
    generate(rows_per_class=50)