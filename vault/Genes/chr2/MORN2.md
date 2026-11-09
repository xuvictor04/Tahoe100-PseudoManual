---
symbol: "MORN2"
type: "gene"
col: 11967
ensembl_id: "ENSG00000188010"
name: "MORN repeat containing 2"
location: "2p22.1"
module: 12
arm: "+"
pooled_cpm: 10.26
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MORN2

*MORN repeat containing 2* — 2p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (17 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.67× (z +12.3, q 8e-32, up in 41 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.701× (z -4.4, q 0.006, down in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Tucidinostat (drug)]] 5 µM in 1 line (MIA PaCa-2 0.155×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OSCP1]] (+0.78, fdr 7e-06), [[SYNRG]] (+0.69, fdr 7e-06), [[DNAL4]] (+0.69, fdr 7e-06); moves opposite to [[MAT2A]] (-0.59, fdr 7e-06), [[IPO7]] (-0.58, fdr 1e-05), [[TCOF1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 17 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11967.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.67×** | +12.3 | 8e-32 | 41/44 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.41×** | +11.0 | 1e-25 | 38/43 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.23×** | +10.0 | 4e-21 | 18/18 (A498, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **3.17×** | +9.6 | 1e-19 | 28/32 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.93×** | +9.5 | 2e-19 | 45/47 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.92×** | +9.5 | 3e-19 | 46/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.81×** | +8.8 | 1e-16 | 30/35 (NCI-H1573, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.67×** | +8.7 | 3e-16 | 43/46 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.62×** | +7.9 | 2e-13 | 22/24 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +6.6 | 3e-09 | 27/44 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.09×** | +6.3 | 2e-08 | 32/45 (PANC-1, SW480, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.06×** | +6.2 | 3e-08 | 28/44 (NCI-H23, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.85×** | +5.5 | 2e-06 | 28/41 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.83×** | +5.1 | 1e-05 | 25/43 (SW480, NCI-H23, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.8 | 5e-05 | 23/47 (PANC-1, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +4.0 | 0.002 | 21/45 (PANC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.004 | 21/47 (SW480, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.034 | 14/46 (SW480, H4, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.048 | 15/46 (NCI-H2030, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11967.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Tucidinostat (drug)]] 5 µM in 1 line (MIA PaCa-2 0.155×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.701×** | -4.4 | 0.006 | 27/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.694× | -3.2 | 0.37 | 15/45 (LOX-IMVI, LS 180, …) | rises with dose |  |
| [[Pentagastrin (drug)]] 5 µM |  | 0.780× | -3.1 | 0.39 | 14/47 (AN3 CA, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11967. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 15.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +12.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.71× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 17.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +13.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 7.12 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +10.0) | — |
| [[SW480 (line)]] | alt | 9.81 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +11.5) | — |
| [[A549 (line)]] | wt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 9.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.62 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.155× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 23.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +11.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11967), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSCP1]] | +0.78 | +0.78 / +0.72 | both halves | 7e-06 | STRING 420 |
| [[SYNRG]] | +0.69 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[DNAL4]] | +0.69 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[IFT22]] | +0.66 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[NUDT16L1]] | +0.64 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[DCTN3]] | +0.64 | +0.58 / +0.74 | both halves | 8e-06 |  |
| [[DRC3]] | +0.64 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[BBOF1]] | +0.63 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[TOGARAM1]] | +0.63 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[ARF5]] | +0.63 | +0.36 / +0.71 | both halves | 1e-04 |  |
| [[DNAJC27]] | +0.61 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[ASB8]] | +0.60 | +0.66 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAT2A]] | -0.59 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[IPO7]] | -0.58 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[TCOF1]] | -0.58 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[CCT5]] | -0.56 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[AHCY]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[GART]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[DKC1]] | -0.54 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[SLC19A1]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[NUP210]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[MCOLN2]] | -0.53 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[TFDP1]] | -0.52 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[ARHGAP4]] | -0.52 | -0.58 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MORN2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GIHCG]] | B | GIHCG activity raises MORN2's level | lines that do not express GIHCG (9) vs lines expressing it (41) | 1.73× lower at baseline in the lines without GIHCG | 0.036 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, LIX1L, HLTF; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.479). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.5, -8.7); signed map (-9.7, -2.2). **Vector** length 63.4, 12.2% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.9 | +11.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +12.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.3 | +6.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.1 | +6.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +1.4 |
|  | [[Sulfatinib (drug)]] 5 µM |  | +1.3 | +3.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.2 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.7 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.5 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -1.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | MORN repeat containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.1 — chr2:38,875,976-38,929,072 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MOPT |
| Gene groups (HGNC) | MORN repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q502X0](https://www.uniprot.org/uniprotkb/Q502X0) (MORN repeat-containing protein 2):

> Might have a role in spermatogenesis.

**Summary**, from NCBI Gene [729967](https://www.ncbi.nlm.nih.gov/gene/729967):

> Predicted to be involved in cell differentiation and spermatogenesis. Predicted to be located in acrosomal vesicle and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30166](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30166) · Entrez [729967](https://www.ncbi.nlm.nih.gov/gene/729967) · UniProt [Q502X0](https://www.uniprot.org/uniprotkb/Q502X0) · Ensembl [ENSG00000188010](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188010)

## Data

Gene col 11967: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11967); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11967, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11967]; `tensor/DDL_lfc|DDL_z.npy` [11967]; `embed/gene_vectors.npy` [11967]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11967 or target_col == 11967). Every well: [[MORN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MORN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
