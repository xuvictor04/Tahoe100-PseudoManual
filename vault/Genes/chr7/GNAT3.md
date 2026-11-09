---
symbol: "GNAT3"
type: "gene"
col: 13201
ensembl_id: "ENSG00000214415"
name: "G protein subunit alpha transducin 3"
location: "7q21.11"
module: 27
arm: "+"
pooled_cpm: 2.44
n_lines_expressing: 18
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 6
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# GNAT3

*G protein subunit alpha transducin 3* — 7q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.52× (z +11.2, q 1e-26, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.60× (z +8.4, q 5e-15, up in 2 of 4 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.150×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (SW48 0.162×; ⚠ unreliable plate only).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR15]] (+0.68, fdr 1e-05), [[CD36]] (+0.62, fdr 7e-06, ⚠ same locus), [[LINC01956]] (+0.56, fdr 4e-05), [[FGF20]] (+0.51, fdr 3e-05); moves opposite to [[RALB]] (-0.45, fdr 2e-04), [[STX1A]] (-0.43, fdr 2e-04), [[STXBP1]] (-0.41, fdr 2e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[KCNB2]] → it (grade C ⚠); 6 go from it, the strongest it → [[RBMS3-AS3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13201.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.52×** | +11.2 | 1e-26 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.61×** | +9.5 | 4e-19 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.80×** | +9.1 | 3e-17 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +8.4 | 5e-15 | 2/4 (C32, HEC-1-A) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +6.5 | 8e-09 | 2/7 (C32, HEC-1-A) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +4.5 | 6e-04 | 0/2 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.76×** | +4.3 | 0.001 | 0/0 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.0 | 0.005 | 0/2 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.29×** | +3.7 | 0.014 | 0/1 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.79×** | +3.6 | 0.016 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +3.5 | 0.028 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.037 | 1/12 (SW48) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.65×** | +3.1 | 0.081 | 3/8 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.64×** | +3.1 | 0.084 | 0/2 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13201.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.150×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (SW48 0.162×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[MK-8353 (drug)]] 0.5 µM |  | 0.507× | -3.0 | 0.98 | 1/13 (HEC-1-A) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13201. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 209 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -12.7) |
| [[A-172 (line)]] | wt | 0.569 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.952 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.471 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.996 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.643 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.574 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.618 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.688 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.640 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.617 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.510 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.614 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.578 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.669 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.713 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.516 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.805 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.640 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.476 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13201), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR15]] | +0.68 | +0.50 / +0.60 | both halves | 1e-05 | pathway: G alpha (s) signalling events |
| [[CD36]] | +0.62 | +0.67 / +0.59 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 434; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[LINC01956]] | +0.56 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[FGF20]] | +0.51 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[RALYL]] | +0.50 | +0.44 / +0.37 | both halves | 9e-05 |  |
| [[CCSER1]] | +0.49 | +0.43 / +0.39 | both halves | 5e-05 |  |
| [[PDK4-AS1]] | +0.49 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[LINC01622]] | +0.49 | +0.36 / +0.46 | both halves | 9e-05 |  |
| [[PTPRO]] | +0.49 | +0.46 / +0.37 | both halves | 7e-05 |  |
| [[AXIN2]] | +0.46 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[PPP1R9A]] | +0.46 | +0.43 / +0.33 | both halves | 1e-04 |  |
| [[OVOL2]] | +0.46 | +0.44 / +0.17 | ⚠ not reproduced | 0.001 |  |
| [[PPP1R9A-AS1]] | +0.46 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[PRSS48]] | +0.45 | +0.38 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALB]] | -0.45 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[STX1A]] | -0.43 | -0.34 / -0.31 | both halves | 2e-04 | pathway: Neuronal System |
| [[STXBP1]] | -0.41 | -0.29 / -0.39 | both halves | 2e-04 | pathway: Neuronal System |
| [[TPD52L2]] | -0.41 | -0.35 / -0.25 | both halves | 4e-04 |  |
| [[ARPC1B]] | -0.40 | -0.31 / -0.28 | both halves | 3e-04 | pathway: Leishmania infection |
| [[NIBAN2]] | -0.40 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[PPM1F]] | -0.39 | -0.33 / -0.30 | both halves | 2e-04 | pathway: Neuronal System |
| [[MAP2K1]] | -0.39 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[A2M]] | -0.39 | -0.31 / -0.44 | both halves | 2e-04 | pathway: Platelet activation, signaling and aggregation |
| [[RHBDF2]] | -0.39 | -0.35 / -0.27 | both halves | 3e-04 | pathway: Anti-inflammatory response favouring Leishmania parasite infection |
| [[ST6GALNAC6]] | -0.39 | -0.38 / -0.21 | both halves | 6e-04 |  |
| [[PDLIM7]] | -0.39 | -0.30 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNB2]] | C | KCNB2 activity raises GNAT3's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.61× lower at baseline in the lines without KCNB2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[A2M]] | C | A2M activity raises GNAT3's level | lines that do not express A2M (42) vs lines expressing it (8) | 1.18× lower at baseline in the lines without A2M | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[GPR15]] | C | GPR15 activity raises GNAT3's level | lines that do not express GPR15 (46) vs lines expressing it (4) | 5.49× lower at baseline in the lines without GPR15 | 0.002 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GCG, APOB, BMP10; co-absent with the target |
| [[LINC01956]] | C | LINC01956 activity raises GNAT3's level | lines that do not express LINC01956 (38) vs lines expressing it (12) | 2.26× lower at baseline in the lines without LINC01956 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01440, SYT4, LINC03000; co-absent with the target |
| [[BMP10]] | C | BMP10 activity raises GNAT3's level | lines that do not express BMP10 (47) vs lines expressing it (3) | 1.60× lower at baseline in the lines without BMP10 | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, APOB, TBXT; co-absent with the target; its own permutation p |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBMS3-AS3]] | B | GNAT3 activity raises RBMS3-AS3's level | lines that do not express GNAT3 (32) vs lines expressing it (18) | 1.34× lower at baseline in the lines without GNAT3 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MEOX2, IHO1, ZFHX4-AS1; maybe low, not absent |
| cells under [[Pralsetinib (drug)]] 5 µM | B | GNAT3 activity raises the cells' numbers under Pralsetinib 5 µM (protects the cells) | lines that do not express GNAT3 (32) vs lines expressing it (16) | the lines without GNAT3: 0.74× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MEOX2, IHO1, ZFHX4-AS1; maybe low, not absent |
| [[CD36]] | C | GNAT3 activity raises CD36's level | lines that do not express GNAT3 (32) vs lines expressing it (18) | 3.41× lower at baseline in the lines without GNAT3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MEOX2, IHO1, ZFHX4-AS1; maybe low, not absent; co-absent with the target |
| [[AXIN2]] | C | GNAT3 activity raises AXIN2's level | lines that do not express GNAT3 (32) vs lines expressing it (18) | 1.33× lower at baseline in the lines without GNAT3 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MEOX2, IHO1, ZFHX4-AS1; maybe low, not absent; co-absent with the target |
| [[GPR15]] | C | GNAT3 activity raises GPR15's level | lines that do not express GNAT3 (32) vs lines expressing it (18) | 1.87× lower at baseline in the lines without GNAT3 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MEOX2, IHO1, ZFHX4-AS1; maybe low, not absent; co-absent with the target |
| [[ZFHX4-AS1]] | C | GNAT3 activity raises ZFHX4-AS1's level | lines that do not express GNAT3 (32) vs lines expressing it (18) | 2.78× lower at baseline in the lines without GNAT3 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MEOX2, IHO1, ZFHX4-AS1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.402). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.4, 36.8); signed map (47.4, 29.1). **Vector** length 11.1, 1.52% of its response variance represented; |z| ≥ 3 in 200 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +1.0 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.6 | +8.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +0.6 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.5 | +0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.4 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.3 | +0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.2 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.2 | +2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +0.2 | +0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.2 | +2.4 |
| fall | [[Mebendazole (drug)]] 5 µM |  | -0.3 | -1.3 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -0.3 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.2 | -0.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.2 | -1.7 |
|  | [[Ralimetinib dimesylate (drug)]] 5 µM |  | -0.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit alpha transducin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.11 — chr7:80,458,635-80,512,064 (-) |
| Ensembl biotype | protein_coding |
| Also known as | gustducin, GDCA |
| Gene groups (HGNC) | G protein subunits alpha, group i |
| Reactome | 33 pathways, smallest: Adenylate cyclase inhibitory pathway; Sensory perception of sweet, bitter, and umami (glutamate) taste; Sensory perception of taste |
| Matched by | ensembl_id |

