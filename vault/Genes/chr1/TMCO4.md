---
symbol: "TMCO4"
type: "gene"
col: 8531
ensembl_id: "ENSG00000162542"
name: "transmembrane and coiled-coil domains 4"
location: "1p36.13"
module: 137
arm: "+"
pooled_cpm: 21.6
n_lines_expressing: 48
n_dd_up: 11
n_dd_down: 37
n_dd_up_clean: 9
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# TMCO4

*transmembrane and coiled-coil domains 4* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.43× (z +5.1, q 2e-04, up in 26 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.289× (z -25.7, q 0e+00, down in 41 of 45 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.195× (z -24.0, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRK1]] (+0.73, fdr 7e-06), [[PHACTR2]] (+0.67, fdr 3e-05), [[SLC25A21]] (+0.65, fdr 3e-05); moves opposite to [[SFXN3]] (-0.60, fdr 9e-05), [[SLC27A1]] (-0.57, fdr 1e-04), [[RAB3A]] (-0.56, fdr 3e-04).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8531.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +5.1 | 2e-04 | 26/44 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.8 | 4e-04 | 19/46 (LS 180, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +4.5 | 0.001 | 19/46 (LS 180, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.41×** | +4.4 | 0.001 | 18/46 (LS 180, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.34×** | +4.4 | 0.001 | 12/46 (RKO, KATO III, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +4.2 | 0.003 | 15/46 (LS 180, AsPC-1, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.61×** | +3.7 | 0.017 | 10/45 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.026 | 14/45 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.5 | 0.031 | 12/46 (LS 180, AsPC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.032 | 14/45 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.032 | 10/46 (LS 180, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.091 | 5/46 (NCI-H1573, HT-29, …) | top dose only |  |
| [[Finasteride (drug)]] 5 µM |  | 1.23× | +3.0 | 0.11 | 5/45 (NCI-H2030, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8531.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.289×** | -25.7 | 0e+00 | 41/45 (NCI-H23, LoVo, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.195×** | -24.0 | 0e+00 | 45/46 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.215×** | -22.6 | 0e+00 | 45/46 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.240×** | -20.9 | 0e+00 | 44/46 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.344×** | -15.6 | 0e+00 | 38/42 (HT-29, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.336×** | -15.4 | 0e+00 | 35/45 (RPMI-7951, NCI-H1573, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.385×** | -14.0 | 1e-42 | 42/46 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.460×** | -11.4 | 4e-28 | 36/46 (LoVo, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.487×** | -10.5 | 4e-24 | 36/44 (LoVo, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.545×** | -8.9 | 4e-17 | 34/46 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.320×** | -8.7 | 1e-16 | 36/45 (LoVo, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.342×** | -8.2 | 9e-15 | 32/43 (RPMI-7951, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.579×** | -8.0 | 6e-14 | 29/45 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.367×** | -7.7 | 6e-13 | 31/45 (HT-29, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.374×** | -7.5 | 2e-12 | 33/44 (NCI-H23, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.624×** | -6.9 | 2e-10 | 31/46 (A-172, hTERT-HPNE, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.631×** | -6.7 | 6e-10 | 26/46 (LoVo, RKO, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.753×** | -5.8 | 2e-07 | 27/46 (RKO, SW1417, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.719×** | -4.8 | 4e-05 | 23/45 (KATO III, LS 180, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.748×** | -4.2 | 6e-04 | 19/46 (J82, NCI-H2347, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8531. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 46.0 | 0 | 12 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0449× (z -26.3) |
| [[NCI-H23 (line)]] | alt | 41.6 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -23.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.175× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 31.4 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -16.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.103× (z -15.9) |
| [[COLO 205 (line)]] | alt | 59.6 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -20.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0870× (z -17.9) |
| [[SW1417 (line)]] | alt | 28.3 | 0 | 8 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.124× (z -16.0) |
| [[AsPC-1 (line)]] | alt | 24.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -20.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.146× (z -12.5) |
| [[HT-29 (line)]] | alt | 35.9 | 0 | 7 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0786× (z -19.1) |
| [[KATO III (line)]] | alt | 29.1 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0363× (z -21.6) |
| [[LS 180 (line)]] | wt | 44.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -17.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.127× (z -16.9) |
| [[RKO (line)]] | wt | 22.7 | 0 | 7 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0874× (z -14.2) |
| [[A498 (line)]] | wt | 25.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -18.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.149× (z -13.3) |
| [[C32 (line)]] | wt | 23.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -14.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.101× (z -12.2) |
| [[J82 (line)]] | alt | 25.1 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.140× (z -13.9) |
| [[NCI-H2030 (line)]] | alt | 33.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.203× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 32.6 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -13.9) |
| [[A-427 (line)]] | wt | 24.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -15.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.218× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 34.0 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.149× (z -16.6) |
| [[NCI-H1573 (line)]] | alt | 31.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -19.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 9.82 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -13.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -11.3) |
| [[SW480 (line)]] | alt | 14.1 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.110× (z -16.9) |
| [[A-172 (line)]] | wt | 11.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -11.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.170× (z -9.1) |
| [[HS-578T (line)]] | alt | 17.2 | 0 | 4 | — | [[Belinostat (drug)]] 0.5 µM 0.180× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 18.9 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0287× (z -17.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0427× (z -8.6) |
| [[Hs 766T (line)]] | wt | 18.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 16.6 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0990× (z -9.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.111× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 24.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -11.2) |
| [[SW48 (line)]] | wt | 29.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0205× (z -19.0) |
| [[A549 (line)]] | wt | 9.53 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0703× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 12.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -9.0) |
| [[PANC-1 (line)]] | alt | 12.4 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.233× (z -10.5) |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -10.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HCT15 (line)]] | alt | 22.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -8.6) |
| [[HOP62 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -13.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -12.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2347 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SNU-1 (line)]] | wt | 15.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.120× (z -8.6) |
| [[SNU-423 (line)]] | alt | 7.97 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0561× (z -11.7) |
| [[SW 900 (line)]] | alt | 9.21 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.116× (z -9.2) |
| [[AN3 CA (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.92 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8531), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRK1]] | +0.73 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[PHACTR2]] | +0.67 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[SLC25A21]] | +0.65 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[HNF4G]] | +0.64 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[CRPPA]] | +0.63 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[GRIP1]] | +0.62 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[NIPAL2]] | +0.62 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[KLHL42]] | +0.61 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[PRDM5]] | +0.61 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[ACTR3C]] | +0.61 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[TOR1A]] | +0.61 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[SLC37A1]] | +0.61 | +0.45 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFXN3]] | -0.60 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[SLC27A1]] | -0.57 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[RAB3A]] | -0.56 | -0.41 / -0.29 | both halves | 3e-04 |  |
| [[DNAAF3]] | -0.55 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[RRAS]] | -0.55 | -0.38 / -0.28 | both halves | 3e-04 |  |
| [[ETHE1]] | -0.55 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[DAD1]] | -0.55 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[GNAI2]] | -0.54 | -0.37 / -0.23 | both halves | 5e-04 |  |
| [[NME7]] | -0.54 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[PJA2]] | -0.54 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[LGALS1]] | -0.52 | -0.47 / -0.21 | both halves | 6e-04 |  |
| [[YIF1B]] | -0.52 | -0.31 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[SLC2A3]] | -0.52 | -0.32 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers TMCO4's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[LRRK1]] | B | LRRK1 activity raises TMCO4's level | lines that do not express LRRK1 (10) vs lines expressing it (40) | 2.46× lower at baseline in the lines without LRRK1 | 0.047 | ⚠ within organs, on part of the lines; also absent: HRH1, ALS2CL, CTSZ; maybe low, not absent |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises TMCO4's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 1.66× lower at baseline in the lines without SLC44A3-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[HTR1D]] | B | HTR1D activity raises TMCO4's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 1.37× lower at baseline in the lines without HTR1D | 0.063 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.708). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-4.7, 8.0); signed map (25.2, -31.1). **Vector** length 87.9, 22.7% of its response variance represented; |z| ≥ 3 in 1,322 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.1 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +5.1 | -3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +3.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.4 | +4.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.8 | -15.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.1 | -14.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.2 | -24.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.0 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -5.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | -3.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.2 | -4.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane and coiled-coil domains 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:19,682,240-19,799,945 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686C23231 |
| Matched by | ensembl_id |

UniProt [Q5TGY1](https://www.uniprot.org/uniprotkb/Q5TGY1) carries no function annotation.

**Summary**, from NCBI Gene [255104](https://www.ncbi.nlm.nih.gov/gene/255104):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27393) · Entrez [255104](https://www.ncbi.nlm.nih.gov/gene/255104) · UniProt [Q5TGY1](https://www.uniprot.org/uniprotkb/Q5TGY1) · Ensembl [ENSG00000162542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162542)

## Data

Gene col 8531: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8531); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8531, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8531]; `tensor/DDL_lfc|DDL_z.npy` [8531]; `embed/gene_vectors.npy` [8531]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8531 or target_col == 8531). Every well: [[TMCO4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMCO4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
