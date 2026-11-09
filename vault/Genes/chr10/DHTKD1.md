---
symbol: "DHTKD1"
type: "gene"
col: 11172
ensembl_id: "ENSG00000181192"
name: "dehydrogenase E1 and transketolase domain containing 1"
location: "10p14"
module: 85
arm: "+"
pooled_cpm: 37.04
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 26
n_dd_up_clean: 7
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# DHTKD1

*dehydrogenase E1 and transketolase domain containing 1* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.40× (z +15.3, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.480× (z -18.2, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIGA2]] (+0.70, fdr 3e-05), [[CBFA2T2]] (+0.70, fdr 1e-05), [[LCMT1]] (+0.69, fdr 1e-05); moves opposite to [[CLIC2]] (-0.66, fdr 2e-05), [[ARRDC3-AS1]] (-0.66, fdr 1e-04), [[ZNF195]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11172.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.40×** | +15.3 | 0e+00 | 45/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.36×** | +15.1 | 0e+00 | 45/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.89×** | +11.2 | 8e-27 | 40/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +7.2 | 9e-11 | 32/48 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.39×** | +5.8 | 7e-07 | 28/43 (NCI-H23, MIA PaCa-2, …) | two highest doses | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +5.1 | 3e-05 | 24/48 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.33×** | +4.9 | 9e-05 | 17/35 (MIA PaCa-2, LoVo, …) | two highest doses | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +4.8 | 1e-04 | 22/47 (SNU-423, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.012 | 14/48 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.14× | +3.3 | 0.064 | 14/48 (BT-474, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.076 | 10/48 (NCI-H2347, NCI-H23, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.19× | +3.1 | 0.095 | 14/47 (A549, AsPC-1, …) | top dose only |  |
| [[Decitabine (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.11 | 8/47 (HEC-1-A, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11172.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.480×** | -18.2 | 0e+00 | 44/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.380×** | -17.0 | 0e+00 | 40/47 (A549, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.482×** | -12.8 | 4e-35 | 40/47 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.486×** | -12.7 | 1e-34 | 40/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.494×** | -12.4 | 4e-33 | 37/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.507×** | -11.9 | 9e-31 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.274×** | -11.9 | 2e-30 | 41/48 (NCI-H23, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.523×** | -10.9 | 6e-26 | 36/48 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.559×** | -10.2 | 1e-22 | 34/48 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.341×** | -9.9 | 4e-21 | 39/49 (HT-29, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.575×** | -9.7 | 1e-20 | 38/47 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.583×** | -9.4 | 2e-19 | 41/47 (SW480, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.626×** | -6.9 | 2e-10 | 31/48 (KATO III, A-172, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.686×** | -6.6 | 2e-09 | 28/48 (HT-29, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.701×** | -6.2 | 2e-08 | 31/48 (HT-29, AsPC-1, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.515×** | -6.1 | 4e-08 | 27/47 (HT-29, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.716×** | -5.8 | 2e-07 | 28/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11172. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 54.0 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -16.8) |
| [[KATO III (line)]] | alt | 43.5 | 3 | 7 | [[Panobinostat (drug)]] 5 µM 3.09× (z +10.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -14.8) |
| [[PANC-1 (line)]] | alt | 27.2 | 3 | 7 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.51× (z +14.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -16.4) |
| [[SW480 (line)]] | alt | 35.1 | 2 | 8 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.46× (z +10.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -17.3) |
| [[AsPC-1 (line)]] | alt | 36.6 | 2 | 7 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.52× (z +10.7) | [[Digitoxin (drug)]] 5 µM 0.116× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -13.3) |
| [[A-172 (line)]] | wt | 54.4 | 1 | 6 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.92× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -16.7) |
| [[MIA PaCa-2 (line)]] | alt | 54.9 | 4 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.68× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 36.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -19.7) |
| [[A498 (line)]] | wt | 44.9 | 3 | 3 | [[Panobinostat (drug)]] 5 µM 2.76× (z +10.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -17.3) |
| [[A549 (line)]] | wt | 35.5 | 2 | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.48× (z +10.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -20.0) |
| [[LS 180 (line)]] | wt | 31.3 | 2 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +8.8) | [[Digitoxin (drug)]] 0.5 µM 0.278× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 21.8 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | [[Harringtonine (drug)]] 5 µM 0.147× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 56.6 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -24.9) |
| [[HOP62 (line)]] | alt | 26.4 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.36× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 40.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -17.9) |
| [[SW 900 (line)]] | alt | 42.9 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.263× (z -9.8) |
| [[SW1417 (line)]] | alt | 49.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.311× (z -11.5) |
| [[Hs 766T (line)]] | wt | 36.8 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.247× (z -14.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.328× (z -11.7) |
| [[LoVo (line)]] | wt | 35.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 27.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -13.8) |
| [[Panc 03.27 (line)]] | alt | 35.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.466× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 33.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.91× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 19.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -13.1) |
| [[HCT15 (line)]] | alt | 35.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 47.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.341× (z -11.0) |
| [[HS-578T (line)]] | alt | 29.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -15.5) |
| [[hTERT-HPNE (line)]] | wt | 24.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 59.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 42.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -14.7) |
| [[SNU-1 (line)]] | wt | 17.9 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0405× (z -13.5) |
| [[A-427 (line)]] | wt | 34.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -10.9) |
| [[BT-474 (line)]] | alt | 70.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[H4 (line)]] | wt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -12.8) |
| [[J82 (line)]] | alt | 58.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.30× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 29.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.321× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 35.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -9.7) |
| [[SNU-423 (line)]] | alt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.3) |
| [[AN3 CA (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11172), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIGA2]] | +0.70 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[CBFA2T2]] | +0.70 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[LCMT1]] | +0.69 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.69 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[CEP131]] | +0.68 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[KIAA1328]] | +0.67 | +0.51 / +0.37 | both halves | 8e-05 |  |
| [[RPA3]] | +0.67 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[ARL3]] | +0.67 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[SPSB3]] | +0.66 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[GPN3]] | +0.66 | +0.32 / +0.55 | both halves | 1e-04 |  |
| [[ANAPC11]] | +0.65 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[MPST]] | +0.65 | +0.49 / +0.51 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives |

