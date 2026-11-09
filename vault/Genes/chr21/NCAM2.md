---
symbol: "NCAM2"
type: "gene"
col: 7825
ensembl_id: "ENSG00000154654"
name: "neural cell adhesion molecule 2"
location: "21q21.1"
module: 9
arm: "+"
pooled_cpm: 26.5
n_lines_expressing: 26
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 15
direction_downstream: 10
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# NCAM2

*neural cell adhesion molecule 2* — 21q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.26× (z +17.1, q 0e+00, up in 21 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Vinblastine (sulfate) (drug)]] 0.5 µM: 0.744× (z -4.4, q 0.006, down in 10 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (CHP-212 0.103×, NCI-H661 0.222×, A-172 0.340×, HS-578T 0.349×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.150×, NCI-H23 0.183×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.0628×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H460 0.243×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.335×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CADM2]] (+0.75, fdr 7e-06), [[PCDH9]] (+0.71, fdr 7e-06), [[CDH10]] (+0.71, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[CSRNP3]] → it (grade B ⚠); 10 go from it, the strongest it → [[ADGRB3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7825.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.26×** | +17.1 | 0e+00 | 21/24 (HOP62, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +16.7 | 0e+00 | 6/23 (NCI-H1792, H4, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.99×** | +15.7 | 0e+00 | 7/18 (SW 900, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.44×** | +13.3 | 5e-38 | 7/21 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +12.8 | 1e-35 | 16/23 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +11.0 | 5e-26 | 20/23 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.05×** | +10.7 | 1e-24 | 20/23 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +10.4 | 2e-23 | 20/23 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.95×** | +10.0 | 2e-21 | 18/23 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +9.6 | 5e-20 | 16/22 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +8.2 | 1e-14 | 9/21 (SK-MEL-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.54×** | +7.3 | 2e-11 | 17/23 (NCI-H23, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +5.3 | 5e-06 | 6/24 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +5.1 | 1e-05 | 12/21 (SHP-77, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.8 | 6e-05 | 13/22 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.002 | 10/22 (A-427, NCI-H23, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.002 | 2/21 (A-427, SHP-77) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.005 | 14/21 (NCI-H2347, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7825.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (CHP-212 0.103×, NCI-H661 0.222×, A-172 0.340×, HS-578T 0.349×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.150×, NCI-H23 0.183×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.0628×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H460 0.243×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.335×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.744×** | -4.4 | 0.006 | 10/22 (CHP-212, SHP-77, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.781×** | -3.7 | 0.070 | 8/22 (NCI-H23, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.642× | -3.4 | 0.11 | 9/21 (A-427, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.804× | -3.2 | 0.17 | 8/23 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Lonafarnib (drug)]] 0.5 µM |  | 0.747× | -3.1 | 0.21 | 0/24 | inconsistent across doses | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.815× | -3.0 | 0.21 | 9/22 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.817× | -3.0 | 0.21 | 10/23 (NCI-H460, CHP-212, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7825. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 10.9 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +19.7) | — |
| [[NCI-H23 (line)]] | alt | 39.9 | 5 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 11.9× (z +14.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -9.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.335× (z -8.9) |
| [[SW 900 (line)]] | alt | 29.7 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +12.2) | — |
| [[J82 (line)]] | alt | 22.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +14.7) | — |
| [[NCI-H2347 (line)]] | alt | 38.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +15.7) | — |
| [[SNU-423 (line)]] | alt | 14.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +12.7) | — |
| [[CHP-212 (line)]] | wt | 546 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -17.0) |
| [[HEC-1-A (line)]] | alt | 9.57 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 7.12× (z +14.5) | — |
| [[H4 (line)]] | wt | 28.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 23.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.73× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 26.0 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.81× (z +9.9) | — |
| [[A-172 (line)]] | wt | 32.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 150 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +15.6) | — |
| [[NCI-H460 (line)]] | wt | 143 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.243× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 32.5 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.95× (z +8.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 90.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0628× (z -20.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 94.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 29.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -9.2) |
| [[NCI-H661 (line)]] | alt | 521 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -11.4) |
| [[SHP-77 (line)]] | alt | 84.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.99× (z +11.0) | — |
| [[A498 (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.01 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.53 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.43 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.44 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.03 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7825), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CADM2]] | +0.75 | +0.69 / +0.71 | both halves | 7e-06 | same gene group |
| [[PCDH9]] | +0.71 | +0.74 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CDH10]] | +0.71 | +0.56 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[ADGRL3]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[GRIA2]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[MARCHF1]] | +0.69 | +0.66 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[EPHA5]] | +0.68 | +0.62 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[TMEM108]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[KCNH7]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[SYT1]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[CTNNA2]] | +0.67 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[CRISPLD1]] | +0.66 | +0.62 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 2, C 13. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSRNP3]] | B | CSRNP3 activity raises NCAM2's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 2.71× lower at baseline in the lines without CSRNP3 | 0.024 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2 |
| [[TENM1]] | B | TENM1 activity raises NCAM2's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 2.58× lower at baseline in the lines without TENM1 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG |
| [[BCHE]] | C | BCHE activity raises NCAM2's level | lines that do not express BCHE (35) vs lines expressing it (15) | 7.13× lower at baseline in the lines without BCHE | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[LINC01885]] | C | LINC01885 activity raises NCAM2's level | lines that do not express LINC01885 (34) vs lines expressing it (16) | 3.73× lower at baseline in the lines without LINC01885 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287598, ZNF208, LINC00383; co-absent with the target |
| [[MIR99AHG]] | C | MIR99AHG activity raises NCAM2's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 4.20× lower at baseline in the lines without MIR99AHG | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[ADGRB3]] | C | ADGRB3 activity raises NCAM2's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 5.12× lower at baseline in the lines without ADGRB3 | 0.018 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4; co-absent with the target |
| [[CDH7]] | C | CDH7 activity raises NCAM2's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 5.53× lower at baseline in the lines without CDH7 | 0.038 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |
| [[BRINP3]] | C | BRINP3 activity raises NCAM2's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 4.11× lower at baseline in the lines without BRINP3 | 0.048 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises NCAM2's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 4.13× lower at baseline in the lines without CSMD3 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[CDH18]] | C | CDH18 activity raises NCAM2's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 4.97× lower at baseline in the lines without CDH18 | 0.054 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[FMN2]] | C | FMN2 activity raises NCAM2's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 5.57× lower at baseline in the lines without FMN2 | 0.060 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent; co-absent with the target |
| [[LINC02506]] | C | LINC02506 activity raises NCAM2's level | lines that do not express LINC02506 (40) vs lines expressing it (10) | 4.60× lower at baseline in the lines without LINC02506 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC01610, ENSG00000241168; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRB3]] | C | NCAM2 activity raises ADGRB3's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 6.29× lower at baseline in the lines without NCAM2 | 0.001 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |
| [[ST8SIA4]] | C | NCAM2 activity raises ST8SIA4's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 3.28× lower at baseline in the lines without NCAM2 | 0.028 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |
| [[RIMS1]] | C | NCAM2 activity raises RIMS1's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 2.46× lower at baseline in the lines without NCAM2 | 0.044 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |
| [[MMP16]] | C | NCAM2 activity raises MMP16's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 6.21× lower at baseline in the lines without NCAM2 | 0.045 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |
| [[B3GALT1]] | C | NCAM2 activity raises B3GALT1's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 2.54× lower at baseline in the lines without NCAM2 | 0.048 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |
| [[BCHE]] | C | NCAM2 activity raises BCHE's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 3.80× lower at baseline in the lines without NCAM2 | 0.055 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |
| [[LINC01885]] | C | NCAM2 activity raises LINC01885's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 3.19× lower at baseline in the lines without NCAM2 | 0.055 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |
| [[ELOVL4]] | C | NCAM2 activity raises ELOVL4's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 4.47× lower at baseline in the lines without NCAM2 | 0.077 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |
| [[UBBP4-1]] | C | NCAM2 activity raises UBBP4-1's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 2.79× lower at baseline in the lines without NCAM2 | 0.094 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |
| [[KCNH5]] | C | NCAM2 activity raises KCNH5's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 2.57× lower at baseline in the lines without NCAM2 | 0.099 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.4, 33.8); signed map (40.5, 35.5). **Vector** length 79.9, 23.2% of its response variance represented; |z| ≥ 3 in 686 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.1 | +13.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +17.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +9.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +2.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.9 | -0.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.5 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.3 | -0.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[crizotinib (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | neural cell adhesion molecule 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.1 — chr21:20,998,409-21,543,329 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NCAM21, MGC51008 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Ig-like cell adhesion molecule family |
| Matched by | ensembl_id |

**Function**, from UniProt [O15394](https://www.uniprot.org/uniprotkb/O15394) (Neural cell adhesion molecule 2):

> May play important roles in selective fasciculation and zone-to-zone projection of the primary olfactory axons.

**Summary**, from NCBI Gene [4685](https://www.ncbi.nlm.nih.gov/gene/4685):

> The protein encoded by this gene belongs to the immunoglobulin superfamily. It is a type I membrane protein and may function in selective fasciculation and zone-to-zone projection of the primary olfactory axons. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7657](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7657) · Entrez [4685](https://www.ncbi.nlm.nih.gov/gene/4685) · UniProt [O15394](https://www.uniprot.org/uniprotkb/O15394) · Ensembl [ENSG00000154654](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154654)

## Data

Gene col 7825: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7825); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7825, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7825]; `tensor/DDL_lfc|DDL_z.npy` [7825]; `embed/gene_vectors.npy` [7825]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7825 or target_col == 7825). Every well: [[NCAM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCAM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
