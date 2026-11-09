---
symbol: "TRAPPC2B"
type: "gene"
col: 14972
ensembl_id: "ENSG00000256060"
name: "trafficking protein particle complex subunit 2B"
location: "19q13.43"
module: 149
arm: "+"
pooled_cpm: 4.59
n_lines_expressing: 43
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# TRAPPC2B

*trafficking protein particle complex subunit 2B* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.21× (z +5.9, q 2e-06, up in 24 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (KATO III 0.151×, NCI-H2347 0.0906×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (A498 0.0753×; ⚠ cell-cycle shift, explains ~40% of this change); [[Doxycycline (monohydrate) (drug)]] 5 µM in 1 line (HOP62 0.0691×); [[Alpelisib (drug)]] 0.05 µM in 1 line (H4 0.0744×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM26]] (+0.74, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[TTF1]] (+0.73, fdr 7e-06), [[RNF181]] (+0.72, fdr 7e-06), [[EMC6]] (+0.71, fdr 8e-06); moves opposite to [[HNRNPA3]] (-0.71, fdr 7e-06), [[IPO5]] (-0.69, fdr 1e-05), [[DHFR]] (-0.69, fdr 3e-05).
> It is in [[Module 149]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF10]] → it (grade B ⚠); 7 go from it, the strongest it → [[ZNF10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14972.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.21×** | +5.9 | 2e-06 | 24/37 (HOP62, KATO III, …) | two highest doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.19×** | +5.5 | 1e-05 | 25/35 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.3 | 0.004 | 13/26 (PANC-1, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.76×** | +4.2 | 0.004 | 12/25 (KATO III, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +3.6 | 0.031 | 15/38 (PANC-1, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.51× | +3.1 | 0.21 | 8/36 (KATO III, COLO 205, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14972.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (KATO III 0.151×, NCI-H2347 0.0906×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (A498 0.0753×; ⚠ cell-cycle shift, explains ~40% of this change); [[Doxycycline (monohydrate) (drug)]] 5 µM in 1 line (HOP62 0.0691×); [[Alpelisib (drug)]] 0.05 µM in 1 line (H4 0.0744×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.635× | -3.4 | 0.38 | 14/39 (AN3 CA, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14972. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.54 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 3.90 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0753× (z -9.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A549 (line)]] | wt | 4.37 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0801× (z -8.9) ⚠ toxic |
| [[H4 (line)]] | wt | 11.3 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0744× (z -8.5) |
| [[HOP62 (line)]] | alt | 3.44 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0691× (z -9.1) |
| [[KATO III (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 3.89 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0906× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.503 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14972), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | +0.74 | +0.59 / +0.77 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[TTF1]] | +0.73 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[RNF181]] | +0.72 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[EMC6]] | +0.71 | +0.57 / +0.75 | both halves | 8e-06 |  |
| [[DCP1A]] | +0.70 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[MRPS18C]] | +0.70 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[NKAP]] | +0.69 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[PIGBOS1]] | +0.69 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | +0.69 | +0.39 / +0.78 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[IGBP1]] | +0.68 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[ZNF791]] | +0.68 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[WDR83OS]] ⚠ | +0.68 | +0.61 / +0.68 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SCAND1]] | +0.67 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[MED19]] | +0.67 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ADPRS]] | +0.66 | +0.50 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPA3]] | -0.71 | -0.62 / -0.71 | both halves | 7e-06 |  |
| [[IPO5]] | -0.69 | -0.56 / -0.73 | both halves | 1e-05 |  |
| [[DHFR]] | -0.69 | -0.45 / -0.74 | both halves | 3e-05 |  |
| [[EMB]] | -0.66 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[PTPN18]] | -0.66 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.65 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[VMA21]] | -0.64 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[UBE2G2]] | -0.64 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[FAM120A]] | -0.63 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[BTBD1]] | -0.63 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[CTSZ]] | -0.63 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[TMEM237]] | -0.63 | -0.45 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF10]] | B | ZNF10 activity raises TRAPPC2B's level | lines that do not express ZNF10 (7) vs lines expressing it (43) | 1.90× lower at baseline in the lines without ZNF10 | 0.048 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KMT2D; also absent: ENSG00000256825, ZNF140, CEP126 |
| [[PSMB5]] | B | PSMB5 activity lowers TRAPPC2B's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF611]] | C | ZNF611 activity raises TRAPPC2B's level | lines that do not express ZNF611 (3) vs lines expressing it (47) | 2.90× lower at baseline in the lines without ZNF611 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF468, ZNF845, ZNF14; its own permutation p |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF10]] | B | TRAPPC2B activity raises ZNF10's level | lines that do not express TRAPPC2B (7) vs lines expressing it (43) | 3.46× lower at baseline in the lines without TRAPPC2B | 0.012 | ⚠ within organs, on part of the lines; also absent: ZNF547, ZNF548, ZNF530 |
| [[ZNF761]] | B | TRAPPC2B activity raises ZNF761's level | lines that do not express TRAPPC2B (7) vs lines expressing it (43) | 1.93× lower at baseline in the lines without TRAPPC2B | 0.023 | ⚠ within organs, on part of the lines; also absent: ZNF547, ZNF548, ZNF530 |
| [[ZNF765]] | B | TRAPPC2B activity raises ZNF765's level | lines that do not express TRAPPC2B (7) vs lines expressing it (43) | 1.73× lower at baseline in the lines without TRAPPC2B | 0.033 | ⚠ within organs, on part of the lines; also absent: ZNF547, ZNF548, ZNF530 |
| [[RPL36AL]] | B | TRAPPC2B activity lowers RPL36AL's level | lines that do not express TRAPPC2B (7) vs lines expressing it (43) | 1.48× higher at baseline in the lines without TRAPPC2B | 0.039 | ⚠ within organs, on part of the lines; also absent: ZNF547, ZNF548, ZNF530 |
| [[RPP21]] | B | TRAPPC2B activity lowers RPP21's level | lines that do not express TRAPPC2B (7) vs lines expressing it (43) | 1.26× higher at baseline in the lines without TRAPPC2B | 0.047 | ⚠ within organs, on part of the lines; also absent: ZNF547, ZNF548, ZNF530 |
| [[ZNF611]] | B | TRAPPC2B activity raises ZNF611's level | lines that do not express TRAPPC2B (7) vs lines expressing it (43) | 2.08× lower at baseline in the lines without TRAPPC2B | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF547, ZNF548, ZNF530 |
| [[FKBP1A]] | B | TRAPPC2B activity raises FKBP1A's level | lines that do not express TRAPPC2B (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without TRAPPC2B | 0.097 | ⚠ within organs, on part of the lines; also absent: ZNF547, ZNF548, ZNF530 |

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.4, -11.5); signed map (-9.0, -7.5). **Vector** length 56.5, 10.6% of its response variance represented; |z| ≥ 3 in 507 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.5 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.2 | +1.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +2.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.0 | +2.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +0.9 | +1.8 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.2 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.1 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.7 | +0.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.4 | -1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.2 | -0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -0.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.1 | +0.0 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | -1.0 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | trafficking protein particle complex subunit 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:57,363,551-57,365,405 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SEDLP1, MIP-2A; previously SEDLP, TRAPPC2P1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P0DI82](https://www.uniprot.org/uniprotkb/P0DI82) (Trafficking protein particle complex subunit 2B):

> Prevents transcriptional repression and induction of cell death by ENO1. May play a role in vesicular transport from endoplasmic reticulum to Golgi.

**Summary**, from NCBI Gene [10597](https://www.ncbi.nlm.nih.gov/gene/10597):

> Enables transcription corepressor binding activity; transcription regulator inhibitor activity; and transmembrane transporter binding activity. Involved in positive regulation of gene expression and skeletal system development. Located in endoplasmic reticulum; nuclear outer membrane; and perinuclear region of cytoplasm. Part of TRAPP complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10710](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10710) · Entrez [10597](https://www.ncbi.nlm.nih.gov/gene/10597) · UniProt [P0DI82](https://www.uniprot.org/uniprotkb/P0DI82) · Ensembl [ENSG00000256060](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256060)

## Data

Gene col 14972: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14972); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14972, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14972]; `tensor/DDL_lfc|DDL_z.npy` [14972]; `embed/gene_vectors.npy` [14972]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14972 or target_col == 14972). Every well: [[TRAPPC2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAPPC2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
