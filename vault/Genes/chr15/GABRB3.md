---
symbol: "GABRB3"
type: "gene"
col: 9262
ensembl_id: "ENSG00000166206"
name: "gamma-aminobutyric acid type A receptor subunit beta3"
location: "15q12"
module: 102
arm: "+"
pooled_cpm: 17.08
n_lines_expressing: 19
n_dd_up: 35
n_dd_down: 4
n_dd_up_clean: 27
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# GABRB3

*gamma-aminobutyric acid type A receptor subunit beta3* — 15q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.66× (z +31.8, q 0e+00, up in 9 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.754× (z -4.2, q 0.016, down in 2 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRID1]] (+0.65, fdr 1e-05), [[SNTG2]] (+0.62, fdr 1e-05), [[SLC6A17]] (+0.59, fdr 2e-05); moves opposite to [[GLE1]] (-0.42, fdr 2e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PCDHA6]] → it (grade B ⚠); 2 go from it, the strongest it → [[PCDHA6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9262.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.66×** | +31.8 | 0e+00 | 9/16 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.56×** | +19.4 | 0e+00 | 5/15 (CFPAC-1, H4, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.54×** | +19.2 | 0e+00 | 8/16 (A498, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.50×** | +18.3 | 0e+00 | 10/16 (A498, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.22×** | +17.1 | 0e+00 | 4/12 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.22×** | +17.1 | 0e+00 | 11/16 (A498, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.83×** | +15.2 | 0e+00 | 9/16 (A498, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +12.3 | 4e-33 | 2/9 (A549, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.15×** | +11.2 | 4e-27 | 7/16 (H4, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +11.0 | 2e-26 | 7/15 (SW1417, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +10.2 | 1e-22 | 5/12 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.71×** | +7.5 | 4e-12 | 5/16 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +6.9 | 2e-10 | 6/16 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +6.8 | 4e-10 | 7/16 (H4, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +5.3 | 4e-06 | 3/16 (BT-474, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.1 | 1e-05 | 1/15 (RKO) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 3e-04 | 0/16 | inconsistent across doses | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.74×** | +4.2 | 8e-04 | 5/16 (H4, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9262.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.754×** | -4.2 | 0.016 | 2/16 (CFPAC-1, SW 900) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.626×** | -3.6 | 0.062 | 7/14 (A-427, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.786×** | -3.6 | 0.062 | 1/16 (SW 1271) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.774×** | -3.5 | 0.062 | 0/16 | inconsistent across doses |  |
| [[Hexylresorcinol (drug)]] 5 µM |  | 0.855× | -3.3 | 0.11 | 6/17 (NCI-H2030, A-427, …) | rises with dose | position effect removed |
| [[Clopidogrel (drug)]] 0.5 µM |  | 0.808× | -3.2 | 0.14 | 0/16 | inconsistent across doses |  |
| [[Decitabine (drug)]] 5 µM |  | 0.808× | -3.0 | 0.19 | 1/16 (SW 1271) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9262. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 15.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 16.1× (z +21.8) | — |
| [[H4 (line)]] | wt | 56.9 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 12.5× (z +15.8) | [[Dinaciclib (drug)]] 0.05 µM 0.0816× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 21.6 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.22× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.0900× (z -15.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 5.28 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.3× (z +11.8) | — |
| [[A-427 (line)]] | wt | 105 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.113× (z -12.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 22.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.95× (z +12.1) | — |
| [[SHP-77 (line)]] | alt | 223 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +10.9) ⚠ cell-cycle shift, explains ~14% of this change | [[Dinaciclib (drug)]] 5 µM 0.106× (z -21.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 63.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -14.6) |
| [[CFPAC-1 (line)]] | alt | 6.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +10.0) | — |
| [[RKO (line)]] | wt | 8.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[A-172 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.05 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9262), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRID1]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[SNTG2]] | +0.62 | +0.50 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[SLC6A17]] | +0.59 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[TEX15]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[HYDIN]] | +0.58 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[KCNQ2]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 | pathway: Neuronal System; STRING 620 |
| [[CACNA2D2]] | +0.55 | +0.51 / +0.48 | both halves | 2e-05 | pathway: Neuronal System |
| [[CELF4]] | +0.53 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[LINC01194]] | +0.53 | +0.27 / +0.66 | both halves | 3e-04 |  |
| [[SYN2]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 | pathway: Neuronal System |
| [[ULBP3]] | +0.52 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[TMEM108]] | +0.52 | +0.41 / +0.64 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLE1]] | -0.42 | -0.37 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDHA6]] | B | PCDHA6 activity raises GABRB3's level | lines that do not express PCDHA6 (17) vs lines expressing it (33) | 2.70× lower at baseline in the lines without PCDHA6 | 0.077 | ⚠ within organs, on part of the lines; also absent: RAB39A, PHF21B, LONRF2 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDHA6]] | B | GABRB3 activity raises PCDHA6's level | lines that do not express GABRB3 (31) vs lines expressing it (19) | 2.24× lower at baseline in the lines without GABRB3 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000244468, S100A9, FGG |
| [[SNTG2]] | B | GABRB3 activity raises SNTG2's level | lines that do not express GABRB3 (31) vs lines expressing it (19) | 2.40× lower at baseline in the lines without GABRB3 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000244468, S100A9, FGG |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.601). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.6, 37.7); signed map (28.1, 26.3). **Vector** length 33.2, 6.58% of its response variance represented; |z| ≥ 3 in 338 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +17.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +19.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +17.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.9 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -2.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | +0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -3.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -0.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.7 | -2.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | gamma-aminobutyric acid type A receptor subunit beta3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q12 — chr15:26,543,552-26,939,539 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Gamma-aminobutyric acid type A receptor subunits |
| Reactome | 6 pathways, smallest: GABA receptor activation; Signaling by ERBB4; Neurotransmitter receptors and postsynaptic signal transmission |
| Matched by | ensembl_id |

**Function**, from UniProt [P28472](https://www.uniprot.org/uniprotkb/P28472) (Gamma-aminobutyric acid receptor subunit beta-3):

> Beta subunit of the heteropentameric ligand-gated chloride channel gated by gamma-aminobutyric acid (GABA), a major inhibitory neurotransmitter in the brain. GABA-gated chloride channels, also named GABA(A) receptors (GABAAR), consist of five subunits arranged around a central pore and contain GABA active binding site(s) located at the alpha and beta subunit interface(s). GABAARs containing beta-3/GABRB3 subunit are found at both synaptic and extrasynaptic sites (By similarity). When activated …

**Summary**, from NCBI Gene [2562](https://www.ncbi.nlm.nih.gov/gene/2562):

> This gene encodes a member of the ligand-gated ionic channel family. The encoded protein is one the subunits of a multi-subunit chloride channel that serves as the receptor for gamma-aminobutyric acid, a major inhibitory neurotransmitter of the mammalian nervous system. This gene is located on the long arm of chromosome 15 in a cluster with two other genes encoding related subunits of the family. This gene may be associated with the pathogenesis of several disorders including Angelman syndrome, …

**Accessions** — [HGNC:4083](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4083) · Entrez [2562](https://www.ncbi.nlm.nih.gov/gene/2562) · UniProt [P28472](https://www.uniprot.org/uniprotkb/P28472) · Ensembl [ENSG00000166206](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166206)

## Data

Gene col 9262: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9262); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9262, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9262]; `tensor/DDL_lfc|DDL_z.npy` [9262]; `embed/gene_vectors.npy` [9262]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9262 or target_col == 9262). Every well: [[GABRB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GABRB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
