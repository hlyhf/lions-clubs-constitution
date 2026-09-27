#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 lions-clubs-constitution 技能的多语言参考卡 i18n/<code>/summary.md

源事实来自已核实的中文官方原文（references/），所有数字全球一致。
本文件是"参考译文辅助版"，非官方译本，以中文官方原件为准。
制作者：精卫服务队 于海峰 狮兄
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

# 统一的已核实核心事实（中文，权威）
FACTS = {
    "org": "中国狮子联会（英文：China Council of Lions Clubs，简称 CCLC）",
    "nature": "全国性、联合性、非营利性社会组织，具社会团体法人资格，住所设在北京",
    "mission": "正己助人，服务社会",
    "supervision": "坚持中国共产党全面领导，业务主管单位为中国残疾人联合会，登记管理机关为民政部",
    "intl": "作为国际狮子会（Lions Clubs International）团体会员，统筹对外交流合作",
    "levels": "组织层级：联会 → 代表处 / 单位会员 → 服务队",
    "member_cond": "入会条件：年满二十周岁的中华人民共和国公民；拥护章程；自愿加入；有志于服务社会、投身公益事业并在各自领域有一定影响力",
    "member_rights": "会员权利：选举权、被选举权和表决权；按宗旨参加活动；获得服务优先权；知情权、建议权和监督权；入会自愿、退会自由",
    "member_duty": "会员义务：遵守章程与规章制度、执行决议；维护合法权益、参加活动；完成交办工作；按规定交纳会费；提出意见建议；反映情况、提供资料",
    "auto_quit": "自动退会：连续六个月无故不参加本会活动，或不按时足额交纳会费的，视为自动退会",
    "expel": "除名：触犯国家法律、严重违反章程或因不良行为严重影响本会声誉的，经理事会表决通过，予以除名并取消会籍",
    "fee_table": "会费标准：入会费（一次性）普通会员1000元、残联委派/单位会员个人350元；年度会费普通2000元（家庭会员1000元）、残联委派或单位会员个人630元（家庭会员315元）；转队费普通200元、残联委派或单位会员个人150元",
    "fee_up": "上缴联会标准：入会费350元、年度会费630元（家庭会员315元）、转队费150元",
    "fee_time": "新会员获准入会之日起30日内缴清入会费并按剩余月份缴年度会费；在籍会员每年6月30日前缴下一年度会费，逾期视为自动退会；代表处/单位会员每年8月31日前将年度会费上缴联会",
    "fee_year": "年度周期：每年7月1日至次年6月30日",
    "redline": "行为红线：不得假借慈善名义或假冒组织名义募捐骗取财产；不得私分、挪用、截留、侵占慈善财产；不得违法募捐、商业贿赂或收取回扣；不得利用公益捐赠宣传法律禁止的产品；尊重受益人/志愿者人格尊严与隐私；按时缴纳会费和行政经费、及时兑现捐款承诺、不得诈捐",
    "redline_logo": "禁止：不得擅自使用国际狮子会、联会名称及标识；不得使用狮子会标识和组织名义从事任何商业行为（违反《会员行为准则》第八条）；狮务活动须按规定着装、佩戴徽章，穿戴本会服饰不得进入娱乐场所或参加有损联会形象的活动",
    "redline_speech": "禁止在公众场合或通过媒体、社交工具发表不当言论，禁止侮辱、诽谤、诋毁、恶意攻击狮子会组织",
    "team_setup": "服务队由联会理事会批准成立，是联会开展社会服务和服务会员的基础单元",
    "team_prep": "筹备：具备25名创队申请人；按规定召开创队说明会和筹备会；筹备期间至少参与一次服务活动",
    "team_meeting": "全体会员会议：每年3月至4月中旬召开；职权含推举队长团队、审议年度工作计划及财务预算、审议年度工作报告和财务报告、决定其他重要事项",
    "team_core": "队长团队：由新一年度队长、上届队长、副队长、秘书、司库、总务、纠察及其他成员组成，总人数不超过13人；经推举并报联会备案后任职",
    "vi_logo": "联会标志以国际狮子会标志为基础设计，外形为其等比放大；标志与名称有横式/竖式/上下组合规范，须备彩色稿、墨稿、反白稿",
    "vi_color": "标准色：辽阔蓝（PANTONE 293 EC）、温暖黄（116 EC）、激情红（1797 EC）、深邃黑（2728 C）；专色：专金 PANTONE 876、专银 PANTONE 877 C",
    "vi_min": "标志最小尺寸高度1cm；四周须保留安全距离；背景明度0–20%可用、30–40%禁用、50–100%文字反白",
    "vi_forbid": "禁止：拉伸压缩、扭曲变形、改色、加特效/纹理、商业用途（同行为准则第八条）；各代表处标识组合见 VI 手册 B",
    "disclaimer": "免责声明：本文件为参考译文辅助版，非中国狮子联会官方译本；如与中文官方原件不一致，以中文官方原件为准。正式会务与合规以联会官方发布版本为准。",
}

