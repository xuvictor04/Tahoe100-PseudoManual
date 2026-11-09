---
symbol: "NOG"
type: "gene"
col: 11438
ensembl_id: "ENSG00000183691"
name: "noggin"
location: "17q22"
module: 144
arm: "+"
pooled_cpm: 12.42
n_lines_expressing: 24
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# NOG

*noggin* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.24× (z +5.4, q 5e-05, up in 1 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +5.1, q 9e-05, up in 3 of 21 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 1 line (Hs 766T 7.52×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.331× (z -7.6, q 1e-11, down in 21 of 21 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IMP3]] (+0.70, fdr 1e-05), [[FUT11]] (+0.64, fdr 1e-05), [[NR2F2]] (+0.63, fdr 3e-05); moves opposite to [[PRELID3B]] (-0.55, fdr 1e-04), [[ANXA7]] (-0.54, fdr 1e-04), [[PSMD11]] (-0.54, fdr 5e-05).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KDM2B-DT]] → it (grade B ⚠); 3 go from it, the strongest it → [[GSR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11438.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 1 line (Hs 766T 7.52×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +5.4 | 5e-05 | 1/13 (NCI-H2030) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +5.1 | 9e-05 | 3/21 (NCI-H460, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +4.7 | 6e-04 | 0/17 | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.87×** | +4.3 | 0.002 | 6/20 (Hs 766T, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.5 | 0.050 | 3/18 (NCI-H2030, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 2.10× | +3.2 | 0.13 | 4/21 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.56× | +3.1 | 0.16 | 6/21 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |
| [[Silodosin (drug)]] 5 µM |  | 1.58× | +3.1 | 0.16 | 10/20 (SK-MEL-2, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11438.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.331×** | -7.6 | 1e-11 | 21/21 (hTERT-HPNE, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.349×** | -6.9 | 2e-09 | 19/21 (hTERT-HPNE, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.408×** | -6.2 | 1e-07 | 19/21 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.522×** | -4.5 | 0.001 | 17/21 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.525×** | -4.4 | 0.001 | 20/21 (hTERT-HPNE, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.643×** | -4.3 | 0.002 | 17/20 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.556×** | -3.9 | 0.008 | 16/21 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.575×** | -3.8 | 0.010 | 17/21 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.567×** | -3.6 | 0.019 | 10/21 (NCI-H460, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.578×** | -3.5 | 0.026 | 8/21 (Hs 766T, Panc 03.27, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.573×** | -3.4 | 0.040 | 11/22 (Hs 766T, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.710×** | -3.3 | 0.050 | 7/21 (Hs 766T, J82, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.601×** | -3.2 | 0.051 | 6/21 (Hs 766T, PANC-1, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.401×** | -3.2 | 0.055 | 16/21 (Panc 03.27, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11438. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 48.0 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0415× (z -15.8) |
| [[MIA PaCa-2 (line)]] | alt | 43.2 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0586× (z -20.7) |
| [[PANC-1 (line)]] | alt | 15.3 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -14.9) |
| [[HOP62 (line)]] | alt | 18.2 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0630× (z -13.3) |
| [[A-172 (line)]] | wt | 104 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0747× (z -20.4) |
| [[Hs 766T (line)]] | wt | 38.9 | 1 (1 ⚠) | 4 | [[Digitoxin (drug)]] 5 µM 7.52× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 24.2 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0907× (z -10.9) |
| [[SNU-423 (line)]] | alt | 82.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0481× (z -15.0) |
| [[CFPAC-1 (line)]] | alt | 21.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0902× (z -10.2) |
| [[J82 (line)]] | alt | 19.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0857× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 34.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0852× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0805× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 4.54 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 7.28 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0441× (z -9.8) |
| [[A-427 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.953 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.953 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.827 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.892 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.903 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.49 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11438), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMP3]] | +0.70 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[FUT11]] | +0.64 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[NR2F2]] | +0.63 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[RNF122]] | +0.59 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[POM121C]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[VKORC1]] | +0.58 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[B3GAT3]] | +0.57 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[CCDC107]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[POLR2H]] | +0.56 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[ZNF8-DT]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[C4orf47]] | +0.55 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[TRIM7-AS2]] | +0.55 | +0.31 / +0.57 | both halves | 2e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRELID3B]] | -0.55 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[ANXA7]] | -0.54 | -0.35 / -0.65 | both halves | 1e-04 |  |
| [[PSMD11]] | -0.54 | -0.39 / -0.58 | both halves | 5e-05 | pathway: Formation of paraxial mesoderm |
| [[GSR]] | -0.53 | -0.39 / -0.61 | both halves | 6e-05 |  |
| [[API5]] | -0.51 | -0.23 / -0.64 | both halves | 5e-04 |  |
| [[EWSR1]] | -0.51 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[LIN7C]] | -0.49 | -0.25 / -0.58 | both halves | 4e-04 |  |
| [[PLEKHA3]] | -0.48 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[IDE]] | -0.48 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[CNBP]] | -0.48 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[SLC25A24]] | -0.47 | -0.18 / -0.49 | ⚠ not reproduced | 9e-04 |  |
| [[UBQLN1]] | -0.47 | -0.15 / -0.58 | ⚠ one half (not replicated) | 0.001 |  |
| [[LPGAT1]] | -0.47 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[OCRL]] | -0.47 | -0.21 / -0.56 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDM2B-DT]] | B | KDM2B-DT activity raises NOG's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 3.28× lower at baseline in the lines without KDM2B-DT | 0.067 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSR]] | B | NOG activity lowers GSR's level | lines that do not express NOG (26) vs lines expressing it (24) | 1.83× higher at baseline in the lines without NOG | 0.028 | ⚠ within organs, on part of the lines; also absent: LINC01776, ENSG00000279289, FLI1 |
| [[HDAC3]] | B | NOG activity raises HDAC3's level | lines that do not express NOG (26) vs lines expressing it (24) | 1.19× lower at baseline in the lines without NOG | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC01776, ENSG00000279289, FLI1 |
| [[RALGDS]] | B | NOG activity raises RALGDS's level | lines that do not express NOG (26) vs lines expressing it (24) | 1.19× lower at baseline in the lines without NOG | 0.096 | ⚠ within organs, on part of the lines; also absent: LINC01776, ENSG00000279289, FLI1 |

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.8, -19.3); signed map (-32.4, 31.2). **Vector** length 60.5, 16.4% of its response variance represented; |z| ≥ 3 in 521 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.6 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +0.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.3 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | -1.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.2 | +1.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.1 | +3.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.6 | +4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | +5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.8 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.5 | -3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -1.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -3.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | noggin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:56,593,699-56,595,611 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SYNS1, SYM1 |
| Gene groups (HGNC) | Noggin family |
| Hallmark sets | TGF_BETA_SIGNALING |
| Reactome | 4 pathways, smallest: Signaling by BMP; Formation of paraxial mesoderm; Gastrulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13253](https://www.uniprot.org/uniprotkb/Q13253) (Noggin):

> Inhibitor of bone morphogenetic proteins (BMP) signaling which is required for growth and patterning of the neural tube and somite. Essential for cartilage morphogenesis and joint formation. Inhibits chondrocyte differentiation through its interaction with GDF5 and, probably, GDF6.

**Summary**, from NCBI Gene [9241](https://www.ncbi.nlm.nih.gov/gene/9241):

> The secreted polypeptide, encoded by this gene, binds and inactivates members of the transforming growth factor-beta (TGF-beta) superfamily signaling proteins, such as bone morphogenetic protein-4 (BMP4). By diffusing through extracellular matrices more efficiently than members of the TGF-beta superfamily, this protein may have a principal role in creating morphogenic gradients. The protein appears to have pleiotropic effect, both early in development as well as in later stages. It was …

**Accessions** — [HGNC:7866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7866) · Entrez [9241](https://www.ncbi.nlm.nih.gov/gene/9241) · UniProt [Q13253](https://www.uniprot.org/uniprotkb/Q13253) · Ensembl [ENSG00000183691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183691)

## Data

Gene col 11438: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11438); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11438, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11438]; `tensor/DDL_lfc|DDL_z.npy` [11438]; `embed/gene_vectors.npy` [11438]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11438 or target_col == 11438). Every well: [[NOG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
