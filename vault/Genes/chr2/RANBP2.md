---
symbol: "RANBP2"
type: "gene"
col: 7700
ensembl_id: "ENSG00000153201"
name: "RAN binding protein 2"
location: "2q13"
module: 16
arm: "+"
pooled_cpm: 138.42
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# RANBP2

*RAN binding protein 2* — 2q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.46× (z +25.2, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.522× (z -12.9, q 3e-35, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.779× (z -3.6, q 0.043, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H1573 0.177×, HEC-1-A 0.193×, NCI-H460 0.303×, Panc 03.27 0.252×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW 900 0.291×, J82 0.314×, NCI-H23 0.382×, C32 0.255×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SW48 0.117×, SK-MEL-2 0.194×, RKO 0.275×; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (CHP-212 0.124×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BMS1]] (+0.62, fdr 7e-06), [[ABCF3]] (+0.62, fdr 1e-05), [[CDPF1]] (+0.61, fdr 3e-05); moves opposite to [[FAM81A]] (-0.50, fdr 3e-04), [[CRNDE]] (-0.49, fdr 4e-05), [[BBIP1]] (-0.47, fdr 6e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7700.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.46×** | +25.2 | 0e+00 | 46/48 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.45×** | +17.7 | 0e+00 | 47/48 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.96×** | +14.2 | 1e-43 | 48/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.01×** | +13.3 | 5e-38 | 47/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.10×** | +11.7 | 2e-29 | 44/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.74×** | +10.9 | 7e-26 | 46/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +10.9 | 7e-26 | 44/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +10.1 | 3e-22 | 45/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +8.9 | 4e-17 | 42/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +8.8 | 1e-16 | 42/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +7.7 | 8e-13 | 34/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +7.6 | 2e-12 | 40/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +7.3 | 9e-12 | 41/48 (SNU-423, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +7.2 | 3e-11 | 41/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +7.1 | 5e-11 | 35/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +5.4 | 3e-06 | 30/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7700.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H1573 0.177×, HEC-1-A 0.193×, NCI-H460 0.303×, Panc 03.27 0.252×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW 900 0.291×, J82 0.314×, NCI-H23 0.382×, C32 0.255×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SW48 0.117×, SK-MEL-2 0.194×, RKO 0.275×; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (CHP-212 0.124×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.522×** | -12.9 | 3e-35 | 44/49 (SW 900, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.595×** | -9.9 | 9e-21 | 36/44 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.641×** | -8.2 | 5e-14 | 33/45 (SW48, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -4.9 | 2e-04 | 23/49 (SK-MEL-2, RPMI-7951, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.779×** | -3.6 | 0.043 | 25/48 (HCT15, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7700. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 132 | 13 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.303× (z -17.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 152 | 10 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +24.2) | [[Dinaciclib (drug)]] 5 µM 0.574× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 146 | 9 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -14.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 103 | 11 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +20.1) | — |
| [[SW480 (line)]] | alt | 188 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.478× (z -11.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 196 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +20.5) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -19.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 119 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -21.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 126 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +20.8) | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -13.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 121 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +21.6) | — |
| [[LS 180 (line)]] | wt | 148 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +16.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 135 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +18.7) | — |
| [[SW48 (line)]] | wt | 170 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -19.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 103 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.455× (z -9.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 132 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +21.2) | [[Dinaciclib (drug)]] 0.5 µM 0.494× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 127 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +15.1) | — |
| [[NCI-H23 (line)]] | alt | 150 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 102 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +19.0) | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -11.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 134 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -15.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 178 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -12.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 97.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +12.0) | — |
| [[HCT15 (line)]] | alt | 143 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +17.5) | — |
| [[HOP62 (line)]] | alt | 156 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -11.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 89.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.5) | — |
| [[NCI-H2030 (line)]] | alt | 104 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -10.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 184 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -9.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 178 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -11.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 130 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +19.4) | — |
| [[BT-474 (line)]] | alt | 104 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +15.5) | — |
| [[HepG2_C3A (line)]] | wt | 146 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +13.7) | — |
| [[J82 (line)]] | alt | 148 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -14.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 76.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +17.5) | — |
| [[RPMI-7951 (line)]] | alt | 208 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -11.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 128 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -18.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 155 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -12.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 269 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -14.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 153 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 99.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +17.7) | — |
| [[H4 (line)]] | wt | 115 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +14.4) | — |
| [[HS-578T (line)]] | alt | 95.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.6) | — |
| [[hTERT-HPNE (line)]] | wt | 110 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.9) | — |
| [[SNU-423 (line)]] | alt | 98.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 146 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.4) | — |
| [[CHP-212 (line)]] | wt | 149 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.124× (z -13.9) |
| [[AN3 CA (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 199 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7700), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMS1]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 | STRING 416 |
| [[ABCF3]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CDPF1]] | +0.61 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[PSMD6]] | +0.59 | +0.63 / +0.57 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[PWP1]] | +0.59 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[AGGF1]] | +0.58 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[PREB]] | +0.56 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[FANCF]] | +0.56 | +0.50 / +0.46 | both halves | 2e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[TSPYL5]] | +0.55 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[MYG1]] | +0.55 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[WDR70]] | +0.54 | +0.36 / +0.57 | both halves | 1e-04 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[THAP7]] | +0.54 | +0.47 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM81A]] | -0.50 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[CRNDE]] | -0.49 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[BBIP1]] | -0.47 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[KPNB1-DT]] | -0.46 | -0.24 / -0.52 | both halves | 5e-04 |  |
| [[TNPO2]] | -0.46 | -0.41 / -0.34 | both halves | 1e-04 | STRING 425 |
| [[TRNAU1AP]] | -0.45 | -0.34 / -0.58 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.421). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-45.0, -6.2); signed map (-4.5, -30.3). **Vector** length 72.9, 22.4% of its response variance represented; |z| ≥ 3 in 1,252 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +7.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.1 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +0.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.6 | +10.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.4 | +7.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | +7.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.1 | +5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -4.9 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | +0.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | +1.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | +0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | RAN binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q13 — chr2:108,719,482-108,785,810 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NUP358, ADANE; previously ANE1 |
| Gene groups (HGNC) | Zinc fingers RANBP2-type; Tetratricopeptide repeat domain containing; Cyclophilin peptidylprolyl isomerases; Nucleoporins; Atypical E3 ubiquitin ligases |
| Reactome | 86 pathways, smallest: IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus; IPs transport between nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [P49792](https://www.uniprot.org/uniprotkb/P49792) (E3 SUMO-protein ligase RanBP2):

> E3 SUMO-protein ligase which facilitates SUMO1 and SUMO2 conjugation by UBE2I. Involved in transport factor (Ran-GTP, karyopherin)-mediated protein import via the F-G repeat-containing domain which acts as a docking site for substrates. Binds single-stranded RNA (in vitro). May bind DNA. Component of the nuclear export pathway. Specific docking site for the nuclear export factor exportin-1. Inhibits EIF4E-dependent mRNA export. Sumoylates PML at 'Lys-490' which is essential for the proper …

**Summary**, from NCBI Gene [5903](https://www.ncbi.nlm.nih.gov/gene/5903):

> RAN is a small GTP-binding protein of the RAS superfamily that is associated with the nuclear membrane and is thought to control a variety of cellular functions through its interactions with other proteins. This gene encodes a very large RAN-binding protein that immunolocalizes to the nuclear pore complex. The protein is a giant scaffold and mosaic cyclophilin-related nucleoporin implicated in the Ran-GTPase cycle. The encoded protein directly interacts with the E2 enzyme UBC9 and strongly …

**Accessions** — [HGNC:9848](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9848) · Entrez [5903](https://www.ncbi.nlm.nih.gov/gene/5903) · UniProt [P49792](https://www.uniprot.org/uniprotkb/P49792) · Ensembl [ENSG00000153201](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153201)

## Data

Gene col 7700: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7700); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7700, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7700]; `tensor/DDL_lfc|DDL_z.npy` [7700]; `embed/gene_vectors.npy` [7700]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7700 or target_col == 7700). Every well: [[RANBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RANBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
