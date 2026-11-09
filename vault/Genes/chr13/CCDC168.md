---
symbol: "CCDC168"
type: "gene"
col: 10653
ensembl_id: "ENSG00000175820"
name: "leucine rich repeat transmembrane protein 3"
location: "13q33.1"
module: 38
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# CCDC168

*leucine rich repeat transmembrane protein 3* — 13q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.29× (z +24.2, q 0e+00, up in 28 of 28 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Neratinib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.143×); [[Ponatinib (drug)]] 5 µM in 1 line (COLO 205 0.0384×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 0.0658×; ⚠ cell-cycle shift, explains ~11% of this change); [[Elagolix sodium (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0779×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DRC1]] (+0.70, fdr 7e-06), [[WDR49]] (+0.68, fdr 1e-05), [[VWCE]] (+0.66, fdr 1e-05); moves opposite to [[IFTAP]] (-0.63, fdr 2e-05), [[NUDT12]] (-0.62, fdr 1e-05), [[SLX4IP]] (-0.62, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10653.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.29×** | +24.2 | 0e+00 | 28/28 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **6.70×** | +15.8 | 0e+00 | 18/22 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.50×** | +12.5 | 2e-33 | 25/30 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **4.17×** | +11.8 | 4e-30 | 12/13 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **3.10×** | +9.7 | 3e-20 | 35/45 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.02×** | +8.5 | 1e-15 | 15/44 (SW480, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.59×** | +7.9 | 3e-13 | 0/2 | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.49×** | +7.9 | 3e-13 | 24/41 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.43×** | +7.6 | 1e-12 | 24/42 (SW480, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.25×** | +7.0 | 2e-10 | 21/45 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.14×** | +6.5 | 3e-09 | 12/35 (SW480, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.03×** | +6.1 | 5e-08 | 1/10 (PANC-1) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.04×** | +5.7 | 6e-07 | 1/5 (HEC-1-A) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +4.3 | 7e-04 | 10/43 (J82, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.57×** | +3.8 | 0.005 | 9/40 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +3.4 | 0.022 | 9/44 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.13×** | +3.4 | 0.022 | 3/16 (SW480, HEC-1-A, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.075 | 6/43 (HEC-1-A, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.075 | 6/45 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10653.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Neratinib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.143×); [[Ponatinib (drug)]] 5 µM in 1 line (COLO 205 0.0384×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 0.0658×; ⚠ cell-cycle shift, explains ~11% of this change); [[Elagolix sodium (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0779×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | 0.670× | -3.5 | 0.11 | 6/44 (C32, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.663× | -3.4 | 0.11 | 11/36 (NCI-H1792, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | 0.693× | -3.4 | 0.11 | 10/45 (CHP-212, SW48, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.682× | -3.4 | 0.11 | 8/20 (PANC-1, A498, …) | two highest doses | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.491× | -3.2 | 0.12 | 9/19 (HEC-1-A, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.692× | -3.2 | 0.12 | 10/43 (COLO 205, CHP-212, …) | top dose only |  |
| [[Brimonidine (drug)]] 0.5 µM |  | 0.704× | -3.1 | 0.15 | 12/31 (NCI-H460, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 0.782× | -3.1 | 0.15 | 9/42 (NCI-H1792, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.68 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10653. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 7.13 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.70× (z +10.6) | [[Neratinib (drug)]] 0.05 µM 0.143× (z -9.5) |
| [[SW480 (line)]] | alt | 4.88 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 1.54 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +11.1) | — |
| [[A-172 (line)]] | wt | 6.07 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0658× (z -8.6) ⚠ cell-cycle shift, explains ~11% of this change |
| [[A498 (line)]] | wt | 3.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.37× (z +11.0) | — |
| [[COLO 205 (line)]] | alt | 4.89 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.0384× (z -8.9) |
| [[HOP62 (line)]] | alt | 2.51 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 26.8× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 2.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 28.3× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 5.22 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0779× (z -8.5) |
| [[PANC-1 (line)]] | alt | 1.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +10.3) | — |
| [[A-427 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.640 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.896 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.982 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.742 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.693 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.912 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10653), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRC1]] | +0.70 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[WDR49]] | +0.68 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[VWCE]] | +0.66 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[EOGT]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[UBE2F-SCLY]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[PHYHD1]] | +0.64 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[GABRR2]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ADORA1]] | +0.63 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[LINC00672]] | +0.63 | +0.41 / +0.73 | both halves | 4e-05 |  |
| [[ADCY10P1]] | +0.63 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[TICAM2]] | +0.63 | +0.59 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFTAP]] | -0.63 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[NUDT12]] | -0.62 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[SLX4IP]] | -0.62 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[WDR7]] | -0.61 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[TBC1D19]] | -0.60 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[NEPRO]] | -0.59 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[SLC25A12]] | -0.59 | -0.65 / -0.37 | both halves | 9e-05 |  |
| [[ZNF45]] | -0.58 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[SCRN3]] | -0.56 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[CEP162]] | -0.56 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[GOPC]] | -0.55 | -0.39 / -0.61 | both halves | 6e-05 |  |
| [[BBS5]] | -0.55 | -0.51 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC168's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.632). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.0, -17.5); signed map (13.2, 8.8). **Vector** length 55.1, 7.12% of its response variance represented; |z| ≥ 3 in 1,262 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +24.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +15.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +12.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +11.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +6.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +8.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +0.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.0 | -3.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat transmembrane protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q33.1 — chr13:102,729,367-102,759,072 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40176; previously C13orf40, CCDC168 |
| Matched by | ensembl_id |

UniProt [Q8NDH2](https://www.uniprot.org/uniprotkb/Q8NDH2) carries no function annotation.

**Summary**, from NCBI Gene [643677](https://www.ncbi.nlm.nih.gov/gene/643677):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26851) · Entrez [643677](https://www.ncbi.nlm.nih.gov/gene/643677) · UniProt [Q8NDH2](https://www.uniprot.org/uniprotkb/Q8NDH2) · Ensembl [ENSG00000175820](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175820)

## Data

Gene col 10653: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10653); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10653, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10653]; `tensor/DDL_lfc|DDL_z.npy` [10653]; `embed/gene_vectors.npy` [10653]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10653 or target_col == 10653). Every well: [[CCDC168 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC168.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
