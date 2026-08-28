# -*- coding: utf-8 -*-
"""All site text. Used only by build/generate.py to write the static HTML."""

SITE = dict(
    name="GS Net Academy",
    subtitle="UGC NET Paper-I | JRF Preparation | Mentorship",
    mission="JRF @ ₹500 Mission 2026",
    exam_target="December 2026",
    batch_start="16 August 2026",
    class_time="6:30 PM",
    contribution="₹500",
    pdf_price="₹50",
    phones=["9266511505", "9810845327"],
    email="gsnetacademy@gmail.com",
    website="www.gsnetacademy.com",
    google_form="https://docs.google.com/forms/d/e/1FAIpQLSeS-HHg-zO3CdFWh-5tumhJbMlfw6inOA9-ZpqPkdKZkv13Ew/viewform?usp=publish-editor",
    whatsapp_group="https://chat.whatsapp.com/KeaQUhOFz0UGAKtLmsM7oU",
    demo_video="FAgtT33U8RY",
    brochure="",          # e.g. "assets/pdf/brochure.pdf"
    exam_portal="",       # blank = "Coming soon" chip in the navbar
)

NAV = [
    ("UGC NET Paper-I", "courses.html", False),
    ("UG / PG (Paper-2)", "", True),
    ("Tutorials", "tutorials.html", False),
    ("Notes", "notes.html", False),
    ("Blog", "blog.html", False),
    ("About", "about.html", False),
    ("Contact", "contact.html", False),
]

BRAND_EXAMS = "UGC NET | SET | JRF | PH.D. | ASSISTANT PROFESSOR"
DESIGNED_BY = "JNU &amp; DU Expert Faculty Guidance में Designed Course"
STRAPLINE = "We Don't Just Teach. We Build Aspirants."

HERO = dict(
    subtitle="UGC NET PAPER-1 SPECIAL MENTORSHIP + FOUNDATION PROGRAM",
    line1="अब पैसे और सही guidance की कमी JRF के लिए barrier नहीं बनेगी।",
    note="पहले Demo Class देखें → Program समझें → फिर Enrollment का informed decision लें।",
    batch_strip="Classes 16 August 2026 से शुरू — Live + Recorded Support के साथ अभी join करें।",
    highlights=[
        ("cap", "Course Fee", "FREE"),
        ("rupee", "Registration &amp; Academic/Logistics", "₹500 Only"),
        ("clock", "Class Time", "6:30 PM"),
        ("globe", "Platform", "Google Meet"),
        ("target", "Target", "UGC NET/JRF 2026"),
        ("book", "Medium", "Hindi + English"),
    ],
    includes=["Live Classes", "Recorded Sessions", "PDF Notes", "PYQs", "Practice", "Tests", "Mentorship"],
)

FEATURES = [
    ("cap", "Free Course", "Full Paper-I course fee is FREE"),
    ("videocam", "Live Classes", "Daily 6:30 PM on Google Meet"),
    ("refresh", "Recorded Sessions", "Miss a class, watch it later"),
    ("pdf", "PDF Notes", "Unit-wise notes for every topic"),
    ("test", "PYQs &amp; Tests", "Practice questions with tests"),
    ("mentor", "Mentorship", "Guidance till the exam"),
]

APPROACH = [
    ("01", "Concept", "Basic से exam-oriented explanation"),
    ("02", "PYQ", "Question कैसे बनता है, यह समझना"),
    ("03", "Practice", "Topic के तुरंत बाद questions"),
    ("04", "Test", "Unit-wise tests"),
    ("05", "Analysis", "Mistakes की classification"),
    ("06", "Revision", "Continuous process"),
    ("07", "Mentorship", "Direction, planning, consistency"),
]

BATCH = dict(
    heading="Batch Status",
    body="Classes 16 August 2026 से शुरू हो चुकी हैं। यदि आपने शुरुआत miss कर दी है, तो preparation postpone करने की जरूरत नहीं है। Program में Live + Recorded Learning Support रखा गया है ताकि नए students current batch के साथ systematically जुड़ सकें।",
    points=["Structured Paper-1 Foundation", "Regular Live Classes", "Recorded Sessions",
            "Exam-Oriented PDF Notes", "PYQ Discussion &amp; Practice", "Tests, Analysis &amp; Mentorship"],
    cta="JOIN CURRENT BATCH",
)

