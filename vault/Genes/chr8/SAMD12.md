---
symbol: "SAMD12"
type: "gene"
col: 10835
ensembl_id: "ENSG00000177570"
name: "sterile alpha motif domain containing 12"
location: "8q24.11-q24.12"
module: 8
arm: "+"
pooled_cpm: 148.03
n_lines_expressing: 30
n_dd_up: 28
n_dd_down: 25
n_dd_up_clean: 26
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 62
direction_downstream: 59
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SAMD12

*sterile alpha motif domain containing 12* — 8q24.11-q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.55× (z +11.3, q 8e-27, up in 15 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.389× (z -17.1, q 0e+00, down in 26 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD12-AS1]] (+0.74, fdr 7e-06, ⚠ same locus), [[CCSER1]] (+0.74, fdr 7e-06), [[PLCH1]] (+0.69, fdr 7e-06), [[SYNPR-AS1]] (+0.68, fdr 7e-06); moves opposite to [[FAM228B]] (-0.54, fdr 2e-05), [[EPOR]] (-0.49, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 62 arrows point to it, the strongest [[HNF1B]] → it (grade B ⚠); 59 go from it, the strongest it → [[RAB3IP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10835.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +11.3 | 8e-27 | 15/28 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +10.2 | 4e-22 | 17/29 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +10.1 | 1e-21 | 16/28 (PANC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.71×** | +9.3 | 1e-18 | 25/28 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.42×** | +6.5 | 1e-08 | 20/29 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +6.2 | 6e-08 | 22/28 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +6.1 | 1e-07 | 19/28 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +5.1 | 2e-05 | 21/28 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +5.1 | 2e-05 | 15/28 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.31×** | +5.0 | 3e-05 | 21/30 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.31×** | +4.9 | 5e-05 | 13/28 (SW 900, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +4.8 | 1e-04 | 13/29 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +4.7 | 1e-04 | 17/28 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.3 | 7e-04 | 14/28 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.002 | 19/29 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.26×** | +3.9 | 0.003 | 15/28 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10835.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.389×** | -17.1 | 0e+00 | 26/28 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.427×** | -15.4 | 0e+00 | 25/28 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.428×** | -15.4 | 0e+00 | 25/28 (NCI-H23, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.421×** | -15.1 | 0e+00 | 28/28 (HT-29, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.587×** | -9.7 | 5e-20 | 26/28 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.399×** | -8.7 | 3e-16 | 25/29 (A-427, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.430×** | -8.0 | 1e-13 | 21/28 (Panc 03.27, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.647×** | -7.9 | 2e-13 | 22/28 (COLO 205, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.647×** | -7.9 | 2e-13 | 24/28 (HT-29, Panc 03.27, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.726×** | -5.8 | 3e-07 | 15/28 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.731×** | -5.7 | 7e-07 | 22/28 (HT-29, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.824×** | -5.0 | 3e-05 | 24/29 (KATO III, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.769×** | -4.6 | 2e-04 | 19/28 (CFPAC-1, NCI-H2030, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.779×** | -4.5 | 3e-04 | 18/28 (HT-29, SW48, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.788×** | -4.3 | 6e-04 | 16/28 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.635×** | -4.3 | 6e-04 | 16/28 (RKO, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.872× | -3.5 | 0.011 | 16/29 (CFPAC-1, NCI-H2030, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.826×** | -3.5 | 0.012 | 11/29 (BT-474, KATO III, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10835. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 1,236 | 0 | 17 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0672× (z -26.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.163× (z -18.5) |
| [[KATO III (line)]] | alt | 552 | 0 | 16 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.113× (z -21.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -18.3) |
| [[Panc 03.27 (line)]] | alt | 465 | 0 | 16 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.204× (z -15.5) |
| [[RKO (line)]] | wt | 304 | 0 | 16 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0597× (z -24.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -15.6) |
| [[SW1417 (line)]] | alt | 172 | 0 | 15 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.142× (z -18.2) |
| [[AsPC-1 (line)]] | alt | 120 | 12 (1 ⚠) | 0 | [[Trametinib (drug)]] 0.5 µM 4.48× (z +15.2) | — |
| [[PANC-1 (line)]] | alt | 40.4 | 6 (2 ⚠) | 6 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.79× (z +15.0) | [[Digitoxin (drug)]] 5 µM 0.292× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.324× (z -11.7) |
| [[COLO 205 (line)]] | alt | 572 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0992× (z -37.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -21.8) |
| [[NCI-H23 (line)]] | alt | 86.6 | 0 | 10 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -15.8) |
| [[SW48 (line)]] | wt | 187 | 0 | 10 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.223× (z -11.7) |
| [[A-427 (line)]] | wt | 41.2 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0385× (z -16.1) |
| [[J82 (line)]] | alt | 363 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -16.0) |
| [[LoVo (line)]] | wt | 131 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -24.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -20.5) |
| [[NCI-H1573 (line)]] | alt | 148 | 2 | 6 (3 ⚠) | [[Cobimetinib (drug)]] 5 µM 3.17× (z +9.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -14.3) |
| [[NCI-H2030 (line)]] | alt | 154 | 0 | 8 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0986× (z -18.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -15.9) |
| [[SHP-77 (line)]] | alt | 180 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -17.1) |
| [[LS 180 (line)]] | wt | 277 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -16.4) |
| [[BT-474 (line)]] | alt | 468 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -14.0) |
| [[SW 900 (line)]] | alt | 76.6 | 1 | 4 (2 ⚠) | [[Panobinostat (drug)]] 0.05 µM 2.76× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -11.6) |
| [[SW480 (line)]] | alt | 47.4 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.320× (z -11.6) |
| [[HCT15 (line)]] | alt | 170 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 64.3 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 254 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.259× (z -13.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 264 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.381× (z -11.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.489× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 66.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.325× (z -9.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 37.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.38× (z +8.5) | — |
| [[A-172 (line)]] | wt | 25.4 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 16.4 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 23.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 15.6 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 14.3 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 15.5 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 21.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 28.7 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 36.1 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.8 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 23.9 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 35.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 27.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 55.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10835), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD12-AS1]] | +0.74 | +0.75 / +0.77 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CCSER1]] | +0.74 | +0.73 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[PLCH1]] | +0.69 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[SYNPR-AS1]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[MTUS1]] | +0.68 | +0.61 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[FAAH2]] | +0.64 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[PROM1]] | +0.64 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[ANK3]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[MUC4]] | +0.64 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[PIP5K1B]] | +0.62 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[TMC5]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[TJP3]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[SLC44A3]] | +0.61 | +0.62 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM228B]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[EPOR]] | -0.49 | -0.54 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*62 arrows, 62 of them with an alert ⚠; grade A 0, B 21, C 41. Shown: the 12 strongest; 50 more arrows (50 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HNF1B]] | B | HNF1B activity raises SAMD12's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 2.97× lower at baseline in the lines without HNF1B | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[EXPH5]] | B | EXPH5 activity raises SAMD12's level | lines that do not express EXPH5 (20) vs lines expressing it (30) | 3.46× lower at baseline in the lines without EXPH5 | 0.016 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000243004, GOLT1A |
| [[POU5F1B]] | B | POU5F1B activity raises SAMD12's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 3.59× lower at baseline in the lines without POU5F1B | 0.020 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[MECOM]] | B | MECOM activity raises SAMD12's level | lines that do not express MECOM (18) vs lines expressing it (32) | 3.46× lower at baseline in the lines without MECOM | 0.021 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |
| [[SIDT1]] | B | SIDT1 activity raises SAMD12's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 3.85× lower at baseline in the lines without SIDT1 | 0.021 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[ALOX5]] | B | ALOX5 activity raises SAMD12's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 3.08× lower at baseline in the lines without ALOX5 | 0.022 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[SPATA6L]] | B | SPATA6L activity raises SAMD12's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 3.87× lower at baseline in the lines without SPATA6L | 0.025 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[IKZF2]] | B | IKZF2 activity raises SAMD12's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 2.18× lower at baseline in the lines without IKZF2 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[PROM2]] | B | PROM2 activity raises SAMD12's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 3.42× lower at baseline in the lines without PROM2 | 0.033 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[PDZK1IP1]] | B | PDZK1IP1 activity raises SAMD12's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 3.15× lower at baseline in the lines without PDZK1IP1 | 0.041 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[COLEC10]] | B | COLEC10 activity raises SAMD12's level | lines that do not express COLEC10 (31) vs lines expressing it (19) | 1.89× lower at baseline in the lines without COLEC10 | 0.050 | ⚠ within organs, on part of the lines; also absent: CCK, TRIM55, AJAP1 |
| [[BCL2L15]] | B | BCL2L15 activity raises SAMD12's level | lines that do not express BCL2L15 (20) vs lines expressing it (30) | 3.20× lower at baseline in the lines without BCL2L15 | 0.050 | ⚠ within organs, on part of the lines; also absent: SYK, NOS3, CASC8; maybe low, not absent |

