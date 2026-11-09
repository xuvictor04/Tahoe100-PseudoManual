---
symbol: "C2orf88"
type: "gene"
col: 11937
ensembl_id: "ENSG00000187699"
name: "A-kinase anchoring protein 19"
location: "2q32.2"
module: 26
arm: "+"
pooled_cpm: 6.71
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# C2orf88

*A-kinase anchoring protein 19* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.18× (z +25.7, q 0e+00, up in 42 of 42 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0759×); [[Belinostat (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0693×; ⚠ cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (A549 0.0846×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.0849×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02955]] (+0.81, fdr 7e-06), [[PSMD7-DT]] (+0.80, fdr 7e-06), [[LINC00393]] (+0.80, fdr 7e-06); moves opposite to [[GPATCH11]] (-0.67, fdr 3e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11937.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.18×** | +25.7 | 0e+00 | 42/42 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.14×** | +14.5 | 3e-45 | 29/30 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +13.1 | 1e-36 | 9/12 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.69×** | +11.6 | 7e-29 | 14/17 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +10.9 | 1e-25 | 27/42 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.22×** | +10.1 | 4e-22 | 32/45 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +9.0 | 2e-17 | 31/40 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.00×** | +8.8 | 1e-16 | 29/46 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.6 | 1e-12 | 27/48 (HOP62, A549, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +5.8 | 3e-07 | 15/47 (NCI-H460, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +4.8 | 1e-04 | 16/40 (HCT15, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +4.4 | 4e-04 | 11/45 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +4.4 | 5e-04 | 11/47 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.39×** | +4.2 | 0.001 | 6/47 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.003 | 12/40 (NCI-H1792, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.018 | 9/45 (A-172, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.049 | 7/44 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.055 | 8/47 (A498, NCI-H460, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.055 | 3/47 (A498, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0759×); [[Belinostat (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0693×; ⚠ cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (A549 0.0846×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.0849×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11937. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 5.41 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +10.9) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0846× (z -10.6) |
| [[LoVo (line)]] | wt | 21.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 6.73 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +9.7) | [[Cobimetinib (drug)]] 0.05 µM 0.0849× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 6.24 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.35× (z +10.9) | [[Belinostat (drug)]] 0.5 µM 0.0693× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 4.97 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +10.0) | — |
| [[SW480 (line)]] | alt | 4.53 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.50× (z +11.5) | — |
| [[A-172 (line)]] | wt | 4.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.57× (z +10.5) | — |
| [[A498 (line)]] | wt | 7.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 7.50 | 0 | 1 | — | [[Ranolazine (drug)]] 0.05 µM 0.0731× (z -9.0) |
| [[HOP62 (line)]] | alt | 4.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 3.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 5.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 4.42 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0759× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 5.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +14.4) | — |
| [[Panc 03.27 (line)]] | alt | 3.77 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0704× (z -8.7) |
| [[RKO (line)]] | wt | 9.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.41× (z +10.8) | — |
| [[SW 900 (line)]] | alt | 5.99 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0699× (z -9.3) |
| [[A-427 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11937), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02955]] | +0.81 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.80 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[LINC00393]] | +0.80 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[PXDNL]] | +0.78 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[CPEB2-DT]] | +0.78 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[LINC01762]] | +0.77 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[MYLK4]] | +0.77 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[SIAH2-AS1]] | +0.77 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[FAM184B]] | +0.76 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[MCF2]] | +0.75 | +0.72 / +0.46 | both halves | 2e-05 |  |
| [[NEB]] | +0.74 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[LINC00880]] | +0.74 | +0.61 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH11]] | -0.67 | -0.27 / -0.38 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers C2orf88's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ARSD]] | C | ARSD activity lowers C2orf88's level | lines that do not express ARSD (4) vs lines expressing it (46) | 1.52× higher at baseline in the lines without ARSD | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MYH16, SGK2, SAT1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.810). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.9, 18.8); signed map (25.0, -1.3). **Vector** length 59.2, 8.03% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +25.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +14.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +3.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.2 | +3.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -1.8 | +4.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | +0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | A-kinase anchoring protein 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2 — chr2:189,879,609-190,203,484 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13057, smAKAP; previously C2orf88 |
| Gene groups (HGNC) | A-kinase anchoring proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSF0](https://www.uniprot.org/uniprotkb/Q9BSF0) (A-kinase anchoring protein 19):

> Binds to type I regulatory subunits of protein kinase A (PKA-RI) and anchors/targets them to the plasma membrane.

**Summary**, from NCBI Gene [84281](https://www.ncbi.nlm.nih.gov/gene/84281):

> Predicted to enable protein kinase A regulatory subunit binding activity. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28191](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28191) · Entrez [84281](https://www.ncbi.nlm.nih.gov/gene/84281) · UniProt [Q9BSF0](https://www.uniprot.org/uniprotkb/Q9BSF0) · Ensembl [ENSG00000187699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187699)

## Data

Gene col 11937: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11937); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11937, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11937]; `tensor/DDL_lfc|DDL_z.npy` [11937]; `embed/gene_vectors.npy` [11937]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11937 or target_col == 11937). Every well: [[C2orf88 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2orf88.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
