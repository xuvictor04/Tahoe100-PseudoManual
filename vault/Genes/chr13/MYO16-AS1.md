---
symbol: "MYO16-AS1"
type: "gene"
col: 14070
ensembl_id: "ENSG00000236242"
name: "MYO16 antisense RNA 1"
location: "13q33.3"
module: 73
arm: "+"
pooled_cpm: 24.19
n_lines_expressing: 27
n_dd_up: 15
n_dd_down: 28
n_dd_up_clean: 11
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 14
direction_downstream: 7
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# MYO16-AS1

*MYO16 antisense RNA 1* — 13q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.93× (z +6.2, q 3e-07, up in 5 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.63× (z +4.6, q 9e-04, up in 19 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.271× (z -12.8, q 2e-34, down in 24 of 25 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.546× (z -5.9, q 3e-07, down in 16 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPINK13]] (+0.61, fdr 2e-05), [[MARCOL]] (+0.55, fdr 1e-04), [[HTR1D]] (+0.55, fdr 8e-05); moves opposite to [[PGF]] (-0.54, fdr 3e-05), [[EDNRA]] (-0.51, fdr 2e-04), [[ZCCHC24]] (-0.50, fdr 5e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 7 go from it, the strongest it → [[SH3D19]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14070.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +6.2 | 3e-07 | 5/18 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +4.8 | 4e-04 | 1/23 (Panc 03.27) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.63×** | +4.6 | 9e-04 | 19/25 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.006 | 16/25 (A-172, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.007 | 8/25 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.007 | 19/25 (NCI-H1573, LS 180, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.012 | 14/25 (LS 180, LoVo, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.021 | 18/25 (A-172, NCI-H460, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.44×** | +3.6 | 0.021 | 16/25 (A-172, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.47×** | +3.4 | 0.033 | 11/25 (Panc 03.27, NCI-H2030, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.036 | 15/25 (A-172, HS-578T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.052 | 16/25 (A-172, NCI-H460, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.41×** | +3.2 | 0.053 | 11/25 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.061 | 13/25 (NCI-H2030, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.81×** | +3.0 | 0.089 | 14/25 (SW48, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14070.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.271×** | -12.8 | 2e-34 | 24/25 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.279×** | -12.5 | 2e-33 | 24/25 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.285×** | -12.3 | 2e-32 | 23/25 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.472×** | -7.4 | 3e-11 | 22/25 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.546×** | -5.9 | 3e-07 | 16/24 (LS 180, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.561×** | -5.7 | 1e-06 | 18/25 (LoVo, LS 180, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.574×** | -5.4 | 5e-06 | 19/25 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.694×** | -5.1 | 3e-05 | 18/24 (LoVo, LS 180, …) | two highest doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.602×** | -5.0 | 4e-05 | 20/25 (LS 180, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.632×** | -4.5 | 4e-04 | 17/25 (LS 180, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.612×** | -4.4 | 6e-04 | 15/25 (LoVo, SW48, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.671×** | -3.9 | 0.004 | 19/25 (MIA PaCa-2, SW48, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.668×** | -3.8 | 0.006 | 20/25 (J82, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.507×** | -3.5 | 0.021 | 13/25 (LoVo, SW48, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.513×** | -3.4 | 0.024 | 14/25 (NCI-H460, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.789×** | -3.3 | 0.034 | 13/25 (LS 180, J82, …) | two highest doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.719×** | -3.1 | 0.056 | 17/25 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.722×** | -3.1 | 0.061 | 8/25 (LS 180, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.728×** | -2.9 | 0.084 | 17/25 (COLO 205, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Asciminib (drug)]] 0.05 µM |  | **0.725×** | -2.9 | 0.093 | 5/25 (A549, CFPAC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.734×** | -2.9 | 0.093 | 6/25 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.814×** | -2.9 | 0.093 | 8/25 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.748×** | -2.8 | 0.093 | 9/25 (Hs 766T, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.89 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14070. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 133 | 0 | 19 (13 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0134× (z -35.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0841× (z -28.7) |
| [[SW48 (line)]] | wt | 254 | 0 | 18 (13 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0325× (z -19.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.115× (z -17.5) |
| [[LS 180 (line)]] | wt | 62.4 | 0 | 16 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0111× (z -27.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0558× (z -24.9) |
| [[NCI-H460 (line)]] | wt | 71.8 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0872× (z -19.0) |
| [[COLO 205 (line)]] | alt | 63.0 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0640× (z -22.7) |
| [[MIA PaCa-2 (line)]] | alt | 45.8 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0713× (z -22.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0536× (z -16.9) |
| [[AsPC-1 (line)]] | alt | 33.5 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0428× (z -17.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.164× (z -14.1) |
| [[CFPAC-1 (line)]] | alt | 26.4 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -13.2) |
| [[KATO III (line)]] | alt | 16.3 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0615× (z -14.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0916× (z -12.0) |
| [[A-172 (line)]] | wt | 26.8 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 9.80× (z +16.7) | [[Hydroxyurea (drug)]] 0.05 µM 0.149× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 27.4 | 0 | 5 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0472× (z -16.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.239× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 22.6 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0992× (z -13.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -12.9) |
| [[C-33 A (line)]] | alt | 29.8 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0579× (z -12.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[Hs 766T (line)]] | wt | 56.0 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0861× (z -12.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.211× (z -10.9) |
| [[J82 (line)]] | alt | 40.7 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -12.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.270× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 34.4 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[A549 (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.116× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 7.48 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[SW480 (line)]] | alt | 8.22 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.88× (z +8.5) | — |
| [[A-427 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.24 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.65 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14070), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPINK13]] | +0.61 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[MARCOL]] | +0.55 | +0.50 / +0.36 | both halves | 1e-04 |  |
| [[HTR1D]] | +0.55 | +0.54 / +0.37 | both halves | 8e-05 |  |
| [[LINC02582]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ROS1]] | +0.55 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[LINC00457]] | +0.54 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[ANXA3]] | +0.54 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[SLCO1B3-SLCO1B7]] | +0.54 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[PITPNM3]] | +0.53 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[KLF3]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[PAX8-AS1]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 | same gene group |
| [[C4BPB]] | +0.52 | +0.50 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGF]] | -0.54 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[EDNRA]] | -0.51 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[ZCCHC24]] | -0.50 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[TMEM132A]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[TSHZ3]] | -0.49 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[LTBP3]] | -0.49 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[AZIN2]] | -0.49 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[PPIL3]] | -0.47 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ITPR1]] | -0.46 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[EPOR]] | -0.45 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[LINC03047]] | -0.44 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[WWTR1]] | -0.44 | -0.37 / -0.41 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 1, C 13. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers MYO16-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[MISP]] | C | MISP activity raises MYO16-AS1's level | lines that do not express MISP (23) vs lines expressing it (27) | 3.38× lower at baseline in the lines without MISP | 0.004 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B; co-absent with the target |
| [[ANXA3]] | C | ANXA3 activity raises MYO16-AS1's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 3.17× lower at baseline in the lines without ANXA3 | 0.017 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132; co-absent with the target |
| [[SPON1]] | C | SPON1 activity raises MYO16-AS1's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 4.31× lower at baseline in the lines without SPON1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A; co-absent with the target |
| [[DSG4]] | C | DSG4 activity raises MYO16-AS1's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 7.64× lower at baseline in the lines without DSG4 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031; co-absent with the target |
| [[KRT6A]] | C | KRT6A activity raises MYO16-AS1's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 5.24× lower at baseline in the lines without KRT6A | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[CATSPERB]] | C | CATSPERB activity raises MYO16-AS1's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 3.03× lower at baseline in the lines without CATSPERB | 0.032 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14; co-absent with the target |
| [[MIR4713HG]] | C | MIR4713HG activity raises MYO16-AS1's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 3.42× lower at baseline in the lines without MIR4713HG | 0.032 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA; co-absent with the target |
| [[MARCOL]], [[SPINK13]] | C | MARCOL, SPINK13 activity raises MYO16-AS1's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 4.81× lower at baseline in the lines without MARCOL, SPINK13 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[LINC02582]] | C | LINC02582 activity raises MYO16-AS1's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 4.19× lower at baseline in the lines without LINC02582 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[C4BPB]] | C | C4BPB activity raises MYO16-AS1's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 3.77× lower at baseline in the lines without C4BPB | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4; co-absent with the target |
| [[COBL]] | C | COBL activity raises MYO16-AS1's level | lines that do not express COBL (23) vs lines expressing it (27) | 2.84× lower at baseline in the lines without COBL | 0.074 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH3D19]] | B | MYO16-AS1 activity raises SH3D19's level | lines that do not express MYO16-AS1 (23) vs lines expressing it (27) | 1.79× lower at baseline in the lines without MYO16-AS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000275216, KRT18, LAMC2 |
| [[ITPR1]] | B | MYO16-AS1 activity lowers ITPR1's level | lines that do not express MYO16-AS1 (23) vs lines expressing it (27) | 2.92× higher at baseline in the lines without MYO16-AS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000275216, KRT18, LAMC2 |
| [[SLCO1B3-SLCO1B7]] | B | MYO16-AS1 activity raises SLCO1B3-SLCO1B7's level | lines that do not express MYO16-AS1 (23) vs lines expressing it (27) | 3.04× lower at baseline in the lines without MYO16-AS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000275216, KRT18, LAMC2 |
| [[HR]] | B | MYO16-AS1 activity raises HR's level | lines that do not express MYO16-AS1 (23) vs lines expressing it (27) | 1.52× lower at baseline in the lines without MYO16-AS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000275216, KRT18, LAMC2 |
| [[LINC01836]] | B | MYO16-AS1 activity raises LINC01836's level | lines that do not express MYO16-AS1 (23) vs lines expressing it (27) | 1.70× lower at baseline in the lines without MYO16-AS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000275216, KRT18, LAMC2 |
| [[MISP]] | C | MYO16-AS1 activity raises MISP's level | lines that do not express MYO16-AS1 (23) vs lines expressing it (27) | 3.54× lower at baseline in the lines without MYO16-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000275216, KRT18, LAMC2; co-absent with the target |
| [[SLCO1B3]] | C | MYO16-AS1 activity raises SLCO1B3's level | lines that do not express MYO16-AS1 (23) vs lines expressing it (27) | 4.03× lower at baseline in the lines without MYO16-AS1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000275216, KRT18, LAMC2; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.4, 47.9); signed map (67.8, 6.7). **Vector** length 88.6, 26.9% of its response variance represented; |z| ≥ 3 in 816 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.2 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | +0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | -5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.3 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +2.9 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.1 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -1.7 | -3.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -1.6 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.7 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.5 | -2.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -2.5 |
|  | [[Ranolazine (drug)]] 0.5 µM |  | -1.5 | -2.2 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | MYO16 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q33.3 — chr13:109,163,902-109,201,483 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:39913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:39913) · Entrez [100885782](https://www.ncbi.nlm.nih.gov/gene/100885782) · Ensembl [ENSG00000236242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236242)

## Data

Gene col 14070: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14070); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14070, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14070]; `tensor/DDL_lfc|DDL_z.npy` [14070]; `embed/gene_vectors.npy` [14070]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14070 or target_col == 14070). Every well: [[MYO16-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO16-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