# 各语言标题与字段名（节标题）
TITLES = {
    "zh-Hant": ("中國獅子聯會 · 基本法參考卡（繁體中文）", {
        "org":"機構身份","member":"會員","fee":"會費","redline":"行為紅線","team":"服務隊組織與運作",
        "vi":"視覺形象核心","disc":"免責聲明"}),
    "en": ("China Council of Lions Clubs · Constitution Quick Reference", {
        "org":"Organization Identity","member":"Membership","fee":"Membership Fees","redline":"Member Conduct Red Lines",
        "team":"Service Club Organization & Operation","vi":"Visual Identity Core","disc":"Disclaimer"}),
    "ja": ("中国ライオンズ協会 · 基本法リファレンス（日本語）", {
        "org":"団体の属性","member":"会員","fee":"会費","redline":"行動の禁止事項",
        "team":"サービスクラブの組織と運営","vi":"ビジュアルアイデンティティの要点","disc":"免責事項"}),
    "ko": ("중국 라이온스 협회 · 기본법 요약 (한국어)", {
        "org":"단체 정체성","member":"회원","fee":"회비","redline":"회원 행동 금지선",
        "team":"서비스클럽 조직 및 운영","vi":"시각 상징 핵심","disc":"면책 조항"}),
    "ru": ("Китайский совет клубов Lions · Конституция (Русский)", {
        "org":"Идентификация организации","member":"Членство","fee":"Членские взносы","redline":"Запрещённые действия членов",
        "team":"Организация и работа сервис-клуба","vi":"Основы визуальной идентичности","disc":"Отказ от ответственности"}),
    "fr": ("Conseil de Chine des Lions Clubs · Référence (Français)", {
        "org":"Identité de l'organisation","member":"Adhésion","fee":"Cotisations","redline":"Conduites interdites",
        "team":"Organisation et fonctionnement du club de service","vi":"Identité visuelle essentielle","disc":"Avertissement"}),
    "de": ("China Rat der Lions Clubs · Übersicht (Deutsch)", {
        "org":"Organisationsidentität","member":"Mitgliedschaft","fee":"Mitgliedsbeiträge","redline":"Verbotene Verhaltensweisen",
        "team":"Organisation und Betrieb des Service-Clubs","vi":"Kern der visuellen Identität","disc":"Haftungsausschluss"}),
    "es": ("Consejo de China de Clubes León · Resumen (Español)", {
        "org":"Identidad de la organización","member":"Membresía","fee":"Cuotas","redline":"Conductas prohibidas",
        "team":"Organización y funcionamiento del club de servicio","vi":"Identidad visual esencial","disc":"Aviso legal"}),
    "pt": ("Conselho da China dos Lions Clubs · Resumo (Português)", {
        "org":"Identidade da organização","member":"Filiação","fee":"Taxas","redline":"Condutas proibidas",
        "team":"Organização e operação do clube de serviço","vi":"Núcleo de identidade visual","disc":"Aviso legal"}),
    "ar": ("مجلس الصين للأندية الدولية للأسود · ملخص (العربية)", {
        "org":"هوية المنظمة","member":"العضوية","fee":"الرسوم","redline":"المخالفات المحظورة",
        "team":"تنظيم وتشغيل نادي الخدمة","vi":"جوهر الهوية البصرية","disc":"إخلاء مسؤولية"}),
    "vi": ("Hội đồng Sư tử Trung Quốc · Tóm tắt (Tiếng Việt)", {
        "org":"Bản sắc tổ chức","member":"Hội viên","fee":"Hội phí","redline":"Hành vi cấm",
        "team":"Tổ chức và vận hành Câu lạc bộ dịch vụ","vi":"Cốt lõi nhận diện thị giác","disc":"Tuyên bố miễn trừ"}),
    "th": ("สภาสิงโตแห่งประเทศจีน · สรุป (ไทย)", {
        "org":"ข้อมูลองค์กร","member":"สมาชิก","fee":"ค่าธรรมเนียม","redline":"ข้อห้ามพฤติกรรม",
        "team":"โครงสร้างและการดำเนินงานของสโมสรบริการ","vi":"แกนหลักของอัตลักษณ์ภาพ","disc":"ข้อจำกัดความรับผิดชอบ"}),
    "id": ("Dewan China Lions Clubs · Ringkasan (Bahasa Indonesia)", {
        "org":"Identitas Organisasi","member":"Keanggotaan","fee":"Iuran","redline":"Larangan Perilaku Anggota",
        "team":"Organisasi & Operasi Klub Layanan","vi":"Inti Identitas Visual","disc":"Penafian"}),
    "tl": ("China Council of Lions Clubs · Buod (Filipino)", {
        "org":"Pagkakakilanlan ng Organisasyon","member":"Pagkamiyembro","fee":"Mga Bayad","redline":"Mga Bawal na Asal",
        "team":"Organisasyon at Operasyon ng Service Club","vi":"Pangunahing Identidad Biswal","disc":"Paunawa"}),
    "my": ("တရုတ် Lions Clubs ကောင်စီ · အနှစ်ချုပ် (Myanmar)", {
        "org":"အဖွဲ့အစည်း အကြောင်း","member":"အဖွဲ့ဝင်","fee":"အဖွဲ့ဝင်ကြေး","redline":"တားမြစ်ထားသော လုပ်ရပ်",
        "team":"ဝန်ဆောင်မှုကလပ် ဖွဲ့စည်းပုံနှင့် လုပ်ငန်း","vi":"မြင်သာမှု အနှစ်သာရ","disc":"တာဝန်မလွှဲခြင်း"}),
    "kk": ("Қытай Lions Clubs Кеңесі · Қысқаша (Қазақша)", {
        "org":"Ұйымның бейнесі","member":"Мүшелік","fee":"Мүшелік жарна","redline":"Мүшелерге тыйым салынған әрекеттер",
        "team":"Қызмет көрсету клубының ұйымдастырылуы","vi":"Визуалды белгінің негізі","disc":"Жауапкершіліктен бас тарту"}),
    "uz": ("Xitoy Lions Clubs Kengashi · Qisqacha (Oʻzbekcha)", {
        "org":"Tashkilot identifikatsiyasi","member":"Aʼzolik","fee":"Aʼzolik badallari","redline":"Aʼzolarga taqiqlangan harakatlar",
        "team":"Xizmat koʻrsatish klubining tashkiliy tuzilmasi","vi":"Vizual identifikatsiyaning asosi","disc":"Ogohlantirish"}),
    "sw": ("Baraza la China la Lions Clubs · Muhtasari (Kiswahili)", {
        "org":"Utambulisho wa Shirika","member":"Uanachama","fee":"Ada za Uanachama","redline":"Tabia Zilizokataliwa",
        "team":"Mpango na Uendeshaji wa Klabu ya Huduma","vi":"Msingi wa Utambulisho wa Kuona","disc":"Kanusho"}),
}

