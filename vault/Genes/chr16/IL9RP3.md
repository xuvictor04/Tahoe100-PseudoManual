---
symbol: "IL9RP3"
type: "gene"
col: 13561
ensembl_id: "ENSG00000226942"
name: "IL9R pseudogene 3"
location: "16p13.3"
module: 36
arm: "+"
pooled_cpm: 2.11
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# IL9RP3

*IL9R pseudogene 3* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.23× (z +13.7, q 7e-40, up in 42 of 43 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.40× (z +13.0, q 6e-36, up in 23 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.579× (z -4.0, q 0.037, down in 16 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Clonidine (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.414×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HT-29 0.0573×; ⚠ toxic; cell-cycle shift, explains ~69% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A498 0.0422×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (HT-29 0.0829×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXL18]] (+0.71, fdr 7e-06), [[HYAL1]] (+0.68, fdr 7e-06), [[ATP2A1]] (+0.66, fdr 7e-06); moves opposite to [[CFL2]] (-0.64, fdr 3e-04), [[NCOA4]] (-0.58, fdr 7e-04), [[VPS13C]] (-0.58, fdr 4e-04).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13561.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **6.23×** | +13.7 | 7e-40 | 42/43 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.40×** | +13.0 | 6e-36 | 23/24 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **4.34×** | +11.0 | 1e-25 | 34/41 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **4.23×** | +10.8 | 5e-25 | 34/38 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.70×** | +9.4 | 6e-19 | 0/2 | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **3.10×** | +8.1 | 4e-14 | 9/9 (SW480, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.86×** | +7.6 | 3e-12 | 12/21 (NCI-H460, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.02×** | +5.3 | 1e-05 | 8/22 (C-33 A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.04×** | +4.9 | 5e-05 | 0/3 | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.88×** | +4.7 | 2e-04 | 0/7 | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +4.3 | 8e-04 | 9/29 (HOP62, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.002 | 6/42 (HEC-1-A, PANC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.70×** | +3.9 | 0.004 | 11/43 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.69×** | +3.8 | 0.007 | 12/26 (SW480, LS 180, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.59×** | +3.5 | 0.021 | 4/44 (LoVo, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.55×** | +3.1 | 0.077 | 3/34 (A-427, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13561.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Clonidine (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.414×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HT-29 0.0573×; ⚠ toxic; cell-cycle shift, explains ~69% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A498 0.0422×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (HT-29 0.0829×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.579×** | -4.0 | 0.037 | 16/39 (SW48, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.603×** | -3.8 | 0.037 | 18/43 (HT-29, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.647× | -3.3 | 0.15 | 13/38 (RKO, C32, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.648× | -3.3 | 0.15 | 15/42 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.83 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13561. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 9.28 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0573× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~69% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0829× (z -9.4) |
| [[A498 (line)]] | wt | 2.18 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0422× (z -9.7) |
| [[J82 (line)]] | alt | 2.02 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0378× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 3.32 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0714× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 1.69 | 0 | 1 | — | [[Clonidine (hydrochloride) (drug)]] 5 µM 0.414× (z -17.9) |
| [[A-172 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.691 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.866 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.953 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.919 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.811 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.700 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.709 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.898 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.637 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.849 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13561), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL18]] | +0.71 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[HYAL1]] | +0.68 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[ATP2A1]] | +0.66 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[SLC27A5]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ZMYND19]] | +0.64 | +0.37 / +0.69 | both halves | 9e-05 |  |
| [[AXIN1]] | +0.64 | +0.31 / +0.61 | both halves | 2e-04 |  |
| [[ST6GALNAC6-1]] | +0.61 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[HIRA]] | +0.61 | +0.22 / +0.64 | both halves | 6e-04 |  |
| [[RSKR]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[RABGEF1P1]] | +0.61 | +0.23 / +0.72 | both halves | 5e-04 |  |
| [[ARPC5L]] | +0.60 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[PYCR3]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFL2]] | -0.64 | -0.28 / -0.67 | both halves | 3e-04 |  |
| [[NCOA4]] | -0.58 | -0.21 / -0.65 | both halves | 7e-04 |  |
| [[VPS13C]] | -0.58 | -0.26 / -0.59 | both halves | 4e-04 |  |
| [[TMEM106B]] | -0.58 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[SGCB]] | -0.56 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[HINT3]] | -0.56 | -0.38 / -0.62 | both halves | 6e-05 |  |
| [[CLCN3]] | -0.56 | -0.30 / -0.61 | both halves | 2e-04 |  |
| [[TAF9]] | -0.56 | -0.21 / -0.58 | both halves | 7e-04 |  |
| [[ARMT1]] | -0.54 | -0.20 / -0.54 | both halves | 7e-04 |  |
| [[MBTPS2]] | -0.54 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[EMD]] | -0.54 | -0.34 / -0.62 | both halves | 1e-04 |  |
| [[HACD2]] | -0.53 | -0.33 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IL9RP3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CUZD1]] | B | CUZD1 activity lowers IL9RP3's level | lines that do not express CUZD1 (9) vs lines expressing it (41) | 1.53× higher at baseline in the lines without CUZD1 | 0.098 | ⚠ within organs, on part of the lines; also absent: FAM24B, C10orf88B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.530). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (37.0, -21.0); signed map (-46.3, -1.7). **Vector** length 47.4, 6.29% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +13.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.6 | +13.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +1.9 | +11.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +1.9 | +10.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +1.7 | +8.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +3.5 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +0.9 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.9 | -0.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.9 | -4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.5 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | IL9R pseudogene 3 |
| Locus type | pseudogene |
| Location | 16p13.3 — chr16:29,336-38,321 (-) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:6033](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6033) · Entrez [729486](https://www.ncbi.nlm.nih.gov/gene/729486) · Ensembl [ENSG00000226942](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226942)

## Data

Gene col 13561: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13561); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13561, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13561]; `tensor/DDL_lfc|DDL_z.npy` [13561]; `embed/gene_vectors.npy` [13561]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13561 or target_col == 13561). Every well: [[IL9RP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL9RP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
