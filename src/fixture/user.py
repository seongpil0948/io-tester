from dataclasses import dataclass


@dataclass
class Tester:
    uid: str
    email: str
    pw: str="0525cc"



TESTERS = {
  "shop": Tester("TZMeyFqKy3gtHvobCVfFAASyLyp2", "seongpil0948@gmail.com" ) ,
  "shop_no": Tester("Oyt9xjgkxvacgYla7eeszdW6VUY2", "junhoi90@gmail.com" ) ,
  "vendor": Tester("hqogcoikE4Z8KAlugFSTRlT6Ge13", "spchoi@gmail.com" ) ,
  "vendor_no": Tester("9BItM1hSq6b6N2J4jpbMsPtsxLs2", "testvendor@gmail.com" ) ,
  "uncle": Tester("2419092443", "inoutbox@kakao.com" ) ,
  "uncle_no": Tester("eRzv2rEXjczNLNJ4tuGUjILGxgnK2", "a@b.com" ) ,
};
