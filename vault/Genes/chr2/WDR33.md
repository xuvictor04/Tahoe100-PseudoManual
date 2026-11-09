---
symbol: "WDR33"
type: "gene"
col: 5890
ensembl_id: "ENSG00000136709"
name: "WD repeat domain 33"
location: "2q14.3"
module: 88
arm: "+"
pooled_cpm: 140.32
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# WDR33

*WD repeat domain 33* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.14× (z +8.3, q 5e-14, up in 38 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 6 lines (LoVo 4.54×, LS 180 3.56×, SW480 3.16×, HT-29 3.45×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (LS 180 1.84×, LoVo 1.68×, SNU-1 1.74×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LS 180 1.81×, LoVo 1.77×); [[PH-797804 (drug)]] 5 µM in 1 line (LS 180 2.88×).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.506× (z -14.3, q 1e-43, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LATS1]] (+0.77, fdr 7e-06), [[ZFX]] (+0.72, fdr 1e-05), [[ZC3H4]] (+0.72, fdr 1e-05); moves opposite to [[USP2]] (-0.67, fdr 1e-05), [[TPST2]] (-0.67, fdr 3e-05), [[INPP5F]] (-0.64, fdr 6e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF876P]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5890.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 6 lines (LoVo 4.54×, LS 180 3.56×, SW480 3.16×, HT-29 3.45×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (LS 180 1.84×, LoVo 1.68×, SNU-1 1.74×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LS 180 1.81×, LoVo 1.77×); [[PH-797804 (drug)]] 5 µM in 1 line (LS 180 2.88×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.14×** | +8.3 | 5e-14 | 38/49 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +5.5 | 1e-05 | 26/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.4 | 2e-05 | 22/48 (LS 180, LoVo, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +5.1 | 5e-05 | 0/50 | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.32× | +3.0 | 0.26 | 21/48 (LS 180, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5890.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.506×** | -14.3 | 1e-43 | 48/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.562×** | -12.1 | 2e-31 | 45/49 (C-33 A, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.586×** | -11.2 | 5e-27 | 48/48 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -10.7 | 2e-24 | 33/44 (LS 180, A-427, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.591×** | -10.2 | 2e-22 | 38/45 (SW48, A549, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.627×** | -9.8 | 9e-21 | 47/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.756×** | -5.9 | 3e-07 | 36/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.767×** | -5.6 | 1e-06 | 34/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.805×** | -4.4 | 7e-04 | 27/47 (MIA PaCa-2, SW 900, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.871× | -4.1 | 0.002 | 14/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.729×** | -3.5 | 0.022 | 24/45 (C-33 A, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | 0.843× | -3.5 | 0.022 | 22/47 (C-33 A, NCI-H1792, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.849× | -3.5 | 0.022 | 20/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | 0.860× | -3.2 | 0.058 | 17/48 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5890. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 160 | 5 (2 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.56× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.491× (z -11.4) |
| [[SW 900 (line)]] | alt | 277 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.366× (z -14.1) |
| [[SW480 (line)]] | alt | 191 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.16× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -16.0) |
| [[HEC-1-A (line)]] | alt | 250 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.75× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.357× (z -17.1) |
| [[LoVo (line)]] | wt | 142 | 4 (2 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.54× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.506× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 151 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.457× (z -10.1) |
| [[HCT15 (line)]] | alt | 248 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.414× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 183 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.435× (z -11.3) |
| [[PANC-1 (line)]] | alt | 146 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.507× (z -10.6) |
| [[A-427 (line)]] | wt | 147 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.492× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 162 | 0 | 4 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.153× (z -13.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.523× (z -8.9) |
| [[A549 (line)]] | wt | 132 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.469× (z -10.2) |
| [[HOP62 (line)]] | alt | 132 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.418× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.523× (z -8.8) |
| [[HT-29 (line)]] | alt | 128 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.45× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.479× (z -10.3) |
| [[KATO III (line)]] | alt | 85.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 172 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.433× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.540× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 139 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.484× (z -9.3) |
| [[C-33 A (line)]] | alt | 189 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.471× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 85.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.456× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 161 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 91.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.464× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.127× (z -14.0) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 101 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.399× (z -9.7) |
| [[SNU-1 (line)]] | wt | 157 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.491× (z -8.9) |
| [[SW1417 (line)]] | alt | 137 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.495× (z -10.4) |
| [[AN3 CA (line)]] | alt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -8.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 158 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.76× (z +8.5) | — |
| [[H4 (line)]] | wt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -13.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 179 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.452× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 96.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.175× (z -9.2) ⚠ toxic |
| [[J82 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -12.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 118 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.432× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 168 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.493× (z -10.0) |
| [[RKO (line)]] | wt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -12.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0635× (z -25.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 96.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 99.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 170 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5890), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LATS1]] | +0.77 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ZFX]] | +0.72 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ZC3H4]] | +0.72 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ZNF689]] | +0.70 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[CLHC1]] | +0.70 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[AEBP2]] | +0.70 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[PCBP1-AS1]] | +0.69 | +0.59 / +0.32 | both halves | 2e-04 |  |
| [[MCPH1]] | +0.69 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[TASOR]] | +0.69 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[FIZ1]] | +0.68 | +0.58 / +0.35 | both halves | 1e-04 |  |
| [[ZFP91]] | +0.68 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[AP5M1]] | +0.68 | +0.62 / +0.24 | both halves | 5e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP2]] | -0.67 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[TPST2]] | -0.67 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[INPP5F]] | -0.64 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[DNAAF3]] | -0.64 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[TSPAN33]] | -0.62 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[MAST3]] | -0.62 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[LPCAT2]] | -0.62 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[FCHO1]] | -0.61 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[FAM118A]] | -0.61 | -0.51 / -0.32 | both halves | 1e-04 |  |
| [[RIMS3]] | -0.61 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[CYTH3]] | -0.61 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[ATP7B]] | -0.60 | -0.53 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF876P]] | B | ZNF876P activity raises WDR33's level | lines that do not express ZNF876P (17) vs lines expressing it (33) | 1.19× lower at baseline in the lines without ZNF876P | 0.066 | ⚠ within organs, on part of the lines; also absent: ZNF718, PAX8 |
| [[HDAC6]] | B | HDAC6 activity raises WDR33's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.728). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (1.5, 9.0); signed map (19.5, -23.7). **Vector** length 97.4, 27.1% of its response variance represented; |z| ≥ 3 in 916 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +1.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +1.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.7 | -9.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.6 | -14.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.2 | -11.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.4 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.5 | -0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Neratinib (drug)]] 5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.3 — chr2:127,701,027-127,811,187 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11294, WDC146, NET14 |
| Gene groups (HGNC) | WD repeat domain containing; Cleavage and polyadenylation specific factor subunits |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 13 pathways, smallest: Processing of Intronless Pre-mRNAs; Processing of Capped Intronless Pre-mRNA; RNA Polymerase II Transcription Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0J8](https://www.uniprot.org/uniprotkb/Q9C0J8) (pre-mRNA 3' end processing protein WDR33):

> Essential for both cleavage and polyadenylation of pre-mRNA 3' ends.

**Summary**, from NCBI Gene [55339](https://www.ncbi.nlm.nih.gov/gene/55339):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. This gene is highly expressed in testis and the protein is localized to the …

**Accessions** — [HGNC:25651](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25651) · Entrez [55339](https://www.ncbi.nlm.nih.gov/gene/55339) · UniProt [Q9C0J8](https://www.uniprot.org/uniprotkb/Q9C0J8) · Ensembl [ENSG00000136709](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136709)

## Data

Gene col 5890: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5890); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5890, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5890]; `tensor/DDL_lfc|DDL_z.npy` [5890]; `embed/gene_vectors.npy` [5890]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5890 or target_col == 5890). Every well: [[WDR33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
