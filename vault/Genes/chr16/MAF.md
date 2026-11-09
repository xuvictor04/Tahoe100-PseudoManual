---
symbol: "MAF"
type: "gene"
col: 10939
ensembl_id: "ENSG00000178573"
name: "MAF bZIP transcription factor"
location: "16q23.2"
module: 14
arm: "+"
pooled_cpm: 14.49
n_lines_expressing: 23
n_dd_up: 14
n_dd_down: 18
n_dd_up_clean: 11
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 35
direction_downstream: 40
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# MAF

*MAF bZIP transcription factor* — 16q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.13× (z +8.2, q 1e-13, up in 7 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.434× (z -6.4, q 6e-08, down in 15 of 20 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Dexamethasone (drug)]] 0.5 µM: 0.436× (z -6.4, q 6e-08, down in 15 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EDIL3]] (+0.71, fdr 7e-06), [[IDO1]] (+0.68, fdr 7e-06), [[C15orf48]] (+0.64, fdr 7e-06); moves opposite to [[STK39]] (-0.54, fdr 1e-05), [[PYGB]] (-0.53, fdr 2e-05), [[LDLRAD3]] (-0.52, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 35 arrows point to it, the strongest [[NEURL3]] → it (grade B ⚠); 40 go from it, the strongest it → [[ZMIZ1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10939.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +8.2 | 1e-13 | 7/20 (A498, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +6.1 | 2e-07 | 1/13 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +5.6 | 4e-06 | 9/20 (HS-578T, SNU-423, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.90×** | +5.5 | 6e-06 | 19/20 (HOP62, SW 900, …) | two highest doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +5.3 | 2e-05 | 1/17 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.96×** | +5.0 | 6e-05 | 16/20 (HOP62, SW 900, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.76×** | +4.3 | 0.001 | 18/20 (SW 900, HOP62, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **1.64×** | +4.1 | 0.002 | 17/21 (HOP62, SW 900, …) | two highest doses | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.67×** | +3.8 | 0.008 | 16/21 (HOP62, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.029 | 13/20 (HOP62, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +3.3 | 0.047 | 6/20 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.35×** | +3.3 | 0.047 | 6/20 (A498, COLO 205, …) | top dose only | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.82×** | +3.2 | 0.052 | 4/18 (SW 900, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.073 | 7/20 (Panc 03.27, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10939.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.434×** | -6.4 | 6e-08 | 15/20 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.436×** | -6.4 | 6e-08 | 15/20 (H4, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **0.477×** | -5.7 | 3e-06 | 17/20 (NCI-H1792, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.512×** | -5.1 | 4e-05 | 16/20 (H4, HOP62, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.562×** | -4.4 | 0.001 | 16/20 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.581×** | -4.2 | 0.003 | 16/20 (H4, NCI-H460, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.596×** | -4.0 | 0.006 | 11/20 (H4, CFPAC-1, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.616×** | -3.7 | 0.013 | 13/20 (H4, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.710×** | -3.7 | 0.013 | 15/20 (H4, CFPAC-1, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.624×** | -3.6 | 0.017 | 17/21 (H4, NCI-H460, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.635×** | -3.5 | 0.026 | 15/20 (NCI-H460, H4, …) | all doses, flat |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.643×** | -3.4 | 0.034 | 7/20 (NCI-H1792, A549, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.653×** | -3.3 | 0.046 | 9/20 (NCI-H1792, A549, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.655×** | -3.2 | 0.047 | 11/20 (NCI-H460, A498, …) | all doses, flat | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.460×** | -3.1 | 0.070 | 13/20 (NCI-H460, H4, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.647×** | -3.1 | 0.071 | 2/20 (SNU-423, RPMI-7951) | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.675×** | -3.0 | 0.085 | 9/20 (RPMI-7951, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.49 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10939. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 133 | 0 | 21 (8 ⚠) | — | [[Clobetasol propionate (drug)]] 5 µM 0.0734× (z -15.1) |
| [[NCI-H460 (line)]] | wt | 85.1 | 0 | 17 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.154× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 18.5 | 0 | 8 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0193× (z -16.1) ⚠ unreliable plate only · without an alert: [[Dexamethasone (drug)]] 5 µM 0.0878× (z -9.9) |
| [[HOP62 (line)]] | alt | 21.8 | 3 (1 ⚠) | 3 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.99× (z +10.2) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 8.12× (z +9.1) | [[Clobetasol propionate (drug)]] 0.5 µM 0.0622× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 43.8 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0625× (z -14.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 34.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.07× (z +22.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.82× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 15.8 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0373× (z -12.2) |
| [[A549 (line)]] | wt | 17.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0597× (z -11.1) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 21.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +10.0) ⚠ cell-cycle shift, explains ~26% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.116× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 52.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0787× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.123× (z -10.2) |
| [[A-172 (line)]] | wt | 4.21 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 5 µM 0.0539× (z -8.6) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.104× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 35.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.194× (z -8.5) |
| [[A-427 (line)]] | wt | 0.856 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.912 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.52 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10939), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDIL3]] | +0.71 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[IDO1]] | +0.68 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[C15orf48]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[GBP2]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[MARCKS]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[KMO]] | +0.60 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[SIRLNT]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[IGFBP3]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[NR3C1]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 | pathway: Transcriptional regulation by RUNX2 |
| [[OR9Q1]] | +0.58 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[BMF]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SHISAL1]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK39]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[PYGB]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[LDLRAD3]] | -0.52 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[AHCTF1]] | -0.49 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[FARP1]] | -0.49 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[BCL2L1]] | -0.48 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[GMPS]] | -0.48 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[SLC26A2]] | -0.48 | -0.43 / -0.46 | both halves | 3e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[LAMB1]] | -0.48 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ADCY3]] | -0.48 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[ARMC8]] | -0.48 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[NSUN2]] | -0.48 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 4, C 31. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEURL3]] | B | NEURL3 activity raises MAF's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 3.44× lower at baseline in the lines without NEURL3 | 0.015 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[PTGES]] | B | PTGES activity raises MAF's level | lines that do not express PTGES (17) vs lines expressing it (33) | 3.08× lower at baseline in the lines without PTGES | 0.043 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[BDKRB2]] | B | BDKRB2 activity raises MAF's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.37× lower at baseline in the lines without BDKRB2 | 0.067 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[P2RX7]] | B | P2RX7 activity raises MAF's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 3.16× lower at baseline in the lines without P2RX7 | 0.080 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[IFI16]] | C | IFI16 activity raises MAF's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 4.43× lower at baseline in the lines without IFI16 | 0.002 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF; co-absent with the target |
| [[IL6]] | C | IL6 activity raises MAF's level | lines that do not express IL6 (32) vs lines expressing it (18) | 6.22× lower at baseline in the lines without IL6 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2; co-absent with the target |
| [[CRLF2]] | C | CRLF2 activity raises MAF's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 5.96× lower at baseline in the lines without CRLF2 | 0.003 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR; co-absent with the target |
| [[ABCA1]] | C | ABCA1 activity raises MAF's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 4.69× lower at baseline in the lines without ABCA1 | 0.003 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7; co-absent with the target |
| [[IGFBP3]] | C | IGFBP3 activity raises MAF's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 4.62× lower at baseline in the lines without IGFBP3 | 0.004 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF; co-absent with the target |
| [[CRTAC1]] | C | CRTAC1 activity raises MAF's level | lines that do not express CRTAC1 (27) vs lines expressing it (23) | 3.90× lower at baseline in the lines without CRTAC1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2; co-absent with the target |
| [[IGFBP7]] | C | IGFBP7 activity raises MAF's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 5.67× lower at baseline in the lines without IGFBP7 | 0.005 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[KYNU]] | C | KYNU activity raises MAF's level | lines that do not express KYNU (29) vs lines expressing it (21) | 4.72× lower at baseline in the lines without KYNU | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725; co-absent with the target |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 18, C 22. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZMIZ1]] | B | MAF activity raises ZMIZ1's level | lines that do not express MAF (27) vs lines expressing it (23) | 1.88× lower at baseline in the lines without MAF | 0.001 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[GBP2]] | B | MAF activity raises GBP2's level | lines that do not express MAF (27) vs lines expressing it (23) | 3.65× lower at baseline in the lines without MAF | 0.001 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[NEURL3]] | B | MAF activity raises NEURL3's level | lines that do not express MAF (27) vs lines expressing it (23) | 2.12× lower at baseline in the lines without MAF | 0.002 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[HLA-E]] | B | MAF activity raises HLA-E's level | lines that do not express MAF (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without MAF | 0.011 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[ARID5A]] | B | MAF activity raises ARID5A's level | lines that do not express MAF (27) vs lines expressing it (23) | 1.67× lower at baseline in the lines without MAF | 0.020 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[THEMIS2]] | B | MAF activity raises THEMIS2's level | lines that do not express MAF (27) vs lines expressing it (23) | 2.59× lower at baseline in the lines without MAF | 0.021 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[RIPK2]] | B | MAF activity raises RIPK2's level | lines that do not express MAF (27) vs lines expressing it (23) | 1.89× lower at baseline in the lines without MAF | 0.025 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[HLA-A]] | B | MAF activity raises HLA-A's level | lines that do not express MAF (27) vs lines expressing it (23) | 2.30× lower at baseline in the lines without MAF | 0.033 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[TMOD1]] | B | MAF activity raises TMOD1's level | lines that do not express MAF (27) vs lines expressing it (23) | 2.60× lower at baseline in the lines without MAF | 0.042 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[PLD1]] | B | MAF activity raises PLD1's level | lines that do not express MAF (27) vs lines expressing it (23) | 2.65× lower at baseline in the lines without MAF | 0.051 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[P2RX7]] | B | MAF activity raises P2RX7's level | lines that do not express MAF (27) vs lines expressing it (23) | 2.55× lower at baseline in the lines without MAF | 0.058 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[ADCY3]] | B | MAF activity lowers ADCY3's level | lines that do not express MAF (27) vs lines expressing it (23) | 1.49× higher at baseline in the lines without MAF | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.419). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.9, 19.5); signed map (49.7, 22.4). **Vector** length 97.2, 32.7% of its response variance represented; |z| ≥ 3 in 820 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.5 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.8 | +5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +5.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -4.6 | -6.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.5 | -4.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.3 | -3.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.9 | -5.7 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -3.6 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | MAF bZIP transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.2 — chr16:79,585,843-79,600,737 (-) |
| Ensembl biotype | protein_coding |
| Also known as | c-MAF |
| Gene groups (HGNC) | Large MAF bZIP transcription factor family |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 8 pathways, smallest: RUNX2 regulates osteoblast differentiation; RUNX2 regulates bone development; Differentiation of naive CD4+ T cells to T helper 2 cells (Th2 cells) |
| Matched by | ensembl_id |

