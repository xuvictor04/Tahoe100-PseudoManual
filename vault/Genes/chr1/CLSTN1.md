---
symbol: "CLSTN1"
type: "gene"
col: 10136
ensembl_id: "ENSG00000171603"
name: "calsyntenin 1"
location: "1p36.22"
module: 50
arm: "+"
pooled_cpm: 111.18
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 16
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# CLSTN1

*calsyntenin 1* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.48× (z +8.6, q 5e-15, up in 36 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 2.09×, HS-578T 2.20×, A-172 2.24×, HEC-1-A 1.92×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1573 2.40×, A-172 2.18×, NCI-H460 2.01×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 2.16×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.559× (z -12.7, q 2e-34, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TWSG1]] (+0.72, fdr 7e-06), [[ITM2C]] (+0.72, fdr 7e-06), [[HDAC1]] (+0.71, fdr 7e-06); moves opposite to [[NIFK]] (-0.67, fdr 7e-06), [[ZNF593]] (-0.67, fdr 7e-06), [[CCDC137]] (-0.66, fdr 7e-06).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MXRA8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10136.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 2.09×, HS-578T 2.20×, A-172 2.24×, HEC-1-A 1.92×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1573 2.40×, A-172 2.18×, NCI-H460 2.01×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 2.16×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +8.6 | 5e-15 | 36/49 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +7.8 | 1e-12 | 28/44 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +5.2 | 4e-05 | 18/48 (KATO III, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.20×** | +3.7 | 0.023 | 20/45 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.023 | 23/48 (KATO III, SW480, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10136.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.559×** | -12.7 | 2e-34 | 42/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.574×** | -11.7 | 3e-29 | 38/48 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.690×** | -11.5 | 2e-28 | 36/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.618×** | -10.6 | 6e-24 | 46/48 (LoVo, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -8.9 | 5e-17 | 32/49 (MIA PaCa-2, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.732×** | -6.8 | 7e-10 | 37/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.656×** | -4.8 | 1e-04 | 31/47 (HCT15, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.824×** | -4.2 | 0.001 | 24/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.818×** | -4.2 | 0.001 | 22/48 (NCI-H23, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.826×** | -4.2 | 0.002 | 24/48 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.827×** | -4.2 | 0.002 | 22/48 (C32, NCI-H460, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.819×** | -4.1 | 0.002 | 27/48 (C32, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **0.824×** | -4.1 | 0.002 | 26/47 (HOP62, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~8% of this change | **0.824×** | -4.1 | 0.002 | 23/47 (HepG2/C3A, LoVo, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.825×** | -4.1 | 0.002 | 26/49 (HS-578T, hTERT-HPNE, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.842× | -3.8 | 0.005 | 18/48 (SNU-1, NCI-H460, …) | top dose only | position effect removed |
| [[Lactate (calcium) (drug)]] 5 µM |  | 0.862× | -3.3 | 0.038 | 11/48 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.865× | -3.1 | 0.065 | 16/48 (LOX-IMVI, LoVo, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.771×** | -3.0 | 0.078 | 14/48 (MIA PaCa-2, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10136. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 77.0 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -20.0) |
| [[HOP62 (line)]] | alt | 201 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.79× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -15.8) |
| [[C32 (line)]] | wt | 99.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 117 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 182 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.386× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 54.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.456× (z -10.5) |
| [[SNU-423 (line)]] | alt | 109 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.402× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 164 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -15.4) |
| [[COLO 205 (line)]] | alt | 107 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.388× (z -9.7) |
| [[HT-29 (line)]] | alt | 167 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.473× (z -9.7) |
| [[PANC-1 (line)]] | alt | 106 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.622× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 154 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.92× (z +10.4) ⚠ toxic; transcription drop | [[Auranofin (drug)]] 5 µM 0.566× (z -9.1) |
| [[Hs 766T (line)]] | wt | 152 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.469× (z -9.1) |
| [[HS-578T (line)]] | alt | 179 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.481× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 136 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -11.2) |
| [[KATO III (line)]] | alt | 99.7 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 99.9 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.407× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 82.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +10.3) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.5 µM 0.498× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 79.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.98× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.596× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 105 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -12.4) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -9.0) |
| [[RKO (line)]] | wt | 100 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.445× (z -9.2) |
| [[SW 900 (line)]] | alt | 107 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.361× (z -11.4) |
| [[A-427 (line)]] | wt | 102 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.517× (z -8.8) |
| [[A498 (line)]] | wt | 51.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.94× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 122 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.174× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 118 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.433× (z -8.9) |
| [[C-33 A (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -11.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 109 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.363× (z -9.4) |
| [[HCT15 (line)]] | alt | 170 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.583× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 119 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.409× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~8% of this change |
| [[J82 (line)]] | alt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.587× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 100 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.449× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 105 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 89.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.428× (z -9.1) |
| [[SNU-1 (line)]] | wt | 141 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.173× (z -9.4) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 131 | 0 | 1 | — | [[Silodosin (drug)]] 0.05 µM 0.0985× (z -9.4) |
| [[SW 1271 (line)]] | alt | 104 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0501× (z -13.9) |
| [[A549 (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 86.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 75.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10136), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TWSG1]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[ITM2C]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[HDAC1]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[GUSB]] | +0.69 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CALM3]] | +0.68 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[PRKACA]] | +0.68 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[ERMP1]] | +0.68 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[TMEM30A]] | +0.67 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[BCAM]] | +0.65 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PPT1]] | +0.64 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[RNPEP]] | +0.64 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[BSG]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIFK]] | -0.67 | -0.67 / -0.71 | both halves | 7e-06 |  |
| [[ZNF593]] | -0.67 | -0.62 / -0.73 | both halves | 7e-06 |  |
| [[CCDC137]] | -0.66 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[NSRP1]] | -0.64 | -0.68 / -0.62 | both halves | 7e-06 |  |
| [[DNTTIP2]] | -0.61 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[NKAPD1]] | -0.60 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[MRPL46]] | -0.59 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[MRPL45P2]] | -0.59 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[FBXO10]] | -0.58 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[TSSC4]] | -0.58 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[NME6]] | -0.58 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[CEBPZ]] | -0.58 | -0.55 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MXRA8]] | B | MXRA8 activity raises CLSTN1's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 1.24× lower at baseline in the lines without MXRA8 | 0.021 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[ATP6AP1]] | C | ATP6AP1's natural level strengthens CLSTN1's drug response | ATP6AP1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.17; direction not clear | 0.078 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.725). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.6, -21.6); signed map (-28.6, -37.6). **Vector** length 128, 37.7% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.8 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.6 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.8 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +1.6 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.7 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.5 | -12.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.9 | -10.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.6 | -11.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -11.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -4.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.0 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | calsyntenin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:9,728,926-9,823,984 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CSTN1, KIAA0911, CDHR12 |
| Gene groups (HGNC) | Cadherin related |
| Matched by | ensembl_id |

