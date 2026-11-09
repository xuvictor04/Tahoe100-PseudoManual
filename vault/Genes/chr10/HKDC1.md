---
symbol: "HKDC1"
type: "gene"
col: 7992
ensembl_id: "ENSG00000156510"
name: "hexokinase domain containing 1"
location: "10q22.1"
module: 117
arm: "+"
pooled_cpm: 51.2
n_lines_expressing: 20
n_dd_up: 33
n_dd_down: 2
n_dd_up_clean: 28
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 18
direction_downstream: 11
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# HKDC1

*hexokinase domain containing 1* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.53× (z +11.1, q 7e-26, up in 17 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.713× (z -4.1, q 0.028, down in 9 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 0.196×, A498 0.209×, LS 180 0.223×, HEC-1-A 0.312×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 4 lines (HT-29 0.171×, LoVo 0.190×, KATO III 0.156×, SW480 0.187×); [[Dinaciclib (drug)]] 5 µM in 2 lines (HT-29 0.111×, LS 180 0.0986×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 2 lines (LoVo 0.182×, SW480 0.304×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (HT-29 0.245×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NIBAN1]] (+0.63, fdr 7e-06), [[HSPA9]] (+0.60, fdr 1e-05), [[LINC01564]] (+0.59, fdr 7e-06).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[PLEKHG1]] → it (grade B ⚠); 11 go from it, the strongest it → [[RBCK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7992.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.53×** | +11.1 | 7e-26 | 17/18 (LS 180, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +8.9 | 1e-16 | 5/19 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.93×** | +7.4 | 2e-11 | 9/18 (LS 180, SW480, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +7.0 | 3e-10 | 7/17 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.68×** | +6.2 | 5e-08 | 17/18 (SW480, LoVo, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **2.70×** | +6.2 | 5e-08 | 15/18 (AsPC-1, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **1.39×** | +5.5 | 3e-06 | 15/18 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +5.4 | 5e-06 | 11/18 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.57×** | +5.4 | 5e-06 | 13/18 (LoVo, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +5.3 | 8e-06 | 1/17 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +5.2 | 8e-06 | 12/18 (A549, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +4.7 | 1e-04 | 10/18 (LS 180, SW480, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.48×** | +4.7 | 1e-04 | 11/18 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 2e-04 | 2/18 (NCI-H2347, A-172) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.78×** | +4.5 | 3e-04 | 1/18 (MIA PaCa-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **2.04×** | +4.4 | 3e-04 | 17/18 (AsPC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +4.3 | 7e-04 | 11/18 (HepG2/C3A, A549, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.43×** | +4.2 | 7e-04 | 13/18 (SW480, LoVo, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.87×** | +3.9 | 0.003 | 10/18 (AsPC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7992.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 0.196×, A498 0.209×, LS 180 0.223×, HEC-1-A 0.312×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 4 lines (HT-29 0.171×, LoVo 0.190×, KATO III 0.156×, SW480 0.187×); [[Dinaciclib (drug)]] 5 µM in 2 lines (HT-29 0.111×, LS 180 0.0986×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 2 lines (LoVo 0.182×, SW480 0.304×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (HT-29 0.245×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.713×** | -4.1 | 0.028 | 9/18 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.738×** | -3.6 | 0.080 | 10/18 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.608× | -3.1 | 0.30 | 5/18 (A498, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -3.1 | 0.30 | 1/19 (MIA PaCa-2) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7992. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 62.0 | 8 (1 ⚠) | 13 (11 ⚠) | [[Neratinib (maleate) (drug)]] 5 µM 2.57× (z +11.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0736× (z -22.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.182× (z -14.6) |
| [[HT-29 (line)]] | alt | 339 | 0 | 15 (12 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.171× (z -13.8) |
| [[LS 180 (line)]] | wt | 42.3 | 4 | 11 (10 ⚠) | [[Auranofin (drug)]] 5 µM 4.82× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.0986× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.319× (z -8.6) |
| [[SW480 (line)]] | alt | 24.3 | 5 (2 ⚠) | 8 (6 ⚠) | [[Artesunate (drug)]] 5 µM 3.22× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.187× (z -11.9) |
| [[KATO III (line)]] | alt | 263 | 1 | 9 (8 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.31× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.111× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.156× (z -12.7) |
| [[SW1417 (line)]] | alt | 200 | 0 | 7 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 170 | 2 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.06× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -18.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 14.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 9.67× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 69.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.43× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 135 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -15.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 32.2 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.05 µM 6.30× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.33× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 189 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 4.34 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.07 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.52 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.77 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.32 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.07 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.03 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.11 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.91 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.03 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.78 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.57 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.22 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.19 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.63 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.44 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7992), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIBAN1]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[HSPA9]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[LINC01564]] | +0.59 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[LURAP1L-AS1]] | +0.58 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[CYP4F11]] | +0.58 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[SLC7A11]] | +0.57 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[OSGIN1]] | +0.56 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[PIP5K1B]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[TRIB3]] | +0.55 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[YARS1]] | +0.55 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[GCNT3]] | +0.55 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[SEL1L3]] | +0.54 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 2, C 16. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG1]] | B | PLEKHG1 activity raises HKDC1's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.84× lower at baseline in the lines without PLEKHG1 | 0.032 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[SH3RF2]] | B | SH3RF2 activity raises HKDC1's level | lines that do not express SH3RF2 (16) vs lines expressing it (34) | 4.08× lower at baseline in the lines without SH3RF2 | 0.047 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent |
| [[GCNT3]] | C | GCNT3 activity raises HKDC1's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 10.32× lower at baseline in the lines without GCNT3 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[INAVA]] | C | INAVA activity raises HKDC1's level | lines that do not express INAVA (29) vs lines expressing it (21) | 6.75× lower at baseline in the lines without INAVA | 5e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3; co-absent with the target |
| [[CYP4F3]] | C | CYP4F3 activity raises HKDC1's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 6.53× lower at baseline in the lines without CYP4F3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6; co-absent with the target |
| [[LINC01564]] | C | LINC01564 activity raises HKDC1's level | lines that do not express LINC01564 (24) vs lines expressing it (26) | 5.53× lower at baseline in the lines without LINC01564 | 0.005 | ⚠ within organs, on part of the lines; also absent: LINC03040, INAVA, CYP4F11; maybe low, not absent; co-absent with the target |
| [[ESRP1]] | C | ESRP1 activity raises HKDC1's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 4.34× lower at baseline in the lines without ESRP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7; co-absent with the target |
| [[LINC03040]] | C | LINC03040 activity raises HKDC1's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 5.02× lower at baseline in the lines without LINC03040 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2; co-absent with the target |
| [[NMRAL2P]] | C | NMRAL2P activity raises HKDC1's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 3.61× lower at baseline in the lines without NMRAL2P | 0.009 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1; co-absent with the target |
| [[SPINK1]] | C | SPINK1 activity raises HKDC1's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 3.36× lower at baseline in the lines without SPINK1 | 0.011 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3; co-absent with the target |
| [[TTC22]] | C | TTC22 activity raises HKDC1's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 4.58× lower at baseline in the lines without TTC22 | 0.018 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5; co-absent with the target |
| [[TMEM125]] | C | TMEM125 activity raises HKDC1's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 4.53× lower at baseline in the lines without TMEM125 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBCK1]] | B | HKDC1 activity raises RBCK1's level | lines that do not express HKDC1 (30) vs lines expressing it (20) | 2.21× lower at baseline in the lines without HKDC1 | 0.001 | ⚠ within organs, on part of the lines; also absent: HHLA2, GCNT3, HNF4A |
| [[TTC39A]] | B | HKDC1 activity strengthens TTC39A's drug response | lines that do not express HKDC1 (28) vs lines expressing it (18) | the lines without HKDC1 respond 0.59× as strongly (z diff +1.10); strongest at Panobinostat 5 µM: 0.87x vs 0.41x (z diff +3.8) | 0.047 | ⚠ within organs, on part of the lines; also absent: HHLA2, GCNT3, HNF4A; target measured in part of the lines; artifact flags |
| [[TTC39A]] | B | HKDC1 activity raises TTC39A's level | lines that do not express HKDC1 (30) vs lines expressing it (20) | 1.51× lower at baseline in the lines without HKDC1 | 0.088 | ⚠ within organs, on part of the lines; also absent: HHLA2, GCNT3, HNF4A |
| [[GCNT3]] | C | HKDC1 activity raises GCNT3's level | lines that do not express HKDC1 (30) vs lines expressing it (20) | 5.10× lower at baseline in the lines without HKDC1 | 0.002 | ⚠ within organs, on part of the lines; also absent: HHLA2, GCNT3, HNF4A; co-absent with the target |
| [[INAVA]] | C | HKDC1 activity raises INAVA's level | lines that do not express HKDC1 (30) vs lines expressing it (20) | 4.81× lower at baseline in the lines without HKDC1 | 0.004 | ⚠ within organs, on part of the lines; also absent: HHLA2, GCNT3, HNF4A; co-absent with the target |
| [[LINC01564]] | C | HKDC1 activity raises LINC01564's level | lines that do not express HKDC1 (30) vs lines expressing it (20) | 3.07× lower at baseline in the lines without HKDC1 | 0.007 | ⚠ within organs, on part of the lines; also absent: HHLA2, GCNT3, HNF4A; co-absent with the target |
| [[SULT1C2]] | C | HKDC1 activity raises SULT1C2's level | lines that do not express HKDC1 (30) vs lines expressing it (20) | 2.94× lower at baseline in the lines without HKDC1 | 0.008 | ⚠ within organs, on part of the lines; also absent: HHLA2, GCNT3, HNF4A; co-absent with the target |
| [[SPINK1]] | C | HKDC1 activity raises SPINK1's level | lines that do not express HKDC1 (30) vs lines expressing it (20) | 2.87× lower at baseline in the lines without HKDC1 | 0.013 | ⚠ within organs, on part of the lines; also absent: HHLA2, GCNT3, HNF4A; co-absent with the target |
| [[KRT80]] | C | HKDC1 activity raises KRT80's level | lines that do not express HKDC1 (30) vs lines expressing it (20) | 3.58× lower at baseline in the lines without HKDC1 | 0.025 | ⚠ within organs, on part of the lines; also absent: HHLA2, GCNT3, HNF4A; co-absent with the target |
| [[CYP4F3]] | C | HKDC1 activity raises CYP4F3's level | lines that do not express HKDC1 (30) vs lines expressing it (20) | 3.15× lower at baseline in the lines without HKDC1 | 0.048 | ⚠ within organs, on part of the lines; also absent: HHLA2, GCNT3, HNF4A; co-absent with the target |
| [[B3GALT5]] | C | HKDC1 activity raises B3GALT5's level | lines that do not express HKDC1 (30) vs lines expressing it (20) | 2.69× lower at baseline in the lines without HKDC1 | 0.079 | ⚠ within organs, on part of the lines; also absent: HHLA2, GCNT3, HNF4A; co-absent with the target |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-10.4, 47.9); signed map (51.7, -11.4). **Vector** length 94.1, 31.3% of its response variance represented; |z| ≥ 3 in 784 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +11.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.2 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +5.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.7 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +4.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +3.9 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -3.6 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | hexokinase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:69,220,332-69,267,552 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37767, FLJ22761 |
| Gene groups (HGNC) | Hexokinase family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 3 pathways, smallest: Glycolysis; Glucose metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2TB90](https://www.uniprot.org/uniprotkb/Q2TB90) (Hexokinase HKDC1):

> Catalyzes the phosphorylation of hexose to hexose 6-phosphate, although at very low level compared to other hexokinases. Has low glucose phosphorylating activity compared to other hexokinases. Involved in glucose homeostasis and hepatic lipid accumulation. Required to maintain whole-body glucose homeostasis during pregnancy; however additional evidence is required to confirm this role (By similarity).

**Summary**, from NCBI Gene [80201](https://www.ncbi.nlm.nih.gov/gene/80201):

> This gene encodes a member of the hexokinase protein family. The encoded protein is involved in glucose metabolism, and reduced expression may be associated with gestational diabetes mellitus. High expression of this gene may also be associated with poor prognosis in hepatocarcinoma. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:23302](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23302) · Entrez [80201](https://www.ncbi.nlm.nih.gov/gene/80201) · UniProt [Q2TB90](https://www.uniprot.org/uniprotkb/Q2TB90) · Ensembl [ENSG00000156510](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156510)

## Data

Gene col 7992: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7992); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7992, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7992]; `tensor/DDL_lfc|DDL_z.npy` [7992]; `embed/gene_vectors.npy` [7992]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7992 or target_col == 7992). Every well: [[HKDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HKDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
