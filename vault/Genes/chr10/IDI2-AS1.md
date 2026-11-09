---
symbol: "IDI2-AS1"
type: "gene"
col: 13858
ensembl_id: "ENSG00000232656"
name: "IDI2 antisense RNA 1"
location: "10p15.3"
module: 38
arm: "+"
pooled_cpm: 16.01
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 14
n_dd_up_clean: 21
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# IDI2-AS1

*IDI2 antisense RNA 1* — 10p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.30× (z +15.7, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.619× (z -4.5, q 0.004, down in 26 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.410× (z -4.3, q 0.004, down in 23 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYOCOS]] (+0.88, fdr 7e-06), [[PPIEL]] (+0.88, fdr 7e-06), [[PPIEL-1]] (+0.87, fdr 7e-06); moves opposite to [[HMGN3]] (-0.67, fdr 4e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PXMP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13858.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.30×** | +15.7 | 0e+00 | 41/47 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.12×** | +14.9 | 0e+00 | 44/45 (HOP62, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.65×** | +12.0 | 6e-31 | 41/45 (SW480, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.53×** | +11.7 | 2e-29 | 39/43 (RPMI-7951, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.57×** | +8.4 | 4e-15 | 36/43 (CFPAC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +8.0 | 1e-13 | 34/45 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +7.8 | 7e-13 | 38/45 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.01×** | +6.5 | 7e-09 | 37/48 (SW480, A498, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +6.2 | 3e-08 | 26/47 (A-172, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.91×** | +6.0 | 1e-07 | 35/47 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.85×** | +5.7 | 6e-07 | 26/47 (NCI-H2347, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +4.8 | 6e-05 | 25/46 (COLO 205, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.75×** | +4.5 | 3e-04 | 28/46 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.52×** | +4.5 | 3e-04 | 14/24 (A549, A-427, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.53×** | +3.9 | 0.003 | 20/47 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.015 | 13/48 (RKO, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.019 | 16/48 (NCI-H1573, KATO III, …) | rises with dose | position effect removed |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.019 | 10/47 (NCI-H460, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13858.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.619×** | -4.5 | 0.004 | 26/45 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.410×** | -4.3 | 0.004 | 23/43 (BT-474, AsPC-1, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.732×** | -4.1 | 0.007 | 22/48 (AsPC-1, RKO, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.650×** | -3.9 | 0.016 | 19/42 (LoVo, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bexarotene (drug)]] 5 µM |  | **0.666×** | -3.8 | 0.018 | 20/47 (HS-578T, J82, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.671×** | -3.7 | 0.019 | 18/47 (AsPC-1, SNU-1, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.637×** | -3.7 | 0.021 | 14/45 (PANC-1, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.684×** | -3.5 | 0.029 | 17/47 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.731×** | -3.5 | 0.030 | 20/47 (SW48, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Ferulic acid (drug)]] 0.5 µM |  | **0.695×** | -3.4 | 0.039 | 12/45 (SNU-423, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.687×** | -3.4 | 0.039 | 16/46 (LoVo, HEC-1-A, …) | all doses, flat |  |
| [[Neratinib (drug)]] 5 µM |  | **0.712×** | -3.2 | 0.071 | 14/47 (BT-474, J82, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.708×** | -3.1 | 0.084 | 16/46 (CHP-212, SNU-1, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.795×** | -3.0 | 0.099 | 18/48 (COLO 205, LOX-IMVI, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13858. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.9 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +12.5) | — |
| [[HOP62 (line)]] | alt | 9.50 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.16× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 27.1 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.0218× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.147× (z -8.7) |
| [[A-172 (line)]] | wt | 5.76 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +11.8) | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.0801× (z -8.7) |
| [[LoVo (line)]] | wt | 36.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +11.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.173× (z -12.1) ⚠ toxic |
| [[SW480 (line)]] | alt | 14.0 | 4 | 0 | [[Auranofin (drug)]] 5 µM 8.29× (z +12.9) | — |
| [[CFPAC-1 (line)]] | alt | 12.7 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.35× (z +11.9) | — |
| [[KATO III (line)]] | alt | 19.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0858× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.165× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 17.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.11× (z +12.8) | — |
| [[PANC-1 (line)]] | alt | 10.7 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.102× (z -11.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 22.2 | 1 | 1 | [[Auranofin (drug)]] 5 µM 5.32× (z +10.1) | [[Verteporfin (drug)]] 5 µM 0.198× (z -9.5) |
| [[Hs 766T (line)]] | wt | 7.61 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.03× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 12.1 | 2 | 0 | [[Auranofin (drug)]] 5 µM 8.32× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 15.6× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 14.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +12.0) | — |
| [[NCI-H23 (line)]] | alt | 29.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 49.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.77× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 6.65 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.06× (z +10.8) | — |
| [[SW 900 (line)]] | alt | 12.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +9.0) | — |
| [[A549 (line)]] | wt | 12.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.05× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 18.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.23× (z +12.9) | — |
| [[COLO 205 (line)]] | alt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.83× (z +10.5) | — |
| [[HepG2_C3A (line)]] | wt | 23.5 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0980× (z -9.4) |
| [[HS-578T (line)]] | alt | 8.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +9.6) | — |
| [[J82 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -8.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 5.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.90× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 6.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.85× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 22.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +13.4) | — |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 1 | — | [[Sulfisoxazole (drug)]] 0.5 µM 0.0453× (z -10.9) |
| [[A-427 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13858), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYOCOS]] | +0.88 | +0.90 / +0.76 | both halves | 7e-06 |  |
| [[PPIEL]] | +0.88 | +0.88 / +0.84 | both halves | 7e-06 |  |
| [[PPIEL-1]] | +0.87 | +0.87 / +0.83 | both halves | 7e-06 |  |
| [[ARL9]] | +0.84 | +0.83 / +0.78 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.84 | +0.84 / +0.78 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.83 | +0.86 / +0.70 | both halves | 7e-06 |  |
| [[PILRA]] | +0.82 | +0.86 / +0.75 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.81 | +0.84 / +0.70 | both halves | 7e-06 |  |
| [[PLAC8L1]] | +0.81 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.80 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.80 | +0.85 / +0.63 | both halves | 7e-06 |  |
| [[MPP4]] | +0.79 | +0.82 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGN3]] | -0.67 | -0.68 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PXMP4]] | B | PXMP4 activity lowers IDI2-AS1's level | lines that do not express PXMP4 (6) vs lines expressing it (44) | 1.86× higher at baseline in the lines without PXMP4 | 0.025 | ⚠ within organs, on part of the lines; also absent: ZNF532 |
| [[IMPA1P1]] | B | IMPA1P1 activity raises IDI2-AS1's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.93× lower at baseline in the lines without IMPA1P1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers IDI2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MYH15]] | B | MYH15 activity raises IDI2-AS1's level | lines that do not express MYH15 (10) vs lines expressing it (40) | 1.39× lower at baseline in the lines without MYH15 | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers IDI2-AS1's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 6.4% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[EOGT]] | C | EOGT's natural level weakens IDI2-AS1's drug response | EOGT's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.11; direction not clear | 0.062 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM72]] | C | TRIM72 activity raises IDI2-AS1's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.83× lower at baseline in the lines without TRIM72 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.857). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.9, -15.7); signed map (16.0, 9.6). **Vector** length 129, 38.1% of its response variance represented; |z| ≥ 3 in 1,268 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.4 | +12.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +14.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +15.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +6.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.8 | +6.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.6 | +4.5 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +3.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.7 | -0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.5 | -0.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.0 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.9 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -4.8 | -3.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.6 | -2.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.6 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | IDI2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10p15.3 — chr10:1,022,618-1,045,425 (+) |
| Ensembl biotype | lncRNA |
| Also known as | HT009, Em:AC022536.4; previously C10orf110, IDI2-AS |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q9NZ38](https://www.uniprot.org/uniprotkb/Q9NZ38) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:30885](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30885) · Entrez [55853](https://www.ncbi.nlm.nih.gov/gene/55853) · UniProt [Q9NZ38](https://www.uniprot.org/uniprotkb/Q9NZ38) · Ensembl [ENSG00000232656](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232656)

## Data

Gene col 13858: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13858); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13858, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13858]; `tensor/DDL_lfc|DDL_z.npy` [13858]; `embed/gene_vectors.npy` [13858]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13858 or target_col == 13858). Every well: [[IDI2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IDI2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
