---
symbol: "CHST8"
type: "gene"
col: 4517
ensembl_id: "ENSG00000124302"
name: "carbohydrate sulfotransferase 8"
location: "19q13.11"
module: 61
arm: "+"
pooled_cpm: 8.19
n_lines_expressing: 21
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 14
direction_downstream: 3
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# CHST8

*carbohydrate sulfotransferase 8* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.40× (z +25.1, q 0e+00, up in 11 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.637× (z -4.0, q 0.030, down in 2 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.127×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.150×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.157×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (SHP-77 0.318×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.222×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RET]] (+0.66, fdr 7e-06), [[ELAVL2]] (+0.65, fdr 1e-05), [[PCSK2]] (+0.64, fdr 7e-06); moves opposite to [[SLC15A5]] (-0.47, fdr 3e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[PDLIM3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4517.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.40×** | +25.1 | 0e+00 | 11/14 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.95×** | +21.6 | 0e+00 | 9/14 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.68×** | +12.4 | 3e-33 | 16/18 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.49×** | +11.9 | 1e-30 | 16/18 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.01×** | +11.8 | 5e-30 | 2/5 (A-427, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.23×** | +11.2 | 6e-27 | 6/11 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.12×** | +10.1 | 5e-22 | 13/16 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.72×** | +9.5 | 1e-19 | 5/11 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.50×** | +8.7 | 2e-16 | 11/18 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.29×** | +7.9 | 2e-13 | 16/18 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +7.7 | 6e-13 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +7.4 | 7e-12 | 6/13 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.3 | 1e-08 | 8/19 (BT-474, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +5.4 | 2e-06 | 8/17 (SW480, C-33 A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +5.3 | 4e-06 | 9/15 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.6 | 2e-04 | 6/14 (NCI-H460, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.58×** | +4.3 | 4e-04 | 6/16 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +3.9 | 0.003 | 6/16 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.008 | 7/16 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4517.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.127×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.150×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.157×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (SHP-77 0.318×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.222×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.637×** | -4.0 | 0.030 | 2/17 (H4, HOP62) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.658×** | -3.8 | 0.049 | 2/18 (NCI-H460, SW480) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4517. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.64 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.0× (z +16.4) | — |
| [[HOP62 (line)]] | alt | 6.95 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 50.2× (z +21.8) | — |
| [[NCI-H2030 (line)]] | alt | 31.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.38× (z +17.1) | [[Digitoxin (drug)]] 5 µM 0.158× (z -10.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 216 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.157× (z -12.6) |
| [[A549 (line)]] | wt | 3.03 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 30.1× (z +14.0) | — |
| [[A-427 (line)]] | wt | 49.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.222× (z -10.5) |
| [[BT-474 (line)]] | alt | 19.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.55× (z +13.6) | — |
| [[C-33 A (line)]] | alt | 20.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 2.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 47.5× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 5.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +12.0) | — |
| [[A-172 (line)]] | wt | 0.821 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.932 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.895 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.817 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.996 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.782 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.830 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.896 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.983 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.881 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4517), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RET]] | +0.66 | +0.58 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[ELAVL2]] | +0.65 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[PCSK2]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[SLC6A17]] | +0.61 | +0.52 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[RFPL1S]] | +0.60 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[CELF4]] | +0.59 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[RGS7]] | +0.58 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[GRIA2]] | +0.58 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[UNC80]] | +0.58 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[SH3GL2]] | +0.58 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[NPTX2]] | +0.57 | +0.67 / +0.40 | both halves | 5e-05 |  |
| [[FMN2]] | +0.57 | +0.50 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC15A5]] | -0.47 | -0.50 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 1, C 13. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CHST8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02197]] | C | LINC02197 activity raises CHST8's level | lines that do not express LINC02197 (35) vs lines expressing it (15) | 2.99× lower at baseline in the lines without LINC02197 | 0.032 | ⚠ within organs, on part of the lines; also absent: RIT2, SNTG1, CALCA; maybe low, not absent; co-absent with the target |
| [[FREM2]] | C | FREM2 activity raises CHST8's level | lines that do not express FREM2 (26) vs lines expressing it (24) | 2.52× lower at baseline in the lines without FREM2 | 0.040 | ⚠ within organs, on part of the lines; also absent: NELL2, ANKRD20A11P, KCNH7; maybe low, not absent; co-absent with the target |
| [[GABRA2]] | C | GABRA2 activity raises CHST8's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 2.34× lower at baseline in the lines without GABRA2 | 0.045 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent; co-absent with the target |
| [[LRFN2]] | C | LRFN2 activity raises CHST8's level | lines that do not express LRFN2 (35) vs lines expressing it (15) | 4.29× lower at baseline in the lines without LRFN2 | 0.070 | ⚠ within organs, on part of the lines; also absent: MAGEA4, CALCA, PI15; maybe low, not absent; co-absent with the target |
| [[MED12L]] | C | MED12L activity raises CHST8's level | lines that do not express MED12L (18) vs lines expressing it (32) | 2.80× lower at baseline in the lines without MED12L | 0.073 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2; co-absent with the target |
| [[RET]] | C | RET activity raises CHST8's level | lines that do not express RET (28) vs lines expressing it (22) | 3.57× lower at baseline in the lines without RET | 0.080 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1; co-absent with the target |
| [[JAKMIP1]] | C | JAKMIP1 activity raises CHST8's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 3.96× lower at baseline in the lines without JAKMIP1 | 0.080 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2; co-absent with the target |
| [[SLITRK6]] | C | SLITRK6 activity raises CHST8's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 2.56× lower at baseline in the lines without SLITRK6 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises CHST8's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 3.59× lower at baseline in the lines without KCNH7 | 0.085 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[SNAP91]] | C | SNAP91 activity raises CHST8's level | lines that do not express SNAP91 (26) vs lines expressing it (24) | 3.43× lower at baseline in the lines without SNAP91 | 0.089 | ⚠ within organs, on part of the lines; also absent: CHST8, PLEKHG4B, COLEC12; maybe low, not absent; co-absent with the target |
| [[GNAO1]] | C | GNAO1 activity raises CHST8's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.23× lower at baseline in the lines without GNAO1 | 0.095 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDLIM3]] | B | CHST8 activity raises PDLIM3's level | lines that do not express CHST8 (29) vs lines expressing it (21) | 1.86× lower at baseline in the lines without CHST8 | 0.052 | ⚠ within organs, on part of the lines; also absent: PLEKHG4B, JAKMIP1, SNAP91 |
| [[OLFM1]] | C | CHST8 activity raises OLFM1's level | lines that do not express CHST8 (29) vs lines expressing it (21) | 3.91× lower at baseline in the lines without CHST8 | 0.055 | ⚠ within organs, on part of the lines; also absent: PLEKHG4B, JAKMIP1, SNAP91; co-absent with the target |
| [[COLEC12]] | C | CHST8 activity raises COLEC12's level | lines that do not express CHST8 (29) vs lines expressing it (21) | 2.62× lower at baseline in the lines without CHST8 | 0.057 | ⚠ within organs, on part of the lines; also absent: PLEKHG4B, JAKMIP1, SNAP91; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.649). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.9, 32.7); signed map (33.3, 25.8). **Vector** length 52.5, 14.2% of its response variance represented; |z| ≥ 3 in 487 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.7 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +25.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +6.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +0.7 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -4.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -0.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -3.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | carbohydrate sulfotransferase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:33,621,953-33,773,509 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GALNAC4ST-1 |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 4 pathways, smallest: Reactions specific to the complex N-glycan synthesis pathway; N-glycan antennae elongation in the medial/trans-Golgi; Transport to the Golgi and subsequent modification |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2A9](https://www.uniprot.org/uniprotkb/Q9H2A9) (Carbohydrate sulfotransferase 8):

