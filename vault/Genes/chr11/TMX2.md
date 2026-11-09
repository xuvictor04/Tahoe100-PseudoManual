---
symbol: "TMX2"
type: "gene"
col: 13116
ensembl_id: "ENSG00000213593"
name: "thioredoxin related transmembrane protein 2"
location: "11q12.1"
module: 5
arm: "+"
pooled_cpm: 56.08
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TMX2

*thioredoxin related transmembrane protein 2* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (15 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.84× (z +14.7, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.781× (z -7.3, q 1e-10, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERH]] (+0.63, fdr 1e-05), [[ACAD9]] (+0.63, fdr 1e-05), [[VPS51]] (+0.62, fdr 1e-05); moves opposite to [[ABI1]] (-0.57, fdr 6e-05), [[PEAK1]] (-0.54, fdr 2e-05), [[STRN]] (-0.50, fdr 7e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 17 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13116.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.84×** | +14.7 | 0e+00 | 47/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.85×** | +11.4 | 9e-28 | 42/48 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.60×** | +9.8 | 2e-20 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.51×** | +8.5 | 2e-15 | 35/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.49×** | +8.3 | 1e-14 | 34/48 (NCI-H460, LoVo, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.48×** | +7.8 | 6e-13 | 31/48 (NCI-H1792, LoVo, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.29×** | +7.5 | 5e-12 | 28/48 (NCI-H1792, LOX-IMVI, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.40×** | +7.1 | 1e-10 | 32/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.40×** | +7.0 | 2e-10 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.43×** | +7.0 | 2e-10 | 27/45 (LoVo, LS 180, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +6.7 | 1e-09 | 35/48 (SW480, SNU-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.79×** | +6.3 | 1e-08 | 25/37 (NCI-H1573, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.35×** | +6.0 | 8e-08 | 24/41 (LS 180, HOP62, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +5.8 | 3e-07 | 29/48 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +5.8 | 3e-07 | 28/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +4.6 | 1e-04 | 26/48 (NCI-H1792, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +4.2 | 7e-04 | 22/47 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.47×** | +4.2 | 8e-04 | 19/48 (PANC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.001 | 19/48 (NCI-H1792, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.002 | 19/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.004 | 20/48 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.005 | 17/48 (NCI-H460, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.008 | 14/48 (NCI-H460, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.029 | 16/48 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.034 | 14/48 (MIA PaCa-2, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.22×** | +2.9 | 0.059 | 9/48 (LOX-IMVI, C32, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13116.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.781×** | -7.3 | 1e-10 | 34/48 (A498, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.737×** | -6.4 | 4e-08 | 27/48 (SW1417, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 0.853× | -4.7 | 4e-04 | 20/48 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.808×** | -4.5 | 1e-03 | 22/48 (SW 1088, NCI-H2347, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.809×** | -4.3 | 0.002 | 23/47 (SNU-423, C-33 A, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.696×** | -4.0 | 0.006 | 18/49 (LoVo, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.832×** | -3.9 | 0.008 | 21/48 (PANC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.835× | -3.8 | 0.009 | 15/47 (SW48, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.8 | 0.009 | 18/48 (PANC-1, SW1417, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~99% of this change | 0.850× | -3.4 | 0.033 | 19/48 (LoVo, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -3.2 | 0.068 | 21/48 (PANC-1, SW1417, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.867× | -3.0 | 0.12 | 9/48 (KATO III, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13116. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 67.2 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +13.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.03× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 49.0 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.48× (z +10.1) | — |
| [[LoVo (line)]] | wt | 52.7 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.33× (z +11.3) | — |
| [[A-427 (line)]] | wt | 75.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HOP62 (line)]] | alt | 52.9 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.63× (z +9.7) | — |
| [[KATO III (line)]] | alt | 59.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.31× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 49.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.2) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.07× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 44.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.60× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 76.7 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +9.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW1417 (line)]] | alt | 89.6 | 1 | 1 | [[TAK-901 (drug)]] 0.05 µM 2.28× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.496× (z -8.8) |
| [[AN3 CA (line)]] | alt | 65.0 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.132× (z -8.7) ⚠ toxic |
| [[C-33 A (line)]] | alt | 73.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.15× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 43.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.27× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 45.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.0× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 50.3 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +9.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1573 (line)]] | alt | 42.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.59× (z +9.2) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[NCI-H1792 (line)]] | alt | 85.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.9) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[NCI-H2030 (line)]] | alt | 66.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.2) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[NCI-H23 (line)]] | alt | 49.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.70× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H460 (line)]] | wt | 38.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A-172 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13116), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERH]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[ACAD9]] | +0.63 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[VPS51]] | +0.62 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[LSM1]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[MAGOH]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[TMEM138]] | +0.60 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[DNAAF5]] | +0.59 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[MAPKAPK5]] | +0.59 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ZNF587B]] | +0.59 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[TSN]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[GCN1]] | +0.57 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[MLH1]] | +0.56 | +0.38 / +0.57 | both halves | 7e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABI1]] | -0.57 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[PEAK1]] | -0.54 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[STRN]] | -0.50 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[OAZ1]] | -0.50 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[USP53]] | -0.50 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[AFDN]] | -0.50 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[MEF2A]] | -0.48 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[CBL]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[KRAS]] | -0.48 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[RAPGEF2]] | -0.46 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[OSBPL9]] | -0.46 | -0.30 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TMX2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises TMX2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.415). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-25.3, -11.3); signed map (-32.5, -29.4). **Vector** length 81.5, 19.6% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +14.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +4.5 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +4.0 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +6.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +4.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -7.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | -3.9 | +3.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | -3.5 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -2.9 | -4.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~99% of this change | -2.7 | -3.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | +1.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | thioredoxin related transmembrane protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:57,712,580-57,742,987 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PDIA12; previously TXNDC14 |
| Gene groups (HGNC) | Protein disulfide isomerases; Thioredoxin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y320](https://www.uniprot.org/uniprotkb/Q9Y320) (Thioredoxin-related transmembrane protein 2):

> Endoplasmic reticulum and mitochondria-associated protein that probably functions as a regulator of cellular redox state and thereby regulates protein post-translational modification, protein folding and mitochondrial activity. Indirectly regulates neuronal proliferation, migration, and organization in the developing brain.

**Summary**, from NCBI Gene [51075](https://www.ncbi.nlm.nih.gov/gene/51075):

> This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, a catalytically active thioredoxin domain, one transmembrane domain and a C-terminal ER-retention sequence. This protein is enriched on the mitochondria-associated-membrane of the ER via palmitoylation of two of its cytosolically exposed cysteines. [provided by …

**Accessions** — [HGNC:30739](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30739) · Entrez [51075](https://www.ncbi.nlm.nih.gov/gene/51075) · UniProt [Q9Y320](https://www.uniprot.org/uniprotkb/Q9Y320) · Ensembl [ENSG00000213593](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213593)

## Data

Gene col 13116: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13116); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13116, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13116]; `tensor/DDL_lfc|DDL_z.npy` [13116]; `embed/gene_vectors.npy` [13116]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13116 or target_col == 13116). Every well: [[TMX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
