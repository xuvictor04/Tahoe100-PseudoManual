---
symbol: "CCDC85A"
type: "gene"
col: 630
ensembl_id: "ENSG00000055813"
name: "coiled-coil domain containing 85A"
location: "2p16.1"
module: 61
arm: "+"
pooled_cpm: 5.61
n_lines_expressing: 31
n_dd_up: 40
n_dd_down: 2
n_dd_up_clean: 37
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# CCDC85A

*coiled-coil domain containing 85A* — 2p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.78× (z +18.8, q 0e+00, up in 19 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.619× (z -4.8, q 8e-04, down in 12 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.115×, BT-474 0.114×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 2 lines (SHP-77 0.181×, HEC-1-A 0.165×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (HEC-1-A 0.126×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (HEC-1-A 0.145×); [[Digitoxin (drug)]] 0.5 µM in 1 line (SHP-77 0.210×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNAP91]] (+0.69, fdr 7e-06), [[ERC2]] (+0.67, fdr 7e-06), [[KCNQ3]] (+0.60, fdr 1e-05); moves opposite to [[RABEP2]] (-0.51, fdr 1e-05), [[SLC30A6]] (-0.47, fdr 3e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ELAVL2]] → it (grade B ⚠); 2 go from it, the strongest it → [[CDC42EP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 630.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.78×** | +18.8 | 0e+00 | 19/25 (BT-474, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.73×** | +18.7 | 0e+00 | 23/27 (NCI-H460, SW1417, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.73×** | +18.6 | 0e+00 | 13/23 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.18×** | +14.3 | 2e-44 | 24/27 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.50×** | +12.5 | 6e-34 | 21/25 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.59×** | +12.3 | 9e-33 | 1/8 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.75×** | +10.1 | 4e-22 | 17/27 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.68×** | +9.9 | 5e-21 | 16/27 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +9.8 | 5e-21 | 2/16 (HS-578T, hTERT-HPNE) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.48×** | +9.1 | 5e-18 | 17/27 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.41×** | +8.8 | 7e-17 | 12/23 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.49×** | +8.8 | 7e-17 | 13/25 (A-172, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.98×** | +7.2 | 2e-11 | 17/26 (A-427, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +7.2 | 2e-11 | 1/11 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +5.8 | 3e-07 | 9/25 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +5.5 | 1e-06 | 7/22 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.62×** | +5.2 | 8e-06 | 11/27 (A-172, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.70×** | +5.1 | 1e-05 | 10/26 (LOX-IMVI, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 630.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.115×, BT-474 0.114×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 2 lines (SHP-77 0.181×, HEC-1-A 0.165×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (HEC-1-A 0.126×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (HEC-1-A 0.145×); [[Digitoxin (drug)]] 0.5 µM in 1 line (SHP-77 0.210×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.619×** | -4.8 | 8e-04 | 12/27 (SHP-77, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.689×** | -3.8 | 0.048 | 14/27 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.725× | -3.2 | 0.18 | 10/27 (HEC-1-A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.728× | -3.2 | 0.18 | 11/27 (BT-474, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 630. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 9.08 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -10.8) |
| [[BT-474 (line)]] | alt | 20.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.48× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.114× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 2.20 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 11.8× (z +10.8) | — |
| [[A-172 (line)]] | wt | 43.7 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 8.42× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.115× (z -10.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 19.2 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 5.19× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 41.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.210× (z -8.7) |
| [[A498 (line)]] | wt | 2.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.68× (z +9.5) | — |
| [[A549 (line)]] | wt | 1.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 4.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +10.7) | — |
| [[J82 (line)]] | alt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 1.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 2.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.3× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 1.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 47.8× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 4.86 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.16× (z +8.6) | — |
| [[A-427 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.763 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.707 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.862 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.672 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.932 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.709 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.798 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.02 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 630), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAP91]] | +0.69 | +0.63 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ERC2]] | +0.67 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[KCNQ3]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[GRIA4]] | +0.59 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[MIR325HG]] | +0.58 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[GPM6A]] | +0.58 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[FAT3]] | +0.57 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[FMN2]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[TBC1D9]] | +0.56 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[UNC80]] | +0.56 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[CDH18]] | +0.56 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[XKR4]] | +0.56 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABEP2]] | -0.51 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[SLC30A6]] | -0.47 | -0.45 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELAVL2]] | B | ELAVL2 activity raises CCDC85A's level | lines that do not express ELAVL2 (34) vs lines expressing it (16) | 2.69× lower at baseline in the lines without ELAVL2 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283982, MIR99AHG, DPP10 |
| [[TOP2A]] | B | TOP2A activity lowers CCDC85A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GUCY1A1]] | C | GUCY1A1 activity raises CCDC85A's level | lines that do not express GUCY1A1 (30) vs lines expressing it (20) | 2.69× lower at baseline in the lines without GUCY1A1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, TLL1, LINC03046; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC42EP3]] | B | CCDC85A activity raises CDC42EP3's level | lines that do not express CCDC85A (19) vs lines expressing it (31) | 2.79× lower at baseline in the lines without CCDC85A | 0.045 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, SERPINB7, KRT86; maybe low, not absent |
| [[WDR17]] | B | CCDC85A activity raises WDR17's level | lines that do not express CCDC85A (19) vs lines expressing it (31) | 2.41× lower at baseline in the lines without CCDC85A | 0.062 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, SERPINB7, KRT86; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.620). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.1, 30.7); signed map (32.9, 21.5). **Vector** length 61.4, 12.7% of its response variance represented; |z| ≥ 3 in 818 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +18.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +18.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +5.1 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | +0.8 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 85A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.1 — chr2:56,183,990-56,386,172 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1912 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PX6](https://www.uniprot.org/uniprotkb/Q96PX6) (Coiled-coil domain-containing protein 85A):

> May play a role in cell-cell adhesion and epithelium development through its interaction with proteins of the beta-catenin family.

**Summary**, from NCBI Gene [114800](https://www.ncbi.nlm.nih.gov/gene/114800):

> Located in adherens junction. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29400](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29400) · Entrez [114800](https://www.ncbi.nlm.nih.gov/gene/114800) · UniProt [Q96PX6](https://www.uniprot.org/uniprotkb/Q96PX6) · Ensembl [ENSG00000055813](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000055813)

## Data

Gene col 630: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 630); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 630, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 630]; `tensor/DDL_lfc|DDL_z.npy` [630]; `embed/gene_vectors.npy` [630]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 630 or target_col == 630). Every well: [[CCDC85A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC85A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
