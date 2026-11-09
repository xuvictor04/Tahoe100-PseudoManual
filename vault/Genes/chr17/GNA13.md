---
symbol: "GNA13"
type: "gene"
col: 4154
ensembl_id: "ENSG00000120063"
name: "G protein subunit alpha 13"
location: "17q24.1"
module: 65
arm: "+"
pooled_cpm: 108.99
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# GNA13

*G protein subunit alpha 13* — 17q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.00× (z +12.4, q 1e-32, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.387× (z -13.5, q 7e-39, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.707× (z -5.1, q 2e-05, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO7]] (+0.55, fdr 1e-05), [[HMGN4]] (+0.53, fdr 1e-05), [[VPS26A]] (+0.52, fdr 1e-05); moves opposite to [[GLYR1]] (-0.56, fdr 1e-05), [[CDK11A]] (-0.49, fdr 4e-05), [[PILRB]] (-0.45, fdr 2e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4154.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.00×** | +12.4 | 1e-32 | 48/49 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +8.7 | 8e-16 | 41/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.64×** | +7.5 | 1e-11 | 40/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +5.7 | 2e-06 | 34/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +5.1 | 4e-05 | 31/48 (NCI-H460, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.003 | 27/48 (A498, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.21×** | +3.9 | 0.008 | 23/48 (AN3 CA, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.5 | 0.028 | 23/48 (NCI-H460, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.029 | 24/48 (COLO 205, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.043 | 22/48 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.069 | 19/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.2 | 0.069 | 20/48 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.084 | 22/48 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.084 | 22/48 (LoVo, SW480, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.084 | 14/48 (SW 900, HT-29, …) | top dose only |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.085 | 21/48 (SNU-423, SW1417, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4154.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.387×** | -13.5 | 7e-39 | 40/44 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.440×** | -12.1 | 2e-31 | 45/49 (NCI-H2347, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.581×** | -8.0 | 2e-13 | 38/48 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.619×** | -7.1 | 2e-10 | 37/48 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.731×** | -6.6 | 5e-09 | 28/49 (CHP-212, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.643×** | -6.0 | 1e-07 | 30/45 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.707×** | -5.1 | 2e-05 | 36/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.729×** | -4.7 | 2e-04 | 34/48 (A-172, PANC-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.818×** | -4.2 | 0.001 | 33/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.784×** | -3.5 | 0.028 | 25/50 (BT-474, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.786×** | -3.4 | 0.030 | 24/48 (A-172, SNU-423, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.807×** | -3.2 | 0.066 | 20/49 (H4, PANC-1, …) | top dose only |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.864× | -3.1 | 0.083 | 12/49 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.813×** | -3.1 | 0.083 | 18/48 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.866× | -3.0 | 0.087 | 14/48 (SHP-77, BT-474, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4154. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 112 | 8 (4 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.28× (z +12.9) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.97× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -11.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 143 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.00× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.358× (z -10.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H2030 (line)]] | alt | 96.3 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.5× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.256× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 122 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -19.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 179 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.330× (z -9.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 199 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.92× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -13.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 90.3 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 14.9× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CHP-212 (line)]] | wt | 253 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[palbociclib (drug)]] 5 µM 0.0709× (z -9.8) |
| [[COLO 205 (line)]] | alt | 74.1 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 13.5× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 105 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.09× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H2347 (line)]] | alt | 172 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[PANC-1 (line)]] | alt | 76.0 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.70× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.397× (z -9.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SW480 (line)]] | alt | 95.9 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.57× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -10.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 97.9 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.48× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -9.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 127 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -11.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 167 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HEC-1-A (line)]] | alt | 95.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.32× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.432× (z -8.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HOP62 (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 137 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.62× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -13.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 102 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.71× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 85.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.1× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -14.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 165 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -11.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 90.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -9.3) |
| [[Hs 766T (line)]] | wt | 87.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.91× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 59.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -10.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -9.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 65.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.83× (z +11.1) ⚠ toxic | — |
| [[NCI-H1573 (line)]] | alt | 62.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 14.1× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 83.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.91× (z +11.6) | — |
| [[Panc 03.27 (line)]] | alt | 121 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.25× (z +9.2) | — |
| [[RKO (line)]] | wt | 75.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.46× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 85.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -12.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 71.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW 1088 (line)]] | alt | 95.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0731× (z -9.6) |
| [[SW 900 (line)]] | alt | 112 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.36× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 107 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 99.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 107 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 61.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4154), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO7]] | +0.55 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[HMGN4]] | +0.53 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[VPS26A]] | +0.52 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[DUBR]] | +0.52 | +0.44 / +0.34 | both halves | 1e-04 |  |
| [[ABRAXAS1]] | +0.51 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[MRS2]] | +0.50 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[TRAF6]] | +0.49 | +0.50 / +0.56 | both halves | 1e-05 | pathway: Cell death signalling via NRAGE, NRIF and NADE |
| [[SMIM13]] | +0.48 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[LTA4H]] | +0.48 | +0.63 / +0.35 | both halves | 1e-04 |  |
| [[MBD2]] | +0.48 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[CAPZA2]] | +0.48 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[SPIN1]] | +0.47 | +0.57 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLYR1]] | -0.56 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[CDK11A]] | -0.49 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[PILRB]] | -0.45 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[CDK11B]] | -0.45 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[DDX46]] | -0.44 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[SRSF9]] ⚠ | -0.44 | -0.46 / -0.38 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RBM25]] | -0.44 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[DDX19A]] | -0.43 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[GON4L]] | -0.43 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[CAAP1]] | -0.43 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[SLC30A7]] | -0.42 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[TUT7]] | -0.42 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[LIN52]] | -0.42 | -0.40 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GNA13's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.396). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-7.9, -9.9); signed map (-34.1, -19.9). **Vector** length 91.4, 31.1% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.0 | +4.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.9 | -0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | -1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | -2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | -0.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.9 | +0.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.7 | +5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.7 | +3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.3 | +5.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | +3.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | +1.4 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.7 | +0.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Darinaparsin (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit alpha 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.1 — chr17:65,009,289-65,056,740 (-) |
| Ensembl biotype | protein_coding |
| Also known as | G13, MGC46138 |
| Gene groups (HGNC) | G protein subunits alpha, group 12/13 |
| Reactome | 17 pathways, smallest: Thromboxane signalling through TP receptor; Signal amplification; Thrombin signalling through proteinase activated receptors (PARs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14344](https://www.uniprot.org/uniprotkb/Q14344) (Guanine nucleotide-binding protein subunit alpha-13):

> Guanine nucleotide-binding proteins (G proteins) are involved as modulators or transducers in various transmembrane signaling systems. Activates effector molecule RhoA by binding and activating RhoGEFs (ARHGEF1/p115RhoGEF, ARHGEF11/PDZ-RhoGEF and ARHGEF12/LARG). GNA13-dependent Rho signaling subsequently regulates transcription factor AP-1 (activating protein-1) (By similarity). Promotes tumor cell invasion and metastasis by activating RhoA/ROCK signaling pathway. Inhibits CDH1-mediated cell …

**Summary**, from NCBI Gene [10672](https://www.ncbi.nlm.nih.gov/gene/10672):

> Enables G protein activity. Involved in Rho-activating G protein-coupled receptor signaling pathway. Located in cytosol and nucleus. Is active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4381](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4381) · Entrez [10672](https://www.ncbi.nlm.nih.gov/gene/10672) · UniProt [Q14344](https://www.uniprot.org/uniprotkb/Q14344) · Ensembl [ENSG00000120063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120063)

## Data

Gene col 4154: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4154); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4154, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4154]; `tensor/DDL_lfc|DDL_z.npy` [4154]; `embed/gene_vectors.npy` [4154]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4154 or target_col == 4154). Every well: [[GNA13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNA13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
