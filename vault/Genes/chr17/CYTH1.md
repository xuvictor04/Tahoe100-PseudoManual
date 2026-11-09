---
symbol: "CYTH1"
type: "gene"
col: 2984
ensembl_id: "ENSG00000108669"
name: "cytohesin 1"
location: "17q25.3"
module: 160
arm: "+"
pooled_cpm: 134.63
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# CYTH1

*cytohesin 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.49× (z +7.7, q 5e-12, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.467× (z -14.9, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.648× (z -8.5, q 3e-15, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC8A]] (+0.66, fdr 7e-06), [[SERINC2]] (+0.65, fdr 1e-05), [[KANK2]] (+0.64, fdr 1e-05); moves opposite to [[DIS3L]] (-0.63, fdr 1e-05), [[ZNF280D]] (-0.62, fdr 2e-05), [[COQ9]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2984.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +7.7 | 5e-12 | 31/48 (SHP-77, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +6.9 | 2e-09 | 31/48 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.42×** | +6.6 | 7e-09 | 36/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +6.5 | 1e-08 | 31/48 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.37×** | +6.2 | 6e-08 | 34/47 (NCI-H460, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +4.4 | 0.001 | 26/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.5 | 0.035 | 16/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.1 | 0.16 | 20/48 (A-172, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2984.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.467×** | -14.9 | 0e+00 | 45/49 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.467×** | -14.3 | 6e-44 | 39/44 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.533×** | -10.7 | 3e-24 | 36/45 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.648×** | -8.5 | 3e-15 | 36/48 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.683×** | -7.5 | 1e-11 | 37/48 (A549, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.712×** | -6.4 | 1e-08 | 32/48 (COLO 205, A549, …) | two highest doses | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.813×** | -5.7 | 8e-07 | 25/48 (A549, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **0.762×** | -5.3 | 8e-06 | 29/48 (CFPAC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.778×** | -4.9 | 6e-05 | 30/48 (BT-474, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.842× | -4.8 | 1e-04 | 21/48 (LoVo, LS 180, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.792×** | -4.6 | 3e-04 | 28/48 (A549, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.852× | -4.4 | 4e-04 | 20/48 (CFPAC-1, SW 1271, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.853× | -4.4 | 4e-04 | 18/48 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.659×** | -4.0 | 0.003 | 25/47 (A549, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.811×** | -3.9 | 0.003 | 25/47 (MIA PaCa-2, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.826×** | -3.6 | 0.011 | 20/49 (HOP62, SW48, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.838× | -3.5 | 0.018 | 16/48 (BT-474, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.735×** | -2.9 | 0.092 | 15/49 (RPMI-7951, H4, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2984. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 230 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -20.6) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -13.1) |
| [[COLO 205 (line)]] | alt | 235 | 3 (2 ⚠) | 4 (4 ⚠) | [[Peretinoin (drug)]] 5 µM 2.63× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -23.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 218 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.420× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 194 | 4 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +22.2) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.36× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -13.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 105 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -14.9) ⚠ cell-cycle shift, explains ~87% of this change |
| [[NCI-H2347 (line)]] | alt | 139 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.489× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 236 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0973× (z -23.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 195 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.471× (z -8.9) |
| [[PANC-1 (line)]] | alt | 104 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.75× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.483× (z -11.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 71.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +12.8) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +9.3) | — |
| [[CHP-212 (line)]] | wt | 249 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[AZD-7648 (drug)]] 5 µM 0.0635× (z -11.1) |
| [[HOP62 (line)]] | alt | 91.8 | 4 | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.48× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 111 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.64× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -13.0) ⚠ cell-cycle shift, explains ~87% of this change |
| [[KATO III (line)]] | alt | 175 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 392 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -15.6) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.389× (z -11.9) |
| [[A-172 (line)]] | wt | 96.9 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.60× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -9.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 105 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -17.0) |
| [[AsPC-1 (line)]] | alt | 126 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.473× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 121 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.12× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.477× (z -9.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 143 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -11.1) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.437× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 92.4 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.53× (z +9.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.290× (z -12.4) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 103 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -10.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 132 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 127 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.354× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 99.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +20.3) ⚠ cell-cycle shift, explains ~87% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -15.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 94.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -10.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -16.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 137 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.483× (z -9.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -9.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -9.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 85.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.8) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 89.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.346× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 97.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -11.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 143 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.403× (z -9.9) |
| [[RKO (line)]] | wt | 69.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -10.5) ⚠ cell-cycle shift, explains ~87% of this change |
| [[RPMI-7951 (line)]] | alt | 86.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +13.3) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[SNU-1 (line)]] | wt | 69.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 214 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -10.5) ⚠ cell-cycle shift, explains ~87% of this change |
| [[SW48 (line)]] | wt | 68.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -9.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 140 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 88.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 95.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2984), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC8A]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SERINC2]] | +0.65 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[KANK2]] | +0.64 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[CORO2A]] | +0.63 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[FA2H]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[CAP1]] | +0.63 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[SLC8B1]] | +0.63 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[AGPAT2]] | +0.62 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[MAPKAPK2]] | +0.62 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[SLC66A2]] | +0.61 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[LMTK3]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[FRMD8]] | +0.61 | +0.55 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIS3L]] | -0.63 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[ZNF280D]] | -0.62 | -0.63 / -0.46 | both halves | 2e-05 |  |
| [[COQ9]] | -0.61 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[MCCC2]] | -0.57 | -0.54 / -0.43 | both halves | 4e-05 |  |
| [[MTPAP]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[RAD52]] | -0.57 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[TRUB1]] | -0.57 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[SRSF8]] | -0.56 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[PHC3]] | -0.56 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[AASDHPPT]] | -0.56 | -0.63 / -0.39 | both halves | 6e-05 |  |
| [[TRMT13]] | -0.56 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[TXNRD2]] | -0.55 | -0.58 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CYTH1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CRYBG2]] | B | CRYBG2 activity strengthens CYTH1's drug response | lines that do not express CRYBG2 (23) vs lines expressing it (26) | the lines without CRYBG2 respond 0.88× as strongly (z diff +0.90); strongest at Homoharringtonine 0.5 µM: 0.84x vs 0.55x (z diff +5.0) | 0.049 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1; target measured in part of the lines; artifact flags |
| [[CRYBG2]] | B | CRYBG2 activity raises CYTH1's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 1.37× lower at baseline in the lines without CRYBG2 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[FA2H]] | B | FA2H activity weakens CYTH1's drug response | lines that do not express FA2H (27) vs lines expressing it (22) | the lines without FA2H respond 1.00× as strongly (z diff +0.16); strongest at Panobinostat 5 µM: 1.69x vs 1.25x (z diff -3.2) | 0.050 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2; target measured in part of the lines; both ways; artifact flags |
| [[TTC9]] | B | TTC9 activity raises CYTH1's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 1.36× lower at baseline in the lines without TTC9 | 0.051 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[FAM83A]] | B | FAM83A activity weakens CYTH1's drug response | lines that do not express FAM83A (37) vs lines expressing it (12) | the lines without FAM83A respond 1.05× as strongly (z diff +0.14); strongest at Panobinostat 5 µM: 1.62x vs 1.10x (z diff -4.5) | 0.058 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9; target measured in part of the lines; artifact flags |
| [[S100P]] | B | S100P activity weakens CYTH1's drug response | lines that do not express S100P (34) vs lines expressing it (15) | the lines without S100P respond 1.04× as strongly (z diff +0.02); strongest at Panobinostat 5 µM: 1.67x vs 1.11x (z diff -4.2) | 0.069 | ⚠ within organs, on part of the lines; also absent: POF1B, ENSG00000287426, CEACAM6; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.749). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (7.8, 1.5); signed map (-13.2, 39.0). **Vector** length 116, 35.7% of its response variance represented; |z| ≥ 3 in 1,196 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.1 | +6.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.6 | +7.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.2 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.9 | +6.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.6 | +2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.1 | -8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.9 | -7.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -6.7 | -6.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.6 | -4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -4.6 | -5.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.2 | -4.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.9 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -4.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | cytohesin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:78,674,048-78,782,297 (-) |
| Ensembl biotype | protein_coding |
| Also known as | B2-1, D17S811E, cytohesin-1; previously PSCD1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Cytohesins |
| Reactome | 4 pathways, smallest: Intra-Golgi traffic; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15438](https://www.uniprot.org/uniprotkb/Q15438) (Cytohesin-1):

> Promotes guanine-nucleotide exchange on ARF1, ARF5 and ARF6. Promotes the activation of ARF factors through replacement of GDP with GTP. Plays an important role in membrane trafficking, during junctional remodeling and epithelial polarization, through regulation of ARF6 activity.

**Summary**, from NCBI Gene [9267](https://www.ncbi.nlm.nih.gov/gene/9267):

> The protein encoded by this gene is a member of the PSCD family. Members of this family have identical structural organization that consists of an N-terminal coiled-coil motif, a central Sec7 domain, and a C-terminal pleckstrin homology (PH) domain. The coiled-coil motif is involved in homodimerization, the Sec7 domain contains guanine-nucleotide exchange protein activity, and the PH domain interacts with phospholipids and is responsible for association of PSCDs with membranes. Members of this …

**Accessions** — [HGNC:9501](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9501) · Entrez [9267](https://www.ncbi.nlm.nih.gov/gene/9267) · UniProt [Q15438](https://www.uniprot.org/uniprotkb/Q15438) · Ensembl [ENSG00000108669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108669)

## Data

Gene col 2984: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2984); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2984, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2984]; `tensor/DDL_lfc|DDL_z.npy` [2984]; `embed/gene_vectors.npy` [2984]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2984 or target_col == 2984). Every well: [[CYTH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYTH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
