# -*- coding: utf-8 -*-
"""Q&A, treatment overview, case-photo footers."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CASE_FOOTER = (
    '<p class="indent" style="font-size:0.85em;color:#444;">'
    "※治療前後の写真は、日本矯正歯科学会ホームページ倫理審査指針に基づき、"
    "本ページの本文で主訴・病態の概要・初診時年齢・抜歯の有無・使用装置の概要を併記しています。"
    "治療期間・費用の目安、起こり得るリスク・副作用の詳細は、診療時の書面説明および"
    '<a href="../../cost/index.html">診療の流れと治療費</a>をあわせてご確認ください。効果には個人差があります。</p>'
)


def patch_infomation_index(path: Path) -> str:
    t = path.read_text(encoding="utf-8")
    t = t.replace(
        '<li><a href="#q04">Q4.医療費控除の適応になりますか？</a></li>',
        '<li><a href="#q04">Q4.医療費控除の適用になりますか？</a></li>',
    )
    t = t.replace(
        '<h5 id="q04">医療費控除の適応になりますか？</h5>',
        '<h5 id="q04">医療費控除の適用になりますか？</h5>',
    )
    old_q1 = (
        '<p class="indent ans">お口の中に装置を入れたときには、若干の違和感があります。矯正治療の痛みは、もちろん耐えられないものではありません。また、歯を動かす時に、痛みが生じる事があります。しかし、この痛みは通常の虫歯による痛みと違い、普段生活している時にはあまり自覚することはなく、硬いものを噛んだ後などに、違和感や痛みを感じます。また、治療後、3日程度で治まることが多く、矯正治療中ずっと痛みが続くことはないので、心配ありません。しかし、痛みに関しては個人差が大きく、必要に応じて当院では痛み止めのお薬を提供しております。矯正治療を始めて、ほとんど痛みを感じない方も大勢います。その方たちは矯正治療は痛くないということを他人に伝えるということをしません。逆に少しでも痛みを感じた患者さんは、痛いということをみなさんに話すという傾向があるようです。そのため、痛みに関するオーバーな話が飛び交い、ますます不安になってしまう人がいます。</p>\n'
        '<p class="indent">今では、矯正治療の技術が向上し、より優しい力で歯を動かすことができるようになり、快適な治療が行われるようになりました。</p>'
    )
    new_q1 = (
        '<p class="indent ans">お口の中に装置を入れたときには、違和感を感じることがあります。歯を動かす加力の直後には、痛みや違和感が出ることがあり、個人差が大きいです。多くの場合は数日以内に軽減しますが、続く場合は調整内容の見直しや鎮痛薬の使用など、診療時にご相談ください。痛みの感じ方は症例・時期によって異なり、他者の体験談と一致するとは限りません。</p>\n'
        '<p class="indent">装置や材料の改良により、歯への負担を抑えつつ治療を進める工夫が進められていますが、無痛を保証するものではありません。</p>'
    )
    t = t.replace(old_q1, new_q1)

    old_q2 = (
        '<p class="indent ans">どんどん楽しんで下さい。スポーツガードというボクサーのマウスピースのようなもので、お口の中を保護することができます。当院の患者さんは、柔道、カラテ、野球、サッカー、バスケットボール等など実際に矯正治療中も楽しんでいますよ！</p>\n'
        '<p class="indent">また、キム・ヨナやシャラポアのように、矯正治療が終って噛み合わせが改善されると、力やバランスが向上し、より能力を発揮できるようになるようですよ！</p>'
    )
    new_q2 = (
        '<p class="indent ans">接触の多い運動では、マウスガード（スポーツガード）などで口腔内を保護することが推奨されることがあります。装着の可否やタイミングは、競技の種類や装置の状態により異なるため、診療時にご相談ください。</p>\n'
        '<p class="indent">矯正治療は咬み合わせや顎運動に関わるため、運動中のトラブルを防ぐための注意事項についても、必要に応じてお伝えします。</p>'
    )
    t = t.replace(old_q2, new_q2)

    old_q8a = (
        "この治療により、噛み合わせの長期的な安定性が得られ、顔貌の調和が良くなり、かつ患者さんの満足度も得られる場合も数多くあります。"
    )
    new_q8a = (
        "この治療により、噛み合わせの改善や顔貌のバランス調整が期待される場合がありますが、効果には個人差があります。"
    )
    t = t.replace(old_q8a, new_q8a)

    old_q8b = (
        '<p class="indent">このような外科的矯正治療を受けられた患者さんの話を聞いてみますと、「今まで噛めないものが噛めるようなって、食事が楽しくなった！」とか「噛むことがこんなに楽なことだとは思わなかった」との意見はもちろん、「長年気にしていた自分のコンプレックスがなくなって人生が変わったような気がする」等の意見も多くあります。</p>\n'
    )
    new_q8b = (
        '<p class="indent">外科的矯正治療には、出血・感染・神経障害・骨癒合不全・審美面の想定外の変化などのリスクが伴います。手術の必要性・手術方法・予想される改善と限界については、口腔外科医および矯正歯科医による検査・説明とインフォームドコンセントに基づき決定します。</p>\n'
    )
    t = t.replace(old_q8b, new_q8b)

    old_q8c = (
        '<p class="indent">たしかに、顎を切る手術にはリスクを伴いますが、歯並びがきれいで、しっかり物が噛めて、そして顔のバランスが良くなるというメリットがあります。本当に手術が必要かどうかは、専門的な知識を持つ矯正歯科医師や口腔外科医師による検査と分析を行うことが必要です。当院では、CTやそれを利用した三次元シミュレーションを用いて、手術後のお顔のバランスの改善度の予想もお見せすることができます。まずはお気軽にご相談ください。</p>'
    )
    new_q8c = (
        '<p class="indent">顎骨切り手術の適応・術式・術後の経過は個人差があります。当院ではCTや三次元シミュレーション等を用いた検査・説明を行います。治療方針については、矯正歯科および口腔外科の診察を踏まえてご判断ください。</p>'
    )
    t = t.replace(old_q8c, new_q8c)

    path.write_text(t, encoding="utf-8")
    return "infomation/index.html"


def patch_treatment_index(path: Path) -> str:
    t = path.read_text(encoding="utf-8")
    t = t.replace(
        "たとえば、受け口の患者さん（反対咬合）では下あごの骨が成長しすぎたり（例えばアントニオ猪木）、上あごの骨の成長が少なすぎたりします。逆に、出っ歯の患者さん（上顎前突）には下あごの成長が小さすぎたりすることがあります（アンガールズの山根）。",
        "たとえば、受け口の患者さん（反対咬合）では下顎骨が相対的に大きく、上顎骨の成長が乏しいことがあります。逆に、出っ歯の患者さん（上顎前突）では下顎の前方成長が相対的に小さいことがあります。",
    )
    t = t.replace(
        "審美ブラケットや歯の裏側につけるリンガルブラケット（舌側矯正）、インビザライン（マウスピース矯正）を行っております。",
        "審美ブラケットや舌側（リンガル）ブラケット、マウスピース型矯正装置（アライナー型）などの治療選択肢については、症例に応じてご説明します。",
    )
    t = t.replace(
        "で治療をしております（現在までに約340人を治療しています）。",
        "で治療を行っております。",
    )
    notice = (
        '<p class="indent" style="font-size:0.9em;color:#444;">'
        "治療例の写真については、日本矯正歯科学会ホームページ倫理審査指針に基づき、"
        "各症例ページの本文で主訴・病態の概要・年齢・抜歯の有無・使用装置などを併記しています。"
        "治療期間・費用の目安、リスク・副作用の詳細は診療時の説明および"
        '<a href="../cost/index.html">診療の流れと治療費</a>をご確認ください。</p>\n'
    )
    needle = '<h4><img src="./common/img/h4Header.gif" alt="見出し｜概要" width="24" height="13" /></h4>\n'
    if needle in t and notice not in t:
        t = t.replace(needle, needle + notice)
    path.write_text(t, encoding="utf-8")
    return "treatment/index.html"


def add_case_footer_if_needed(path: Path) -> bool:
    rel = str(path.relative_to(ROOT)).replace("\\", "/")
    if not rel.startswith("treatment/") or rel.count("/") < 2:
        return False
    if "index_err" in rel:
        return False
    t = path.read_text(encoding="utf-8")
    if "治療前" not in t and "術前" not in t:
        return False
    if CASE_FOOTER in t or "倫理審査指針に基づき" in t:
        return False
    # メインの編集領域直前（<!-- InstanceEndEditable --> の直前の </div>）に挿入
    anchor = '<!-- InstanceBeginEditable name="EditRegion02" -->'
    end_editable = "<!-- InstanceEndEditable -->"
    if anchor not in t or end_editable not in t:
        return False
    region_start = t.find(anchor) + len(anchor)
    region_end = t.find(end_editable, region_start)
    if region_end == -1:
        return False
    region = t[region_start:region_end]
    marker = "</div>\n"
    last = region.rfind(marker)
    if last == -1:
        return False
    insert_at = region_start + last + len(marker)
    new_t = t[:insert_at] + CASE_FOOTER + "\n" + t[insert_at:]
    path.write_text(new_t, encoding="utf-8")
    return True


def patch_ontona_index02_index03() -> None:
    for rel in ("infomation/ontona_etc/index02.html", "infomation/ontona_etc/index03.html"):
        p = ROOT / rel
        if not p.exists():
            continue
        t = p.read_text(encoding="utf-8")
        t = t.replace(
            "「アントニオ猪木」タイプです。",
            "骨格性反対咬合で下顎が相対的に大きいパターンです。",
        )
        t = t.replace(
            "いわゆる「あごなし」などと呼ばれる「アンガールズ」タイプの例ですが、",
            "下顎の前方突出が弱く、上顎が相対的に前突して見える例では、",
        )
        p.write_text(t, encoding="utf-8")


def patch_end07() -> None:
    p = ROOT / "treatment" / "end" / "index07.html"
    if not p.exists():
        return
    t = p.read_text(encoding="utf-8")
    t = t.replace(
        "その結果、横顔も初診時と比べてとてもスマートになりました！",
        "その結果、横顔のバランスも初診時と比べて落ち着いた印象になりました。",
    )
    p.write_text(t, encoding="utf-8")


def main():
    patch_infomation_index(ROOT / "infomation" / "index.html")
    patch_treatment_index(ROOT / "treatment" / "index.html")
    patch_ontona_index02_index03()
    patch_end07()

    n = 0
    for p in ROOT.rglob("*.html"):
        if "tools" in p.parts:
            continue
        if add_case_footer_if_needed(p):
            n += 1
    print("case footers added:", n)


if __name__ == "__main__":
    main()
