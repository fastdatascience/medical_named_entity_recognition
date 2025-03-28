'''
MIT License

Copyright (c) 2023 Fast Data Science Ltd (https://fastdatascience.com)

Maintainer: Thomas Wood

Tutorial at https://fastdatascience.com/drug-named-entity-recognition-python-library/

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

diseases_to_exclude_under_all_variants = {
    "syndrome",
    "disease",
    "death",
    "sleep",
    "behavior",
    "consciousness",
    "appetite",
    "data display",
    "adjustment",
    "speech",
    "language",
    "ability",
    "comprehension",
    "lying",
    "household",
    "respect",
    "thinking",
    "norm",
    "character",
    "orientation",
    "attention",
    "association",
    "perception",
    "gender",
    "power",
    "association",
    "habit",
    "self",
    "relatives",
    "family members",
    "separated",
    "feeling",
    "ery",
    "hearing",
    "illiteracy",
    "opinion",
    "emergency"
}

extra_terms_to_exclude_from_disease_dictionary = {
    "ability",
    "abreaction",
    "absenteeism",
    "acceptance process",
    "accomplishment",
    "accountability",
    "ache",
    "achievement",
    "active learning",
    "adaptive behavior",
    "adjustment",
    "adolescent behavior",
    "adolescent development",
    "adolescent father",
    "adolescent fatherhood",
    "adolescent psychiatry",
    "adolescent psychology",
    "adult daughter",
    "adult offspring",
    "adult son",
    "adult sons",
    "adultery",
    "aesthetics",
    "affect",
    "affective symptom",
    "afterimage",
    "age discrimination",
    "aggression",
    "agonistic behavior",
    "alarm fatigue",
    "alcohol abstinence",
    "alcohol consumption",
    "alcohol drinking",
    "alcoholism",
    "alpha feedback",
    "altruism",
    "ambidexterity",
    "anal stage",
    "anesthesia refusal",
    "anger",
    "anger management",
    "angers",
    "angst",
    "animal behavior",
    "animal communication",
    "animal dispersal",
    "animal distribution",
    "animal grazing",
    "animal hypnosis",
    "animal migration",
    "animal singing",
    "animal vocalization",
    "anniversary reaction",
    "anthropology",
    "anti semitism",
    "anticipatory coping",
    "apathy",
    "appetite",
    "appetite alteration",
    "appetitive behavior",
    "applied psychology",
    "approach behavior",
    "approach coping",
    "aptitude",
    "aptitude test",
    "arbitration",
    "arc",
    "aroma therapy",
    "arousal",
    "arson",
    "art therapy",
    "artistic creativity",
    "assertiveness",
    "association",
    "association learning",
    "attention",
    "attention focus",
    "attentional bias",
    "attentional blink",
    "attentional blinks",
    "attitude",
    "audio feedback",
    "audition",
    "auditory illusion",
    "auditory inattention",
    "auditory localization",
    "auditory perception",
    "auditory threshold",
    "authoritarianism",
    "autism",
    "autobiographical memory",
    "autohypnosis",
    "autokinetic effect",
    "autokinetic effects",
    "autokinetic illusion",
    "automatism",
    "autosuggestion",
    "autotomy animal",
    "aversion behavior",
    "aversion learning",
    "aversion therapy",
    "aversive behavior",
    "aversive learning",
    "aversive therapy",
    "avoidance behavior",
    "avoidance learning",
    "awareness",
    "beauty",
    "behavior",
    "behavior control",
    "behavior modification",
    "behavior observation",
    "behavior therapy",
    "behavioral control",
    "behavioral coping",
    "behavioral economics",
    "behavioral laterality",
    "behavioral manipulation",
    "behavioral medicine",
    "behavioral observation",
    "behavioral research",
    "behavioral science",
    "behavioral symptom",
    "behavioral test",
    "behaviorism",
    "bereavement",
    "betrayal",
    "bewilderment",
    "bibliotherapy",
    "binocular disparity",
    "binocular vision",
    "birth order",
    "bisexuality",
    "blushing",
    "body identity",
    "body language",
    "body rocking",
    "body schema",
    "bone conduction",
    "borderline schizophrenia",
    "boredom",
    "bottle feeding",
    "brain reserve",
    "bravery",
    "breakfast skipping",
    "breakthrough pain",
    "breast fed",
    "breast feeding",
    "breastfeeding",
    "brief advice",
    "brief intervention",
    "brief psychotherapy",
    "brief treatment",
    "brother",
    "bullying",
    "cannabis smoking",
    "cannibalism",
    "cantab",
    "care burden",
    "career choice",
    "castration anxiety",
    "castration complex",
    "catastrophic thinking",
    "catharsis",
    "celibacy",
    "cerebral dominance",
    "ceremonial behavior",
    "character",
    "chemotaxis",
    "child behavior",
    "child development",
    "child guidance",
    "child language",
    "choice behavior",
    "chromotherapy",
    "clairvoyance",
    "client adherence",
    "client compliance",
    "clinical hypnosis",
    "clinical psychology",
    "clock test",
    "cocaine smoking",
    "cognition",
    "cognition therapy",
    "cognitive coping",
    "cognitive dissonance",
    "cognitive exhaustion",
    "cognitive function",
    "cognitive manifestation",
    "cognitive orientation",
    "cognitive psychology",
    "cognitive psychotherapy",
    "cognitive reflection",
    "cognitive reserve",
    "cognitive rumination",
    "cognitive science",
    "cognitive symptom",
    "cognitive therapy",
    "cognitive weariness",
    "coherence sense",
    "coital frequency",
    "coitus",
    "collective behavior",
    "collective efficacy",
    "color perception",
    "color therapy",
    "color vision",
    "commercial sex",
    "communication",
    "communication program",
    "communication research",
    "community psychiatry",
    "community sense",
    "compass orientation",
    "compassion",
    "competence",
    "competitive behavior",
    "compliant behavior",
    "comprehension",
    "concept acquisition",
    "concept formation",
    "concept learning",
    "conceptualization",
    "conditioned reflex",
    "confidentiality",
    "conflict resolution",
    "confusion",
    "conscience",
    "consciousness",
    "consensual union",
    "consensus",
    "consensus development",
    "constructive coping",
    "constructive feedback",
    "consumer behavior",
    "consumer preference",
    "consumer satisfaction",
    "consummatory behavior",
    "contempt",
    "contour perception",
    "contraception behavior",
    "contraceptive behavior",
    "contraceptive usage",
    "contrast sensitivity",
    "control locus",
    "convulsive therapy",
    "coping behavior",
    "coping skill",
    "coping strategy",
    "coping technique",
    "copulation",
    "core balance",
    "core stability",
    "corpse",
    "cortical vigilance",
    "countertransference",
    "couple therapy",
    "courage",
    "courtship",
    "covert racism",
    "craving",
    "creative ability",
    "creative thinking",
    "creativeness",
    "creativity",
    "credit assignment",
    "criminal behavior",
    "criminal conduct",
    "criminal intent",
    "criminal psychology",
    "criminal recidivism",
    "criminality",
    "crisis intervention",
    "critical thinking",
    "crying",
    "cue",
    "cultural psychiatry",
    "curiosity",
    "currently married",
    "dance therapy",
    "dangerous behavior",
    "dangerousness",
    "data display",
    "daughter",
    "day dream",
    "daydream",
    "daylight vision",
    "deadline pressure",
    "death feigning",
    "deception",
    "decision making",
    "deep sleep",
    "deferred gratification",
    "dehumanization",
    "delirium",
    "delta sleep",
    "delusion",
    "dementia",
    "demoralization",
    "dependency burden",
    "depersonalization",
    "depression",
    "depth perception",
    "developmental psychology",
    "deviant behavior",
    "dialect",
    "diet habit",
    "dietary habit",
    "difference limen",
    "differential threshold",
    "dignity",
    "dignity psychotherapy",
    "dignity therapy",
    "diplomacy",
    "disability discrimination",
    "disclosure",
    "discrimination exposure",
    "discrimination learning",
    "discriminative learning",
    "discriminatory practice",
    "disgust",
    "disorientation",
    "dispute",
    "disruptive behavior",
    "dissent",
    "dissociation",
    "distance discrimination",
    "distance perception",
    "divorce",
    "domestic partner",
    "dominance hierarchy",
    "dominance subordination",
    "dowry",
    "drama therapy",
    "dream",
    "drive",
    "drug adherence",
    "drug compliance",
    "drunk driving",
    "drunken driving",
    "drunkenness",
    "dyslexia",
    "e therapy",
    "early awakening",
    "eating behavior",
    "economic burden",
    "economic hardship",
    "educational psychology",
    "efficiency",
    "ego",
    "egocentricity",
    "egocentrism",
    "eidetic imagery",
    "electroshock",
    "electroshock therapy",
    "eliminative behavior",
    "embarrassment",
    "emergence agitation",
    "emergence excitement",
    "emmetropia",
    "emotion",
    "emotion regulation",
    "emotional adaptation",
    "emotional adjustment",
    "emotional bond",
    "emotional intelligence",
    "emotional regulation",
    "empathy",
    "empowerment",
    "encounter group",
    "engineering psychology",
    "enjoyment",
    "entoptic phenomena",
    "entoptic phenomenon",
    "entoptic vision",
    "environmental psychology",
    "envy",
    "episodic memory",
    "error disclosure",
    "escape reaction",
    "ethanol abstinence",
    "ethnopsychology",
    "ethology",
    "euphoria",
    "ever married",
    "everyday racism",
    "exam stress",
    "exceptional child",
    "exclusive breastfeeding",
    "executive control",
    "executive function",
    "existential psychology",
    "existentialism",
    "expectation",
    "experience sampling",
    "experiential learning",
    "experimental psychology",
    "exploratory behavior",
    "exposure therapy",
    "expressed emotion",
    "extended family",
    "extended household",
    "extrasensory perception",
    "extraversion",
    "extroversion",
    "face expression",
    "face perception",
    "face recognition",
    "facial expression",
    "facial recognition",
    "fake news",
    "false allegation",
    "familiarity",
    "family",
    "family assistance",
    "family characteristic",
    "family conflict",
    "family demography",
    "family dynamic",
    "family dynamics",
    "family encouragement",
    "family member",
    "family relation",
    "family relationship",
    "family research",
    "family separation",
    "family size",
    "family sizes",
    "family structure",
    "family support",
    "family therapy",
    "fantasy",
    "farsightedness",
    "fasting",
    "fatal attempt",
    "fatal suicide",
    "father",
    "fear",
    "feeding behavior",
    "feeding pattern",
    "feeling",
    "female homosexuality",
    "femininity",
    "figural aftereffect",
    "filiation",
    "financial burden",
    "financial challenge",
    "financial contribution",
    "financial disclosure",
    "financial gift",
    "financial hardship",
    "financial pressure",
    "financial strain",
    "financial stress",
    "financial toxicity",
    "finger sucking",
    "first birth",
    "first intercourse",
    "fixation disparity",
    "flicker fusion",
    "flight reaction",
    "flooding therapy",
    "food fussiness",
    "food habit",
    "food preference",
    "food selection",
    "forensic psychiatry",
    "forensic psychology",
    "forgiveness",
    "formative feedback",
    "free association",
    "free will",
    "freudian theory",
    "frigidity",
    "frustration",
    "fugue",
    "functional laterality",
    "future generation",
    "gambling",
    "garden therapy",
    "gardening therapy",
    "gender",
    "gender bias",
    "gender discrimination",
    "gender identity",
    "gender role",
    "generation gap",
    "genetic determinism",
    "gestalt theory",
    "gestalt therapy",
    "gestational carrier",
    "gestational mother",
    "gesture",
    "gift giving",
    "gifted adolescent",
    "gifted child",
    "gladness",
    "glue sniffing",
    "goal",
    "grandfather",
    "grandmother",
    "grandparent",
    "gratification",
    "grief",
    "group behavior",
    "group cohesion",
    "group cohesiveness",
    "group dynamic",
    "group dynamics",
    "group identification",
    "group interaction",
    "group meeting",
    "group potency",
    "group pressure",
    "group process",
    "group psychotherapy",
    "group solidarity",
    "group structure",
    "group therapy",
    "group thinking",
    "growth opportunity",
    "guilt",
    "gustation",
    "gustatory perception",
    "gustatory response",
    "habit",
    "hallucination",
    "handedness",
    "happiness",
    "haptic communication",
    "haptic perception",
    "harm minimization",
    "harm reduction",
    "hashish smoking",
    "hate",
    "hazardous behavior",
    "head banging",
    "health attitude",
    "health behavior",
    "healthy adaptation",
    "healthy diet",
    "healthy eating",
    "healthy nutrition",
    "hearing",
    "heat avoidance",
    "helping behavior",
    "herbal smoking",
    "herbivore",
    "heroism",
    "heterosexual",
    "heterosexuality",
    "heuristic",
    "hiccup",
    "hidden bias",
    "hidden grief",
    "historic trauma",
    "historical trauma",
    "hoarding",
    "hoax",
    "home range",
    "homesickness",
    "homosexuality",
    "hope",
    "hopefulness",
    "horticultural therapy",
    "horticulture therapy",
    "host mother",
    "hostility",
    "household",
    "household head",
    "housing discrimination",
    "human characteristic",
    "human development",
    "human engineering",
    "human nature",
    "humanitarianism",
    "hunger",
    "husband",
    "hypersomnia",
    "hypnagogic hallucination",
    "hypnoanalysis",
    "hypnosis",
    "hypnotherapy",
    "hypnotism",
    "hypomania",
    "hysteria",
    "identity crises",
    "identity crisis",
    "identity recognition",
    "idiocy",
    "illegal behavior",
    "illicit behavior",
    "illiteracy",
    "illness behavior",
    "illusion",
    "imagery psychotherapy",
    "imaginal flooding",
    "imagination",
    "imitative behavior",
    "immediate memory",
    "immediate recall",
    "implicit bias",
    "implosive therapy",
    "impotence",
    "inadequate personality",
    "incentive",
    "incivility",
    "individual difference",
    "individuality",
    "individuation",
    "industrial psychology",
    "infant behavior",
    "infant development",
    "infant psychology",
    "information avoidance",
    "information denial",
    "information disclosure",
    "information display",
    "innate behavior",
    "insanity defense",
    "insomnia",
    "instinct",
    "institutional racism",
    "instrumental learning",
    "intelligence",
    "intelligence test",
    "intention",
    "intermarriage",
    "intermittent fasting",
    "interparental conflict",
    "interpersonal psychotherapy",
    "interpersonal relation",
    "interpersonal skill",
    "intersectional framework",
    "introversion",
    "intuition",
    "irritable mood",
    "jealousy",
    "job control",
    "job demand",
    "job satisfaction",
    "joy",
    "judgment",
    "kinesics",
    "kinesis",
    "kinesthetic illusion",
    "kinesthetic sense",
    "kinship network",
    "language",
    "language acquisition",
    "language development",
    "language test",
    "laughter",
    "leadership",
    "learned helplessness",
    "learning",
    "learning curve",
    "learning disturbance",
    "learning transfer",
    "lesbianism",
    "lethargy",
    "libido",
    "lie detection",
    "life course",
    "life crises",
    "life crisis",
    "life experience",
    "life satisfaction",
    "life stress",
    "life style",
    "listening effort",
    "literacy",
    "lobotomy",
    "lockjaw",
    "loneliness",
    "loudness perception",
    "love",
    "lying",
    "machiavellianism",
    "male homosexuality",
    "mans role",
    "manual communication",
    "marijuana use",
    "marital conflict",
    "marital relationship",
    "marital status",
    "marital therapy",
    "marriage",
    "marriage age",
    "marriage consummation",
    "marriage duration",
    "marriage pattern",
    "marriage postponement",
    "marriage therapy",
    "married person",
    "masculinity",
    "masochism",
    "mass behavior",
    "mass gathering",
    "masturbation",
    "mate selection",
    "maternal behavior",
    "maternal deprivation",
    "matriarchy",
    "maze learning",
    "maze test",
    "meal skipping",
    "media exposure",
    "mediating",
    "mediation",
    "medical etiquette",
    "medical sociology",
    "medication adherence",
    "medication compliance",
    "medication nonadherence",
    "medication noncompliance",
    "medication persistence",
    "meditation",
    "memory",
    "memory consolidation",
    "mental competence",
    "mental competency",
    "mental fog",
    "mental growth",
    "mental hygiene",
    "mental orientation",
    "mental recall",
    "merycism",
    "mesmerism",
    "mesopic vision",
    "meta cognition",
    "meta emotion",
    "meta memory",
    "migratory pain",
    "milieu therapy",
    "military family",
    "mindfulness",
    "mirror writing",
    "misinformation",
    "monocular vision",
    "mood",
    "moral claim",
    "moral development",
    "moral duty",
    "moral obligation",
    "moral status",
    "morale",
    "morality",
    "morals",
    "moro reflex",
    "mother",
    "motion perception",
    "motivation",
    "motor activity",
    "motor skill",
    "mourning",
    "movement perception",
    "movement sensation",
    "multiple psychotherapy",
    "muscle soreness",
    "music therapy",
    "narcissism",
    "narcosynthesis",
    "narcotherapy",
    "narration",
    "narrative ethics",
    "narrative medicine",
    "narrative therapy",
    "nature therapy",
    "negative reinforcement",
    "negative thinking",
    "negativism",
    "negotiation",
    "nervousness",
    "nest leaving",
    "neuropsychiatry",
    "neuropsychology",
    "neuroticism trait",
    "night vision",
    "nightmare",
    "nonsexual harassment",
    "nonverbal communication",
    "norm",
    "nuclear family",
    "nuptiality",
    "obesity bias",
    "object relation",
    "object relationship",
    "obsession",
    "ocular disparity",
    "ocular parallax",
    "ocular vision",
    "oedipus complex",
    "olfaction",
    "olfactory perception",
    "only child",
    "opinion",
    "optic flow",
    "optical flow",
    "optical illusion",
    "optimism",
    "oral character",
    "oral phase",
    "oral sex",
    "oral stage",
    "organizational behavior",
    "organizational dynamic",
    "organizational dynamics",
    "organoleptic",
    "orgasm",
    "orientation",
    "originality",
    "orthopsychiatry",
    "ostracism",
    "outpatient commitment",
    "pain",
    "pain perception",
    "pain threshold",
    "pair bond",
    "paradoxical sleep",
    "parapsychology",
    "parent",
    "parental age",
    "parenthood status",
    "partner communication",
    "pastoral psychology",
    "paternal behavior",
    "paternal deprivation",
    "paternalism",
    "patient activation",
    "patient adherence",
    "patient compliance",
    "patient dropout",
    "patient elopement",
    "patient empowerment",
    "patient engagement",
    "patient involvement",
    "patient nonadherence",
    "patient noncompliance",
    "patient participation",
    "patient preference",
    "patient satisfaction",
    "patriarchy",
    "pederasty",
    "pediatric psychology",
    "peer group",
    "peer influence",
    "peer pressure",
    "peer review",
    "perception",
    "perceptual closure",
    "perceptual defense",
    "perceptual distortion",
    "perceptual psychology",
    "perfectionism",
    "permissiveness",
    "personal autonomy",
    "personal communication",
    "personal power",
    "personal respect",
    "personal satisfaction",
    "personal space",
    "personality",
    "personality assessment",
    "personality development",
    "personality inventory",
    "pessimism",
    "pet therapy",
    "phallic stage",
    "pharyngeal reflex",
    "phosphene",
    "photographic memory",
    "photokinesis",
    "photopic vision",
    "physical inactivity",
    "physical suffering",
    "physician role",
    "physiological psychology",
    "picky eating",
    "piloerection",
    "pipe smoking",
    "pitch discrimination",
    "pitch perception",
    "play therapy",
    "pleasure",
    "political dissent",
    "polygamy",
    "polygyny",
    "position sense",
    "positive adaptation",
    "positive psychology",
    "positive reinforcement",
    "postanesthetic excitement",
    "posttraumatic growth",
    "postural balance",
    "postural control",
    "postural equilibrium",
    "posture balance",
    "posture control",
    "posture equilibrium",
    "posture sense",
    "power",
    "practice community",
    "practice scope",
    "predation",
    "predatory behavior",
    "prejudice",
    "preventive psychiatry",
    "primary coping",
    "privileged communication",
    "probability learning",
    "problem behavior",
    "procrastination",
    "productivity",
    "professional identification",
    "professional power",
    "professional role",
    "progressive relaxation",
    "projection",
    "projective technic",
    "projective technics",
    "projective technique",
    "proprioception",
    "proprioceptive feedback",
    "prospective memory",
    "prostitution",
    "prudent diet",
    "pseudodementia",
    "psychiatric jurisprudence",
    "psychiatry",
    "psychic research",
    "psychical research",
    "psychoanalysis",
    "psychoanalytic interpretation",
    "psychoanalytic theory",
    "psychoanalytical interpretation",
    "psychoanalytical theory",
    "psychoanalytical therapy",
    "psychodrama",
    "psychodynamic analyses",
    "psychodynamic analysis",
    "psychodynamic assessment",
    "psychodynamic psychotherapy",
    "psychogalvanic reflex",
    "psychogenetics",
    "psychologic adaptation",
    "psychologic desensitization",
    "psychologic interview",
    "psychologic manipulation",
    "psychologic technic",
    "psychologic technics",
    "psychologic technique",
    "psychologic test",
    "psychologic theory",
    "psychological adaptation",
    "psychological adjustment",
    "psychological anticipation",
    "psychological aspiration",
    "psychological bonding",
    "psychological conflict",
    "psychological denial",
    "psychological desensitization",
    "psychological discrimination",
    "psychological displacement",
    "psychological distance",
    "psychological extinction",
    "psychological extraversion",
    "psychological extroversion",
    "psychological factor",
    "psychological feedback",
    "psychological generalization",
    "psychological growth",
    "psychological handling",
    "psychological identification",
    "psychological inhibition",
    "psychological intervention",
    "psychological interview",
    "psychological introversion",
    "psychological manipulation",
    "psychological orientation",
    "psychological phenomena",
    "psychological power",
    "psychological practice",
    "psychological recognition",
    "psychological recovery",
    "psychological reinforcement",
    "psychological rejection",
    "psychological resilience",
    "psychological resiliency",
    "psychological retention",
    "psychological safety",
    "psychological set",
    "psychological stress",
    "psychological sublimation",
    "psychological technic",
    "psychological technics",
    "psychological technique",
    "psychological test",
    "psychological theory",
    "psychological transference",
    "psychological unconscious",
    "psychological wellness",
    "psychologist",
    "psychology",
    "psychology extraversion",
    "psychology generalization",
    "psychology handling",
    "psychology identification",
    "psychology inhibition",
    "psychology introversion",
    "psychology practice",
    "psychology recognition",
    "psychology regression",
    "psychology reinforcement",
    "psychology rejection",
    "psychology repression",
    "psychology retention",
    "psychology set",
    "psychology transfer",
    "psychology transference",
    "psychology unconscious",
    "psychometric",
    "psychometrics",
    "psychomotor performance",
    "psychomotor speed",
    "psychophysic",
    "psychophysics",
    "psychophysiologic feedback",
    "psychophysiologic habituation",
    "psychophysiological habituation",
    "psychophysiology",
    "psychosexual development",
    "psychosocial factor",
    "psychosocial intervention",
    "psychosomatic assessment",
    "psychosurgery",
    "psychotherapeutic process",
    "psychotherapy",
    "psychotherapy imagery",
    "public demonstration",
    "public speaking",
    "punishment",
    "pyromania",
    "q sort",
    "racial bias",
    "racial discrimination",
    "racial prejudice",
    "racism",
    "rage",
    "rational psychotherapy",
    "rationalization",
    "raven test",
    "reaction time",
    "reaction times",
    "reactive confusion",
    "reactive inhibition",
    "readability",
    "reality testing",
    "reality therapy",
    "recidivism",
    "recontact",
    "red s",
    "reflection process",
    "reflective practice",
    "reflective thinking",
    "reflex",
    "regret",
    "reinforcement schedule",
    "relaxation technic",
    "relaxation technics",
    "relaxation technique",
    "relaxation therapy",
    "remarriage",
    "remedial teaching",
    "remote memory",
    "repetition priming",
    "repressed memory",
    "repression",
    "repression sensitization",
    "reproductive behavior",
    "residential treatment",
    "resilience",
    "resiliency",
    "respect",
    "response generalization",
    "response latency",
    "response speed",
    "response time",
    "response times",
    "responsible sex",
    "restlessness",
    "retinal disparity",
    "reversal learning",
    "revulsion",
    "reward",
    "risk behavior",
    "risk reduction",
    "road rage",
    "rod vision",
    "role",
    "role concept",
    "role conflict",
    "role strain",
    "rudeness",
    "sadism",
    "sadness",
    "satiation",
    "satiety response",
    "satisfaction",
    "schema therapy",
    "schizophrenic language",
    "school dropout",
    "scotopic vision",
    "searching behavior",
    "secrecy",
    "sedentary behavior",
    "sedentary time",
    "selective attention",
    "self",
    "self appraisal",
    "self assessment",
    "self compassion",
    "self concept",
    "self confidence",
    "self control",
    "self criticism",
    "self determination",
    "self disclosure",
    "self efficacy",
    "self esteem",
    "self evaluation",
    "self examination",
    "self forgiveness",
    "self hypnosis",
    "self perception",
    "self regulation",
    "self stimulation",
    "semantic differential",
    "semiconsciousness",
    "sensation",
    "sensorimotor feedback",
    "sensory deprivation",
    "sensory feedback",
    "sensory function",
    "sensory threshold",
    "sentiment",
    "separation",
    "serial learning",
    "sex abstinence",
    "sex behavior",
    "sex bias",
    "sex deviation",
    "sex discrimination",
    "sex education",
    "sex industry",
    "sex orientation",
    "sex role",
    "sex work",
    "sexology",
    "sexual abstinence",
    "sexual activity",
    "sexual arousal",
    "sexual behavior",
    "sexual discrimination",
    "sexual excitement",
    "sexual gratification",
    "sexual harassment",
    "sexual intercourse",
    "sexual masochism",
    "sexual orientation",
    "sexual satisfaction",
    "sexuality",
    "sexuality education",
    "shame",
    "shock therapy",
    "shyness",
    "sibling",
    "sibling relation",
    "sick role",
    "sickness behavior",
    "sickness presence",
    "sign language",
    "single parent",
    "single person",
    "single stepparent",
    "sister",
    "situation awareness",
    "situational awareness",
    "situational therapy",
    "size perception",
    "sleep",
    "sleep debt",
    "sleep duration",
    "sleep hygiene",
    "sleep latency",
    "sleep quality",
    "sleep quantity",
    "sleep stage",
    "sleeping habit",
    "sleeplessness",
    "sleepwalking",
    "smell",
    "smell sense",
    "smiling",
    "smoking",
    "smoking blunt",
    "smoking cessation",
    "smoking reduction",
    "social ability",
    "social accountability",
    "social adjustment",
    "social attention",
    "social behavior",
    "social cognition",
    "social cohesion",
    "social communication",
    "social comparison",
    "social competence",
    "social conformity",
    "social coping",
    "social desirability",
    "social discrimination",
    "social disorganization",
    "social dominance",
    "social dynamic",
    "social dynamics",
    "social evolution",
    "social exclusion",
    "social facilitation",
    "social identification",
    "social identity",
    "social inclusion",
    "social integration",
    "social intelligence",
    "social interaction",
    "social learning",
    "social loafing",
    "social norm",
    "social obligation",
    "social perception",
    "social power",
    "social psychiatry",
    "social psychology",
    "social reinforcement",
    "social relationship",
    "social responsibility",
    "social science",
    "social skill",
    "social stigma",
    "social theory",
    "social worth",
    "sociality",
    "societal",
    "socioeconomic adversity",
    "sociological theory",
    "sociology",
    "son",
    "sons",
    "sound localization",
    "space perception",
    "space privacy",
    "spatial ability",
    "spatial behavior",
    "spatial learning",
    "spatial memory",
    "spatial navigation",
    "spatial orientation",
    "spatial visualization",
    "speech",
    "speech discrimination",
    "speech intelligibility",
    "speech perception",
    "spiritual sensitivity",
    "spirituality",
    "splitting pain",
    "sport psychology",
    "sports psychology",
    "spousal notification",
    "spouse",
    "staff attitude",
    "stalking",
    "startle reaction",
    "startle reflex",
    "startle response",
    "stepparent",
    "stepparent family",
    "stereoscopic vision",
    "stereotyping",
    "stigmatization",
    "stimulus generalization",
    "stopping smoking",
    "stress immunity",
    "structural racism",
    "student dropout",
    "subconscious",
    "subconscious bias",
    "subjective health",
    "subjective stress",
    "subliminal perception",
    "subliminal stimulation",
    "subliminal stimulus",
    "sucking behavior",
    "suggestion",
    "suicide attempt",
    "superego",
    "surrogate mother",
    "survivorship",
    "symbolic interactionism",
    "systematic racism",
    "systemic racism",
    "tactile gnosis",
    "tactile illusion",
    "tactile perception",
    "tactile sense",
    "taction",
    "talent",
    "task performance",
    "taste",
    "taste perception",
    "taste sense",
    "taste threshold",
    "taxis response",
    "team efficacy",
    "teen father",
    "teenage drinking",
    "teenage father",
    "telepathy",
    "temperament",
    "temperance",
    "temperature sense",
    "temporal perception",
    "territoriality",
    "theoretical technic",
    "theoretical technics",
    "theoretical technique",
    "therapeutic adherence",
    "therapeutic alliance",
    "therapeutic community",
    "therapeutic compliance",
    "therapeutic horticulture",
    "therapeutic relaxation",
    "thermal avoidance",
    "thermotaxis",
    "thinking",
    "thinking skill",
    "thirst",
    "thought",
    "threat cue",
    "threat sensitivity",
    "timbre discrimination",
    "timbre identification",
    "timbre perception",
    "time constraint",
    "time management",
    "time perception",
    "time pressure",
    "time study",
    "timidity",
    "tobacco cessation",
    "tobacco smoking",
    "toilet training",
    "token economy",
    "token reinforcement",
    "tonal discrimination",
    "tone differentiation",
    "tone identification",
    "tone perception",
    "tonic immobilization",
    "touch",
    "touch perception",
    "touch sense",
    "training transfer",
    "transactional analyses",
    "transactional analysis",
    "transvestism",
    "treatment adherence",
    "treatment compliance",
    "treatment refusal",
    "trust",
    "truth disclosure",
    "uncertainty",
    "uncivil behavior",
    "unconscious bias",
    "understanding",
    "unhappiness",
    "unlawful behavior",
    "unmarried",
    "unprotected intercourse",
    "unprotected sex",
    "vaccination delay",
    "vaccination hesitancy",
    "vaccination refusal",
    "vaccine delay",
    "vaccine hesitancy",
    "vaccine refusal",
    "value orientation",
    "verbal behavior",
    "verbal learning",
    "verbal reinforcement",
    "vertigo",
    "vestibular sense",
    "virginity",
    "virtual bullying",
    "virtue",
    "vision",
    "visual disparity",
    "visual feedback",
    "visual field",
    "visual illusion",
    "visual perception",
    "visual transduction",
    "vocational guidance",
    "voice identification",
    "voice recognition",
    "volition",
    "voluntary childlessness",
    "voyeurism",
    "wakefulness",
    "weight bias",
    "weight perception",
    "weight prejudice",
    "weight stigma",
    "well aging",
    "wet nursing",
    "whistle blower",
    "whistle blowing",
    "widow",
    "widowed",
    "widower",
    "widowhood",
    "wife",
    "wit",
    "work satisfaction",
    "work simplification",
    "working memory",
    "workplace abuse",
    "workplace bullying",
    "workplace incivility",
    "xenophobia",
    "youth drinking"
}
