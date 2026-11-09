---
symbol: "TJP3"
type: "gene"
col: 2577
ensembl_id: "ENSG00000105289"
name: "tight junction protein 3"
location: "19p13.3"
module: 44
arm: "+"
pooled_cpm: 10.6
n_lines_expressing: 21
n_dd_up: 31
n_dd_down: 34
n_dd_up_clean: 27
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 134
direction_downstream: 171
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# TJP3

*tight junction protein 3* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 7.60× (z +23.4, q 0e+00, up in 17 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.427× (z -9.8, q 4e-20, down in 17 of 19 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.525× (z -7.1, q 4e-10, down in 16 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYP4F12]] (+0.84, fdr 7e-06), [[PLEKHG6]] (+0.82, fdr 7e-06), [[CLDN3]] (+0.78, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 134 arrows point to it, the strongest [[MCF2L]] → it (grade B ⚠); 171 go from it, the strongest it → [[SLC44A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2577.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **7.60×** | +23.4 | 0e+00 | 17/19 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.65×** | +21.1 | 0e+00 | 18/19 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.65×** | +18.9 | 0e+00 | 15/19 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.92×** | +15.8 | 0e+00 | 13/19 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.29×** | +13.7 | 6e-41 | 19/19 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.04×** | +12.4 | 4e-33 | 4/12 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.56×** | +10.8 | 2e-25 | 16/19 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.18×** | +9.0 | 2e-17 | 3/16 (BT-474, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +6.0 | 1e-07 | 2/14 (NCI-H2347, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.53×** | +5.7 | 8e-07 | 14/19 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.54×** | +5.3 | 5e-06 | 8/19 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.54×** | +4.9 | 5e-05 | 15/19 (AsPC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.51×** | +4.7 | 1e-04 | 9/19 (LS 180, A-427, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.5 | 2e-04 | 0/17 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.48×** | +4.5 | 3e-04 | 8/19 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.54×** | +4.3 | 6e-04 | 13/18 (AsPC-1, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.60×** | +3.9 | 0.003 | 2/17 (KATO III, LS 180) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.005 | 13/19 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2577.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.427×** | -9.8 | 4e-20 | 17/19 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.525×** | -7.1 | 4e-10 | 16/19 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.545×** | -7.0 | 4e-10 | 17/19 (NCI-H1573, Panc 03.27, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.597×** | -6.0 | 3e-07 | 17/19 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.715×** | -5.5 | 5e-06 | 14/19 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.658×** | -4.8 | 1e-04 | 11/19 (COLO 205, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.663×** | -4.8 | 2e-04 | 12/19 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.665×** | -4.7 | 2e-04 | 12/19 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.672×** | -4.6 | 3e-04 | 12/17 (COLO 205, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.695×** | -4.2 | 0.001 | 13/18 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.690×** | -4.1 | 0.002 | 10/18 (HT-29, HepG2/C3A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.688×** | -4.1 | 0.002 | 12/19 (SW1417, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.695×** | -4.0 | 0.003 | 13/19 (COLO 205, HT-29, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -3.9 | 0.003 | 13/17 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.703×** | -3.8 | 0.006 | 0/19 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.725×** | -3.7 | 0.007 | 13/19 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.530×** | -3.6 | 0.010 | 13/17 (HT-29, SW1417, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.726×** | -3.6 | 0.012 | 6/19 (SW480, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2577. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 66.8 | 0 | 15 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0777× (z -28.8) |
| [[LoVo (line)]] | wt | 15.4 | 2 | 7 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.06× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -13.7) |
| [[KATO III (line)]] | alt | 43.3 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -20.6) |
| [[COLO 205 (line)]] | alt | 46.4 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0785× (z -22.3) |
| [[Panc 03.27 (line)]] | alt | 21.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0876× (z -12.4) |
| [[SW480 (line)]] | alt | 6.46 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 7.20× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -8.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 61.7 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -25.8) |
| [[SW1417 (line)]] | alt | 18.7 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 20.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -10.6) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -9.7) |
| [[A-427 (line)]] | wt | 7.94 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.122× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 17.5 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.110× (z -9.7) |
| [[HCT15 (line)]] | alt | 49.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 24.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -10.8) |
| [[A-172 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.987 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.925 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.34 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2577), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP4F12]] | +0.84 | +0.82 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[PLEKHG6]] | +0.82 | +0.73 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[CLDN3]] | +0.78 | +0.76 / +0.76 | both halves | 7e-06 | STRING 988 |
| [[ALOX5]] | +0.77 | +0.77 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SLC44A4]] | +0.77 | +0.70 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[MUC3A]] | +0.75 | +0.64 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[TC2N]] | +0.75 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[PRR15L]] | +0.74 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[BCAS1]] | +0.72 | +0.64 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[VIPR1]] | +0.72 | +0.62 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ELF3]] | +0.72 | +0.63 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[RNF183]] | +0.72 | +0.62 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*134 arrows, 134 of them with an alert ⚠; grade A 0, B 18, C 116. Shown: the 12 strongest; 122 more arrows (122 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCF2L]] | B | MCF2L activity raises TJP3's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 3.59× lower at baseline in the lines without MCF2L | 0.007 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[SLC44A3]] | B | SLC44A3 activity raises TJP3's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.51× lower at baseline in the lines without SLC44A3 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[NR3C2]] | B | NR3C2 activity raises TJP3's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 2.48× lower at baseline in the lines without NR3C2 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[C4orf19]] | B | C4orf19 activity raises TJP3's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 2.38× lower at baseline in the lines without C4orf19 | 0.028 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[LNX1]] | B | LNX1 activity raises TJP3's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 2.39× lower at baseline in the lines without LNX1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[MROH7]] | B | MROH7 activity raises TJP3's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 2.83× lower at baseline in the lines without MROH7 | 0.035 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[CRACR2B]] | B | CRACR2B activity raises TJP3's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 3.07× lower at baseline in the lines without CRACR2B | 0.053 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[TOP2A]] | B | TOP2A activity raises TJP3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDC42EP5]] | B | CDC42EP5 activity raises TJP3's level | lines that do not express CDC42EP5 (11) vs lines expressing it (39) | 2.97× lower at baseline in the lines without CDC42EP5 | 0.065 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[VAV1]] | B | VAV1 activity raises TJP3's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 2.02× lower at baseline in the lines without VAV1 | 0.068 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises TJP3's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.74× lower at baseline in the lines without ELF3-AS1 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[FUT2]] | B | FUT2 activity raises TJP3's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 2.23× lower at baseline in the lines without FUT2 | 0.071 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |

