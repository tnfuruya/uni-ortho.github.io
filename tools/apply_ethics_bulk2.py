# -*- coding: utf-8 -*-
"""Second-pass ethics updates: titles, nav, feature copy, index02 stub, etc."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TITLE_SUFFIX_OLD = "札幌市琴似にある、矯正専門の歯科医院です"
TITLE_SUFFIX_NEW = "札幌市西区琴似の矯正歯科クリニックです"

FEATURE_CT_OLD = (
    '<p class="indent">当院では、2003年から<span class="red">コーンビームCT</span>と呼ばれる、X線の被爆量が少なく、高精度な顎顔面領域に特化した歯科用CTを運用しており、これは北海道の矯正専門医で、唯一当院だけが所有しております。主に<span class="red">あごの骨の三次元分析</span>（外科的矯正治療）や、<span class="red">顎関節の分析</span>、<span class="red">親しらずや埋伏歯</span>（骨の中に歯が埋まって出てこない状態の歯）の位置確認、<span class="red">耳鼻疾患の確認</span>などに利用しています。また、一般の歯科クリニックからの依頼として、近年普及してきている歯科用<span class="red">インプラント</span>（人工歯根）の骨検査なども行っています。</p>'
)
FEATURE_CT_NEW = (
    '<p class="indent">当院では、2003年から<span class="red">コーンビームCT</span>と呼ばれる、X線の被爆量が少なく、顎顔面領域に特化した歯科用CTを運用しています。主に<span class="red">あごの骨の三次元分析</span>（外科的矯正治療）や、<span class="red">顎関節の分析</span>、<span class="red">親しらずや埋伏歯</span>（骨の中に歯が埋まって出てこない状態の歯）の位置確認、<span class="red">耳鼻疾患の確認</span>などに利用しています。</p>'
)

INDEX02_BODY = """<h3><img src="./common/img/h3Header.gif" alt="見出し｜ユニからの情報" width="103" height="14" /></h3>
<h4><img src="./common/img/impression/h4Header01.gif" alt="見出し｜患者さんのご感想について" width="95" height="12" /></h4>
<p class="indent btm40">医療広告ガイドラインおよび日本矯正歯科学会ホームページ倫理審査指針に基づき、患者さまの主観に基づく体験談・感想文の掲載を非公開としました。治療内容や費用、リスク・副作用については、初診時の説明や<a href="../cost/index.html">診療の流れと治療費</a>のページ、または<a href="../contact/index.html">お問合せ</a>にてご案内いたします。</p>
"""

INDEX02_OLD_MAIN = """<!-- InstanceBeginEditable name="EditRegion02" -->
<h3><img src="./common/img/h3Header.gif" alt="見出し｜ユニからの情報" width="103" height="14" /></h3>
<h4><img src="./common/img/impression/h4Header01.gif" alt="見出し｜患者さんの感想文" width="95" height="12" /></h4>
<p class="indent btm40">当クリニックでは治療された患者様からご感想をいただいております。その中から一部をご紹介いたします。
画像をクリックするとPDFで拡大表示されます。</p>

