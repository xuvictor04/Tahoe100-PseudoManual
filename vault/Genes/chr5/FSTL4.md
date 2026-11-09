---
symbol: "FSTL4"
type: "gene"
col: 590
ensembl_id: "ENSG00000053108"
name: "follistatin like 4"
location: "5q31.1"
module: 140
arm: "+"
pooled_cpm: 7.28
n_lines_expressing: 28
n_dd_up: 41
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# FSTL4

*follistatin like 4* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.46× (z +28.7, q 0e+00, up in 18 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Binimetinib (drug)]] 5 µM in 1 line (NCI-H460 0.128×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (NCI-H460 0.109×); [[Trametinib (drug)]] 5 µM in 1 line (NCI-H460 0.136×; ⚠ cell-cycle shift, explains ~73% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBFOX1]] (+0.66, fdr 7e-06), [[AGBL1]] (+0.61, fdr 2e-05), [[TMEM132D]] (+0.61, fdr 7e-06); moves opposite to [[IMPA2]] (-0.46, fdr 2e-04), [[NTAQ1]] (-0.44, fdr 3e-04).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[EDARADD]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FGF9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 590.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **9.46×** | +28.7 | 0e+00 | 18/20 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.04×** | +23.0 | 0e+00 | 17/21 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **4.73×** | +19.8 | 0e+00 | 20/24 (SW480, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.96×** | +17.5 | 0e+00 | 19/19 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **6.07×** | +16.3 | 0e+00 | 17/24 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **5.09×** | +14.1 | 3e-43 | 17/21 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.03×** | +12.6 | 2e-34 | 15/23 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.91×** | +11.8 | 2e-30 | 1/4 (A498) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.31×** | +10.8 | 2e-25 | 13/23 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.25×** | +10.6 | 1e-24 | 2/10 (A498, HT-29) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.93×** | +9.7 | 2e-20 | 16/23 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.95×** | +8.5 | 7e-16 | 11/24 (NCI-H1573, A549, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.47×** | +8.2 | 2e-14 | 9/23 (HEC-1-A, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.37×** | +7.5 | 3e-12 | 9/19 (A549, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +6.6 | 1e-09 | 10/23 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.03×** | +6.4 | 6e-09 | 13/23 (NCI-H1573, SW48, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +6.1 | 4e-08 | 14/22 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +4.8 | 4e-05 | 7/24 (NCI-H1573, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.76×** | +4.8 | 4e-05 | 6/23 (SW480, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Binimetinib (drug)]] 5 µM in 1 line (NCI-H460 0.128×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (NCI-H460 0.109×); [[Trametinib (drug)]] 5 µM in 1 line (NCI-H460 0.136×; ⚠ cell-cycle shift, explains ~73% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 590. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 5.70 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.5× (z +16.1) | — |
| [[SW480 (line)]] | alt | 14.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +14.2) | — |
| [[A-172 (line)]] | wt | 2.35 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 94.3× (z +14.8) | — |
| [[LoVo (line)]] | wt | 2.12 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.5× (z +13.9) | — |
| [[NCI-H460 (line)]] | wt | 76.9 | 0 | 3 (1 ⚠) | — | [[Binimetinib (drug)]] 5 µM 0.128× (z -9.0) |
| [[A-427 (line)]] | wt | 2.61 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 15.5× (z +9.7) | — |
| [[A549 (line)]] | wt | 5.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.0× (z +11.4) | — |
| [[BT-474 (line)]] | alt | 40.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 2.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 253× (z +15.7) | — |
| [[HEC-1-A (line)]] | alt | 1.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 6.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.15× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 2.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 4.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 2.10 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 14.5× (z +8.5) | — |
| [[A498 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.929 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.000 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 590), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBFOX1]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 | same gene group |
| [[AGBL1]] | +0.61 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[TMEM132D]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[LINC00922]] | +0.58 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[LINC02755]] | +0.57 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[GABBR2]] | +0.56 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[AMDHD1]] | +0.55 | +0.41 / +0.67 | both halves | 4e-05 |  |
| [[XKR4]] | +0.55 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[DNAH3]] | +0.54 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ARL14]] | +0.54 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[COL28A1]] | +0.54 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CHGB]] | +0.53 | +0.59 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMPA2]] | -0.46 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[NTAQ1]] | -0.44 | -0.51 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDARADD]] | B | EDARADD activity raises FSTL4's level | lines that do not express EDARADD (26) vs lines expressing it (24) | 2.17× lower at baseline in the lines without EDARADD | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000239268, NOL4, ASXL3 |
| [[TOP2A]] | B | TOP2A activity lowers FSTL4's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 8.4% of all compounds | 0.015 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CTNND2]] | B | CTNND2 activity raises FSTL4's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.51× lower at baseline in the lines without CTNND2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent |
| [[NLGN4Y]] | B | NLGN4Y activity raises FSTL4's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 1.60× lower at baseline in the lines without NLGN4Y | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9 |
| [[LAMB4]] | C | LAMB4 activity raises FSTL4's level | lines that do not express LAMB4 (26) vs lines expressing it (24) | 1.90× lower at baseline in the lines without LAMB4 | 0.072 | ⚠ within organs, on part of the lines; also absent: NRCAM, MEIOB, SOX2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGF9]] | C | FSTL4 activity raises FGF9's level | lines that do not express FSTL4 (22) vs lines expressing it (28) | 2.65× lower at baseline in the lines without FSTL4 | 0.074 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, CDHR2, IGFL4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.484). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.3, 25.2); signed map (28.1, 15.0). **Vector** length 54.8, 11.6% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.7 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +5.7 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +19.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +4.8 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +28.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +8.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +2.8 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -0.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -1.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | follistatin like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:133,196,455-133,612,541 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1061 |
| Gene groups (HGNC) | I-set domain containing; EF-hand domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q6MZW2](https://www.uniprot.org/uniprotkb/Q6MZW2) carries no function annotation.

**Summary**, from NCBI Gene [23105](https://www.ncbi.nlm.nih.gov/gene/23105):

> Predicted to enable brain-derived neurotrophic factor binding activity and calcium ion binding activity. Predicted to be involved in cell differentiation and regulation of BMP signaling pathway. Predicted to act upstream of or within negative regulation of brain-derived neurotrophic factor receptor signaling pathway; negative regulation of collateral sprouting; and negative regulation of dendritic spine development. Predicted to be located in secretory granule. Predicted to be active in …

**Accessions** — [HGNC:21389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21389) · Entrez [23105](https://www.ncbi.nlm.nih.gov/gene/23105) · UniProt [Q6MZW2](https://www.uniprot.org/uniprotkb/Q6MZW2) · Ensembl [ENSG00000053108](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000053108)

## Data

Gene col 590: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 590); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 590, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 590]; `tensor/DDL_lfc|DDL_z.npy` [590]; `embed/gene_vectors.npy` [590]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 590 or target_col == 590). Every well: [[FSTL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FSTL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
