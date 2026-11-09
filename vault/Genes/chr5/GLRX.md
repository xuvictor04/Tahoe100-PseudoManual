---
symbol: "GLRX"
type: "gene"
col: 10357
ensembl_id: "ENSG00000173221"
name: "glutaredoxin"
location: "5q15"
module: 113
arm: "+"
pooled_cpm: 71.98
n_lines_expressing: 40
n_dd_up: 1
n_dd_down: 27
n_dd_up_clean: 1
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 6
direction_downstream: 20
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# GLRX

*glutaredoxin* — 5q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.40× (z +5.1, q 2e-04, up in 29 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Triamcinolone (drug)]] 5 µM in 2 lines (AsPC-1 2.75×, Hs 766T 2.39×); [[Auranofin (drug)]] 5 µM in 1 line (LS 180 3.21×).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.358× (z -15.8, q 0e+00, down in 36 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT1X]] (+0.68, fdr 7e-06), [[ANGPTL4]] (+0.64, fdr 7e-06), [[SLC2A3]] (+0.64, fdr 7e-06); moves opposite to [[ADGRA3]] (-0.56, fdr 2e-05), [[ARHGAP42]] (-0.55, fdr 1e-05), [[GALNT7]] (-0.54, fdr 1e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TREM1]] → it (grade B ⚠); 20 go from it, the strongest it → [[ZNF236]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10357.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Triamcinolone (drug)]] 5 µM in 2 lines (AsPC-1 2.75×, Hs 766T 2.39×); [[Auranofin (drug)]] 5 µM in 1 line (LS 180 3.21×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +5.1 | 2e-04 | 29/38 (KATO III, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.37× | +3.4 | 0.12 | 19/38 (LS 180, LoVo, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.39× | +3.4 | 0.12 | 17/39 (AsPC-1, A549, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.37× | +3.3 | 0.12 | 19/38 (AsPC-1, SNU-423, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.24× | +3.3 | 0.12 | 19/38 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 1.33× | +3.1 | 0.20 | 18/38 (AsPC-1, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10357.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.358×** | -15.8 | 0e+00 | 36/37 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.376×** | -10.2 | 5e-22 | 36/38 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.391×** | -10.2 | 5e-22 | 34/37 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.399×** | -10.0 | 3e-21 | 35/38 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.499×** | -7.5 | 5e-12 | 29/38 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.518×** | -7.1 | 9e-11 | 33/38 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.524×** | -7.0 | 2e-10 | 34/38 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.590×** | -5.4 | 6e-06 | 23/40 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.610×** | -5.2 | 2e-05 | 27/37 (NCI-H460, RKO, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.413×** | -5.0 | 3e-05 | 29/38 (RKO, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.637×** | -4.7 | 1e-04 | 25/37 (HS-578T, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.668×** | -4.4 | 6e-04 | 26/37 (RKO, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.676×** | -4.3 | 9e-04 | 21/38 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.664×** | -4.1 | 0.002 | 25/38 (RKO, NCI-H460, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.697×** | -3.9 | 0.003 | 21/38 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.749×** | -3.9 | 0.003 | 21/38 (NCI-H460, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.779×** | -3.8 | 0.006 | 22/38 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.538×** | -3.5 | 0.014 | 22/37 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10357. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 198 | 0 | 22 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -27.1) |
| [[RKO (line)]] | wt | 315 | 0 | 20 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0851× (z -23.1) |
| [[HepG2_C3A (line)]] | wt | 157 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -22.4) |
| [[H4 (line)]] | wt | 149 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0628× (z -27.6) |
| [[HS-578T (line)]] | alt | 115 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -17.0) |
| [[C32 (line)]] | wt | 102 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 215 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -14.8) |
| [[HOP62 (line)]] | alt | 144 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -14.7) |
| [[J82 (line)]] | alt | 128 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.7) |
| [[LS 180 (line)]] | wt | 54.7 | 1 | 2 | [[Auranofin (drug)]] 5 µM 3.21× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -9.9) |
| [[A549 (line)]] | wt | 80.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -17.7) |
| [[AsPC-1 (line)]] | alt | 35.2 | 1 | 1 | [[Triamcinolone (drug)]] 5 µM 2.75× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -8.6) |
| [[HCT15 (line)]] | alt | 57.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -11.4) |
| [[Hs 766T (line)]] | wt | 77.8 | 1 | 1 | [[Triamcinolone (drug)]] 5 µM 2.39× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -17.6) |
| [[hTERT-HPNE (line)]] | wt | 129 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 136 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -19.7) |
| [[RPMI-7951 (line)]] | alt | 64.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change |
| [[SHP-77 (line)]] | alt | 35.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -14.6) |
| [[COLO 205 (line)]] | alt | 64.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -10.0) |
| [[HT-29 (line)]] | alt | 37.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.6) |
| [[KATO III (line)]] | alt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -11.6) |
| [[LoVo (line)]] | wt | 43.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.254× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 75.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 37.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 44.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -10.0) |
| [[SW 1271 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0667× (z -11.1) ⚠ toxic |
| [[SW 900 (line)]] | alt | 49.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -11.1) |
| [[A-172 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.91 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 59.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.80 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.39 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.44 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 33.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10357), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1X]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[ANGPTL4]] | +0.64 | +0.61 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[SLC2A3]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[RILPL2]] | +0.62 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SEC14L2]] | +0.61 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[TNFRSF10D]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[MT2A]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[ERRFI1]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[MAP2K1]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ZFYVE28]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[HK1]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[SMAP2]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRA3]] | -0.56 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[ARHGAP42]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[GALNT7]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[PTPRK]] | -0.53 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[TBC1D22B]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ZNF532]] | -0.51 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[RNF207]] | -0.51 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[FGF2]] | -0.50 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[PER3]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ZNF236]] | -0.49 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[NHLRC2]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[TCF12]] | -0.49 | -0.47 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TREM1]] | B | TREM1 activity raises GLRX's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 2.67× lower at baseline in the lines without TREM1 | 0.006 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[ELL2]] | B | ELL2 activity raises GLRX's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 3.40× lower at baseline in the lines without ELL2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[ARHGAP42]] | B | ARHGAP42 activity weakens GLRX's drug response | lines that do not express ARHGAP42 (7) vs lines expressing it (33) | the lines without ARHGAP42 respond 1.36× as strongly (z diff -1.80); strongest at Cobimetinib 5 µM: 0.38x vs 0.65x (z diff -3.6) | 0.068 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[RGS2]] | B | RGS2 activity raises GLRX's level | lines that do not express RGS2 (17) vs lines expressing it (33) | 2.03× lower at baseline in the lines without RGS2 | 0.071 | ⚠ within organs, on part of the lines; also absent: LINC01393, P2RY1, MEF2C-AS1; maybe low, not absent |
| [[TLR2]] | B | TLR2 activity raises GLRX's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 2.02× lower at baseline in the lines without TLR2 | 0.089 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[TCAF2]] | C | TCAF2 activity raises GLRX's level | lines that do not express TCAF2 (4) vs lines expressing it (46) | 4.43× lower at baseline in the lines without TCAF2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF236]] | B | GLRX activity lowers ZNF236's level | lines that do not express GLRX (10) vs lines expressing it (40) | 1.91× higher at baseline in the lines without GLRX | 0.002 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[CBLB]] | B | GLRX activity raises CBLB's level | lines that do not express GLRX (10) vs lines expressing it (40) | 2.59× lower at baseline in the lines without GLRX | 0.007 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[ELL2]] | B | GLRX activity raises ELL2's level | lines that do not express GLRX (10) vs lines expressing it (40) | 3.42× lower at baseline in the lines without GLRX | 0.008 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[PNPLA8]] | B | GLRX activity raises PNPLA8's level | lines that do not express GLRX (10) vs lines expressing it (40) | 1.39× lower at baseline in the lines without GLRX | 0.022 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[SMAP1]] | B | GLRX activity strengthens SMAP1's drug response | lines that do not express GLRX (10) vs lines expressing it (39) | the lines without GLRX respond 0.73× as strongly (z diff +1.33); strongest at Panobinostat 5 µM: 0.79x vs 0.59x (z diff +3.8) | 0.026 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[RGS2]] | B | GLRX activity raises RGS2's level | lines that do not express GLRX (10) vs lines expressing it (40) | 2.50× lower at baseline in the lines without GLRX | 0.031 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[RAB20]] | B | GLRX activity raises RAB20's level | lines that do not express GLRX (10) vs lines expressing it (40) | 2.17× lower at baseline in the lines without GLRX | 0.051 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[TREM1]] | B | GLRX activity raises TREM1's level | lines that do not express GLRX (10) vs lines expressing it (40) | 1.92× lower at baseline in the lines without GLRX | 0.056 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[HERC3]] | B | GLRX activity raises HERC3's level | lines that do not express GLRX (10) vs lines expressing it (40) | 1.76× lower at baseline in the lines without GLRX | 0.058 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[NAMPT]] | B | GLRX activity raises NAMPT's level | lines that do not express GLRX (10) vs lines expressing it (40) | 1.83× lower at baseline in the lines without GLRX | 0.063 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[MAP2K1]] | B | GLRX activity raises MAP2K1's level | lines that do not express GLRX (10) vs lines expressing it (40) | 1.46× lower at baseline in the lines without GLRX | 0.069 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[CNOT8]] | B | GLRX activity raises CNOT8's level | lines that do not express GLRX (10) vs lines expressing it (40) | 1.35× lower at baseline in the lines without GLRX | 0.069 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.616). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.7, 11.3); signed map (14.6, 35.7). **Vector** length 133, 42.6% of its response variance represented; |z| ≥ 3 in 1,248 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Metallothioneins bind metals* (reactome, mean cos +0.53 to 5); *metallothionein* (control, mean cos +0.53 to 5); *Response to metal ions* (reactome, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +2.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.2 | +2.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.9 | +3.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.8 | +3.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.7 | -5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.9 | -3.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.8 | -3.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -4.7 | -4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.6 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.5 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | glutaredoxin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:95,751,319-95,822,726 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GRX, GRX1 |
| Gene groups (HGNC) | Glutaredoxin domain containing |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, KRAS_SIGNALING_UP, GLYCOLYSIS, HYPOXIA, MTORC1_SIGNALING |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P35754](https://www.uniprot.org/uniprotkb/P35754) (Glutaredoxin-1):

> Has a glutathione-disulfide oxidoreductase activity in the presence of NADPH and glutathione reductase. Reduces low molecular weight disulfides and proteins.

**Summary**, from NCBI Gene [2745](https://www.ncbi.nlm.nih.gov/gene/2745):

> This gene encodes a member of the glutaredoxin family. The encoded protein is a cytoplasmic enzyme catalyzing the reversible reduction of glutathione-protein mixed disulfides. This enzyme highly contributes to the antioxidant defense system. It is crucial for several signalling pathways by controlling the S-glutathionylation status of signalling mediators. It is involved in beta-amyloid toxicity and Alzheimer's disease. Multiple alternatively spliced transcript variants encoding the same …

**Accessions** — [HGNC:4330](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4330) · Entrez [2745](https://www.ncbi.nlm.nih.gov/gene/2745) · UniProt [P35754](https://www.uniprot.org/uniprotkb/P35754) · Ensembl [ENSG00000173221](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173221)

## Data

Gene col 10357: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10357); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10357, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10357]; `tensor/DDL_lfc|DDL_z.npy` [10357]; `embed/gene_vectors.npy` [10357]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10357 or target_col == 10357). Every well: [[GLRX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLRX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
