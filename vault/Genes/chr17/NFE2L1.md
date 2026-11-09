---
symbol: "NFE2L1"
type: "gene"
col: 1353
ensembl_id: "ENSG00000082641"
name: "NFE2 like bZIP transcription factor 1"
location: "17q21.32"
module: 133
arm: "+"
pooled_cpm: 164.55
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# NFE2L1

*NFE2 like bZIP transcription factor 1* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.74× (z +13.4, q 6e-38, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.301× (z -29.0, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCK2]] (+0.63, fdr 1e-05), [[NBR2]] (+0.63, fdr 1e-05), [[DNASE2]] (+0.63, fdr 7e-06); moves opposite to [[MPHOSPH6]] (-0.49, fdr 6e-05), [[IER2]] (-0.49, fdr 3e-05), [[EIF2B3]] (-0.46, fdr 3e-05).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1353.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +13.4 | 6e-38 | 43/49 (MIA PaCa-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +7.9 | 8e-13 | 44/50 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.0 | 4e-07 | 30/48 (NCI-H2347, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **1.27×** | +5.9 | 7e-07 | 30/48 (COLO 205, SNU-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.39×** | +5.6 | 2e-06 | 38/48 (hTERT-HPNE, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.37×** | +5.4 | 6e-06 | 32/48 (LoVo, hTERT-HPNE, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.3 | 8e-06 | 37/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +4.8 | 1e-04 | 33/48 (RPMI-7951, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.26×** | +4.0 | 0.005 | 25/49 (HEC-1-A, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.022 | 25/48 (hTERT-HPNE, A-172, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.022 | 25/48 (NCI-H2347, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.042 | 24/48 (Hs 766T, hTERT-HPNE, …) | top dose only |  |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.067 | 24/48 (RPMI-7951, H4, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.1 | 0.067 | 21/44 (hTERT-HPNE, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1353.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.301×** | -29.0 | 0e+00 | 48/48 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.314×** | -19.0 | 0e+00 | 48/48 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.401×** | -15.6 | 0e+00 | 48/48 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.568×** | -9.7 | 6e-20 | 45/48 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.670×** | -6.8 | 1e-09 | 46/49 (SW1417, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.499×** | -6.2 | 5e-08 | 40/49 (A498, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.699×** | -6.1 | 8e-08 | 46/49 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.732×** | -5.3 | 7e-06 | 32/48 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.737×** | -5.2 | 1e-05 | 30/48 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.602×** | -4.5 | 3e-04 | 34/48 (SK-MEL-2, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.779×** | -4.3 | 0.001 | 30/48 (NCI-H23, SW 900, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.772×** | -4.2 | 0.001 | 27/49 (HepG2/C3A, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.781×** | -4.2 | 0.001 | 26/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.783×** | -4.2 | 0.001 | 26/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | **0.802×** | -3.8 | 0.006 | 27/48 (HepG2/C3A, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1353. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 137 | 3 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -19.2) |
| [[HOP62 (line)]] | alt | 212 | 4 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +14.1) | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -21.6) |
| [[MIA PaCa-2 (line)]] | alt | 125 | 5 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +25.0) | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -18.6) |
| [[SNU-1 (line)]] | wt | 138 | 2 | 5 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.19× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -13.6) |
| [[A-172 (line)]] | wt | 372 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -27.7) |
| [[KATO III (line)]] | alt | 281 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -21.5) |
| [[NCI-H460 (line)]] | wt | 163 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -27.0) |
| [[A549 (line)]] | wt | 131 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -23.1) |
| [[C32 (line)]] | wt | 202 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -22.4) |
| [[NCI-H1573 (line)]] | alt | 140 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -28.0) |
| [[NCI-H23 (line)]] | alt | 140 | 2 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +15.3) | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -25.2) |
| [[PANC-1 (line)]] | alt | 197 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -22.4) |
| [[SK-MEL-2 (line)]] | alt | 251 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -29.5) |
| [[A-427 (line)]] | wt | 161 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -27.1) |
| [[CFPAC-1 (line)]] | alt | 222 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -21.6) |
| [[COLO 205 (line)]] | alt | 126 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +13.3) | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -11.9) |
| [[H4 (line)]] | wt | 383 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -19.9) |
| [[HCT15 (line)]] | alt | 148 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -18.2) |
| [[HepG2_C3A (line)]] | wt | 251 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -23.5) |
| [[HS-578T (line)]] | alt | 264 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -16.0) |
| [[LoVo (line)]] | wt | 89.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -16.1) |
| [[LOX-IMVI (line)]] | wt | 117 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -22.2) |
| [[NCI-H1792 (line)]] | alt | 170 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +13.0) | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -24.6) |
| [[NCI-H2030 (line)]] | alt | 113 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -20.1) |
| [[NCI-H2347 (line)]] | alt | 112 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +16.5) | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -16.5) |
| [[SW 900 (line)]] | alt | 168 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -11.1) |
| [[SW480 (line)]] | alt | 107 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -17.1) |
| [[A498 (line)]] | wt | 253 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -14.8) |
| [[BT-474 (line)]] | alt | 111 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -18.1) |
| [[C-33 A (line)]] | alt | 146 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -17.0) |
| [[Hs 766T (line)]] | wt | 104 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -15.1) |
| [[HT-29 (line)]] | alt | 187 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -23.3) |
| [[Panc 03.27 (line)]] | alt | 115 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +13.4) | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -15.0) |
| [[RKO (line)]] | wt | 103 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +13.4) | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 156 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -21.6) |
| [[SNU-423 (line)]] | alt | 172 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -27.7) |
| [[SW48 (line)]] | wt | 107 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -14.0) |
| [[AsPC-1 (line)]] | alt | 68.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.4) | [[Harringtonine (drug)]] 5 µM 0.396× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 264 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -14.2) |
| [[J82 (line)]] | alt | 162 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -16.1) |
| [[NCI-H661 (line)]] | alt | 165 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -14.4) |
| [[SHP-77 (line)]] | alt | 106 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -10.6) |
| [[SW 1088 (line)]] | alt | 202 | 0 | 2 | — | [[Dexamethasone (drug)]] 5 µM 0.111× (z -10.6) |
| [[SW1417 (line)]] | alt | 122 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -10.7) |
| [[CHP-212 (line)]] | wt | 272 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -11.2) |
| [[SW 1271 (line)]] | alt | 148 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -8.6) |
| [[AN3 CA (line)]] | alt | 128 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 75.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1353), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCK2]] | +0.63 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[NBR2]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[DNASE2]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[GHITM]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SLC6A9]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[HYOU1]] | +0.60 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[NRSN2-AS1]] | +0.59 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[MTHFD2]] | +0.57 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[SARS1]] | +0.57 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[LMAN2]] | +0.57 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[GARS1-DT]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[AARS1]] | +0.56 | +0.61 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPHOSPH6]] | -0.49 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[IER2]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[EIF2B3]] | -0.46 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[CD22]] | -0.45 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[IRAK2]] | -0.45 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[COA7]] | -0.44 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[RRP15]] | -0.44 | -0.42 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NFE2L1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.588). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.4, 45.3); signed map (-14.8, 21.9). **Vector** length 139, 48.7% of its response variance represented; |z| ≥ 3 in 1,276 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.6 | +13.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +5.3 |
|  | [[Artesunate (drug)]] 5 µM |  | +6.9 | +5.9 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +6.0 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +6.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.0 | +5.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.7 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +1.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +4.4 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -10.1 | -19.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.9 | -15.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.2 | -9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.6 | -29.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.4 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -4.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.6 | -2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -4.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | NFE2 like bZIP transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,048,329-48,061,545 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NRF1, LCR-F1, FLJ00380, NRF-1; previously TCF11 |
| Gene groups (HGNC) | NFE2 family bZIP transcription factors |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14494](https://www.uniprot.org/uniprotkb/Q14494) (Endoplasmic reticulum membrane sensor NFE2L1):

> [Endoplasmic reticulum membrane sensor NFE2L1]: Endoplasmic reticulum membrane sensor that translocates into the nucleus in response to various stresses to act as a transcription factor. Constitutes a precursor of the transcription factor NRF1 (By similarity). Able to detect various cellular stresses, such as cholesterol excess, oxidative stress or proteasome inhibition. In response to stress, it is released from the endoplasmic reticulum membrane following cleavage by the protease DDI2 and …

**Summary**, from NCBI Gene [4779](https://www.ncbi.nlm.nih.gov/gene/4779):

> This gene encodes a protein that is involved in globin gene expression in erythrocytes. Confusion has occurred in bibliographic databases due to the shared symbol of NRF1 for this gene, NFE2L1, and for "nuclear respiratory factor 1" which has an official symbol of NRF1. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7781](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7781) · Entrez [4779](https://www.ncbi.nlm.nih.gov/gene/4779) · UniProt [Q14494](https://www.uniprot.org/uniprotkb/Q14494) · Ensembl [ENSG00000082641](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082641)

## Data

Gene col 1353: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1353); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1353, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1353]; `tensor/DDL_lfc|DDL_z.npy` [1353]; `embed/gene_vectors.npy` [1353]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1353 or target_col == 1353). Every well: [[NFE2L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFE2L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