**Function**, from UniProt [O75444](https://www.uniprot.org/uniprotkb/O75444) (Transcription factor Maf):

> Acts as a transcriptional activator or repressor. Involved in embryonic lens fiber cell development. Recruits the transcriptional coactivators CREBBP and/or EP300 to crystallin promoters leading to up-regulation of crystallin gene during lens fiber cell differentiation. Activates the expression of IL4 in T helper 2 (Th2) cells. Increases T-cell susceptibility to apoptosis by interacting with MYB and decreasing BCL2 expression. Together with PAX6, transactivates strongly the glucagon gene …

**Summary**, from NCBI Gene [4094](https://www.ncbi.nlm.nih.gov/gene/4094):

> The protein encoded by this gene is a DNA-binding, leucine zipper-containing transcription factor that acts as a homodimer or as a heterodimer. Depending on the binding site and binding partner, the encoded protein can be a transcriptional activator or repressor. This protein plays a role in the regulation of several cellular processes, including embryonic lens fiber cell development, increased T-cell susceptibility to apoptosis, and chondrocyte terminal differentiation. Defects in this gene …

**Accessions** — [HGNC:6776](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6776) · Entrez [4094](https://www.ncbi.nlm.nih.gov/gene/4094) · UniProt [O75444](https://www.uniprot.org/uniprotkb/O75444) · Ensembl [ENSG00000178573](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178573)

## Data

Gene col 10939: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10939); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10939, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10939]; `tensor/DDL_lfc|DDL_z.npy` [10939]; `embed/gene_vectors.npy` [10939]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10939 or target_col == 10939). Every well: [[MAF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
