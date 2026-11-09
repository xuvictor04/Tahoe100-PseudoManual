---
symbol: "CPE"
type: "gene"
col: 3054
ensembl_id: "ENSG00000109472"
name: "carboxypeptidase E"
location: "4q32.3"
module: 9
arm: "+"
pooled_cpm: 52.05
n_lines_expressing: 22
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 1
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CPE

*carboxypeptidase E* — 4q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.21× (z +18.2, q 0e+00, up in 19 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.03× (z +11.1, q 2e-26, up in 16 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.246×, HepG2/C3A 0.206×, NCI-H1573 0.270×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (HepG2/C3A 0.188×, SHP-77 0.359×, NCI-H1573 0.294×); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (NCI-H1573 0.235×, SHP-77 0.443×; ⚠ cell-cycle shift, would explain all of this change); [[Verteporfin (drug)]] 5 µM in 2 lines (HepG2/C3A 0.364×, SHP-77 0.440×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (NCI-H1573 0.343×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINI1]] (+0.58, fdr 1e-05), [[CALCA]] (+0.57, fdr 2e-04), [[BCHE]] (+0.56, fdr 1e-05); moves opposite to [[PHF5A]] (-0.50, fdr 2e-04), [[RIN3]] (-0.42, fdr 4e-04), [[JMJD4]] (-0.42, fdr 4e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[PPARGC1A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CFI]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3054.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.21×** | +18.2 | 0e+00 | 19/19 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.78×** | +14.1 | 6e-43 | 16/16 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.36×** | +12.4 | 5e-33 | 15/16 (NCI-H1573, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.03×** | +11.1 | 2e-26 | 16/20 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +8.3 | 1e-14 | 9/21 (HepG2/C3A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +7.0 | 2e-10 | 13/19 (HepG2/C3A, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +6.7 | 2e-09 | 15/21 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.20×** | +4.5 | 4e-04 | 8/15 (HEC-1-A, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.006 | 8/20 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.012 | 8/19 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.014 | 8/22 (A-427, HS-578T, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.38×** | +3.5 | 0.019 | 2/19 (NCI-H1573, NCI-H1792) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.054 | 11/20 (NCI-H2347, NCI-H1792, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.68× | +3.0 | 0.10 | 4/17 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3054.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.246×, HepG2/C3A 0.206×, NCI-H1573 0.270×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (HepG2/C3A 0.188×, SHP-77 0.359×, NCI-H1573 0.294×); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (NCI-H1573 0.235×, SHP-77 0.443×; ⚠ cell-cycle shift, would explain all of this change); [[Verteporfin (drug)]] 5 µM in 2 lines (HepG2/C3A 0.364×, SHP-77 0.440×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (NCI-H1573 0.343×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.727× | -3.5 | 0.14 | 14/18 (HepG2/C3A, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.546× | -3.5 | 0.14 | 6/20 (NCI-H1573, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.721× | -3.3 | 0.16 | 2/19 (A-427, HEC-1-A) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.745× | -3.3 | 0.16 | 7/20 (NCI-H1573, SHP-77, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.755× | -3.1 | 0.22 | 7/19 (HEC-1-A, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3054. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 612 | 2 (2 ⚠) | 8 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +14.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -16.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.343× (z -13.6) |
| [[SHP-77 (line)]] | alt | 776 | 1 (1 ⚠) | 7 (5 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -22.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.359× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 602 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -20.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 23.5 | 3 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.40× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 89.1 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 1.92× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 60.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +9.7) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 17.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.4× (z +11.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 39.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.25× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 30.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +9.1) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 22.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 8.99× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 30.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 22.8 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.180× (z -10.0) |
| [[A-172 (line)]] | wt | 9.13 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.97 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.16 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.80 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.84 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.18 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.45 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.57 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.04 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.09 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 11.5 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.93 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.98 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.99 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.29 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.99 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.39 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.46 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.87 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.98 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.31 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3054), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINI1]] | +0.58 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[CALCA]] | +0.57 | +0.62 / +0.31 | both halves | 2e-04 |  |
| [[BCHE]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 | pathway: Peptide hormone metabolism |
| [[POSTN]] | +0.54 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[GABRA2]] | +0.54 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[AGT]] | +0.54 | +0.58 / +0.40 | both halves | 5e-05 | pathway: Peptide hormone metabolism |
| [[FKBP7]] | +0.53 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[CHRDL1]] | +0.53 | +0.28 / +0.53 | both halves | 3e-04 |  |
| [[CFI]] | +0.52 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[PPARGC1A]] | +0.52 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[SPP1]] | +0.51 | +0.45 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[COL3A1]] | +0.51 | +0.39 / +0.44 | both halves | 5e-05 | same gene group |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF5A]] | -0.50 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[RIN3]] | -0.42 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[JMJD4]] | -0.42 | -0.25 / -0.40 | both halves | 4e-04 |  |
| [[CCDC137]] | -0.42 | -0.25 / -0.40 | both halves | 4e-04 |  |
| [[WAPL]] | -0.42 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[DPH2]] | -0.41 | -0.26 / -0.46 | both halves | 3e-04 |  |
| [[LRRC47]] | -0.40 | -0.26 / -0.43 | both halves | 4e-04 |  |
| [[ARL16]] | -0.40 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[GEMIN4]] | -0.40 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[COMMD5]] | -0.40 | -0.27 / -0.37 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPARGC1A]] | B | PPARGC1A activity raises CPE's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 2.24× lower at baseline in the lines without PPARGC1A | 0.048 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[MPZL3]] | B | MPZL3 activity raises CPE's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.53× lower at baseline in the lines without MPZL3 | 0.060 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[SCIN]] | B | SCIN activity raises CPE's level | lines that do not express SCIN (22) vs lines expressing it (28) | 1.90× lower at baseline in the lines without SCIN | 0.071 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[FRY]] | B | FRY activity raises CPE's level | lines that do not express FRY (14) vs lines expressing it (36) | 2.52× lower at baseline in the lines without FRY | 0.074 | ⚠ within organs, on part of the lines; also absent: ADGRV1, DTNA, ZNF385B |
| [[CFI]] | C | CFI activity raises CPE's level | lines that do not express CFI (31) vs lines expressing it (19) | 3.24× lower at baseline in the lines without CFI | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1; co-absent with the target |
| [[CGA]] | C | CGA activity raises CPE's level | lines that do not express CGA (44) vs lines expressing it (6) | 8.44× lower at baseline in the lines without CGA | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[IGFBP5]] | C | IGFBP5 activity raises CPE's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 2.69× lower at baseline in the lines without IGFBP5 | 0.076 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2; co-absent with the target |
| [[AMBP]] | C | AMBP activity raises CPE's level | lines that do not express AMBP (41) vs lines expressing it (9) | 3.91× lower at baseline in the lines without AMBP | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2; co-absent with the target |
| [[AGT]] | C | AGT activity raises CPE's level | lines that do not express AGT (33) vs lines expressing it (17) | 2.72× lower at baseline in the lines without AGT | 0.084 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises CPE's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 4.27× lower at baseline in the lines without RIT2 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFI]] | C | CPE activity raises CFI's level | lines that do not express CPE (28) vs lines expressing it (22) | 2.63× lower at baseline in the lines without CPE | 0.007 | ⚠ within organs, on part of the lines; also absent: PEX5L, SLC7A2, NPFFR2; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.452). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.7, 37.5); signed map (44.3, 36.8). **Vector** length 50.3, 12.3% of its response variance represented; |z| ≥ 3 in 425 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +18.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +14.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +1.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.2 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -0.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | carboxypeptidase E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.3 — chr4:165,361,194-165,498,547 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | M14 carboxypeptidases; MicroRNA protein coding host genes |
| Hallmark sets | KRAS_SIGNALING_UP, ESTROGEN_RESPONSE_LATE |
| Reactome | 2 pathways, smallest: Insulin processing; Peptide hormone metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P16870](https://www.uniprot.org/uniprotkb/P16870) (Carboxypeptidase E):

> Sorting receptor that directs prohormones to the regulated secretory pathway. Also acts as a prohormone processing enzyme in neuro/endocrine cells, removing dibasic residues from the C-terminal end of peptide hormone precursors after initial endoprotease cleavage.

**Summary**, from NCBI Gene [1363](https://www.ncbi.nlm.nih.gov/gene/1363):

> This gene encodes a member of the M14 family of metallocarboxypeptidases. The encoded preproprotein is proteolytically processed to generate the mature peptidase. This peripheral membrane protein cleaves C-terminal amino acid residues and is involved in the biosynthesis of peptide hormones and neurotransmitters, including insulin. This protein may also function independently of its peptidase activity, as a neurotrophic factor that promotes neuronal survival, and as a sorting receptor that binds …

**Accessions** — [HGNC:2303](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2303) · Entrez [1363](https://www.ncbi.nlm.nih.gov/gene/1363) · UniProt [P16870](https://www.uniprot.org/uniprotkb/P16870) · Ensembl [ENSG00000109472](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109472)

## Data

Gene col 3054: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3054); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3054, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3054]; `tensor/DDL_lfc|DDL_z.npy` [3054]; `embed/gene_vectors.npy` [3054]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3054 or target_col == 3054). Every well: [[CPE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
