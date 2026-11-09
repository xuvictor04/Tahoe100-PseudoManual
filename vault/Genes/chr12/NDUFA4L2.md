---
symbol: "NDUFA4L2"
type: "gene"
col: 11707
ensembl_id: "ENSG00000185633"
name: "cytochrome c oxidase hypoxia associated subunit FA4L2"
location: "12q13.3"
module: 27
arm: "+"
pooled_cpm: 4.59
n_lines_expressing: 34
n_dd_up: 4
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 10
direction_downstream: 3
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# NDUFA4L2

*cytochrome c oxidase hypoxia associated subunit FA4L2* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.67× (z +6.3, q 1e-07, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Entrectinib (drug)]] 5 µM: 1.84× (z +4.1, q 0.006, up in 12 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.389× (z -6.1, q 4e-07, down in 16 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF703]] (+0.64, fdr 2e-05), [[PKHD1]] (+0.60, fdr 3e-05), [[GLDN]] (+0.60, fdr 2e-05); moves opposite to [[TREX2]] (-0.45, fdr 5e-05), [[CROCCP3-1]] (-0.45, fdr 9e-05), [[ITGB1BP1]] (-0.45, fdr 2e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[WDR72]] → it (grade B ⚠); 3 go from it, the strongest it → [[BTBD16]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11707.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +6.3 | 1e-07 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +4.4 | 0.003 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +4.2 | 0.005 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.84×** | +4.1 | 0.006 | 12/28 (SW480, NCI-H460, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.62× | +3.2 | 0.13 | 2/29 (hTERT-HPNE, RKO) | rises with dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 1.61× | +3.2 | 0.13 | 4/29 (HT-29, NCI-H1792, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11707.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.389×** | -6.1 | 4e-07 | 16/27 (HCT15, SW480, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.429×** | -5.7 | 4e-06 | 20/29 (HT-29, COLO 205, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.426×** | -5.5 | 7e-06 | 12/25 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.453×** | -5.3 | 2e-05 | 17/29 (H4, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.452×** | -5.2 | 3e-05 | 15/26 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.502×** | -4.6 | 4e-04 | 13/21 (NCI-H1792, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.521×** | -4.2 | 0.002 | 17/29 (COLO 205, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.533×** | -4.2 | 0.002 | 17/29 (HT-29, SW480, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.563×** | -3.8 | 0.008 | 13/28 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.572×** | -3.7 | 0.010 | 17/28 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.577×** | -3.4 | 0.035 | 9/29 (RKO, C-33 A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.610×** | -3.3 | 0.044 | 12/20 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.601×** | -3.2 | 0.056 | 12/23 (HT-29, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.629×** | -3.1 | 0.076 | 10/24 (HT-29, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11707. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 46.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0587× (z -16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0367× (z -13.4) |
| [[AN3 CA (line)]] | alt | 101 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 10.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0426× (z -9.0) |
| [[SW480 (line)]] | alt | 5.82 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0992× (z -9.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.116× (z -8.7) |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0639× (z -9.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HCT15 (line)]] | alt | 5.43 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0333× (z -8.9) |
| [[SHP-77 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.669 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.881 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.802 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.831 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.866 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11707), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF703]] | +0.64 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[PKHD1]] | +0.60 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[GLDN]] | +0.60 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[LINC02058]] | +0.57 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[BCAR3-AS1]] | +0.57 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[MIR4713HG]] | +0.56 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[TFF3]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[A1CF]] | +0.55 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[C9orf152]] | +0.53 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[LINC02253]] | +0.53 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[ST18]] | +0.53 | +0.60 / +0.31 | both halves | 2e-04 |  |
| [[CA9]] | +0.53 | +0.39 / +0.60 | both halves | 5e-05 | STRING 534 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TREX2]] | -0.45 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[CROCCP3-1]] | -0.45 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[ITGB1BP1]] | -0.45 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[DROSHA]] | -0.44 | -0.32 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDR72]] | B | WDR72 activity raises NDUFA4L2's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 2.30× lower at baseline in the lines without WDR72 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2 |
| [[MIR4713HG]] | B | MIR4713HG activity raises NDUFA4L2's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 2.01× lower at baseline in the lines without MIR4713HG | 0.009 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA |
| [[TFF3]] | B | TFF3 activity raises NDUFA4L2's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 2.72× lower at baseline in the lines without TFF3 | 0.015 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[AMBP]] | B | AMBP activity raises NDUFA4L2's level | lines that do not express AMBP (41) vs lines expressing it (9) | 3.39× lower at baseline in the lines without AMBP | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |
| [[GLDN]] | B | GLDN activity raises NDUFA4L2's level | lines that do not express GLDN (25) vs lines expressing it (25) | 1.85× lower at baseline in the lines without GLDN | 0.022 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595 |
| [[ASB4]] | B | ASB4 activity raises NDUFA4L2's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 2.44× lower at baseline in the lines without ASB4 | 0.052 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D |
| [[CA9]] | B | CA9 activity raises NDUFA4L2's level | lines that do not express CA9 (19) vs lines expressing it (31) | 2.21× lower at baseline in the lines without CA9 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[PROX1]] | B | PROX1 activity raises NDUFA4L2's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 1.96× lower at baseline in the lines without PROX1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964 |
| [[AXIN2]] | B | AXIN2 activity raises NDUFA4L2's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 3.05× lower at baseline in the lines without AXIN2 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[LINC02058]] | B | LINC02058 activity raises NDUFA4L2's level | lines that do not express LINC02058 (34) vs lines expressing it (16) | 2.26× lower at baseline in the lines without LINC02058 | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC02253, ENSG00000260573, ST18; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BTBD16]] | B | NDUFA4L2 activity raises BTBD16's level | lines that do not express NDUFA4L2 (16) vs lines expressing it (34) | 2.21× lower at baseline in the lines without NDUFA4L2 | 0.003 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CCDC162P]] | B | NDUFA4L2 activity raises CCDC162P's level | lines that do not express NDUFA4L2 (16) vs lines expressing it (34) | 1.94× lower at baseline in the lines without NDUFA4L2 | 0.063 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[KCNN1]] | B | NDUFA4L2 activity raises KCNN1's level | lines that do not express NDUFA4L2 (16) vs lines expressing it (34) | 1.60× lower at baseline in the lines without NDUFA4L2 | 0.076 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.9, 44.1); signed map (59.8, 16.6). **Vector** length 47.4, 8.53% of its response variance represented; |z| ≥ 3 in 719 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +0.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.9 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.1 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -6.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.6 | -2.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.6 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase hypoxia associated subunit FA4L2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,234,903-57,240,715 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NUOMS, FLJ26118, MISTRH; previously NDUFA4L2 |
| Gene groups (HGNC) | Mitochondrial complex IV: cytochrome c oxidase subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRX3](https://www.uniprot.org/uniprotkb/Q9NRX3) (Cytochrome c oxidase hypoxia associated subunit FA4L2):

> Mitochondrial protein that plays a regulatory role in cellular metabolism, particularly under hypoxic conditions. Down-regulates mitochondrial respiratory chain complex I activity under hypoxia, reduces oxygen consumption and ROS and helps cells adapt by switching to glycolysis.

**Summary**, from NCBI Gene [56901](https://www.ncbi.nlm.nih.gov/gene/56901):

> Enables enzyme inhibitor activity. Involved in cellular response to hypoxia and negative regulation of mitochondrial electron transport, NADH to ubiquinone. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29836](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29836) · Entrez [56901](https://www.ncbi.nlm.nih.gov/gene/56901) · UniProt [Q9NRX3](https://www.uniprot.org/uniprotkb/Q9NRX3) · Ensembl [ENSG00000185633](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185633)

## Data

Gene col 11707: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11707); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11707, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11707]; `tensor/DDL_lfc|DDL_z.npy` [11707]; `embed/gene_vectors.npy` [11707]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11707 or target_col == 11707). Every well: [[NDUFA4L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFA4L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
