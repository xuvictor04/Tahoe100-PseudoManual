---
symbol: "NRTN"
type: "gene"
col: 10053
ensembl_id: "ENSG00000171119"
name: "neurturin"
location: "19p13.3"
module: 100
arm: "+"
pooled_cpm: 2.37
n_lines_expressing: 46
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# NRTN

*neurturin* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.24× (z +12.8, q 1e-34, up in 36 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.499× (z -6.2, q 4e-07, down in 18 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LS 180 0.0573×, SK-MEL-2 0.0804×); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.0472×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H2030 0.0610×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.149×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAST1]] (+0.72, fdr 7e-06), [[SLC66A2]] (+0.68, fdr 3e-05), [[HIP1]] (+0.67, fdr 1e-05); moves opposite to [[ENOX2]] (-0.64, fdr 4e-05), [[SNX19]] (-0.63, fdr 3e-05), [[GPATCH2]] (-0.62, fdr 1e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CAMSAP3]] → it (grade B ⚠); 4 go from it, the strongest it → [[KANK3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10053.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.24×** | +12.8 | 1e-34 | 36/41 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +12.5 | 3e-33 | 15/30 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.63×** | +11.4 | 7e-28 | 29/38 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.51×** | +11.1 | 2e-26 | 36/38 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.34×** | +10.6 | 3e-24 | 19/30 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.98×** | +9.3 | 1e-18 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.71×** | +8.8 | 1e-16 | 34/41 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.48×** | +8.0 | 6e-14 | 19/24 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.89×** | +7.9 | 1e-13 | 25/36 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **3.34×** | +5.6 | 1e-06 | 9/33 (PANC-1, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +4.6 | 2e-04 | 12/32 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +4.1 | 0.002 | 8/32 (A-172, SW480, …) | top dose only |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.88×** | +4.0 | 0.003 | 0/36 | rises with dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.83×** | +3.8 | 0.006 | 2/18 (MIA PaCa-2, SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.6 | 0.011 | 3/22 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | **1.48×** | +3.4 | 0.018 | 2/36 (SNU-423, LoVo) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.46×** | +3.3 | 0.025 | 4/36 (NCI-H2030, KATO III, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10053.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LS 180 0.0573×, SK-MEL-2 0.0804×); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.0472×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H2030 0.0610×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.149×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.499×** | -6.2 | 4e-07 | 18/38 (A-427, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.648×** | -3.9 | 0.032 | 13/37 (SW480, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.689× | -3.3 | 0.17 | 12/34 (A-172, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.696× | -3.2 | 0.17 | 10/35 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.689× | -3.1 | 0.25 | 6/41 (C32, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10053. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 7.46 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.149× (z -8.7) |
| [[C32 (line)]] | wt | 1.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.9× (z +9.6) | — |
| [[LoVo (line)]] | wt | 3.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.13× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 4.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0573× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 2.95 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0610× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 4.68 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SK-MEL-2 (line)]] | alt | 5.93 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0804× (z -8.8) |
| [[SW480 (line)]] | alt | 1.83 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0472× (z -10.6) |
| [[A-172 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.617 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.727 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.876 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.713 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.684 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.532 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.779 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.648 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.832 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.876 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10053), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST1]] | +0.72 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SLC66A2]] | +0.68 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[HIP1]] | +0.67 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[TNNI3]] | +0.66 | +0.42 / +0.68 | both halves | 4e-05 |  |
| [[PLEKHH3]] | +0.66 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[AHDC1]] | +0.66 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[FOXO6]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ARID3A]] | +0.63 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[SETD5]] | +0.63 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[MARCHF9]] | +0.62 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[PDE4A]] | +0.62 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ITGA7]] | +0.62 | +0.47 / +0.66 | both halves | 2e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOX2]] | -0.64 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[SNX19]] | -0.63 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[GPATCH2]] | -0.62 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[AVEN]] | -0.61 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[RNASEH1]] | -0.60 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ATXN10]] | -0.60 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[TOR1A]] | -0.60 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[ATR]] | -0.59 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[EIF4G2]] | -0.59 | -0.32 / -0.63 | both halves | 2e-04 |  |
| [[ABCF2]] | -0.59 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[DNAJC11]] | -0.59 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[NSD1]] | -0.58 | -0.36 / -0.57 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAMSAP3]] | B | CAMSAP3 activity weakens NRTN's drug response | lines that do not express CAMSAP3 (11) vs lines expressing it (31) | the lines without CAMSAP3 respond 1.29× as strongly (z diff -0.38); strongest at Idarubicin (hydrochloride) 5 µM: 3.59x vs 1.60x (z diff -3.3) | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[CAMSAP3]] | B | CAMSAP3 activity raises NRTN's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 1.80× lower at baseline in the lines without CAMSAP3 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KANK3]] | C | NRTN activity raises KANK3's level | lines that do not express NRTN (4) vs lines expressing it (46) | 1.62× lower at baseline in the lines without NRTN | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, ATP11A, BRME1; maybe low, not absent |
| [[RAB11FIP5]] | C | NRTN activity lowers RAB11FIP5's level | lines that do not express NRTN (4) vs lines expressing it (46) | 1.77× higher at baseline in the lines without NRTN | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, ATP11A, BRME1; maybe low, not absent |
| [[AGFG2]] | C | NRTN activity raises AGFG2's level | lines that do not express NRTN (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without NRTN | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, ATP11A, BRME1; maybe low, not absent |
| [[MTHFSD]] | C | NRTN activity raises MTHFSD's level | lines that do not express NRTN (4) vs lines expressing it (46) | 1.43× lower at baseline in the lines without NRTN | 0.0999 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, ATP11A, BRME1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.6, -2.6); signed map (-28.1, 21.0). **Vector** length 49.4, 7.20% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +10.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.6 | +8.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.5 | +8.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +3.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -3.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | neurturin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:5,805,067-5,828,324 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NTN |
| Gene groups (HGNC) | GDNF family ligands |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 8 pathways, smallest: NCAM1 interactions; RET signaling; NCAM signaling for neurite out-growth |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99748](https://www.uniprot.org/uniprotkb/Q99748) (Neurturin):

> Growth factor that supports the survival of sympathetic neurons in culture. May regulate the development and maintenance of the CNS. Involved in the development of the neural crest. Might control the size of non-neuronal cell population such as haemopoietic cells. Acts by binding to its coreceptor, GFRA2, leading to autophosphorylation and activation of the RET receptor. Heparan sulfate-binding is required for signaling.

**Summary**, from NCBI Gene [4902](https://www.ncbi.nlm.nih.gov/gene/4902):

> This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. The encoded preproprotein is proteolytically processed to generate the mature protein. This protein signals through the RET receptor tyrosine kinase and a GPI-linked coreceptor, and promotes survival of neuronal populations. A neurturin mutation has been described in a family with Hirschsprung Disease. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:8007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8007) · Entrez [4902](https://www.ncbi.nlm.nih.gov/gene/4902) · UniProt [Q99748](https://www.uniprot.org/uniprotkb/Q99748) · Ensembl [ENSG00000171119](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171119)

## Data

Gene col 10053: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10053); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10053, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10053]; `tensor/DDL_lfc|DDL_z.npy` [10053]; `embed/gene_vectors.npy` [10053]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10053 or target_col == 10053). Every well: [[NRTN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRTN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
