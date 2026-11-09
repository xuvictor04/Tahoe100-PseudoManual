---
symbol: "CADM1"
type: "gene"
col: 11352
ensembl_id: "ENSG00000182985"
name: "cell adhesion molecule 1"
location: "11q23.3"
module: 14
arm: "+"
pooled_cpm: 164.46
n_lines_expressing: 32
n_dd_up: 15
n_dd_down: 22
n_dd_up_clean: 15
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 10
direction_downstream: 8
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CADM1

*cell adhesion molecule 1* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.27× (z +32.8, q 0e+00, up in 25 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.521× (z -12.7, q 2e-34, down in 23 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRAD]] (+0.70, fdr 7e-06), [[LRIG1]] (+0.68, fdr 7e-06), [[CGNL1]] (+0.65, fdr 7e-06); moves opposite to [[BMS1P23]] (-0.48, fdr 7e-05), [[MOSMO]] (-0.48, fdr 3e-05), [[C8orf76]] (-0.46, fdr 7e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[GRIN2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[ESPN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11352.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.27×** | +32.8 | 0e+00 | 25/30 (CFPAC-1, A549, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.93×** | +18.2 | 0e+00 | 19/30 (SW1417, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.57×** | +17.8 | 0e+00 | 23/30 (A549, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.16×** | +15.1 | 0e+00 | 21/30 (A549, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.93×** | +12.9 | 5e-36 | 17/30 (SW1417, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +12.6 | 3e-34 | 19/30 (SW1417, A549, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +11.4 | 2e-28 | 18/30 (SW1417, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +10.7 | 1e-24 | 19/30 (SW1417, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.68×** | +10.1 | 3e-22 | 21/31 (BT-474, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +9.9 | 2e-21 | 17/31 (SW1417, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +6.2 | 3e-08 | 17/30 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +6.0 | 9e-08 | 14/31 (SW1417, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +5.7 | 7e-07 | 15/30 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.003 | 12/30 (NCI-H2347, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.007 | 10/30 (A549, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11352.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.521×** | -12.7 | 2e-34 | 23/30 (SK-MEL-2, SHP-77, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.705×** | -9.6 | 2e-19 | 22/31 (PANC-1, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.606×** | -9.4 | 1e-18 | 18/29 (HepG2/C3A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.644×** | -8.6 | 1e-15 | 19/30 (RPMI-7951, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.684×** | -6.9 | 8e-10 | 20/29 (RKO, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.711×** | -6.6 | 3e-09 | 19/31 (A498, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.703×** | -6.5 | 7e-09 | 19/30 (PANC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.724×** | -6.0 | 1e-07 | 17/28 (SK-MEL-2, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dexamethasone (drug)]] 5 µM |  | **0.751×** | -5.6 | 2e-06 | 15/30 (A498, HOP62, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.754×** | -5.5 | 2e-06 | 16/30 (SK-MEL-2, HOP62, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.757×** | -5.4 | 3e-06 | 20/30 (SW480, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.821×** | -5.4 | 3e-06 | 12/30 (NCI-H1792, A498, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.759×** | -5.4 | 4e-06 | 18/30 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.787×** | -4.7 | 1e-04 | 13/30 (SW 900, HOP62, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.796×** | -4.4 | 3e-04 | 14/30 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.796×** | -4.4 | 3e-04 | 15/30 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.797×** | -4.4 | 3e-04 | 19/30 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.798×** | -4.2 | 8e-04 | 15/30 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.765×** | -3.7 | 0.006 | 14/30 (SK-MEL-2, RPMI-7951, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.708×** | -3.5 | 0.012 | 10/29 (SK-MEL-2, H4, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11352. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 466 | 2 | 19 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +13.8) | [[Budesonide (drug)]] 0.5 µM 0.184× (z -11.4) |
| [[SW 900 (line)]] | alt | 354 | 3 | 13 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +18.8) | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.264× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 391 | 0 | 15 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.218× (z -15.2) |
| [[HOP62 (line)]] | alt | 209 | 2 | 11 | [[Harringtonine (drug)]] 5 µM 7.10× (z +13.2) | [[Dexamethasone (drug)]] 0.05 µM 0.224× (z -10.5) |
| [[SNU-423 (line)]] | alt | 964 | 1 | 11 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.4) | [[Auranofin (drug)]] 5 µM 0.290× (z -10.9) |
| [[SW1417 (line)]] | alt | 67.0 | 10 | 2 | [[Tucidinostat (drug)]] 5 µM 9.77× (z +30.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -11.3) |
| [[A549 (line)]] | wt | 78.1 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +34.8) | — |
| [[PANC-1 (line)]] | alt | 210 | 4 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -20.0) |
| [[BT-474 (line)]] | alt | 72.1 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.3× (z +27.7) | — |
| [[SW480 (line)]] | alt | 181 | 6 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.15× (z +11.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.296× (z -12.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 54.6 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.6× (z +39.2) | — |
| [[LoVo (line)]] | wt | 54.9 | 8 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.08× (z +19.6) | — |
| [[NCI-H1792 (line)]] | alt | 99.2 | 0 | 8 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.253× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 97.9 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +30.1) | — |
| [[RPMI-7951 (line)]] | alt | 269 | 2 | 6 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 5.66× (z +14.0) | [[Auranofin (drug)]] 5 µM 0.250× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 41.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 38.3× (z +31.9) | — |
| [[RKO (line)]] | wt | 126 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +17.8) | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -21.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 52.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +21.0) | — |
| [[C32 (line)]] | wt | 351 | 2 | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.46× (z +9.8) | [[Bortezomib (drug)]] 0.05 µM 0.354× (z -11.0) |
| [[H4 (line)]] | wt | 522 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +19.1) | [[Auranofin (drug)]] 5 µM 0.220× (z -11.3) |
| [[HepG2_C3A (line)]] | wt | 319 | 1 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.16× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.198× (z -15.8) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.354× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 82.8 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.25× (z +13.8) | — |
| [[SHP-77 (line)]] | alt | 609 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -16.5) |
| [[J82 (line)]] | alt | 176 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +21.2) | — |
| [[CHP-212 (line)]] | wt | 431 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -11.0) |
| [[HS-578T (line)]] | alt | 1,013 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +15.3) | — |
| [[HCT15 (line)]] | alt | 60.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 532 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.97× (z +13.3) | — |
| [[A-427 (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 24.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 20.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 35.7 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.4 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 16.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.98 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 21.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.6 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 40.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 20.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 14.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11352), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAD]] | +0.70 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[LRIG1]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[CGNL1]] | +0.65 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[CYRIA]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[DUSP10]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[TNFRSF9]] | +0.61 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[MARCKS]] | +0.60 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[CA8]] | +0.60 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[CCL2]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 | STRING 543 |
| [[IER3]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[CD82]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[MIR3142HG]] | +0.58 | +0.58 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMS1P23]] | -0.48 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[MOSMO]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[C8orf76]] | -0.46 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[THAP4]] | -0.46 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[ZFYVE9]] | -0.46 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[LTBR]] | -0.45 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIN2A]] | B | GRIN2A activity raises CADM1's level | lines that do not express GRIN2A (39) vs lines expressing it (11) | 7.29× lower at baseline in the lines without GRIN2A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000237268, ENSG00000234426, AMPH |
| [[ICAM1]] | B | ICAM1 activity raises CADM1's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 4.05× lower at baseline in the lines without ICAM1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[CA8]] | B | CA8 activity raises CADM1's level | lines that do not express CA8 (27) vs lines expressing it (23) | 3.78× lower at baseline in the lines without CA8 | 0.049 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[SNAP25]] | B | SNAP25 activity raises CADM1's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 4.19× lower at baseline in the lines without SNAP25 | 0.051 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3 |
| [[NINJ1]] | B | NINJ1 activity raises CADM1's level | lines that do not express NINJ1 (5) vs lines expressing it (45) | 3.42× lower at baseline in the lines without NINJ1 | 0.051 | ⚠ within organs, on part of the lines; also absent: FAM102A, ZMIZ1, MBNL2; maybe low, not absent |
| [[TNFRSF9]] | B | TNFRSF9 activity raises CADM1's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 3.59× lower at baseline in the lines without TNFRSF9 | 0.067 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2 |
| [[LIF-AS2]] | B | LIF-AS2 activity raises CADM1's level | lines that do not express LIF-AS2 (13) vs lines expressing it (37) | 2.14× lower at baseline in the lines without LIF-AS2 | 0.073 | ⚠ within organs, on part of the lines; also absent: STING1, CFB; maybe low, not absent |
| [[SHISAL1]] | B | SHISAL1 activity raises CADM1's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 4.03× lower at baseline in the lines without SHISAL1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11 |
| [[MARCKS]] | B | MARCKS activity raises CADM1's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 3.96× lower at baseline in the lines without MARCKS | 0.084 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |
| [[SOX5]] | C | SOX5 activity raises CADM1's level | lines that do not express SOX5 (24) vs lines expressing it (26) | 5.60× lower at baseline in the lines without SOX5 | 0.004 | ⚠ within organs, on part of the lines; also absent: CTHRC1, MOXD1, AK5; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESPN]] | B | CADM1 activity raises ESPN's level | lines that do not express CADM1 (18) vs lines expressing it (32) | 2.00× lower at baseline in the lines without CADM1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, BEND6, ARNT2 |
| [[NFKBIE]] | B | CADM1 activity raises NFKBIE's level | lines that do not express CADM1 (18) vs lines expressing it (32) | 1.51× lower at baseline in the lines without CADM1 | 0.041 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, BEND6, ARNT2 |
| [[ICAM1]] | B | CADM1 activity raises ICAM1's level | lines that do not express CADM1 (18) vs lines expressing it (32) | 3.31× lower at baseline in the lines without CADM1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, BEND6, ARNT2 |
| [[RRAD]] | B | CADM1 activity raises RRAD's level | lines that do not express CADM1 (18) vs lines expressing it (32) | 2.32× lower at baseline in the lines without CADM1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, BEND6, ARNT2 |
| [[CCL2]] | B | CADM1 activity raises CCL2's level | lines that do not express CADM1 (18) vs lines expressing it (32) | 2.97× lower at baseline in the lines without CADM1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, BEND6, ARNT2 |
| [[EYA1]] | B | CADM1 activity raises EYA1's level | lines that do not express CADM1 (18) vs lines expressing it (32) | 2.29× lower at baseline in the lines without CADM1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, BEND6, ARNT2 |
| [[BHLHE40]] | B | CADM1 activity raises BHLHE40's level | lines that do not express CADM1 (18) vs lines expressing it (32) | 1.43× lower at baseline in the lines without CADM1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, BEND6, ARNT2 |
| [[GRIK4]] | B | CADM1 activity raises GRIK4's level | lines that do not express CADM1 (18) vs lines expressing it (32) | 2.20× lower at baseline in the lines without CADM1 | 0.0998 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, BEND6, ARNT2 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.6, 1.4); signed map (45.3, 10.8). **Vector** length 122, 34.4% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +18.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +17.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +32.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +2.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.0 | -12.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.7 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.0 | -6.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.9 | -5.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.7 | -4.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.5 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | cell adhesion molecule 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:115,169,218-115,504,957 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NECL2, ST17, BL2, SYNCAM, IGSF4A, Necl-2, SYNCAM1, RA175; previously TSLC1, IGSF4 |
| Gene groups (HGNC) | V-set domain containing; C2-set domain containing; Nectins and nectin-like molecules |
| Hallmark sets | PEROXISOME, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 5 pathways, smallest: Nectin/Necl  trans heterodimerization; Adherens junctions interactions; Cell-cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY67](https://www.uniprot.org/uniprotkb/Q9BY67) (Cell adhesion molecule 1):

> Mediates homophilic cell-cell adhesion in a Ca(2+)-independent manner. Also mediates heterophilic cell-cell adhesion with CADM3 and NECTIN3 in a Ca(2+)-independent manner (By similarity). Interaction with CRTAM promotes natural killer (NK) cell cytotoxicity and interferon-gamma (IFN-gamma) secretion by CD8+ cells in vitro as well as NK cell-mediated rejection of tumors expressing CADM1 in vivo. In mast cells, may mediate attachment to and promote communication with nerves. CADM1, together with …

**Summary**, from NCBI Gene [23705](https://www.ncbi.nlm.nih.gov/gene/23705):

> Enables identical protein binding activity and signaling receptor binding activity. Involved in several processes, including cell recognition; positive regulation of cytokine production; and susceptibility to natural killer cell mediated cytotoxicity. Located in plasma membrane. Implicated in breast carcinoma and prostate cancer. Biomarker of cervix uteri carcinoma in situ. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:5951](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5951) · Entrez [23705](https://www.ncbi.nlm.nih.gov/gene/23705) · UniProt [Q9BY67](https://www.uniprot.org/uniprotkb/Q9BY67) · Ensembl [ENSG00000182985](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182985)

## Data

Gene col 11352: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11352); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11352, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11352]; `tensor/DDL_lfc|DDL_z.npy` [11352]; `embed/gene_vectors.npy` [11352]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11352 or target_col == 11352). Every well: [[CADM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CADM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
