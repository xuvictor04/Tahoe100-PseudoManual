---
symbol: "PCDH17"
type: "gene"
col: 4028
ensembl_id: "ENSG00000118946"
name: "protocadherin 17"
location: "13q21.1"
module: 9
arm: "+"
pooled_cpm: 4.39
n_lines_expressing: 21
n_dd_up: 31
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PCDH17

*protocadherin 17* — 13q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.96× (z +21.9, q 0e+00, up in 12 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.594× (z -4.2, q 0.014, down in 6 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCDH10]] (+0.75, fdr 7e-06), [[RORB]] (+0.72, fdr 7e-06), [[B3GALT1]] (+0.65, fdr 7e-06); moves opposite to [[CROCCP3]] (-0.47, fdr 2e-04), [[NUDCD3]] (-0.46, fdr 8e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PCDH10]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4028.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.96×** | +21.9 | 0e+00 | 12/15 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.52×** | +19.3 | 0e+00 | 10/15 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.04×** | +12.4 | 4e-33 | 1/9 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.91×** | +10.9 | 2e-25 | 0/10 | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.41×** | +9.9 | 4e-21 | 15/17 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.21×** | +9.3 | 1e-18 | 8/14 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.31×** | +8.8 | 9e-17 | 3/9 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.85×** | +8.0 | 7e-14 | 6/11 (HOP62, J82, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.71×** | +7.9 | 1e-13 | 8/13 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.62×** | +7.7 | 1e-12 | 9/17 (SK-MEL-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.39×** | +6.9 | 2e-10 | 10/17 (LOX-IMVI, CFPAC-1, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.20×** | +6.3 | 2e-08 | 8/15 (HOP62, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.19×** | +6.0 | 8e-08 | 10/16 (LOX-IMVI, J82, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +5.9 | 1e-07 | 4/10 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.99×** | +5.5 | 2e-06 | 11/16 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +5.2 | 7e-06 | 8/14 (HOP62, J82, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.0 | 2e-05 | 8/17 (J82, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +3.9 | 0.003 | 6/17 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.016 | 3/17 (J82, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +3.4 | 0.017 | 11/17 (SK-MEL-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.53×** | +3.4 | 0.017 | 0/12 | inconsistent across doses | low cells (technical?) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.49×** | +3.1 | 0.036 | 2/17 (A-172, SHP-77) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.050 | 2/14 (NCI-H23, SHP-77) | rises with dose | cell-cycle shift (explains ~22% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4028.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.594×** | -4.2 | 0.014 | 6/17 (NCI-H2347, C32, …) | all doses, flat | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | **0.627×** | -3.8 | 0.039 | 0/17 | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.725×** | -3.7 | 0.039 | 6/17 (LOX-IMVI, NCI-H2030, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **0.649×** | -3.5 | 0.062 | 6/17 (NCI-H2347, CHP-212, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.669× | -3.3 | 0.12 | 4/17 (SHP-77, RPMI-7951, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.691× | -3.0 | 0.25 | 3/17 (RPMI-7951, CHP-212, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4028. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 5.55 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 36.8× (z +15.8) | — |
| [[J82 (line)]] | alt | 23.7 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +15.5) | — |
| [[LOX-IMVI (line)]] | wt | 47.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +17.8) | — |
| [[C32 (line)]] | wt | 14.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.0× (z +13.8) | — |
| [[CFPAC-1 (line)]] | alt | 4.29 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.3× (z +12.6) | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +9.7) | — |
| [[CHP-212 (line)]] | wt | 76.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0427× (z -10.7) ⚠ transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 3.31 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 49.5× (z +8.7) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[SHP-77 (line)]] | alt | 30.4 | 0 | 1 | — | [[Binimetinib (drug)]] 5 µM 0.169× (z -8.5) |
| [[A-172 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.862 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.929 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.908 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.943 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.286 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.348 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4028), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCDH10]] | +0.75 | +0.73 / +0.73 | both halves | 7e-06 | same gene group |
| [[RORB]] | +0.72 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[B3GALT1]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PCDH9]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 | same gene group |
| [[EPHA7]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 | STRING 437 |
| [[SLIT2]] | +0.61 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[LYPD1]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[DMD]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[LINC00958]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[NCAM2]] | +0.57 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[EPHA5]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PEG10]] | +0.56 | +0.59 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP3]] | -0.47 | -0.50 / -0.29 | both halves | 2e-04 |  |
| [[NUDCD3]] | -0.46 | -0.40 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PCDH17's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.2% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[RBP1]] | C | RBP1 activity raises PCDH17's level | lines that do not express RBP1 (37) vs lines expressing it (13) | 1.93× lower at baseline in the lines without RBP1 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ENSG00000260573, LGR5; co-absent with the target |
| [[DDX43]] | C | DDX43 activity raises PCDH17's level | lines that do not express DDX43 (34) vs lines expressing it (16) | 2.18× lower at baseline in the lines without DDX43 | 0.050 | ⚠ within organs, on part of the lines; also absent: SLC34A2, LINC02377, RNF17; co-absent with the target |
| [[NOVA1]] | C | NOVA1 activity raises PCDH17's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 1.72× lower at baseline in the lines without NOVA1 | 0.094 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDH10]] | C | PCDH17 activity raises PCDH10's level | lines that do not express PCDH17 (29) vs lines expressing it (21) | 3.96× lower at baseline in the lines without PCDH17 | 0.076 | ⚠ within organs, on part of the lines; also absent: WNK3, PCDH10, PTPRN; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.8, 29.7); signed map (37.9, 30.4). **Vector** length 45.3, 11.2% of its response variance represented; |z| ≥ 3 in 441 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.8 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +21.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +0.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -4.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -3.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | protocadherin 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q21.1 — chr13:57,631,744-57,729,311 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PCDH68, PCH68 |
| Gene groups (HGNC) | Non-clustered protocadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [O14917](https://www.uniprot.org/uniprotkb/O14917) (Protocadherin-17):

> Potential calcium-dependent cell-adhesion protein.

**Summary**, from NCBI Gene [27253](https://www.ncbi.nlm.nih.gov/gene/27253):

> This gene belongs to the protocadherin gene family, a subfamily of the cadherin superfamily. The encoded protein contains six extracellular cadherin domains, a transmembrane domain, and a cytoplasmic tail differing from those of the classical cadherins. The encoded protein may play a role in the establishment and function of specific cell-cell connections in the brain. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14267](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14267) · Entrez [27253](https://www.ncbi.nlm.nih.gov/gene/27253) · UniProt [O14917](https://www.uniprot.org/uniprotkb/O14917) · Ensembl [ENSG00000118946](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118946)

## Data

Gene col 4028: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4028); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4028, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4028]; `tensor/DDL_lfc|DDL_z.npy` [4028]; `embed/gene_vectors.npy` [4028]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4028 or target_col == 4028). Every well: [[PCDH17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCDH17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