**Function**, from UniProt [O94985](https://www.uniprot.org/uniprotkb/O94985) (Calsyntenin-1):

> Postsynaptic adhesion molecule that binds to presynaptic neurexins to mediate both excitatory and inhibitory synapse formation (By similarity). Promotes synapse development by acting as a cell adhesion molecule at the postsynaptic membrane, which associates with neurexin-alpha at the presynaptic membrane (By similarity). Also functions as a cargo in axonal anterograde transport by acting as a molecular adapter that promotes KLC1 association with vesicles. Complex formation with APBA2 and APP, …

**Summary**, from NCBI Gene [22883](https://www.ncbi.nlm.nih.gov/gene/22883):

> This gene is a member of the calsyntenin family, a subset of the cadherin superfamily. The encoded transmembrane protein, also known as alcadein-alpha, is thought to bind to kinesin-1 motors to mediate the axonal anterograde transport of certain types of vesicle. Amyloid precursor protein (APP) is trafficked via these vesicles and so this protein is being investigated to see how it might contribute to the mechanisms underlying Alzheimer's disease. Alternative splicing results in multiple …

**Accessions** — [HGNC:17447](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17447) · Entrez [22883](https://www.ncbi.nlm.nih.gov/gene/22883) · UniProt [O94985](https://www.uniprot.org/uniprotkb/O94985) · Ensembl [ENSG00000171603](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171603)

## Data

Gene col 10136: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10136); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10136, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10136]; `tensor/DDL_lfc|DDL_z.npy` [10136]; `embed/gene_vectors.npy` [10136]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10136 or target_col == 10136). Every well: [[CLSTN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLSTN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
