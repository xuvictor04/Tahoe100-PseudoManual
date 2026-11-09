---
symbol: "CCSER1"
type: "gene"
col: 11517
ensembl_id: "ENSG00000184305"
name: "coiled-coil serine rich protein 1"
location: "4q22.1"
module: 8
arm: "+"
pooled_cpm: 142.43
n_lines_expressing: 30
n_dd_up: 15
n_dd_down: 28
n_dd_up_clean: 15
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 24
direction_downstream: 24
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# CCSER1

*coiled-coil serine rich protein 1* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.56× (z +10.2, q 9e-22, up in 19 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.376× (z -15.2, q 0e+00, down in 26 of 28 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.310× (z -9.9, q 1e-20, down in 25 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD12]] (+0.74, fdr 7e-06), [[PLCH1]] (+0.70, fdr 7e-06), [[LINC02331]] (+0.64, fdr 1e-05); moves opposite to [[SNX21]] (-0.53, fdr 3e-05), [[CROCCP3]] (-0.52, fdr 4e-05), [[AP1M1]] (-0.52, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[FAAH2]] → it (grade B ⚠); 24 go from it, the strongest it → [[PCAT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, none with an alert; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11517.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +10.2 | 9e-22 | 19/28 (HOP62, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.78×** | +9.4 | 2e-18 | 22/29 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +6.7 | 3e-09 | 20/28 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +5.4 | 8e-06 | 18/28 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +4.3 | 0.002 | 13/28 (NCI-H1573, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +4.3 | 0.002 | 12/28 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.29×** | +4.2 | 0.003 | 16/28 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.20× | +4.0 | 0.004 | 12/29 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.007 | 12/28 (NCI-H1573, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.014 | 11/29 (NCI-H1573, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.018 | 12/28 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.018 | 8/28 (A498, HOP62, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.029 | 14/28 (AsPC-1, C-33 A, …) | rises with dose |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.035 | 10/29 (HOP62, Panc 03.27, …) | inconsistent across doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.036 | 5/29 (Panc 03.27, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11517.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.376×** | -15.2 | 0e+00 | 26/28 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.310×** | -9.9 | 1e-20 | 25/29 (LS 180, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.570×** | -8.7 | 6e-16 | 23/28 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.591×** | -8.5 | 4e-15 | 25/28 (LS 180, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.609×** | -8.0 | 1e-13 | 20/28 (SW48, COLO 205, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.634×** | -7.3 | 2e-11 | 21/28 (SW48, SW480, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.432×** | -7.1 | 1e-10 | 25/28 (LS 180, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.657×** | -6.8 | 9e-10 | 17/28 (NCI-H1792, NCI-H23, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.666×** | -6.3 | 2e-08 | 20/28 (SW48, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.678×** | -6.0 | 1e-07 | 19/28 (SW48, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.700×** | -5.7 | 5e-07 | 17/28 (A-427, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.710×** | -5.1 | 2e-05 | 18/28 (NCI-H661, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.729×** | -5.1 | 2e-05 | 19/28 (COLO 205, SW48, …) | two highest doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.729×** | -4.9 | 4e-05 | 21/28 (SW48, LS 180, …) | top dose only | plate-row cell shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.742×** | -4.8 | 6e-05 | 17/28 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.756×** | -4.5 | 2e-04 | 17/28 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.748×** | -4.5 | 2e-04 | 17/28 (LS 180, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.769×** | -4.2 | 7e-04 | 17/28 (SW48, A498, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.833×** | -4.1 | 1e-03 | 14/29 (SW48, Panc 03.27, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.778×** | -4.0 | 0.001 | 18/28 (LS 180, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.843× | -3.9 | 0.003 | 15/29 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Irinotecan (drug)]] 5 µM |  | **0.657×** | -3.5 | 0.010 | 17/30 (LoVo, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.809×** | -3.3 | 0.024 | 11/28 (CFPAC-1, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11517. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 833 | 0 | 20 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -25.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -18.7) |
| [[LS 180 (line)]] | wt | 525 | 0 | 16 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0952× (z -12.3) |
| [[HT-29 (line)]] | alt | 885 | 0 | 13 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0926× (z -23.0) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.285× (z -12.1) |
| [[A-427 (line)]] | wt | 436 | 1 (1 ⚠) | 11 (7 ⚠) | [[Selinexor (drug)]] 5 µM 1.83× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -18.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -18.8) |
| [[LoVo (line)]] | wt | 725 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.344× (z -12.0) |
| [[SW480 (line)]] | alt | 112 | 0 | 10 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H1573 (line)]] | alt | 307 | 3 (1 ⚠) | 5 (5 ⚠) | [[Cobimetinib (drug)]] 5 µM 3.02× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.143× (z -17.2) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 86.4 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -15.3) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.278× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 227 | 1 | 6 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.05× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.176× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H2030 (line)]] | alt | 120 | 0 | 7 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.177× (z -13.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.292× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 78.0 | 2 (1 ⚠) | 5 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.44× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.174× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[RKO (line)]] | wt | 66.5 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -10.7) |
| [[C-33 A (line)]] | alt | 278 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.108× (z -14.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.202× (z -10.7) |
| [[SHP-77 (line)]] | alt | 222 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -15.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.212× (z -9.8) |
| [[BT-474 (line)]] | alt | 296 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.334× (z -10.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.354× (z -9.0) |
| [[HOP62 (line)]] | alt | 49.7 | 4 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.78× (z +11.8) | — |
| [[A498 (line)]] | wt | 88.6 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.213× (z -13.8) |
| [[KATO III (line)]] | alt | 96.9 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.152× (z -16.3) ⚠ toxic |
| [[SW 900 (line)]] | alt | 208 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.151× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 73.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 110 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.10× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.212× (z -12.5) ⚠ toxic |
| [[A-172 (line)]] | wt | 14.1 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 27.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 13.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 60.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 25.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 17.0 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.3 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.7 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 28.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 41.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11517), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD12]] | +0.74 | +0.73 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[PLCH1]] | +0.70 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[LINC02331]] | +0.64 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[GRHL2]] | +0.63 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[MTUS1]] | +0.62 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PIP5K1B]] | +0.61 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ANK3]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[DENND2D]] | +0.59 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[ARHGEF38]] | +0.59 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[NPNT]] | +0.58 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[SLC44A3-AS1]] | +0.58 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[RASSF6]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX21]] | -0.53 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[CROCCP3]] | -0.52 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[AP1M1]] | -0.52 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[PDLIM7]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ZNF333]] | -0.50 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[SIRT3]] | -0.49 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[BCL7C]] | -0.48 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[TUBGCP2]] | -0.48 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[ITGB1BP1]] | -0.47 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[CCM2]] | -0.47 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[CROCCP3-1]] | -0.46 | -0.45 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 13, C 11. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAAH2]] | B | FAAH2 activity raises CCSER1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 3.14× lower at baseline in the lines without FAAH2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[POU5F1B]] | B | POU5F1B activity raises CCSER1's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 3.54× lower at baseline in the lines without POU5F1B | 0.014 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[ANK3]] | B | ANK3 activity raises CCSER1's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 3.13× lower at baseline in the lines without ANK3 | 0.020 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[PCAT1]] | B | PCAT1 activity raises CCSER1's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 3.47× lower at baseline in the lines without PCAT1 | 0.027 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[FOXP2]] | B | FOXP2 activity raises CCSER1's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 3.04× lower at baseline in the lines without FOXP2 | 0.033 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6 |
| [[MTUS1]] | B | MTUS1 activity raises CCSER1's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 3.65× lower at baseline in the lines without MTUS1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[SAMD12-AS1]] | B | SAMD12-AS1 activity raises CCSER1's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 2.59× lower at baseline in the lines without SAMD12-AS1 | 0.037 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[SH3BGRL2]] | B | SH3BGRL2 activity raises CCSER1's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 3.26× lower at baseline in the lines without SH3BGRL2 | 0.049 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers CCSER1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[MGC32805]] | B | MGC32805 activity raises CCSER1's level | lines that do not express MGC32805 (32) vs lines expressing it (18) | 3.66× lower at baseline in the lines without MGC32805 | 0.055 | ⚠ within organs, on part of the lines; also absent: CEACAM5, ST18, PRR15L; maybe low, not absent |
| [[LINC02331]] | B | LINC02331 activity raises CCSER1's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 3.05× lower at baseline in the lines without LINC02331 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2 |
| [[SORL1]] | B | SORL1 activity raises CCSER1's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.78× lower at baseline in the lines without SORL1 | 0.073 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 15, C 9. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCAT1]] | B | CCSER1 activity raises PCAT1's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 2.35× lower at baseline in the lines without CCSER1 | 0.008 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |
| [[HNF4G]] | B | CCSER1 activity raises HNF4G's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 2.75× lower at baseline in the lines without CCSER1 | 0.021 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |
| [[SIRT3]] | B | CCSER1 activity lowers SIRT3's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 1.31× higher at baseline in the lines without CCSER1 | 0.026 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |
| [[SH3BGRL2]] | B | CCSER1 activity raises SH3BGRL2's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 2.73× lower at baseline in the lines without CCSER1 | 0.033 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |
| [[SAMD12-AS1]] | B | CCSER1 activity raises SAMD12-AS1's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 2.19× lower at baseline in the lines without CCSER1 | 0.042 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |
| [[SLC44A3-AS1]] | B | CCSER1 activity raises SLC44A3-AS1's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 1.83× lower at baseline in the lines without CCSER1 | 0.046 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |
| [[FOXP2]] | B | CCSER1 activity raises FOXP2's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 2.63× lower at baseline in the lines without CCSER1 | 0.061 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |
| [[PROM1]] | B | CCSER1 activity raises PROM1's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 2.33× lower at baseline in the lines without CCSER1 | 0.066 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |
| [[POU5F1B]] | B | CCSER1 activity raises POU5F1B's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 1.79× lower at baseline in the lines without CCSER1 | 0.070 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |
| [[CHN2]] | B | CCSER1 activity raises CHN2's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 2.17× lower at baseline in the lines without CCSER1 | 0.071 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |
| [[BCL7C]] | B | CCSER1 activity lowers BCL7C's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 1.28× higher at baseline in the lines without CCSER1 | 0.073 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |
| cells under [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM | B | CCSER1 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express CCSER1 (20) vs lines expressing it (28) | the lines without CCSER1: 0.90× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.6, 51.1); signed map (58.2, 1.5). **Vector** length 106, 32.2% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.9 | +2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.7 | -1.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.6 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | -1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +3.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.8 | -15.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.8 | -8.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.8 | -8.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -2.5 | -5.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.3 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -4.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.8 | -4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -5.1 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil serine rich protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.1 — chr4:90,127,394-91,605,295 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1680; previously FAM190A |
| Matched by | ensembl_id |

UniProt [Q9C0I3](https://www.uniprot.org/uniprotkb/Q9C0I3) carries no function annotation.

**Summary**, from NCBI Gene [401145](https://www.ncbi.nlm.nih.gov/gene/401145):

> Predicted to act upstream of or within several processes, including osteoclast differentiation; protein activation cascade; and protein stabilization. Implicated in alcohol dependence and cocaine dependence. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29349) · Entrez [401145](https://www.ncbi.nlm.nih.gov/gene/401145) · UniProt [Q9C0I3](https://www.uniprot.org/uniprotkb/Q9C0I3) · Ensembl [ENSG00000184305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184305)

## Data

Gene col 11517: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11517); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11517, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11517]; `tensor/DDL_lfc|DDL_z.npy` [11517]; `embed/gene_vectors.npy` [11517]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11517 or target_col == 11517). Every well: [[CCSER1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCSER1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