WHY_JOIN = dict(
    heading="UGC NET/JRF Paper-1 की तैयारी अभी से क्यों शुरू करें?",
    intro="JRF preparation में सबसे common problem syllabus की कमी नहीं, बल्कि systematic preparation की कमी होती है। बहुत से aspirants content consume करते हैं, लेकिन उनके पास fixed learning system, revision cycle और test-analysis process नहीं होता।",
    problems=[
        "Paper-1 को last months के लिए छोड़ देना",
        "अलग-अलग YouTube videos से fragmented preparation करना",
        "Notes collect करना लेकिन revise न करना",
        "PYQs solve करना लेकिन उनका analysis न करना",
        "Mock test देना लेकिन mistakes classify न करना",
        "Paper-2 पर पूरा focus करके Paper-1 को underestimate करना",
        "सही guidance के बिना strategy बार-बार बदलना",
    ],
    booster_heading="Paper-1 को JRF Score Booster बनाइए",
    booster_body="Paper-1 को केवल qualifying paper की तरह पढ़ना पर्याप्त नहीं है। एक well-prepared aspirant Paper-1 में अपनी overall performance को significantly strengthen कर सकता है। हमारा target Paper-1 को weakness से strength में convert करना है।",
    booster_points=["Conceptual clarity", "Question-solving ability", "PYQ understanding",
                    "Accuracy", "Revision", "Test performance"],
    disclaimer="हम किसी fixed score या JRF selection की guarantee नहीं देते। हमारा commitment quality teaching, structured preparation और academic guidance है।",
)

COVERAGE = [
    ("01", "Teaching Aptitude", "Teaching, Objectives, Levels of Teaching, Learner Characteristics, Teaching Methods, Evaluation आदि।"),
    ("02", "Research Aptitude", "Research Types, Methods, Sampling, Hypothesis, Ethics, Research Process आदि।"),
    ("03", "Comprehension", "Reading, Interpretation और Question-solving approach."),
    ("04", "Communication", "Types, Models, Barriers, Classroom Communication और Mass Communication."),
    ("05", "Mathematical Reasoning &amp; Aptitude", "Ratio, Percentage, Average, Time &amp; Work, Series और exam-relevant aptitude."),
    ("06", "Logical Reasoning", "Arguments, Fallacies, Analogy, Indian Logic और reasoning concepts."),
    ("07", "Data Interpretation", "Tables, Graphs, Charts, Percentage और Data-based Questions."),
    ("08", "ICT", "Internet, Digital Initiatives, Communication Technology, Cyber Concepts आदि।"),
    ("09", "People, Development &amp; Environment", "Development, Pollution, Environment, Sustainable Development आदि।"),
    ("10", "Higher Education System", "Institutions, Policies, Governance, Regulatory Bodies और Indian Higher Education."),
]

DIFFERENT = [
    ("1", "Conceptual Clarity", "हर topic को exam-oriented तरीके से basic से समझाया जाएगा ताकि learner केवल definition याद न करे बल्कि concept को identify और apply कर सके।"),
    ("2", "PYQ Intelligence", "Previous Year Questions को केवल solve नहीं किया जाएगा। Question किस concept से बना, distractor कैसे बनाया गया, बाकी options गलत क्यों हैं और इसी concept को नए तरीके से कैसे पूछा जा सकता है—यह approach develop की जाएगी।"),
    ("3", "Exam-Oriented Notes", "Classes के साथ structured bilingual notes दिए जाएंगे जिन्हें student mobile पर आसानी से पढ़ और revise कर सके।"),
    ("4", "Smart Practice", "Topic के बाद relevant questions और practice ताकि concept immediately test हो सके।"),
    ("5", "Test &amp; Analysis", "Mistakes को Concept Error, Memory Error, Calculation Error और Question-Reading Error में identify करने की habit develop की जाएगी।"),
    ("6", "Revision &amp; Recall", "Revision को preparation का अंतिम हिस्सा नहीं बल्कि continuous process माना जाएगा।"),
    ("7", "Mentorship", "Preparation direction, planning, consistency और exam approach पर regular guidance दिया जाएगा।"),
]

DEMO = dict(
    heading="पहले हमारी Teaching Experience कीजिए — फिर Decide कीजिए",
    body="किसी coaching program को केवल poster या advertisement देखकर join नहीं करना चाहिए। पहले Shardool Sir की actual class देखिए।",
    points=["Concepts कैसे explain किए जाते हैं",
            "Hindi-English bilingual approach आपके लिए comfortable है या नहीं",
            "Notes कैसे structured हैं", "PYQs कैसे discuss होते हैं", "Class कितनी exam-oriented है"],
)

