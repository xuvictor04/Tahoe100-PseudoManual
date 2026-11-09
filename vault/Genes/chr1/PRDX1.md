---
symbol: "PRDX1"
type: "gene"
col: 3909
ensembl_id: "ENSG00000117450"
name: "peroxiredoxin 1"
location: "1p34.1"
module: 60
arm: "+"
pooled_cpm: 133.46
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# PRDX1

*peroxiredoxin 1* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.29× (z +11.3, q 1e-26, up in 48 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.53× (z +8.8, q 3e-16, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.560× (z -7.5, q 3e-11, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (A-427 0.163×, NCI-H2030 0.245×, NCI-H23 0.282×, RKO 0.298×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.173×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SW 1088 0.0793×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXN]] (+0.70, fdr 7e-06), [[HSP90AA1]] (+0.66, fdr 7e-06), [[HSP90AA2P]] (+0.62, fdr 1e-05); moves opposite to [[YY1AP1]] (-0.65, fdr 7e-06), [[RCHY1]] (-0.63, fdr 7e-06), [[ZC3H7A]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3909.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **3.29×** | +11.3 | 1e-26 | 48/48 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **3.17×** | +10.5 | 3e-23 | 43/44 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.53×** | +8.8 | 3e-16 | 46/48 (C32, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.44×** | +7.7 | 2e-12 | 41/45 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +7.5 | 8e-12 | 41/49 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.14×** | +7.2 | 7e-11 | 46/48 (HOP62, CFPAC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.94×** | +6.3 | 3e-08 | 45/48 (CFPAC-1, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.85×** | +5.8 | 5e-07 | 36/48 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.79×** | +5.5 | 2e-06 | 41/48 (SNU-1, HCT15, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.78×** | +5.1 | 1e-05 | 41/48 (HT-29, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.74×** | +5.0 | 3e-05 | 40/50 (SW480, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.60×** | +4.4 | 5e-04 | 31/48 (HCT15, SNU-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.59×** | +4.4 | 5e-04 | 37/47 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.59×** | +4.2 | 0.001 | 33/48 (SNU-423, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.001 | 32/48 (HOP62, A-172, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.050 | 35/48 (AsPC-1, A498, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.077 | 29/48 (HT-29, NCI-H460, …) | top dose only |  |
| [[Auranofin (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.077 | 26/48 (BT-474, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3909.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (A-427 0.163×, NCI-H2030 0.245×, NCI-H23 0.282×, RKO 0.298×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.173×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SW 1088 0.0793×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.560×** | -7.5 | 3e-11 | 35/48 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 5 µM |  | 0.689× | -3.6 | 0.11 | 35/48 (NCI-H2030, Hs 766T, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.714× | -3.2 | 0.24 | 36/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.510× | -3.1 | 0.30 | 35/49 (Hs 766T, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.797× | -3.0 | 0.30 | 30/48 (A-172, LoVo, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3909. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 102 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.46× (z +9.0) | — |
| [[C32 (line)]] | wt | 45.3 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.45× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 104 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.08× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 135 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.18× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -9.8) |
| [[SW480 (line)]] | alt | 119 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.85× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -8.8) |
| [[A549 (line)]] | wt | 115 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[KATO III (line)]] | alt | 148 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 161 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.2× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H1792 (line)]] | alt | 69.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.8× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[Panc 03.27 (line)]] | alt | 82.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 63.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +10.2) | — |
| [[A-172 (line)]] | wt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A-427 (line)]] | wt | 268 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -17.9) |
| [[A498 (line)]] | wt | 184 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[AsPC-1 (line)]] | alt | 110 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.05× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.3) |
| [[C-33 A (line)]] | alt | 105 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -10.7) |
| [[Hs 766T (line)]] | wt | 135 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 63.4 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.97× (z +9.8) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[J82 (line)]] | alt | 123 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.35× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[LoVo (line)]] | wt | 172 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.78× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 86.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H460 (line)]] | wt | 197 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.28× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[RKO (line)]] | wt | 116 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -12.3) |
| [[SHP-77 (line)]] | alt | 74.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 111 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.81× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[AN3 CA (line)]] | alt | 100 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.98× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[BT-474 (line)]] | alt | 90.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -9.9) |
| [[CHP-212 (line)]] | wt | 46.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.13× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[COLO 205 (line)]] | alt | 88.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.64× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 177 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 148 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[HS-578T (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H2030 (line)]] | alt | 298 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 142 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 101 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[RPMI-7951 (line)]] | alt | 67.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[SNU-1 (line)]] | wt | 134 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.75× (z +8.7) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[SW 1088 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0793× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 65.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[H4 (line)]] | wt | 171 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 92.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 151 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 145 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3909), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXN]] | +0.70 | +0.73 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_REACTIVE_OXYGEN_SPECIES_PATHWAY; STRING 990 |
| [[HSP90AA1]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 | pathway: Binding and Uptake of Ligands by Scavenger Receptors; STRING 753 |
| [[HSP90AA2P]] | +0.62 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[ARPC5]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[HSPE1]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 610 |
| [[VCP]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 | pathway: Cellular response to chemical stress; STRING 404 |
| [[SFXN5]] | +0.58 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[TXNRD1]] | +0.58 | +0.65 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 795 |
| [[HSPA8]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 | STRING 812 |
| [[SOD1]] | +0.56 | +0.51 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_PEROXISOME; STRING 876 |
| [[CCT3]] | +0.55 | +0.63 / +0.43 | both halves | 3e-05 | STRING 475 |
| [[PIP4K2A]] | +0.54 | +0.54 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YY1AP1]] | -0.65 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[RCHY1]] | -0.63 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[ZC3H7A]] | -0.61 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[XPA]] | -0.60 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[PATL1]] | -0.60 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[TYW5]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[OSGEP]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[TMEM128]] | -0.59 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[CLK4]] | -0.58 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[SREK1]] | -0.58 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[SPEF2]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[PRPF39]] | -0.56 | -0.59 / -0.57 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PRDX1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GYPC]] | B | GYPC activity lowers PRDX1's level | lines that do not express GYPC (35) vs lines expressing it (15) | 1.44× higher at baseline in the lines without GYPC | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.657). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-20.9, -10.9); signed map (-25.6, -28.9). **Vector** length 97.3, 41.6% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial unfolded protein response (UPRmt)* (reactome, mean cos +0.52 to 5); *Chaperone Mediated Autophagy* (reactome, mean cos +0.54 to 4); *Aggrephagy* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.7 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.7 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.7 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +8.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.5 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | -0.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.0 | -7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -6.7 | +7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -5.9 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -5.8 | +11.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | -4.7 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.0 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -1.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.1 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.5 | -1.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | peroxiredoxin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:45,510,914-45,542,732 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NKEFA; previously PAGA |
| Gene groups (HGNC) | Peroxiredoxins |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, PEROXISOME, MTORC1_SIGNALING |
| Reactome | 16 pathways, smallest: Scavenging by Class B Receptors; NFE2L2 regulating anti-oxidant/detoxification enzymes; Deregulated CDK5 triggers multiple neurodegenerative pathways in Alzheimer's disease models |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06830](https://www.uniprot.org/uniprotkb/Q06830) (Peroxiredoxin-1):

