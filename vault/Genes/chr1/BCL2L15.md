---
symbol: "BCL2L15"
type: "gene"
col: 12047
ensembl_id: "ENSG00000188761"
name: "BCL2 like 15"
location: "1p13.2"
module: 8
arm: "+"
pooled_cpm: 4.36
n_lines_expressing: 30
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 132
direction_downstream: 18
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# BCL2L15

*BCL2 like 15* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.06× (z +10.7, q 5e-24, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.56× (z +6.2, q 7e-08, up in 9 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.655× (z -4.1, q 0.027, down in 8 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.0897×, KATO III 0.0552×, CFPAC-1 0.128×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (COLO 205 0.0626×, HT-29 0.102×; ⚠ cell-cycle shift, explains ~3% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (COLO 205 0.103×, HT-29 0.167×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 0.0613×, COLO 205 0.180×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC13]] (+0.80, fdr 7e-06), [[MGAM2]] (+0.80, fdr 7e-06), [[PROM1]] (+0.78, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 132 arrows point to it, the strongest [[WFDC2]] → it (grade B ⚠); 18 go from it, the strongest it → [[RAMP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12047.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.06×** | +10.7 | 5e-24 | 2/5 (SW480, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +9.8 | 5e-20 | 4/12 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +8.0 | 2e-13 | 3/8 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +6.2 | 7e-08 | 9/25 (LoVo, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.5 | 5e-06 | 4/18 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +5.2 | 2e-05 | 3/21 (RKO, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +4.3 | 0.002 | 1/19 (LoVo) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +4.2 | 0.002 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +4.1 | 0.003 | 13/19 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.0 | 0.004 | 1/10 (LS 180) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.005 | 5/25 (SW1417, LS 180, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.05×** | +3.7 | 0.009 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +3.7 | 0.010 | 8/20 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.019 | 11/24 (AsPC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.63×** | +3.5 | 0.019 | 1/10 (SW1417) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.019 | 11/25 (HT-29, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +3.3 | 0.028 | 10/25 (HT-29, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.047 | 11/25 (CFPAC-1, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12047.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.0897×, KATO III 0.0552×, CFPAC-1 0.128×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (COLO 205 0.0626×, HT-29 0.102×; ⚠ cell-cycle shift, explains ~3% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (COLO 205 0.103×, HT-29 0.167×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 0.0613×, COLO 205 0.180×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.655×** | -4.1 | 0.027 | 8/22 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.784× | -3.4 | 0.16 | 10/23 (CFPAC-1, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.717× | -3.3 | 0.17 | 5/24 (KATO III, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12047. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 53.4 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0897× (z -20.6) |
| [[KATO III (line)]] | alt | 16.9 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0552× (z -19.7) |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.102× (z -9.9) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.128× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -11.6) |
| [[SW480 (line)]] | alt | 12.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.19× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.252× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 5.85 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.102× (z -9.3) |
| [[A-172 (line)]] | wt | 0.892 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.883 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.940 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.813 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.749 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.922 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.883 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.943 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.909 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.940 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.744 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.921 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.866 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12047), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC13]] | +0.80 | +0.77 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[MGAM2]] | +0.80 | +0.78 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[PROM1]] | +0.78 | +0.80 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[PRR15]] | +0.77 | +0.79 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PTPN22]] | +0.77 | +0.85 / +0.69 | both halves | 7e-06 | STRING 478; ⚠ same locus (5.1 kb, same strand: neighbours can correlate without regulation) |
| [[TRIM31]] | +0.77 | +0.74 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[SAMD12-AS1]] | +0.77 | +0.76 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[HNF1A-AS1]] | +0.77 | +0.83 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[PLCH1]] | +0.77 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[POF1B]] | +0.77 | +0.79 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[BCAS1]] | +0.75 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[SLC40A1]] | +0.75 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[NPNT]] | +0.75 | +0.73 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*132 arrows, 132 of them with an alert ⚠; grade A 0, B 86, C 46. Shown: the 12 strongest; 120 more arrows (120 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WFDC2]] | B | WFDC2 activity raises BCL2L15's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 3.66× lower at baseline in the lines without WFDC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[KRT23]] | B | KRT23 activity raises BCL2L15's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 3.36× lower at baseline in the lines without KRT23 | 0.002 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[LINC02331]] | B | LINC02331 activity raises BCL2L15's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 2.99× lower at baseline in the lines without LINC02331 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2 |
| [[LYZ]] | B | LYZ activity raises BCL2L15's level | lines that do not express LYZ (40) vs lines expressing it (10) | 4.06× lower at baseline in the lines without LYZ | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17 |
| [[HLA-DRA]] | B | HLA-DRA activity raises BCL2L15's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 2.21× lower at baseline in the lines without HLA-DRA | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |
| [[FAAH2]] | B | FAAH2 activity raises BCL2L15's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.52× lower at baseline in the lines without FAAH2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[LINC01814]] | B | LINC01814 activity raises BCL2L15's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 2.87× lower at baseline in the lines without LINC01814 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3 |
| [[MMP7]] | B | MMP7 activity raises BCL2L15's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.01× lower at baseline in the lines without MMP7 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[GCNT3]] | B | GCNT3 activity raises BCL2L15's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.52× lower at baseline in the lines without GCNT3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[TOX3]] | B | TOX3 activity raises BCL2L15's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.58× lower at baseline in the lines without TOX3 | 0.008 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[STEAP4]] | B | STEAP4 activity raises BCL2L15's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 3.25× lower at baseline in the lines without STEAP4 | 0.008 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[HNF1A-AS1]] | B | HNF1A-AS1 activity raises BCL2L15's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 2.69× lower at baseline in the lines without HNF1A-AS1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 6, C 12. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAMP1]] | B | BCL2L15 activity raises RAMP1's level | lines that do not express BCL2L15 (20) vs lines expressing it (30) | 1.98× lower at baseline in the lines without BCL2L15 | 0.027 | ⚠ within organs, on part of the lines; also absent: SYK, NOS3, CASC8; maybe low, not absent |
| [[SAMD12]] | B | BCL2L15 activity raises SAMD12's level | lines that do not express BCL2L15 (20) vs lines expressing it (30) | 3.20× lower at baseline in the lines without BCL2L15 | 0.050 | ⚠ within organs, on part of the lines; also absent: SYK, NOS3, CASC8; maybe low, not absent |
| [[PRSS51]] | B | BCL2L15 activity raises PRSS51's level | lines that do not express BCL2L15 (20) vs lines expressing it (30) | 1.77× lower at baseline in the lines without BCL2L15 | 0.079 | ⚠ within organs, on part of the lines; also absent: SYK, NOS3, CASC8; maybe low, not absent |
| [[MUC16]] | B | BCL2L15 activity raises MUC16's level | lines that do not express BCL2L15 (20) vs lines expressing it (30) | 2.88× lower at baseline in the lines without BCL2L15 | 0.079 | ⚠ within organs, on part of the lines; also absent: SYK, NOS3, CASC8; maybe low, not absent |
| [[PLAAT4]] | B | BCL2L15 activity raises PLAAT4's level | lines that do not express BCL2L15 (20) vs lines expressing it (30) | 1.73× lower at baseline in the lines without BCL2L15 | 0.082 | ⚠ within organs, on part of the lines; also absent: SYK, NOS3, CASC8; maybe low, not absent |
| [[MUC4]] | B | BCL2L15 activity raises MUC4's level | lines that do not express BCL2L15 (20) vs lines expressing it (30) | 2.61× lower at baseline in the lines without BCL2L15 | 0.084 | ⚠ within organs, on part of the lines; also absent: SYK, NOS3, CASC8; maybe low, not absent |
| [[SLC44A3]] | C | BCL2L15 activity raises SLC44A3's level | lines that do not express BCL2L15 (20) vs lines expressing it (30) | 2.75× lower at baseline in the lines without BCL2L15 | 0.006 | ⚠ within organs, on part of the lines; also absent: SYK, NOS3, CASC8; maybe low, not absent; co-absent with the target |
| [[SLC44A3-AS1]] | C | BCL2L15 activity raises SLC44A3-AS1's level | lines that do not express BCL2L15 (20) vs lines expressing it (30) | 2.89× lower at baseline in the lines without BCL2L15 | 0.007 | ⚠ within organs, on part of the lines; also absent: SYK, NOS3, CASC8; maybe low, not absent; co-absent with the target |
| [[ABO]] | C | BCL2L15 activity raises ABO's level | lines that do not express BCL2L15 (20) vs lines expressing it (30) | 3.64× lower at baseline in the lines without BCL2L15 | 0.034 | ⚠ within organs, on part of the lines; also absent: SYK, NOS3, CASC8; maybe low, not absent; co-absent with the target |
| [[TNFSF15]] | C | BCL2L15 activity raises TNFSF15's level | lines that do not express BCL2L15 (20) vs lines expressing it (30) | 3.40× lower at baseline in the lines without BCL2L15 | 0.044 | ⚠ within organs, on part of the lines; also absent: SYK, NOS3, CASC8; maybe low, not absent; co-absent with the target |
| [[TTC22]] | C | BCL2L15 activity raises TTC22's level | lines that do not express BCL2L15 (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without BCL2L15 | 0.052 | ⚠ within organs, on part of the lines; also absent: SYK, NOS3, CASC8; maybe low, not absent; co-absent with the target |
| [[CGN]] | C | BCL2L15 activity raises CGN's level | lines that do not express BCL2L15 (20) vs lines expressing it (30) | 3.76× lower at baseline in the lines without BCL2L15 | 0.060 | ⚠ within organs, on part of the lines; also absent: SYK, NOS3, CASC8; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.834). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.3, 52.6); signed map (60.2, 2.1). **Vector** length 66.6, 17.8% of its response variance represented; |z| ≥ 3 in 701 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.58 to 5); *O-linked glycosylation of mucins* (reactome, mean cos +0.53 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +10.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -1.3 | +2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -0.9 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 like 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:113,876,816-113,887,581 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Bfk, FLJ22588; previously C1orf178 |
| Gene groups (HGNC) | BCL2 family |
| Matched by | ensembl_id |

UniProt [Q5TBC7](https://www.uniprot.org/uniprotkb/Q5TBC7) carries no function annotation.

**Summary**, from NCBI Gene [440603](https://www.ncbi.nlm.nih.gov/gene/440603):

> Predicted to be involved in apoptotic process and regulation of apoptotic process. Predicted to be active in cytosol and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33624](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33624) · Entrez [440603](https://www.ncbi.nlm.nih.gov/gene/440603) · UniProt [Q5TBC7](https://www.uniprot.org/uniprotkb/Q5TBC7) · Ensembl [ENSG00000188761](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188761)

## Data

Gene col 12047: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12047); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12047, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12047]; `tensor/DDL_lfc|DDL_z.npy` [12047]; `embed/gene_vectors.npy` [12047]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12047 or target_col == 12047). Every well: [[BCL2L15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL2L15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