FACULTY = dict(
    name="Dr. Shardool Sir",
    photo="assets/images/faculty.jpg",
    credentials=["14+ Years of Teaching &amp; Research Experience",
                 "Ex-Employee, Ministry of Social Justice &amp; Empowerment, Government of India",
                 "M.A. – Jawaharlal Nehru University (JNUEE AIR-1)",
                 "M.Phil. &amp; Ph.D. – University of Delhi",
                 "UGC NET-JRF Qualified"],
    why_heading="Why Learn with Dr. Shardool Sir?",
    why=["Strong academic background from JNU &amp; University of Delhi",
         "Teaching + research-oriented conceptual approach",
         "UGC NET/JRF Paper-1 focused mentoring",
         "Exam-oriented bilingual teaching",
         "Concept clarity + PYQ analysis + practice + revision",
         "Personal guidance for NET, JRF, Assistant Professor &amp; Ph.D. aspirants"],
    quote="हम आपको केवल syllabus complete नहीं कराते—हम आपकी Paper-1 preparation को systematically build करते हैं।",
)

WHY_ACADEMY = dict(
    heading="GS Net Academy क्यों?",
    body="GS Net Academy का focus केवल course sell करना नहीं बल्कि aspirant को structured academic support देना है।",
    formula="RIGHT DIRECTION + CONCEPTUAL CLARITY + PYQ INTELLIGENCE + PRACTICE + TEST + REVISION + MENTORSHIP",
    points=["UGC NET Paper-1 focused preparation", "Bilingual Teaching", "Exam-oriented Notes",
            "Live Interaction", "Recorded Learning Support", "PYQ-based Approach",
            "Regular Practice", "Doubt Support", "Mentorship", "Affordable Learning Opportunity"],
)

WHO = dict(
    join_heading="Who Should Join?",
    join=["December 2026 UGC NET/JRF target करने वाले aspirants",
          "Paper-1 की शुरुआत basic से करना चाहते हैं",
          "पहले Paper-1 पढ़ चुके हैं लेकिन concepts fragmented हैं",
          "YouTube से पढ़ते-पढ़ते structured preparation चाहते हैं",
          "Paper-1 mock score improve करना चाहते हैं",
          "Hindi-English bilingual classes पसंद करते हैं",
          "PYQ + Notes + Practice + Mentorship एक साथ चाहते हैं",
          "कम budget में quality guidance चाहते हैं"],
    not_heading="Who Should Not Join?",
    not_join=["बिना regular study के केवल certificate चाहते हैं",
              "Classes attend/revise करने के लिए समय नहीं देना चाहते",
              "केवल shortcut tricks पर depend करना चाहते हैं",
              "Practice और tests नहीं करना चाहते",
              "Guaranteed JRF जैसी unrealistic promise चाहते हैं"],
)

PROGRAM_ROWS = [
    ("cap", "Program", "UGC NET Paper-1 Special Mentorship Batch"),
    ("target", "Target", "UGC NET/JRF 2026"),
    ("globe", "Mode", "Online"),
    ("videocam", "Platform", "Google Meet"),
    ("clock", "Class Time", "6:30 PM"),
    ("book", "Medium", "Hindi + English"),
    ("layers", "Coverage", "Complete Paper-1"),
    ("refresh", "Support", "Live + Recorded Sessions"),
    ("pdf", "Notes", "PDF Study Material"),
    ("test", "Practice", "PYQ + Questions + Tests"),
    ("mentor", "Mentorship", "Regular Academic Guidance"),
]

FEE = dict(
    heading="COURSE FEE — FREE",
    label="Registration &amp; Academic/Logistics Support Contribution",
    amount="₹500/- ONLY",
    note="यह contribution program की academic और logistics support व्यवस्था के लिए है।",
)

JOIN_STEPS = [
    dict(title="STEP 1 — Registration Form Fill करें",
         body="Google Registration Form में अपनी basic details भरें और ₹500 Registration &amp; Academic/Logistics Contribution का payment proof upload करें।",
         cta="OPEN GOOGLE REGISTRATION FORM", points=[]),
    dict(title="STEP 2 — Join Class Community",
         body="Verification के बाद student को GS Net Academy की official class community में add किया जाएगा।",
         cta="", points=["Google Meet Class Link", "PDF Notes", "Class Updates",
                         "Recorded Session Information", "Test Information", "Mentorship Updates"]),
]

