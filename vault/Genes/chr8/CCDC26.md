---
symbol: "CCDC26"
type: "gene"
col: 13694
ensembl_id: "ENSG00000229140"
name: "CCDC26 long non-coding RNA"
location: "8q24.21"
module: 165
arm: "+"
pooled_cpm: 9.62
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# CCDC26

*CCDC26 long non-coding RNA* — 8q24.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 11.1× (z +45.0, q 0e+00, up in 40 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (NCI-H23 0.0549×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (C32 0.0550×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.232×; ⚠ toxic); [[Lenalidomide (hemihydrate) (drug)]] 5 µM in 1 line (RPMI-7951 0.0990×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HPSE2]] (+0.81, fdr 7e-06), [[DPP6]] (+0.79, fdr 7e-06), [[GALNTL6]] (+0.78, fdr 7e-06).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13694.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **11.1×** | +45.0 | 0e+00 | 40/41 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **7.19×** | +26.2 | 0e+00 | 41/42 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.99×** | +14.5 | 1e-45 | 17/25 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.16×** | +14.1 | 4e-43 | 11/18 (NCI-H460, J82, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.07×** | +13.7 | 2e-40 | 31/46 (NCI-H460, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.78×** | +13.0 | 7e-37 | 8/11 (NCI-H1792, HOP62, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.99×** | +12.9 | 5e-36 | 29/44 (SW480, BT-474, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +10.9 | 1e-25 | 21/37 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +9.9 | 2e-21 | 24/40 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.95×** | +8.9 | 5e-17 | 24/44 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +7.6 | 2e-12 | 17/38 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +7.1 | 5e-11 | 17/43 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.37×** | +5.9 | 2e-07 | 14/44 (A549, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.8 | 7e-05 | 11/36 (C32, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +4.8 | 7e-05 | 6/28 (SW1417, RKO, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.007 | 4/38 (SHP-77, A549, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Temsirolimus (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.012 | 6/44 (Hs 766T, HT-29, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.014 | 0/42 | inconsistent across doses | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.035 | 5/44 (H4, RPMI-7951, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13694.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (NCI-H23 0.0549×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (C32 0.0550×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.232×; ⚠ toxic); [[Lenalidomide (hemihydrate) (drug)]] 5 µM in 1 line (RPMI-7951 0.0990×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -4.4 | 0.007 | 6/48 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.788× | -3.2 | 0.43 | 10/44 (LOX-IMVI, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13694. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.1 | 8 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.7× (z +22.7) | — |
| [[C32 (line)]] | wt | 18.4 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 21.8× (z +17.1) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0550× (z -11.3) |
| [[A498 (line)]] | wt | 4.47 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +14.6) | — |
| [[NCI-H23 (line)]] | alt | 12.2 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 19.9× (z +12.7) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0549× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 4.64 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.7× (z +16.8) | — |
| [[A-172 (line)]] | wt | 3.20 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.7× (z +12.3) | — |
| [[A549 (line)]] | wt | 2.96 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 35.9× (z +13.7) | — |
| [[HEC-1-A (line)]] | alt | 4.11 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.4× (z +15.3) | — |
| [[HOP62 (line)]] | alt | 3.70 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +13.7) | — |
| [[NCI-H1792 (line)]] | alt | 159 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.232× (z -10.3) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 3.10 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.5× (z +16.4) | — |
| [[RPMI-7951 (line)]] | alt | 3.60 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.3× (z +10.2) | [[Lenalidomide (hemihydrate) (drug)]] 5 µM 0.0990× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 3.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 5.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 2.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.3× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 3.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 3.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.0× (z +13.0) | — |
| [[HT-29 (line)]] | alt | 3.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.3× (z +13.1) | — |
| [[J82 (line)]] | alt | 4.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +12.0) | — |
| [[KATO III (line)]] | alt | 3.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +11.5) | — |
| [[LoVo (line)]] | wt | 2.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.3× (z +15.0) | — |
| [[LOX-IMVI (line)]] | wt | 18.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.59× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 2.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.0× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 4.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.24× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 3.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.92× (z +11.3) | — |
| [[NCI-H2347 (line)]] | alt | 2.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.92× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 3.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.4× (z +10.3) | — |
| [[RKO (line)]] | wt | 3.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 43.0× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.105× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 2.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.9× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 3.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +10.0) | — |
| [[A-427 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13694), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPSE2]] | +0.81 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[DPP6]] | +0.79 | +0.61 / +0.78 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.78 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[SORCS3]] | +0.78 | +0.62 / +0.80 | both halves | 7e-06 |  |
| [[ATP8A2]] | +0.77 | +0.69 / +0.81 | both halves | 7e-06 |  |
| [[SLC27A6]] | +0.77 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.77 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[GRM8]] | +0.75 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[CLVS1]] | +0.75 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[RELN]] | +0.75 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[THSD7B]] | +0.75 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.74 | +0.64 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC26's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.7% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[SLC35F4]] | B | SLC35F4 activity lowers CCDC26's level | lines that do not express SLC35F4 (6) vs lines expressing it (44) | 2.95× higher at baseline in the lines without SLC35F4 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC01811, LINC01482; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.824). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.6, 28.4); signed map (32.3, 13.3). **Vector** length 76.0, 13.0% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +14.0 | +45.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.6 | +14.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.6 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.9 | +14.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.0 | +13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.9 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +12.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.2 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +0.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | CCDC26 long non-coding RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q24.21 — chr8:128,634,199-129,683,770 (-) |
| Ensembl biotype | lncRNA |
| Also known as | MGC27434, RAM |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [137196](https://www.ncbi.nlm.nih.gov/gene/137196):

> Implicated in brain cancer and high grade glioma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28416](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28416) · Entrez [137196](https://www.ncbi.nlm.nih.gov/gene/137196) · Ensembl [ENSG00000229140](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229140)

## Data

Gene col 13694: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13694); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13694, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13694]; `tensor/DDL_lfc|DDL_z.npy` [13694]; `embed/gene_vectors.npy` [13694]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13694 or target_col == 13694). Every well: [[CCDC26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
