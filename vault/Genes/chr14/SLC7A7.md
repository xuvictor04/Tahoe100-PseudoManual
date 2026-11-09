---
symbol: "SLC7A7"
type: "gene"
col: 7897
ensembl_id: "ENSG00000155465"
name: "solute carrier family 7 member 7"
location: "14q11.2"
module: 90
arm: "+"
pooled_cpm: 2.72
n_lines_expressing: 48
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# SLC7A7

*solute carrier family 7 member 7* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.59× (z +23.5, q 0e+00, up in 23 of 23 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.305×); [[Menadione (drug)]] 0.05 µM in 1 line (A549 0.0635×); [[Digitoxin (drug)]] 5 µM in 1 line (COLO 205 0.113×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLVS1]] (+0.66, fdr 1e-05), [[CCDC170]] (+0.66, fdr 1e-05), [[GRM7]] (+0.64, fdr 1e-05); moves opposite to [[STUB1]] (-0.52, fdr 6e-04).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HLA-DRA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7897.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.59×** | +23.5 | 0e+00 | 23/23 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.65×** | +13.3 | 7e-38 | 15/27 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.82×** | +12.5 | 3e-33 | 3/4 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.96×** | +10.5 | 1e-23 | 7/10 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.07×** | +10.0 | 2e-21 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.48×** | +8.8 | 2e-16 | 13/31 (SW480, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +7.5 | 4e-12 | 16/39 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +6.8 | 6e-10 | 6/41 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.94×** | +6.4 | 1e-08 | 16/33 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +5.7 | 6e-07 | 2/14 (HCT15, LS 180) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +5.7 | 8e-07 | 7/27 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +5.4 | 3e-06 | 5/40 (NCI-H2347, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.0 | 2e-05 | 5/20 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +4.6 | 2e-04 | 6/29 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.31×** | +4.2 | 9e-04 | 0/10 | inconsistent across doses | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.74×** | +3.8 | 0.004 | 1/12 (A549) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.44×** | +3.5 | 0.015 | 5/38 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +3.3 | 0.022 | 4/30 (COLO 205, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.022 | 3/39 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +3.3 | 0.024 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7897.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.305×); [[Menadione (drug)]] 0.05 µM in 1 line (A549 0.0635×); [[Digitoxin (drug)]] 5 µM in 1 line (COLO 205 0.113×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.709× | -3.4 | 0.40 | 7/37 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Decitabine (drug)]] 5 µM |  | 0.727× | -3.0 | 0.47 | 5/30 (SNU-423, KATO III, …) | top dose only | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.718× | -3.0 | 0.47 | 3/39 (H4, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7897. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 16.7 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 3.74× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -10.9) |
| [[A-172 (line)]] | wt | 1.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.2× (z +8.5) | — |
| [[A549 (line)]] | wt | 5.59 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0635× (z -8.8) |
| [[C32 (line)]] | wt | 1.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 50.0× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 1.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.85× (z +9.0) | — |
| [[LoVo (line)]] | wt | 3.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.13× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 1.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +8.6) | — |
| [[A-427 (line)]] | wt | 0.960 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.987 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.829 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.785 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.789 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.653 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.990 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.927 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7897), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLVS1]] | +0.66 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CCDC170]] | +0.66 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[GRM7]] | +0.64 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[LINC02006]] | +0.63 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ELAPOR1]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[LINC01483]] | +0.61 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[CEACAM16-AS1]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[HSD11B1-AS1]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[DGUOK-AS1]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[LINC02694]] | +0.61 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[LINC00578]] | +0.60 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[LINC02608]] | +0.60 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STUB1]] | -0.52 | -0.43 / -0.21 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-DRA]] | B | HLA-DRA activity raises SLC7A7's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 1.40× lower at baseline in the lines without HLA-DRA | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |
| [[TOP2A]] | B | TOP2A activity lowers SLC7A7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[QPCT]] | B | QPCT activity raises SLC7A7's level | lines that do not express QPCT (25) vs lines expressing it (25) | 1.23× lower at baseline in the lines without QPCT | 0.072 | ⚠ within organs, on part of the lines; also absent: WFDC10B, LRRN1, KRT81 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.638). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.6, 26.4); signed map (35.3, 12.6). **Vector** length 42.7, 5.35% of its response variance represented; |z| ≥ 3 in 854 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +23.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +6.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +0.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -0.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -0.9 | -1.7 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.9 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 7 member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:22,773,222-22,829,820 (-) |
| Ensembl biotype | protein_coding |
| Also known as | y+LAT-1, Y+LAT1; previously LPI |
| Gene groups (HGNC) | Solute carrier family 7 |
| Reactome | 9 pathways, smallest: Basigin interactions; Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UM01](https://www.uniprot.org/uniprotkb/Q9UM01) (Y+L amino acid transporter 1):

> Heterodimer with SLC3A2, that functions as an antiporter which operates as an efflux route by exporting cationic amino acids from inside the cells in exchange with neutral amino acids plus sodium ions and may participate in nitric oxide synthesis via the transport of L-arginine. Also mediates arginine transport in non-polarized cells, such as monocytes, and is essential for the correct function of these cells. The transport mechanism is electroneutral and operates with a stoichiometry of 1:1 …

**Summary**, from NCBI Gene [9056](https://www.ncbi.nlm.nih.gov/gene/9056):

> The protein encoded by this gene is the light subunit of a cationic amino acid transporter. This sodium-independent transporter is formed when the light subunit encoded by this gene dimerizes with the heavy subunit transporter protein SLC3A2. This transporter is found in epithelial cell membranes where it transfers cationic and large neutral amino acids from the cell to the extracellular space. Defects in this gene are a cause of lysinuric protein intolerance (LPI). Alternative splicing results …

**Accessions** — [HGNC:11065](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11065) · Entrez [9056](https://www.ncbi.nlm.nih.gov/gene/9056) · UniProt [Q9UM01](https://www.uniprot.org/uniprotkb/Q9UM01) · Ensembl [ENSG00000155465](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155465)

## Data

Gene col 7897: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7897); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7897, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7897]; `tensor/DDL_lfc|DDL_z.npy` [7897]; `embed/gene_vectors.npy` [7897]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7897 or target_col == 7897). Every well: [[SLC7A7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC7A7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
