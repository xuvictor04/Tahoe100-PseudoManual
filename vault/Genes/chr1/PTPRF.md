---
symbol: "PTPRF"
type: "gene"
col: 6668
ensembl_id: "ENSG00000142949"
name: "protein tyrosine phosphatase receptor type F"
location: "1p34.2"
module: 180
arm: "+"
pooled_cpm: 220.54
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 34
n_dd_up_clean: 3
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# PTPRF

*protein tyrosine phosphatase receptor type F* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Peretinoin (drug)]] 5 µM: 1.32× (z +4.1, q 0.022, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.243× (z -30.5, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPT]] (+0.63, fdr 3e-05), [[SLC29A4]] (+0.63, fdr 1e-05), [[PTPRS]] (+0.60, fdr 6e-05); moves opposite to [[ANGEL2]] (-0.60, fdr 8e-05), [[RNF146]] (-0.55, fdr 4e-04), [[EFCAB2]] (-0.53, fdr 1e-03, ⚠ not reproduced), [[DECR1]] (-0.52, fdr 5e-04).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6668.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Peretinoin (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.022 | 34/47 (NCI-H460, C32, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.30×** | +4.0 | 0.022 | 28/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.29×** | +3.8 | 0.025 | 24/49 (NCI-H1573, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.6 | 0.042 | 19/49 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.4 | 0.081 | 0/50 | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.51×** | +3.3 | 0.081 | 28/46 (NCI-H460, C32, …) | rises with dose | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.52×** | +3.3 | 0.081 | 33/48 (NCI-H23, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.23× | +3.1 | 0.13 | 25/47 (NCI-H460, C32, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | 1.48× | +3.1 | 0.13 | 29/48 (NCI-H460, SK-MEL-2, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6668.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.243×** | -30.5 | 0e+00 | 44/48 (RKO, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.304×** | -17.4 | 0e+00 | 45/48 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.465×** | -16.5 | 0e+00 | 44/49 (RPMI-7951, COLO 205, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.340×** | -15.3 | 0e+00 | 43/48 (SW48, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.507×** | -10.3 | 5e-23 | 44/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.547×** | -9.2 | 4e-18 | 43/48 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.553×** | -8.7 | 3e-16 | 43/48 (C32, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.595×** | -7.9 | 2e-13 | 42/48 (LoVo, HepG2/C3A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.596×** | -7.9 | 2e-13 | 38/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.621×** | -7.0 | 2e-10 | 34/47 (COLO 205, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.643×** | -6.7 | 9e-10 | 38/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.738×** | -6.5 | 3e-09 | 36/48 (J82, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.756×** | -6.0 | 7e-08 | 34/48 (SNU-1, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.694×** | -5.6 | 1e-06 | 33/48 (LS 180, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.693×** | -5.4 | 3e-06 | 32/50 (COLO 205, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.733×** | -4.7 | 7e-05 | 34/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.554×** | -4.7 | 8e-05 | 38/48 (RKO, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.573×** | -4.4 | 2e-04 | 34/49 (RKO, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.757×** | -4.1 | 0.001 | 35/49 (HepG2/C3A, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.784×** | -3.7 | 0.005 | 30/47 (LOX-IMVI, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.804×** | -3.3 | 0.019 | 25/48 (C32, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6668. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 352 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -32.5) |
| [[NCI-H23 (line)]] | alt | 347 | 0 | 11 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.126× (z -24.7) |
| [[C32 (line)]] | wt | 245 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -27.5) |
| [[NCI-H460 (line)]] | wt | 145 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -28.0) |
| [[RKO (line)]] | wt | 189 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -36.8) |
| [[HS-578T (line)]] | alt | 265 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -19.3) |
| [[LoVo (line)]] | wt | 160 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -19.7) |
| [[LS 180 (line)]] | wt | 207 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -24.4) |
| [[SNU-1 (line)]] | wt | 184 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -26.9) |
| [[A549 (line)]] | wt | 273 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -16.1) |
| [[AsPC-1 (line)]] | alt | 350 | 1 | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.286× (z -14.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -9.4) |
| [[COLO 205 (line)]] | alt | 292 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -21.7) |
| [[HepG2_C3A (line)]] | wt | 368 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.312× (z -12.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -11.1) |
| [[HOP62 (line)]] | alt | 266 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -27.9) |
| [[Panc 03.27 (line)]] | alt | 227 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -23.8) |
| [[BT-474 (line)]] | alt | 267 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -26.0) |
| [[C-33 A (line)]] | alt | 205 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 269 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -30.9) |
| [[HT-29 (line)]] | alt | 359 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -21.4) |
| [[MIA PaCa-2 (line)]] | alt | 486 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +8.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -16.1) |
| [[NCI-H1573 (line)]] | alt | 104 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 5.19× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -13.3) |
| [[NCI-H1792 (line)]] | alt | 225 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 209 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -25.5) |
| [[PANC-1 (line)]] | alt | 177 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -25.1) |
| [[RPMI-7951 (line)]] | alt | 301 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -27.8) |
| [[SK-MEL-2 (line)]] | alt | 170 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -14.1) |
| [[SW48 (line)]] | wt | 268 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0932× (z -35.3) |
| [[SW480 (line)]] | alt | 96.6 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -14.7) |
| [[AN3 CA (line)]] | alt | 236 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -13.9) |
| [[CFPAC-1 (line)]] | alt | 257 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -25.2) |
| [[Hs 766T (line)]] | wt | 218 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -27.0) |
| [[hTERT-HPNE (line)]] | wt | 128 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -21.6) |
| [[LOX-IMVI (line)]] | wt | 256 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -26.1) |
| [[SNU-423 (line)]] | alt | 251 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -20.7) |
| [[SW 900 (line)]] | alt | 98.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -18.1) |
| [[A-427 (line)]] | wt | 148 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -16.8) |
| [[HCT15 (line)]] | alt | 217 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -23.0) |
| [[KATO III (line)]] | alt | 191 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -16.4) |
| [[NCI-H2347 (line)]] | alt | 270 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -20.4) |
| [[A-172 (line)]] | wt | 217 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.326× (z -11.7) |
| [[CHP-212 (line)]] | wt | 71.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -10.2) |
| [[H4 (line)]] | wt | 121 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -21.0) |
| [[SW1417 (line)]] | alt | 179 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -11.0) |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -8.9) |
| [[SW 1088 (line)]] | alt | 208 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -13.7) |
| [[SW 1271 (line)]] | alt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -12.4) |
| [[A498 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 80.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6668), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPT]] | +0.63 | +0.60 / +0.45 | both halves | 3e-05 | pathway: Neuronal System |
| [[SLC29A4]] | +0.63 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[PTPRS]] | +0.60 | +0.55 / +0.38 | both halves | 6e-05 | same gene group; pathway: Neuronal System |
| [[GNAI2]] | +0.60 | +0.63 / +0.32 | both halves | 2e-04 | pathway: Neuronal System |
| [[SMS]] | +0.60 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[GOLGA6L9]] | +0.60 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[QSOX1]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ARHGEF10]] | +0.59 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[MAST1]] | +0.59 | +0.42 / +0.37 | both halves | 8e-05 |  |
| [[RAB11FIP5]] | +0.59 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[PPP2R5B]] | +0.58 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[TMEM184B]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANGEL2]] | -0.60 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[RNF146]] | -0.55 | -0.55 / -0.24 | both halves | 4e-04 |  |
| [[EFCAB2]] | -0.53 | -0.49 / -0.18 | ⚠ not reproduced | 1e-03 |  |
| [[DECR1]] | -0.52 | -0.49 / -0.24 | both halves | 5e-04 |  |
| [[SOCS6]] | -0.52 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[PSME3IP1]] | -0.51 | -0.45 / -0.24 | both halves | 4e-04 |  |
| [[CLHC1]] | -0.51 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[FAIM]] | -0.51 | -0.44 / -0.22 | both halves | 6e-04 |  |
| [[LINC01145-1]] | -0.50 | -0.30 / -0.24 | both halves | 4e-04 |  |
| [[EPM2A]] | -0.49 | -0.51 / -0.07 | ⚠ one half (not replicated) | 0.004 |  |
| [[AVEN]] | -0.49 | -0.47 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[ERMAP]] | -0.49 | -0.47 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PTPRF's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PASD1]] | B | PASD1 activity lowers PTPRF's level | lines that do not express PASD1 (41) vs lines expressing it (9) | 1.40× higher at baseline in the lines without PASD1 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, RNF17; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.5, -1.8); signed map (-29.1, 22.5). **Vector** length 98.3, 34.6% of its response variance represented; |z| ≥ 3 in 1,397 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.1 | -3.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.0 | -0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +5.7 | -7.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.2 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.8 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.4 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.2 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.8 | -7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -17.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -3.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.5 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -2.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.7 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase receptor type F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:43,525,187-43,623,666 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously LAR |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Protein tyrosine phosphatases receptor type; LAR protein receptor tyrosine phosphatase family |
| Reactome | 7 pathways, smallest: Receptor-type tyrosine-protein phosphatases; Synaptic adhesion-like molecules; Insulin receptor recycling |
| Matched by | ensembl_id |

**Function**, from UniProt [P10586](https://www.uniprot.org/uniprotkb/P10586) (Receptor-type tyrosine-protein phosphatase F):

> Possible cell adhesion receptor. It possesses an intrinsic protein tyrosine phosphatase activity (PTPase) and dephosphorylates EPHA2 regulating its activity.; The first PTPase domain has enzymatic activity, while the second one seems to affect the substrate specificity of the first one.

**Summary**, from NCBI Gene [5792](https://www.ncbi.nlm.nih.gov/gene/5792):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP possesses an extracellular region, a single transmembrane region, and two tandem intracytoplasmic catalytic domains, and thus represents a receptor-type PTP. The extracellular region contains three Ig-like domains, and nine …

**Accessions** — [HGNC:9670](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9670) · Entrez [5792](https://www.ncbi.nlm.nih.gov/gene/5792) · UniProt [P10586](https://www.uniprot.org/uniprotkb/P10586) · Ensembl [ENSG00000142949](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142949)

## Data

Gene col 6668: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6668); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6668, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6668]; `tensor/DDL_lfc|DDL_z.npy` [6668]; `embed/gene_vectors.npy` [6668]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6668 or target_col == 6668). Every well: [[PTPRF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
