---
symbol: "FIG4"
type: "gene"
col: 3364
ensembl_id: "ENSG00000112367"
name: "FIG4 phosphoinositide 5-phosphatase"
location: "6q21"
module: 65
arm: "+"
pooled_cpm: 40.95
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# FIG4

*FIG4 phosphoinositide 5-phosphatase* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.67× (z +8.8, q 8e-16, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (14 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.537× (z -10.6, q 1e-23, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LTA4H]] (+0.70, fdr 7e-06), [[STX7]] (+0.67, fdr 7e-06), [[MINDY3]] (+0.67, fdr 7e-06); moves opposite to [[AGAP6]] (-0.57, fdr 2e-05), [[WDR82]] (-0.56, fdr 4e-05), [[PPRC1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ENPP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3364.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +8.8 | 8e-16 | 36/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +8.1 | 1e-13 | 36/48 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +7.5 | 2e-11 | 33/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.31×** | +6.6 | 7e-09 | 29/48 (LoVo, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.38×** | +5.5 | 5e-06 | 26/48 (LoVo, BT-474, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.57×** | +4.0 | 0.005 | 21/48 (A-427, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.0 | 0.006 | 23/48 (hTERT-HPNE, A498, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +3.8 | 0.010 | 18/48 (BT-474, SK-MEL-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.25×** | +3.8 | 0.010 | 19/48 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.010 | 15/48 (SK-MEL-2, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.21×** | +3.3 | 0.052 | 12/48 (SNU-423, SW 900, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.079 | 10/48 (J82, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3364.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.537×** | -10.6 | 1e-23 | 39/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.546×** | -9.6 | 3e-19 | 29/45 (NCI-H2347, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.574×** | -9.5 | 4e-19 | 37/47 (SW480, SW48, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.595×** | -8.9 | 9e-17 | 34/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.606×** | -8.6 | 1e-15 | 33/48 (KATO III, NCI-H1792, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.638×** | -7.7 | 2e-12 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.748×** | -7.0 | 2e-10 | 28/48 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.760×** | -6.6 | 2e-09 | 26/48 (NCI-H1792, HEC-1-A, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.691×** | -6.3 | 2e-08 | 32/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.544×** | -5.5 | 3e-06 | 25/49 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **0.743×** | -4.9 | 5e-05 | 21/40 (NCI-H1792, NCI-H1573, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.757×** | -4.8 | 9e-05 | 23/48 (NCI-H1792, H4, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.752×** | -4.7 | 1e-04 | 23/48 (MIA PaCa-2, KATO III, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | **0.757×** | -4.6 | 2e-04 | 23/47 (MIA PaCa-2, SW 1271, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.611×** | -4.4 | 4e-04 | 20/43 (HEC-1-A, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.789×** | -4.0 | 0.002 | 21/48 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.667×** | -3.6 | 0.010 | 21/48 (MIA PaCa-2, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **0.818×** | -3.3 | 0.026 | 12/47 (SW 1271, NCI-H1573, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **0.828×** | -3.1 | 0.051 | 13/48 (RPMI-7951, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.827×** | -3.1 | 0.057 | 13/48 (AN3 CA, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 5 µM |  | 0.882× | -3.0 | 0.061 | 9/48 (HOP62, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3364. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 54.1 | 0 | 10 (9 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.264× (z -16.4) |
| [[NCI-H460 (line)]] | wt | 25.9 | 0 | 8 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.261× (z -13.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.411× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 55.3 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -15.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 50.5 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -17.9) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 58.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[LS 180 (line)]] | wt | 57.6 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.196× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[MIA PaCa-2 (line)]] | alt | 45.8 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.237× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 46.1 | 0 | 4 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0382× (z -17.5) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 48.9 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.225× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 36.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -10.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -8.8) |
| [[LoVo (line)]] | wt | 30.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.259× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[NCI-H1573 (line)]] | alt | 31.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[RKO (line)]] | wt | 47.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[RPMI-7951 (line)]] | alt | 39.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -14.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 99.5 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.291× (z -11.7) |
| [[A498 (line)]] | wt | 17.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.231× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[C32 (line)]] | wt | 49.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 39.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -8.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HCT15 (line)]] | alt | 62.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.227× (z -10.9) |
| [[HOP62 (line)]] | alt | 23.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.255× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 59.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 48.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.436× (z -8.6) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SW48 (line)]] | wt | 30.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0850× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3364), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTA4H]] | +0.70 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[STX7]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ATP6V1B2]] | +0.65 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[UBXN2B]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[MTX2]] | +0.63 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[CMC1]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[PREPL]] | +0.62 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[DUSP11]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[DNAJC19]] | +0.61 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[RAB8B]] | +0.60 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[ALG9]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGAP6]] | -0.57 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[WDR82]] | -0.56 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[PPRC1]] | -0.56 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[CRK]] | -0.55 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[HNRNPAB]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[SPEN]] | -0.53 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[CHSY3]] | -0.52 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[GBX2-AS1]] | -0.52 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[NR2F1-AS1]] | -0.52 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[NID1]] | -0.52 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[PHF23]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[SATB2]] | -0.52 | -0.51 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENPP4]] | B | ENPP4 activity raises FIG4's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 1.36× lower at baseline in the lines without ENPP4 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers FIG4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers FIG4's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.668). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-4.6, -9.5); signed map (-31.5, -13.2). **Vector** length 92.5, 23.2% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +6.7 | +6.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +4.7 | +5.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +8.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +7.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.3 | +1.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.0 | +1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.9 | +3.8 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +0.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.4 | -10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.7 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.2 | -7.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.0 | -4.4 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.3 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | FIG4 phosphoinositide 5-phosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:109,690,609-109,878,098 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SAC3, hSac3, dJ249I4.1, ALS11, CMT4J; previously KIAA0274 |
| Gene groups (HGNC) | Phosphoinositide phosphatases |
| Reactome | 6 pathways, smallest: Synthesis of PIPs at the late endosome membrane; Synthesis of PIPs at the early endosome membrane; Synthesis of PIPs at the Golgi membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92562](https://www.uniprot.org/uniprotkb/Q92562) (Polyphosphoinositide phosphatase):

> Dual specificity phosphatase component of the PI(3,5)P2 regulatory complex which regulates both the synthesis and turnover of phosphatidylinositol 3,5-bisphosphate (PtdIns(3,5)P2). Catalyzes the dephosphorylation of phosphatidylinositol 3,5-bisphosphate (PtdIns(3,5)P2) to form phosphatidylinositol 3-phosphate. Has serine-protein phosphatase activity acting on PIKfyve to stimulate its lipid kinase activity, its catalytically activity being required for maximal PI(3,5)P2 production. In vitro, …

**Summary**, from NCBI Gene [9896](https://www.ncbi.nlm.nih.gov/gene/9896):

> The protein encoded by this gene belongs to the SAC domain-containing protein gene family. The SAC domain, approximately 400 amino acids in length and consisting of seven conserved motifs, has been shown to possess phosphoinositide phosphatase activity. The yeast homolog, Sac1p, is involved in the regulation of various phosphoinositides, and affects diverse cellular functions such as actin cytoskeleton organization, Golgi function, and maintenance of vacuole morphology. Membrane-bound …

**Accessions** — [HGNC:16873](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16873) · Entrez [9896](https://www.ncbi.nlm.nih.gov/gene/9896) · UniProt [Q92562](https://www.uniprot.org/uniprotkb/Q92562) · Ensembl [ENSG00000112367](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112367)

## Data

Gene col 3364: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3364); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3364, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3364]; `tensor/DDL_lfc|DDL_z.npy` [3364]; `embed/gene_vectors.npy` [3364]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3364 or target_col == 3364). Every well: [[FIG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FIG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
