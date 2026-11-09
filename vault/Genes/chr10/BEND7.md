---
symbol: "BEND7"
type: "gene"
col: 9150
ensembl_id: "ENSG00000165626"
name: "BEN domain containing 7"
location: "10p13"
module: 222
arm: "+"
pooled_cpm: 19.95
n_lines_expressing: 38
n_dd_up: 26
n_dd_down: 18
n_dd_up_clean: 20
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/222"]
generated_by: "tahoemap"
---

# BEND7

*BEN domain containing 7* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.69× (z +9.1, q 4e-17, up in 19 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.466× (z -13.3, q 1e-37, down in 26 of 35 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.554× (z -5.4, q 6e-06, down in 19 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DENND5B]] (+0.65, fdr 7e-06), [[GKAP1]] (+0.62, fdr 7e-06), [[TLCD5]] (+0.60, fdr 1e-05); moves opposite to [[TXN2]] (-0.49, fdr 4e-05), [[WDR37]] (-0.48, fdr 9e-05), [[LOX]] (-0.48, fdr 4e-05).
> It is in [[Module 222]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MCOLN3]] → it (grade B ⚠); 3 go from it, the strongest it → [[RUFY3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9150.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.69×** | +9.1 | 4e-17 | 19/35 (HOP62, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +8.0 | 4e-13 | 23/35 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +7.6 | 4e-12 | 22/34 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +7.4 | 2e-11 | 19/35 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +6.4 | 2e-08 | 15/35 (NCI-H1792, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +6.3 | 3e-08 | 15/35 (HOP62, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.43×** | +6.3 | 3e-08 | 16/35 (A-172, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.43×** | +6.0 | 1e-07 | 18/35 (A-172, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +5.9 | 3e-07 | 16/35 (HOP62, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +5.4 | 3e-06 | 18/35 (HOP62, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | **1.24×** | +5.2 | 9e-06 | 14/36 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +5.1 | 2e-05 | 17/36 (A-172, RKO, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +4.9 | 4e-05 | 14/34 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 4e-04 | 13/34 (A-172, SW 900, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.28×** | +4.3 | 5e-04 | 12/33 (Hs 766T, CFPAC-1, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.002 | 14/35 (A-172, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.002 | 13/35 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9150.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.466×** | -13.3 | 1e-37 | 26/35 (A549, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.467×** | -13.3 | 1e-37 | 27/35 (A549, Panc 03.27, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.552×** | -10.4 | 8e-23 | 23/35 (A549, HepG2/C3A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.754×** | -6.9 | 5e-10 | 23/35 (HepG2/C3A, NCI-H2030, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **0.665×** | -6.6 | 6e-09 | 19/30 (NCI-H1792, A-427, …) | inconsistent across doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.706×** | -5.8 | 6e-07 | 17/35 (NCI-H23, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.554×** | -5.4 | 6e-06 | 19/35 (NCI-H2030, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.766×** | -4.5 | 6e-04 | 14/35 (SW48, NCI-H2030, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.776×** | -4.4 | 6e-04 | 16/35 (RKO, HEC-1-A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.777×** | -4.4 | 7e-04 | 16/32 (A-427, RKO, …) | inconsistent across doses | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.648×** | -3.9 | 0.004 | 11/34 (A498, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.662×** | -3.7 | 0.008 | 11/34 (MIA PaCa-2, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.815×** | -3.5 | 0.017 | 8/35 (AsPC-1, SW 900, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.808×** | -3.5 | 0.019 | 10/35 (RKO, HCT15, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.821×** | -3.4 | 0.024 | 12/35 (A-172, SW 900, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.828×** | -3.3 | 0.037 | 8/35 (A-172, HS-578T, …) | all doses, flat |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.708×** | -3.1 | 0.056 | 9/30 (RKO, A549, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.882× | -3.1 | 0.065 | 13/36 (A-427, SW1417, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.719×** | -3.0 | 0.076 | 13/34 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | 0.844× | -2.9 | 0.089 | 11/34 (A-172, A498, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 0.834× | -2.9 | 0.090 | 9/34 (HOP62, SW 900, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.846× | -2.9 | 0.092 | 7/35 (J82, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.59 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9150. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 123 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -15.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[RKO (line)]] | wt | 110 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.266× (z -12.3) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 54.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -11.7) |
| [[A-427 (line)]] | wt | 39.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 40.2 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.214× (z -14.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H2030 (line)]] | alt | 36.7 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.179× (z -14.3) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.136× (z -9.0) |
| [[KATO III (line)]] | alt | 21.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.220× (z -10.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[LoVo (line)]] | wt | 35.4 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -13.4) ⚠ cell-cycle shift, explains ~50% of this change |
| [[C-33 A (line)]] | alt | 55.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 11.9 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.70× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.61× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 26.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -13.2) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW1417 (line)]] | alt | 15.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.247× (z -10.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 43.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0808× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[NCI-H23 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0722× (z -15.7) ⚠ cell-cycle shift, explains ~62% of this change |
| [[PANC-1 (line)]] | alt | 6.19 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0272× (z -11.1) |
| [[SNU-1 (line)]] | wt | 47.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 37.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -10.2) ⚠ cell-cycle shift, explains ~89% of this change |
| [[SW480 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 4.73 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9150), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND5B]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[GKAP1]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[TLCD5]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[FAM171A1]] | +0.59 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ITSN2]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[MARK1]] | +0.57 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[DNMT3A]] | +0.56 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[AGO4]] | +0.54 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[ZDHHC1]] | +0.54 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[MAFG]] | +0.52 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[ZNRF2P2]] | +0.52 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[PAWR]] | +0.52 | +0.49 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXN2]] | -0.49 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[WDR37]] | -0.48 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[LOX]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ATP5F1B]] | -0.47 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[CHPF]] | -0.47 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[MAN1B1]] | -0.45 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[SEC24C]] | -0.45 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[JPH2]] | -0.45 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[DDX41]] | -0.44 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[GNAI3]] | -0.44 | -0.45 / -0.32 | both halves | 1e-04 |  |
| [[MATCAP1]] | -0.43 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[SMAP2]] | -0.43 | -0.31 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCOLN3]] | B | MCOLN3 activity raises BEND7's level | lines that do not express MCOLN3 (18) vs lines expressing it (32) | 2.39× lower at baseline in the lines without MCOLN3 | 0.013 | ⚠ within organs, on part of the lines; also absent: PNMA2, STOX2, NTN1 |
| [[MSI1]] | B | MSI1 activity raises BEND7's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.84× lower at baseline in the lines without MSI1 | 0.093 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[ZDHHC2]] | B | ZDHHC2 activity raises BEND7's level | lines that do not express ZDHHC2 (10) vs lines expressing it (40) | 1.88× lower at baseline in the lines without ZDHHC2 | 0.0999 | ⚠ within organs, on part of the lines; also absent: ENSG00000289145, TGFB1, PGM5P2 |
| [[HOMER3]] | C | HOMER3 activity raises BEND7's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 5.68× lower at baseline in the lines without HOMER3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RUFY3]] | B | BEND7 activity lowers RUFY3's level | lines that do not express BEND7 (12) vs lines expressing it (38) | 1.59× higher at baseline in the lines without BEND7 | 0.013 | ⚠ within organs, on part of the lines; also absent: ZIC2 |
| [[SNX24]] | B | BEND7 activity raises SNX24's level | lines that do not express BEND7 (12) vs lines expressing it (38) | 1.31× lower at baseline in the lines without BEND7 | 0.039 | ⚠ within organs, on part of the lines; also absent: ZIC2 |
| [[MCOLN3]] | B | BEND7 activity raises MCOLN3's level | lines that do not express BEND7 (12) vs lines expressing it (38) | 1.88× lower at baseline in the lines without BEND7 | 0.043 | ⚠ within organs, on part of the lines; also absent: ZIC2 |

## Where it sits

- **Module**: [[Module 222]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.5, 12.4); signed map (8.0, -6.6). **Vector** length 94.7, 23.1% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +7.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.5 | +8.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.1 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.0 | +5.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.3 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.3 | -13.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.1 | -13.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -2.4 | -5.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.3 | -2.0 |
|  | [[EX229 (drug)]] 0.05 µM |  | -2.1 | -3.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -3.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | BEN domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:13,438,484-13,529,014 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40283; previously C10orf30 |
| Gene groups (HGNC) | BEN domain containing |
| Matched by | ensembl_id |

UniProt [Q8N7W2](https://www.uniprot.org/uniprotkb/Q8N7W2) carries no function annotation.

**Summary**, from NCBI Gene [222389](https://www.ncbi.nlm.nih.gov/gene/222389):

> Predicted to enable DNA binding activity. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23514](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23514) · Entrez [222389](https://www.ncbi.nlm.nih.gov/gene/222389) · UniProt [Q8N7W2](https://www.uniprot.org/uniprotkb/Q8N7W2) · Ensembl [ENSG00000165626](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165626)

## Data

Gene col 9150: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9150); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9150, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9150]; `tensor/DDL_lfc|DDL_z.npy` [9150]; `embed/gene_vectors.npy` [9150]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9150 or target_col == 9150). Every well: [[BEND7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BEND7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
