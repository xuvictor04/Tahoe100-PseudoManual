---
symbol: "SCIN"
type: "gene"
col: 129
ensembl_id: "ENSG00000006747"
name: "scinderin"
location: "7p21.3"
module: 8
arm: "+"
pooled_cpm: 5.17
n_lines_expressing: 28
n_dd_up: 46
n_dd_down: 0
n_dd_up_clean: 39
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 34
direction_downstream: 31
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SCIN

*scinderin* — 7p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.14× (z +24.2, q 0e+00, up in 19 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.436×); [[Auranofin (drug)]] 5 µM in 1 line (HT-29 0.177×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SELENOP]] (+0.72, fdr 7e-06), [[RASGEF1B]] (+0.71, fdr 7e-06), [[STEAP4]] (+0.65, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 34 arrows point to it, the strongest [[ALOX5]] → it (grade B ⚠); 31 go from it, the strongest it → [[PKIB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 129.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.14×** | +24.2 | 0e+00 | 19/20 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **4.67×** | +20.6 | 0e+00 | 22/24 (LoVo, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.32×** | +13.8 | 2e-41 | 8/13 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.35×** | +13.4 | 1e-38 | 3/5 (HEC-1-A, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.54×** | +13.2 | 5e-38 | 4/7 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.49×** | +11.8 | 3e-30 | 19/23 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.27×** | +11.0 | 4e-26 | 10/24 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.44×** | +8.4 | 2e-15 | 16/24 (A-427, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +8.2 | 2e-14 | 8/21 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.30×** | +7.9 | 2e-13 | 16/24 (KATO III, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.22×** | +7.5 | 3e-12 | 14/23 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +7.4 | 7e-12 | 7/18 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +7.2 | 3e-11 | 9/19 (HEC-1-A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +6.4 | 6e-09 | 15/23 (A-427, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.85×** | +5.8 | 3e-07 | 5/23 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.71×** | +5.1 | 1e-05 | 10/24 (HT-29, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.67×** | +4.6 | 1e-04 | 13/21 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +4.6 | 1e-04 | 10/20 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 129.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.436×); [[Auranofin (drug)]] 5 µM in 1 line (HT-29 0.177×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dabrafenib (drug)]] 5 µM |  | 0.518× | -3.3 | 0.61 | 3/24 (SHP-77, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.728× | -3.0 | 0.63 | 6/22 (HT-29, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 129. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 4.72 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +12.8) | — |
| [[A-427 (line)]] | wt | 1.58 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 57.3× (z +8.6) | — |
| [[A498 (line)]] | wt | 1.64 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.6× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 9.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.52× (z +13.9) | — |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.177× (z -8.7) |
| [[KATO III (line)]] | alt | 8.78 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.47× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 2.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.9× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 57.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -9.3) |
| [[SW1417 (line)]] | alt | 2.18 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 14.3× (z +9.0) | — |
| [[A-172 (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.852 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.580 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.890 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.651 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.790 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.650 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.714 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.831 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.528 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.578 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.723 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 129), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOP]] | +0.72 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[RASGEF1B]] | +0.71 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[STEAP4]] | +0.65 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[BCL2L15]] | +0.64 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[MMP7]] | +0.63 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SYNPR-AS1]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[HHLA2]] | +0.59 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[CRACDL]] | +0.59 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[FMO5]] | +0.59 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[SLC40A1]] | +0.58 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[TRIM31]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[SLC34A2]] | +0.58 | +0.45 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 20, C 14. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALOX5]] | B | ALOX5 activity raises SCIN's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 2.33× lower at baseline in the lines without ALOX5 | 0.005 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[LRG1]] | B | LRG1 activity raises SCIN's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 2.35× lower at baseline in the lines without LRG1 | 0.011 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |
| [[SLC40A1]] | B | SLC40A1 activity raises SCIN's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.34× lower at baseline in the lines without SLC40A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[TOP2A]] | B | TOP2A activity lowers SCIN's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 8.7% of all compounds | 0.015 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[SH3BGRL2]] | B | SH3BGRL2 activity raises SCIN's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 2.30× lower at baseline in the lines without SH3BGRL2 | 0.023 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[CGN]] | B | CGN activity raises SCIN's level | lines that do not express CGN (21) vs lines expressing it (29) | 2.15× lower at baseline in the lines without CGN | 0.037 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[ARSL]] | B | ARSL activity raises SCIN's level | lines that do not express ARSL (26) vs lines expressing it (24) | 1.87× lower at baseline in the lines without ARSL | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4 |
| [[C11orf52]] | B | C11orf52 activity raises SCIN's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 1.99× lower at baseline in the lines without C11orf52 | 0.039 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[LNX1]] | B | LNX1 activity raises SCIN's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 1.88× lower at baseline in the lines without LNX1 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[CRACDL]] | B | CRACDL activity raises SCIN's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 2.13× lower at baseline in the lines without CRACDL | 0.049 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[RAB17]] | B | RAB17 activity raises SCIN's level | lines that do not express RAB17 (22) vs lines expressing it (28) | 1.96× lower at baseline in the lines without RAB17 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MAL2, TNNT2, BSPRY |
| [[NR3C2]] | B | NR3C2 activity raises SCIN's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.73× lower at baseline in the lines without NR3C2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 21, C 10. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKIB]] | B | SCIN activity raises PKIB's level | lines that do not express SCIN (22) vs lines expressing it (28) | 2.34× lower at baseline in the lines without SCIN | 0.013 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[KITLG]] | B | SCIN activity raises KITLG's level | lines that do not express SCIN (22) vs lines expressing it (28) | 2.11× lower at baseline in the lines without SCIN | 0.013 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[RAB17]] | B | SCIN activity raises RAB17's level | lines that do not express SCIN (22) vs lines expressing it (28) | 1.98× lower at baseline in the lines without SCIN | 0.019 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[SELENOP]] | B | SCIN activity raises SELENOP's level | lines that do not express SCIN (22) vs lines expressing it (28) | 1.42× lower at baseline in the lines without SCIN | 0.021 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[ATP8B1]] | B | SCIN activity raises ATP8B1's level | lines that do not express SCIN (22) vs lines expressing it (28) | 2.23× lower at baseline in the lines without SCIN | 0.028 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[SH3BGRL2]] | B | SCIN activity raises SH3BGRL2's level | lines that do not express SCIN (22) vs lines expressing it (28) | 1.87× lower at baseline in the lines without SCIN | 0.029 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[CGN]] | B | SCIN activity raises CGN's level | lines that do not express SCIN (22) vs lines expressing it (28) | 3.22× lower at baseline in the lines without SCIN | 0.037 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[LINC00578]] | B | SCIN activity raises LINC00578's level | lines that do not express SCIN (22) vs lines expressing it (28) | 1.65× lower at baseline in the lines without SCIN | 0.043 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[RASGEF1B]] | B | SCIN activity raises RASGEF1B's level | lines that do not express SCIN (22) vs lines expressing it (28) | 1.98× lower at baseline in the lines without SCIN | 0.046 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[ALOX5]] | B | SCIN activity raises ALOX5's level | lines that do not express SCIN (22) vs lines expressing it (28) | 2.16× lower at baseline in the lines without SCIN | 0.056 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[TSPAN12]] | B | SCIN activity raises TSPAN12's level | lines that do not express SCIN (22) vs lines expressing it (28) | 2.18× lower at baseline in the lines without SCIN | 0.057 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[DPP4]] | B | SCIN activity raises DPP4's level | lines that do not express SCIN (22) vs lines expressing it (28) | 2.24× lower at baseline in the lines without SCIN | 0.058 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.584). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.6, 52.5); signed map (54.1, 0.9). **Vector** length 57.4, 13.0% of its response variance represented; |z| ≥ 3 in 712 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +20.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +13.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +11.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +4.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | +0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -0.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -0.0 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.4 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | scinderin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.3 — chr7:12,570,577-12,660,182 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1905 |
| Gene groups (HGNC) | Gelsolin/villins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6U3](https://www.uniprot.org/uniprotkb/Q9Y6U3) (Scinderin):

> Ca(2+)-dependent actin filament-severing protein that has a regulatory function in exocytosis by affecting the organization of the microfilament network underneath the plasma membrane. Severing activity is inhibited by phosphatidylinositol 4,5-bis-phosphate (PIP2) (By similarity). In vitro, also has barbed end capping and nucleating activities in the presence of Ca(2+). Required for megakaryocyte differentiation, maturation, polyploidization and apoptosis with the release of platelet-like …

**Summary**, from NCBI Gene [85477](https://www.ncbi.nlm.nih.gov/gene/85477):

> SCIN is a Ca(2+)-dependent actin-severing and -capping protein (Zunino et al., 2001 [PubMed 11568009]).[supplied by OMIM, May 2010]

**Accessions** — [HGNC:21695](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21695) · Entrez [85477](https://www.ncbi.nlm.nih.gov/gene/85477) · UniProt [Q9Y6U3](https://www.uniprot.org/uniprotkb/Q9Y6U3) · Ensembl [ENSG00000006747](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006747)

## Data

Gene col 129: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 129); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 129, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 129]; `tensor/DDL_lfc|DDL_z.npy` [129]; `embed/gene_vectors.npy` [129]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 129 or target_col == 129). Every well: [[SCIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
