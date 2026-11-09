---
symbol: "SLTM"
type: "gene"
col: 6064
ensembl_id: "ENSG00000137776"
name: "SAFB like transcription modulator"
location: "15q22.1"
module: 51
arm: "+"
pooled_cpm: 215.34
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# SLTM

*SAFB like transcription modulator* — 15q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.46× (z +25.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.646× (z -8.7, q 1e-15, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSB]] (+0.69, fdr 7e-06), [[ZNF326]] (+0.68, fdr 7e-06), [[SREK1]] (+0.66, fdr 7e-06); moves opposite to [[ALDOA]] (-0.59, fdr 5e-05), [[BSG]] (-0.57, fdr 2e-05), [[BRK1]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6064.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.46×** | +25.5 | 0e+00 | 48/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.27×** | +16.4 | 0e+00 | 48/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.21×** | +15.2 | 0e+00 | 48/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +11.5 | 3e-28 | 45/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +10.9 | 1e-25 | 46/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +9.1 | 1e-17 | 43/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +7.6 | 2e-12 | 37/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +7.0 | 2e-10 | 38/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +6.4 | 8e-09 | 33/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +6.3 | 1e-08 | 39/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **1.30×** | +5.3 | 7e-06 | 30/49 (SW480, A549, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +5.0 | 3e-05 | 27/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 3e-04 | 27/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.24×** | +4.3 | 7e-04 | 26/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.23×** | +4.2 | 0.001 | 26/48 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.0 | 0.003 | 12/49 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.43×** | +3.8 | 0.005 | 26/49 (SW48, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.006 | 28/48 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.010 | 22/48 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6064.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.646×** | -8.7 | 1e-15 | 44/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.650×** | -8.6 | 2e-15 | 46/48 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.678×** | -7.8 | 2e-12 | 43/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.794×** | -6.5 | 1e-08 | 31/49 (A498, A549, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.729×** | -6.3 | 3e-08 | 43/48 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -6.2 | 4e-08 | 1/50 (NCI-H23) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.789×** | -4.7 | 2e-04 | 27/48 (A549, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.852× | -4.5 | 4e-04 | 16/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.670×** | -4.2 | 0.002 | 33/49 (KATO III, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.5 | 0.030 | 19/49 (KATO III, HT-29, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.842× | -3.4 | 0.030 | 18/48 (AsPC-1, A-427, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.854× | -3.1 | 0.078 | 14/48 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6064. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 187 | 11 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +19.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.651× (z -9.0) ⚠ cell-cycle shift, explains ~13% of this change |
| [[SW480 (line)]] | alt | 217 | 9 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +21.3) | [[Belinostat (drug)]] 5 µM 0.525× (z -11.6) |
| [[LoVo (line)]] | wt | 317 | 10 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.60× (z +24.7) | — |
| [[KATO III (line)]] | alt | 248 | 6 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +22.2) | [[Belinostat (drug)]] 5 µM 0.460× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 249 | 6 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +20.8) | [[Panobinostat (drug)]] 0.5 µM 0.474× (z -11.3) |
| [[HT-29 (line)]] | alt | 255 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +21.6) | — |
| [[A498 (line)]] | wt | 266 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +16.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -15.0) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.507× (z -10.0) |
| [[COLO 205 (line)]] | alt | 227 | 6 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +22.4) | [[Panobinostat (drug)]] 0.5 µM 0.436× (z -11.8) |
| [[LS 180 (line)]] | wt | 251 | 6 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.78× (z +17.0) | [[Panobinostat (drug)]] 0.5 µM 0.498× (z -8.9) |
| [[PANC-1 (line)]] | alt | 206 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +28.2) | — |
| [[A549 (line)]] | wt | 273 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +24.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -14.5) ⚠ cell-cycle shift, explains ~13% of this change |
| [[SW48 (line)]] | wt | 248 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +17.6) | — |
| [[A-172 (line)]] | wt | 144 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +13.0) | — |
| [[A-427 (line)]] | wt | 159 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.1) | — |
| [[AsPC-1 (line)]] | alt | 177 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HOP62 (line)]] | alt | 157 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +17.6) | — |
| [[RKO (line)]] | wt | 216 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +24.5) | — |
| [[SNU-1 (line)]] | wt | 410 | 1 | 3 (2 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.87× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.455× (z -9.1) |
| [[SW1417 (line)]] | alt | 298 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +23.9) | — |
| [[C32 (line)]] | wt | 160 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +15.1) | — |
| [[H4 (line)]] | wt | 167 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +16.5) | — |
| [[HCT15 (line)]] | alt | 231 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +13.0) | — |
| [[HEC-1-A (line)]] | alt | 245 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +19.0) | — |
| [[hTERT-HPNE (line)]] | wt | 139 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +15.0) | — |
| [[J82 (line)]] | alt | 203 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 180 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +15.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 220 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.9) | — |
| [[NCI-H1792 (line)]] | alt | 215 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +18.3) | — |
| [[Panc 03.27 (line)]] | alt | 270 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +19.0) | — |
| [[RPMI-7951 (line)]] | alt | 200 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 161 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +15.0) | — |
| [[C-33 A (line)]] | alt | 208 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 196 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +19.5) | — |
| [[HepG2_C3A (line)]] | wt | 160 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 136 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.9) | — |
| [[HS-578T (line)]] | alt | 136 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.1) | — |
| [[NCI-H2347 (line)]] | alt | 207 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +15.7) | — |
| [[SHP-77 (line)]] | alt | 209 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.18× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 204 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 193 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +14.9) | — |
| [[CHP-212 (line)]] | wt | 199 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 300 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 121 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.7) | — |
| [[SW 1088 (line)]] | alt | 140 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0725× (z -12.5) |
| [[SW 1271 (line)]] | alt | 275 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.189× (z -10.7) |
| [[AN3 CA (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 310 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6064), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSB]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 | same gene group |
| [[ZNF326]] | +0.68 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[SREK1]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 | same gene group; STRING 413 |
| [[MTIF2]] | +0.64 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[U2SURP]] | +0.63 | +0.61 / +0.58 | both halves | 8e-06 | same gene group; STRING 544 |
| [[CCAR1]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[KCNMB3]] | +0.62 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[CCDC25]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ZNF428]] | +0.62 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[CCT6P3]] | +0.60 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[SENP6]] | +0.60 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[TLK1]] | +0.58 | +0.43 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDOA]] | -0.59 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[BSG]] | -0.57 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[BRK1]] | -0.57 | -0.60 / -0.40 | both halves | 4e-05 |  |
| [[PDCD6]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[GAPDH]] | -0.53 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[P3H1]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[TMED4]] | -0.51 | -0.59 / -0.38 | both halves | 7e-05 |  |
| [[TK1]] | -0.51 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[TRAPPC1]] | -0.51 | -0.63 / -0.25 | both halves | 4e-04 |  |
| [[LSM4]] | -0.51 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[SDHA]] | -0.51 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[TMBIM6]] | -0.51 | -0.56 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SLTM's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.552). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-22.5, 6.2); signed map (12.2, -35.9). **Vector** length 101, 38.0% of its response variance represented; |z| ≥ 3 in 1,326 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +25.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.6 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +16.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.9 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.8 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +5.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.3 | +0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.3 | +3.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.4 | +3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.7 | +7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.1 | -8.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.9 | -7.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | +3.7 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -2.2 | -1.5 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -3.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.1 | -1.3 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | SAFB like transcription modulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.1 — chr15:58,879,050-58,933,679 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Met, FLJ13213 |
| Gene groups (HGNC) | RNA binding motif containing; Scaffold attachment factor B family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWH9](https://www.uniprot.org/uniprotkb/Q9NWH9) (SAFB-like transcription modulator):

> When overexpressed, acts as a general inhibitor of transcription that eventually leads to apoptosis.

**Summary**, from NCBI Gene [79811](https://www.ncbi.nlm.nih.gov/gene/79811):

> Enables RNA binding activity. Predicted to be involved in DNA-templated transcription and apoptotic process. Located in nuclear body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20709](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20709) · Entrez [79811](https://www.ncbi.nlm.nih.gov/gene/79811) · UniProt [Q9NWH9](https://www.uniprot.org/uniprotkb/Q9NWH9) · Ensembl [ENSG00000137776](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137776)

## Data

Gene col 6064: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6064); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6064, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6064]; `tensor/DDL_lfc|DDL_z.npy` [6064]; `embed/gene_vectors.npy` [6064]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6064 or target_col == 6064). Every well: [[SLTM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLTM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
