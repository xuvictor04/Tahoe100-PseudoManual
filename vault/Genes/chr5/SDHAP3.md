---
symbol: "SDHAP3"
type: "gene"
col: 11762
ensembl_id: "ENSG00000185986"
name: "SDHA pseudogene 3"
location: "5p15.33"
module: 1
arm: "+"
pooled_cpm: 17.29
n_lines_expressing: 42
n_dd_up: 0
n_dd_down: 31
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SDHAP3

*SDHA pseudogene 3* — 5p15.33

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (20 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.392× (z -13.0, q 8e-36, down in 33 of 39 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.589× (z -10.4, q 5e-23, down in 31 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZP3]] (+0.52, fdr 2e-05), [[JPX]] (+0.50, fdr 3e-05), [[PDCD6P1]] (+0.49, fdr 2e-05, ⚠ same locus), [[LINC01341]] (+0.49, fdr 3e-05); moves opposite to [[SYTL3]] (-0.51, fdr 4e-05), [[LINC01615]] (-0.47, fdr 5e-05), [[PAMR1]] (-0.45, fdr 2e-04).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC01615]] → it (grade B ⚠); 4 go from it, the strongest it → [[LINC01615]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11762.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rifaximin (drug)]] 5 µM |  | 1.28× | +3.3 | 0.31 | 12/39 (NCI-H460, SW48, …) | rises with dose | position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.26× | +3.2 | 0.31 | 3/39 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.27× | +3.1 | 0.31 | 7/40 (HEC-1-A, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 21 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11762.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.392×** | -13.0 | 8e-36 | 33/39 (PANC-1, BT-474, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.440×** | -10.9 | 2e-25 | 26/37 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.578×** | -10.7 | 1e-24 | 25/38 (HT-29, C32, …) | rises with dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.589×** | -10.4 | 5e-23 | 31/39 (MIA PaCa-2, SW 900, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.477×** | -10.3 | 1e-22 | 32/37 (PANC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.545×** | -8.1 | 8e-14 | 26/39 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.568×** | -7.8 | 4e-13 | 29/39 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.564×** | -7.6 | 2e-12 | 29/39 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.578×** | -7.2 | 5e-11 | 25/39 (CHP-212, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.420×** | -6.3 | 2e-08 | 27/39 (BT-474, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.676×** | -5.4 | 3e-06 | 24/39 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.671×** | -5.3 | 5e-06 | 21/39 (SW480, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.705×** | -4.7 | 1e-04 | 23/39 (Panc 03.27, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **0.716×** | -4.6 | 2e-04 | 19/36 (HCT15, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.718×** | -4.6 | 2e-04 | 18/39 (NCI-H460, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.709×** | -4.6 | 2e-04 | 21/39 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.551×** | -4.3 | 5e-04 | 15/37 (MIA PaCa-2, HCT15, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.736×** | -4.2 | 7e-04 | 17/37 (PANC-1, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.751×** | -3.8 | 0.003 | 20/39 (AN3 CA, SW480, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.782×** | -3.3 | 0.023 | 11/40 (SW 1088, NCI-H460, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.802×** | -3.1 | 0.044 | 11/39 (C32, HT-29, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.679×** | -2.8 | 0.089 | 7/39 (NCI-H1792, SW480, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11762. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 38.3 | 0 | 9 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -19.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 50.4 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -17.3) |
| [[NCI-H460 (line)]] | wt | 13.6 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.131× (z -13.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 11.5 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.296× (z -8.5) |
| [[BT-474 (line)]] | alt | 59.4 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -11.9) |
| [[A549 (line)]] | wt | 15.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -10.1) ⚠ cell-cycle shift, explains ~45% of this change |
| [[AN3 CA (line)]] | alt | 26.1 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0965× (z -8.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.101× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 39.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -10.9) |
| [[HT-29 (line)]] | alt | 13.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -17.0) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H1573 (line)]] | alt | 5.12 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -9.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0977× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 20.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.154× (z -11.8) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 27.2 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.235× (z -9.2) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 42.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 22.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0729× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 29.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -13.7) |
| [[A-427 (line)]] | wt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -9.2) ⚠ cell-cycle shift, explains ~45% of this change |
| [[C32 (line)]] | wt | 16.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -14.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[CFPAC-1 (line)]] | alt | 26.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -13.4) |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0807× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[HepG2_C3A (line)]] | wt | 41.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -10.0) |
| [[HOP62 (line)]] | alt | 6.55 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.160× (z -8.7) |
| [[Hs 766T (line)]] | wt | 9.61 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0427× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 9.65 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0750× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H661 (line)]] | alt | 44.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0520× (z -9.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0823× (z -12.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11762), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZP3]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[JPX]] | +0.50 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[PDCD6P1]] | +0.49 | +0.57 / +0.48 | both halves | 2e-05 | ⚠ same locus (5.6 kb, same strand: neighbours can correlate without regulation) |
| [[LINC01341]] | +0.49 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[METAP1D]] | +0.49 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[ZNF839]] | +0.48 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[C5orf63]] | +0.48 | +0.47 / +0.38 | both halves | 6e-05 |  |
| [[RAD51D]] | +0.48 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[LINC01029]] | +0.47 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[EIF3A]] | +0.46 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[TGFBRAP1]] | +0.46 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[ACSF3]] | +0.45 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[GUCY1B2]] | +0.44 | +0.35 / +0.46 | both halves | 1e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYTL3]] | -0.51 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[LINC01615]] | -0.47 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[PAMR1]] | -0.45 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[GLUD1]] | -0.42 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[TGFB1]] | -0.42 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[STK17B]] | -0.41 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[AAMDC]] | -0.41 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[LINC01500]] | -0.41 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[SNHG18]] | -0.41 | -0.50 / -0.26 | both halves | 4e-04 |  |
| [[HOOK3]] | -0.41 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[THBS2]] | -0.40 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[CNPY4]] | -0.40 | -0.24 / -0.40 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01615]] | B | LINC01615 activity lowers SDHAP3's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 2.72× higher at baseline in the lines without LINC01615 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC |
| [[NR5A2]] | B | NR5A2 activity raises SDHAP3's level | lines that do not express NR5A2 (33) vs lines expressing it (17) | 1.90× lower at baseline in the lines without NR5A2 | 0.078 | ⚠ within organs, on part of the lines; also absent: FGA, ENSG00000237031, CYP24A1 |
| [[PDGFRB]] | B | PDGFRB activity lowers SDHAP3's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.12× higher at baseline in the lines without PDGFRB | 0.095 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[PDCD6P1]] | C | PDCD6P1 activity raises SDHAP3's level | lines that do not express PDCD6P1 (4) vs lines expressing it (46) | 5.39× lower at baseline in the lines without PDCD6P1 | 0.004 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: NSUN5, KIAA1671, ENSG00000291079; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01615]] | B | SDHAP3 activity lowers LINC01615's level | lines that do not express SDHAP3 (8) vs lines expressing it (42) | 3.64× higher at baseline in the lines without SDHAP3 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000291079, PHKA1, C1orf115 |
| [[IRS1]] | B | SDHAP3 activity raises IRS1's level | lines that do not express SDHAP3 (8) vs lines expressing it (42) | 2.45× lower at baseline in the lines without SDHAP3 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000291079, PHKA1, C1orf115 |
| [[SYTL3]] | B | SDHAP3 activity lowers SYTL3's level | lines that do not express SDHAP3 (8) vs lines expressing it (42) | 2.45× higher at baseline in the lines without SDHAP3 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000291079, PHKA1, C1orf115 |
| [[PDCD6P1]] | C | SDHAP3 activity raises PDCD6P1's level | lines that do not express SDHAP3 (8) vs lines expressing it (42) | 3.21× lower at baseline in the lines without SDHAP3 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000291079, PHKA1, C1orf115; co-absent with the target |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.437). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-31.8, 25.2); signed map (5.0, -42.5). **Vector** length 56.1, 8.64% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | -1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +0.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.1 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -10.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.8 | -10.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.8 | -4.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.6 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.0 | -2.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -0.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | SDHA pseudogene 3 |
| Locus type | pseudogene |
| Location | 5p15.33 — chr5:1,572,222-1,593,289 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously SDHAL, SDHACL |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:18781](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18781) · Entrez [728609](https://www.ncbi.nlm.nih.gov/gene/728609) · Ensembl [ENSG00000185986](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185986)

## Data

Gene col 11762: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11762); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11762, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11762]; `tensor/DDL_lfc|DDL_z.npy` [11762]; `embed/gene_vectors.npy` [11762]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11762 or target_col == 11762). Every well: [[SDHAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDHAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
