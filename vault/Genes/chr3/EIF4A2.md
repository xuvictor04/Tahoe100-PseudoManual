---
symbol: "EIF4A2"
type: "gene"
col: 8032
ensembl_id: "ENSG00000156976"
name: "eukaryotic translation initiation factor 4A2"
location: "3q27.3"
module: 12
arm: "+"
pooled_cpm: 237.33
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# EIF4A2

*eukaryotic translation initiation factor 4A2* — 3q27.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.12× (z +14.3, q 1e-43, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.640× (z -6.8, q 7e-09, down in 37 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.798× (z -3.4, q 0.073, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IMPDH2]] (+0.63, fdr 2e-05), [[NOB1]] (+0.63, fdr 1e-05), [[ALAS1]] (+0.57, fdr 5e-05); moves opposite to [[ANXA2R-OT1]] (-0.54, fdr 3e-05), [[TNPO2]] (-0.52, fdr 2e-04), [[ZBTB8OS]] (-0.51, fdr 2e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IRF6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8032.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.12×** | +14.3 | 1e-43 | 44/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.20×** | +12.4 | 6e-33 | 46/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.04×** | +11.2 | 8e-27 | 45/48 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.80×** | +9.3 | 2e-18 | 46/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +7.9 | 3e-13 | 42/48 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.31×** | +6.9 | 5e-10 | 43/49 (C32, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +6.8 | 1e-09 | 41/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +6.4 | 9e-09 | 41/48 (SK-MEL-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +6.0 | 1e-07 | 34/48 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.9 | 2e-07 | 37/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.87×** | +5.1 | 1e-05 | 37/45 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 3e-05 | 35/48 (HS-578T, HCT15, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +4.5 | 3e-04 | 32/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.29×** | +4.0 | 0.002 | 28/48 (NCI-H460, LS 180, …) | inconsistent across doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +3.6 | 0.011 | 26/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.012 | 34/48 (NCI-H2347, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.012 | 28/48 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.013 | 29/48 (H4, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Clopidogrel (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.076 | 25/48 (SNU-423, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8032.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.640×** | -6.8 | 7e-09 | 37/44 (SNU-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.708×** | -5.4 | 1e-05 | 34/49 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.755×** | -4.1 | 0.008 | 29/45 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.798×** | -3.4 | 0.073 | 27/48 (SW480, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.829×** | -3.4 | 0.073 | 23/49 (LoVo, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.854× | -3.4 | 0.076 | 17/49 (SNU-1, LS 180, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.812×** | -3.3 | 0.081 | 26/48 (HepG2/C3A, LS 180, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.807×** | -3.3 | 0.081 | 26/47 (KATO III, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8032. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 149 | 8 (7 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.43× (z +12.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.5) | — |
| [[SW480 (line)]] | alt | 285 | 6 | 2 | [[Panobinostat (drug)]] 5 µM 2.79× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -11.6) |
| [[A-427 (line)]] | wt | 373 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.29× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.424× (z -9.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 188 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.84× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 218 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +15.0) | — |
| [[SW48 (line)]] | wt | 279 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.62× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 245 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +18.3) | [[Dinaciclib (drug)]] 0.5 µM 0.485× (z -8.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 171 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +19.6) | — |
| [[HOP62 (line)]] | alt | 163 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +18.8) | — |
| [[hTERT-HPNE (line)]] | wt | 165 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +18.2) | — |
| [[PANC-1 (line)]] | alt | 190 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -11.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 186 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -12.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 192 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -10.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 193 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +15.0) | — |
| [[HT-29 (line)]] | alt | 241 | 3 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -10.5) |
| [[SNU-423 (line)]] | alt | 178 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +13.9) | — |
| [[SW 900 (line)]] | alt | 132 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.7) | — |
| [[A-172 (line)]] | wt | 168 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.26× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.495× (z -9.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 403 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +9.0) ⚠ cell-cycle shift, explains ~43% of this change | [[Dinaciclib (drug)]] 5 µM 0.307× (z -13.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 356 | 2 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.65× (z +11.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 2.19× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 219 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.74× (z +13.2) | — |
| [[LS 180 (line)]] | wt | 298 | 2 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +10.9) ⚠ cell-cycle shift, explains ~43% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 288 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 147 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +18.0) | — |
| [[NCI-H2347 (line)]] | alt | 256 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.37× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 442 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -12.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 195 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +11.6) | — |
| [[RPMI-7951 (line)]] | alt | 157 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +10.7) | — |
| [[SNU-1 (line)]] | wt | 600 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 309 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.1) | — |
| [[J82 (line)]] | alt | 180 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 287 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 265 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.6) | — |
| [[HCT15 (line)]] | alt | 226 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.18× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 218 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.16× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 130 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.2) | — |
| [[SW 1088 (line)]] | alt | 133 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0746× (z -10.4) |
| [[SW1417 (line)]] | alt | 368 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.6) | — |
| [[A549 (line)]] | wt | 184 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 169 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 264 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 218 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 234 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 176 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8032), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMPDH2]] | +0.63 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[NOB1]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ALAS1]] | +0.57 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[NOA1]] | +0.56 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[PPP2R2A]] | +0.55 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[RPP40]] | +0.52 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[MLST8]] | +0.52 | +0.48 / +0.39 | both halves | 6e-05 | STRING 415 |
| [[THYN1]] | +0.51 | +0.51 / +0.33 | both halves | 1e-04 |  |
| [[MRPL17]] | +0.51 | +0.33 / +0.36 | both halves | 1e-04 |  |
| [[C17orf58]] | +0.51 | +0.34 / +0.46 | both halves | 1e-04 |  |
| [[MRPL10]] | +0.51 | +0.40 / +0.40 | both halves | 5e-05 |  |
| [[MYG1]] | +0.51 | +0.47 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA2R-OT1]] | -0.54 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[TNPO2]] | -0.52 | -0.51 / -0.29 | both halves | 2e-04 | same gene group |
| [[ZBTB8OS]] | -0.51 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[NFATC2IP]] | -0.48 | -0.52 / -0.43 | both halves | 3e-05 | same gene group |
| [[AP4S1]] | -0.48 | -0.20 / -0.51 | both halves | 7e-04 |  |
| [[BCL2L2-PABPN1]] | -0.47 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[RBBP4]] | -0.47 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[GPALPP1]] | -0.47 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[SUZ12P1]] | -0.47 | -0.58 / -0.22 | both halves | 6e-04 |  |
| [[LAMTOR5-AS1]] | -0.46 | -0.27 / -0.29 | both halves | 3e-04 |  |
| [[SOCS4]] | -0.45 | -0.37 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[SLC25A53]] | -0.45 | -0.35 / -0.32 | both halves | 1e-04 |  |
| [[URM1]] | -0.45 | -0.33 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF6]] | B | IRF6 activity raises EIF4A2's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.43× lower at baseline in the lines without IRF6 | 0.073 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.357). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-46.1, -7.8); signed map (-16.6, -24.3). **Vector** length 106, 34.7% of its response variance represented; |z| ≥ 3 in 1,121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +9.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +11.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | +4.3 | +3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +2.5 |
|  | [[Uridine (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +1.2 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | +2.2 | +1.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +2.0 | +1.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.5 | -0.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | -8.0 | +3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -7.2 | +3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -7.1 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | +3.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 4A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.3 — chr3:186,783,205-186,789,897 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DDX2B, EIF4A, BM-010; previously EIF4F |
| Gene groups (HGNC) | DEAD-box helicases; MicroRNA protein coding host genes; Small nucleolar RNA protein coding host genes |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, MYOGENESIS |
| Reactome | 21 pathways, smallest: Z-decay: degradation of maternal mRNAs by zygotically expressed factors; Deadenylation of mRNA; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14240](https://www.uniprot.org/uniprotkb/Q14240) (Eukaryotic initiation factor 4A-II):

> ATP-dependent RNA helicase which is a subunit of the eIF4F complex involved in cap recognition and is required for mRNA binding to ribosome. In the current model of translation initiation, eIF4A unwinds RNA secondary structures in the 5'-UTR of mRNAs which is necessary to allow efficient binding of the small ribosomal subunit, and subsequent scanning for the initiator codon.

**Summary**, from NCBI Gene [1974](https://www.ncbi.nlm.nih.gov/gene/1974):

> Enables ATP hydrolysis activity. Involved in negative regulation of RNA-dependent RNA polymerase activity. Located in perinuclear region of cytoplasm. Implicated in neurodevelopmental disorder with hypotonia and speech delay. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3284](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3284) · Entrez [1974](https://www.ncbi.nlm.nih.gov/gene/1974) · UniProt [Q14240](https://www.uniprot.org/uniprotkb/Q14240) · Ensembl [ENSG00000156976](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156976)

## Data

Gene col 8032: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8032); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8032, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8032]; `tensor/DDL_lfc|DDL_z.npy` [8032]; `embed/gene_vectors.npy` [8032]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8032 or target_col == 8032). Every well: [[EIF4A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF4A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
