---
symbol: "BLZF1"
type: "gene"
col: 3912
ensembl_id: "ENSG00000117475"
name: "basic leucine zipper nuclear factor 1"
location: "1q24.2"
module: 41
arm: "+"
pooled_cpm: 170.96
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 31
n_dd_up_clean: 1
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# BLZF1

*basic leucine zipper nuclear factor 1* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM: 1.21× (z +4.1, q 0.027, up in 21 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.01×; ⚠ cell-cycle shift, explains ~36% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 2.32×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.499× (z -10.0, q 1e-20, down in 42 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.690× (z -7.8, q 7e-13, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARF4]] (+0.72, fdr 7e-06), [[COQ10B]] (+0.71, fdr 7e-06), [[SPTY2D1]] (+0.68, fdr 7e-06); moves opposite to [[NCKAP1]] (-0.61, fdr 4e-05), [[LARP1]] (-0.60, fdr 1e-05), [[HDAC2]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[WFDC3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3912.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.01×; ⚠ cell-cycle shift, explains ~36% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 2.32×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.027 | 21/49 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3912.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.499×** | -10.0 | 1e-20 | 42/47 (NCI-H1573, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.531×** | -9.4 | 1e-18 | 39/49 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.553×** | -8.5 | 4e-15 | 35/44 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.690×** | -7.8 | 7e-13 | 39/48 (RPMI-7951, CFPAC-1, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.627×** | -7.0 | 4e-10 | 37/48 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.643×** | -6.1 | 1e-07 | 36/45 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.756×** | -5.9 | 3e-07 | 27/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.689×** | -5.3 | 7e-06 | 35/48 (NCI-H1573, C32, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.702×** | -5.3 | 9e-06 | 31/48 (CFPAC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.707×** | -5.1 | 1e-05 | 36/49 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.703×** | -5.0 | 2e-05 | 32/48 (NCI-H1792, J82, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.697×** | -5.0 | 3e-05 | 35/48 (C32, RKO, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.767×** | -4.8 | 6e-05 | 28/48 (AsPC-1, RKO, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.730×** | -4.7 | 1e-04 | 30/49 (C32, NCI-H1573, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.732×** | -4.6 | 1e-04 | 38/48 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.800×** | -4.6 | 1e-04 | 25/48 (C32, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.742×** | -4.4 | 3e-04 | 32/48 (CFPAC-1, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.740×** | -4.3 | 5e-04 | 27/47 (C32, NCI-H1573, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.754×** | -4.2 | 8e-04 | 27/48 (HOP62, LOX-IMVI, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3912. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 399 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -14.2) |
| [[NCI-H1573 (line)]] | alt | 377 | 0 | 7 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.205× (z -13.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.461× (z -9.6) |
| [[C32 (line)]] | wt | 90.6 | 0 | 6 | — | [[Binimetinib (drug)]] 0.5 µM 0.408× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 339 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.434× (z -9.7) |
| [[RKO (line)]] | wt | 228 | 0 | 5 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.314× (z -9.9) ⚠ toxic · without an alert: [[Trametinib (drug)]] 0.5 µM 0.431× (z -9.4) |
| [[A498 (line)]] | wt | 241 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -13.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.603× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 231 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.372× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.412× (z -8.6) |
| [[CHP-212 (line)]] | wt | 163 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.183× (z -11.9) ⚠ toxic · without an alert: [[DT-061 (drug)]] 5 µM 0.0682× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 103 | 2 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.3) ⚠ cell-cycle shift, explains ~36% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.298× (z -12.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 176 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -12.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 168 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.548× (z -8.5) |
| [[HCT15 (line)]] | alt | 226 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -12.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 141 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.377× (z -12.2) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 151 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.526× (z -8.6) |
| [[J82 (line)]] | alt | 170 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.293× (z -12.9) ⚠ toxic |
| [[LoVo (line)]] | wt | 132 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.392× (z -10.6) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 209 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 290 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -10.4) |
| [[A-427 (line)]] | wt | 148 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -9.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[H4 (line)]] | wt | 206 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -8.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 122 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.581× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 100.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 131 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.405× (z -9.4) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 210 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -9.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 187 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.548× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 167 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.421× (z -10.4) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.344× (z -10.5) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 91.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.141× (z -8.7) ⚠ transcription drop |
| [[AN3 CA (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 94.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 193 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 96.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 86.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3912), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARF4]] | +0.72 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[COQ10B]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SAP30BP]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[RABGEF1]] | +0.67 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[ATP6V1D]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[GTF2B]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[YIPF5]] | +0.64 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[TAF13]] | +0.64 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[DIS3]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[GP6-AS1]] | +0.63 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[RAB5A]] | +0.63 | +0.66 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCKAP1]] | -0.61 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[LARP1]] | -0.60 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[HDAC2]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[TNPO1]] | -0.57 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[VAPA]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[KCTD3]] | -0.55 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[USP24]] | -0.54 | -0.60 / -0.38 | both halves | 7e-05 |  |
| [[KDM1A]] | -0.54 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[ENAH]] | -0.53 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[RAD23B]] | -0.53 | -0.24 / -0.58 | both halves | 5e-04 |  |
| [[FECH]] | -0.53 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[NDUFAF5]] | -0.53 | -0.44 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WFDC3]] | B | WFDC3 activity raises BLZF1's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 1.42× lower at baseline in the lines without WFDC3 | 0.074 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[PDE2A]] | C | PDE2A activity raises BLZF1's level | lines that do not express PDE2A (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without PDE2A | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GOLGA8N, TMEFF1, LUCAT1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.539). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (17.6, -25.8); signed map (7.6, 16.4). **Vector** length 152, 56.0% of its response variance represented; |z| ≥ 3 in 1,414 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.7 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | -2.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | +3.3 | +1.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | +3.3 | +2.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.8 | +2.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -11.3 | -10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.6 | -8.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.6 | -7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.2 | -7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.7 | -9.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.6 | -5.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -5.9 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.8 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | basic leucine zipper nuclear factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:169,367,970-169,396,540 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JEM-1 |
| Reactome | 5 pathways, smallest: Golgi Cisternae Pericentriolar Stack Reorganization; Mitotic Prophase; M Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2G9](https://www.uniprot.org/uniprotkb/Q9H2G9) (Golgin-45):

> Required for normal Golgi structure and for protein transport from the endoplasmic reticulum (ER) through the Golgi apparatus to the cell surface.

**Summary**, from NCBI Gene [8548](https://www.ncbi.nlm.nih.gov/gene/8548):

> Enables ubiquitin protein ligase binding activity. Acts upstream of or within Golgi organization and Golgi to plasma membrane protein transport. Located in Golgi apparatus and nucleoplasm. Biomarker of hepatocellular carcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1065](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1065) · Entrez [8548](https://www.ncbi.nlm.nih.gov/gene/8548) · UniProt [Q9H2G9](https://www.uniprot.org/uniprotkb/Q9H2G9) · Ensembl [ENSG00000117475](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117475)

## Data

Gene col 3912: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3912); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3912, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3912]; `tensor/DDL_lfc|DDL_z.npy` [3912]; `embed/gene_vectors.npy` [3912]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3912 or target_col == 3912). Every well: [[BLZF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLZF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
