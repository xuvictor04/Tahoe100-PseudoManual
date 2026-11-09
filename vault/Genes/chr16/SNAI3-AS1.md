---
symbol: "SNAI3-AS1"
type: "gene"
col: 15295
ensembl_id: "ENSG00000260630"
name: "SNAI3 antisense RNA 1"
location: "16q24.2"
module: 86
arm: "+"
pooled_cpm: 5.84
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 20
n_dd_up_clean: 18
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# SNAI3-AS1

*SNAI3 antisense RNA 1* — 16q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 2.08× (z +10.5, q 7e-23, up in 32 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.215× (z -15.6, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDI1]] (+0.69, fdr 7e-06), [[HMGCR]] (+0.69, fdr 7e-06), [[MSMO1]] (+0.69, fdr 7e-06); moves opposite to [[MAP3K1]] (-0.48, fdr 2e-04), [[CNTRL]] (-0.38, fdr 4e-04), [[RMI1]] (-0.37, fdr 4e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PCSK9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15295.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **2.08×** | +10.5 | 7e-23 | 32/45 (NCI-H23, A549, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | **1.56×** | +6.4 | 5e-08 | 25/46 (HEC-1-A, C-33 A, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.85×** | +6.2 | 7e-08 | 20/42 (A498, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +6.2 | 7e-08 | 4/10 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +5.9 | 4e-07 | 8/25 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.68×** | +5.2 | 2e-05 | 18/45 (PANC-1, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.65×** | +5.1 | 3e-05 | 19/46 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +4.9 | 7e-05 | 17/45 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.51×** | +4.2 | 0.002 | 15/43 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.005 | 15/42 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.005 | 8/41 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.015 | 10/44 (A-427, A498, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.015 | 4/45 (HOP62, SNU-1, …) | all doses, flat |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.015 | 12/42 (A498, A549, …) | top dose only |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.020 | 15/45 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift |
| [[crizotinib (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.026 | 11/44 (A549, HEC-1-A, …) | top dose only | position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.033 | 9/44 (C-33 A, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15295.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.215×** | -15.6 | 0e+00 | 41/46 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.279×** | -12.9 | 1e-35 | 36/43 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.350×** | -10.2 | 3e-22 | 32/43 (hTERT-HPNE, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.393×** | -9.5 | 4e-19 | 30/40 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.412×** | -9.0 | 3e-17 | 31/42 (C-33 A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.440×** | -8.3 | 9e-15 | 28/45 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.517×** | -6.7 | 2e-09 | 24/37 (HOP62, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.527×** | -6.2 | 3e-08 | 19/29 (A498, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.665×** | -5.8 | 3e-07 | 21/39 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.584×** | -5.4 | 3e-06 | 23/46 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.612×** | -5.0 | 3e-05 | 18/45 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.623×** | -4.3 | 9e-04 | 17/46 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.623×** | -4.3 | 9e-04 | 16/45 (hTERT-HPNE, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.465×** | -4.1 | 0.002 | 13/38 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.674×** | -4.0 | 0.002 | 14/42 (BT-474, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.680×** | -3.9 | 0.003 | 7/46 (BT-474, SW 1271, …) | rises with dose |  |
| [[Silodosin (drug)]] 5 µM |  | **0.690×** | -3.6 | 0.010 | 14/39 (A549, A-172, …) | top dose only |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.712×** | -3.4 | 0.019 | 12/43 (SW480, HS-578T, …) | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.722×** | -3.3 | 0.028 | 13/46 (KATO III, AN3 CA, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15295. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.86 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -16.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0664× (z -15.3) |
| [[HOP62 (line)]] | alt | 11.3 | 3 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 12.6× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -11.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 6.09 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -10.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Silodosin (drug)]] 5 µM 0.0809× (z -9.6) |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -10.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0901× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 7.00 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -12.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0908× (z -11.0) |
| [[A-427 (line)]] | wt | 10.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.161× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 8.06 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0180× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 13.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -14.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 4.55 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0956× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 7.59 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0329× (z -14.3) |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0546× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 6.00 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0895× (z -9.3) |
| [[Hs 766T (line)]] | wt | 8.37 | 0 | 1 (1 ⚠) | — | [[OTS514 (drug)]] 0.05 µM 0.105× (z -9.0) ⚠ transcription drop |
| [[HS-578T (line)]] | alt | 6.82 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0901× (z -9.0) |
| [[KATO III (line)]] | alt | 5.73 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0721× (z -9.4) |
| [[LoVo (line)]] | wt | 5.20 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 7.74 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0960× (z -9.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 7.33 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0707× (z -10.1) |
| [[SNU-1 (line)]] | wt | 8.76 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0345× (z -10.5) |
| [[SW480 (line)]] | alt | 2.71 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0397× (z -12.5) |
| [[A-172 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15295), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDI1]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[HMGCR]] | +0.69 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[MSMO1]] | +0.69 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[HMGCS1]] | +0.68 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[CYP51A1]] | +0.65 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[DHCR7]] | +0.65 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[FDPS]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MVD]] | +0.64 | +0.58 / +0.68 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[SCD]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[SQLE]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ACAT2]] | +0.61 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[HSD17B7]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ACSS2]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K1]] | -0.48 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[CNTRL]] | -0.38 | -0.25 / -0.39 | both halves | 4e-04 |  |
| [[RMI1]] | -0.37 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[GYG1]] | -0.36 | -0.21 / -0.33 | both halves | 7e-04 |  |
| [[CEP295]] | -0.36 | -0.27 / -0.41 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCSK9]] | B | PCSK9 activity lowers SNAI3-AS1's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 1.37× higher at baseline in the lines without PCSK9 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SNAI3-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.716). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.4, -49.3); signed map (-52.8, 32.1). **Vector** length 68.3, 11.7% of its response variance represented; |z| ≥ 3 in 1,156 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *cholesterol synthesis* (control, mean cos +0.59 to 22); *Cholesterol biosynthesis* (reactome, mean cos +0.58 to 20); *cholesterol homeostasis* (hallmark, mean cos +0.58 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +4.4 | +10.5 |
|  | [[Berbamine (drug)]] 5 µM |  | +3.2 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +6.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.0 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +4.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.4 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +1.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -8.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.4 | -10.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -15.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -12.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -9.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.7 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | -1.3 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | SNAI3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16q24.2 — chr16:88,663,298-88,687,282 (+) |
| Ensembl biotype | lncRNA |
| Also known as | MGC23284 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28327](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28327) · Entrez [197187](https://www.ncbi.nlm.nih.gov/gene/197187) · Ensembl [ENSG00000260630](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260630)

## Data

Gene col 15295: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15295); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15295, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15295]; `tensor/DDL_lfc|DDL_z.npy` [15295]; `embed/gene_vectors.npy` [15295]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15295 or target_col == 15295). Every well: [[SNAI3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNAI3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
