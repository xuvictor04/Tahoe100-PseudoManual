---
symbol: "APPAT"
type: "gene"
col: 13761
ensembl_id: "ENSG00000230606"
name: "atherosclerotic plaque pathogenesis associated transcript"
location: "2q11.2"
module: 41
arm: "-"
pooled_cpm: 4.14
n_lines_expressing: 43
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 10
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# APPAT

*atherosclerotic plaque pathogenesis associated transcript* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.33× (z +9.0, q 1e-16, up in 7 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +3.8, q 0.021, up in 9 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.574× (z -5.9, q 2e-06, down in 22 of 32 measured lines) ⚠ cell-cycle shift, explains ~54% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.555× (z -4.4, q 0.002, down in 17 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00342]] (+0.71, fdr 7e-06), [[CRPPA]] (+0.59, fdr 3e-05), [[FRG1-DT]] (+0.55, fdr 2e-05); moves opposite to [[EML2]] (-0.58, fdr 3e-05), [[HADHB]] (-0.57, fdr 3e-05), [[SEC22A]] (-0.55, fdr 3e-05).
> It sits in the **-** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2B]] → it (grade B ⚠); 10 go from it, the strongest it → [[SUCLA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13761.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.33×** | +9.0 | 1e-16 | 7/12 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +7.4 | 3e-11 | 2/2 (MIA PaCa-2, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +5.7 | 2e-06 | 4/6 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +3.8 | 0.021 | 9/30 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.048 | 6/38 (SW480, AsPC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.56×** | +3.3 | 0.087 | 7/34 (A549, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13761.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.574×** | -5.9 | 2e-06 | 22/32 (NCI-H1573, Hs 766T, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.555×** | -4.4 | 0.002 | 17/36 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.557×** | -4.4 | 0.002 | 19/38 (NCI-H23, MIA PaCa-2, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.567×** | -4.2 | 0.003 | 16/37 (KATO III, SNU-1, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.368×** | -3.9 | 0.010 | 16/28 (RKO, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.604×** | -3.6 | 0.031 | 14/36 (PANC-1, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.404×** | -3.5 | 0.031 | 13/34 (NCI-H23, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.633×** | -3.4 | 0.042 | 17/36 (LoVo, NCI-H23, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.635×** | -3.4 | 0.042 | 11/36 (SNU-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.651×** | -3.2 | 0.075 | 11/38 (C32, RKO, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.643×** | -3.2 | 0.077 | 13/35 (A-172, HEC-1-A, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.657×** | -3.1 | 0.078 | 14/32 (RPMI-7951, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13761. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 3.29 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -8.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[A-172 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.984 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.969 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13761), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00342]] | +0.71 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[CRPPA]] | +0.59 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[FRG1-DT]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[CFAP44]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[CATSPERE]] | +0.55 | +0.53 / +0.40 | both halves | 4e-05 |  |
| [[ARSB]] | +0.54 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[HNRNPM]] | +0.53 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[RNF32-AS1]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[AVEN]] | +0.52 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[ZNF876P]] | +0.52 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[RAP2C-AS1]] | +0.52 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[TAFA2]] | +0.51 | +0.50 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EML2]] | -0.58 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[HADHB]] | -0.57 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[SEC22A]] | -0.55 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[SLC35A1]] | -0.55 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[GOLGA2]] | -0.54 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[ESCO1]] | -0.54 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[SNAPC3]] | -0.54 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[BBS4]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[MTIF3]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[RARS1]] | -0.53 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[CHURC1-FNTB]] | -0.53 | -0.58 / -0.40 | both halves | 4e-05 |  |
| [[LCMT1]] | -0.52 | -0.48 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2B]] | B | TOP2B activity lowers APPAT's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SUCLA2]] | B | APPAT activity raises SUCLA2's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.57× lower at baseline in the lines without APPAT | 0.012 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MTIF3]] | B | APPAT activity raises MTIF3's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without APPAT | 0.027 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SUMO3]] | B | APPAT activity lowers SUMO3's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.48× higher at baseline in the lines without APPAT | 0.032 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[UFL1-AS1]] | B | APPAT activity raises UFL1-AS1's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.74× lower at baseline in the lines without APPAT | 0.036 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RNF32-AS1]] | B | APPAT activity raises RNF32-AS1's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.38× lower at baseline in the lines without APPAT | 0.051 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PMM1]] | B | APPAT activity lowers PMM1's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.73× higher at baseline in the lines without APPAT | 0.062 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CFAP44]] | B | APPAT activity raises CFAP44's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without APPAT | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CFAP44]] | B | APPAT activity strengthens CFAP44's drug response | lines that do not express APPAT (6) vs lines expressing it (40) | the lines without APPAT respond 0.54× as strongly (z diff +2.36); strongest at Niclosamide (olamine) 5 µM: 0.95x vs 0.38x (z diff +4.6) | 0.074 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SLC35A1]] | B | APPAT activity raises SLC35A1's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.29× lower at baseline in the lines without APPAT | 0.086 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ETFDH]] | B | APPAT activity raises ETFDH's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.44× lower at baseline in the lines without APPAT | 0.098 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.509). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (26.4, -10.0); signed map (26.3, -30.1). **Vector** length 45.3, 5.79% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +5.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.0 | +2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | +0.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.0 | +1.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.0 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.9 | +1.9 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.4 | -3.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -0.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.2 | -0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | atherosclerotic plaque pathogenesis associated transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q11.2 — chr2:97,416,165-97,433,527 (-) |
| Ensembl biotype | lncRNA |
| Also known as | AC092683.1; previously LINC02969 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56009](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56009) · Entrez [100506123](https://www.ncbi.nlm.nih.gov/gene/100506123) · Ensembl [ENSG00000230606](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000230606)

## Data

Gene col 13761: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13761); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13761, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13761]; `tensor/DDL_lfc|DDL_z.npy` [13761]; `embed/gene_vectors.npy` [13761]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13761 or target_col == 13761). Every well: [[APPAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APPAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
