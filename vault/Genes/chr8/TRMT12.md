---
symbol: "TRMT12"
type: "gene"
col: 11431
ensembl_id: "ENSG00000183665"
name: "tRNA wybutosine-synthesizing protein 2"
location: "8q24.13"
module: 5
arm: "+"
pooled_cpm: 4.7
n_lines_expressing: 47
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TRMT12

*tRNA wybutosine-synthesizing protein 2* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.79× (z +17.9, q 0e+00, up in 33 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.686× (z -4.6, q 0.002, down in 13 of 34 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H2347 0.0825×, LoVo 0.116×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LS 180 0.0793×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HOP62 0.0800×); [[Ipatasertib (drug)]] 0.05 µM in 1 line (HOP62 0.0808×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.211×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLAD1]] (+0.72, fdr 7e-06), [[SCO1]] (+0.67, fdr 7e-06), [[TWNK]] (+0.67, fdr 7e-06); moves opposite to [[SIRT2]] (-0.58, fdr 2e-05), [[MAK]] (-0.56, fdr 3e-04), [[MLF1]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Riluzole hydrochloride (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11431.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +17.9 | 0e+00 | 33/36 (BT-474, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.92×** | +11.4 | 1e-27 | 26/43 (SW1417, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.42×** | +10.9 | 2e-25 | 37/44 (BT-474, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.22×** | +9.9 | 9e-21 | 33/42 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.96×** | +8.3 | 1e-14 | 29/44 (BT-474, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +8.2 | 2e-14 | 5/8 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +6.4 | 1e-08 | 17/40 (RPMI-7951, SHP-77, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.64×** | +5.9 | 3e-07 | 16/33 (SW480, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +5.6 | 2e-06 | 15/44 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.60×** | +5.4 | 4e-06 | 5/14 (HOP62, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.54×** | +5.1 | 2e-05 | 10/27 (NCI-H1573, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.44×** | +4.2 | 0.001 | 12/36 (HS-578T, COLO 205, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.27×** | +4.1 | 0.002 | 13/44 (A498, NCI-H1573, …) | top dose only | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.007 | 11/39 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.38×** | +3.7 | 0.007 | 8/23 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.011 | 4/43 (Panc 03.27, SW1417, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +3.3 | 0.028 | 0/38 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.056 | 0/44 | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.058 | 6/35 (Hs 766T, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.058 | 4/35 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Penfluridol (drug)]] 5 µM |  | **1.28×** | +2.9 | 0.077 | 6/40 (A498, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +2.9 | 0.094 | 7/41 (A-427, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11431.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H2347 0.0825×, LoVo 0.116×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LS 180 0.0793×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HOP62 0.0800×); [[Ipatasertib (drug)]] 0.05 µM in 1 line (HOP62 0.0808×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.211×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.686×** | -4.6 | 0.002 | 13/34 (NCI-H2347, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.770× | -3.2 | 0.35 | 12/44 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11431. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 4.01 | 0 | 2 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0800× (z -9.3) |
| [[PANC-1 (line)]] | alt | 5.37 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -9.0) |
| [[BT-474 (line)]] | alt | 7.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.84× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 5.44 | 0 | 1 | — | [[Rapamycin (drug)]] 0.5 µM 0.101× (z -8.6) |
| [[LoVo (line)]] | wt | 4.58 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -9.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 4.41 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0793× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 3.46 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0825× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 3.34 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.134× (z -9.1) ⚠ transcription drop |
| [[SW480 (line)]] | alt | 5.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +9.3) | — |
| [[A-172 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.550 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.645 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11431), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLAD1]] | +0.72 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[SCO1]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TWNK]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.65 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[ZNF142]] | +0.63 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[PIGW]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[GTPBP10]] | +0.62 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[GTF2E1]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[METTL13]] | +0.61 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD40]] | +0.60 | +0.70 / +0.41 | both halves | 4e-05 |  |
| [[MRM1]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[LSG1]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT2]] | -0.58 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[MAK]] | -0.56 | -0.29 / -0.49 | both halves | 3e-04 |  |
| [[MLF1]] | -0.55 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[CCNI]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[HIP1]] | -0.54 | -0.52 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TRMT12's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Riluzole hydrochloride (drug)]] 0.05 µM | C | TRMT12 activity lowers the cells' numbers under Riluzole hydrochloride 0.05 µM (makes them more sensitive) | lines that do not express TRMT12 (3) vs lines expressing it (45) | the lines without TRMT12: 1.31× the cells of the other lines | 0.041 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000283491, MBOAT2, TRIM68 |
| [[MLF1]] | C | TRMT12 activity raises MLF1's level | lines that do not express TRMT12 (3) vs lines expressing it (47) | 3.84× lower at baseline in the lines without TRMT12 | 0.051 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000283491, MBOAT2, TRIM68 |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.6, -31.9); signed map (-5.0, -41.9). **Vector** length 41.0, 4.35% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +17.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +2.7 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +8.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +4.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.0 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -0.5 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -0.9 | -1.1 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -0.9 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | tRNA wybutosine-synthesizing protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:124,450,820-124,462,150 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20772, Trm12, TYW2; previously TRMT12 |
| Gene groups (HGNC) | 7BS non-methyltransferases |
| Reactome | 4 pathways, smallest: Synthesis of wybutosine at G37 of tRNA(Phe); tRNA modification in the nucleus and cytosol; tRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53H54](https://www.uniprot.org/uniprotkb/Q53H54) (tRNA wybutosine-synthesizing protein 2 homolog):

> S-adenosyl-L-methionine-dependent transferase that acts as a component of the wybutosine biosynthesis pathway. Wybutosine is a hyper modified guanosine with a tricyclic base found at the 3'-position adjacent to the anticodon of eukaryotic phenylalanine tRNA. Catalyzes the transfer of the alpha-amino-alpha-carboxypropyl (acp) group from S-adenosyl-L-methionine to the C-7 position of 4-demethylwyosine (imG-14) to produce wybutosine-86.

**Summary**, from NCBI Gene [55039](https://www.ncbi.nlm.nih.gov/gene/55039):

> Wybutosine (yW) is a hypermodified guanosine at the 3-prime position adjacent to the anticodon of phenylalanine tRNA that stabilizes codon-anticodon interactions during decoding on the ribosome. TRMT12 is the human homolog of a yeast gene essential for yW synthesis (Noma and Suzuki, 2006).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:26091](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26091) · Entrez [55039](https://www.ncbi.nlm.nih.gov/gene/55039) · UniProt [Q53H54](https://www.uniprot.org/uniprotkb/Q53H54) · Ensembl [ENSG00000183665](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183665)

## Data

Gene col 11431: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11431); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11431, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11431]; `tensor/DDL_lfc|DDL_z.npy` [11431]; `embed/gene_vectors.npy` [11431]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11431 or target_col == 11431). Every well: [[TRMT12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMT12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
