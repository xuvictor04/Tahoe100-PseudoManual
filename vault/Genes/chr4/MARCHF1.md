---
symbol: "MARCHF1"
type: "gene"
col: 6990
ensembl_id: "ENSG00000145416"
name: "membrane associated ring-CH-type finger 1"
location: "4q32.2-q32.3"
module: 9
arm: "+"
pooled_cpm: 36.57
n_lines_expressing: 17
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 26
direction_downstream: 15
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# MARCHF1

*membrane associated ring-CH-type finger 1* — 4q32.2-q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.29× (z +15.1, q 0e+00, up in 2 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.729× (z -4.0, q 0.043, down in 5 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H460 0.206×, SHP-77 0.259×, HT-29 0.244×, SNU-423 0.366×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 0.165×, SNU-423 0.184×, SK-MEL-2 0.196×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 0.140×, NCI-H460 0.208×, J82 0.228×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NKAIN2]] (+0.75, fdr 7e-06), [[KCNJ6]] (+0.71, fdr 7e-06), [[ASXL3]] (+0.70, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[CDH7]] → it (grade C ⚠); 15 go from it, the strongest it → [[LSAMP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6990.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +15.1 | 0e+00 | 2/15 (HOP62, HS-578T) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.08×** | +13.4 | 2e-38 | 9/14 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +11.7 | 2e-29 | 11/15 (J82, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +8.9 | 5e-17 | 0/12 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +8.9 | 5e-17 | 1/10 (HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +8.5 | 1e-15 | 2/11 (NCI-H1573, SK-MEL-2) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +6.5 | 7e-09 | 1/15 (NCI-H23) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +6.4 | 1e-08 | 8/14 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.62×** | +6.2 | 3e-08 | 1/15 (J82) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.48×** | +4.9 | 7e-05 | 0/13 | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +4.6 | 2e-04 | 9/14 (CHP-212, HOP62, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 4e-04 | 0/14 | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.003 | 3/14 (SNU-423, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.36×** | +4.0 | 0.003 | 6/13 (HS-578T, SK-MEL-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.33×** | +3.5 | 0.015 | 5/13 (SK-MEL-2, SNU-423, …) | inconsistent across doses | composition shift; position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.028 | 7/14 (HOP62, HS-578T, …) | top dose only |  |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.073 | 0/14 | rises with dose | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.42×** | +3.0 | 0.073 | 0/14 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.077 | 7/14 (J82, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.25×** | +2.9 | 0.088 | 2/12 (J82, NCI-H23) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6990.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H460 0.206×, SHP-77 0.259×, HT-29 0.244×, SNU-423 0.366×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 0.165×, SNU-423 0.184×, SK-MEL-2 0.196×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 0.140×, NCI-H460 0.208×, J82 0.228×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.729×** | -4.0 | 0.043 | 5/14 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.783× | -3.2 | 0.33 | 8/14 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.791× | -3.0 | 0.33 | 0/14 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6990. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 348 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -17.1) |
| [[SNU-423 (line)]] | alt | 126 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +18.5) | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -11.2) |
| [[HT-29 (line)]] | alt | 55.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -12.3) |
| [[J82 (line)]] | alt | 38.1 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.86× (z +10.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.228× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 352 | 1 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.93× (z +11.5) ⚠ cell-cycle shift, explains ~36% of this change | [[Dinaciclib (drug)]] 5 µM 0.196× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -10.7) |
| [[H4 (line)]] | wt | 59.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 18.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.79× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +8.9) | — |
| [[NCI-H596 (line)]] | alt | 60.7 | 1 | 0 | [[Methylthiouracil (drug)]] 5 µM 8.84× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 156 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -14.0) |
| [[A-172 (line)]] | wt | 8.56 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.48 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.31 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.29 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.98 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.39 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.46 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.31 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.69 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.17 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.02 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.69 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.82 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.34 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.27 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.67 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.23 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.97 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.43 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.22 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.00 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6990), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAIN2]] | +0.75 | +0.70 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[KCNJ6]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[ASXL3]] | +0.70 | +0.49 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[RIMS1]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[NCAM2]] | +0.69 | +0.66 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[KCNH7]] | +0.67 | +0.64 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[RAB3C]] | +0.66 | +0.45 / +0.66 | both halves | 3e-05 | **novel candidate** |
| [[MSR1]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[LSAMP]] | +0.65 | +0.50 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[MIR4307HG]] | +0.65 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[TENM1]] | +0.65 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[PCDH15]] | +0.64 | +0.59 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 0, C 26. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDH7]] | C | CDH7 activity raises MARCHF1's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 3.82× lower at baseline in the lines without CDH7 | 0.011 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |
| [[RALYL]] | C | RALYL activity raises MARCHF1's level | lines that do not express RALYL (17) vs lines expressing it (33) | 2.78× lower at baseline in the lines without RALYL | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises MARCHF1's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 3.55× lower at baseline in the lines without DPP10 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[NKAIN2]] | C | NKAIN2 activity raises MARCHF1's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 3.30× lower at baseline in the lines without NKAIN2 | 0.033 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[CSRNP3]] | C | CSRNP3 activity raises MARCHF1's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 2.13× lower at baseline in the lines without CSRNP3 | 0.038 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2; co-absent with the target |
| [[WDR72]] | C | WDR72 activity raises MARCHF1's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 2.23× lower at baseline in the lines without WDR72 | 0.039 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises MARCHF1's level | lines that do not express BCHE (35) vs lines expressing it (15) | 3.07× lower at baseline in the lines without BCHE | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[LINC01885]] | C | LINC01885 activity raises MARCHF1's level | lines that do not express LINC01885 (34) vs lines expressing it (16) | 3.18× lower at baseline in the lines without LINC01885 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287598, ZNF208, LINC00383; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises MARCHF1's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 3.69× lower at baseline in the lines without KCNH5 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[LINC02506]] | C | LINC02506 activity raises MARCHF1's level | lines that do not express LINC02506 (40) vs lines expressing it (10) | 3.74× lower at baseline in the lines without LINC02506 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC01610, ENSG00000241168; co-absent with the target |
| [[VIPR2]] | C | VIPR2 activity raises MARCHF1's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 2.28× lower at baseline in the lines without VIPR2 | 0.057 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent; co-absent with the target |
| [[TENM1]] | C | TENM1 activity raises MARCHF1's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 2.63× lower at baseline in the lines without TENM1 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 1, C 14. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSAMP]] | B | MARCHF1 activity raises LSAMP's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 2.50× lower at baseline in the lines without MARCHF1 | 0.095 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent |
| [[LINC02994]] | C | MARCHF1 activity raises LINC02994's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 4.09× lower at baseline in the lines without MARCHF1 | 0.018 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent; co-absent with the target |
| [[NAA11]] | C | MARCHF1 activity raises NAA11's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 2.74× lower at baseline in the lines without MARCHF1 | 0.040 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent; co-absent with the target |
| [[TENM1]] | C | MARCHF1 activity raises TENM1's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 3.44× lower at baseline in the lines without MARCHF1 | 0.049 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent; co-absent with the target |
| [[KCNH5]] | C | MARCHF1 activity raises KCNH5's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 3.27× lower at baseline in the lines without MARCHF1 | 0.049 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent; co-absent with the target |
| [[PDE10A]] | C | MARCHF1 activity raises PDE10A's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 4.79× lower at baseline in the lines without MARCHF1 | 0.050 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent; co-absent with the target |
| [[GABRA2]] | C | MARCHF1 activity raises GABRA2's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 2.37× lower at baseline in the lines without MARCHF1 | 0.055 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent; co-absent with the target |
| [[EPHA3]] | C | MARCHF1 activity raises EPHA3's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 3.99× lower at baseline in the lines without MARCHF1 | 0.055 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent; co-absent with the target |
| [[KCNJ6]] | C | MARCHF1 activity raises KCNJ6's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 2.78× lower at baseline in the lines without MARCHF1 | 0.070 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent; co-absent with the target |
| [[LINC02484]] | C | MARCHF1 activity raises LINC02484's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 3.02× lower at baseline in the lines without MARCHF1 | 0.073 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent; co-absent with the target |
| [[LINC01035]] | C | MARCHF1 activity raises LINC01035's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 2.71× lower at baseline in the lines without MARCHF1 | 0.075 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent; co-absent with the target |
| [[ADARB2]] | C | MARCHF1 activity raises ADARB2's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 2.94× lower at baseline in the lines without MARCHF1 | 0.076 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.5, 34.2); signed map (41.8, 37.9). **Vector** length 50.0, 15.9% of its response variance represented; |z| ≥ 3 in 348 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.50 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +3.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.4 | -3.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -2.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.7 | -2.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | membrane associated ring-CH-type finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.2-q32.3 — chr4:163,524,298-164,384,050 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20668, MARCH-I, RNF171; previously MARCH1 |
| Gene groups (HGNC) | Ring finger proteins; Membrane associated ring-CH-type fingers |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCQ1](https://www.uniprot.org/uniprotkb/Q8TCQ1) (E3 ubiquitin-protein ligase MARCHF1):

> E3 ubiquitin-protein ligase that mediates ubiquitination of TFRC, CD86, FAS and MHC class II proteins, such as HLA-DR alpha and beta, and promotes their subsequent endocytosis and sorting to lysosomes via multivesicular bodies. By constitutively ubiquitinating MHC class II proteins in immature dendritic cells, down-regulates their cell surface localization thus sequestering them in the intracellular endosomal system. Also regulates insulin sensitivity by controlling surface expression of the …

**Summary**, from NCBI Gene [55016](https://www.ncbi.nlm.nih.gov/gene/55016):

> MARCH1 is a member of the MARCH family of membrane-bound E3 ubiquitin ligases (EC 6.3.2.19). MARCH proteins add ubiquitin (see MIM 191339) to target lysines in substrate proteins, thereby signaling their vesicular transport between membrane compartments. MARCH1 downregulates the surface expression of major histocompatibility complex (MHC) class II molecules (see MIM 142880) and other glycoproteins by directing them to the late endosomal/lysosomal compartment (Bartee et al., 2004 [PubMed …

**Accessions** — [HGNC:26077](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26077) · Entrez [55016](https://www.ncbi.nlm.nih.gov/gene/55016) · UniProt [Q8TCQ1](https://www.uniprot.org/uniprotkb/Q8TCQ1) · Ensembl [ENSG00000145416](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145416)

## Data

Gene col 6990: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6990); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6990, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6990]; `tensor/DDL_lfc|DDL_z.npy` [6990]; `embed/gene_vectors.npy` [6990]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6990 or target_col == 6990). Every well: [[MARCHF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARCHF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
