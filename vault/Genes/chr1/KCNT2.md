---
symbol: "KCNT2"
type: "gene"
col: 8560
ensembl_id: "ENSG00000162687"
name: "potassium sodium-activated channel subfamily T member 2"
location: "1q31.3"
module: 121
arm: "+"
pooled_cpm: 13.1
n_lines_expressing: 25
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 32
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 12
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# KCNT2

*potassium sodium-activated channel subfamily T member 2* — 1q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.20× (z +18.7, q 0e+00, up in 14 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1792 0.0651×, CHP-212 0.124×, SHP-77 0.330×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (CHP-212 0.0820×, NCI-H1792 0.195×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (CHP-212 0.129×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.318×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.115×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRP1B]] (+0.75, fdr 7e-06), [[LINC00882]] (+0.73, fdr 7e-06), [[CFH]] (+0.72, fdr 7e-06, ⚠ same locus), [[LINC02328]] (+0.70, fdr 7e-06).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → [[SLC9A9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8560.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.20×** | +18.7 | 0e+00 | 14/21 (SW 900, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.17×** | +18.5 | 0e+00 | 20/21 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.03×** | +12.1 | 3e-31 | 20/22 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +9.5 | 3e-19 | 19/23 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.18×** | +8.8 | 1e-16 | 19/22 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.08×** | +8.3 | 1e-14 | 16/21 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +7.3 | 2e-11 | 3/14 (HS-578T, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +6.6 | 3e-09 | 1/15 (hTERT-HPNE) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +6.3 | 1e-08 | 10/21 (SW 900, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.73×** | +6.2 | 3e-08 | 9/22 (SK-MEL-2, A498, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.1 | 7e-08 | 9/22 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.8 | 3e-07 | 11/23 (HOP62, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +5.8 | 3e-07 | 6/20 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.63×** | +5.6 | 1e-06 | 15/22 (NCI-H460, J82, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +4.5 | 2e-04 | 16/22 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.001 | 8/22 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.46×** | +3.9 | 0.003 | 1/22 (HOP62) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.003 | 16/22 (NCI-H23, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8560.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1792 0.0651×, CHP-212 0.124×, SHP-77 0.330×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (CHP-212 0.0820×, NCI-H1792 0.195×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (CHP-212 0.129×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.318×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.115×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.726× | -3.6 | 0.10 | 9/22 (HS-578T, CFPAC-1, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.731× | -3.6 | 0.10 | 9/22 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.742× | -3.3 | 0.20 | 4/23 (CFPAC-1, A549, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.821× | -3.2 | 0.20 | 6/22 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.764× | -3.1 | 0.21 | 3/22 (NCI-H1573, SHP-77, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.765× | -3.1 | 0.21 | 13/22 (CFPAC-1, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8560. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 41.6 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +18.1) | — |
| [[HOP62 (line)]] | alt | 16.9 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 23.4× (z +23.7) | — |
| [[A-172 (line)]] | wt | 49.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.83× (z +19.4) | — |
| [[CHP-212 (line)]] | wt | 288 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0820× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 36.8 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 5.59× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.0651× (z -14.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 36.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +20.3) | — |
| [[NCI-H460 (line)]] | wt | 8.51 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +12.1) | — |
| [[A-427 (line)]] | wt | 15.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -10.1) |
| [[A549 (line)]] | wt | 9.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.79× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 29.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.70× (z +13.5) | — |
| [[Panc 03.27 (line)]] | alt | 6.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.00× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 8.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.25× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -9.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 3.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 54.1× (z +10.4) | — |
| [[A498 (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.88 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.58 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8560), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRP1B]] | +0.75 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[LINC00882]] | +0.73 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[CFH]] | +0.72 | +0.67 / +0.65 | both halves | 7e-06 | ⚠ same locus (42.5 kb: neighbours can correlate without regulation) |
| [[LINC02328]] | +0.70 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[SYNPO2]] | +0.70 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[ADAMTS3]] | +0.69 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[HDX]] | +0.65 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[L3MBTL4]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 | same gene group |
| [[LINC02605]] | +0.64 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[EPHA5]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[CSF1]] | +0.63 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[OLR1]] | +0.63 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[SPAG17]] | +0.63 | +0.60 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KCNT2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.0% of all compounds | 0.009 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MAPK10]] | B | MAPK10 activity raises KCNT2's level | lines that do not express MAPK10 (11) vs lines expressing it (39) | 3.51× lower at baseline in the lines without MAPK10 | 0.061 | ⚠ within organs, on part of the lines; also absent: PTPN13, HDGFL3, EML1; maybe low, not absent |
| [[LINC02328]] | B | LINC02328 activity raises KCNT2's level | lines that do not express LINC02328 (14) vs lines expressing it (36) | 2.23× lower at baseline in the lines without LINC02328 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, PDE4B; maybe low, not absent |
| [[PEX5L]] | C | PEX5L activity raises KCNT2's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.75× lower at baseline in the lines without PEX5L | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |
| [[HOXD3]] | C | HOXD3 activity raises KCNT2's level | lines that do not express HOXD3 (17) vs lines expressing it (33) | 3.04× lower at baseline in the lines without HOXD3 | 0.024 | ⚠ within organs, on part of the lines; also absent: PPFIA2, SCN8A, FGF14; co-absent with the target |
| [[DMRTA1]] | C | DMRTA1 activity raises KCNT2's level | lines that do not express DMRTA1 (19) vs lines expressing it (31) | 3.03× lower at baseline in the lines without DMRTA1 | 0.026 | ⚠ within organs, on part of the lines; also absent: LINC01239, CFAP20DC, NALCN; co-absent with the target |
| [[RORB]] | C | RORB activity raises KCNT2's level | lines that do not express RORB (27) vs lines expressing it (23) | 4.16× lower at baseline in the lines without RORB | 0.036 | ⚠ within organs, on part of the lines; also absent: JAM2, NEGR1, PTPRN; maybe low, not absent; co-absent with the target |
| [[CDH12]] | C | CDH12 activity raises KCNT2's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 3.15× lower at baseline in the lines without CDH12 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[NEGR1]] | C | NEGR1 activity raises KCNT2's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 3.45× lower at baseline in the lines without NEGR1 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[PTN]] | C | PTN activity raises KCNT2's level | lines that do not express PTN (28) vs lines expressing it (22) | 2.46× lower at baseline in the lines without PTN | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC; co-absent with the target |
| [[CCDC169]] | C | CCDC169 activity raises KCNT2's level | lines that do not express CCDC169 (17) vs lines expressing it (33) | 3.93× lower at baseline in the lines without CCDC169 | 0.096 | ⚠ within organs, on part of the lines; also absent: SPART-AS1, SPART, FIGN; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 4, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC9A9]] | B | KCNT2 activity raises SLC9A9's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 2.47× lower at baseline in the lines without KCNT2 | 0.003 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1 |
| [[CTNNA3]] | B | KCNT2 activity lowers CTNNA3's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 1.82× higher at baseline in the lines without KCNT2 | 0.085 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1 |
| [[OR51B5]] | B | KCNT2 activity raises OR51B5's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 1.93× lower at baseline in the lines without KCNT2 | 0.089 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1 |
| [[DIO2]] | B | KCNT2 activity raises DIO2's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 2.49× lower at baseline in the lines without KCNT2 | 0.094 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1 |
| [[CFH]] | C | KCNT2 activity raises CFH's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 4.52× lower at baseline in the lines without KCNT2 | 0.042 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1; co-absent with the target |
| [[PTN]] | C | KCNT2 activity raises PTN's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 2.90× lower at baseline in the lines without KCNT2 | 0.064 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1; co-absent with the target |
| [[MIR3171HG]] | C | KCNT2 activity raises MIR3171HG's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 4.05× lower at baseline in the lines without KCNT2 | 0.069 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1; co-absent with the target |
| [[TRIM58]] | C | KCNT2 activity raises TRIM58's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 1.41× lower at baseline in the lines without KCNT2 | 0.076 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1; co-absent with the target |
| [[FLRT2]] | C | KCNT2 activity raises FLRT2's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 4.27× lower at baseline in the lines without KCNT2 | 0.083 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1; co-absent with the target |
| [[HECW2]] | C | KCNT2 activity raises HECW2's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 3.82× lower at baseline in the lines without KCNT2 | 0.093 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1; co-absent with the target |
| [[CDH18]] | C | KCNT2 activity raises CDH18's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 1.80× lower at baseline in the lines without KCNT2 | 0.098 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1; co-absent with the target |
| [[PEX5L]] | C | KCNT2 activity raises PEX5L's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 2.53× lower at baseline in the lines without KCNT2 | 0.099 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.8, 24.0); signed map (46.2, 25.0). **Vector** length 80.8, 24.7% of its response variance represented; |z| ≥ 3 in 665 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +18.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +18.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +3.1 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | +0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.5 | -1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +0.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -0.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | potassium sodium-activated channel subfamily T member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q31.3 — chr1:196,225,779-196,609,225 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KCa4.2, SLICK, SLO2.1 |
| Gene groups (HGNC) | Potassium sodium-activated channel subfamily T ; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UVM3](https://www.uniprot.org/uniprotkb/Q6UVM3) (Potassium channel subfamily T member 2):

> Sodium-activated and chloride-activated potassium channel. Produces rapidly activating outward rectifier K(+) currents. Contributes to regulate neuronal excitability.

**Summary**, from NCBI Gene [343450](https://www.ncbi.nlm.nih.gov/gene/343450):

> Enables chloride-activated potassium channel activity and intracellular sodium-activated potassium channel activity. Involved in potassium ion export across plasma membrane. Located in plasma membrane. Implicated in developmental and epileptic encephalopathy 57. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18866) · Entrez [343450](https://www.ncbi.nlm.nih.gov/gene/343450) · UniProt [Q6UVM3](https://www.uniprot.org/uniprotkb/Q6UVM3) · Ensembl [ENSG00000162687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162687)

## Data

Gene col 8560: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8560); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8560, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8560]; `tensor/DDL_lfc|DDL_z.npy` [8560]; `embed/gene_vectors.npy` [8560]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8560 or target_col == 8560). Every well: [[KCNT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
