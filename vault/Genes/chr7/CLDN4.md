---
symbol: "CLDN4"
type: "gene"
col: 12094
ensembl_id: "ENSG00000189143"
name: "claudin 4"
location: "7q11.23"
module: 31
arm: "+"
pooled_cpm: 75.99
n_lines_expressing: 24
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 98
direction_downstream: 123
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# CLDN4

*claudin 4* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +6.3, q 1e-07, up in 1 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.450× (z -3.8, q 0.078, down in 19 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (NCI-H2347 0.192×, KATO III 0.204×, LoVo 0.204×, Panc 03.27 0.252×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2347 0.225×, KATO III 0.258×, LoVo 0.256×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.0343×, HT-29 0.128×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Verteporfin (drug)]] 5 µM in 2 lines (HT-29 0.218×, LoVo 0.213×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.185×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NECTIN4]] (+0.72, fdr 7e-06), [[TMPRSS4]] (+0.72, fdr 7e-06), [[C1orf116]] (+0.70, fdr 7e-06); moves opposite to [[TAS2R30]] (-0.54, fdr 5e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 98 arrows point to it, the strongest [[SEMA3B]] → it (grade B ⚠); 123 go from it, the strongest it → [[RHPN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12094.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +6.3 | 1e-07 | 1/23 (A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +4.7 | 9e-04 | 7/22 (MIA PaCa-2, A498, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.60×** | +4.3 | 0.003 | 18/22 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.006 | 16/23 (HepG2/C3A, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.018 | 18/22 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.039 | 16/22 (KATO III, LS 180, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.045 | 8/22 (MIA PaCa-2, HepG2/C3A, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.44×** | +3.4 | 0.045 | 8/22 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.43×** | +3.3 | 0.053 | 15/22 (NCI-H1573, CFPAC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.083 | 13/22 (A498, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.1 | 0.085 | 6/22 (AsPC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.43× | +3.0 | 0.11 | 1/21 (AsPC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12094.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (NCI-H2347 0.192×, KATO III 0.204×, LoVo 0.204×, Panc 03.27 0.252×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2347 0.225×, KATO III 0.258×, LoVo 0.256×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.0343×, HT-29 0.128×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Verteporfin (drug)]] 5 µM in 2 lines (HT-29 0.218×, LoVo 0.213×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.185×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.450×** | -3.8 | 0.078 | 19/22 (LS 180, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.680× | -3.5 | 0.14 | 19/22 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.698× | -3.4 | 0.14 | 9/22 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.711× | -3.2 | 0.16 | 12/22 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.712× | -3.2 | 0.16 | 13/22 (KATO III, HT-29, …) | top dose only |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.707× | -3.0 | 0.25 | 6/22 (LoVo, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12094. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 206 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -16.0) |
| [[HT-29 (line)]] | alt | 233 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 193 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -11.9) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -10.7) |
| [[LoVo (line)]] | wt | 332 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -14.1) |
| [[COLO 205 (line)]] | alt | 166 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -10.1) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -8.8) |
| [[KATO III (line)]] | alt | 306 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -14.3) |
| [[LS 180 (line)]] | wt | 168 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0343× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 218 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 34.1 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.56× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.195× (z -9.8) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 235 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -11.5) |
| [[BT-474 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 217 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -12.1) |
| [[SW48 (line)]] | wt | 42.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0704× (z -10.0) |
| [[SW480 (line)]] | alt | 58.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 9.23 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.57 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.17 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.82 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.78 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.71 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.15 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.20 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.68 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.09 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.54 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.68 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.16 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.99 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.34 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.17 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.39 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.75 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 43.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12094), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NECTIN4]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[TMPRSS4]] | +0.72 | +0.79 / +0.60 | both halves | 7e-06 |  |
| [[C1orf116]] | +0.70 | +0.73 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[CRYBG2]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[RDH13]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[LIPH]] | +0.68 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[ST14]] | +0.68 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[TACSTD2]] | +0.68 | +0.70 / +0.61 | both halves | 7e-06 | STRING 555 |
| [[TTC9]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[CLDN7]] | +0.67 | +0.68 / +0.58 | both halves | 7e-06 | same gene group; pathway: HALLMARK_APICAL_JUNCTION; STRING 953 |
| [[CDH1]] | +0.67 | +0.67 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION; STRING 829 |
| [[BICDL2]] | +0.66 | +0.57 / +0.65 | both halves | 9e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAS2R30]] | -0.54 | -0.40 / -0.58 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*98 arrows, 98 of them with an alert ⚠; grade A 0, B 11, C 87. Shown: the 12 strongest; 86 more arrows (86 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA3B]] | B | SEMA3B activity raises CLDN4's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.86× lower at baseline in the lines without SEMA3B | 0.010 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[KPNA7]] | B | KPNA7 activity raises CLDN4's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 4.12× lower at baseline in the lines without KPNA7 | 0.025 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[ADGRF1]] | B | ADGRF1 activity weakens CLDN4's drug response | lines that do not express ADGRF1 (9) vs lines expressing it (14) | the lines without ADGRF1 respond 1.66× as strongly (z diff -1.02); strongest at Idarubicin (hydrochloride) 5 µM: 0.80x vs 0.32x (z diff -6.5) | 0.026 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; target measured in part of the lines; both ways; artifact flags |
| [[GRHL3]] | B | GRHL3 activity raises CLDN4's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 3.74× lower at baseline in the lines without GRHL3 | 0.033 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[GPRC5A]] | B | GPRC5A activity raises CLDN4's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 3.59× lower at baseline in the lines without GPRC5A | 0.041 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[ADCY4]] | B | ADCY4 activity weakens CLDN4's drug response | lines that do not express ADCY4 (10) vs lines expressing it (13) | the lines without ADCY4 respond 1.47× as strongly (z diff -0.88); strongest at Idarubicin (hydrochloride) 5 µM: 0.75x vs 0.32x (z diff -6.0) | 0.054 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5; target measured in part of the lines; both ways; artifact flags |
| [[PLEKHG1]] | B | PLEKHG1 activity raises CLDN4's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.53× lower at baseline in the lines without PLEKHG1 | 0.057 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[ARHGAP30]] | B | ARHGAP30 activity raises CLDN4's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 2.97× lower at baseline in the lines without ARHGAP30 | 0.057 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[SLC44A4]] | B | SLC44A4 activity strengthens CLDN4's drug response | lines that do not express SLC44A4 (11) vs lines expressing it (12) | the lines without SLC44A4 respond 1.48× as strongly (z diff -0.58); rises at some drug-doses, falls at others (55% from rises): Doxorubicin (hydrochloride) 5 µM: 0.59x vs 0.39x (z diff +3.7); Entrectinib 5 µM: 1.34x vs 1.69x (z diff +1.4); PH-797804 5 µM: 0.40x vs 0.34x (z diff +1.1) | 0.070 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |
| [[EPS8L1]] | B | EPS8L1 activity raises CLDN4's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.98× lower at baseline in the lines without EPS8L1 | 0.085 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[TMC6]] | B | TMC6 activity raises CLDN4's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 3.85× lower at baseline in the lines without TMC6 | 0.091 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[TMPRSS4]] | C | TMPRSS4 activity raises CLDN4's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 11.21× lower at baseline in the lines without TMPRSS4 | 7e-06 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |

