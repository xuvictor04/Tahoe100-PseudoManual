---
symbol: "BCL2L13"
type: "gene"
col: 1836
ensembl_id: "ENSG00000099968"
name: "BCL2 like 13"
location: "22q11.21"
module: 88
arm: "+"
pooled_cpm: 66.1
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# BCL2L13

*BCL2 like 13* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.46× (z +14.9, q 0e+00, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.720× (z -9.2, q 3e-17, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB30-DT]] (+0.74, fdr 7e-06), [[C6orf62]] (+0.67, fdr 1e-05), [[SLC9A8]] (+0.67, fdr 1e-05); moves opposite to [[LPCAT4]] (-0.69, fdr 7e-06), [[GMCL1]] (-0.64, fdr 1e-05), [[PLEKHH3]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 088]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1836.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +14.9 | 0e+00 | 36/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +9.2 | 2e-17 | 36/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +8.8 | 2e-16 | 32/48 (COLO 205, C32, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +6.8 | 1e-09 | 29/48 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.27×** | +6.7 | 2e-09 | 23/48 (COLO 205, NCI-H2347, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +6.4 | 2e-08 | 25/48 (Hs 766T, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +5.0 | 5e-05 | 9/48 (A498, Panc 03.27, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.19× | +4.8 | 9e-05 | 19/48 (J82, A498, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.18× | +4.6 | 2e-04 | 18/48 (NCI-H2347, RKO, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.18× | +4.6 | 3e-04 | 18/49 (A498, hTERT-HPNE, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +4.1 | 0.002 | 19/45 (J82, C-33 A, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.14× | +3.6 | 0.017 | 17/48 (NCI-H23, SNU-1, …) | inconsistent across doses | composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.14× | +3.5 | 0.021 | 15/48 (COLO 205, H4, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.12× | +3.1 | 0.069 | 12/48 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~8% of this change | 1.12× | +3.1 | 0.080 | 10/46 (A-172, NCI-H2347, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1836.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.720×** | -9.2 | 3e-17 | 35/48 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.725×** | -8.9 | 1e-16 | 33/48 (RKO, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.718×** | -8.9 | 2e-16 | 31/47 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.735×** | -8.6 | 1e-15 | 34/48 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.828×** | -7.4 | 1e-11 | 28/48 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.788×** | -6.6 | 3e-09 | 26/48 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[NG25 (drug)]] 5 µM |  | **0.664×** | -6.0 | 2e-07 | 30/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.811×** | -5.8 | 4e-07 | 23/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.681×** | -5.6 | 1e-06 | 21/37 (BT-474, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.873× | -5.4 | 5e-06 | 13/48 (RKO, CHP-212, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.705×** | -5.1 | 2e-05 | 19/48 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.834× | -5.1 | 2e-05 | 23/48 (RKO, H4, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -4.9 | 5e-05 | 22/48 (CHP-212, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.774×** | -3.7 | 0.007 | 12/49 (RKO, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.876× | -3.7 | 0.008 | 19/47 (SW480, C-33 A, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1836. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 53.2 | 1 (1 ⚠) | 5 (5 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.94× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.319× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 67.5 | 1 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.53× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.407× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[RKO (line)]] | wt | 86.8 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.275× (z -14.9) |
| [[NCI-H2030 (line)]] | alt | 76.9 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +14.8) | [[Panobinostat (drug)]] 0.5 µM 0.431× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 63.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 72.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.428× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 45.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.2) | — |
| [[A498 (line)]] | wt | 84.0 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 1.85× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 66.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 70.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 77.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.8) | — |
| [[LoVo (line)]] | wt | 58.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.443× (z -10.1) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 145 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.527× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 54.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +13.0) | — |
| [[CFPAC-1 (line)]] | alt | 59.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.6) | — |
| [[HepG2_C3A (line)]] | wt | 41.7 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.225× (z -8.8) |
| [[Hs 766T (line)]] | wt | 82.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 108 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +14.6) | — |
| [[NCI-H1792 (line)]] | alt | 82.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.421× (z -9.8) |
| [[NCI-H596 (line)]] | alt | 59.8 | 0 | 1 | — | [[Elimusertib hydrochloride (drug)]] 0.5 µM 0.339× (z -10.4) |
| [[SHP-77 (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0960× (z -11.1) ⚠ toxic |
| [[SW 900 (line)]] | alt | 46.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 63.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 84.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1836), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB30-DT]] | +0.74 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[C6orf62]] | +0.67 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[SLC9A8]] | +0.67 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[GABPB2]] | +0.65 | +0.66 / +0.46 | both halves | 2e-05 |  |
| [[ZCWPW1]] | +0.65 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[CLHC1]] | +0.64 | +0.66 / +0.32 | both halves | 1e-04 |  |
| [[MRPL45]] | +0.63 | +0.75 / +0.32 | both halves | 2e-04 |  |
| [[CARD8]] | +0.63 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ZNF181]] | +0.63 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[FKRP]] | +0.63 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[LACC1]] | +0.62 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[SNAPC5]] | +0.62 | +0.68 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPCAT4]] | -0.69 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.64 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.62 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[FAM102B]] | -0.62 | -0.63 / -0.49 | both halves | 2e-05 |  |
| [[SLC9A6]] | -0.61 | -0.64 / -0.38 | both halves | 7e-05 |  |
| [[GLRX5]] | -0.60 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[SMARCD2]] | -0.60 | -0.70 / -0.39 | both halves | 5e-05 |  |
| [[METAP1]] | -0.59 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[KIAA2013]] | -0.59 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[PCMT1]] | -0.59 | -0.63 / -0.30 | both halves | 2e-04 |  |
| [[NFRKB]] | -0.59 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.58 | -0.60 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.700). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (4.5, 6.5); signed map (17.6, -24.2). **Vector** length 111, 26.5% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +9.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.0 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +14.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.2 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +4.9 | +4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +5.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.4 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -7.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.0 | -8.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.6 | -8.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.6 | -9.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.5 | -8.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.6 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 like 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:17,628,855-17,730,855 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MIL1, BCL-RAMBO |
| Gene groups (HGNC) | BCL2 family |
| Hallmark sets | ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXK5](https://www.uniprot.org/uniprotkb/Q9BXK5) (Bcl-2-like protein 13):

> May promote the activation of caspase-3 and apoptosis.

**Summary**, from NCBI Gene [23786](https://www.ncbi.nlm.nih.gov/gene/23786):

> This gene encodes a mitochondrially-localized protein with conserved B-cell lymphoma 2 homology motifs. Overexpression of the encoded protein results in apoptosis. Alternatively spliced transcript variants have been observed for this gene. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:17164](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17164) · Entrez [23786](https://www.ncbi.nlm.nih.gov/gene/23786) · UniProt [Q9BXK5](https://www.uniprot.org/uniprotkb/Q9BXK5) · Ensembl [ENSG00000099968](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099968)

## Data

Gene col 1836: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1836); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1836, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1836]; `tensor/DDL_lfc|DDL_z.npy` [1836]; `embed/gene_vectors.npy` [1836]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1836 or target_col == 1836). Every well: [[BCL2L13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL2L13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