<div class="inpBox">
<a href="./common/pdf/pdf01.pdf" target="_blank"><img src="./common/img/impression/pic01.jpg" width="250" height="340" alt="画像｜患者さんの感想文01" /></a><a href="./common/pdf/pdf03.pdf" target="_blank"><img src="./common/img/impression/pic03.jpg" width="250" height="340" alt="画像｜患者さんの感想文03" /></a>
<a href="./common/pdf/pdf04.pdf" target="_blank"><img src="./common/img/impression/pic04.jpg" width="250" height="340" alt="画像｜患者さんの感想文04" /></a>
<a href="./common/pdf/pdf05.pdf" target="_blank"><img src="./common/img/impression/pic05.jpg" width="250" height="340" alt="画像｜患者さんの感想文05" /></a><a href="./common/pdf/pdf07.pdf" target="_blank"><img src="./common/img/impression/pic07.jpg" width="250" height="340" alt="画像｜患者さんの感想文07" /></a>
<a href="./common/pdf/pdf08.pdf" target="_blank"><img src="./common/img/impression/pic08.jpg" width="250" height="340" alt="画像｜患者さんの感想文08" /></a>
<a href="./common/pdf/pdf09.pdf" target="_blank"><img src="./common/img/impression/pic09.jpg" width="250" height="340" alt="画像｜患者さんの感想文09" /></a>
<a href="./common/pdf/pdf10.pdf" target="_blank"><img src="./common/img/impression/pic10.jpg" width="250" height="340" alt="画像｜患者さんの感想文10" /></a>
<a href="./common/pdf/pdf11.pdf" target="_blank"><img src="./common/img/impression/pic11.jpg" width="250" height="340" alt="画像｜患者さんの感想文11" /></a>
<a href="./common/pdf/pdf12.pdf" target="_blank"><img src="./common/img/impression/pic12.jpg" width="250" height="340" alt="画像｜患者さんの感想文12" /></a>
<a href="./common/pdf/pdf13.pdf" target="_blank"><img src="./common/img/impression/pic13.jpg" width="250" height="340" alt="画像｜患者さんの感想文13" /></a>
<a href="./common/pdf/pdf14.pdf" target="_blank"><img src="./common/img/impression/pic14.jpg" width="250" height="340" alt="画像｜患者さんの感想文14" /></a>
<a href="./common/pdf/pdf15.pdf" target="_blank"><img src="./common/img/impression/pic15.jpg" width="250" height="340" alt="画像｜患者さんの感想文15" /></a>
<a href="./common/pdf/pdf16.pdf" target="_blank"><img src="./common/img/impression/pic16.jpg" width="250" height="340" alt="画像｜患者さんの感想文16" /></a>
<a href="./common/pdf/pdf17.pdf" target="_blank"><img src="./common/img/impression/pic17.jpg" width="250" height="340" alt="画像｜患者さんの感想文17" /></a>
</div>
<!-- InstanceEndEditable -->"""


def remove_impression_nav_lines(text: str) -> str:
    """Drop <li>…患者さんの感想文…</li> (any href)."""
    return re.sub(
        r"\s*<li><a [^>]*>患者さんの感想文</a></li>\s*\n?",
        "\n",
        text,
        flags=re.IGNORECASE,
    )


def patch_infomation_index02(path: Path) -> None:
    t = path.read_text(encoding="utf-8")
    t = t.replace(
        "<title>患者さんの感想文｜ユニからの情報｜ユニ矯正歯科クリニック｜"
        + TITLE_SUFFIX_NEW
        + "</title>",
        "<title>患者さんのご感想について｜ユニからの情報｜ユニ矯正歯科クリニック｜"
        + TITLE_SUFFIX_NEW
        + "</title>",
    )
    t = t.replace("<li>患者さんの感想文</li>", "<li>患者さんのご感想について</li>")
    t = t.replace(
        '<li><a href="./index02.html">患者さんの感想文</a></li>\n',
        "",
    )
    t = t.replace(
        INDEX02_OLD_MAIN,
        "<!-- InstanceBeginEditable name=\"EditRegion02\" -->\n"
        + INDEX02_BODY
        + "\n<!-- InstanceEndEditable -->",
    )
    path.write_text(t, encoding="utf-8")


def process(path: Path) -> bool:
    rel = str(path.relative_to(ROOT)).replace("\\", "/")
    raw = path.read_text(encoding="utf-8")
    orig = raw

    raw = raw.replace(TITLE_SUFFIX_OLD, TITLE_SUFFIX_NEW)

    if rel == "feature/index.html":
        raw = raw.replace(FEATURE_CT_OLD, FEATURE_CT_NEW)
        raw = raw.replace('alt="見出し｜見えない矯正"', 'alt="見出し｜舌側（リンガル）矯正"')
        raw = raw.replace('alt="画像｜見えない矯正イメージ"', 'alt="画像｜舌側（リンガル）矯正のイメージ"')
        raw = raw.replace('alt="見出し｜見せて魅せる矯正治療"', 'alt="見出し｜ワイヤー矯正（装置の見え方）"')
        raw = raw.replace('alt="画像｜見せて魅せる矯正治療イメージ"', 'alt="画像｜ワイヤー矯正のイメージ"')
        raw = raw.replace(">見えない矯正</a>", ">舌側（リンガル）矯正</a>")
        raw = raw.replace(">見せて魅せる矯正治療</a>", ">ワイヤー矯正について</a>")
        raw = raw.replace('alt="ボタン｜見えない矯正について詳しく見る"', 'alt="ボタン｜舌側（リンガル）矯正について詳しく見る"')
        raw = raw.replace('alt="ボタン｜見せて魅せる矯正治療について詳しく見る"', 'alt="ボタン｜ワイヤー矯正について詳しく見る"')
        # Body copy: avoid 見えない as product name
        raw = raw.replace(
            "当院では、見えない：目立たない矯正装置として、ブラケットを歯の裏側につけるリンガルブラケットを使用して治療しています。これは、「矯正をしたいけど、目立つのはいやだなあ」と矯正治療を始める勇気のなかった方におすすめの矯正歯科治療法です。",
            "当院では、目立ちにくい矯正装置として、ブラケットを歯の舌側（裏側）に装着するリンガルブラケット矯正を行っています。装置が目立ちにくいことを希望される場合の選択肢のひとつです。適応やリスクは検査・診断のうえでご説明します。",
        )
        raw = raw.replace(
            "<p class=\"indent\">今や矯正歯科治療は普及し、一般の理解も得られるようになりました。こそこそと隠れて治療したり、目立たなくしてもらうのではなく、むしろ積極的に治療していることをアピールするようになってきています。</p>\n<p class=\"indent\">当院でも、装置を止めるゴム（ブラケットとワイヤーをとめるゴム）を、下の写真のように、ピンクやグリーン、ブルーやオレンジなど、いろいろな色を使用して、ファッション感覚で楽しんでいる患者さんが増えてきています。このゴムは、通院時に交換するので、毎回いろいろな色を楽しむことができます。このコーナーでは、色のコーディネート例なども紹介しています！また、矯正治療の話題の映画や、矯正治療を経験した有名人などもご紹介いたします！</p>",
            "<p class=\"indent\">ブラケット矯正では、装置を固定するゴムの色を選ぶなど、通院ごとに外観を変えられることがあります。見た目の好みに合わせた選択は医師の指示の範囲で行います。</p>\n<p class=\"indent\">本ページでは、ワイヤー矯正における装置の見え方や装着イメージについて、写真を用いて説明しています。</p>",
        )

    if rel == "treatment/index.html":
        raw = raw.replace(
            "コーンビームCT（顎顔面に特化した最新式のCT）を導入しており、",
            "コーンビームCT（顎顔面に特化した歯科用CT）を導入しており、",
        )

    if rel == "treatment/surgery/index02.html":
        raw = raw.replace(
            '<p class="indent">手術後の術後矯正が終了し、装置がはずれ、保定期間(裏側から見えない装置で押さえて歯がためすること)に入りました。ものをかみ切ることができるようになり、発音も明瞭になりました。顔のゆがみもとれて、すてきな笑顔となりました！</p>\n',
            '<p class="indent">外科的矯正後の術後矯正を経て、保定に移行した症例の一例です（個人の感想や効果を保証するものではありません）。</p>\n',
        )

    if rel == "sitemap/index.html":
        raw = raw.replace(
            '<li><a href="../feature/index06.html">見えない矯正</a></li>',
            '<li><a href="../feature/index06.html">舌側（リンガル）矯正</a></li>',
        )
        raw = raw.replace(
            '<li><a href="../feature/index07.html">見せて魅せる矯正治療</a></li>',
            '<li><a href="../feature/index07.html">ワイヤー矯正について</a></li>',
        )
        raw = raw.replace(
            '<li><a href="../infomation/index02.html">患者さんの感想文</a></li>',
            '<li><a href="../infomation/index02.html">患者さんのご感想について</a></li>',
        )

    if rel == "link/index.html":
        raw = raw.replace(
            "<dd>私達が所属している矯正歯科専門医の集まりです。</dd>",
            "<dd>矯正歯科治療に取り組む歯科医師の学術団体です。</dd>",
        )

    if rel == "introduction/index.html":
        raw = raw.replace(
            "<li>日本矯正歯科学会専門医</li>",
            "<li>日本矯正歯科学会臨床指導医（旧専門医制度に基づく資格）</li>",
        )
        raw = raw.replace(
            "最良の治療を目指したいと考えております",
            "説明に基づく適切な治療を目指してまいります",
        )

    if rel == "infomation/ontona_etc/index20.html":
        raw = raw.replace(
            "お気軽に専門医に相談してください。",
            "お気軽に当院の歯科医師へご相談ください。",
        )

    # Global phrase replacements (safe)
    raw = raw.replace(">見えない矯正</a>", ">舌側（リンガル）矯正</a>")
    raw = raw.replace(">見せて魅せる矯正治療</a>", ">ワイヤー矯正について</a>")

    raw = remove_impression_nav_lines(raw)

    if raw != orig:
        path.write_text(raw, encoding="utf-8")
        return True
    return False


def main():
    for p in sorted(ROOT.rglob("*.html")):
        if "tools" in p.parts:
            continue
        process(p)
    patch_infomation_index02(ROOT / "infomation" / "index02.html")
    print("pass2 done")


if __name__ == "__main__":
    main()