### Downstream of this gene

*123 arrows, 123 of them with an alert ⚠; grade A 0, B 47, C 76. Shown: the 12 strongest; 111 more arrows (111 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHPN2]] | B | CLDN4 activity raises RHPN2's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 3.55× lower at baseline in the lines without CLDN4 | 4e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[RDH13]] | B | CLDN4 activity raises RDH13's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 2.27× lower at baseline in the lines without CLDN4 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[MYO6]] | B | CLDN4 activity raises MYO6's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 2.14× lower at baseline in the lines without CLDN4 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[EPS8L1]] | B | CLDN4 activity raises EPS8L1's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 3.60× lower at baseline in the lines without CLDN4 | 0.002 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[KPNA7]] | B | CLDN4 activity raises KPNA7's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 3.04× lower at baseline in the lines without CLDN4 | 0.003 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[PARD6B]] | B | CLDN4 activity raises PARD6B's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 3.16× lower at baseline in the lines without CLDN4 | 0.004 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[RAB11FIP1]] | B | CLDN4 activity raises RAB11FIP1's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 2.71× lower at baseline in the lines without CLDN4 | 0.005 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[GPRC5A]] | B | CLDN4 activity raises GPRC5A's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 3.81× lower at baseline in the lines without CLDN4 | 0.006 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[ABHD11]] | B | CLDN4 activity raises ABHD11's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 2.58× lower at baseline in the lines without CLDN4 | 0.006 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[FAM83E]] | B | CLDN4 activity raises FAM83E's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 3.23× lower at baseline in the lines without CLDN4 | 0.006 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[EZR]] | B | CLDN4 activity raises EZR's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 2.64× lower at baseline in the lines without CLDN4 | 0.007 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[TNFRSF21]] | B | CLDN4 activity raises TNFRSF21's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 3.55× lower at baseline in the lines without CLDN4 | 0.008 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.7, 56.2); signed map (57.2, 8.0). **Vector** length 100, 42.7% of its response variance represented; |z| ≥ 3 in 607 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.4 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.7 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +2.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.1 | +4.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.0 | +3.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.8 | +3.5 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -3.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.4 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | claudin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:73,799,542-73,832,690 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CPE-R, WBSCR8, hCPE-R; previously CPETR, CPETR1 |
| Gene groups (HGNC) | Claudins |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 4 pathways, smallest: Tight junction interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O14493](https://www.uniprot.org/uniprotkb/O14493) (Claudin-4):

> Can associate with other claudins to regulate tight junction structural and functional strand dynamics. May coassemble with CLDN8 into tight junction strands containing anion-selective channels that convey paracellular chloride permeability in renal collecting ducts (By similarity). May integrate into CLDN3 strands to modulate localized tight junction barrier properties. May disrupt strand assembly of channel-forming CLDN2 and CLDN15 and inhibit cation conductance. Cannot form tight junction …

**Summary**, from NCBI Gene [1364](https://www.ncbi.nlm.nih.gov/gene/1364):

> The protein encoded by this intronless gene belongs to the claudin family. Claudins are integral membrane proteins that are components of the epithelial cell tight junctions, which regulate movement of solutes and ions through the paracellular space. This protein is a high-affinity receptor for Clostridium perfringens enterotoxin (CPE) and may play a role in internal organ development and function during pre- and postnatal life. This gene is deleted in Williams-Beuren syndrome, a …

**Accessions** — [HGNC:2046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2046) · Entrez [1364](https://www.ncbi.nlm.nih.gov/gene/1364) · UniProt [O14493](https://www.uniprot.org/uniprotkb/O14493) · Ensembl [ENSG00000189143](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189143)

## Data

Gene col 12094: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12094); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12094, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12094]; `tensor/DDL_lfc|DDL_z.npy` [12094]; `embed/gene_vectors.npy` [12094]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12094 or target_col == 12094). Every well: [[CLDN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLDN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
