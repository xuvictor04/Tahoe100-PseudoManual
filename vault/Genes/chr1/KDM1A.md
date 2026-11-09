---
symbol: "KDM1A"
type: "gene"
col: 47
ensembl_id: "ENSG00000004487"
name: "lysine demethylase 1A"
location: "1p36.12"
module: 182
arm: "+"
pooled_cpm: 105.21
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# KDM1A

*lysine demethylase 1A* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.74× (z +8.2, q 2e-13, up in 41 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.49× (z +7.3, q 6e-11, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 0.709× (z -3.8, q 0.057, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRPA1]] (+0.76, fdr 7e-06), [[SKP2]] (+0.74, fdr 7e-06), [[RPA1]] (+0.69, fdr 7e-06); moves opposite to [[TUT7]] (-0.76, fdr 7e-06), [[ZNF274]] (-0.67, fdr 7e-06), [[ZNF674]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 182]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RNF103-CHMP3]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 47.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +8.2 | 2e-13 | 41/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.49×** | +7.3 | 6e-11 | 40/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +6.5 | 1e-08 | 35/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.10×** | +6.0 | 4e-07 | 39/49 (KATO III, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +5.6 | 3e-06 | 28/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +5.5 | 4e-06 | 31/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.010 | 27/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.26×** | +3.5 | 0.027 | 24/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.5 | 0.027 | 20/48 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.22× | +3.0 | 0.15 | 19/48 (KATO III, HEC-1-A, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 47.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.709×** | -3.8 | 0.057 | 31/48 (KATO III, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.846× | -3.6 | 0.057 | 19/48 (AN3 CA, HepG2/C3A, …) | top dose only | position effect removed |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.790×** | -3.6 | 0.057 | 25/48 (KATO III, NCI-H1792, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **0.796×** | -3.5 | 0.067 | 27/48 (RKO, NCI-H460, …) | two highest doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.803×** | -3.4 | 0.087 | 23/48 (HEC-1-A, A549, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.739×** | -3.3 | 0.088 | 22/48 (KATO III, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.814× | -3.2 | 0.12 | 21/48 (SK-MEL-2, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.816× | -3.1 | 0.12 | 23/48 (AN3 CA, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.810× | -3.1 | 0.12 | 21/49 (HEC-1-A, NCI-H1792, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 47. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 137 | 2 (1 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.71× (z +12.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -12.0) ⚠ cell-cycle shift, explains ~84% of this change |
| [[PANC-1 (line)]] | alt | 119 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +14.8) | — |
| [[C-33 A (line)]] | alt | 285 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 76.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 199 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0695× (z -21.2) |
| [[AsPC-1 (line)]] | alt | 140 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.38× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 86.8 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 8.28× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 52.4 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.60× (z +10.8) ⚠ toxic | — |
| [[HCT15 (line)]] | alt | 130 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.320× (z -8.5) |
| [[LS 180 (line)]] | wt | 118 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 89.1 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.21× (z +9.6) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 86.7 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.37× (z +9.2) ⚠ toxic | — |
| [[SW48 (line)]] | wt | 145 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.93× (z +11.4) | — |
| [[A-172 (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 81.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 92.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 84.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 105 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 145 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 138 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 131 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 82.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 98.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 130 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 47), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPA1]] | +0.76 | +0.82 / +0.68 | both halves | 7e-06 |  |
| [[SKP2]] | +0.74 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[RPA1]] | +0.69 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[METAP1]] | +0.68 | +0.76 / +0.64 | both halves | 7e-06 | same gene group |
| [[IARS2]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[HDAC2]] | +0.67 | +0.66 / +0.69 | both halves | 7e-06 | same gene group; pathway: Adherens junctions interactions; STRING 999 |
| [[GPD1L]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[RNPEP]] | +0.66 | +0.70 / +0.60 | both halves | 7e-06 | same gene group |
| [[COPS7B]] | +0.66 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[ZDHHC20]] | +0.66 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[HSF2]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[USP3]] | +0.65 | +0.76 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUT7]] | -0.76 | -0.77 / -0.69 | both halves | 7e-06 |  |
| [[ZNF274]] | -0.67 | -0.70 / -0.58 | both halves | 7e-06 |  |
| [[ZNF674]] | -0.64 | -0.72 / -0.53 | both halves | 1e-05 |  |
| [[C6orf62]] | -0.64 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[IER5]] | -0.63 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[MIR22HG]] | -0.62 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[NSRP1]] | -0.62 | -0.70 / -0.55 | both halves | 1e-05 | same gene group |
| [[SAP30BP]] | -0.62 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[C3orf62]] | -0.61 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[XIAP]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 | pathway: Adherens junctions interactions |
| [[ABL2]] | -0.61 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[USE1]] | -0.61 | -0.52 / -0.70 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF103-CHMP3]] | B | RNF103-CHMP3 activity lowers KDM1A's level | lines that do not express RNF103-CHMP3 (5) vs lines expressing it (45) | 1.31× higher at baseline in the lines without RNF103-CHMP3 | 0.076 | ⚠ within organs, on part of the lines; also absent: TMEM144, YBX3, DTX4; maybe low, not absent |
| [[CLCF1]] | B | CLCF1 activity lowers KDM1A's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.36× higher at baseline in the lines without CLCF1 | 0.093 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[PHKG2]] | C | PHKG2's natural level weakens KDM1A's drug response | PHKG2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse +0.04; direction not clear | 0.095 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | KDM1A's natural level raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | KDM1A's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.61 | 0.440 over the table, 0.049 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **+** arm (projection on the module's main direction 0.841). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-7.3, -12.9); signed map (-37.9, -13.8). **Vector** length 118, 37.8% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.1 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.0 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.0 | -0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +0.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.2 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.1 | -3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.8 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | +0.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -2.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | lysine demethylase 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:23,019,443-23,083,689 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0601, BHC110, LSD1; previously AOF2, KDM1 |
| Gene groups (HGNC) | CoREST complex subunits; MicroRNA protein coding host genes; Flavoproteins; Lysine demethylase 1 family |
| Reactome | 32 pathways, smallest: Activated PKN1 stimulates transcription of AR (androgen receptor) regulated genes KLK2 and KLK3; HDMs demethylate histones; NR1H3 & NR1H2 regulate gene expression linked to cholesterol transport and efflux |
| Matched by | ensembl_id |

