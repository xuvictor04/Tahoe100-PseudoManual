---
symbol: "GUCY2C-AS1"
type: "gene"
col: 13221
ensembl_id: "ENSG00000214772"
name: "GUCY2C antisense RNA 1"
location: "12p12.3"
module: 10
arm: "+"
pooled_cpm: 3.12
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# GUCY2C-AS1

*GUCY2C antisense RNA 1* — 12p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.46× (z +18.9, q 0e+00, up in 28 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0492×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (LoVo 0.0796×; ⚠ cell-cycle shift, explains ~51% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.128×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM202-AS1]] (+0.82, fdr 1e-05), [[NEB]] (+0.81, fdr 7e-06), [[PCNX4-DT]] (+0.80, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13221.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.46×** | +18.9 | 0e+00 | 28/31 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.51×** | +16.7 | 0e+00 | 27/29 (Panc 03.27, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.31×** | +9.4 | 8e-19 | 21/29 (LoVo, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.15×** | +9.0 | 3e-17 | 6/12 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.16×** | +8.6 | 1e-15 | 12/45 (Panc 03.27, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.00×** | +8.3 | 9e-15 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.70×** | +7.5 | 5e-12 | 14/22 (Panc 03.27, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +6.5 | 7e-09 | 16/29 (Panc 03.27, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +5.5 | 2e-06 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +4.7 | 2e-04 | 11/42 (LoVo, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +4.3 | 0.001 | 16/45 (KATO III, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +4.0 | 0.002 | 9/36 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +4.0 | 0.003 | 14/38 (LoVo, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.63×** | +3.9 | 0.005 | 8/39 (LoVo, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.61×** | +3.8 | 0.006 | 8/36 (LoVo, LS 180, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +3.6 | 0.012 | 3/42 (A549, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.063 | 7/29 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +3.0 | 0.070 | 12/45 (LoVo, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13221.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0492×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (LoVo 0.0796×; ⚠ cell-cycle shift, explains ~51% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.128×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.660× | -3.3 | 0.33 | 7/45 (HCT15, NCI-H23, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.883× | -3.2 | 0.33 | 10/46 (RKO, C32, …) | inconsistent across doses |  |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.672× | -3.1 | 0.34 | 7/43 (RKO, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13221. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 10.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +13.9) | [[Belinostat (drug)]] 0.5 µM 0.0492× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 9.77 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.180× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[C32 (line)]] | wt | 1.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +9.1) | — |
| [[J82 (line)]] | alt | 2.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 1.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +11.3) | — |
| [[NCI-H460 (line)]] | wt | 0.907 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 2.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.35× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.128× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.886 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.846 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.904 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.915 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13221), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM202-AS1]] | +0.82 | +0.84 / +0.56 | both halves | 1e-05 | same gene group |
| [[NEB]] | +0.81 | +0.82 / +0.60 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | +0.80 | +0.83 / +0.51 | both halves | 1e-05 |  |
| [[DNAH12]] | +0.80 | +0.85 / +0.60 | both halves | 7e-06 |  |
| [[PATL2]] | +0.80 | +0.85 / +0.48 | both halves | 2e-05 |  |
| [[LINC00240]] | +0.78 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[PLBD1-AS1]] | +0.78 | +0.81 / +0.51 | both halves | 1e-05 | same gene group; ⚠ same locus (41.5 kb, same strand: neighbours can correlate without regulation) |
| [[OXA1L-DT]] | +0.77 | +0.80 / +0.47 | both halves | 2e-05 |  |
| [[AK9]] | +0.77 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[RBM26-AS1]] | +0.77 | +0.81 / +0.45 | both halves | 3e-05 | same gene group |
| [[INTS6-AS1]] | +0.76 | +0.81 / +0.59 | both halves | 7e-06 | same gene group |
| [[UNC79]] | +0.76 | +0.77 / +0.57 | both halves | 1e-05 |  |
| [[LINC02951]] | +0.76 | +0.69 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GUCY2C-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[STEAP2-AS1]] | B | STEAP2-AS1 activity lowers GUCY2C-AS1's level | lines that do not express STEAP2-AS1 (12) vs lines expressing it (38) | 1.40× higher at baseline in the lines without STEAP2-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: STEAP2, STEAP1, FCGRT; maybe low, not absent |
| [[CPEB2]] | C | CPEB2 activity lowers GUCY2C-AS1's level | lines that do not express CPEB2 (3) vs lines expressing it (47) | 2.89× higher at baseline in the lines without CPEB2 | 0.020 | ⚠ few lines (3 vs 47); across organs; also absent: SFXN3, CDKN1A, LRIG3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.784). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (10.1, 16.3); signed map (29.8, -4.7). **Vector** length 56.0, 7.58% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +18.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +16.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +3.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.3 | +1.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -2.7 | -1.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.6 | -0.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -1.8 |
|  | [[Posaconazole (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.6 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -0.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | GUCY2C antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12p12.3 — chr12:14,665,655-14,757,963 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56054](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56054) · Entrez [123706531](https://www.ncbi.nlm.nih.gov/gene/123706531) · Ensembl [ENSG00000214772](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214772)

## Data

Gene col 13221: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13221); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13221, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13221]; `tensor/DDL_lfc|DDL_z.npy` [13221]; `embed/gene_vectors.npy` [13221]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13221 or target_col == 13221). Every well: [[GUCY2C-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GUCY2C-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