> Thiol-specific peroxidase that catalyzes the reduction of hydrogen peroxide and organic hydroperoxides to water and alcohols, respectively. Plays a role in cell protection against oxidative stress by detoxifying peroxides and as sensor of hydrogen peroxide-mediated signaling events. Might participate in the signaling cascades of growth factors and tumor necrosis factor-alpha by regulating the intracellular concentrations of H(2)O(2). Reduces an intramolecular disulfide bond in GDPD5 that gates …

**Summary**, from NCBI Gene [5052](https://www.ncbi.nlm.nih.gov/gene/5052):

> This gene encodes a member of the peroxiredoxin family of antioxidant enzymes, which reduce hydrogen peroxide and alkyl hydroperoxides. The encoded protein may play an antioxidant protective role in cells, and may contribute to the antiviral activity of CD8(+) T-cells. This protein may have a proliferative effect and play a role in cancer development or progression. Four transcript variants encoding the same protein have been identified for this gene. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:9352](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9352) · Entrez [5052](https://www.ncbi.nlm.nih.gov/gene/5052) · UniProt [Q06830](https://www.uniprot.org/uniprotkb/Q06830) · Ensembl [ENSG00000117450](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117450)

## Data

Gene col 3909: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3909); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3909, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3909]; `tensor/DDL_lfc|DDL_z.npy` [3909]; `embed/gene_vectors.npy` [3909]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3909 or target_col == 3909). Every well: [[PRDX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRDX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
