---
symbol: "NOP58"
type: "gene"
col: 619
ensembl_id: "ENSG00000055044"
name: "NOP58 ribonucleoprotein"
location: "2q33.1"
module: 40
arm: "+"
pooled_cpm: 237.73
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# NOP58

*NOP58 ribonucleoprotein* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.13× (z +11.9, q 4e-30, up in 48 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.718×; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW 1271 0.146×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNL3]] (+0.61, fdr 1e-05), [[EIF2A]] (+0.59, fdr 3e-05), [[TFB2M]] (+0.57, fdr 2e-05); moves opposite to [[LRRC57]] (-0.55, fdr 1e-05), [[ANKRD50]] (-0.54, fdr 5e-05), [[PPM1A]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CUZD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 619.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.13×** | +11.9 | 4e-30 | 48/49 (COLO 205, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.40×** | +10.2 | 7e-22 | 46/48 (NCI-H1792, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **5.07×** | +9.9 | 1e-20 | 47/48 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.29×** | +9.6 | 1e-19 | 46/48 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.72×** | +8.9 | 5e-17 | 42/48 (NCI-H1792, LoVo, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.13×** | +8.8 | 1e-16 | 44/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.04×** | +8.3 | 8e-15 | 43/48 (BT-474, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.93×** | +7.6 | 2e-12 | 47/48 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.92×** | +7.3 | 2e-11 | 45/47 (COLO 205, LoVo, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.67×** | +6.0 | 1e-07 | 34/38 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.61×** | +5.3 | 6e-06 | 39/48 (COLO 205, NCI-H1792, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.56×** | +5.2 | 1e-05 | 37/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +5.0 | 3e-05 | 39/48 (RKO, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.50×** | +4.7 | 9e-05 | 38/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.73×** | +4.5 | 2e-04 | 44/49 (SW1417, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +4.5 | 3e-04 | 43/48 (CFPAC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.010 | 30/48 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.010 | 32/48 (MIA PaCa-2, NCI-H460, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.028 | 28/49 (H4, SK-MEL-2, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.058 | 23/48 (CFPAC-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.42×** | +2.9 | 0.084 | 37/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 619.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.718×; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW 1271 0.146×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 0.728× | -3.6 | 0.11 | 31/47 (LoVo, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.742× | -3.5 | 0.11 | 35/47 (LoVo, C32, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.743× | -3.5 | 0.11 | 36/47 (LoVo, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.819× | -3.2 | 0.18 | 27/48 (LoVo, SW480, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.826× | -3.2 | 0.18 | 25/48 (SHP-77, AsPC-1, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.770× | -3.0 | 0.22 | 29/48 (AsPC-1, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 619. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 243 | 9 (6 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.53× (z +14.6) | — |
| [[LoVo (line)]] | wt | 213 | 8 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.16× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 223 | 7 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 6.94× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 161 | 7 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.07× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.5× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 197 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.65× (z +14.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 8.53× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 305 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +12.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.78× (z +10.3) | — |
| [[COLO 205 (line)]] | alt | 134 | 5 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 6.45× (z +14.7) ⚠ toxic; cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 21.4× (z +13.1) | — |
| [[HepG2_C3A (line)]] | wt | 184 | 5 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.12× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 144 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.90× (z +12.4) | — |
| [[LOX-IMVI (line)]] | wt | 251 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.02× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 167 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +14.9) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.92× (z +13.9) | — |
| [[NCI-H460 (line)]] | wt | 197 | 5 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.63× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[Panc 03.27 (line)]] | alt | 176 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.07× (z +12.7) | — |
| [[PANC-1 (line)]] | alt | 249 | 5 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.30× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.39× (z +11.5) | — |
| [[SHP-77 (line)]] | alt | 316 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.62× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 174 | 4 | 0 | [[Auranofin (drug)]] 5 µM 4.77× (z +16.7) | — |
| [[C32 (line)]] | wt | 221 | 4 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 15.0× (z +10.1) | — |
| [[KATO III (line)]] | alt | 158 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.00× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 312 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +10.8) | — |
| [[RKO (line)]] | wt | 258 | 4 | 0 | [[PH-797804 (drug)]] 5 µM 9.59× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 329 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.19× (z +9.7) | — |
| [[A-172 (line)]] | wt | 120 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.7) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.23× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 255 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.38× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 187 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.06× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 136 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.71× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 256 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.18× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 232 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.85× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 247 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.23× (z +10.6) | — |
| [[SNU-1 (line)]] | wt | 209 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.43× (z +10.5) | — |
| [[SW48 (line)]] | wt | 256 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 5.97× (z +15.2) | — |
| [[J82 (line)]] | alt | 337 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.22× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 289 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.10× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 299 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +8.8) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.40× (z +8.7) | — |
| [[A549 (line)]] | wt | 209 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.6) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[AN3 CA (line)]] | alt | 213 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.81× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 242 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.25× (z +10.4) | — |
| [[H4 (line)]] | wt | 311 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.41× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 440 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +8.5) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[SW 1271 (line)]] | alt | 217 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 215 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 410 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 249 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 219 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 163 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 392 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 270 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 619), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNL3]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 946 |
| [[EIF2A]] | +0.59 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[TFB2M]] | +0.57 | +0.60 / +0.46 | both halves | 2e-05 | STRING 631 |
| [[GNL2]] | +0.55 | +0.63 / +0.41 | both halves | 4e-05 | STRING 814 |
| [[UTP6]] | +0.55 | +0.67 / +0.41 | both halves | 4e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 998 |
| [[USPL1]] | +0.54 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[DCAF13]] | +0.53 | +0.46 / +0.55 | both halves | 2e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 998 |
| [[EIF3B]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 | STRING 620 |
| [[GAR1]] | +0.53 | +0.58 / +0.35 | both halves | 1e-04 | pathway: rRNA modification in the nucleus and cytosol; STRING 985 |
| [[PMM2]] | +0.53 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[DNAJC25]] | +0.52 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[SNHG15]] | +0.52 | +0.58 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC57]] | -0.55 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ANKRD50]] | -0.54 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[PPM1A]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[RO60]] | -0.46 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[PSENEN]] | -0.46 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[TRAPPC3]] | -0.46 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[LIG4]] | -0.46 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[BMAL1]] | -0.46 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[PPP1CA]] | -0.46 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[SP1]] | -0.45 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[AKIRIN1]] | -0.45 | -0.39 / -0.37 | both halves | 7e-05 |  |
| [[RAB1B]] | -0.45 | -0.48 / -0.34 | both halves | 1e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CUZD1]] | B | CUZD1 activity raises NOP58's level | lines that do not express CUZD1 (9) vs lines expressing it (41) | 1.29× lower at baseline in the lines without CUZD1 | 0.079 | ⚠ within organs, on part of the lines; also absent: FAM24B, C10orf88B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.424). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-9.8, -19.3); signed map (-59.5, 11.0). **Vector** length 87.0, 44.0% of its response variance represented; |z| ≥ 3 in 1,355 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +1.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.1 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +9.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.3 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -8.1 | +4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -7.9 | +8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -6.8 | +5.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -5.9 | +5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -5.5 | +9.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | +0.7 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | NOP58 ribonucleoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:202,265,736-202,303,661 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NOP5, HSPC120 |
| Gene groups (HGNC) | U3 small nucleolar ribonucleoprotein; Small nucleolar RNA protein coding host genes |
| Reactome | 8 pathways, smallest: SUMOylation of RNA binding proteins; rRNA modification in the nucleus and cytosol; SUMO E3 ligases SUMOylate target proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2X3](https://www.uniprot.org/uniprotkb/Q9Y2X3) (Nucleolar protein 58):

> Required for the biogenesis of box C/D snoRNAs such as U3, U8 and U14 snoRNAs. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the …

**Summary**, from NCBI Gene [51602](https://www.ncbi.nlm.nih.gov/gene/51602):

> The protein encoded by this gene is a core component of box C/D small nucleolar ribonucleoproteins. Some box C/D small nucleolar RNAs (snoRNAs), such as U3, U8, and U14, are dependent upon the encoded protein for their synthesis. This protein is SUMOylated, which is necessary for high affinity binding to snoRNAs. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:29926](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29926) · Entrez [51602](https://www.ncbi.nlm.nih.gov/gene/51602) · UniProt [Q9Y2X3](https://www.uniprot.org/uniprotkb/Q9Y2X3) · Ensembl [ENSG00000055044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000055044)

## Data

Gene col 619: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 619); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 619, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 619]; `tensor/DDL_lfc|DDL_z.npy` [619]; `embed/gene_vectors.npy` [619]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 619 or target_col == 619). Every well: [[NOP58 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOP58.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
