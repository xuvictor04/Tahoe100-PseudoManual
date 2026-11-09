---
symbol: "RREB1"
type: "gene"
col: 4567
ensembl_id: "ENSG00000124782"
name: "ras responsive element binding protein 1"
location: "6p24.3"
module: 204
arm: "+"
pooled_cpm: 185.78
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/204"]
generated_by: "tahoemap"
---

# RREB1

*ras responsive element binding protein 1* — 6p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 1.79× (z +5.2, q 1e-04, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.263× (z -22.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPB41L4B]] (+0.61, fdr 1e-05), [[HERC3]] (+0.58, fdr 1e-05), [[LRP5L]] (+0.57, fdr 4e-05); moves opposite to [[PBRM1]] (-0.52, fdr 2e-05), [[PIGL]] (-0.51, fdr 2e-05), [[ZSCAN5A]] (-0.50, fdr 4e-05).
> It is in [[Module 204]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KRT6A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4567.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +5.2 | 1e-04 | 38/48 (C32, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +4.7 | 7e-04 | 35/49 (A-427, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.096 | 25/48 (LS 180, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.100 | 24/49 (COLO 205, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.14× | +3.1 | 0.19 | 6/48 (Panc 03.27, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4567.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.263×** | -22.8 | 0e+00 | 48/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.276×** | -22.0 | 0e+00 | 48/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.347×** | -17.4 | 0e+00 | 42/44 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.374×** | -16.8 | 0e+00 | 49/49 (CHP-212, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.386×** | -16.2 | 0e+00 | 48/48 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.365×** | -15.9 | 0e+00 | 43/45 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.530×** | -15.3 | 0e+00 | 40/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.652×** | -7.3 | 2e-11 | 31/48 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.662×** | -6.8 | 8e-10 | 34/48 (NCI-H1573, C32, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.671×** | -6.6 | 3e-09 | 40/47 (MIA PaCa-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.744×** | -5.0 | 2e-05 | 37/48 (AsPC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.755×** | -4.8 | 7e-05 | 31/49 (NCI-H2347, SNU-423, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.839× | -4.2 | 9e-04 | 21/48 (RPMI-7951, HCT15, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.775×** | -4.2 | 0.001 | 27/48 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.788×** | -3.9 | 0.003 | 27/50 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.809×** | -3.6 | 0.010 | 26/48 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.837× | -3.0 | 0.075 | 23/48 (C32, HT-29, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.884× | -3.0 | 0.087 | 7/48 (SNU-423, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4567. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 235 | 0 | 13 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -20.5) |
| [[C32 (line)]] | wt | 165 | 1 | 10 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 4.59× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -32.2) |
| [[LoVo (line)]] | wt | 380 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -35.2) |
| [[NCI-H2347 (line)]] | alt | 234 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.231× (z -17.8) |
| [[A498 (line)]] | wt | 168 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -17.6) |
| [[AsPC-1 (line)]] | alt | 232 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.143× (z -22.0) |
| [[CFPAC-1 (line)]] | alt | 268 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.374× (z -14.6) |
| [[HOP62 (line)]] | alt | 143 | 1 (1 ⚠) | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +8.5) ⚠ cell-cycle shift, explains ~72% of this change | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -16.3) |
| [[LOX-IMVI (line)]] | wt | 154 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -17.9) |
| [[LS 180 (line)]] | wt | 426 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -19.1) |
| [[A-172 (line)]] | wt | 169 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.179× (z -17.2) |
| [[A-427 (line)]] | wt | 127 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.84× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.350× (z -12.6) |
| [[Hs 766T (line)]] | wt | 192 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -17.0) |
| [[NCI-H1792 (line)]] | alt | 125 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -28.9) |
| [[PANC-1 (line)]] | alt | 133 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.371× (z -15.3) |
| [[SW48 (line)]] | wt | 320 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.106× (z -15.4) |
| [[SW480 (line)]] | alt | 189 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -23.1) |
| [[A549 (line)]] | wt | 113 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -16.4) |
| [[hTERT-HPNE (line)]] | wt | 152 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -19.0) |
| [[KATO III (line)]] | alt | 196 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.262× (z -17.4) |
| [[NCI-H1573 (line)]] | alt | 192 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -32.7) |
| [[NCI-H460 (line)]] | wt | 163 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.203× (z -21.2) |
| [[Panc 03.27 (line)]] | alt | 215 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.270× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 159 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.247× (z -13.0) |
| [[COLO 205 (line)]] | alt | 206 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -21.4) |
| [[H4 (line)]] | wt | 125 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.288× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 182 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -15.7) |
| [[HS-578T (line)]] | alt | 115 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -11.4) |
| [[HT-29 (line)]] | alt | 193 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -19.0) |
| [[J82 (line)]] | alt | 147 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 152 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -14.8) |
| [[SHP-77 (line)]] | alt | 154 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -13.6) |
| [[SNU-423 (line)]] | alt | 181 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -17.2) |
| [[SW 900 (line)]] | alt | 112 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -13.2) |
| [[SW1417 (line)]] | alt | 242 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -17.8) |
| [[AN3 CA (line)]] | alt | 254 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.254× (z -9.6) |
| [[BT-474 (line)]] | alt | 203 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -17.0) |
| [[CHP-212 (line)]] | wt | 149 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0789× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.213× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 205 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -13.5) |
| [[C-33 A (line)]] | alt | 146 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -11.6) |
| [[RKO (line)]] | wt | 129 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.347× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 98.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -11.8) |
| [[HCT15 (line)]] | alt | 240 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -9.6) |
| [[NCI-H661 (line)]] | alt | 249 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.232× (z -8.5) |
| [[SNU-1 (line)]] | wt | 172 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.242× (z -13.7) |
| [[SW 1271 (line)]] | alt | 139 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0890× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.139× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 112 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -12.0) |
| [[NCI-H2122 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4567), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L4B]] | +0.61 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[HERC3]] | +0.58 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[LRP5L]] | +0.57 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[TRIM7]] | +0.54 | +0.33 / +0.58 | both halves | 1e-04 |  |
| [[PPARGC1B]] | +0.53 | +0.46 / +0.37 | both halves | 7e-05 |  |
| [[L3MBTL3]] | +0.52 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[UGP2]] | +0.51 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[RAB20]] | +0.51 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[USP3]] | +0.51 | +0.66 / +0.41 | both halves | 4e-05 |  |
| [[MMP15]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[MANBA]] | +0.51 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[GATA4]] | +0.50 | +0.45 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBRM1]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PIGL]] | -0.51 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[ZSCAN5A]] | -0.50 | -0.56 / -0.41 | both halves | 4e-05 | same gene group |
| [[ZNF674]] | -0.48 | -0.56 / -0.42 | both halves | 4e-05 | same gene group |
| [[IQCK]] | -0.48 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[NCOA5]] | -0.48 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[ZNF140]] | -0.48 | -0.58 / -0.43 | both halves | 3e-05 | same gene group |
| [[ENDOV]] | -0.46 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[APCDD1L-DT]] | -0.46 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[TAF2]] | -0.45 | -0.62 / -0.35 | both halves | 1e-04 |  |
| [[ENSA]] | -0.45 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[SLC36A4]] | -0.45 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT6A]] | B | KRT6A activity raises RREB1's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 1.59× lower at baseline in the lines without KRT6A | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 204]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.585). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.54; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.3, -5.3); signed map (-21.4, 18.4). **Vector** length 101, 36.3% of its response variance represented; |z| ≥ 3 in 1,201 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +12.1 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | +2.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +0.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +5.0 | -16.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.2 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | -0.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.0 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.3 | -15.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -7.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.5 | -6.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.0 | +0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -4.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.1 | -1.0 |
|  | [[9-ING-41 (drug)]] 0.05 µM |  | -1.9 | -0.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | ras responsive element binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.3 — chr6:7,107,597-7,251,980 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HNT |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Hallmark sets | ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92766](https://www.uniprot.org/uniprotkb/Q92766) (Ras-responsive element-binding protein 1):

> Transcription factor that binds specifically to the RAS-responsive elements (RRE) of gene promoters. Represses the angiotensinogen gene. Negatively regulates the transcriptional activity of AR. Potentiates the transcriptional activity of NEUROD1. Promotes brown adipocyte differentiation (By similarity). May be involved in Ras/Raf-mediated cell differentiation by enhancing calcitonin expression.

**Summary**, from NCBI Gene [6239](https://www.ncbi.nlm.nih.gov/gene/6239):

> The protein encoded by this gene is a zinc finger transcription factor that binds to RAS-responsive elements (RREs) of gene promoters. It has been shown that the calcitonin gene promoter contains an RRE and that the encoded protein binds there and increases expression of calcitonin, which may be involved in Ras/Raf-mediated cell differentiation. Multiple transcript variants encoding several different isoforms have been found for this gene. [provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:10449](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10449) · Entrez [6239](https://www.ncbi.nlm.nih.gov/gene/6239) · UniProt [Q92766](https://www.uniprot.org/uniprotkb/Q92766) · Ensembl [ENSG00000124782](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124782)

## Data

Gene col 4567: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4567); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4567, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4567]; `tensor/DDL_lfc|DDL_z.npy` [4567]; `embed/gene_vectors.npy` [4567]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4567 or target_col == 4567). Every well: [[RREB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RREB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
