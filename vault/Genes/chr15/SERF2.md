---
symbol: "SERF2"
type: "gene"
col: 6381
ensembl_id: "ENSG00000140264"
name: "small EDRK-rich factor 2"
location: "15q15.3"
module: 48
arm: "+"
pooled_cpm: 150.18
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# SERF2

*small EDRK-rich factor 2* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.16× (z +8.7, q 2e-15, up in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +3.4, q 0.068, up in 28 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 11 lines (SHP-77 5.72×, C-33 A 4.81×, NCI-H1573 4.31×, SW480 3.85×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 6.18×, SW480 5.19×, A549 5.84×, C-33 A 5.93×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.421×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA1]] (+0.81, fdr 7e-06), [[OST4]] (+0.77, fdr 7e-06), [[COX7A2]] (+0.77, fdr 7e-06, ⚠ COX7A2 in the vector space only through flagged drug-doses), [[ATP5F1E]] (+0.77, fdr 7e-06); moves opposite to [[PSMG1]] (-0.74, fdr 7e-06), [[CCT5]] (-0.68, fdr 7e-06), [[CEP41]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[APOE]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6381.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 11 lines (SHP-77 5.72×, C-33 A 4.81×, NCI-H1573 4.31×, SW480 3.85×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 6.18×, SW480 5.19×, A549 5.84×, C-33 A 5.93×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.16×** | +8.7 | 2e-15 | 44/44 (SHP-77, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.69×** | +8.0 | 3e-13 | 49/49 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.39×** | +6.3 | 5e-08 | 43/45 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.96×** | +5.3 | 2e-05 | 48/48 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.80×** | +4.6 | 4e-04 | 45/48 (NCI-H1573, PANC-1, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.068 | 28/49 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.53× | +3.2 | 0.10 | 38/47 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | 1.52× | +3.2 | 0.11 | 40/48 (A498, HS-578T, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | 1.49× | +3.0 | 0.15 | 42/48 (AsPC-1, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6381.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.421×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 5 µM |  | 0.444× | -3.3 | 0.39 | 43/49 (AsPC-1, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6381. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 126 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.81× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 187 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.18× (z +10.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 197 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 94.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 147 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.25× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 95.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 130 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +8.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 92.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 128 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +9.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 156 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +8.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 229 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +9.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 201 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 98.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 112 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 99.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.43× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.72× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 87.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.08× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 232 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 130 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 186 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 110 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 116 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 140 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 188 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 161 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 326 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 121 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 118 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6381), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 12 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA1]] | +0.81 | +0.81 / +0.79 | both halves | 7e-06 |  |
| [[OST4]] | +0.77 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[COX7A2]] ⚠ | +0.77 | +0.75 / +0.76 | both halves | 7e-06 | STRING 533; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5F1E]] | +0.77 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[SSR4]] | +0.75 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[RPS29]] | +0.73 | +0.68 / +0.75 | both halves | 7e-06 | STRING 419 |
| [[COX7B]] | +0.73 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[UQCRB]] ⚠ | +0.72 | +0.64 / +0.74 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RABAC1]] | +0.72 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[UBL5]] | +0.72 | +0.69 / +0.74 | both halves | 7e-06 | STRING 408 |
| [[NDUFB11]] ⚠ | +0.72 | +0.74 / +0.66 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPLP2]] | +0.71 | +0.67 / +0.75 | both halves | 7e-06 | STRING 437 |
| [[COX6A1]] | +0.71 | +0.71 / +0.80 | both halves | 7e-06 |  |
| [[FAU]] | +0.71 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[MIF]] | +0.71 | +0.67 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMG1]] | -0.74 | -0.64 / -0.74 | both halves | 7e-06 |  |
| [[CCT5]] | -0.68 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[CEP41]] | -0.67 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[CCT2]] | -0.67 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[ATIC]] | -0.65 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[HGH1]] | -0.64 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[RUVBL1]] | -0.64 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[MAK16]] | -0.63 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[RIF1]] | -0.63 | -0.57 / -0.64 | both halves | 9e-06 |  |
| [[DCLRE1A]] | -0.63 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[IFRD2]] | -0.62 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[CCT7]] | -0.60 | -0.57 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOE]] | B | APOE activity raises SERF2's level | lines that do not express APOE (25) vs lines expressing it (25) | 1.09× lower at baseline in the lines without APOE | 0.086 | ⚠ within organs, on part of the lines; also absent: SYT11, RNF175, GRIA2; maybe low, not absent |
| [[SACS]] | B | SACS activity lowers SERF2's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.47× higher at baseline in the lines without SACS | 0.098 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.752). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.5, -23.1); signed map (-34.5, 10.5). **Vector** length 70.3, 35.0% of its response variance represented; |z| ≥ 3 in 502 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.59 to 31); *Respiratory electron transport* (reactome, mean cos +0.59 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.61 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +3.0 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +0.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.9 | +0.9 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.8 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | +8.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | +0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | +0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | +1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | small EDRK-rich factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3 — chr15:43,777,087-43,804,427 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FAM2C, Hero7, 4F5REL, H4F5rel, HsT17089 |
| Gene groups (HGNC) | Small EDRK-rich factor family; SERF domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P84101](https://www.uniprot.org/uniprotkb/P84101) (Small EDRK-rich factor 2):

> Positive regulator of amyloid protein aggregation and proteotoxicity. Induces conformational changes in amyloid proteins, such as HTT, driving them into compact formations preceding the formation of aggregates.

**Summary**, from NCBI Gene [10169](https://www.ncbi.nlm.nih.gov/gene/10169):

> Involved in protein destabilization. Predicted to be located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10757](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10757) · Entrez [10169](https://www.ncbi.nlm.nih.gov/gene/10169) · UniProt [P84101](https://www.uniprot.org/uniprotkb/P84101) · Ensembl [ENSG00000140264](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140264)

## Data

Gene col 6381: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6381); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6381, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6381]; `tensor/DDL_lfc|DDL_z.npy` [6381]; `embed/gene_vectors.npy` [6381]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6381 or target_col == 6381). Every well: [[SERF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
