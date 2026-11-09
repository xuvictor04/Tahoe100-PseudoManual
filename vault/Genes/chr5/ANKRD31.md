---
symbol: "ANKRD31"
type: "gene"
col: 7013
ensembl_id: "ENSG00000145700"
name: "ankyrin repeat domain 31"
location: "5q13.3"
module: 10
arm: "+"
pooled_cpm: 3.09
n_lines_expressing: 47
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ANKRD31

*ankyrin repeat domain 31* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.24× (z +17.8, q 0e+00, up in 28 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.554× (z -5.0, q 3e-04, down in 20 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (A-427 0.0348×, NCI-H23 0.132×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H23 0.0690×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H23 0.0790×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCNX4-DT]] (+0.78, fdr 7e-06), [[FRG1-DT]] (+0.76, fdr 7e-06), [[LINC00240]] (+0.76, fdr 7e-06).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7013.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.24×** | +17.8 | 0e+00 | 28/29 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.06×** | +13.8 | 1e-40 | 22/28 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.34×** | +12.8 | 5e-35 | 26/27 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.11×** | +11.8 | 5e-30 | 3/4 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.97×** | +9.5 | 3e-19 | 5/10 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.59×** | +8.3 | 1e-14 | 20/35 (C32, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +7.8 | 4e-13 | 2/6 (HEC-1-A, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.78×** | +7.1 | 9e-11 | 17/42 (A-427, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.27×** | +6.9 | 4e-10 | 17/38 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.09×** | +6.4 | 9e-09 | 24/41 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +5.6 | 9e-07 | 11/22 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.89×** | +5.5 | 1e-06 | 16/40 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.88×** | +5.5 | 2e-06 | 21/40 (A-427, LS 180, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.8 | 5e-05 | 12/41 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +3.7 | 0.008 | 2/14 (MIA PaCa-2, RKO) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.008 | 8/41 (SW480, BT-474, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.011 | 8/33 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.021 | 3/40 (LoVo, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.027 | 5/23 (NCI-H1573, SW 900, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7013.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (A-427 0.0348×, NCI-H23 0.132×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H23 0.0690×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H23 0.0790×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.554×** | -5.0 | 3e-04 | 20/40 (NCI-H23, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.572×** | -4.3 | 0.004 | 10/42 (NCI-H23, A-427, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.656× | -3.5 | 0.10 | 9/34 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.688× | -3.2 | 0.19 | 17/36 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Asciminib (drug)]] 0.05 µM |  | 0.669× | -3.1 | 0.19 | 10/39 (SW 900, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.702× | -3.1 | 0.19 | 14/37 (HEC-1-A, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.704× | -3.0 | 0.19 | 11/43 (HT-29, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7013. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0690× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0790× (z -11.3) |
| [[A-427 (line)]] | wt | 7.26 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0348× (z -13.5) |
| [[C32 (line)]] | wt | 2.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 3.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.68× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 1.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +9.8) | — |
| [[SW480 (line)]] | alt | 1.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +8.8) | — |
| [[A-172 (line)]] | wt | 0.701 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.840 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.712 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.779 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.869 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.953 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.668 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.824 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7013), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX4-DT]] | +0.78 | +0.83 / +0.62 | both halves | 7e-06 |  |
| [[FRG1-DT]] | +0.76 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[LINC00240]] | +0.76 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[GUCY2C-AS1]] | +0.75 | +0.81 / +0.47 | both halves | 2e-05 |  |
| [[TMEM202-AS1]] | +0.75 | +0.83 / +0.48 | both halves | 2e-05 |  |
| [[LEKR1]] | +0.75 | +0.81 / +0.53 | both halves | 1e-05 |  |
| [[NEB]] | +0.75 | +0.82 / +0.57 | both halves | 9e-06 |  |
| [[ZNF747]] | +0.75 | +0.78 / +0.45 | both halves | 3e-05 |  |
| [[PATL2]] | +0.74 | +0.83 / +0.47 | both halves | 2e-05 |  |
| [[ACAD9-DT]] | +0.74 | +0.81 / +0.54 | both halves | 1e-05 |  |
| [[RP1]] | +0.73 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PDCL3P4]] | +0.73 | +0.81 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANKRD31's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00886]] | B | LINC00886 activity raises ANKRD31's level | lines that do not express LINC00886 (16) vs lines expressing it (34) | 1.53× lower at baseline in the lines without LINC00886 | 0.042 | ⚠ within organs, on part of the lines; also absent: RASEF; maybe low, not absent |
| [[LINC01088]] | B | LINC01088 activity raises ANKRD31's level | lines that do not express LINC01088 (9) vs lines expressing it (41) | 1.65× lower at baseline in the lines without LINC01088 | 0.071 | ⚠ within organs, on part of the lines; also absent: PPP4R4, GPR155, PKIG; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.843). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.3, 15.8); signed map (33.3, -9.8). **Vector** length 61.1, 10.1% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +17.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +1.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +2.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | +0.7 |
|  | [[Piroxicam (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:75,068,275-75,236,911 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40191 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N7Z5](https://www.uniprot.org/uniprotkb/Q8N7Z5) (Ankyrin repeat domain-containing protein 31):

> Required for DNA double-strand breaks (DSBs) formation during meiotic recombination. Regulates the spatial and temporal patterns of pre-DSB recombinosome assembly and recombination activity by acting as a scaffold that anchors REC114 and other factors to specific genomic locations, thereby regulating DSB formation. Plays a key role in recombination in the pseudoautosomal regions of sex chromosomes.

**Summary**, from NCBI Gene [256006](https://www.ncbi.nlm.nih.gov/gene/256006):

> This gene encodes a protein containing multiple ankyrin repeats. Ankyrin domains function in protein-protein interactions in a variety of cellular processes. Mutations in this gene are associated with a Rett syndrome (RTT)-like phenotype. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:26853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26853) · Entrez [256006](https://www.ncbi.nlm.nih.gov/gene/256006) · UniProt [Q8N7Z5](https://www.uniprot.org/uniprotkb/Q8N7Z5) · Ensembl [ENSG00000145700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145700)

## Data

Gene col 7013: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7013); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7013, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7013]; `tensor/DDL_lfc|DDL_z.npy` [7013]; `embed/gene_vectors.npy` [7013]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7013 or target_col == 7013). Every well: [[ANKRD31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
