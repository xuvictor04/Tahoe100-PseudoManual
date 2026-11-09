---
symbol: "CNTNAP1"
type: "gene"
col: 2995
ensembl_id: "ENSG00000108797"
name: "contactin associated protein 1"
location: "17q21.2"
module: 14
arm: "+"
pooled_cpm: 18.1
n_lines_expressing: 46
n_dd_up: 14
n_dd_down: 25
n_dd_up_clean: 14
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CNTNAP1

*contactin associated protein 1* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.77× (z +7.2, q 4e-10, up in 31 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.489× (z -9.4, q 2e-18, down in 37 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIXDC1]] (+0.63, fdr 7e-06), [[PHF21A]] (+0.60, fdr 1e-05), [[SLC39A1]] (+0.58, fdr 1e-05); moves opposite to [[ITGA2]] (-0.58, fdr 1e-05), [[ARHGAP27P1-BPTFP1-KPNA2P3]] (-0.55, fdr 1e-05), [[PTPRE]] (-0.53, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 9 go from it, the strongest it → [[TMEM39B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2995.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.77×** | +7.2 | 4e-10 | 31/42 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **1.54×** | +6.5 | 2e-08 | 29/44 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.55×** | +6.3 | 6e-08 | 27/44 (MIA PaCa-2, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.58×** | +5.8 | 1e-06 | 27/43 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +5.6 | 2e-06 | 21/44 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.35×** | +5.4 | 7e-06 | 20/44 (NCI-H2347, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.32×** | +5.1 | 3e-05 | 22/44 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.39×** | +5.0 | 5e-05 | 23/44 (MIA PaCa-2, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.48×** | +4.9 | 7e-05 | 24/44 (NCI-H2347, MIA PaCa-2, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **1.28×** | +4.6 | 3e-04 | 20/44 (NCI-H2347, NCI-H23, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.39×** | +4.3 | 7e-04 | 21/43 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.002 | 16/44 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.39×** | +4.0 | 0.003 | 16/43 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.040 | 10/44 (NCI-H1792, SNU-423, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2995.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.489×** | -9.4 | 2e-18 | 37/43 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.554×** | -7.8 | 2e-12 | 26/44 (LOX-IMVI, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.559×** | -7.7 | 3e-12 | 29/43 (LOX-IMVI, HCT15, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.560×** | -7.7 | 3e-12 | 32/43 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.596×** | -6.8 | 1e-09 | 26/41 (RKO, C32, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.596×** | -6.6 | 5e-09 | 22/39 (HCT15, SNU-423, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.603×** | -6.3 | 2e-08 | 26/42 (C32, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.613×** | -5.9 | 3e-07 | 26/44 (HCT15, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.652×** | -5.7 | 1e-06 | 25/43 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.638×** | -5.4 | 4e-06 | 25/42 (LOX-IMVI, HOP62, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.684×** | -4.8 | 7e-05 | 23/39 (C-33 A, SW48, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.779×** | -4.7 | 1e-04 | 22/44 (RKO, HCT15, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.702×** | -4.7 | 1e-04 | 15/40 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.711×** | -4.3 | 6e-04 | 18/43 (C32, PANC-1, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.723×** | -4.3 | 7e-04 | 19/43 (LOX-IMVI, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.726×** | -4.2 | 8e-04 | 17/44 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.706×** | -4.2 | 9e-04 | 18/41 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.739×** | -3.9 | 0.004 | 12/43 (CFPAC-1, NCI-H2030, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2995. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 1 (1 ⚠) | 3 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.02× (z +15.6) ⚠ position not correctable | [[Auranofin (drug)]] 5 µM 0.190× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 17.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -11.8) |
| [[C32 (line)]] | wt | 23.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0883× (z -13.1) |
| [[HCT15 (line)]] | alt | 47.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0765× (z -14.9) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 26.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.241× (z -9.6) |
| [[PANC-1 (line)]] | alt | 23.2 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.313× (z -9.4) |
| [[SNU-423 (line)]] | alt | 30.7 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.113× (z -12.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.209× (z -9.5) |
| [[CHP-212 (line)]] | wt | 79.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 22.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0806× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 11.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.104× (z -9.1) ⚠ toxic; unreliable plate only |
| [[Hs 766T (line)]] | wt | 18.7 | 0 | 1 | — | [[ULK-101 (drug)]] 0.05 µM 0.179× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 40.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.217× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.124× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 39.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -15.1) |
| [[RPMI-7951 (line)]] | alt | 25.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -12.9) |
| [[A-172 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2995), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIXDC1]] | +0.63 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[PHF21A]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[SLC39A1]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[ZBTB25]] | +0.55 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[COL5A2]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[CFAP418]] | +0.55 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[YY1AP1]] | +0.54 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[PLPP1]] | +0.54 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[AMOT]] | +0.53 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ATP23]] | +0.53 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[PER1]] | +0.52 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ECH1]] | +0.52 | +0.45 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA2]] | -0.58 | -0.53 / -0.54 | both halves | 1e-05 | pathway: L1CAM interactions |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | -0.55 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[PTPRE]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[CDCP1]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ASAP2]] | -0.50 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[DCBLD2]] | -0.50 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[CORO2B]] | -0.50 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[ATP8B5P-1]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[KPNA2P3]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[S100A16]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[BLZF2P]] | -0.49 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[EFL1]] | -0.48 | -0.43 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers CNTNAP1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[RBMS3]] | B | RBMS3 activity raises CNTNAP1's level | lines that do not express RBMS3 (19) vs lines expressing it (31) | 2.22× lower at baseline in the lines without RBMS3 | 0.029 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472 |
| [[SMAD9]] | B | SMAD9 activity raises CNTNAP1's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 2.57× lower at baseline in the lines without SMAD9 | 0.051 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[DUSP4]] | B | DUSP4 activity lowers CNTNAP1's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 1.76× higher at baseline in the lines without DUSP4 | 0.073 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[MAP2K2]] | B | MAP2K2 activity lowers CNTNAP1's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM39B]] | C | CNTNAP1 activity raises TMEM39B's level | lines that do not express CNTNAP1 (4) vs lines expressing it (46) | 2.12× lower at baseline in the lines without CNTNAP1 | 0.006 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZCCHC24, KIF17, SLC29A4 |
| [[C3orf18]] | C | CNTNAP1 activity raises C3orf18's level | lines that do not express CNTNAP1 (4) vs lines expressing it (46) | 1.98× lower at baseline in the lines without CNTNAP1 | 0.028 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZCCHC24, KIF17, SLC29A4 |
| [[CSF1]] | C | CNTNAP1 activity raises CSF1's level | lines that do not express CNTNAP1 (4) vs lines expressing it (46) | 3.71× lower at baseline in the lines without CNTNAP1 | 0.055 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZCCHC24, KIF17, SLC29A4 |
| [[RBMS3]] | C | CNTNAP1 activity raises RBMS3's level | lines that do not express CNTNAP1 (4) vs lines expressing it (46) | 6.53× lower at baseline in the lines without CNTNAP1 | 0.058 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZCCHC24, KIF17, SLC29A4 |
| [[PLPP1]] | C | CNTNAP1 activity raises PLPP1's level | lines that do not express CNTNAP1 (4) vs lines expressing it (46) | 2.70× lower at baseline in the lines without CNTNAP1 | 0.071 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZCCHC24, KIF17, SLC29A4 |
| cells under [[Procainamide (hydrochloride) (drug)]] 0.5 µM | C | CNTNAP1 activity lowers the cells' numbers under Procainamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express CNTNAP1 (4) vs lines expressing it (44) | the lines without CNTNAP1: 1.27× the cells of the other lines | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZCCHC24, KIF17, SLC29A4 |
| [[BCOR]] | C | CNTNAP1 activity raises BCOR's level | lines that do not express CNTNAP1 (4) vs lines expressing it (46) | 1.61× lower at baseline in the lines without CNTNAP1 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZCCHC24, KIF17, SLC29A4 |
| [[SLC44A2]] | C | CNTNAP1 activity raises SLC44A2's level | lines that do not express CNTNAP1 (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without CNTNAP1 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZCCHC24, KIF17, SLC29A4 |
| [[DIXDC1]] | C | CNTNAP1 activity raises DIXDC1's level | lines that do not express CNTNAP1 (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without CNTNAP1 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZCCHC24, KIF17, SLC29A4 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.435). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.0, -8.4); signed map (-6.7, 7.7). **Vector** length 104, 25.0% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +5.1 | +7.2 |
|  | [[Trametinib (drug)]] 5 µM |  | +4.8 | +6.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.7 | +6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.3 | +5.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.1 | +5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +4.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.5 | -9.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.7 | -6.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.2 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -5.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | contactin associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,682,531-42,699,993 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p190, Caspr, CNTNAP; previously NRXN4 |
| Gene groups (HGNC) | Contactin associated protein family |
| Reactome | 4 pathways, smallest: Neurofascin interactions; L1CAM interactions; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [P78357](https://www.uniprot.org/uniprotkb/P78357) (Contactin-associated protein 1):

> Required, with CNTNAP2, for radial and longitudinal organization of myelinated axons. Plays a role in the formation of functional distinct domains critical for saltatory conduction of nerve impulses in myelinated nerve fibers. Demarcates the paranodal region of the axo-glial junction. In association with contactin involved in the signaling between axons and myelinating glial cells.

**Summary**, from NCBI Gene [8506](https://www.ncbi.nlm.nih.gov/gene/8506):

> The gene product was initially identified as a 190-kD protein associated with the contactin-PTPRZ1 complex. The 1,384-amino acid protein, also designated p190 or CASPR for 'contactin-associated protein,' includes an extracellular domain with several putative protein-protein interaction domains, a putative transmembrane domain, and a 74-amino acid cytoplasmic domain. Northern blot analysis showed that the gene is transcribed predominantly in brain as a transcript of 6.2 kb, with weak expression …

**Accessions** — [HGNC:8011](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8011) · Entrez [8506](https://www.ncbi.nlm.nih.gov/gene/8506) · UniProt [P78357](https://www.uniprot.org/uniprotkb/P78357) · Ensembl [ENSG00000108797](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108797)

## Data

Gene col 2995: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2995); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2995, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2995]; `tensor/DDL_lfc|DDL_z.npy` [2995]; `embed/gene_vectors.npy` [2995]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2995 or target_col == 2995). Every well: [[CNTNAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNTNAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
