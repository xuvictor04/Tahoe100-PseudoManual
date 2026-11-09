---
symbol: "KLHL12"
type: "gene"
col: 3881
ensembl_id: "ENSG00000117153"
name: "kelch like family member 12"
location: "1q32.1"
module: 170
arm: "+"
pooled_cpm: 32.46
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 25
n_dd_up_clean: 7
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# KLHL12

*kelch like family member 12* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.40× (z +8.6, q 5e-15, up in 30 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.45× (z +6.7, q 5e-09, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.495× (z -12.8, q 1e-34, down in 40 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.522× (z -11.8, q 1e-29, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC22]] (+0.74, fdr 7e-06), [[ZNF333]] (+0.67, fdr 1e-05), [[TATDN3]] (+0.65, fdr 7e-06); moves opposite to [[PPP3CA]] (-0.56, fdr 2e-05), [[CHD4]] (-0.55, fdr 3e-05), [[HNRNPA2B1]] (-0.51, fdr 2e-04).
> It sits in the **+** arm of [[Module 170]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DCP1B]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3881.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.40×** | +8.6 | 5e-15 | 30/48 (A498, RKO, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +6.7 | 5e-09 | 30/48 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +6.5 | 2e-08 | 36/48 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +6.4 | 3e-08 | 26/45 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.36×** | +5.6 | 2e-06 | 28/48 (A498, A-172, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +5.4 | 7e-06 | 24/46 (NCI-H460, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.28×** | +4.5 | 6e-04 | 22/47 (CFPAC-1, A498, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.4 | 7e-04 | 20/47 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.4 | 7e-04 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.1 | 0.003 | 15/38 (NCI-H1573, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.17× | +4.0 | 0.004 | 14/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.007 | 15/47 (Hs 766T, SW 1271, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.20× | +3.3 | 0.044 | 13/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.052 | 10/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.071 | 15/47 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.20×** | +3.1 | 0.071 | 4/46 (COLO 205, SW 900, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.071 | 9/45 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3881.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.495×** | -12.8 | 1e-34 | 40/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.522×** | -11.8 | 1e-29 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.586×** | -9.7 | 5e-20 | 40/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.574×** | -9.7 | 5e-20 | 38/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.609×** | -9.0 | 2e-17 | 34/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.752×** | -7.3 | 3e-11 | 28/47 (H4, NCI-H1792, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.656×** | -7.1 | 1e-10 | 26/42 (SW 900, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.533×** | -6.0 | 2e-07 | 31/47 (MIA PaCa-2, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.728×** | -5.7 | 6e-07 | 24/48 (NCI-H460, SW1417, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.758×** | -5.0 | 3e-05 | 23/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.750×** | -5.0 | 3e-05 | 21/48 (HEC-1-A, NCI-H1792, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.591×** | -5.0 | 3e-05 | 22/48 (AsPC-1, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.761×** | -5.0 | 3e-05 | 23/47 (J82, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.764×** | -4.9 | 4e-05 | 23/44 (NCI-H23, SW48, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.761×** | -4.7 | 1e-04 | 23/48 (CFPAC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.781×** | -4.5 | 3e-04 | 20/48 (NCI-H460, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.819×** | -3.6 | 0.009 | 19/47 (NCI-H2030, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Gefitinib (drug)]] 5 µM |  | **0.822×** | -3.6 | 0.010 | 15/48 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.697×** | -3.4 | 0.016 | 11/46 (HT-29, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.830×** | -3.2 | 0.034 | 15/47 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.853× | -2.9 | 0.089 | 4/48 (AN3 CA, NCI-H2347, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.803×** | -2.8 | 0.098 | 13/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3881. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 42.5 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.324× (z -12.4) |
| [[SW480 (line)]] | alt | 30.3 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -25.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.227× (z -17.5) |
| [[A498 (line)]] | wt | 32.0 | 2 (1 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +10.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 27.6 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.319× (z -9.6) |
| [[PANC-1 (line)]] | alt | 49.8 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.367× (z -13.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.403× (z -12.6) |
| [[A-172 (line)]] | wt | 39.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -11.2) ⚠ cell-cycle shift, explains ~78% of this change |
| [[A-427 (line)]] | wt | 44.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -14.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 34.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[C32 (line)]] | wt | 58.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -11.6) ⚠ cell-cycle shift, explains ~78% of this change |
| [[COLO 205 (line)]] | alt | 37.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[H4 (line)]] | wt | 31.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -14.5) ⚠ cell-cycle shift, explains ~78% of this change |
| [[HEC-1-A (line)]] | alt | 35.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -8.8) ⚠ cell-cycle shift, explains ~78% of this change |
| [[J82 (line)]] | alt | 27.4 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.338× (z -9.5) |
| [[LS 180 (line)]] | wt | 29.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -8.7) |
| [[SW1417 (line)]] | alt | 30.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.251× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.280× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 23.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -8.5) |
| [[CHP-212 (line)]] | wt | 33.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0559× (z -11.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 40.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.177× (z -8.7) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -12.8) ⚠ cell-cycle shift, explains ~78% of this change |
| [[NCI-H23 (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2347 (line)]] | alt | 32.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.389× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0832× (z -9.9) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -9.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0699× (z -17.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0957× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[AN3 CA (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3881), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC22]] | +0.74 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[ZNF333]] | +0.67 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[TATDN3]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[PARL]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ADPRM]] | +0.64 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[ACTR10]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[METTL22]] | +0.62 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[KCTD18]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[NDUFV3]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[CIAO3]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ZNF7]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[C6orf89]] | +0.59 | +0.63 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP3CA]] | -0.56 | -0.55 / -0.47 | both halves | 2e-05 | pathway: Signaling by WNT |
| [[CHD4]] | -0.55 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[HNRNPA2B1]] | -0.51 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[NID1]] | -0.50 | -0.36 / -0.55 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCP1B]] | C | DCP1B activity raises KLHL12's level | lines that do not express DCP1B (3) vs lines expressing it (47) | 1.33× lower at baseline in the lines without DCP1B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPRASP3, DISC1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.672). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-26.4, 21.3); signed map (-14.3, -14.7). **Vector** length 91.5, 21.2% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.9 | +6.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +6.1 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.0 | +4.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.8 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +5.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.7 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.7 | +3.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.7 | -9.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.5 | -9.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -4.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:202,891,116-202,928,636 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C3IP1 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Reactome | 3 pathways, smallest: Degradation of DVL; TCF dependent signaling in response to WNT; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53G59](https://www.uniprot.org/uniprotkb/Q53G59) (Kelch-like protein 12):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin ligase complex that acts as a negative regulator of Wnt signaling pathway and ER-Golgi transport. The BCR(KLHL12) complex is involved in ER-Golgi transport by regulating the size of COPII coats, thereby playing a key role in collagen export, which is required for embryonic stem (ES) cells division: BCR(KLHL12) acts by mediating monoubiquitination of SEC31 (SEC31A or SEC31B). The BCR(KLHL12) complex is also involved in neural crest …

**Summary**, from NCBI Gene [59349](https://www.ncbi.nlm.nih.gov/gene/59349):

> This gene encodes a member of the KLHL (Kelch-like) family of proteins. This protein has been identified as an autoantigen in the autoimmune disease Sjogren's syndrome and as a potential biomarker in primary biliary cirrhosis. This protein may act as a substrate adaptor of the Cullin-3 ubiquitin ligase complex to promote substrate-specific ubiquitylation. Ubiquitylation by this complex has been shown to regulate the Wnt signaling pathway as well as COPII vesicle coat size. A pseudogene has been …

**Accessions** — [HGNC:19360](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19360) · Entrez [59349](https://www.ncbi.nlm.nih.gov/gene/59349) · UniProt [Q53G59](https://www.uniprot.org/uniprotkb/Q53G59) · Ensembl [ENSG00000117153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117153)

## Data

Gene col 3881: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3881); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3881, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3881]; `tensor/DDL_lfc|DDL_z.npy` [3881]; `embed/gene_vectors.npy` [3881]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3881 or target_col == 3881). Every well: [[KLHL12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
