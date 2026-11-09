---
symbol: "FAM3C"
type: "gene"
col: 12307
ensembl_id: "ENSG00000196937"
name: "FAM3 metabolism regulating signaling molecule C"
location: "7q31.31"
module: 34
arm: "+"
pooled_cpm: 162.22
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 26
n_dd_up_clean: 7
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# FAM3C

*FAM3 metabolism regulating signaling molecule C* — 7q31.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.33× (z +6.2, q 2e-07, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.600× (z -11.0, q 1e-25, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM3C2P]] (+0.67, fdr 1e-05), [[ITGB5]] (+0.65, fdr 8e-06), [[ETV5]] (+0.60, fdr 2e-05); moves opposite to [[ZCCHC8]] (-0.56, fdr 2e-05), [[HSPB1]] (-0.50, fdr 3e-05), [[GAS2]] (-0.49, fdr 2e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CNTNAP3C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12307.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +6.2 | 2e-07 | 32/47 (RPMI-7951, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +5.8 | 2e-06 | 37/48 (RPMI-7951, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +4.9 | 2e-04 | 32/47 (PANC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 0.004 | 29/47 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +4.0 | 0.006 | 22/47 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.006 | 28/47 (BT-474, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +3.9 | 0.009 | 30/47 (Panc 03.27, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.61×** | +3.8 | 0.009 | 28/47 (LS 180, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.22× | +3.1 | 0.14 | 22/47 (BT-474, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[4EGI-1 (drug)]] 0.5 µM |  | 1.32× | +3.0 | 0.14 | 18/47 (Hs 766T, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12307.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -11.0 | 1e-25 | 39/48 (Panc 03.27, SW1417, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.684×** | -6.1 | 3e-07 | 36/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.718×** | -6.0 | 3e-07 | 34/47 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.679×** | -5.9 | 5e-07 | 36/47 (SW48, Panc 03.27, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.716×** | -5.9 | 5e-07 | 34/49 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.673×** | -5.8 | 6e-07 | 37/47 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.735×** | -5.6 | 2e-06 | 36/47 (AsPC-1, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.698×** | -5.5 | 3e-06 | 33/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.724×** | -4.9 | 5e-05 | 29/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.731×** | -4.8 | 1e-04 | 28/47 (AsPC-1, HEC-1-A, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.809×** | -4.4 | 5e-04 | 26/48 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.734×** | -4.4 | 6e-04 | 25/45 (NCI-H23, SW1417, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.730×** | -4.3 | 6e-04 | 31/47 (NCI-H2347, C32, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.587×** | -4.3 | 9e-04 | 28/44 (AsPC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.759×** | -4.2 | 1e-03 | 25/47 (SW48, NCI-H2347, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.763×** | -4.0 | 0.002 | 25/47 (SW48, SW1417, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.764×** | -3.7 | 0.006 | 27/47 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12307. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 473 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -18.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -15.1) |
| [[Panc 03.27 (line)]] | alt | 761 | 0 | 12 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -21.4) |
| [[NCI-H2347 (line)]] | alt | 492 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -11.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -10.9) |
| [[SW48 (line)]] | wt | 383 | 0 | 10 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -18.0) |
| [[SW1417 (line)]] | alt | 434 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -18.7) |
| [[CFPAC-1 (line)]] | alt | 459 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.416× (z -10.4) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.446× (z -9.5) |
| [[BT-474 (line)]] | alt | 74.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.9) ⚠ cell-cycle shift, explains ~32% of this change | [[Dinaciclib (drug)]] 5 µM 0.167× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 168 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -14.2) |
| [[NCI-H1792 (line)]] | alt | 225 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -15.5) |
| [[NCI-H23 (line)]] | alt | 97.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -9.4) |
| [[PANC-1 (line)]] | alt | 163 | 2 | 1 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.57× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -15.9) |
| [[SNU-423 (line)]] | alt | 159 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -10.2) |
| [[SW480 (line)]] | alt | 92.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.462× (z -9.1) |
| [[A-427 (line)]] | wt | 131 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.472× (z -9.3) ⚠ cell-cycle shift, explains ~10% of this change |
| [[A498 (line)]] | wt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 75.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -9.5) |
| [[HOP62 (line)]] | alt | 80.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -8.6) |
| [[HS-578T (line)]] | alt | 111 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.636× (z -14.4) ⚠ position not correctable |
| [[RKO (line)]] | wt | 153 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 149 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.3) |
| [[SW 1088 (line)]] | alt | 186 | 0 | 1 | — | [[Bestatin (hydrochloride) (drug)]] 0.05 µM 0.133× (z -8.8) |
| [[SW 1271 (line)]] | alt | 260 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -8.7) |
| [[SW 900 (line)]] | alt | 262 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -11.3) |
| [[A-172 (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 191 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.8 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 161 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 63.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 109 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 105 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 77.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 81.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12307), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM3C2P]] | +0.67 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[ITGB5]] | +0.65 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[ETV5]] | +0.60 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[ITGA2]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[SLC9A7]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CDCP1]] | +0.56 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[EML4]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[BAIAP3]] | +0.56 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[ITGA3]] | +0.55 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[SYN1]] | +0.55 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[OSBPL3]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[KRT15]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC8]] | -0.56 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[HSPB1]] | -0.50 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[GAS2]] | -0.49 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[IRAK4]] | -0.49 | -0.58 / -0.29 | both halves | 2e-04 |  |
| [[GANC]] | -0.49 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[TNNI3K]] | -0.48 | -0.44 / -0.37 | both halves | 9e-05 |  |
| [[LINC00278]] | -0.48 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[DGLUCY]] | -0.48 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[ZRANB2-DT]] | -0.48 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[GPATCH3]] | -0.47 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[ARFGAP2]] | -0.47 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[GNGT1]] | -0.47 | -0.46 / -0.31 | both halves | 2e-04 | pathway: Platelet activation, signaling and aggregation |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNTNAP3C]] | B | CNTNAP3C activity raises FAM3C's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without CNTNAP3C | 1e-03 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA |
| [[ROR1]] | B | ROR1 activity raises FAM3C's level | lines that do not express ROR1 (14) vs lines expressing it (36) | 1.94× lower at baseline in the lines without ROR1 | 0.010 | ⚠ within organs, on part of the lines |
| [[FAM3C2P]] | B | FAM3C2P activity raises FAM3C's level | lines that do not express FAM3C2P (6) vs lines expressing it (44) | 2.82× lower at baseline in the lines without FAM3C2P | 0.012 | ⚠ within organs, on part of the lines; also absent: CMTM7, ARHGAP10, IQSEC2; maybe low, not absent |
| [[CNTNAP3C]] | B | CNTNAP3C activity strengthens FAM3C's drug response | lines that do not express CNTNAP3C (22) vs lines expressing it (27) | the lines without CNTNAP3C respond 0.85× as strongly (z diff +0.55); strongest at Idarubicin (hydrochloride) 5 µM: 0.70x vs 0.49x (z diff +3.6) | 0.039 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA; target measured in part of the lines; both ways; artifact flags |
| [[WNT7B]] | B | WNT7B activity raises FAM3C's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.56× lower at baseline in the lines without WNT7B | 0.073 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[WNT7A]] | B | WNT7A activity raises FAM3C's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.94× lower at baseline in the lines without WNT7A | 0.074 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[MAP2K1]] | B | MAP2K1 activity raises FAM3C's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[TTTY14]] | B | TTTY14 activity lowers FAM3C's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 1.89× higher at baseline in the lines without TTTY14 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.5, 4.7); signed map (6.5, 47.5). **Vector** length 122, 37.8% of its response variance represented; |z| ≥ 3 in 1,364 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +1.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | -0.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.3 | +2.7 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -7.0 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -7.0 | -4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.0 | -6.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.9 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.7 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.3 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | FAM3 metabolism regulating signaling molecule C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.31 — chr7:121,348,878-121,396,364 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GS3876, ILEI |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92520](https://www.uniprot.org/uniprotkb/Q92520) (Protein FAM3C):

> May be involved in retinal laminar formation. Promotes epithelial to mesenchymal transition.

**Summary**, from NCBI Gene [10447](https://www.ncbi.nlm.nih.gov/gene/10447):

> This gene is a member of the family with sequence similarity 3 (FAM3) family and encodes a secreted protein with a GG domain. A change in expression of this protein has been noted in pancreatic cancer-derived cells. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:18664](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18664) · Entrez [10447](https://www.ncbi.nlm.nih.gov/gene/10447) · UniProt [Q92520](https://www.uniprot.org/uniprotkb/Q92520) · Ensembl [ENSG00000196937](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196937)

## Data

Gene col 12307: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12307); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12307, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12307]; `tensor/DDL_lfc|DDL_z.npy` [12307]; `embed/gene_vectors.npy` [12307]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12307 or target_col == 12307). Every well: [[FAM3C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM3C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
