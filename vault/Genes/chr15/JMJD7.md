---
symbol: "JMJD7"
type: "gene"
col: 14378
ensembl_id: "ENSG00000243789"
name: "jumonji domain containing 7"
location: "15q15.1"
module: 153
arm: "+"
pooled_cpm: 5.54
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# JMJD7

*jumonji domain containing 7* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.95× (z +7.7, q 7e-12, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.703× (z -4.1, q 0.015, down in 17 of 47 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Sulfatinib (drug)]] 5 µM: 0.697× (z -4.0, q 0.015, down in 13 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 0.0904×, HEC-1-A 0.1000×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H23 0.0883×; ⚠ cell-cycle shift, explains ~0% of this change); [[Vilanterol (drug)]] 0.5 µM in 1 line (BT-474 0.0926×); [[Hesperidin (drug)]] 5 µM in 1 line (A549 0.0985×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLA2G4B]] (+0.73, fdr 7e-06, ⚠ same locus), [[OPLAH]] (+0.65, fdr 7e-06, ⚠ OPLAH in the vector space only through flagged drug-doses), [[NBEAL2]] (+0.64, fdr 1e-05), [[PCNX3]] (+0.64, fdr 1e-05), [[CYP2D7]] (+0.62, fdr 1e-05); moves opposite to [[YY1]] (-0.62, fdr 1e-05), [[SCAF11]] (-0.59, fdr 2e-05), [[NR2F2]] (-0.59, fdr 1e-05).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14378.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +7.7 | 7e-12 | 32/47 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +6.5 | 2e-08 | 26/45 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +4.3 | 0.003 | 11/46 (PANC-1, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.6 | 0.050 | 3/48 (LoVo, RKO, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.43×** | +3.4 | 0.075 | 3/46 (C32, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.075 | 2/45 (SW 900, PANC-1) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.078 | 6/43 (SNU-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.086 | 3/47 (NCI-H1573, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.086 | 6/47 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.33×** | +3.1 | 0.093 | 5/37 (A-172, AsPC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **1.33×** | +3.1 | 0.093 | 6/34 (SK-MEL-2, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14378.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 0.0904×, HEC-1-A 0.1000×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H23 0.0883×; ⚠ cell-cycle shift, explains ~0% of this change); [[Vilanterol (drug)]] 0.5 µM in 1 line (BT-474 0.0926×); [[Hesperidin (drug)]] 5 µM in 1 line (A549 0.0985×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.703×** | -4.1 | 0.015 | 17/47 (PANC-1, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Sulfatinib (drug)]] 5 µM |  | **0.697×** | -4.0 | 0.015 | 13/43 (HCT15, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.732×** | -3.6 | 0.054 | 19/41 (HOP62, SW480, …) | rises with dose |  |
| [[Sinomenine (drug)]] 0.5 µM |  | 0.752× | -3.3 | 0.13 | 4/45 (AN3 CA, J82, …) | inconsistent across doses | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.758× | -3.2 | 0.14 | 6/47 (HEC-1-A, NCI-H661, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.768× | -3.1 | 0.19 | 6/44 (SHP-77, SK-MEL-2, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14378. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 4.75 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0985× (z -8.7) |
| [[BT-474 (line)]] | alt | 6.30 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0926× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 7.68 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.1000× (z -9.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 3.60 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H23 (line)]] | alt | 5.59 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0883× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 7.13 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0904× (z -11.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14378), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLA2G4B]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 | STRING 624; ⚠ same locus (0.2 kb, same strand: neighbours can correlate without regulation) |
| [[OPLAH]] ⚠ | +0.65 | +0.62 / +0.63 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[NBEAL2]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[PCNX3]] | +0.64 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[CYP2D7]] | +0.62 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[BMS1P2]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[DTX2P1]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ABHD17A]] | +0.60 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[WASH9P]] | +0.58 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[KAT2A]] | +0.57 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[ANAPC2]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[WASH8P]] ⚠ | +0.56 | +0.53 / +0.59 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ARHGAP4]] | +0.55 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ADAMTSL5]] | +0.55 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[CUL9]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YY1]] | -0.62 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[SCAF11]] | -0.59 | -0.49 / -0.58 | both halves | 2e-05 |  |
| [[NR2F2]] | -0.59 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[REST]] | -0.56 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[PURA]] | -0.55 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[THAP1]] | -0.53 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[LINC02307]] | -0.52 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[ASH1L]] | -0.52 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[SIRT1]] | -0.51 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[ANKRD12]] | -0.51 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[CRIP1]] | -0.51 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[RSF1]] | -0.51 | -0.36 / -0.52 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers JMJD7's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.421). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.2, -24.4); signed map (-12.6, -32.1). **Vector** length 45.2, 4.86% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.3 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.0 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | -3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.6 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +1.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.2 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.2 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | +2.1 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.0 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | -0.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -1.8 | -4.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -1.8 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | jumonji domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:41,828,092-41,837,581 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Iron (II) and 2-oxoglutarate dependent oxygenases |
| Reactome | 2 pathways, smallest: Protein hydroxylation; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P0C870](https://www.uniprot.org/uniprotkb/P0C870) (Bifunctional peptidase and):

> Bifunctional enzyme that acts both as an endopeptidase and 2-oxoglutarate-dependent monooxygenase. Endopeptidase that cleaves histones N-terminal tails at the carboxyl side of methylated arginine or lysine residues, to generate 'tailless nucleosomes', which may trigger transcription elongation. Preferentially recognizes and cleaves monomethylated and dimethylated arginine residues of histones H2, H3 and H4. After initial cleavage, continues to digest histones tails via its aminopeptidase …

**Summary**, from NCBI Gene [100137047](https://www.ncbi.nlm.nih.gov/gene/100137047):

> This gene encodes a highly conserved protein with a JmjC domain, which are part of the cupin metalloenzyme superfamily. JmjC proteins may function as 2-oxoglutarate-Fe(II)-dependent dioxygenases. Most tissues also express read-through transcripts from this gene into the downstream phospholipase A2, group IVB (cytosolic) gene, some of which may encode fusion proteins combining the N-terminus of this protein with the phospholipase A2, group IVB protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:34397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34397) · Entrez [100137047](https://www.ncbi.nlm.nih.gov/gene/100137047) · UniProt [P0C870](https://www.uniprot.org/uniprotkb/P0C870) · Ensembl [ENSG00000243789](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243789)

## Data

Gene col 14378: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14378); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14378, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14378]; `tensor/DDL_lfc|DDL_z.npy` [14378]; `embed/gene_vectors.npy` [14378]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14378 or target_col == 14378). Every well: [[JMJD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JMJD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