**Function**, from UniProt [O60341](https://www.uniprot.org/uniprotkb/O60341) (Lysine-specific histone demethylase 1A):

> Histone demethylase that can demethylate both 'Lys-4' (H3K4me) and 'Lys-9' (H3K9me) of histone H3, thereby acting as a coactivator or a corepressor, depending on the context. Acts by oxidizing the substrate by FAD to generate the corresponding imine that is subsequently hydrolyzed. Acts as a corepressor by mediating demethylation of H3K4me, a specific tag for epigenetic transcriptional activation. Demethylates both mono- (H3K4me1) and di-methylated (H3K4me2). May play a role in the repression …

**Summary**, from NCBI Gene [23028](https://www.ncbi.nlm.nih.gov/gene/23028):

> This gene encodes a nuclear protein containing a SWIRM domain, a FAD-binding motif, and an amine oxidase domain. This protein is a component of several histone deacetylase complexes, though it silences genes by functioning as a histone demethylase. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:29079](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29079) · Entrez [23028](https://www.ncbi.nlm.nih.gov/gene/23028) · UniProt [O60341](https://www.uniprot.org/uniprotkb/O60341) · Ensembl [ENSG00000004487](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004487)

## Data

Gene col 47: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 47); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 47, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 47]; `tensor/DDL_lfc|DDL_z.npy` [47]; `embed/gene_vectors.npy` [47]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 47 or target_col == 47). Every well: [[KDM1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
