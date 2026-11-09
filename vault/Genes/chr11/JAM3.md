---
symbol: "JAM3"
type: "gene"
col: 9235
ensembl_id: "ENSG00000166086"
name: "junctional adhesion molecule 3"
location: "11q25"
module: 132
arm: "+"
pooled_cpm: 22.54
n_lines_expressing: 27
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# JAM3

*junctional adhesion molecule 3* — 11q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.85× (z +9.1, q 8e-17, up in 19 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.397× (z -19.2, q 0e+00, down in 20 of 25 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASF3]] (+0.73, fdr 7e-06), [[ZNF483]] (+0.66, fdr 1e-05), [[CNIH1]] (+0.65, fdr 1e-05); moves opposite to [[HELQ]] (-0.65, fdr 2e-05), [[UNK]] (-0.60, fdr 2e-05), [[WARS2-AS1]] (-0.59, fdr 3e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[EFR3B]] → it (grade B ⚠); 6 go from it, the strongest it → [[ATRN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9235.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +9.1 | 8e-17 | 19/25 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +7.5 | 1e-11 | 15/25 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +6.1 | 1e-07 | 14/25 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.50×** | +6.0 | 3e-07 | 15/25 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +5.5 | 4e-06 | 10/25 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.89×** | +4.9 | 9e-05 | 12/21 (RPMI-7951, A-427, …) | all doses, flat | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +4.8 | 1e-04 | 11/25 (RPMI-7951, C-33 A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +4.7 | 2e-04 | 13/25 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.39×** | +4.6 | 2e-04 | 14/25 (A-172, hTERT-HPNE, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +4.3 | 9e-04 | 13/25 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.1 | 0.002 | 7/18 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.003 | 12/25 (RPMI-7951, NCI-H1573, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.60×** | +3.6 | 0.012 | 9/25 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.039 | 8/25 (RPMI-7951, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.066 | 7/24 (LOX-IMVI, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9235.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.397×** | -19.2 | 0e+00 | 20/25 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.454×** | -11.6 | 1e-28 | 21/25 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.521×** | -9.2 | 6e-18 | 17/25 (HOP62, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.629×** | -6.8 | 1e-09 | 17/25 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.729×** | -6.6 | 6e-09 | 16/25 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.661×** | -6.1 | 1e-07 | 20/25 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.740×** | -4.4 | 8e-04 | 12/25 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.728×** | -4.3 | 0.001 | 11/23 (A-172, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.779×** | -3.7 | 0.016 | 12/23 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.710×** | -3.2 | 0.084 | 10/24 (H4, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.804× | -3.1 | 0.11 | 9/25 (AN3 CA, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | 0.807× | -3.0 | 0.12 | 11/23 (NCI-H1573, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9235. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 48.5 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.13× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -10.7) |
| [[A-172 (line)]] | wt | 41.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -19.0) |
| [[NCI-H460 (line)]] | wt | 18.2 | 3 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.41× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.469× (z -8.9) |
| [[C-33 A (line)]] | alt | 125 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -10.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 62.6 | 2 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 5.12× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -9.8) |
| [[HOP62 (line)]] | alt | 35.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -13.2) |
| [[LOX-IMVI (line)]] | wt | 43.9 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 3.49× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -14.0) |
| [[HS-578T (line)]] | alt | 38.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -12.8) |
| [[hTERT-HPNE (line)]] | wt | 38.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -10.2) |
| [[AN3 CA (line)]] | alt | 111 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -12.6) |
| [[C32 (line)]] | wt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 32.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.247× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 48.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -20.8) |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0648× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 47.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -11.9) |
| [[SHP-77 (line)]] | alt | 238 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 56.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 30.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -8.5) |
| [[A-427 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.00 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.38 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.72 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9235), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASF3]] | +0.73 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[ZNF483]] | +0.66 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[CNIH1]] | +0.65 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[RAB6B]] | +0.65 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SHANK3]] | +0.64 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[NDRG3]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PACC1]] | +0.62 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[ANXA6]] | +0.62 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[PTPRS]] | +0.61 | +0.50 / +0.55 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[HACE1]] | +0.61 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ATP2C1]] | +0.60 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[GNAZ]] | +0.60 | +0.50 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HELQ]] | -0.65 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[UNK]] | -0.60 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[WARS2-AS1]] | -0.59 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[ZFY]] | -0.59 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[GTF2IRD2B]] | -0.59 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[PDCD7]] | -0.58 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[BPTF]] | -0.58 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[LINC02340]] | -0.57 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[TRIP11]] | -0.57 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[SLC9A8]] | -0.57 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[INO80D]] | -0.56 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[FAM200A]] | -0.56 | -0.56 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFR3B]] | B | EFR3B activity raises JAM3's level | lines that do not express EFR3B (10) vs lines expressing it (40) | 4.86× lower at baseline in the lines without EFR3B | 0.050 | ⚠ within organs, on part of the lines; also absent: RTN4RL1, SEPTIN5, NT5M; maybe low, not absent |
| [[PTK7]] | B | PTK7 activity raises JAM3's level | lines that do not express PTK7 (9) vs lines expressing it (41) | 2.31× lower at baseline in the lines without PTK7 | 0.0995 | ⚠ within organs, on part of the lines; also absent: ENSG00000289985, ZNF433, ENSG00000269755 |
| [[GNAO1]] | C | GNAO1 activity raises JAM3's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 3.89× lower at baseline in the lines without GNAO1 | 0.004 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17; co-absent with the target |
| [[SSX1]] | C | SSX1 activity raises JAM3's level | lines that do not express SSX1 (43) vs lines expressing it (7) | 4.15× lower at baseline in the lines without SSX1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00879, LINC02099, RNF17; co-absent with the target |
| [[SEPTIN5]] | C | SEPTIN5 activity raises JAM3's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 5.67× lower at baseline in the lines without SEPTIN5 | 0.069 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1; co-absent with the target |
| [[SDK2]] | C | SDK2 activity raises JAM3's level | lines that do not express SDK2 (16) vs lines expressing it (34) | 5.39× lower at baseline in the lines without SDK2 | 0.086 | ⚠ within organs, on part of the lines; also absent: NRIP3, ZNF549, MGAT5B; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATRN]] | B | JAM3 activity raises ATRN's level | lines that do not express JAM3 (23) vs lines expressing it (27) | 1.76× lower at baseline in the lines without JAM3 | 0.025 | ⚠ within organs, on part of the lines; also absent: NPTX1, NOVA2, GDNF-AS1 |
| [[GNAZ]] | B | JAM3 activity raises GNAZ's level | lines that do not express JAM3 (23) vs lines expressing it (27) | 1.64× lower at baseline in the lines without JAM3 | 0.050 | ⚠ within organs, on part of the lines; also absent: NPTX1, NOVA2, GDNF-AS1 |
| [[CDKL3]] | B | JAM3 activity raises CDKL3's level | lines that do not express JAM3 (23) vs lines expressing it (27) | 1.39× lower at baseline in the lines without JAM3 | 0.088 | ⚠ within organs, on part of the lines; also absent: NPTX1, NOVA2, GDNF-AS1 |
| [[GNAO1]] | C | JAM3 activity raises GNAO1's level | lines that do not express JAM3 (23) vs lines expressing it (27) | 3.28× lower at baseline in the lines without JAM3 | 0.060 | ⚠ within organs, on part of the lines; also absent: NPTX1, NOVA2, GDNF-AS1; co-absent with the target |
| [[SLIT3]] | C | JAM3 activity raises SLIT3's level | lines that do not express JAM3 (23) vs lines expressing it (27) | 2.17× lower at baseline in the lines without JAM3 | 0.085 | ⚠ within organs, on part of the lines; also absent: NPTX1, NOVA2, GDNF-AS1; co-absent with the target |
| [[SEPTIN5]] | C | JAM3 activity raises SEPTIN5's level | lines that do not express JAM3 (23) vs lines expressing it (27) | 2.76× lower at baseline in the lines without JAM3 | 0.089 | ⚠ within organs, on part of the lines; also absent: NPTX1, NOVA2, GDNF-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.6, 41.4); signed map (-35.2, -14.5). **Vector** length 66.8, 16.3% of its response variance represented; |z| ≥ 3 in 623 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.8 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.6 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -11.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -19.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.5 | -9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.1 | -1.6 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.0 | -0.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -0.9 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | junctional adhesion molecule 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q25 — chr11:134,069,071-134,152,001 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JAM-C, JAMC, JAM-3 |
| Gene groups (HGNC) | V-set domain containing; Ig-like cell adhesion molecule family; Small nucleolar RNA protein coding host genes |
| Hallmark sets | SPERMATOGENESIS, APICAL_JUNCTION |
| Reactome | 4 pathways, smallest: Integrin cell surface interactions; Cell surface interactions at the vascular wall; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BX67](https://www.uniprot.org/uniprotkb/Q9BX67) (Junctional adhesion molecule C):

> Junctional adhesion protein that mediates heterotypic cell-cell interactions with its cognate receptor JAM2 to regulate different cellular processes. Plays a role in homing and mobilization of hematopoietic stem and progenitor cells within the bone marrow. At the surface of bone marrow stromal cells, it contributes to the retention of the hematopoietic stem and progenitor cells expressing JAM3. Plays a central role in leukocytes extravasation by facilitating transmigration through the …

**Summary**, from NCBI Gene [83700](https://www.ncbi.nlm.nih.gov/gene/83700):

> Tight junctions represent one mode of cell-to-cell adhesion in epithelial or endothelial cell sheets, forming continuous seals around cells and serving as a physical barrier to prevent solutes and water from passing freely through the paracellular space. The protein encoded by this immunoglobulin superfamily gene member is localized in the tight junctions between high endothelial cells. Unlike other proteins in this family, the this protein is unable to adhere to leukocyte cell lines and only …

**Accessions** — [HGNC:15532](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15532) · Entrez [83700](https://www.ncbi.nlm.nih.gov/gene/83700) · UniProt [Q9BX67](https://www.uniprot.org/uniprotkb/Q9BX67) · Ensembl [ENSG00000166086](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166086)

## Data

Gene col 9235: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9235); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9235, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9235]; `tensor/DDL_lfc|DDL_z.npy` [9235]; `embed/gene_vectors.npy` [9235]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9235 or target_col == 9235). Every well: [[JAM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JAM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
