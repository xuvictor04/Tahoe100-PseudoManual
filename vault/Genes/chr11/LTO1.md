---
symbol: "LTO1"
type: "gene"
col: 7404
ensembl_id: "ENSG00000149716"
name: "LTO1 maturation factor of ABCE1"
location: "11q13.2"
module: 83
arm: "+"
pooled_cpm: 19.24
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# LTO1

*LTO1 maturation factor of ABCE1* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.09× (z +18.1, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.754× (z -4.9, q 5e-04, down in 18 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (SW480 0.109×; ⚠ toxic); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (NCI-H1792 0.203×); [[AZD2858 (drug)]] 0.5 µM in 1 line (CFPAC-1 0.112×; ⚠ toxic); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.150×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF621]] (+0.76, fdr 7e-06), [[PPP1R3F]] (+0.68, fdr 1e-05), [[AFG3L1P]] (+0.67, fdr 1e-05); moves opposite to [[NUP62CL]] (-0.67, fdr 1e-05), [[SPATA6]] (-0.66, fdr 3e-05), [[EFNA4]] (-0.66, fdr 3e-05).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7404.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +18.1 | 0e+00 | 43/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.21×** | +13.8 | 6e-41 | 40/47 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +12.2 | 8e-32 | 33/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +10.2 | 4e-22 | 32/46 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +8.0 | 1e-13 | 22/33 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +8.0 | 1e-13 | 28/41 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +7.9 | 3e-13 | 35/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +7.5 | 3e-12 | 30/47 (SW480, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +7.1 | 6e-11 | 28/46 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +6.8 | 5e-10 | 29/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +6.8 | 6e-10 | 23/41 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +6.5 | 4e-09 | 26/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +5.9 | 2e-07 | 21/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.9 | 2e-07 | 23/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +5.7 | 4e-07 | 19/37 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.2 | 7e-06 | 23/48 (A-172, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.2 | 8e-04 | 12/48 (NCI-H23, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +4.2 | 8e-04 | 15/46 (SK-MEL-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.015 | 13/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7404.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (SW480 0.109×; ⚠ toxic); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (NCI-H1792 0.203×); [[AZD2858 (drug)]] 0.5 µM in 1 line (CFPAC-1 0.112×; ⚠ toxic); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.150×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.754×** | -4.9 | 5e-04 | 18/48 (SW480, LoVo, …) | inconsistent across doses | composition shift |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.837× | -3.1 | 0.46 | 8/48 (CHP-212, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | 0.817× | -3.0 | 0.46 | 11/47 (SW48, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7404. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 34.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.75× (z +9.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.04× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -8.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 24.0 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +11.6) | [[Lonafarnib (drug)]] 5 µM 0.109× (z -12.3) ⚠ toxic |
| [[HOP62 (line)]] | alt | 24.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 11.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +9.6) | [[Palmatine (chloride) (drug)]] 0.5 µM 0.203× (z -9.1) |
| [[A-172 (line)]] | wt | 22.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +8.8) | — |
| [[A498 (line)]] | wt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.6) | — |
| [[A549 (line)]] | wt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 23.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.112× (z -9.0) ⚠ toxic |
| [[HS-578T (line)]] | alt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +9.7) | — |
| [[NCI-H460 (line)]] | wt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 20.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 23.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +17.2) | — |
| [[SK-MEL-2 (line)]] | alt | 53.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.53× (z +10.1) | — |
| [[SNU-1 (line)]] | wt | 23.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -9.0) |
| [[A-427 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7404), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF621]] | +0.76 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[PPP1R3F]] | +0.68 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[AFG3L1P]] | +0.67 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[RAB30-DT]] | +0.67 | +0.76 / +0.38 | both halves | 7e-05 |  |
| [[RGS20]] | +0.66 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[MAEA]] | +0.66 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[CSTF3]] | +0.65 | +0.69 / +0.40 | both halves | 5e-05 |  |
| [[SMIM15-AS1]] | +0.64 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[ARRDC3-AS1]] | +0.64 | +0.74 / +0.30 | both halves | 2e-04 |  |
| [[RNASEH1]] | +0.64 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[ITPA]] | +0.64 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[FBXO30]] | +0.64 | +0.58 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP62CL]] | -0.67 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[SPATA6]] | -0.66 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[EFNA4]] | -0.66 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[TTLL5]] | -0.65 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[RADX]] | -0.64 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[ZDHHC12]] | -0.64 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ACACB]] | -0.63 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[PGAP1]] | -0.63 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[SUFU]] | -0.63 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[ORC4]] | -0.62 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ALAD]] | -0.60 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[CHEK2]] | -0.60 | -0.51 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LTO1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.739). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.9, 7.5); signed map (19.7, -26.2). **Vector** length 77.1, 14.1% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +13.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.7 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +18.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +7.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +2.1 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | +1.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -0.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.6 | +7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.4 | +5.9 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +2.4 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.6 | -1.9 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | LTO1 maturation factor of ABCE1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:69,653,076-69,675,416 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAOS1, CIAB1; previously ORAOV1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WV07](https://www.uniprot.org/uniprotkb/Q8WV07) (Protein LTO1 homolog):

> The complex LTO1:YAE1 functions as a target specific adapter that probably recruits apo-ABCE1 to the cytosolic iron-sulfur protein assembly (CIA) complex machinery. May be required for biogenesis of the large ribosomal subunit and initiation of translation. May play a role in the regulation of proline metabolism and ROS production.

**Summary**, from NCBI Gene [220064](https://www.ncbi.nlm.nih.gov/gene/220064):

> Involved in protein maturation; ribosomal large subunit biogenesis; and translational initiation. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17589](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17589) · Entrez [220064](https://www.ncbi.nlm.nih.gov/gene/220064) · UniProt [Q8WV07](https://www.uniprot.org/uniprotkb/Q8WV07) · Ensembl [ENSG00000149716](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149716)

## Data

Gene col 7404: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7404); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7404, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7404]; `tensor/DDL_lfc|DDL_z.npy` [7404]; `embed/gene_vectors.npy` [7404]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7404 or target_col == 7404). Every well: [[LTO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LTO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