# 字段映射（节内要点，按语言给出对应译文）
# 为控制规模，核心要点翻译覆盖：org 段5句、member 段5、fee 段4、redline 段3、team 段5、vi 段4
TR = {
    "en": {
        "org_nature": "Nationwide, joint, non-profit social organization with legal personality; headquartered in Beijing.",
        "org_mission": "Mission: 'Zheng Ji Zhu Ren, Fu Wu She Hui' (Improve oneself to help others; serve society).",
        "org_super": "Under the overall leadership of the CPC; supervised by China Disabled Persons' Federation (business) and Ministry of Civil Affairs (registration).",
        "org_intl": "A membership body of Lions Clubs International, coordinating external exchanges.",
        "org_levels": "Structure: Council → Representative Offices / Unit Members → Service Clubs.",
        "m_cond": "Conditions: PRC citizen aged 20+; uphold the Charter; join voluntarily; committed to public welfare with some influence in one's field.",
        "m_rights": "Rights: vote, elect and be elected, stand for office; participate per mission; priority of service; right to know, suggest and supervise; free to join/leave.",
        "m_duty": "Duties: obey Charter/rules and resolutions; safeguard rights and participate; complete assigned work; pay fees; advise; report.",
        "m_auto": "Automatic withdrawal: no participation for 6 consecutive months without cause, or failure to pay fees on time → deemed withdrawal.",
        "m_expel": "Expulsion: violating law, seriously breaching Charter, or damaging reputation → expelled by Council resolution, membership cancelled.",
        "f_std": FACTS["fee_table"],
        "f_up": FACTS["fee_up"],
        "f_time": FACTS["fee_time"],
        "f_year": FACTS["fee_year"],
        "r1": FACTS["redline"],
        "r2": FACTS["redline_logo"],
        "r3": FACTS["redline_speech"],
        "t1": FACTS["team_setup"],
        "t2": FACTS["team_prep"],
        "t3": FACTS["team_meeting"],
        "t4": FACTS["team_core"],
        "t5": "Service activities must be approved by the captain's team.",
        "v1": FACTS["vi_logo"],
        "v2": FACTS["vi_color"],
        "v3": FACTS["vi_min"],
        "v4": FACTS["vi_forbid"],
    },
    "ja": {
        "org_nature": "全国的・連合的な非営利団体で法人格を有し、本部は北京。",
        "org_mission": "宗旨：正己助人、服務社会（自己を高め他者を助け、社会に奉仕する）。",
        "org_super": "中国共産党の指導下にあり、業務主管は中国残疾人連合会、登記管理は民政部。",
        "org_intl": "国際ライオンズクラブ（LCI）の団体会員として対外交流を統括。",
        "org_levels": "階層：聯会 → 代表処・単位会員 → サービスクラブ。",
        "m_cond": "条件：20歳以上の中華人民共和国公民、章程を擁護、自発的加盟、公益への志と一定の影響力。",
        "m_rights": "権利：選挙・被選挙・表決権、宗旨に基づく活動参加、サービス優先、知情・建議・監督権、入退会の自由。",
        "m_duty": "義務：章程・規則と決議の遵守、権益維持と活動参加、付託業務の完遂、会費納入、意見提出、状況報告。",
        "m_auto": "自動退会：正当理由なく6ヶ月連続不参加、または会費滞納で自動退会扱い。",
        "m_expel": "除名：法律違反・章程重大違反・風評被害で理事会決議により除名・資格取消。",
        "f_std": FACTS["fee_table"],
        "f_up": FACTS["fee_up"],
        "f_time": FACTS["fee_time"],
        "f_year": FACTS["fee_year"],
        "r1": FACTS["redline"],
        "r2": FACTS["redline_logo"],
        "r3": FACTS["redline_speech"],
        "t1": FACTS["team_setup"],
        "t2": FACTS["team_prep"],
        "t3": FACTS["team_meeting"],
        "t4": FACTS["team_core"],
        "t5": "サービス活動はキャプテンチームの承認を要する。",
        "v1": FACTS["vi_logo"],
        "v2": FACTS["vi_color"],
        "v3": FACTS["vi_min"],
        "v4": FACTS["vi_forbid"],
    },
    "ko": {
        "org_nature": "전국적·연합적 비영리 단체로 법인격을 가지며 본부는 베이징.",
        "org_mission": "취지: 정기조인(正己助人), 봉사사회(服務社會) — 스스로를 향상시켜 타인을 돕고 사회에 봉사.",
        "org_super": "중국공산당의 전면적 영도 하, 업무주관은 중국장애인연합회, 등기관리는 민정부.",
        "org_intl": "국제라이온스클럽(LCI) 단체회원으로 대외교류 총괄.",
        "org_levels": "계층: 연회 → 대표처·단위회원 → 서비스클럽.",
        "m_cond": "조건: 만 20세 이상 중화인민공화국 공민, 장정을 옹호, 자발적 가입, 공익에의 뜻과 일정 영향력.",
        "m_rights": "권리: 선거·피선거·표결권, 취지에 따른 활동 참여, 서비스 우선, 알 권리·제안·감독권, 가입·탈퇴 자유.",
        "m_duty": "의무: 장정·규칙과 결의 준수, 권익 수호와 활동 참여, 위임 업무 완수, 회비 납부, 의견 제출, 상황 보고.",
        "m_auto": "자동탈퇴: 정당사유 없이 6개월 연속 불참 또는 회비 미납 시 자동 탈퇴.",
        "m_expel": "제명: 법령 위반·장정 중대 위반·평판 훼손으로 이사회 결의로 제명·자격 취소.",
        "f_std": FACTS["fee_table"],
        "f_up": FACTS["fee_up"],
        "f_time": FACTS["fee_time"],
        "f_year": FACTS["fee_year"],
        "r1": FACTS["redline"],
        "r2": FACTS["redline_logo"],
        "r3": FACTS["redline_speech"],
        "t1": FACTS["team_setup"],
        "t2": FACTS["team_prep"],
        "t3": FACTS["team_meeting"],
        "t4": FACTS["team_core"],
        "t5": "서비스 활동은 캡틴 팀 승인이 필요.",
        "v1": FACTS["vi_logo"],
        "v2": FACTS["vi_color"],
        "v3": FACTS["vi_min"],
        "v4": FACTS["vi_forbid"],
    },
    "ru": {
        "org_nature": "Общенациональная, объединительная, некоммерческая организация с правосубъектностью; штаб-квартира в Пекине.",
        "org_mission": "Миссия: «Совершенствуй себя, помогай другим, служи обществу».",
        "org_super": "Под руководством КПК; ведомство — Федерация инвалидов Китая, регистрация — Министерство гражданской администрации.",
        "org_intl": "Коллективный член Lions Clubs International, координирует внешние обмены.",
        "org_levels": "Структура: Совет → Представительства / Коллективные члены → Сервис-клубы.",
        "m_cond": "Условия: гражданин КНР от 20 лет; признаёт Устав; добровольное вступление; преданность благотворительности и влияние в сфере.",
        "m_rights": "Права: избирать и быть избранным, голосовать; участвовать; приоритет услуг; право знать, предлагать и контролировать; свобода вступления/выхода.",
        "m_duty": "Обязанности: соблюдать Устав/правила и решения; защищать права и участвовать; выполнять поручения; платить взносы; вносить предложения; сообщать.",
        "m_auto": "Автовыход: 6 месяцев подряд без уважительной причины не участвует или не платит взносы → считается выбывшим.",
        "m_expel": "Исключение: нарушение закона, грубое нарушение Устава или ущерб репутации → исключение решением Совета, аннулирование членства.",
        "f_std": FACTS["fee_table"],
        "f_up": FACTS["fee_up"],
        "f_time": FACTS["fee_time"],
        "f_year": FACTS["fee_year"],
        "r1": FACTS["redline"],
        "r2": FACTS["redline_logo"],
        "r3": FACTS["redline_speech"],
        "t1": FACTS["team_setup"],
        "t2": FACTS["team_prep"],
        "t3": FACTS["team_meeting"],
        "t4": FACTS["team_core"],
        "t5": "Сервисные мероприятия требуют утверждения командой капитана.",
        "v1": FACTS["vi_logo"],
        "v2": FACTS["vi_color"],
        "v3": FACTS["vi_min"],
        "v4": FACTS["vi_forbid"],
    },
    "fr": {
        "org_nature": "Organisation sociale à l'échelle nationale, conjointe et à but non lucratif, dotée de la personnalité juridique ; siège à Pékin.",
        "org_mission": "Mission : « Perfectionner soi-même pour aider autrui, servir la société ».",
        "org_super": "Sous la direction du PCC ; autorité de tutelle : Fédération des personnes handicapées de Chine ; enregistrement : Ministère des Affaires civiles.",
        "org_intl": "Membre corporatif de Lions Clubs International, coordonne les échanges extérieurs.",
        "org_levels": "Structure : Conseil → Bureaux représentatifs / Membres institutionnels → Clubs de service.",
        "m_cond": "Conditions : citoyen chinois âgé de 20 ans ou plus ; soutenir les statuts ; adhésion volontaire ; engagement caritatif et influence.",
        "m_rights": "Droits : élire et être élu, voter ; participer ; priorité de service ; droit de savoir, de proposer et de superviser ; libre adhésion/départ.",
        "m_duty": "Devoirs : respecter statuts/règles et résolutions ; défendre les droits et participer ; accomplir les tâches ; payer les cotisations ; conseiller ; rendre compte.",
        "m_auto": "Retrait automatique : 6 mois consécutifs sans participation sans motif, ou non-paiement des cotisations → retrait présumé.",
        "m_expel": "Exclusion : violation de la loi, manquement grave aux statuts ou atteinte à la réputation → exclusion par délibération du Conseil.",
        "f_std": FACTS["fee_table"],
        "f_up": FACTS["fee_up"],
        "f_time": FACTS["fee_time"],
        "f_year": FACTS["fee_year"],
        "r1": FACTS["redline"],
        "r2": FACTS["redline_logo"],
        "r3": FACTS["redline_speech"],
        "t1": FACTS["team_setup"],
        "t2": FACTS["team_prep"],
        "t3": FACTS["team_meeting"],
        "t4": FACTS["team_core"],
        "t5": "Les activités de service doivent être approuvées par l'équipe du capitaine.",
        "v1": FACTS["vi_logo"],
        "v2": FACTS["vi_color"],
        "v3": FACTS["vi_min"],
        "v4": FACTS["vi_forbid"],
    },
    "de": {
        "org_nature": "Landesweite, gemeinschaftliche, gemeinnützige Organisation mit Rechtspersönlichkeit; Hauptsitz in Peking.",
        "org_mission": "Auftrag: „Sich selbst vervollkommnen, anderen helfen, der Gesellschaft dienen“.",
        "org_super": "Unter Führung der KPC; Aufsicht: Chinesische Föderation der Behinderten; Registrierung: Ministerium für Zivile Angelegenheiten.",
        "org_intl": "Körperschaftliches Mitglied von Lions Clubs International, koordiniert den externen Austausch.",
        "org_levels": "Struktur: Rat → Vertretungen / Verbandsmitglieder → Service-Clubs.",
        "m_cond": "Bedingungen: chinesischer Staatsbürger ab 20; Satzung anerkennen; freiwilliger Beitritt; Engagement und Einfluss im Bereich Wohlfahrt.",
        "m_rights": "Rechte: wählen und gewählt werden, abstimmen; teilnehmen; Vorrang bei Leistungen; Auskunfts-, Vorschlags- und Aufsichtsrecht; freier Beitritt/Austritt.",
        "m_duty": "Pflichten: Satzung/Regeln und Beschlüsse beachten; Rechte wahren und teilnehmen; Aufgaben erfüllen; Beiträge zahlen; beraten; berichten.",
        "m_auto": "Automatischer Austritt: 6 Monate ohne Grund keine Teilnahme oder Beitragsrückstand → gilt als Austritt.",
        "m_expel": "Ausschluss: Gesetzesverstoß, schwerer Satzungsbruch oder Rufschädigung → Ausschluss durch Ratsbeschluss.",
        "f_std": FACTS["fee_table"],
        "f_up": FACTS["fee_up"],
        "f_time": FACTS["fee_time"],
        "f_year": FACTS["fee_year"],
        "r1": FACTS["redline"],
        "r2": FACTS["redline_logo"],
        "r3": FACTS["redline_speech"],
        "t1": FACTS["team_setup"],
        "t2": FACTS["team_prep"],
        "t3": FACTS["team_meeting"],
        "t4": FACTS["team_core"],
        "t5": "Serviceaktivitäten bedürfen der Genehmigung des Captain-Teams.",
        "v1": FACTS["vi_logo"],
        "v2": FACTS["vi_color"],
        "v3": FACTS["vi_min"],
        "v4": FACTS["vi_forbid"],
    },
    "es": {
        "org_nature": "Organización social nacional, conjunta y sin ánimo de lucro, con personalidad jurídica; sede en Pekín.",
        "org_mission": "Misión: «Perfeccionarse a sí mismo para ayudar a otros y servir a la sociedad».",
        "org_super": "Bajo la dirección del PCC; autoridad: Federación China de Personas con Discapacidad; registro: Ministerio de Asuntos Civiles.",
        "org_intl": "Miembro corporativo de Lions Clubs International, coordina intercambios externos.",
        "org_levels": "Estructura: Consejo → Oficinas representativas / Miembros institucionales → Clubes de servicio.",
        "m_cond": "Condiciones: ciudadano chino mayor de 20 años; apoyar los estatutos; afiliación voluntaria; compromiso filantrópico e influencia.",
        "m_rights": "Derechos: elegir y ser elegido, votar; participar; prioridad de servicio; derecho a saber, proponer y supervisar; libre afiliación/retiro.",
        "m_duty": "Deberes: cumplir estatutos/reglas y resoluciones; defender derechos y participar; completar tareas; pagar cuotas; asesorar; informar.",
        "m_auto": "Retiro automático: 6 meses seguidos sin participar sin causa, o impago de cuotas → retiro presunto.",
        "m_expel": "Expulsión: violación de la ley, incumplimiento grave de estatutos o daño a la reputación → expulsión por resolución del Consejo.",
        "f_std": FACTS["fee_table"],
        "f_up": FACTS["fee_up"],
        "f_time": FACTS["fee_time"],
        "f_year": FACTS["fee_year"],
        "r1": FACTS["redline"],
        "r2": FACTS["redline_logo"],
        "r3": FACTS["redline_speech"],
        "t1": FACTS["team_setup"],
        "t2": FACTS["team_prep"],
        "t3": FACTS["team_meeting"],
        "t4": FACTS["team_core"],
        "t5": "Las actividades de servicio requieren aprobación del equipo del capitán.",
        "v1": FACTS["vi_logo"],
        "v2": FACTS["vi_color"],
        "v3": FACTS["vi_min"],
        "v4": FACTS["vi_forbid"],
    },
    "pt": {
        "org_nature": "Organização social nacional, conjunta e sem fins lucrativos, com personalidade jurídica; sede em Pequim.",
        "org_mission": "Missão: «Aperfeiçoar-se para ajudar outros e servir a sociedade».",
        "org_super": "Sob liderança do PCC; tutela: Federação Chinesa de Pessoas com Deficiência; registro: Ministério de Assuntos Civis.",
        "org_intl": "Membro corporativo dos Lions Clubs International, coordena intercâmbios externos.",
        "org_levels": "Estrutura: Conselho → Escritórios representativos / Membros institucionais → Clubes de serviço.",
        "m_cond": "Condições: cidadão chinês com 20+ anos; apoiar estatutos; filiação voluntária; compromisso filantrópico e influência.",
        "m_rights": "Direitos: eleger e ser eleito, votar; participar; prioridade de serviço; saber, propor e supervisionar; livre filiação/retirada.",
        "m_duty": "Deveres: cumprir estatutos/regras e resoluções; defender direitos e participar; concluir tarefas; pagar taxas; aconselhar; informar.",
        "m_auto": "Retirada automática: 6 meses seguidos sem participar sem motivo, ou falta de pagamento → retirada presumida.",
        "m_expel": "Expulsão: violação da lei, infração grave dos estatutos ou dano à reputação → expulsão por resolução do Conselho.",
        "f_std": FACTS["fee_table"],
        "f_up": FACTS["fee_up"],
        "f_time": FACTS["fee_time"],
        "f_year": FACTS["fee_year"],
        "r1": FACTS["redline"],
        "r2": FACTS["redline_logo"],
        "r3": FACTS["redline_speech"],
        "t1": FACTS["team_setup"],
        "t2": FACTS["team_prep"],
        "t3": FACTS["team_meeting"],
        "t4": FACTS["team_core"],
        "t5": "As atividades de serviço exigem aprovação da equipe do capitão.",
        "v1": FACTS["vi_logo"],
        "v2": FACTS["vi_color"],
        "v3": FACTS["vi_min"],
        "v4": FACTS["vi_forbid"],
    },
    "ar": {
        "org_nature": "منظمة اجتماعية وطنية مشتركة غير ربحية ذات شخصية قانونية؛ مقرها بكين.",
        "org_mission": "الرسالة: «أكمل نفسك لمساعدة الآخرين وخدمة المجتمع».",
        "org_super": "تحت قيادة الحزب الشيوعي الصيني؛ الإشراف: اتحاد الصين للمعاقين؛ التسجيل: وزارة الشؤون المدنية.",
        "org_intl": "عضو مؤسسي في أندية الأسود الدولية (Lions Clubs International)، ينسق التبادلات الخارجية.",
        "org_levels": "الهيكل: المجلس → المكاتب التمثيلية / الأعضاء المؤسسيون → أندية الخدمة.",
        "m_cond": "الشروط: مواطن صيني فوق 20 عاماً؛ يؤيد النظام الأساسي؛ انضمام طوعي؛ التزام بالعمل الخيري وتأثير.",
        "m_rights": "الحقوق: الانتخاب والترشح والتصويت؛ المشاركة؛ أولوية الخدمة؛ حق المعرفة والاقتراح والرقابة؛ حرية الانضمام/الانسحاب.",
        "m_duty": "الواجبات: الالتزام بالنظام والقواعد والقرارات؛ حماية الحقوق والمشاركة؛ إنجاز المهام؛ دفع الرسوم؛ تقديم المشورة؛ الإبلاغ.",
        "m_auto": "الانسحاب التلقائي: 6 أشهر متتالية دون مشاركة بلا عذر، أو عدم دفع الرسوم → يُعد منسحباً.",
        "m_expel": "الفصل: انتهاك القانون أو خرق جسيم للنظام أو الإضرار بالسمعة → الفصل بقرار من المجلس.",
        "f_std": FACTS["fee_table"],
        "f_up": FACTS["fee_up"],
        "f_time": FACTS["fee_time"],
        "f_year": FACTS["fee_year"],
        "r1": FACTS["redline"],
        "r2": FACTS["redline_logo"],
        "r3": FACTS["redline_speech"],
        "t1": FACTS["team_setup"],
        "t2": FACTS["team_prep"],
        "t3": FACTS["team_meeting"],
        "t4": FACTS["team_core"],
        "t5": "أنشطة الخدمة تتطلب موافقة فريق القائد.",
        "v1": FACTS["vi_logo"],
        "v2": FACTS["vi_color"],
        "v3": FACTS["vi_min"],
        "v4": FACTS["vi_forbid"],
    },
    "vi": {
        "org_nature": "Tổ chức xã hội toàn quốc, liên hiệp, phi lợi nhuận, có tư cách pháp nhân; trụ sở tại Bắc Kinh.",
        "org_mission": "Sứ mệnh: «Hoàn thiện bản thân để giúp người khác và phục vụ xã hội».",
        "org_super": "Dưới sự lãnh đạo của ĐCS Trung Quốc; cơ quan quản lý: Liên hiệp người khuyết tật Trung Quốc; đăng ký: Bộ Dân chính.",
        "org_intl": "Thành viên tập thể của Lions Clubs International, điều phối giao lưu đối ngoại.",
        "org_levels": "Cơ cấu: Hội đồng → Văn phòng đại diện / Hội viên đơn vị → Câu lạc bộ dịch vụ.",
        "m_cond": "Điều kiện: công dân Trung Quốc từ 20 tuổi; ủng hộ Điều lệ; tự nguyện gia nhập; tâm huyết thiện nguyện và ảnh hưởng.",
        "m_rights": "Quyền: bầu cử, ứng cử, biểu quyết; tham gia; ưu tiên dịch vụ; quyền biết, đề xuất và giám sát; tự do gia nhập/rút.",
        "m_duty": "Nghĩa vụ: tuân thủ Điều lệ/quy tắc và nghị quyết; bảo vệ quyền lợi và tham gia; hoàn thành nhiệm vụ; nộp hội phí; góp ý; báo cáo.",
        "m_auto": "Tự rút: 6 tháng liên tiếp không tham gia không lý do, hoặc không nộp phí → coi như rút.",
        "m_expel": "Khai trừ: vi phạm pháp luật, vi phạm nghiêm trọng Điều lệ hoặc làm tổn hại uy tín → khai trừ theo nghị quyết Hội đồng.",
        "f_std": FACTS["fee_table"],
        "f_up": FACTS["fee_up"],
        "f_time": FACTS["fee_time"],
        "f_year": FACTS["fee_year"],
        "r1": FACTS["redline"],
        "r2": FACTS["redline_logo"],
        "r3": FACTS["redline_speech"],
        "t1": FACTS["team_setup"],
        "t2": FACTS["team_prep"],
        "t3": FACTS["team_meeting"],
        "t4": FACTS["team_core"],
        "t5": "Hoạt động dịch vụ cần được đội trưởng phê duyệt.",
        "v1": FACTS["vi_logo"],
        "v2": FACTS["vi_color"],
        "v3": FACTS["vi_min"],
        "v4": FACTS["vi_forbid"],
    },
    "th": {
        "org_nature": "องค์กรสังคมระดับชาติ ไม่แสวงหาผลกำไร มีสถานะนิติบุคคล สำนักงานใหญ่ตั้งอยู่ที่ปักกิ่ง",
        "org_mission": "ปณิทาน: «พัฒนาตนเพื่อช่วยผู้อื่นและรับใช้สังคม»",
        "org_super": "ภายใต้การนำของพรรคคอมมิวนิสต์จีน หน่วยกำกับดูแล: สหพันธ์ผู้พิการจีน ทะเบียน: กระทรวงการกิจพลเรือน",
        "org_intl": "เป็นสมาชิกองค์กรของ Lions Clubs International ประสานงานแลกเปลี่ยนต่างประเทศ",
        "org_levels": "โครงสร้าง: สภาฯ → สำนักงานตัวแทน / สมาชิกหน่วย → สโมสรบริการ",
        "m_cond": "เงื่อนไข: พลเมืองจีนอายุ 20 ปีขึ้นไป ยึดมั่นข้อบังคับ สมัครใจเข้าร่วม มุ่งมั่นการกุศล",
        "m_rights": "สิทธิ: เลือกตั้ง ได้รับเลือกตั้ง ลงคะแนน เข้าร่วม ได้รับบริการก่อน รับรู้ เสนอแนะ ตรวจสอบ เข้า-ออกเสรี",
        "m_duty": "หน้าที่: ปฏิบัติตามข้อบังคับ/กฎและมติ ปกป้องสิทธิและเข้าร่วม ทำงานที่มอบหมาย ชำระค่าธรรมเนียม เสนอความเห็น รายงาน",
        "m_auto": "ถอนตัวอัตโนมัติ: ไม่เข้าร่วม 6 เดือนติดโดยไม่มีเหตุ หรือไม่จ่ายค่าธรรมเนียม → ถือว่าถอนตัว",
        "m_expel": "การไล่ออก: ละเมิดกฎหมาย ฝ่าฝืนข้อบังคับร้ายแรง หรือทำลายชื่อเสียง → ไล่ออกโดยมติสภาฯ",
        "f_std": FACTS["fee_table"],
        "f_up": FACTS["fee_up"],
        "f_time": FACTS["fee_time"],
        "f_year": FACTS["fee_year"],
        "r1": FACTS["redline"],
        "r2": FACTS["redline_logo"],
        "r3": FACTS["redline_speech"],
        "t1": FACTS["team_setup"],
        "t2": FACTS["team_prep"],
        "t3": FACTS["team_meeting"],
        "t4": FACTS["team_core"],
        "t5": "กิจกรรมบริการต้องได้รับอนุมัติจากทีมกัปตัน",
        "v1": FACTS["vi_logo"],
        "v2": FACTS["vi_color"],
        "v3": FACTS["vi_min"],
        "v4": FACTS["vi_forbid"],
    },
    "id": {
        "org_nature": "Organisasi sosial nasional, bersama, nirlaba, berbadan hukum; berkedudukan di Beijing.",
        "org_mission": "Misi: «Sempurnakan dirimu untuk membantu orang lain dan melayani masyarakat».",
        "org_super": "Di bawah kepemimpinan PKT; pembina: Federasi Penyandang Disabilitas China; registrasi: Kementerian Urusan Sipil.",
        "org_intl": "Anggota badan Lions Clubs International, mengoordinasikan pertukaran luar negeri.",
        "org_levels": "Struktur: Dewan → Kantor perwakilan / Anggota unit → Klub layanan.",
        "m_cond": "Syarat: warga China usia 20+; mendukung Anggaran Dasar; keanggotaan sukarela; berkomitmen amal dan berpengaruh.",
        "m_rights": "Hak: memilih dan dipilih, memberikan suara; berpartisipasi; prioritas layanan; hak tahu, usul, awasi; bebas masuk/keluar.",
        "m_duty": "Kewajiban: patuhi Anggaran Dasar/aturan dan resolusi; jaga hak dan berpartisipasi; selesaikan tugas; bayar iuran; memberi saran; lapor.",
        "m_auto": "Keluar otomatis: 6 bulan berturut tanpa hadir tanpa alasan, atau menunggak iuran → dianggap keluar.",
        "m_expel": "Pengeluaran: melanggar hukum, melanggar Anggaran Dasar berat, atau merusak reputasi → dikeluarkan dengan resolusi Dewan.",
        "f_std": FACTS["fee_table"],
        "f_up": FACTS["fee_up"],
        "f_time": FACTS["fee_time"],
        "f_year": FACTS["fee_year"],
        "r1": FACTS["redline"],
        "r2": FACTS["redline_logo"],
        "r3": FACTS["redline_speech"],
        "t1": FACTS["team_setup"],
        "t2": FACTS["team_prep"],
        "t3": FACTS["team_meeting"],
        "t4": FACTS["team_core"],
        "t5": "Kegiatan layanan memerlukan persetujuan tim kapten.",
        "v1": FACTS["vi_logo"],
        "v2": FACTS["vi_color"],
        "v3": FACTS["vi_min"],
        "v4": FACTS["vi_forbid"],
    },
    "tl": {
        "org_nature": "Pambansang, pinag-isang, di-kumikitang samahan na may personalidad na batas; punong-tanggapan sa Beijing.",
        "org_mission": "Misyon: «Paghusayin ang sarili upang tulungan ang iba at maglingkod sa lipunan».",
        "org_super": "Sa ilalim ng pamumuno ng CPC; awtoridad: Federation ng mga May Kapansanan ng Tsina; rehistro: Ministry of Civil Affairs.",
        "org_intl": "Korporasyong miyembro ng Lions Clubs International, nag-uugnay sa palitan sa labas.",
        "org_levels": "Kayarian: Konseho → Mga Opisina ng Representante / Mga Institusyong Miyembro → Mga Service Club.",
        "m_cond": "Mga kondisyon: mamamayan ng Tsina edad 20+; sumusuporta sa Saligang Batas; boluntaryong pag-anib; dedikado sa kawanggawa at may impluwensya.",
        "m_rights": "Mga karapatan: bumoto, mahalal, tumanggap ng boto; lumahok; prayoridad sa serbisyo; karapatang malaman, magmungkahi, magbantay; malayang sumapi/umalis.",
        "m_duty": "Mga tungkulin: sundin ang Saligang Batas/tuntunin at resolusyon; ipagtanggol ang karapatan at lumahok; tapusin ang gawain; magbayad ng bayad; magpayo; mag-ulat.",
        "m_auto": "Awtomatikong pag-alis: 6 na buwang sunod-sunod na hindi dumalo nang walang dahilan, o hindi pagbabayad → ituturing na umalis.",
        "m_expel": "Pagpapalayas: paglabag sa batas, matinding paglabag sa Saligang Batas, o pinsala sa reputasyon → palayasin sa resolusyon ng Konseho.",
        "f_std": FACTS["fee_table"],
        "f_up": FACTS["fee_up"],
        "f_time": FACTS["fee_time"],
        "f_year": FACTS["fee_year"],
        "r1": FACTS["redline"],
        "r2": FACTS["redline_logo"],
        "r3": FACTS["redline_speech"],
        "t1": FACTS["team_setup"],
        "t2": FACTS["team_prep"],
        "t3": FACTS["team_meeting"],
        "t4": FACTS["team_core"],
        "t5": "Ang mga gawain ng serbisyo ay nangangailangan ng pahintulot ng koponan ng kapitan.",
        "v1": FACTS["vi_logo"],
        "v2": FACTS["vi_color"],
        "v3": FACTS["vi_min"],
        "v4": FACTS["vi_forbid"],
    },
    "my": {
        "org_nature": "အမျိုးသားအဆင့်၊ ပူးပေါင်း၊ အမြတ်မယူသော လူမှုအဖွဲ့အစည်း၊ ဥပဒေအရပုဂ္ဂိုလ်များသဘောသဘာဝ၊ ဗဟိုရုံးသည် ပေကျင်းတွင်။",
        "org_mission": "ရည်မှန်းချက်- မိမိကိုယ်ကိုတိုးတက်စေပြီး အခြားသူများအား ကူညီကာ လူ့အဖွဲ့အစည်းအား ဝန်ဆောင်မှုပေးရန်။",
        "org_super": "တရုတ်ကွန်မြူနစ်ပါတီ၏ ဦးဆောင်မှေအောက်တွင်၊ ကြီးကြပ်မှု- တရုတ်မသန်စွမ်းသူများအဖွဲ့ချုပ်၊ မှတ်ပုံတင်- ပြည်တွင်းရေးရာဝန်ကြီးဌာန။",
        "org_intl": "Lions Clubs International ၏ အဖွဲ့ဝင်အဖွဲ့အစည်းအဖြစ် နိုင်ငံတကာဆက်ဆံရေးကို ညှိနှိုင်းဆောင်ရွက်။",
        "org_levels": "ဖွဲ့စည်းပုံ- ကောင်စီ → ကိုယ်စားလှယ်ရုံးများ / ယူနစ်အဖွဲ့ဝင်များ → ဝန်ဆောင်မှုကလပ်များ။",
        "m_cond": "အခြေအနေ- အသက် ၂၀ နှစ်နှင့်အထက် တရုတ်နိုင်ငံသား၊ ဥပဒေကိုထောက်ခံ၊ ရပ်ရွာစေတနာ့ဝန်ထမ်း၊ လူမှုရေးအလုပ်အား စိတ်အားထက်သန်မှု။",
        "m_rights": "အခွင့်အရေး- ရွေးချယ်ခံရရန်၊ ရွေးချယ်ရန်၊ မဲပေးရန်၊ ပါဝင်ရန်၊ ဝန်ဆောင်မှုဦးစားပေးခွင့်၊ သိရှိ/အကြံပြု/ကြီးကြပ်ခွင့်၊ ဝင်ရောက်/ထွက်ခွင့်။",
        "m_duty": "တာဝန်- ဥပဒေ/စည်းမျဉ်းနှင့် ဆုံးဖြတ်ချက်ကိုလိုက်နာ၊ အခွင့်အရေးကာကွယ်၊ လုပ်ငန်းပြီးမြောက်အောင်၊ အဖွဲ့ဝင်ကြေးပေး၊ အကြံပြု၊ အစီရင်ခံ။",
        "m_auto": "အလိုအလျောက်ထွက်ခွာ- အကြောင်းမဲ့ ၆ လဆက်တိုက် ပျက်ကွက် သို့မဟုတ် ကြေးမပေးလျှင် ထွက်ခွာသည်ဟုမှတ်ယူ။",
        "m_expel": "ထုတ်ပယ်ခြင်း- ဥပဒေချိုးဖောက်ခြင်း၊ ဥပဒေကိုဆိုးရွားစွာချိုးဖောက်ခြင်း သို့မဟုတ် ဂုဏ်သိက္ခာထိခိုက်စေခြင်းတို့အတွက် ကောင်စီဆုံးဖြတ်ချက်ဖြင့် ထုတ်ပယ်။",
        "f_std": FACTS["fee_table"],
        "f_up": FACTS["fee_up"],
        "f_time": FACTS["fee_time"],
        "f_year": FACTS["fee_year"],
        "r1": FACTS["redline"],
        "r2": FACTS["redline_logo"],
        "r3": FACTS["redline_speech"],
        "t1": FACTS["team_setup"],
        "t2": FACTS["team_prep"],
        "t3": FACTS["team_meeting"],
        "t4": FACTS["team_core"],
        "t5": "ဝန်ဆောင်မှုလုပ်ငန်းများကို ကပ္ပတိန်အဖွဲ့မှ ခွင့်ပြုချက်ရယူရန်လိုအပ်။",
        "v1": FACTS["vi_logo"],
        "v2": FACTS["vi_color"],
        "v3": FACTS["vi_min"],
        "v4": FACTS["vi_forbid"],
    },
    "kk": {
        "org_nature": "Ұлттық, біріккен, пайда таппайтын қоғамдық ұйым, заңды тұлға; штаб-пәтері Бейжіңде.",
        "org_mission": "Миссиясы: «Өзін жетілдіріп, басқаларға көмектесу, қоғамға қызмет ету».",
        "org_super": "ҚКП басшылығымен; қадағалаушы: Қытай мүгедектігі бар адамдар федерациясы; тіркеу: Азаматтық істер министрлігі.",
        "org_intl": "Lions Clubs International ұйымының корпоративтік мүшесі, сыртқы алмасуларды үйлестіреді.",
        "org_levels": "Құрылымы: Кеңес → Өкілдіктер / Мекеме мүшелері → Қызмет көрсету клубтары.",
        "m_cond": "Шарттары: 20 жастан асқан ҚХР азаматы; Жарғыны қолдау; ерікті мүше болу; қайырымдылыққа ұмтылыс пен ықпал.",
        "m_rights": "Құқықтары: сайлау және сайлану, дауыс беру; қатысу; қызметте басымдық; білу, ұсыныс жасау және бақылау құқығы; еркін кіру/шығу.",
        "m_duty": "Міндеттері: Жарғы/ережелер мен шешімдерді сақтау; құқықтарды қорғау және қатысу; тапсырмаларды орындау; жарна төлеу; кеңес беру; есеп беру.",
        "m_auto": "Автоматты шығу: негізсіз 6 ай қатарынан қатыспау немесе жарна төлемеу → шыққан саналады.",
        "m_expel": "Шығару: заңды бұзу, Жарғыны ауыр бұзу немесе беделге нұқсан келтіру → Кеңес шешімімен шығару.",
        "f_std": FACTS["fee_table"],
        "f_up": FACTS["fee_up"],
        "f_time": FACTS["fee_time"],
        "f_year": FACTS["fee_year"],
        "r1": FACTS["redline"],
        "r2": FACTS["redline_logo"],
        "r3": FACTS["redline_speech"],
        "t1": FACTS["team_setup"],
        "t2": FACTS["team_prep"],
        "t3": FACTS["team_meeting"],
        "t4": FACTS["team_core"],
        "t5": "Қызмет көрсету іс-шаралары капитан тобының бекітуін қажет етеді.",
        "v1": FACTS["vi_logo"],
        "v2": FACTS["vi_color"],
        "v3": FACTS["vi_min"],
        "v4": FACTS["vi_forbid"],
    },
    "uz": {
        "org_nature": "Milliy, birlashgan, notijorat ijtimoiy tashkilot, huquqiy shaxs; shtab-kvartirasi Pekinda.",
        "org_mission": "Missiya: «Oʻzini takomillashtirib, boshqalarga yordam berish va jamiyatga xizmat qilish».",
        "org_super": "KKP rahbarligi ostida; nazorat: Xitoy nogironlar federatsiyasi; roʻyxat: Fuqarolik ishlari vazirligi.",
        "org_intl": "Lions Clubs International korporativ aʼzosi, tashqi almashinuvni muvofiqlashtiradi.",
        "org_levels": "Tuzilma: Kengash → Vakolatxonalar / Muassasa aʼzolari → Xizmat koʻrsatish klublari.",
        "m_cond": "Shartlar: 20 yoshdan oshgan Xitoy fuqarosi; Nizomni qoʻllab-quvvatlash; ixtiyoriy aʼzolik; xayriya va taʼsirga intilish.",
        "m_rights": "Huquqlar: saylash va saylanish, ovoz berish; ishtirok etish; xizmatda ustuvorlik; bilish, taklif qilish va nazorat qilish; erkin kirish/chiqish.",
        "m_duty": "Majburiyatlar: Nizom/qoidalar va qarorlarga rioya qilish; huquqlarni himoya qilish va ishtirok etish; vazifalarni bajarish; badal toʻlash; maslahat berish; hisobot.",
        "m_auto": "Avtomatik chiqish: asossiz 6 oy ketma-ket qatnashmaslik yoki badal toʻlamaslik → chiqqan hisoblanadi.",
        "m_expel": "Chiqqarib yuborish: qonunni buzish, Nizomni ogʻir buzish yoki obroʻga putur yetkazish → Kengash qarori bilan chiqarib yuborish.",
        "f_std": FACTS["fee_table"],
        "f_up": FACTS["fee_up"],
        "f_time": FACTS["fee_time"],
        "f_year": FACTS["fee_year"],
        "r1": FACTS["redline"],
        "r2": FACTS["redline_logo"],
        "r3": FACTS["redline_speech"],
        "t1": FACTS["team_setup"],
        "t2": FACTS["team_prep"],
        "t3": FACTS["team_meeting"],
        "t4": FACTS["team_core"],
        "t5": "Xizmat tadbirlari kapitan jamoasining tasdiqini talab qiladi.",
        "v1": FACTS["vi_logo"],
        "v2": FACTS["vi_color"],
        "v3": FACTS["vi_min"],
        "v4": FACTS["vi_forbid"],
    },
    "sw": {
        "org_nature": "Shirika la kijamii la kitaifa, la pamoja, lisilo la faida, lenye utu wa kisheria; makao yake makuu yako Beijing.",
        "org_mission": "Dhamira: «Jipuuze ili uwasaidie wengine na kutumikia jamii».",
        "org_super": "Chini ya uongozi wa CPC; msimamizi: Shirikisho la Walemavu wa China; usajili: Wizara ya Mambo ya Kiraia.",
        "org_intl": "Mwanachama wa shirika wa Lions Clubs International, inayoratibu ubadilishanaji wa nje.",
        "org_levels": "Muundo: Baraza → Ofisi za Wawakilishi / Wanachama wa Taasisi → Vilabu vya Huduma.",
        "m_cond": "Masharti: raia wa China mwenye umri wa miaka 20+; kuunga mkono Katiba; uanachama wa hiari; kujitolea kwa hisani na ushawishi.",
        "m_rights": "Haki: kuchagua na kuchaguliwa, kupiga kura; kushiriki; kipaumbele cha huduma; haki ya kujua, kupendekeza na kusimamia; uhuru wa kujiunga/kutoka.",
        "m_duty": "Majukumu: kutii Katiba/sheria na maamuzi; kulinda haki na kushiriki; kukamilisha kazi; kulipa ada; kutoa ushauri; kuripoti.",
        "m_auto": "Kujitoa kiotomatiki: miezi 6 mfululizo bila kuhudhuria bila sababu, au kukosa kulipa ada → huzingatiwa amejitoa.",
        "m_expel": "Kufukuzwa: ukiukaji wa sheria, ukiukaji mkubwa wa Katiba, au uharibifu wa sifa → kufukuzwa kwa uamuzi wa Baraza.",
        "f_std": FACTS["fee_table"],
        "f_up": FACTS["fee_up"],
        "f_time": FACTS["fee_time"],
        "f_year": FACTS["fee_year"],
        "r1": FACTS["redline"],
        "r2": FACTS["redline_logo"],
        "r3": FACTS["redline_speech"],
        "t1": FACTS["team_setup"],
        "t2": FACTS["team_prep"],
        "t3": FACTS["team_meeting"],
        "t4": FACTS["team_core"],
        "t5": "Shughuli za huduma zinahitaji idhini ya timu ya nahodha.",
        "v1": FACTS["vi_logo"],
        "v2": FACTS["vi_color"],
        "v3": FACTS["vi_min"],
        "v4": FACTS["vi_forbid"],
    },
}