### Downstream of this gene

*59 arrows, 59 of them with an alert ⚠; grade A 0, B 20, C 39. Shown: the 12 strongest; 47 more arrows (47 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB3IP]] | B | SAMD12 activity raises RAB3IP's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 3.11× lower at baseline in the lines without SAMD12 | 0.001 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[EXPH5]] | B | SAMD12 activity raises EXPH5's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 3.83× lower at baseline in the lines without SAMD12 | 0.008 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[SLC44A3-AS1]] | B | SAMD12 activity raises SLC44A3-AS1's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 2.91× lower at baseline in the lines without SAMD12 | 0.022 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[SLC44A3]] | B | SAMD12 activity raises SLC44A3's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 2.65× lower at baseline in the lines without SAMD12 | 0.030 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[PCAT1]] | B | SAMD12 activity raises PCAT1's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 2.22× lower at baseline in the lines without SAMD12 | 0.039 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[PROM2]] | B | SAMD12 activity raises PROM2's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 2.09× lower at baseline in the lines without SAMD12 | 0.040 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[PPM1H]] | B | SAMD12 activity raises PPM1H's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 2.22× lower at baseline in the lines without SAMD12 | 0.044 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[C4orf19]] | B | SAMD12 activity raises C4orf19's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 2.13× lower at baseline in the lines without SAMD12 | 0.055 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[FRK]] | B | SAMD12 activity raises FRK's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 2.61× lower at baseline in the lines without SAMD12 | 0.060 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[MBD1]] | B | SAMD12 activity raises MBD1's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 1.25× lower at baseline in the lines without SAMD12 | 0.061 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[ARHGAP32]] | B | SAMD12 activity raises ARHGAP32's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 1.66× lower at baseline in the lines without SAMD12 | 0.062 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[ELF3-AS1]] | B | SAMD12 activity raises ELF3-AS1's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 2.33× lower at baseline in the lines without SAMD12 | 0.064 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.6, 51.3); signed map (58.4, 1.7). **Vector** length 124, 43.2% of its response variance represented; |z| ≥ 3 in 1,192 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.4 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +10.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.2 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +9.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.1 | +5.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +6.5 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | +3.0 | +3.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.4 | -15.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.4 | -2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -7.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -1.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.2 | -2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | sterile alpha motif domain containing 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.11-q24.12 — chr8:118,189,455-118,622,112 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39458 |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Matched by | ensembl_id |

UniProt [Q8N8I0](https://www.uniprot.org/uniprotkb/Q8N8I0) carries no function annotation.

**Summary**, from NCBI Gene [401474](https://www.ncbi.nlm.nih.gov/gene/401474):

> Predicted to be involved in cell surface receptor protein tyrosine kinase signaling pathway. Predicted to be active in cytoplasmic side of plasma membrane. Implicated in familial adult myoclonic epilepsy 1. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31750](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31750) · Entrez [401474](https://www.ncbi.nlm.nih.gov/gene/401474) · UniProt [Q8N8I0](https://www.uniprot.org/uniprotkb/Q8N8I0) · Ensembl [ENSG00000177570](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177570)

## Data

Gene col 10835: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10835); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10835, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10835]; `tensor/DDL_lfc|DDL_z.npy` [10835]; `embed/gene_vectors.npy` [10835]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10835 or target_col == 10835). Every well: [[SAMD12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMD12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
