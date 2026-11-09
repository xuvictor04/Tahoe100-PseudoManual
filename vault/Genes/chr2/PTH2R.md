---
symbol: "PTH2R"
type: "gene"
col: 6877
ensembl_id: "ENSG00000144407"
name: "parathyroid hormone 2 receptor"
location: "2q34"
module: 121
arm: "+"
pooled_cpm: 12.91
n_lines_expressing: 14
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# PTH2R

*parathyroid hormone 2 receptor* — 2q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.82× (z +20.9, q 0e+00, up in 5 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.0768×, SNU-423 0.0997×, CHP-212 0.113×); [[Harringtonine (drug)]] 5 µM in 2 lines (A498 0.0784×, SNU-423 0.119×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A498 0.164×, SNU-423 0.233×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.269×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTN6]] (+0.65, fdr 1e-05), [[TEX41]] (+0.57, fdr 1e-05), [[CASC15]] (+0.53, fdr 3e-05); moves opposite to [[SDC3]] (-0.42, fdr 8e-05), [[MCAM]] (-0.41, fdr 2e-04), [[TBC1D2B]] (-0.41, fdr 3e-04).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[SEMA6D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6877.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.82×** | +20.9 | 0e+00 | 5/10 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.21×** | +11.9 | 3e-30 | 1/6 (SHP-77) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.68×** | +10.9 | 3e-25 | 3/9 (HEC-1-A, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +10.2 | 2e-22 | 5/11 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.35×** | +9.4 | 4e-19 | 7/12 (C32, SHP-77, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.04×** | +7.9 | 3e-13 | 3/12 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +7.9 | 3e-13 | 0/4 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +5.6 | 2e-06 | 2/12 (C32, SHP-77) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.6 | 2e-06 | 1/12 (LOX-IMVI) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +5.2 | 1e-05 | 3/11 (LOX-IMVI, H4, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.7 | 1e-04 | 2/11 (SK-MEL-2, HEC-1-A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +4.4 | 5e-04 | 2/12 (C32, SK-MEL-2) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.004 | 2/10 (HEC-1-A, A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +3.7 | 0.008 | 1/9 (NCI-H2030) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.40×** | +3.5 | 0.016 | 2/11 (LOX-IMVI, A498) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.73×** | +3.2 | 0.047 | 1/9 (SHP-77) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.054 | 3/11 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.069 | 4/12 (CHP-212, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.080 | 0/12 | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6877.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.0768×, SNU-423 0.0997×, CHP-212 0.113×); [[Harringtonine (drug)]] 5 µM in 2 lines (A498 0.0784×, SNU-423 0.119×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A498 0.164×, SNU-423 0.233×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.269×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vortioxetine (drug)]] 0.05 µM |  | 0.763× | -3.0 | 0.59 | 3/12 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6877. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 148 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0997× (z -19.2) |
| [[HEC-1-A (line)]] | alt | 6.46 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +9.4) | — |
| [[A498 (line)]] | wt | 170 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0768× (z -19.3) |
| [[CHP-212 (line)]] | wt | 56.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -11.4) |
| [[NCI-H661 (line)]] | alt | 74.3 | 0 | 1 | — | [[Verteporfin (drug)]] 0.05 µM 0.0327× (z -10.1) |
| [[A-172 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.78 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6877), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTN6]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[TEX41]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CASC15]] | +0.53 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[C9]] | +0.53 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[PREX2]] | +0.52 | +0.43 / +0.54 | both halves | 4e-05 |  |
| [[DOK6]] | +0.51 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[LINC01320]] | +0.51 | +0.32 / +0.47 | both halves | 2e-04 |  |
| [[GLIS1]] | +0.50 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[LINC02268]] | +0.49 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[LINC01798]] | +0.47 | +0.44 / +0.35 | both halves | 1e-04 |  |
| [[EPHA6]] | +0.47 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[PTGFR]] | +0.47 | +0.41 / +0.47 | both halves | 4e-05 | pathway: GPCR ligand binding |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDC3]] | -0.42 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[MCAM]] | -0.41 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[TBC1D2B]] | -0.41 | -0.41 / -0.27 | both halves | 3e-04 |  |
| [[MED14]] | -0.41 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[CTNNBIP1]] | -0.40 | -0.36 / -0.23 | both halves | 5e-04 |  |
| [[INPP5F]] | -0.39 | -0.37 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PTH2R's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6D]] | B | PTH2R activity raises SEMA6D's level | lines that do not express PTH2R (36) vs lines expressing it (14) | 2.60× lower at baseline in the lines without PTH2R | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, ENSG00000286523, CNTN6; maybe low, not absent |
| [[RALYL]] | B | PTH2R activity raises RALYL's level | lines that do not express PTH2R (36) vs lines expressing it (14) | 2.41× lower at baseline in the lines without PTH2R | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, ENSG00000286523, CNTN6; maybe low, not absent |
| [[LINC02882]] | C | PTH2R activity raises LINC02882's level | lines that do not express PTH2R (36) vs lines expressing it (14) | 3.54× lower at baseline in the lines without PTH2R | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, ENSG00000286523, CNTN6; maybe low, not absent; co-absent with the target |
| [[LINC01320]] | C | PTH2R activity raises LINC01320's level | lines that do not express PTH2R (36) vs lines expressing it (14) | 4.53× lower at baseline in the lines without PTH2R | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, ENSG00000286523, CNTN6; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.426). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.1, 24.8); signed map (42.8, 27.3). **Vector** length 33.4, 8.09% of its response variance represented; |z| ≥ 3 in 315 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +10.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +20.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +11.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +5.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | +1.1 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | +0.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.8 | -1.1 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -0.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | parathyroid hormone 2 receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q34 — chr2:208,359,714-208,854,503 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PTHR2 |
| Gene groups (HGNC) | Parathyroid hormone receptors |
| Reactome | 5 pathways, smallest: Class B/2 (Secretin family receptors); G alpha (s) signalling events; GPCR ligand binding |
| Matched by | ensembl_id |

**Function**, from UniProt [P49190](https://www.uniprot.org/uniprotkb/P49190) (Parathyroid hormone 2 receptor):

> This is a specific receptor for parathyroid hormone. The activity of this receptor is mediated by G proteins which activate adenylyl cyclase. PTH2R may be responsible for PTH effects in a number of physiological systems. It may play a significant role in pancreatic function. PTH2R presence in neurons indicates that it may function as a neurotransmitter receptor (By similarity).

**Summary**, from NCBI Gene [5746](https://www.ncbi.nlm.nih.gov/gene/5746):

> The protein encoded by this gene is a member of the G-protein coupled receptor 2 family. This protein is a receptor for parathyroid hormone (PTH). This receptor is more selective in ligand recognition and has a more specific tissue distribution compared to parathyroid hormone receptor 1 (PTHR1). It is activated only by PTH and not by parathyroid hormone-like hormone (PTHLH) and is particularly abundant in brain and pancreas. Alternative splicing results in multiple transcript variants. …

**Accessions** — [HGNC:9609](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9609) · Entrez [5746](https://www.ncbi.nlm.nih.gov/gene/5746) · UniProt [P49190](https://www.uniprot.org/uniprotkb/P49190) · Ensembl [ENSG00000144407](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144407)

## Data

Gene col 6877: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6877); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6877, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6877]; `tensor/DDL_lfc|DDL_z.npy` [6877]; `embed/gene_vectors.npy` [6877]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6877 or target_col == 6877). Every well: [[PTH2R — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTH2R.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
