---
symbol: "CRYBG1"
type: "gene"
col: 3350
ensembl_id: "ENSG00000112297"
name: "crystallin beta-gamma domain containing 1"
location: "6q21"
module: 40
arm: "-"
pooled_cpm: 46.24
n_lines_expressing: 32
n_dd_up: 12
n_dd_down: 17
n_dd_up_clean: 12
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 5
direction_downstream: 11
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# CRYBG1

*crystallin beta-gamma domain containing 1* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.34× (z +5.5, q 3e-05, up in 14 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.580× (z -10.3, q 5e-22, down in 28 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLCE1]] (+0.53, fdr 3e-05), [[PCDH7]] (+0.49, fdr 3e-05), [[TNC]] (+0.49, fdr 4e-05); moves opposite to [[PPOX]] (-0.51, fdr 2e-05), [[GET1-SH3BGR]] (-0.50, fdr 4e-05), [[PGPEP1]] (-0.50, fdr 6e-05).
> It sits in the **-** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[IL15]] → it (grade B ⚠); 11 go from it, the strongest it → [[ZIM2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3350.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.5 | 3e-05 | 14/30 (SW1417, NCI-H2030, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.46×** | +4.8 | 4e-04 | 18/29 (HOP62, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +4.6 | 6e-04 | 17/30 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **1.41×** | +4.6 | 6e-04 | 16/31 (HOP62, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +4.2 | 0.003 | 13/30 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.005 | 12/30 (Hs 766T, NCI-H2347, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.023 | 13/30 (HT-29, CFPAC-1, …) | all doses, flat |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.033 | 11/30 (RPMI-7951, HT-29, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.042 | 10/30 (LS 180, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.042 | 13/31 (LS 180, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.082 | 14/29 (HOP62, LS 180, …) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.082 | 7/30 (SK-MEL-2, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3350.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.580×** | -10.3 | 5e-22 | 28/30 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.552×** | -7.9 | 5e-13 | 25/30 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.648×** | -5.8 | 1e-06 | 21/30 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.728×** | -4.3 | 0.003 | 20/31 (BT-474, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.723×** | -4.2 | 0.003 | 15/29 (C32, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.737×** | -4.1 | 0.004 | 16/30 (C32, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.738×** | -4.1 | 0.004 | 15/29 (C32, SK-MEL-2, …) | two highest doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.744×** | -4.0 | 0.005 | 20/30 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.818×** | -3.8 | 0.009 | 15/31 (RPMI-7951, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.753×** | -3.5 | 0.025 | 16/28 (HEC-1-A, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.776×** | -3.4 | 0.036 | 17/30 (C32, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.781×** | -3.3 | 0.044 | 19/30 (HT-29, HEC-1-A, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.786×** | -3.2 | 0.054 | 15/30 (LoVo, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.793×** | -3.1 | 0.071 | 11/30 (C32, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.793×** | -3.1 | 0.071 | 14/30 (C32, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.795×** | -3.1 | 0.075 | 15/30 (C32, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.855× | -3.0 | 0.089 | 9/31 (HOP62, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3350. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 119 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -13.0) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.142× (z -11.7) |
| [[LoVo (line)]] | wt | 91.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -17.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.408× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 68.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -24.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.350× (z -13.0) |
| [[PANC-1 (line)]] | alt | 102 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.36× (z +9.8) | — |
| [[H4 (line)]] | wt | 50.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0804× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 31.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.306× (z -9.9) |
| [[HT-29 (line)]] | alt | 172 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.194× (z -13.8) |
| [[A-172 (line)]] | wt | 48.6 | 1 | 1 | [[Harringtonine (drug)]] 0.5 µM 3.55× (z +8.8) | [[Selinexor (drug)]] 5 µM 0.328× (z -11.0) |
| [[A498 (line)]] | wt | 56.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -8.8) |
| [[HOP62 (line)]] | alt | 53.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.444× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 16.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 163 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 63.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.455× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 87.5 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.489× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 52.5 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.396× (z -9.5) |
| [[SW48 (line)]] | wt | 83.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 5.32 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.71 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.85 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.52 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.83 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.01 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.95 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.54 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3350), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLCE1]] | +0.53 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[PCDH7]] | +0.49 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[TNC]] | +0.49 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[TAGLN2]] | +0.48 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[KCTD12]] | +0.47 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[CAV1]] | +0.47 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[SLCO3A1]] | +0.47 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[ARNT2]] | +0.46 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[PLCB4]] | +0.46 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[GLI3]] | +0.45 | +0.41 / +0.37 | both halves | 8e-05 |  |
| [[ANGPT1]] | +0.45 | +0.43 / +0.36 | both halves | 1e-04 |  |
| [[CTTNBP2]] | +0.44 | +0.44 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPOX]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[GET1-SH3BGR]] | -0.50 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[PGPEP1]] | -0.50 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[HCG25]] | -0.49 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[CAPN10-DT]] | -0.48 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[SGSM3]] | -0.48 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[TVP23C]] | -0.48 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[ZNF552]] | -0.48 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[FRG1HP]] | -0.48 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ZKSCAN2-DT]] | -0.48 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[COX7A2L]] | -0.48 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[DRD4]] | -0.48 | -0.32 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL15]] | B | IL15 activity raises CRYBG1's level | lines that do not express IL15 (10) vs lines expressing it (40) | 5.91× lower at baseline in the lines without IL15 | 2e-04 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers CRYBG1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ATP10B]] | B | ATP10B activity raises CRYBG1's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 3.27× lower at baseline in the lines without ATP10B | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[IL7]] | B | IL7 activity raises CRYBG1's level | lines that do not express IL7 (7) vs lines expressing it (43) | 3.77× lower at baseline in the lines without IL7 | 0.0998 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, HIPK2; maybe low, not absent |
| [[SHROOM4]] | C | SHROOM4 activity raises CRYBG1's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 2.67× lower at baseline in the lines without SHROOM4 | 0.068 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZIM2-AS1]] | B | CRYBG1 activity lowers ZIM2-AS1's level | lines that do not express CRYBG1 (18) vs lines expressing it (32) | 1.57× higher at baseline in the lines without CRYBG1 | 0.024 | ⚠ within organs, on part of the lines; also absent: TSPOAP1, MPZL3, LNX1 |
| [[ALCAM]] | B | CRYBG1 activity raises ALCAM's level | lines that do not express CRYBG1 (18) vs lines expressing it (32) | 2.42× lower at baseline in the lines without CRYBG1 | 0.037 | ⚠ within organs, on part of the lines; also absent: TSPOAP1, MPZL3, LNX1 |
| [[NUP188]] | B | CRYBG1 activity lowers NUP188's level | lines that do not express CRYBG1 (18) vs lines expressing it (32) | 1.52× higher at baseline in the lines without CRYBG1 | 0.040 | ⚠ within organs, on part of the lines; also absent: TSPOAP1, MPZL3, LNX1 |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | CRYBG1 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express CRYBG1 (18) vs lines expressing it (30) | the lines without CRYBG1: 0.90× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: TSPOAP1, MPZL3, LNX1 |
| [[IL15]] | B | CRYBG1 activity raises IL15's level | lines that do not express CRYBG1 (18) vs lines expressing it (32) | 2.31× lower at baseline in the lines without CRYBG1 | 0.047 | ⚠ within organs, on part of the lines; also absent: TSPOAP1, MPZL3, LNX1 |
| cells under [[Tolcapone (drug)]] 5 µM | B | CRYBG1 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express CRYBG1 (18) vs lines expressing it (30) | the lines without CRYBG1: 0.85× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: TSPOAP1, MPZL3, LNX1 |
| cells under [[Trifluridine (drug)]] 5 µM | B | CRYBG1 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express CRYBG1 (18) vs lines expressing it (30) | the lines without CRYBG1: 0.90× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: TSPOAP1, MPZL3, LNX1 |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM | B | CRYBG1 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express CRYBG1 (18) vs lines expressing it (30) | the lines without CRYBG1: 0.84× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: TSPOAP1, MPZL3, LNX1 |
| cells under [[Pyridoxine (hydrochloride) (drug)]] 5 µM | B | CRYBG1 activity lowers the cells' numbers under Pyridoxine (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express CRYBG1 (18) vs lines expressing it (30) | the lines without CRYBG1: 1.13× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: TSPOAP1, MPZL3, LNX1 |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | CRYBG1 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express CRYBG1 (18) vs lines expressing it (30) | the lines without CRYBG1: 0.83× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: TSPOAP1, MPZL3, LNX1 |
| [[SHROOM4]] | C | CRYBG1 activity raises SHROOM4's level | lines that do not express CRYBG1 (18) vs lines expressing it (32) | 2.86× lower at baseline in the lines without CRYBG1 | 0.032 | ⚠ within organs, on part of the lines; also absent: TSPOAP1, MPZL3, LNX1; co-absent with the target |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.419). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (21.3, -36.5); signed map (45.5, 27.2). **Vector** length 93.6, 25.9% of its response variance represented; |z| ≥ 3 in 856 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.0 | +4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +3.5 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +4.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.0 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +0.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.0 | -10.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.9 | -5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -7.9 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | crystallin beta-gamma domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:106,360,717-106,572,017 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ST4, AIM1 |
| Gene groups (HGNC) | Beta-gamma crystallin domain containing |
| Hallmark sets | APICAL_SURFACE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4K1](https://www.uniprot.org/uniprotkb/Q9Y4K1) (Beta/gamma crystallin domain-containing protein 1):

> May function as suppressor of malignant melanoma. It may exert its effects through interactions with the cytoskeleton.

**Summary**, from NCBI Gene [202](https://www.ncbi.nlm.nih.gov/gene/202):

> Predicted to enable carbohydrate binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:356](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:356) · Entrez [202](https://www.ncbi.nlm.nih.gov/gene/202) · UniProt [Q9Y4K1](https://www.uniprot.org/uniprotkb/Q9Y4K1) · Ensembl [ENSG00000112297](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112297)

## Data

Gene col 3350: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3350); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3350, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3350]; `tensor/DDL_lfc|DDL_z.npy` [3350]; `embed/gene_vectors.npy` [3350]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3350 or target_col == 3350). Every well: [[CRYBG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRYBG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
