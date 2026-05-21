from functools import reduce


def parse_line(line):
    parts = line.strip().split()

    return {
        "filename": parts[0],
        "permission": parts[1]
    }


def analyze_permission(file_info):
    permission = file_info["permission"]
    risks = []

    # izin kontrolu
    if permission[7] == "w":
        risks.append("Diger kullanicilar dosyaya yazabilir.")

    if permission[8] == "x":
        risks.append("Diger kullanicilar dosyayi calistirabilir.")

    if permission[6] == "r":
        risks.append("Diger kullanicilar dosyayi okuyabilir.")

    return {
        "filename": file_info["filename"],
        "permission": permission,
        "risks": risks
    }


def is_risky(file_info):
    return len(file_info["risks"]) > 0


def calculate_total_risk(total, file_info):
    return total + len(file_info["risks"])


def print_report(all_files, risky_files, total_risk):
    print("DOSYA IZIN ANALIZ RAPORU")
    print("=" * 30)

    for file_info in all_files:
        print("Dosya:", file_info["filename"])
        print("Izin :", file_info["permission"])

        if is_risky(file_info):
            print("Durum: Riskli")
            print("Riskler:")

            for risk in file_info["risks"]:
                print("-", risk)
        else:
            print("Durum: Guvenli")

        print("-" * 30)

    print("Toplam dosya sayisi:", len(all_files))
    print("Riskli dosya sayisi:", len(risky_files))
    print("Toplam risk sayisi :", total_risk)


def main():
    # dosyayi oku
    with open("sample_permissions.txt", "r") as file:
        lines = file.readlines()

    # satirlari ayristir
    parsed_files = list(map(parse_line, lines))

    # izinleri analiz et
    analyzed_files = list(map(analyze_permission, parsed_files))

    # riskli dosyalari bul
    risky_files = list(filter(is_risky, analyzed_files))

    # toplam risk sayisi
    total_risk = reduce(calculate_total_risk, analyzed_files, 0)

    print_report(analyzed_files, risky_files, total_risk)


if __name__ == "__main__":
    main()