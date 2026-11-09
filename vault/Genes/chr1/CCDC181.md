---
symbol: "CCDC181"
type: "gene"
col: 3913
ensembl_id: "ENSG00000117477"
name: "coiled-coil domain containing 181"
location: "1q24.2"
module: 39
arm: "+"
pooled_cpm: 5.25
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# CCDC181

*coiled-coil domain containing 181* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.13× (z +24.3, q 0e+00, up in 38 of 39 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Fingolimod (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.0446×; ⚠ toxic); [[Dimethyl fumarate (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0630×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM in 1 line (RPMI-7951 0.0722×); [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0755×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL9]] (+0.76, fdr 7e-06), [[TEX29]] (+0.72, fdr 7e-06), [[LINC01030]] (+0.72, fdr 7e-06); moves opposite to [[NAA40]] (-0.65, fdr 4e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[XG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3913.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.13×** | +24.3 | 0e+00 | 38/39 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.41×** | +13.5 | 4e-39 | 23/35 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.36×** | +11.5 | 3e-28 | 32/39 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.49×** | +11.4 | 8e-28 | 29/38 (SW 900, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.41×** | +11.2 | 6e-27 | 23/29 (CFPAC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.04×** | +9.5 | 1e-19 | 31/45 (NCI-H2347, BT-474, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.02×** | +9.4 | 4e-19 | 26/47 (HOP62, BT-474, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.20×** | +7.5 | 5e-12 | 10/24 (NCI-H460, NCI-H2030, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.20×** | +7.5 | 5e-12 | 30/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.17×** | +7.3 | 1e-11 | 29/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.05×** | +6.8 | 7e-10 | 25/46 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +6.0 | 1e-07 | 15/37 (SW 900, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +5.3 | 4e-06 | 18/41 (A-172, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +5.2 | 8e-06 | 17/46 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.75×** | +5.1 | 1e-05 | 3/8 (HOP62, PANC-1, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +4.5 | 2e-04 | 15/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.55×** | +4.1 | 0.001 | 11/47 (BT-474, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +4.1 | 0.001 | 17/43 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +4.0 | 0.002 | 16/42 (SW 900, NCI-H23, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.52×** | +3.9 | 0.002 | 15/43 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.00×** | +3.4 | 0.016 | 11/42 (BT-474, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Fingolimod (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.0446×; ⚠ toxic); [[Dimethyl fumarate (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0630×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM in 1 line (RPMI-7951 0.0722×); [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0755×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3913. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.92 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 16.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.89× (z +12.6) | — |
| [[HEC-1-A (line)]] | alt | 4.25 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.11× (z +11.0) | [[Dimethyl fumarate (drug)]] 0.05 µM 0.0630× (z -9.5) |
| [[HOP62 (line)]] | alt | 5.22 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 5.77 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.34× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 3.07 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +12.2) | — |
| [[A-172 (line)]] | wt | 2.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.2× (z +10.7) | — |
| [[A498 (line)]] | wt | 3.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.6× (z +14.2) | — |
| [[AsPC-1 (line)]] | alt | 2.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.2× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.45× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 3.51 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0446× (z -9.7) ⚠ toxic |
| [[HT-29 (line)]] | alt | 5.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +10.7) | — |
| [[LoVo (line)]] | wt | 2.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.02× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 4.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.57× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 3.33 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM 0.0755× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 2.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 6.68 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM 0.0722× (z -8.7) |
| [[A-427 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3913), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL9]] | +0.76 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[TEX29]] | +0.72 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[LINC01030]] | +0.72 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[LDHC]] | +0.71 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[SLC4A10]] | +0.71 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.71 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[C21orf91-OT1]] | +0.70 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[CD200R1]] | +0.70 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.70 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[TOMM20L-DT]] | +0.70 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[MFSD2B]] | +0.70 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[PLCD4]] | +0.69 | +0.64 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA40]] | -0.65 | -0.62 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XG]] | B | XG activity lowers CCDC181's level | lines that do not express XG (5) vs lines expressing it (45) | 1.68× higher at baseline in the lines without XG | 0.016 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |
| [[IMPA1P1]] | B | IMPA1P1 activity raises CCDC181's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.86× lower at baseline in the lines without IMPA1P1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CCDC181's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.2, -17.9); signed map (14.1, 8.4). **Vector** length 64.5, 9.93% of its response variance represented; |z| ≥ 3 in 1,121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +24.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.3 | +9.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +11.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +13.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.2 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +5.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +5.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | +2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.5 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +1.9 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 181 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:169,394,870-169,460,669 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25846; previously C1orf114 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TID7](https://www.uniprot.org/uniprotkb/Q5TID7) (Coiled-coil domain-containing protein 181):

> Microtubule-binding protein that is essential for the integrity and function of the manchette, facilitating proper sperm head shaping and subsequent flagellum formation during spermatogenesis.

**Summary**, from NCBI Gene [57821](https://www.ncbi.nlm.nih.gov/gene/57821):

> Predicted to enable microtubule binding activity. Predicted to be involved in manchette assembly and sperm flagellum assembly. Located in axoneme. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28051](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28051) · Entrez [57821](https://www.ncbi.nlm.nih.gov/gene/57821) · UniProt [Q5TID7](https://www.uniprot.org/uniprotkb/Q5TID7) · Ensembl [ENSG00000117477](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117477)

## Data

Gene col 3913: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3913); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3913, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3913]; `tensor/DDL_lfc|DDL_z.npy` [3913]; `embed/gene_vectors.npy` [3913]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3913 or target_col == 3913). Every well: [[CCDC181 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC181.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