### Downstream of this gene

*171 arrows, 171 of them with an alert ⚠; grade A 0, B 61, C 110. Shown: the 12 strongest; 159 more arrows (159 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3]] | B | TJP3 activity raises SLC44A3's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 3.68× lower at baseline in the lines without TJP3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[MROH7]] | B | TJP3 activity raises MROH7's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.63× lower at baseline in the lines without TJP3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[PLS1]] | B | TJP3 activity raises PLS1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 4.26× lower at baseline in the lines without TJP3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[ARHGEF16]] | B | TJP3 activity raises ARHGEF16's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 3.47× lower at baseline in the lines without TJP3 | 7e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[LNX1]] | B | TJP3 activity raises LNX1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 4.40× lower at baseline in the lines without TJP3 | 0.003 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[RSPH1]] | B | TJP3 activity raises RSPH1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.21× lower at baseline in the lines without TJP3 | 0.004 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[KIAA1522]] | B | TJP3 activity raises KIAA1522's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 3.01× lower at baseline in the lines without TJP3 | 0.004 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[FUT2]] | B | TJP3 activity raises FUT2's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.21× lower at baseline in the lines without TJP3 | 0.006 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[RHPN2]] | B | TJP3 activity raises RHPN2's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.76× lower at baseline in the lines without TJP3 | 0.008 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[TUFT1]] | B | TJP3 activity raises TUFT1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.36× lower at baseline in the lines without TJP3 | 0.010 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[IL22RA1]] | B | TJP3 activity raises IL22RA1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.83× lower at baseline in the lines without TJP3 | 0.010 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[BCL2L15]] | B | TJP3 activity raises BCL2L15's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.64× lower at baseline in the lines without TJP3 | 0.011 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.800). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.1, 53.4); signed map (60.2, 4.7). **Vector** length 97.4, 38.8% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.56 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.56 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.56 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +21.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +12.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +18.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.3 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +5.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.9 | -3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.7 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -7.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -0.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | tight junction protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:3,708,362-3,750,813 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZO-3 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; PDZ domain containing; SH3 domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [O95049](https://www.uniprot.org/uniprotkb/O95049) (Tight junction protein ZO-3):

> TJP1, TJP2, and TJP3 are closely related scaffolding proteins that link tight junction (TJ) transmembrane proteins such as claudins, junctional adhesion molecules, and occludin to the actin cytoskeleton. The tight junction acts to limit movement of substances through the paracellular space and as a boundary between the compositionally distinct apical and basolateral plasma membrane domains of epithelial and endothelial cells. Binds and recruits PATJ to tight junctions where it connects and …

**Summary**, from NCBI Gene [27134](https://www.ncbi.nlm.nih.gov/gene/27134):

> The protein encoded by this gene is a member of the membrane-associated guanylate kinase-like (MAGUK) protein family which is characterized by members having multiple PDZ domains, a single SH3 domain, and a single guanylate kinase-like (GUK)-domain. In addition, members of the zonula occludens protein subfamily have an acidic domain, a basic arginine-rich region, and a proline-rich domain. The protein encoded by this gene plays a role in the linkage between the actin cytoskeleton and …

**Accessions** — [HGNC:11829](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11829) · Entrez [27134](https://www.ncbi.nlm.nih.gov/gene/27134) · UniProt [O95049](https://www.uniprot.org/uniprotkb/O95049) · Ensembl [ENSG00000105289](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105289)

## Data

Gene col 2577: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2577); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2577, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2577]; `tensor/DDL_lfc|DDL_z.npy` [2577]; `embed/gene_vectors.npy` [2577]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2577 or target_col == 2577). Every well: [[TJP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TJP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