> Catalyzes the transfer of sulfate to position 4 of non-reducing N-acetylgalactosamine (GalNAc) residues in both N-glycans and O-glycans. Transfers sulfate to the 4-position of GalNAc in the context of GalNAcbeta1->4GlcNAcbeta1->R attached to both N-linked and core 2 branched O-linked oligosaccharides. Required for biosynthesis of glycoprotein hormones lutropin and thyrotropin, by mediating sulfation of their carbohydrate structures. Not active toward chondroitin and dermatan.

**Summary**, from NCBI Gene [64377](https://www.ncbi.nlm.nih.gov/gene/64377):

> The protein encoded by this gene belongs to the sulfotransferase 2 family. It is predominantly expressed in the pituitary gland, and is localized to the golgi membrane. This protein catalyzes the transfer of sulfate to position 4 of non-reducing N-acetylgalactosamine (GalNAc) residues in both N-glycans and O-glycans. It is responsible for sulfation of GalNAc on luteinizing hormone (LH), which is required for production of the sex hormones. Mice lacking this enzyme, exhibit increased levels of …

**Accessions** — [HGNC:15993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15993) · Entrez [64377](https://www.ncbi.nlm.nih.gov/gene/64377) · UniProt [Q9H2A9](https://www.uniprot.org/uniprotkb/Q9H2A9) · Ensembl [ENSG00000124302](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124302)

## Data

Gene col 4517: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4517); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4517, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4517]; `tensor/DDL_lfc|DDL_z.npy` [4517]; `embed/gene_vectors.npy` [4517]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4517 or target_col == 4517). Every well: [[CHST8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHST8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