FORM_FIELDS = [
    "Full Name", "Mobile Number / WhatsApp Number", "Email ID", "UGC NET Subject",
    "Target Exam: NET / JRF / Assistant Professor / Ph.D. Entrance",
    "Attempt: First Attempt / Previous Attempt",
    "Current Paper-1 Preparation Level: Beginner / Basic Done / PYQ Practising / Mock-Test Stage",
    "How did you hear about GS Net Academy? YouTube / Instagram / Facebook / Google / Friend / WhatsApp / Other",
    "Payment Transaction ID", "Payment Screenshot Upload",
    "Declaration: मैं GS Net Academy के academic instructions और class discipline को follow करने के लिए सहमत हूँ।",
]

JOURNEY = ["JOIN", "ORIENTATION", "CONCEPT CLASSES", "NOTES", "PYQs", "PRACTICE",
           "UNIT TEST", "MISTAKE ANALYSIS", "REVISION", "MOCK TEST", "MENTORSHIP",
           "JRF-ORIENTED PREPARATION"]

FAQS = [
    ("क्या ₹500 में पूरा Paper-1 पढ़ाया जाएगा?", "Program UGC NET Paper-1 की structured foundation और mentorship preparation के लिए बनाया गया है। Complete coverage और schedule brochure में दिया जाएगा।"),
    ("Course Fee FREE क्यों रखा गया है?", "JRF@500 को affordable academic initiative की तरह design किया गया है। Course fee free रखी गई है और ₹500 registration तथा academic/logistics support contribution लिया जा रहा है।"),
    ("Classes कहाँ होंगी?", "Classes online Google Meet पर आयोजित की जाएंगी।"),
    ("Class का medium क्या रहेगा?", "Teaching bilingual होगी — Hindi + English।"),
    ("अगर कोई class miss हो जाए तो?", "Program में live classes के साथ recorded learning support भी रखा गया है। Availability और access rules batch instructions के अनुसार रहेंगे।"),
    ("क्या Notes मिलेंगे?", "हाँ। Topics के लिए exam-oriented PDF notes और relevant learning material share किया जाएगा।"),
    ("क्या PYQs भी होंगे?", "हाँ। PYQs program का core हिस्सा होंगे और concept के साथ analyse किए जाएंगे।"),
    ("क्या tests होंगे?", "हाँ। Unit-wise practice और tests preparation process में शामिल होंगे।"),
    ("क्या doubts पूछ सकते हैं?", "Regular doubt support और mentorship program का हिस्सा है।"),
    ("क्या JRF Selection Guarantee है?", "नहीं। JRF/NET qualification कई factors और candidate की performance पर निर्भर करती है। GS Net Academy quality teaching, notes, PYQ practice, test preparation और mentorship प्रदान करता है—selection guarantee नहीं।"),
    ("क्या batch अभी join कर सकते हैं?", "Admissions open रहने तक current batch join किया जा सकता है।"),
]

FINAL_CTA = dict(
    heading="JRF का सपना बड़ा है। Preparation भी systematic होनी चाहिए।",
    body="अगर आप UGC NET/JRF Paper-1 को सही direction, conceptual clarity, PYQ intelligence, practice, revision और mentorship के साथ तैयार करना चाहते हैं—",
    join="Join GS Net Academy's Paper-1 Special Mentorship Program",
)

RESULTS = [
    ("netjrf", "NET / JRF Qualified", ["01-shubham-rana.jpg", "02-pawan.jpg", "03-neha-upadhayay.jpg",
                                       "04-arti-vats.jpg", "05-lali-kumari.jpg"]),
    ("phd", "Ph.D Admission &amp; Research", ["01-kanhaiya.jpg", "02-sonali.jpg", "03-kanhaiya-lal.jpg",
                                              "04-sunita.jpg", "05-sachin.jpg", "06-anjula-yadav.jpg",
                                              "07-meenakshi.jpg", "08-sikha-gaur.jpg", "09-sarita.jpg",
                                              "10-deepak-kumar.jpg", "11-chanchal-bhagat.jpg"]),
    ("teacher", "Teacher &amp; Assistant Professor", []),
]

