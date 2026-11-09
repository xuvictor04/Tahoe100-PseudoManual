---
symbol: "DYNLRB2-AS1"
type: "gene"
col: 15241
ensembl_id: "ENSG00000259867"
name: "DYNLRB2 antisense RNA 1"
location: "16q23.2"
module: 191
arm: "+"
pooled_cpm: 3.46
n_lines_expressing: 45
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/191"]
generated_by: "tahoemap"
---

# DYNLRB2-AS1

*DYNLRB2 antisense RNA 1* — 16q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.23× (z +19.7, q 0e+00, up in 22 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.646× (z -4.2, q 0.013, down in 13 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (HepG2/C3A 0.149×, LOX-IMVI 0.0581×); [[Panobinostat (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0266×); [[Digitoxin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0438×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (HepG2/C3A 0.0670×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRM8]] (+0.77, fdr 7e-06), [[NEB]] (+0.74, fdr 7e-06), [[DNAH12]] (+0.74, fdr 7e-06).
> It is in [[Module 191]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LINC02694]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15241.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.23×** | +19.7 | 0e+00 | 22/25 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.13×** | +15.6 | 0e+00 | 18/26 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.56×** | +12.8 | 2e-35 | 21/38 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **3.71×** | +12.7 | 1e-34 | 25/31 (HOP62, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.43×** | +11.9 | 2e-30 | 7/17 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.53×** | +11.7 | 1e-29 | 2/4 (A498, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.29×** | +11.3 | 8e-28 | 23/35 (NCI-H460, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +9.7 | 2e-20 | 5/8 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.37×** | +8.3 | 5e-15 | 16/27 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.09×** | +7.1 | 6e-11 | 15/32 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +4.8 | 9e-05 | 17/40 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.6 | 2e-04 | 7/23 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +4.5 | 3e-04 | 7/30 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +4.3 | 8e-04 | 12/31 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.003 | 5/28 (A-172, A549, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.48×** | +3.8 | 0.006 | 10/34 (SW480, NCI-H1792, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.46×** | +3.4 | 0.020 | 6/31 (LoVo, RPMI-7951, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.029 | 11/26 (SW480, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15241.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (HepG2/C3A 0.149×, LOX-IMVI 0.0581×); [[Panobinostat (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0266×); [[Digitoxin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0438×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (HepG2/C3A 0.0670×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.646×** | -4.2 | 0.013 | 13/32 (LoVo, A498, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.725× | -3.1 | 0.51 | 7/37 (SHP-77, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15241. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 65.3 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0266× (z -17.7) |
| [[NCI-H460 (line)]] | wt | 3.72 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +9.5) | [[Menadione (drug)]] 0.05 µM 0.0685× (z -10.6) |
| [[A-172 (line)]] | wt | 3.81 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +12.3) | [[Erythromycin (drug)]] 0.05 µM 0.0634× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 4.11 | 0 | 2 | — | [[Bexarotene (drug)]] 0.05 µM 0.0491× (z -10.0) |
| [[C32 (line)]] | wt | 1.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.5× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 3.34 | 1 | 0 | [[Auranofin (drug)]] 5 µM 25.4× (z +11.1) | — |
| [[LoVo (line)]] | wt | 3.65 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0732× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 3.87 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0581× (z -9.2) |
| [[SW480 (line)]] | alt | 7.38 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.54× (z +8.8) | — |
| [[A-427 (line)]] | wt | 0.985 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.897 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.824 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.850 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.940 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.984 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15241), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRM8]] | +0.77 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[NEB]] | +0.74 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.74 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[HULC]] | +0.72 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[LINC01933]] | +0.71 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[LINC01340]] | +0.71 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[LINC03002]] | +0.71 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[ELAPOR1]] | +0.71 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[DPP6]] | +0.70 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[SYNPO2]] | +0.70 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.70 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[SYT16]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DYNLRB2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MALRD1]] | B | MALRD1 activity raises DYNLRB2-AS1's level | lines that do not express MALRD1 (14) vs lines expressing it (36) | 1.73× lower at baseline in the lines without MALRD1 | 0.033 | ⚠ within organs, on part of the lines; also absent: NELL1; maybe low, not absent |
| [[LINC01252]] | B | LINC01252 activity raises DYNLRB2-AS1's level | lines that do not express LINC01252 (17) vs lines expressing it (33) | 1.20× lower at baseline in the lines without LINC01252 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000275119, EPHB6, ABCC2; maybe low, not absent |
| [[LINC02147]] | B | LINC02147 activity raises DYNLRB2-AS1's level | lines that do not express LINC02147 (26) vs lines expressing it (24) | 1.62× lower at baseline in the lines without LINC02147 | 0.070 | ⚠ within organs, on part of the lines; also absent: LINC00992, PROX1-AS1, MOGAT3; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02694]] | B | DYNLRB2-AS1 activity raises LINC02694's level | lines that do not express DYNLRB2-AS1 (5) vs lines expressing it (45) | 1.46× lower at baseline in the lines without DYNLRB2-AS1 | 0.063 | ⚠ within organs, on part of the lines; also absent: ESRRB, LINC02932, ARHGAP15; maybe low, not absent |

## Where it sits

- **Module**: [[Module 191]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.643). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.1, 25.0); signed map (25.3, 12.2). **Vector** length 54.5, 8.33% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.5 | +12.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +11.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +12.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +1.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -1.5 | +0.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.4 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.1 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | +0.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | DYNLRB2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16q23.2 — chr16:80,154,979-80,563,354 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55405](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55405) · Entrez [102724084](https://www.ncbi.nlm.nih.gov/gene/102724084) · Ensembl [ENSG00000259867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259867)

## Data

Gene col 15241: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15241); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15241, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15241]; `tensor/DDL_lfc|DDL_z.npy` [15241]; `embed/gene_vectors.npy` [15241]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15241 or target_col == 15241). Every well: [[DYNLRB2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYNLRB2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
