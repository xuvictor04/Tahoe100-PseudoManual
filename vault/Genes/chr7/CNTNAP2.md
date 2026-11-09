---
symbol: "CNTNAP2"
type: "gene"
col: 10496
ensembl_id: "ENSG00000174469"
name: "contactin associated protein 2"
location: "7q35-q36.1"
module: 90
arm: "+"
pooled_cpm: 29.53
n_lines_expressing: 40
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 13
direction_downstream: 4
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# CNTNAP2

*contactin associated protein 2* — 7q35-q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.40× (z +24.7, q 0e+00, up in 28 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 5 lines (SHP-77 0.346×, LoVo 0.207×, KATO III 0.207×, RPMI-7951 0.218×, …); [[Topotecan (hydrochloride) (drug)]] 5 µM in 4 lines (SHP-77 0.167×, RPMI-7951 0.0478×, LoVo 0.174×, LOX-IMVI 0.199×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.367×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.528×); [[Pemetrexed (drug)]] 5 µM in 1 line (H4 0.0642×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00298]] (+0.68, fdr 1e-05), [[MIR325HG]] (+0.67, fdr 7e-06), [[CNBD1]] (+0.66, fdr 1e-05).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[LINC01980]] → it (grade B ⚠); 4 go from it, the strongest it → [[SLC7A8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10496.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.40×** | +24.7 | 0e+00 | 28/33 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.96×** | +21.9 | 0e+00 | 27/35 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.31×** | +20.1 | 0e+00 | 13/19 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.73×** | +18.8 | 0e+00 | 20/29 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.06×** | +14.6 | 0e+00 | 33/38 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.48×** | +13.0 | 1e-36 | 24/37 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.62×** | +12.7 | 3e-35 | 15/25 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.78×** | +8.2 | 1e-14 | 21/35 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +7.5 | 4e-12 | 16/33 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +7.2 | 3e-11 | 20/38 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +7.1 | 7e-11 | 24/36 (LoVo, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +6.6 | 2e-09 | 17/36 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +6.2 | 2e-08 | 17/38 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +5.6 | 7e-07 | 11/34 (A-172, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.3 | 5e-06 | 10/35 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +4.9 | 4e-05 | 15/37 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.38×** | +4.4 | 4e-04 | 8/36 (H4, AsPC-1, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 4e-04 | 12/38 (SW480, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +4.2 | 7e-04 | 15/35 (SW480, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10496.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 5 lines (SHP-77 0.346×, LoVo 0.207×, KATO III 0.207×, RPMI-7951 0.218×, …); [[Topotecan (hydrochloride) (drug)]] 5 µM in 4 lines (SHP-77 0.167×, RPMI-7951 0.0478×, LoVo 0.174×, LOX-IMVI 0.199×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.367×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.528×); [[Pemetrexed (drug)]] 5 µM in 1 line (H4 0.0642×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.914× | -4.5 | 0.003 | 4/39 (HOP62, AsPC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.790× | -3.4 | 0.19 | 11/37 (SHP-77, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.781× | -3.3 | 0.19 | 8/33 (SNU-423, HS-578T, …) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.793× | -3.1 | 0.29 | 4/38 (SW 1088, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10496. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 20.6 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.98× (z +13.4) | — |
| [[LoVo (line)]] | wt | 85.8 | 4 (1 ⚠) | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.16× (z +11.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.174× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.207× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 17.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +13.6) | — |
| [[NCI-H23 (line)]] | alt | 8.39 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +16.6) | — |
| [[SHP-77 (line)]] | alt | 576 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.167× (z -17.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.346× (z -10.8) |
| [[A-172 (line)]] | wt | 10.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +18.7) | — |
| [[C32 (line)]] | wt | 8.71 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.5× (z +17.3) | — |
| [[SW480 (line)]] | alt | 49.3 | 4 | 0 | [[Cobimetinib (drug)]] 5 µM 6.68× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 7.98 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.21× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 7.98 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.21× (z +12.1) | — |
| [[BT-474 (line)]] | alt | 44.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +13.5) | — |
| [[HT-29 (line)]] | alt | 9.18 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.91× (z +10.8) | — |
| [[KATO III (line)]] | alt | 39.3 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.90× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.207× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 43.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +12.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.199× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 24.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.65× (z +12.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 119 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0478× (z -17.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.218× (z -9.0) |
| [[A-427 (line)]] | wt | 7.94 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.90× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 7.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +9.0) | — |
| [[H4 (line)]] | wt | 19.5 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0642× (z -8.7) |
| [[HCT15 (line)]] | alt | 9.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.97× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 36.4 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.193× (z -8.6) |
| [[SNU-423 (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.58× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 8.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +9.1) | — |
| [[SW48 (line)]] | wt | 31.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +9.4) | — |
| [[A549 (line)]] | wt | 6.39 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.22 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 69.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.53 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.33 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.54 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.14 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.32 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10496), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00298]] | +0.68 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[MIR325HG]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[CNBD1]] | +0.66 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[GRM7]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[KIF6]] | +0.65 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[LINC00871]] | +0.65 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[LINC02208]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[RALYL]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[SORCS1]] | +0.62 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[CSMD1]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[LUZP2]] | +0.61 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[LINC01226]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01980]] | B | LINC01980 activity raises CNTNAP2's level | lines that do not express LINC01980 (22) vs lines expressing it (28) | 2.54× lower at baseline in the lines without LINC01980 | 0.007 | ⚠ within organs, on part of the lines; also absent: KCNMB2, LINC00698, PAPPA2; maybe low, not absent |
| [[SLC24A3]] | B | SLC24A3 activity raises CNTNAP2's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 3.26× lower at baseline in the lines without SLC24A3 | 0.011 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[PGR]] | B | PGR activity raises CNTNAP2's level | lines that do not express PGR (36) vs lines expressing it (14) | 2.52× lower at baseline in the lines without PGR | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent |
| [[LINC01611]] | B | LINC01611 activity raises CNTNAP2's level | lines that do not express LINC01611 (34) vs lines expressing it (16) | 2.08× lower at baseline in the lines without LINC01611 | 0.015 | ⚠ within organs, on part of the lines; also absent: CDH13, ENSG00000248973, LINC02377 |
| [[POU6F2]] | B | POU6F2 activity raises CNTNAP2's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 2.57× lower at baseline in the lines without POU6F2 | 0.028 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[LRP2]] | B | LRP2 activity raises CNTNAP2's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 2.02× lower at baseline in the lines without LRP2 | 0.040 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent |
| [[SLC24A3]] | B | SLC24A3 activity weakens CNTNAP2's drug response | lines that do not express SLC24A3 (27) vs lines expressing it (11) | the lines without SLC24A3 respond 2.93× as strongly (z diff -2.73); strongest at Dinaciclib 0.5 µM: 3.33x vs 1.21x (z diff -5.6) | 0.047 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PHYHIPL]] | B | PHYHIPL activity raises CNTNAP2's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 2.01× lower at baseline in the lines without PHYHIPL | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[SLC25A24P1]] | B | SLC25A24P1 activity raises CNTNAP2's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 2.74× lower at baseline in the lines without SLC25A24P1 | 0.056 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2 |
| [[SERPINF1]] | B | SERPINF1 activity raises CNTNAP2's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.57× lower at baseline in the lines without SERPINF1 | 0.060 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[HTR2C]] | B | HTR2C activity raises CNTNAP2's level | lines that do not express HTR2C (22) vs lines expressing it (28) | 1.99× lower at baseline in the lines without HTR2C | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, KCNJ6, PTPRN; maybe low, not absent |
| [[AMBP]] | B | AMBP activity raises CNTNAP2's level | lines that do not express AMBP (41) vs lines expressing it (9) | 1.97× lower at baseline in the lines without AMBP | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC7A8]] | B | CNTNAP2 activity raises SLC7A8's level | lines that do not express CNTNAP2 (10) vs lines expressing it (40) | 2.44× lower at baseline in the lines without CNTNAP2 | 0.032 | ⚠ within organs, on part of the lines; also absent: VENTXP1, CACNA1C, COP1-DT; maybe low, not absent |
| [[LINC00624]] | B | CNTNAP2 activity strengthens LINC00624's drug response | lines that do not express CNTNAP2 (10) vs lines expressing it (38) | the lines without CNTNAP2 respond 0.89× as strongly (z diff +1.20); strongest at Belinostat 5 µM: 2.90x vs 8.95x (z diff +3.5) | 0.086 | ⚠ within organs, on part of the lines; also absent: VENTXP1, CACNA1C, COP1-DT; maybe low, not absent; target measured in part of the lines; artifact flags |
| cells under [[Riluzole hydrochloride (drug)]] 0.05 µM | B | CNTNAP2 activity raises the cells' numbers under Riluzole hydrochloride 0.05 µM (protects the cells) | lines that do not express CNTNAP2 (10) vs lines expressing it (38) | the lines without CNTNAP2: 0.85× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: VENTXP1, CACNA1C, COP1-DT; maybe low, not absent |
| cells under [[Docetaxel (drug)]] 0.5 µM | B | CNTNAP2 activity raises the cells' numbers under Docetaxel 0.5 µM (protects the cells) | lines that do not express CNTNAP2 (10) vs lines expressing it (38) | the lines without CNTNAP2: 0.86× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: VENTXP1, CACNA1C, COP1-DT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.1, 29.8); signed map (35.0, 17.1). **Vector** length 74.9, 14.6% of its response variance represented; |z| ≥ 3 in 820 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.7 | +20.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.4 | +18.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.5 | +12.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +24.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +7.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.8 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.3 | +4.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.5 | -3.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | contactin associated protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q35-q36.1 — chr7:146,116,002-148,420,998 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Caspr2, KIAA0868, NRXN4 |
| Gene groups (HGNC) | Contactin associated protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHC6](https://www.uniprot.org/uniprotkb/Q9UHC6) (Contactin-associated protein-like 2):

> Required for gap junction formation (Probable). Required, with CNTNAP1, for radial and longitudinal organization of myelinated axons. Plays a role in the formation of functional distinct domains critical for saltatory conduction of nerve impulses in myelinated nerve fibers. Demarcates the juxtaparanodal region of the axo-glial junction.

**Summary**, from NCBI Gene [26047](https://www.ncbi.nlm.nih.gov/gene/26047):

> This gene encodes a member of the neurexin family which functions in the vertebrate nervous system as cell adhesion molecules and receptors. This protein, like other neurexin proteins, contains epidermal growth factor repeats and laminin G domains. In addition, it includes an F5/8 type C domain, discoidin/neuropilin- and fibrinogen-like domains, thrombospondin N-terminal-like domains and a putative PDZ binding site. This protein is localized at the juxtaparanodes of myelinated axons, and …

**Accessions** — [HGNC:13830](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13830) · Entrez [26047](https://www.ncbi.nlm.nih.gov/gene/26047) · UniProt [Q9UHC6](https://www.uniprot.org/uniprotkb/Q9UHC6) · Ensembl [ENSG00000174469](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174469)

## Data

Gene col 10496: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10496); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10496, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10496]; `tensor/DDL_lfc|DDL_z.npy` [10496]; `embed/gene_vectors.npy` [10496]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10496 or target_col == 10496). Every well: [[CNTNAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNTNAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