# zh-Hant: convert Simplified Chinese facts to Traditional (light manual mapping for key terms)
def to_hant(s):
    rep = {
        "中国狮子联会":"中國獅子聯會","服务":"服務","社会":"社會","组织":"組織","成员":"成員","会员":"會員",
        "会费":"會費","财务":"財務","费用":"費用","标准":"標準","规范":"規範","制度":"制度","机构":"機構",
        "代表处":"代表處","单位":"單位","服务队":"服務隊","权利":"權利","义务":"義務","缴纳":"繳納",
        "逾期":"逾期","自动退会":"自動退會","除名":"除名","宗旨":"宗旨","自愿":"自願","公益":"公益",
        "不得":"不得","禁止":"禁止","标识":"標識","商业":"商業","行为准则":"行為準則","章程":"章程",
        "理事会":"理事會","决议":"決議","监督":"監督","事项":"事項","年度":"年度","筹备":"籌備",
        "创队":"創隊","申请人":"申請人","队长":"隊長","团队":"團隊","会议":"會議","视觉":"視覺",
        "形象":"形象","识别":"識別","色彩":"色彩","组合":"組合","安全":"安全","距离":"距離",
        "尺寸":"尺寸","背景":"背景","明度":"明度","禁止":"禁止","外文":"外文","参考":"參考",
        "译本":"譯本","原文":"原文","免责声明":"免責聲明","以中文":"以中文","为准":"為準",
        "正己助人，服务社会":"正己助人，服務社會","热爱祖国":"熱愛祖國","拥护":"擁護","中国公民":"中國公民",
        "年满二十周岁":"年滿二十周歲","连续六个月":"連續六個月","无故":"無故","不参加":"不參加","活动":"活動",
        "不按时足额":"不按時足額","交纳":"交納","经理事会":"經理事會","表决通过":"表決通過","予以除名":"予以除名",
        "取消其会籍":"取消其會籍","入会费":"入會費","年度会费":"年度會費","转队费":"轉隊費","残联委派":"殘聯委派",
        "单位会员":"單位會員","家庭会员":"家庭會員","上缴":"上繳","获准入会":"獲准入會","之日起":"之日起",
        "新会员":"新會員","在籍会员":"在籍會員","每年":"每年","视为":"視為","代表处及":"代表處及",
        "及时":"及時","周期":"週期","次年":"次年","称":"稱","依据":"依據","制定":"制定","办法":"辦法",
        "用途":"用途","用于":"用於","开展":"開展","业务":"業務","支出":"支出","收取":"收取","授权":"授權",
        "各代表处":"各代表處","代收代缴":"代收代繳","方式":"方式","规定":"規定","其余":"其餘","经费":"經費",
        "联会收取":"聯會收取","开具":"開具","合法票据":"合法票據","收支":"收支","接受":"接受","监督公开公布":"監督公開公佈",
        "官网":"官網","解释权":"解釋權","实行":"實行","本法":"本辦法","第七条":"第七條","第八条":"第八條",
    }
    for k,v in rep.items():
        s = s.replace(k,v)
    return s

