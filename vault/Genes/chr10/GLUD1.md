---
symbol: "GLUD1"
type: "gene"
col: 7303
ensembl_id: "ENSG00000148672"
name: "glutamate dehydrogenase 1"
location: "10q23.2"
module: 11
arm: "-"
pooled_cpm: 124.28
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# GLUD1

*glutamate dehydrogenase 1* — 10q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +7.5, q 3e-11, up in 31 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.745× (z -5.8, q 3e-06, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABHD12]] (+0.55, fdr 2e-05), [[PRDX6]] (+0.54, fdr 3e-05), [[EPB41L4B]] (+0.53, fdr 3e-05); moves opposite to [[NCOA5]] (-0.60, fdr 9e-06), [[FAF2]] (-0.59, fdr 1e-05), [[ABCF1]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EPB41L4B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7303.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +7.5 | 3e-11 | 31/49 (NCI-H460, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +7.3 | 7e-11 | 35/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +5.6 | 3e-06 | 27/48 (NCI-H1792, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +5.5 | 7e-06 | 28/49 (LoVo, A549, …) | two highest doses | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +5.1 | 4e-05 | 25/48 (SW480, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +4.5 | 6e-04 | 25/48 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.24×** | +4.2 | 0.002 | 22/48 (NCI-H1792, LS 180, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.23×** | +4.0 | 0.004 | 21/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.012 | 23/48 (HCT15, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.20×** | +3.6 | 0.019 | 19/48 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change | **1.21×** | +3.5 | 0.020 | 21/43 (A549, SHP-77, …) | two highest doses | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.1 | 0.092 | 14/38 (Panc 03.27, BT-474, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7303.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.745×** | -5.8 | 3e-06 | 26/48 (NCI-H1573, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.778×** | -4.8 | 3e-04 | 25/47 (SW 1271, Hs 766T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.779×** | -4.8 | 3e-04 | 26/47 (HOP62, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.788×** | -4.7 | 3e-04 | 25/48 (Hs 766T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.801×** | -4.2 | 0.003 | 25/48 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.810×** | -4.2 | 0.003 | 23/48 (AsPC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -4.1 | 0.003 | 25/48 (HepG2/C3A, Hs 766T, …) | two highest doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.817×** | -4.0 | 0.004 | 22/48 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 5 µM |  | 0.874× | -3.8 | 0.010 | 18/48 (CFPAC-1, NCI-H1792, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.829×** | -3.7 | 0.011 | 23/48 (RPMI-7951, NCI-H1792, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.874× | -3.7 | 0.013 | 14/49 (Hs 766T, SW480, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.840× | -3.5 | 0.026 | 20/49 (A498, SW1417, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.853× | -3.2 | 0.069 | 16/47 (Hs 766T, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7303. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 167 | 21 (2 ⚠) | 1 (1 ⚠) | [[Binimetinib (drug)]] 5 µM 6.22× (z +18.5) | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 96.4 | 3 (3 ⚠) | 3 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.22× (z +15.1) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.497× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 102 | 6 (5 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.91× (z +13.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 70.6 | 1 (1 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.346× (z -11.5) |
| [[SW1417 (line)]] | alt | 140 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +29.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.57× (z +16.3) | — |
| [[SW480 (line)]] | alt | 168 | 5 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.23× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.02× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 209 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.264× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.344× (z -10.0) |
| [[HOP62 (line)]] | alt | 148 | 1 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.23× (z +9.7) ⚠ cell-cycle shift, explains ~12% of this change | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.504× (z -8.5) |
| [[Hs 766T (line)]] | wt | 366 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.344× (z -10.4) |
| [[LS 180 (line)]] | wt | 90.6 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.53× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 117 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.16× (z +12.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 130 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.472× (z -8.7) |
| [[A549 (line)]] | wt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +9.3) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 72.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 78.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 193 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.373× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 107 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.367× (z -9.1) |
| [[A498 (line)]] | wt | 168 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 70.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 96.9 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.82× (z +8.5) ⚠ cell-cycle shift, explains ~12% of this change | — |
| [[HCT15 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 147 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.84× (z +8.6) ⚠ cell-cycle shift, explains ~12% of this change | — |
| [[Panc 03.27 (line)]] | alt | 129 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[PANC-1 (line)]] | alt | 123 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.80× (z +8.9) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.357× (z -10.1) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 52.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change | — |
| [[SNU-1 (line)]] | wt | 76.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 87.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 115 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 108 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 152 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7303), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*26 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD12]] | +0.55 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[PRDX6]] | +0.54 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[EPB41L4B]] | +0.53 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[SRD5A1]] | +0.53 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[ATP11B]] | +0.51 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[CPD]] | +0.51 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[TFEB]] | +0.51 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[RREB1]] | +0.50 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[SETD3]] | +0.50 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[ATP1A1]] | +0.48 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[NDFIP1]] | +0.48 | +0.67 / +0.35 | both halves | 1e-04 |  |
| [[LPCAT4]] | +0.48 | +0.68 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*74 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCOA5]] | -0.60 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[FAF2]] | -0.59 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ABCF1]] | -0.57 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[CWC22]] | -0.55 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[ZNF140]] | -0.55 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[ZNF480]] | -0.53 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[ZNF75A]] | -0.52 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[SFSWAP]] | -0.52 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[JPX]] | -0.52 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[RPP14]] | -0.52 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[ZNF268]] | -0.52 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[LLPH]] | -0.52 | -0.60 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPB41L4B]] | B | EPB41L4B activity lowers GLUD1's level | lines that do not express EPB41L4B (9) vs lines expressing it (41) | 1.07× higher at baseline in the lines without EPB41L4B | 0.089 | ⚠ within organs, on part of the lines; also absent: MYRF, GRTP1, MARVELD2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.468). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-42.4, 2.8); signed map (-21.5, 18.6). **Vector** length 110, 29.5% of its response variance represented; |z| ≥ 3 in 1,258 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +7.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.4 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +5.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.1 | +2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.4 | +0.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.3 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.0 | -4.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -2.4 |
|  | [[Docetaxel (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | -2.6 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | glutamate dehydrogenase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.2 — chr10:87,050,202-87,094,843 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GDH, GDH1, hGDH1; previously GLUD |
| Gene groups (HGNC) | Glutamate dehydrogenase family |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 6 pathways, smallest: Glutamate and glutamine metabolism; Transcriptional activation of mitochondrial biogenesis; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P00367](https://www.uniprot.org/uniprotkb/P00367) (Glutamate dehydrogenase 1, mitochondrial):

> Mitochondrial glutamate dehydrogenase that catalyzes the conversion of L-glutamate into alpha-ketoglutarate. Plays a key role in glutamine anaplerosis by producing alpha-ketoglutarate, an important intermediate in the tricarboxylic acid cycle. Plays a role in insulin homeostasis. May be involved in learning and memory reactions by increasing the turnover of the excitatory neurotransmitter glutamate (By similarity).

**Summary**, from NCBI Gene [2746](https://www.ncbi.nlm.nih.gov/gene/2746):

> This gene encodes glutamate dehydrogenase, which is a mitochondrial matrix enzyme that catalyzes the oxidative deamination of glutamate to alpha-ketoglutarate and ammonia. This enzyme has an important role in regulating amino acid-induced insulin secretion. It is allosterically activated by ADP and inhibited by GTP and ATP. Activating mutations in this gene are a common cause of congenital hyperinsulinism. Alternative splicing of this gene results in multiple transcript variants. The related …

**Accessions** — [HGNC:4335](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4335) · Entrez [2746](https://www.ncbi.nlm.nih.gov/gene/2746) · UniProt [P00367](https://www.uniprot.org/uniprotkb/P00367) · Ensembl [ENSG00000148672](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148672)

## Data

Gene col 7303: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7303); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7303, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7303]; `tensor/DDL_lfc|DDL_z.npy` [7303]; `embed/gene_vectors.npy` [7303]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7303 or target_col == 7303). Every well: [[GLUD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLUD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
