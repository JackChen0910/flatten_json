from main import JsonParser

if __name__ == '__main__':
    # result = JsonParser().parse_forward(json.loads(open('./jylb.json', 'r').read()))
    # df = pandas.DataFrame(result)
    # df.to_excel("output.xlsx")

    a = [{'a': 1, 'b': 2},
         {'x': 7,
          'c': [
              {'d': [
                  {'e': 3}
              ]},
              {'o': [
                  {'p': 4},
                  {'q': 5}
              ]
              }, {'r': 6}
          ],
          },
         {'m': 123},
         ]
    print(JsonParser().parse_forward(a))
