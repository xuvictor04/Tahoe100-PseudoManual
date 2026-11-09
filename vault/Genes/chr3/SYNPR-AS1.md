---
symbol: "SYNPR-AS1"
type: "gene"
col: 14269
ensembl_id: "ENSG00000241359"
name: "SYNPR antisense RNA 1"
location: "3p14.2"
module: 8
arm: "+"
pooled_cpm: 2.06
n_lines_expressing: 17
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 59
direction_downstream: 70
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SYNPR-AS1

*SYNPR antisense RNA 1* — 3p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.67× (z +11.9, q 4e-30, up in 1 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (Panc 03.27 0.0225×, HT-29 0.0894×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW1417 0.112×, HT-29 0.204×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.0565×, SW1417 0.116×; ⚠ toxic); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Panc 03.27 0.0890×, LS 180 0.119×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCAS1]] (+0.77, fdr 7e-06), [[GABRP]] (+0.72, fdr 7e-06), [[BCL2L15]] (+0.69, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 59 arrows point to it, the strongest [[LNX1]] → it (grade B ⚠); 70 go from it, the strongest it → [[RAPGEF5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14269.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.67×** | +11.9 | 4e-30 | 1/13 (NCI-H460) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.18×** | +11.4 | 2e-27 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.55×** | +9.8 | 1e-20 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.42×** | +8.9 | 6e-17 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.36×** | +7.9 | 5e-13 | 10/14 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +5.0 | 6e-05 | 0/12 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.15×** | +5.0 | 6e-05 | 8/12 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.89×** | +4.9 | 6e-05 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +4.8 | 9e-05 | 1/14 (BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +4.2 | 0.001 | 1/10 (AsPC-1) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +4.2 | 0.001 | 3/15 (LS 180, BT-474, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.37×** | +4.0 | 0.003 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.82×** | +3.9 | 0.005 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.8 | 0.006 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.76×** | +3.7 | 0.010 | 10/15 (KATO III, LS 180, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.57×** | +3.5 | 0.016 | 5/13 (J82, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.69×** | +3.4 | 0.020 | 0/10 | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.68×** | +3.4 | 0.021 | 7/13 (KATO III, Panc 03.27, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.45×** | +3.3 | 0.024 | 6/15 (SW1417, NCI-H460, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.66×** | +3.3 | 0.025 | 0/14 | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.65×** | +3.2 | 0.031 | 3/15 (SW1417, HCT15, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.58×** | +3.0 | 0.069 | 0/9 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14269.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (Panc 03.27 0.0225×, HT-29 0.0894×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW1417 0.112×, HT-29 0.204×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.0565×, SW1417 0.116×; ⚠ toxic); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Panc 03.27 0.0890×, LS 180 0.119×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | 0.601× | -3.1 | 0.73 | 2/15 (NCI-H460, J82) | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.631× | -3.0 | 0.73 | 3/15 (COLO 205, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14269. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 17.7 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0206× (z -14.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0225× (z -14.5) |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0406× (z -12.9) |
| [[SW1417 (line)]] | alt | 14.7 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -13.1) |
| [[LS 180 (line)]] | wt | 15.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -8.5) |
| [[A-172 (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.241 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.268 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.290 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.242 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.876 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.325 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.216 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.690 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.281 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.687 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.284 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.417 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14269), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAS1]] | +0.77 | +0.68 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[GABRP]] | +0.72 | +0.71 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[BCL2L15]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[SAMD12]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[CLIC5]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[CRACDL]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PROM1]] | +0.65 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[SAMD12-AS1]] | +0.64 | +0.67 / +0.62 | both halves | 7e-06 | same gene group |
| [[MGAM2]] | +0.64 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[TJP3]] | +0.64 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[SLC40A1]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[LINC00992]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*59 arrows, 59 of them with an alert ⚠; grade A 0, B 7, C 52. Shown: the 12 strongest; 47 more arrows (47 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LNX1]] | B | LNX1 activity raises SYNPR-AS1's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 1.70× lower at baseline in the lines without LNX1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[MPP7]] | B | MPP7 activity raises SYNPR-AS1's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 1.82× lower at baseline in the lines without MPP7 | 0.055 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[RAPGEF5]] | B | RAPGEF5 activity raises SYNPR-AS1's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 1.86× lower at baseline in the lines without RAPGEF5 | 0.069 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises SYNPR-AS1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 1.86× lower at baseline in the lines without ELF3-AS1 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[SPATA6L]] | B | SPATA6L activity raises SYNPR-AS1's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 1.84× lower at baseline in the lines without SPATA6L | 0.094 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[C4orf19]] | B | C4orf19 activity raises SYNPR-AS1's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 1.71× lower at baseline in the lines without C4orf19 | 0.094 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[POU5F1B]] | B | POU5F1B activity raises SYNPR-AS1's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 1.78× lower at baseline in the lines without POU5F1B | 0.096 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[ADGRF1]] | C | ADGRF1 activity raises SYNPR-AS1's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 2.95× lower at baseline in the lines without ADGRF1 | 0.002 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[ALOX5]] | C | ALOX5 activity raises SYNPR-AS1's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 2.33× lower at baseline in the lines without ALOX5 | 0.004 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6; co-absent with the target |
| [[C11orf52]] | C | C11orf52 activity raises SYNPR-AS1's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 2.20× lower at baseline in the lines without C11orf52 | 0.004 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39; co-absent with the target |
| [[RNF39]] | C | RNF39 activity raises SYNPR-AS1's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 2.61× lower at baseline in the lines without RNF39 | 0.005 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises SYNPR-AS1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.93× lower at baseline in the lines without TMPRSS2 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |

### Downstream of this gene

*70 arrows, 70 of them with an alert ⚠; grade A 0, B 18, C 52. Shown: the 12 strongest; 58 more arrows (58 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAPGEF5]] | B | SYNPR-AS1 activity raises RAPGEF5's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 3.72× lower at baseline in the lines without SYNPR-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |
| [[LNX1]] | B | SYNPR-AS1 activity raises LNX1's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 3.92× lower at baseline in the lines without SYNPR-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |
| [[ELF3-AS1]] | B | SYNPR-AS1 activity raises ELF3-AS1's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 3.18× lower at baseline in the lines without SYNPR-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |
| [[CARD14]] | B | SYNPR-AS1 activity raises CARD14's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 1.95× lower at baseline in the lines without SYNPR-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |
| [[SELENOP]] | B | SYNPR-AS1 activity raises SELENOP's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 1.96× lower at baseline in the lines without SYNPR-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |
| [[FMO5]] | B | SYNPR-AS1 activity raises FMO5's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 1.60× lower at baseline in the lines without SYNPR-AS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |
| [[MUC20]] | B | SYNPR-AS1 activity raises MUC20's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 3.19× lower at baseline in the lines without SYNPR-AS1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |
| [[MTUS1]] | B | SYNPR-AS1 activity raises MTUS1's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 3.38× lower at baseline in the lines without SYNPR-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |
| [[MANSC1]] | B | SYNPR-AS1 activity raises MANSC1's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 2.43× lower at baseline in the lines without SYNPR-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |
| [[SH3BGRL2]] | B | SYNPR-AS1 activity raises SH3BGRL2's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 2.78× lower at baseline in the lines without SYNPR-AS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |
| [[C4orf19]] | B | SYNPR-AS1 activity raises C4orf19's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 2.74× lower at baseline in the lines without SYNPR-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |
| [[SLC44A3]] | B | SYNPR-AS1 activity raises SLC44A3's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 2.22× lower at baseline in the lines without SYNPR-AS1 | 0.036 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.4, 52.5); signed map (60.8, 1.7). **Vector** length 44.4, 13.3% of its response variance represented; |z| ≥ 3 in 395 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.8 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.2 | +9.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +3.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -1.1 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.8 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.8 | -2.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.7 | -1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -0.6 | +1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.5 | -1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.5 | +0.0 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | SYNPR antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p14.2 — chr3:63,423,596-63,550,051 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LncFASA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40774](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40774) · Entrez [100874016](https://www.ncbi.nlm.nih.gov/gene/100874016) · Ensembl [ENSG00000241359](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241359)

## Data

Gene col 14269: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14269); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14269, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14269]; `tensor/DDL_lfc|DDL_z.npy` [14269]; `embed/gene_vectors.npy` [14269]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14269 or target_col == 14269). Every well: [[SYNPR-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNPR-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
