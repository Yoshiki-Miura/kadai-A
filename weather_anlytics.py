def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    temperature = 0
    oosaka_station = []
    fukuoka_temperature = 0

    for i in range(len(weather_information)):
        temperature += weather_information[i]["temperature"]
        if (weather_information[i]["prefecture"] == "大阪府"):
            oosaka_station.append(weather_information[i]["station"])
        if (weather_information[i]["prefecture"] == "福岡県"):
            fukuoka_temperature += weather_information[i]["temperature"]
    temperature /= len(weather_information)
    fukuoka_temperature /= 2

    print(temperature)

    for i in range(len(oosaka_station)):
        if i == 0:
            print("\'" + oosaka_station[i] + ",", end="")
        elif i == len(oosaka_station) - 1:
            print(oosaka_station[i] + "\'")
        else:
            print(oosaka_station[i] + ",", end="")

    print(fukuoka_temperature)


if __name__ == '__main__':
    main()
