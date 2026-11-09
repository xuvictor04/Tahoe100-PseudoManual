---
symbol: "DLG3"
type: "gene"
col: 1347
ensembl_id: "ENSG00000082458"
name: "discs large MAGUK scaffold protein 3"
location: "Xq13.1"
module: 8
arm: "+"
pooled_cpm: 35.8
n_lines_expressing: 43
n_dd_up: 2
n_dd_down: 29
n_dd_up_clean: 1
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 56
direction_downstream: 0
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# DLG3

*discs large MAGUK scaffold protein 3* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.29× (z +5.1, q 2e-04, up in 20 of 39 measured lines) ⚠ cell-cycle shift, explains ~15% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.28× (z +4.8, q 5e-04, up in 20 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.453× (z -22.7, q 0e+00, down in 30 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TC2N]] (+0.68, fdr 7e-06), [[EPS8L3]] (+0.63, fdr 9e-06), [[ANXA11]] (+0.61, fdr 7e-06); moves opposite to [[ZNF785]] (-0.49, fdr 4e-05), [[FAM228B]] (-0.49, fdr 1e-04), [[MME-AS1]] (-0.48, fdr 7e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 56 arrows point to it, the strongest [[CDH1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1347.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.29×** | +5.1 | 2e-04 | 20/39 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +4.8 | 5e-04 | 20/39 (NCI-H460, LoVo, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.5 | 0.077 | 14/40 (HOP62, Hs 766T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.3 | 0.14 | 7/41 (PANC-1, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1347.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.453×** | -22.7 | 0e+00 | 30/41 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.433×** | -17.0 | 0e+00 | 32/40 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.438×** | -16.8 | 0e+00 | 32/39 (BT-474, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.459×** | -15.8 | 0e+00 | 34/40 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.492×** | -13.9 | 1e-41 | 31/40 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.549×** | -12.2 | 4e-32 | 33/39 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.558×** | -11.9 | 2e-30 | 32/39 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.561×** | -11.7 | 7e-30 | 34/40 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.595×** | -10.5 | 4e-24 | 29/40 (LS 180, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.405×** | -9.6 | 5e-20 | 28/42 (KATO III, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.632×** | -9.3 | 7e-19 | 24/40 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.638×** | -9.1 | 4e-18 | 28/40 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.656×** | -8.1 | 4e-14 | 27/40 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.665×** | -8.0 | 7e-14 | 28/38 (NCI-H2030, LS 180, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.765×** | -7.7 | 7e-13 | 24/41 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -7.4 | 4e-12 | 24/39 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.717×** | -6.7 | 5e-10 | 23/40 (KATO III, LS 180, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.795×** | -6.6 | 2e-09 | 19/41 (BT-474, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.743×** | -5.7 | 4e-07 | 23/40 (COLO 205, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1347. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 48.7 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -27.3) |
| [[LS 180 (line)]] | wt | 98.0 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -23.1) |
| [[AsPC-1 (line)]] | alt | 71.0 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -17.3) |
| [[COLO 205 (line)]] | alt | 85.0 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0982× (z -25.3) |
| [[KATO III (line)]] | alt | 81.5 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -19.2) |
| [[LoVo (line)]] | wt | 61.3 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -23.3) |
| [[NCI-H1792 (line)]] | alt | 29.8 | 0 | 7 | — | [[Harringtonine (drug)]] 5 µM 0.171× (z -13.3) |
| [[BT-474 (line)]] | alt | 51.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -16.8) |
| [[HT-29 (line)]] | alt | 91.8 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -21.6) |
| [[SW480 (line)]] | alt | 66.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 44.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -21.9) |
| [[Hs 766T (line)]] | wt | 59.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -18.0) |
| [[NCI-H2347 (line)]] | alt | 39.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -16.2) |
| [[NCI-H1573 (line)]] | alt | 27.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -22.6) |
| [[SW 900 (line)]] | alt | 29.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 61.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.403× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 52.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.340× (z -10.4) |
| [[A-427 (line)]] | wt | 21.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.3) |
| [[A498 (line)]] | wt | 20.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -16.4) |
| [[HepG2_C3A (line)]] | wt | 25.8 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.184× (z -9.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.338× (z -8.5) |
| [[HOP62 (line)]] | alt | 22.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 12.3 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0790× (z -14.7) |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -9.0) |
| [[SW48 (line)]] | wt | 40.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -12.5) |
| [[AN3 CA (line)]] | alt | 50.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -9.9) |
| [[H4 (line)]] | wt | 11.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0879× (z -9.0) |
| [[HCT15 (line)]] | alt | 53.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.176× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~58% of this change |
| [[RKO (line)]] | wt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -10.5) |
| [[SHP-77 (line)]] | alt | 23.4 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.222× (z -9.2) |
| [[SW1417 (line)]] | alt | 68.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -9.6) |
| [[A-172 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.79 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.89 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.49 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.63 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.03 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.63 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1347), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TC2N]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.63 | +0.63 / +0.57 | both halves | 9e-06 | same gene group |
| [[ANXA11]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ARHGEF16]] | +0.60 | +0.61 / +0.50 | both halves | 1e-05 | same gene group |
| [[INAVA]] | +0.59 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[TANC1]] | +0.57 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ST14]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[GLCE]] | +0.57 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[POF1B]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[HNF4A]] | +0.57 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[IL22RA1]] | +0.56 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[AFAP1L2]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF785]] | -0.49 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[FAM228B]] | -0.49 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[MME-AS1]] | -0.48 | -0.45 / -0.37 | both halves | 7e-05 |  |
| [[HERC4]] | -0.48 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[DCAF10]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[TRPC1]] | -0.47 | -0.56 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 56, C 0. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDH1]] | B | CDH1 activity raises DLG3's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 3.51× lower at baseline in the lines without CDH1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[HS3ST1]] | B | HS3ST1 activity raises DLG3's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 3.29× lower at baseline in the lines without HS3ST1 | 0.002 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises DLG3's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.30× lower at baseline in the lines without TMPRSS2 | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises DLG3's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.40× lower at baseline in the lines without TMPRSS4 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[TTC22]] | B | TTC22 activity raises DLG3's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 3.21× lower at baseline in the lines without TTC22 | 0.004 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[MPZL2]] | B | MPZL2 activity raises DLG3's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 3.40× lower at baseline in the lines without MPZL2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[PLEKHG6]] | B | PLEKHG6 activity raises DLG3's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 3.16× lower at baseline in the lines without PLEKHG6 | 0.005 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[SCNN1A]] | B | SCNN1A activity raises DLG3's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 3.28× lower at baseline in the lines without SCNN1A | 0.005 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[ST14]] | B | ST14 activity raises DLG3's level | lines that do not express ST14 (32) vs lines expressing it (18) | 3.59× lower at baseline in the lines without ST14 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[JUP]] | B | JUP activity raises DLG3's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.95× lower at baseline in the lines without JUP | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[ESRP1]] | B | ESRP1 activity raises DLG3's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 3.46× lower at baseline in the lines without ESRP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[ITGB6]] | B | ITGB6 activity raises DLG3's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 3.31× lower at baseline in the lines without ITGB6 | 0.008 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.499). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.6, 53.0); signed map (60.4, 9.4). **Vector** length 93.4, 23.3% of its response variance represented; |z| ≥ 3 in 1,133 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | +5.7 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.4 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.5 | -2.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.4 | +2.2 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.6 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +4.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.3 | +0.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -11.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -15.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.1 | -12.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -17.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.4 | -16.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -11.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | discs large MAGUK scaffold protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:70,444,835-70,505,490 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NE-Dlg, SAP102, SAP-102, NEDLG, KIAA1232, MRX90, PPP1R82 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Membrane associated guanylate kinases; PDZ domain containing; SH3 domain containing |
| Reactome | 24 pathways, smallest: NrCAM interactions; Activation of Ca-permeable Kainate Receptor; Ionotropic activity of kainate receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92796](https://www.uniprot.org/uniprotkb/Q92796) (MAGUK scaffold protein DLG3):

> Post-synaptic scaffolding protein involved in the clustering of NMDA receptors (N-methyl-D-aspartate receptors, NMDARs) at excitatory synapses (By similarity). Assists in the delivery of NMDA receptors to the synaptic plasma membrane by coupling NMDAR cargo to the exocyst complex (By similarity). During synaptogenesis, mediates synaptic trafficking of both NMDA and AMPA (alpha-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid) receptors (By similarity).

**Summary**, from NCBI Gene [1741](https://www.ncbi.nlm.nih.gov/gene/1741):

> This gene encodes a member of the membrane-associated guanylate kinase protein family. The encoded protein may play a role in clustering of NMDA receptors at excitatory synapses. It may also negatively regulate cell proliferation through interaction with the C-terminal region of the adenomatosis polyposis coli tumor suppressor protein. Mutations in this gene have been associated with X-linked cognitive disability. Alternatively spliced transcript variants have been described. [provided by …

**Accessions** — [HGNC:2902](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2902) · Entrez [1741](https://www.ncbi.nlm.nih.gov/gene/1741) · UniProt [Q92796](https://www.uniprot.org/uniprotkb/Q92796) · Ensembl [ENSG00000082458](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082458)

## Data

Gene col 1347: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1347); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1347, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1347]; `tensor/DDL_lfc|DDL_z.npy` [1347]; `embed/gene_vectors.npy` [1347]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1347 or target_col == 1347). Every well: [[DLG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