## Genes that move opposite

*51 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLIC2]] | -0.66 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[ARRDC3-AS1]] | -0.66 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[ZNF195]] | -0.65 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[BAG2]] | -0.65 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[KICS2]] | -0.65 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[POLR2M]] | -0.65 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[CCDC90B-AS1]] | -0.64 | -0.49 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[MMADHC-DT]] | -0.64 | -0.49 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[PCNX4-DT]] | -0.64 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[AP5M1]] | -0.64 | -0.52 / -0.22 | both halves | 6e-04 |  |
| [[GPRASP1]] | -0.63 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[LINC01340]] | -0.63 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[NEB]] | -0.63 | -0.53 / -0.23 | both halves | 5e-04 |  |
| [[NCR3LG1]] | -0.62 | -0.48 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers DHTKD1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.686). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (4.5, -14.5); signed map (-34.2, 15.4). **Vector** length 94.7, 26.2% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.8 | +11.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.4 | +15.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.1 | +15.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.8 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +5.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.9 | +1.2 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.8 | +0.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.8 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.3 | -9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.8 | -17.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.7 | -18.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.7 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.7 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | dehydrogenase E1 and transketolase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p14 — chr10:12,068,954-12,123,221 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1630, MGC3090, DKFZP762M115, CMT2Q, OADC-E1, OADH-E1, E1a |
| Gene groups (HGNC) | Oxoglutarate dehydrogenase family; Oxoadipate dehydrogenase complex subunits |
| Reactome | 3 pathways, smallest: OADH complex synthesizes glutaryl-CoA from 2-OA; Lysine catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HY7](https://www.uniprot.org/uniprotkb/Q96HY7) (2-oxoadipate dehydrogenase complex component E1):

> 2-oxoadipate dehydrogenase (E1a) component of the 2-oxoadipate dehydrogenase complex (OADHC). Participates in the first step, rate limiting for the overall conversion of 2-oxoadipate (alpha-ketoadipate) to glutaryl-CoA and CO(2) catalyzed by the whole OADHC. Catalyzes the irreversible decarboxylation of 2-oxoadipate via the thiamine diphosphate (ThDP) cofactor and subsequent transfer of the decarboxylated acyl intermediate on an oxidized dihydrolipoyl group that is covalently amidated to the E2 …

**Summary**, from NCBI Gene [55526](https://www.ncbi.nlm.nih.gov/gene/55526):

> This gene encodes a component of a mitochondrial 2-oxoglutarate-dehydrogenase-complex-like protein involved in the degradation pathways of several amino acids, including lysine. Mutations in this gene are associated with 2-aminoadipic 2-oxoadipic aciduria and Charcot-Marie-Tooth Disease Type 2Q. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:23537](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23537) · Entrez [55526](https://www.ncbi.nlm.nih.gov/gene/55526) · UniProt [Q96HY7](https://www.uniprot.org/uniprotkb/Q96HY7) · Ensembl [ENSG00000181192](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181192)

## Data

Gene col 11172: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11172); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11172, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11172]; `tensor/DDL_lfc|DDL_z.npy` [11172]; `embed/gene_vectors.npy` [11172]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11172 or target_col == 11172). Every well: [[DHTKD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHTKD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
