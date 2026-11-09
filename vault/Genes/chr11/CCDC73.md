---
symbol: "CCDC73"
type: "gene"
col: 11848
ensembl_id: "ENSG00000186714"
name: "coiled-coil domain containing 73"
location: "11p13"
module: 35
arm: "+"
pooled_cpm: 2.71
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# CCDC73

*coiled-coil domain containing 73* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 9.10× (z +33.5, q 0e+00, up in 32 of 32 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (RKO 0.0912×, J82 0.207×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (RKO 0.0746×); [[Belinostat (drug)]] 5 µM in 1 line (J82 0.129×; ⚠ cell-cycle shift, explains ~0% of this change); [[Radotinib (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0677×); [[Fumaric acid (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0638×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC27A6]] (+0.75, fdr 7e-06), [[CIBAR1-DT]] (+0.73, fdr 1e-05), [[ST7-AS2]] (+0.73, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11848.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **9.10×** | +33.5 | 0e+00 | 32/32 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.71×** | +15.1 | 0e+00 | 20/33 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.92×** | +14.1 | 9e-43 | 1/4 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.11×** | +14.0 | 2e-42 | 3/4 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.29×** | +12.7 | 4e-35 | 6/12 (SW 900, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.81×** | +11.1 | 1e-26 | 29/40 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.93×** | +11.1 | 1e-26 | 25/32 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.74×** | +10.8 | 2e-25 | 21/37 (C32, BT-474, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +10.6 | 3e-24 | 20/27 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.89×** | +9.6 | 4e-20 | 19/43 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.04×** | +7.6 | 1e-12 | 16/42 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +7.1 | 4e-11 | 12/31 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +7.1 | 5e-11 | 3/12 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +5.1 | 1e-05 | 12/43 (SW480, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +4.9 | 4e-05 | 13/32 (BT-474, RKO, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +4.7 | 9e-05 | 11/40 (BT-474, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +4.6 | 2e-04 | 3/42 (LoVo, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.43×** | +3.8 | 0.004 | 4/36 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.009 | 5/40 (BT-474, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (RKO 0.0912×, J82 0.207×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (RKO 0.0746×); [[Belinostat (drug)]] 5 µM in 1 line (J82 0.129×; ⚠ cell-cycle shift, explains ~0% of this change); [[Radotinib (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0677×); [[Fumaric acid (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0638×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11848. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 14.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +9.9) | [[Simotinib (drug)]] 5 µM 0.0943× (z -8.8) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 2.95 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.49× (z +11.1) | [[Radotinib (drug)]] 0.5 µM 0.0677× (z -9.4) |
| [[J82 (line)]] | alt | 12.3 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.129× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 3.27 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +12.4) | — |
| [[RKO (line)]] | wt | 12.7 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0746× (z -11.8) |
| [[A-172 (line)]] | wt | 1.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.7× (z +10.6) | — |
| [[A498 (line)]] | wt | 2.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +13.3) | — |
| [[A549 (line)]] | wt | 2.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.10× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 5.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 1.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 3.18 | 0 | 1 | — | [[Fumaric acid (drug)]] 0.05 µM 0.0638× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 1.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.81× (z +10.3) | — |
| [[PANC-1 (line)]] | alt | 1.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +12.0) | — |
| [[SW480 (line)]] | alt | 2.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.35× (z +12.3) | — |
| [[A-427 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11848), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A6]] | +0.75 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[CIBAR1-DT]] | +0.73 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ST7-AS2]] | +0.73 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[HSD11B1-AS1]] | +0.73 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[MED28-DT]] | +0.73 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[TP53TG5]] | +0.73 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[DENND6A-AS1]] | +0.72 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[PSMD14-DT]] | +0.72 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[LRRC8C-DT]] | +0.72 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[LINC01090]] | +0.72 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[CCDC26]] | +0.72 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[ZFHX2-AS1]] | +0.72 | +0.57 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC73's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PRRG4]] | B | PRRG4 activity raises CCDC73's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 1.53× lower at baseline in the lines without PRRG4 | 0.074 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |
| [[TRPM2]] | B | TRPM2 activity lowers CCDC73's level | lines that do not express TRPM2 (11) vs lines expressing it (39) | 1.32× higher at baseline in the lines without TRPM2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.759). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (16.4, 23.5); signed map (30.5, 3.5). **Vector** length 60.6, 8.89% of its response variance represented; |z| ≥ 3 in 1,063 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +33.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +14.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +14.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +5.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +3.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.3 | -1.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -0.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.2 | -0.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 73 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:32,602,721-32,794,662 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NY-SAR-79 |
| Matched by | ensembl_id |

UniProt [Q6ZRK6](https://www.uniprot.org/uniprotkb/Q6ZRK6) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23261](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23261) · Entrez [493860](https://www.ncbi.nlm.nih.gov/gene/493860) · UniProt [Q6ZRK6](https://www.uniprot.org/uniprotkb/Q6ZRK6) · Ensembl [ENSG00000186714](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186714)

## Data

Gene col 11848: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11848); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11848, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11848]; `tensor/DDL_lfc|DDL_z.npy` [11848]; `embed/gene_vectors.npy` [11848]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11848 or target_col == 11848). Every well: [[CCDC73 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC73.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