**Function**, from UniProt [A8MTJ3](https://www.uniprot.org/uniprotkb/A8MTJ3) (Guanine nucleotide-binding protein G(t) subunit alpha-3):

> Guanine nucleotide-binding protein (G protein) alpha subunit playing a prominent role in bitter and sweet taste transduction as well as in umami (monosodium glutamate, monopotassium glutamate, and inosine monophosphate) taste transduction. Transduction by this alpha subunit involves coupling of specific cell-surface receptors with a cGMP-phosphodiesterase; Activation of phosphodiesterase lowers intracellular levels of cAMP and cGMP which may open a cyclic nucleotide-suppressible cation channel …

**Summary**, from NCBI Gene [346562](https://www.ncbi.nlm.nih.gov/gene/346562):

> Sweet, bitter, and umami tastes are transmitted from taste receptors by a specific guanine nucleotide binding protein. The protein encoded by this gene is the alpha subunit of this heterotrimeric G protein, which is found not only in the oral epithelium but also in gut tissues. Variations in this gene have been linked to metabolic syndrome. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:22800](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22800) · Entrez [346562](https://www.ncbi.nlm.nih.gov/gene/346562) · UniProt [A8MTJ3](https://www.uniprot.org/uniprotkb/A8MTJ3) · Ensembl [ENSG00000214415](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214415)

## Data

Gene col 13201: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13201); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13201, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13201]; `tensor/DDL_lfc|DDL_z.npy` [13201]; `embed/gene_vectors.npy` [13201]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13201 or target_col == 13201). Every well: [[GNAT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNAT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