UNITS = [
    (1, "Teaching Aptitude", "cap", "Nature, objectives, methods and evaluation of teaching."),
    (2, "Research Aptitude", "flask", "Research types, methods, steps, ethics and thesis writing."),
    (3, "Comprehension", "book", "Passage reading strategy, speed, accuracy and elimination."),
    (4, "Communication", "megaphone", "Types, barriers, classroom and mass-media communication."),
    (5, "Mathematical Reasoning &amp; Aptitude", "chart", "Series, codes, relationships and numerical aptitude."),
    (6, "Logical Reasoning", "search", "Arguments, deduction, induction, Venn diagrams, Indian logic."),
    (7, "Data Interpretation", "signal", "Data sources, graphs, tables, mapping and DI practice."),
    (8, "Information &amp; Communication Technology", "settings", "ICT basics, internet, digital initiatives in higher education."),
    (9, "People, Development &amp; Environment", "globe", "Development, pollution, hazards, energy and policies."),
    (10, "Higher Education System", "layers", "Indian higher education, governance, policies and value education."),
]

MODULES = {
    1: ["Teaching: Concept, Objectives &amp; Characteristics", "Learner Characteristics &amp; Factors Affecting Teaching", "Methods of Teaching &amp; Teaching Support System", "Evaluation Systems: Types, Elements &amp; Innovations"],
    2: ["Meaning, Types &amp; Characteristics of Research", "Research Methods &amp; Steps of Research", "Thesis, Article Writing &amp; Reference Styles", "Research Ethics &amp; Application of ICT in Research"],
    3: ["How to Read a Passage: Strategy &amp; Speed", "Question Types in Comprehension", "Option Elimination &amp; Common Traps", "Practice Set with Solved Explanations"],
    4: ["Communication: Meaning, Types &amp; Characteristics", "Effective Communication &amp; Barriers", "Classroom Communication &amp; Group Dynamics", "Mass Media, ICT &amp; Modern Communication"],
    5: ["Number &amp; Letter Series", "Codes, Relationships &amp; Classification", "Number System &amp; Basic Arithmetic", "Practice: Mathematical Aptitude PYQs"],
    6: ["Structure of Arguments &amp; Forms of Reasoning", "Deductive &amp; Inductive Reasoning", "Analogies, Venn Diagrams &amp; Syllogism", "Indian Logic: Pramanas &amp; Fallacies"],
    7: ["Sources &amp; Types of Data", "Tables, Bar Graphs &amp; Pie Charts", "Data Mapping &amp; Interpretation", "Practice: DI Question Sets"],
    8: ["ICT: Basics, Terms &amp; Abbreviations", "Internet, Email &amp; Digital Communication", "Digital Initiatives in Higher Education", "Cyber Security &amp; Emerging Technology"],
    9: ["Development &amp; Environment: Key Concepts", "Pollution: Types, Causes &amp; Control", "Natural Hazards &amp; Disaster Management", "Energy Resources, Policies &amp; Programmes"],
    10: ["Evolution of Indian Higher Education", "Institutions &amp; Regulatory Bodies", "Policies, Governance &amp; Administration", "Value Education &amp; Environmental Education"],
}

COURSES = [
    ("live", "cap", "courses.html#paper-1", "UGC NET Paper 1", "Foundation Program", "",
     "Complete Paper-I preparation — all 10 units with concept classes, PYQ analysis, practice and revision.",
     ["10 units · 50 questions", "Concept + PYQ + practice", "Notes, PDFs and tests", "Live mentorship"]),
    ("live", "trophy", "enroll.html", "UGC NET / JRF Preparation", "JRF @ ₹500 Mission 2026", "",
     "Open mentorship programme built around a JRF-focused approach, not just qualifying the exam.",
     ["Target December 2026", "Course fee FREE", "₹500 logistics contribution", "Daily live class"]),
    ("soon", "layers", "", "UG / PG (Paper-2)", "Subject paper", "",
     "A dedicated Paper-2 subject track from GS Net Academy. Details will be announced soon.",
     ["Subject-wise coverage", "Concept-first teaching", "Practice and tests", "Mentorship"]),
    ("soon", "spark", "", "Career Guidance", "AI-Powered Career Guidance", "AI-Powered",
     "Personalised guidance for NET, JRF, Ph.D. and teaching aspirants. Coming soon.",
     ["Personalised study plans", "Subject and career mapping", "Doubt support", "Progress guidance"]),
]

EXAM_PATTERN = [
    ("Paper-I (General Paper)", "50", "100", "Teaching &amp; Research Aptitude + General Aptitude", False),
    ("Paper-II (Subject Paper)", "100", "200", "Subject Specific", False),
    ("Total", "150", "300", "JRF / Assistant Professor Eligibility", True),
]

EXAM_FACTS = [
    ("clock", "Duration", "3 Hours (180 min)"),
    ("globe", "Mode", "Computer Based Test"),
    ("check", "Marking", "+2 per correct answer"),
    ("shield", "Negative Marking", "None"),
]