TITLES["zh-Hant"] = TITLES["zh-Hant"]  # keep

def build():
    for code,(h1,sections) in TITLES.items():
        d = os.path.join(BASE, code)
        os.makedirs(d, exist_ok=True)
        tr = TR.get(code, {})
        lines = []
        lines.append("# %s\n" % h1)
        lines.append("> 制作者：精卫服务队 于海峰 狮兄 ｜ v1.0.0 ｜ 2025-09-28")
        lines.append("> **参考译文辅助版 · 非中国狮子联会官方译本**；以中文官方原件为准。\n")
        # 1 org
        lines.append("## %s" % sections["org"])
        if code == "zh-Hant":
            facts_org = [FACTS["org"], to_hant(FACTS["nature"]), to_hant(FACTS["mission"]),
                         to_hant(FACTS["supervision"]), to_hant(FACTS["intl"]), to_hant(FACTS["levels"])]
        else:
            facts_org = [FACTS["org"], tr.get("org_nature",""), tr.get("org_mission",""),
                         tr.get("org_super",""), tr.get("org_intl",""), tr.get("org_levels","")]
        for f in facts_org:
            if f: lines.append("- %s" % f)
        # 2 member
        lines.append("\n## %s" % sections["member"])
        if code == "zh-Hant":
            facts_m = [to_hant(FACTS["member_cond"]), to_hant(FACTS["member_rights"]), to_hant(FACTS["member_duty"]),
                       to_hant(FACTS["auto_quit"]), to_hant(FACTS["expel"])]
        else:
            facts_m = [tr.get("m_cond",""), tr.get("m_rights",""), tr.get("m_duty",""), tr.get("m_auto",""), tr.get("m_expel","")]
        for f in facts_m:
            if f: lines.append("- %s" % f)
        # 3 fee
        lines.append("\n## %s" % sections["fee"])
        if code == "zh-Hant":
            facts_f = [to_hant(FACTS["fee_table"]), to_hant(FACTS["fee_up"]), to_hant(FACTS["fee_time"]), to_hant(FACTS["fee_year"])]
        else:
            facts_f = [tr.get("f_std",""), tr.get("f_up",""), tr.get("f_time",""), tr.get("f_year","")]
        for f in facts_f:
            if f: lines.append("- %s" % f)
        # 4 redline
        lines.append("\n## %s" % sections["redline"])
        if code == "zh-Hant":
            facts_r = [to_hant(FACTS["redline"]), to_hant(FACTS["redline_logo"]), to_hant(FACTS["redline_speech"])]
        else:
            facts_r = [tr.get("r1",""), tr.get("r2",""), tr.get("r3","")]
        for f in facts_r:
            if f: lines.append("- %s" % f)
        # 5 team
        lines.append("\n## %s" % sections["team"])
        if code == "zh-Hant":
            facts_t = [to_hant(FACTS["team_setup"]), to_hant(FACTS["team_prep"]), to_hant(FACTS["team_meeting"]),
                       to_hant(FACTS["team_core"]), to_hant("Service activities must be approved by the captain's team.")]
        else:
            facts_t = [tr.get("t1",""), tr.get("t2",""), tr.get("t3",""), tr.get("t4",""), tr.get("t5","")]
        for f in facts_t:
            if f: lines.append("- %s" % f)
        # 6 vi
        lines.append("\n## %s" % sections["vi"])
        if code == "zh-Hant":
            facts_v = [to_hant(FACTS["vi_logo"]), to_hant(FACTS["vi_color"]), to_hant(FACTS["vi_min"]), to_hant(FACTS["vi_forbid"])]
        else:
            facts_v = [tr.get("v1",""), tr.get("v2",""), tr.get("v3",""), tr.get("v4","")]
        for f in facts_v:
            if f: lines.append("- %s" % f)
        # 7 disclaimer
        lines.append("\n## %s" % sections["disc"])
        lines.append("- %s" % (to_hant(FACTS["disclaimer"]) if code=="zh-Hant" else FACTS["disclaimer"]))
        lines.append("\n---\n> 完整条款请查阅中文官方原件（`references/`）。本文件为便于理解而译，正式会务以联会官方发布版本为准。")
        with open(os.path.join(d,"summary.md"),"w",encoding="utf-8") as fh:
            fh.write("\n".join(lines)+"\n")
        print("generated", code, "summary.md", len(lines), "lines")

if __name__ == "__main__":
    build()
