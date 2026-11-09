---
symbol: "ATRN"
type: "gene"
col: 1544
ensembl_id: "ENSG00000088812"
name: "attractin"
location: "20p13"
module: 134
arm: "+"
pooled_cpm: 143.26
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# ATRN

*attractin* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.04× (z +18.0, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.512× (z -23.8, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CABIN1]] (+0.72, fdr 1e-05), [[ARL6]] (+0.72, fdr 7e-06), [[GLG1]] (+0.71, fdr 1e-05); moves opposite to [[SLC9A8]] (-0.69, fdr 1e-05), [[LPXN]] (-0.69, fdr 2e-05), [[PPP3CB-AS1]] (-0.69, fdr 2e-04).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[JAM3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1544.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.04×** | +18.0 | 0e+00 | 44/46 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.89×** | +16.1 | 0e+00 | 44/46 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +12.8 | 3e-35 | 44/46 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.88×** | +8.3 | 1e-14 | 35/47 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.83×** | +8.0 | 1e-13 | 43/47 (PANC-1, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +8.0 | 1e-13 | 38/46 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +6.7 | 2e-09 | 30/46 (SW480, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +5.2 | 1e-05 | 32/46 (CFPAC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.16× | +3.7 | 0.014 | 18/45 (SW480, HOP62, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.13× | +3.1 | 0.10 | 5/46 (NCI-H1573, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1544.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.512×** | -23.8 | 0e+00 | 41/46 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.413×** | -21.4 | 0e+00 | 44/46 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.509×** | -16.3 | 0e+00 | 38/43 (HEC-1-A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.574×** | -14.0 | 4e-42 | 38/47 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.583×** | -13.6 | 6e-40 | 43/46 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.671×** | -9.7 | 4e-20 | 31/45 (NCI-H460, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.665×** | -9.5 | 2e-19 | 39/44 (J82, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.745×** | -7.4 | 1e-11 | 35/46 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.821×** | -7.0 | 2e-10 | 23/47 (J82, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.831×** | -4.7 | 2e-04 | 24/46 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.830×** | -4.5 | 4e-04 | 22/45 (HepG2/C3A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -4.4 | 6e-04 | 22/48 (C32, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.847× | -4.1 | 0.001 | 21/46 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.955× | -3.8 | 0.006 | 0/48 | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.900× | -3.7 | 0.008 | 13/46 (HOP62, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.855× | -3.6 | 0.011 | 18/45 (NCI-H460, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.877× | -3.3 | 0.034 | 12/45 (SNU-423, SW480, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.879× | -3.0 | 0.083 | 6/46 (A-172, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1544. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 194 | 2 | 12 (7 ⚠) | [[Belinostat (drug)]] 5 µM 1.77× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -27.6) |
| [[PANC-1 (line)]] | alt | 163 | 4 | 8 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.06× (z +13.4) | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -32.9) |
| [[C32 (line)]] | wt | 242 | 1 | 10 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 3.45× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -22.8) |
| [[HS-578T (line)]] | alt | 208 | 2 | 7 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.01× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -23.5) |
| [[NCI-H1573 (line)]] | alt | 71.6 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -18.4) |
| [[HOP62 (line)]] | alt | 201 | 2 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -25.6) |
| [[J82 (line)]] | alt | 137 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -24.2) |
| [[LOX-IMVI (line)]] | wt | 163 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -28.0) |
| [[MIA PaCa-2 (line)]] | alt | 154 | 4 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.77× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.553× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 155 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -18.4) |
| [[RPMI-7951 (line)]] | alt | 236 | 2 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.17× (z +10.1) | [[Harringtonine (drug)]] 5 µM 0.292× (z -15.5) |
| [[A-172 (line)]] | wt | 161 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.158× (z -23.7) |
| [[A549 (line)]] | wt | 186 | 2 | 4 | [[Panobinostat (drug)]] 5 µM 2.17× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -20.2) |
| [[H4 (line)]] | wt | 117 | 3 | 3 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.14× (z +11.2) | [[Harringtonine (drug)]] 5 µM 0.308× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 123 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -23.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 214 | 1 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.09× (z +10.4) | [[Harringtonine (drug)]] 5 µM 0.477× (z -10.0) |
| [[SW480 (line)]] | alt | 164 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.01× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.468× (z -14.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 138 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -32.4) |
| [[AsPC-1 (line)]] | alt | 50.7 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 4.52× (z +14.0) | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 87.1 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 2.43× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.613× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 322 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.15× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 143 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.07× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.442× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.594× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 89.7 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 2.43× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -11.0) |
| [[A498 (line)]] | wt | 60.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -17.3) |
| [[C-33 A (line)]] | alt | 387 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.7) |
| [[LS 180 (line)]] | wt | 104 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.12× (z +14.3) | — |
| [[NCI-H2030 (line)]] | alt | 77.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -14.1) |
| [[SHP-77 (line)]] | alt | 213 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.19× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.484× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 249 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.48× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.450× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.466× (z -8.6) |
| [[SNU-423 (line)]] | alt | 187 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.89× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -26.3) |
| [[SW 900 (line)]] | alt | 129 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 2.03× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -13.2) |
| [[BT-474 (line)]] | alt | 134 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.58× (z +10.2) | — |
| [[hTERT-HPNE (line)]] | wt | 134 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -14.9) |
| [[LoVo (line)]] | wt | 95.7 | 2 | 1 | [[Belinostat (drug)]] 5 µM 2.09× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.592× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 211 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -13.6) |
| [[HCT15 (line)]] | alt | 172 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.21× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -11.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 138 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.46× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -10.1) |
| [[KATO III (line)]] | alt | 95.2 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.25× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.616× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 98.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.492× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.498× (z -9.1) |
| [[SW 1271 (line)]] | alt | 240 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.349× (z -10.1) |
| [[AN3 CA (line)]] | alt | 225 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.298× (z -9.6) |
| [[CHP-212 (line)]] | wt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -8.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 68.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.60× (z +10.4) | — |
| [[SW1417 (line)]] | alt | 82.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.00× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 27.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1544), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CABIN1]] | +0.72 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[ARL6]] | +0.72 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[GLG1]] | +0.71 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[WASF3]] | +0.70 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[SNAPC3]] | +0.69 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[STIMATE]] | +0.69 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[UBE2O]] | +0.69 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.68 | +0.68 / +0.39 | both halves | 5e-05 |  |
| [[RHOT1]] | +0.68 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[RNF216]] | +0.67 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[FAM234B]] | +0.67 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[SDHB]] | +0.67 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A8]] | -0.69 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[LPXN]] | -0.69 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[PPP3CB-AS1]] | -0.69 | -0.60 / -0.32 | both halves | 2e-04 |  |
| [[PATL2]] | -0.67 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[LACC1]] | -0.66 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[RIPK2-DT]] | -0.65 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[PPP1R12A-AS2]] | -0.65 | -0.62 / -0.23 | both halves | 5e-04 |  |
| [[PLA2G4C]] | -0.65 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[GABPB2]] | -0.65 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[RFX3-DT]] | -0.65 | -0.60 / -0.28 | both halves | 3e-04 |  |
| [[PCNX4-DT]] | -0.64 | -0.65 / -0.20 | both halves | 7e-04 |  |
| [[MMADHC-DT]] | -0.64 | -0.61 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAM3]] | B | JAM3 activity raises ATRN's level | lines that do not express JAM3 (23) vs lines expressing it (27) | 1.76× lower at baseline in the lines without JAM3 | 0.025 | ⚠ within organs, on part of the lines; also absent: NPTX1, NOVA2, GDNF-AS1 |
| [[CTXN1]] | B | CTXN1 activity raises ATRN's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without CTXN1 | 0.031 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[ZNF888]] | B | ZNF888 activity raises ATRN's level | lines that do not express ZNF888 (6) vs lines expressing it (44) | 1.79× lower at baseline in the lines without ZNF888 | 0.050 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF816, ZNF468, ZNF701 |
| [[SLC2A3]] | B | SLC2A3 activity raises ATRN's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 1.70× lower at baseline in the lines without SLC2A3 | 0.062 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[HDAC6]] | B | HDAC6 activity lowers ATRN's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.756). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.0, -13.8); signed map (-37.1, -3.8). **Vector** length 125, 41.3% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +8.5 | +16.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.3 | +12.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.7 | +18.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.3 | +8.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.1 | +5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.8 | +6.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.8 | +8.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +1.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.0 | +1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -13.7 | -23.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.6 | -13.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -10.1 | -21.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -7.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -3.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.5 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | attractin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:3,471,018-3,651,118 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DPPT-L, MGCA |
| Gene groups (HGNC) | C-type lectin domain containing |
| Hallmark sets | UV_RESPONSE_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [O75882](https://www.uniprot.org/uniprotkb/O75882) (Attractin):

> Substrate-recognition component of a membrane-tethered ubiquitin ligase complex that acts as a negative regulator of melanocortin receptor signaling by mediating ubiquitination of MC1R and MC4R (By similarity). Within the complex, MEGF8 both recognizes MC1R and MC4R and recruits the cytoplasmic E3 ubiquitin ligase MGRN1 (By similarity). Involved in the initial immune cell clustering during inflammatory response and may regulate chemotactic activity of chemokines. Has a critical role in normal …

**Summary**, from NCBI Gene [8455](https://www.ncbi.nlm.nih.gov/gene/8455):

> This gene encodes both membrane-bound and secreted protein isoforms. A membrane-bound isoform exhibits sequence similarity with the mouse mahogany protein, a receptor involved in controlling obesity. A secreted isoform is involved in the initial immune cell clustering during inflammatory responses that may regulate the chemotactic activity of chemokines. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:885](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:885) · Entrez [8455](https://www.ncbi.nlm.nih.gov/gene/8455) · UniProt [O75882](https://www.uniprot.org/uniprotkb/O75882) · Ensembl [ENSG00000088812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088812)

## Data

Gene col 1544: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1544); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1544, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1544]; `tensor/DDL_lfc|DDL_z.npy` [1544]; `embed/gene_vectors.npy` [1544]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1544 or target_col == 1544). Every well: [[ATRN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATRN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
