---
symbol: "SATB1-AS1"
type: "gene"
col: 13684
ensembl_id: "ENSG00000228956"
name: "SATB1 antisense RNA 1"
location: "3p24.3"
module: 26
arm: "+"
pooled_cpm: 3.75
n_lines_expressing: 38
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# SATB1-AS1

*SATB1 antisense RNA 1* — 3p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.59× (z +19.3, q 0e+00, up in 21 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.0709×, RPMI-7951 0.112×; ⚠ cell-cycle shift, explains ~48% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (RPMI-7951 0.0788×, LS 180 0.163×; ⚠ cell-cycle shift, explains ~54% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RPMI-7951 0.0918×); [[Auranofin (drug)]] 5 µM in 1 line (RPMI-7951 0.101×); [[Altretamine (drug)]] 5 µM in 1 line (SK-MEL-2 0.0564×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRM8]] (+0.72, fdr 1e-05), [[GAS2]] (+0.71, fdr 1e-05), [[ITFG2-AS1]] (+0.71, fdr 2e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[SATB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13684.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.59×** | +19.3 | 0e+00 | 21/25 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.95×** | +15.4 | 0e+00 | 3/4 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.63×** | +11.5 | 2e-28 | 6/13 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.47×** | +10.3 | 1e-22 | 4/8 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.04×** | +6.4 | 2e-08 | 15/26 (HOP62, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.00×** | +6.2 | 4e-08 | 12/30 (BT-474, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +6.0 | 2e-07 | 5/25 (SHP-77, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +5.3 | 6e-06 | 9/23 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.9 | 5e-05 | 3/31 (SW480, LS 180, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.7 | 1e-04 | 3/12 (HT-29, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +4.6 | 2e-04 | 9/17 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.002 | 11/31 (NCI-H1792, SW1417, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +3.6 | 0.013 | 1/12 (NCI-H1792) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.3 | 0.042 | 5/22 (KATO III, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.2 | 0.049 | 1/15 (Hs 766T) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.076 | 4/26 (LS 180, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13684.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.0709×, RPMI-7951 0.112×; ⚠ cell-cycle shift, explains ~48% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (RPMI-7951 0.0788×, LS 180 0.163×; ⚠ cell-cycle shift, explains ~54% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RPMI-7951 0.0918×); [[Auranofin (drug)]] 5 µM in 1 line (RPMI-7951 0.101×); [[Altretamine (drug)]] 5 µM in 1 line (SK-MEL-2 0.0564×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.702× | -3.2 | 0.70 | 14/32 (RPMI-7951, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.712× | -3.0 | 0.70 | 8/28 (NCI-H1573, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13684. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 17.8 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0918× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0709× (z -11.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A-172 (line)]] | wt | 1.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.7× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 20.2 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -9.2) ⚠ cell-cycle shift, explains ~54% of this change |
| [[RKO (line)]] | wt | 12.9 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.102× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 5.21 | 0 | 1 | — | [[Altretamine (drug)]] 5 µM 0.0564× (z -9.0) |
| [[A-427 (line)]] | wt | 0.784 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.838 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.914 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.941 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.829 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.878 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.880 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13684), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRM8]] | +0.72 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[GAS2]] | +0.71 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ITFG2-AS1]] | +0.71 | +0.58 / +0.48 | both halves | 2e-05 | same gene group |
| [[GRM7]] | +0.71 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[CLVS1]] | +0.70 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[LINC01762]] | +0.70 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[UFL1-AS1]] | +0.70 | +0.57 / +0.43 | both halves | 3e-05 | same gene group |
| [[INTS6-AS1]] | +0.69 | +0.55 / +0.54 | both halves | 1e-05 | same gene group |
| [[AHI1-DT]] | +0.69 | +0.53 / +0.39 | both halves | 6e-05 |  |
| [[TMEM202-AS1]] | +0.69 | +0.57 / +0.50 | both halves | 1e-05 | same gene group |
| [[STEAP2-AS1]] | +0.68 | +0.63 / +0.52 | both halves | 1e-05 | same gene group |
| [[CCNO-DT]] | +0.68 | +0.57 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SATB1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00491]] | B | LINC00491 activity raises SATB1-AS1's level | lines that do not express LINC00491 (33) vs lines expressing it (17) | 1.60× lower at baseline in the lines without LINC00491 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APCDD1L, LINC01905, ADGRG7 |
| [[LINC01980]] | B | LINC01980 activity raises SATB1-AS1's level | lines that do not express LINC01980 (22) vs lines expressing it (28) | 1.72× lower at baseline in the lines without LINC01980 | 0.052 | ⚠ within organs, on part of the lines; also absent: KCNMB2, LINC00698, PAPPA2; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SATB1]] | B | SATB1-AS1 activity raises SATB1's level | lines that do not express SATB1-AS1 (12) vs lines expressing it (38) | 2.57× lower at baseline in the lines without SATB1-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: CMKLR2, ENSG00000289609; maybe low, not absent |
| [[MKLN1-AS]] | B | SATB1-AS1 activity lowers MKLN1-AS's level | lines that do not express SATB1-AS1 (12) vs lines expressing it (38) | 1.35× higher at baseline in the lines without SATB1-AS1 | 0.036 | ⚠ within organs, on part of the lines; also absent: CMKLR2, ENSG00000289609; maybe low, not absent |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (8.6, 18.4); signed map (29.6, -5.9). **Vector** length 45.3, 7.25% of its response variance represented; |z| ≥ 3 in 743 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +19.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +15.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +11.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +2.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -2.3 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -1.7 | -3.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -1.4 | -3.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.3 | -0.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -0.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.9 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | SATB1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p24.3 — chr3:18,445,024-18,923,280 (+) |
| Ensembl biotype | lncRNA |
| Also known as | uc.114, uc.113 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50687](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50687) · Entrez [101927777](https://www.ncbi.nlm.nih.gov/gene/101927777) · Ensembl [ENSG00000228956](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228956)

## Data

Gene col 13684: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13684); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13684, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13684]; `tensor/DDL_lfc|DDL_z.npy` [13684]; `embed/gene_vectors.npy` [13684]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13684 or target_col == 13684). Every well: [[SATB1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SATB1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
