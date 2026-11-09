---
symbol: "NLGN1"
type: "gene"
col: 9853
ensembl_id: "ENSG00000169760"
name: "neuroligin 1"
location: "3q26.31"
module: 121
arm: "+"
pooled_cpm: 155.18
n_lines_expressing: 20
n_dd_up: 11
n_dd_down: 19
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 14
direction_downstream: 14
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# NLGN1

*neuroligin 1* — 3q26.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.23× (z +14.3, q 3e-43, up in 3 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.508× (z -8.5, q 7e-15, down in 18 of 18 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.628× (z -5.9, q 6e-07, down in 13 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPY19L2]] (+0.65, fdr 1e-05), [[SAMMSON]] (+0.64, fdr 7e-06), [[LINC01205]] (+0.63, fdr 1e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[CHRM3]] → it (grade B ⚠); 14 go from it, the strongest it → [[CHRM3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9853.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +14.3 | 3e-43 | 3/19 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +11.0 | 1e-25 | 2/19 (HS-578T, NCI-H460) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +6.2 | 8e-08 | 1/18 (HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +6.1 | 2e-07 | 2/18 (HS-578T, NCI-H460) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.39×** | +5.8 | 8e-07 | 10/18 (HOP62, hTERT-HPNE, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.2 | 2e-05 | 4/18 (Panc 03.27, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.1 | 3e-05 | 1/20 (HS-578T) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.004 | 12/18 (HS-578T, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.058 | 0/18 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.072 | 7/18 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.083 | 2/19 (A498, NCI-H2030) | rises with dose | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | 1.28× | +3.1 | 0.10 | 9/18 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 0.5 µM |  | 1.28× | +3.0 | 0.10 | 0/19 | rises with dose | position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | 1.27× | +3.0 | 0.11 | 3/18 (A498, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9853.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.508×** | -8.5 | 7e-15 | 18/18 (C32, A-427, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.571×** | -7.1 | 5e-10 | 16/18 (C32, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.595×** | -6.6 | 1e-08 | 16/18 (C32, A-427, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.628×** | -5.9 | 6e-07 | 13/18 (LOX-IMVI, C32, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.651×** | -5.4 | 7e-06 | 16/18 (C32, SK-MEL-2, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.663×** | -5.2 | 2e-05 | 17/18 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.680×** | -4.7 | 2e-04 | 17/18 (C32, NCI-H23, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.703×** | -4.5 | 6e-04 | 13/18 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.530×** | -4.2 | 0.002 | 10/18 (C32, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.742×** | -3.8 | 0.009 | 16/18 (C32, SK-MEL-2, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.764×** | -3.4 | 0.033 | 11/18 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.752×** | -3.3 | 0.040 | 14/18 (HOP62, A-427, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.607×** | -3.3 | 0.043 | 7/18 (C32, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.763×** | -3.2 | 0.049 | 0/18 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.776×** | -3.2 | 0.051 | 11/18 (LOX-IMVI, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.842× | -3.1 | 0.067 | 15/19 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.777×** | -3.1 | 0.067 | 4/18 (Panc 03.27, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9853. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 1,683 | 0 | 17 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -16.2) |
| [[A-427 (line)]] | wt | 2,524 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -12.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 1,148 | 0 | 9 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.191× (z -12.0) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -11.4) |
| [[A498 (line)]] | wt | 151 | 0 | 6 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.175× (z -11.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.288× (z -8.5) |
| [[SHP-77 (line)]] | alt | 346 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -10.5) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 271 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -9.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H23 (line)]] | alt | 212 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0691× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -9.1) |
| [[HOP62 (line)]] | alt | 116 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +16.8) ⚠ cell-cycle shift, explains ~57% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.221× (z -10.1) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.228× (z -9.8) |
| [[HS-578T (line)]] | alt | 72.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +11.5) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.34× (z +10.2) | — |
| [[H4 (line)]] | wt | 538 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -9.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[hTERT-HPNE (line)]] | wt | 113 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.35× (z +15.4) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.35× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 74.7 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.367× (z -8.9) ⚠ cell-cycle shift, explains ~62% of this change |
| [[CFPAC-1 (line)]] | alt | 126 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.309× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 45.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +12.2) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[SW 900 (line)]] | alt | 69.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.193× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 32.1 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.81 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 24.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 25.9 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 17.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.55 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 22.5 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.56 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 30.3 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 13.3 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 13.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9853), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L2]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[SAMMSON]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[LINC01205]] | +0.63 | +0.49 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[NREP]] | +0.63 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[PTPRD]] | +0.60 | +0.57 / +0.60 | both halves | 1e-05 | pathway: Neuronal System; STRING 451 |
| [[PI15]] | +0.60 | +0.40 / +0.66 | both halves | 4e-05 |  |
| [[LINC00383]] | +0.60 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[MAGI2]] | +0.60 | +0.59 / +0.51 | both halves | 1e-05 | STRING 893 |
| [[MIR548XHG]] | +0.59 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[LINC02941]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[MAGI2-AS3]] | +0.59 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[LINC02438]] | +0.59 | +0.46 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 2, C 12. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHRM3]] | B | CHRM3 activity raises NLGN1's level | lines that do not express CHRM3 (20) vs lines expressing it (30) | 2.62× lower at baseline in the lines without CHRM3 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, NRXN1, MIR2052HG |
| [[FZD1]] | B | FZD1 activity raises NLGN1's level | lines that do not express FZD1 (6) vs lines expressing it (44) | 4.28× lower at baseline in the lines without FZD1 | 0.0999 | ⚠ within organs, on part of the lines; also absent: TMOD2, SNPH, DNAI1; maybe low, not absent |
| [[NEGR1]] | C | NEGR1 activity raises NLGN1's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 6.17× lower at baseline in the lines without NEGR1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[ATRNL1]] | C | ATRNL1 activity raises NLGN1's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 5.04× lower at baseline in the lines without ATRNL1 | 0.017 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent; co-absent with the target |
| [[LEF1]] | C | LEF1 activity raises NLGN1's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 3.82× lower at baseline in the lines without LEF1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1; co-absent with the target |
| [[CACNA2D1]] | C | CACNA2D1 activity raises NLGN1's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 5.19× lower at baseline in the lines without CACNA2D1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169; co-absent with the target |
| [[MEF2C-AS1]] | C | MEF2C-AS1 activity raises NLGN1's level | lines that do not express MEF2C-AS1 (16) vs lines expressing it (34) | 5.03× lower at baseline in the lines without MEF2C-AS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: MEF2C, RGS2, ADGRL4; co-absent with the target |
| [[LINC01205]] | C | LINC01205 activity raises NLGN1's level | lines that do not express LINC01205 (44) vs lines expressing it (6) | 10.56× lower at baseline in the lines without LINC01205 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, ENSG00000241168, GPR15; maybe low, not absent; co-absent with the target |
| [[LEF1-AS1]] | C | LEF1-AS1 activity raises NLGN1's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 5.09× lower at baseline in the lines without LEF1-AS1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent; co-absent with the target |
| [[RNF17]] | C | RNF17 activity raises NLGN1's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 5.52× lower at baseline in the lines without RNF17 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD; co-absent with the target |
| [[EPHA3]] | C | EPHA3 activity raises NLGN1's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 3.73× lower at baseline in the lines without EPHA3 | 0.074 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491; co-absent with the target |
| [[NLGN4X]] | C | NLGN4X activity raises NLGN1's level | lines that do not express NLGN4X (37) vs lines expressing it (13) | 5.73× lower at baseline in the lines without NLGN4X | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 2, C 12. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHRM3]] | B | NLGN1 activity raises CHRM3's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 1.77× lower at baseline in the lines without NLGN1 | 0.017 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1 |
| [[NFATC4]] | B | NLGN1 activity raises NFATC4's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 1.89× lower at baseline in the lines without NLGN1 | 0.097 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1 |
| [[NEGR1]] | C | NLGN1 activity raises NEGR1's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 4.19× lower at baseline in the lines without NLGN1 | 0.009 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |
| [[PAX3]] | C | NLGN1 activity raises PAX3's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 3.76× lower at baseline in the lines without NLGN1 | 0.014 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |
| [[ATRNL1]] | C | NLGN1 activity raises ATRNL1's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 2.28× lower at baseline in the lines without NLGN1 | 0.045 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |
| [[PCDH7]] | C | NLGN1 activity raises PCDH7's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 3.57× lower at baseline in the lines without NLGN1 | 0.047 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |
| [[EPHA3]] | C | NLGN1 activity raises EPHA3's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 3.08× lower at baseline in the lines without NLGN1 | 0.050 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |
| [[LEF1]] | C | NLGN1 activity raises LEF1's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 2.24× lower at baseline in the lines without NLGN1 | 0.052 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |
| [[ADAMTS3]] | C | NLGN1 activity raises ADAMTS3's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 2.22× lower at baseline in the lines without NLGN1 | 0.054 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |
| [[DPY19L2]] | C | NLGN1 activity raises DPY19L2's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 2.43× lower at baseline in the lines without NLGN1 | 0.055 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |
| [[EYA1]] | C | NLGN1 activity raises EYA1's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 3.35× lower at baseline in the lines without NLGN1 | 0.064 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |
| [[SOX5]] | C | NLGN1 activity raises SOX5's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 3.03× lower at baseline in the lines without NLGN1 | 0.072 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.3, 28.5); signed map (31.7, 39.3). **Vector** length 91.8, 36.5% of its response variance represented; |z| ≥ 3 in 604 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +7.7 | +5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +5.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +4.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.1 | -7.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | -2.7 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -2.5 | -3.8 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -5.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | neuroligin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.31 — chr3:173,396,284-174,294,372 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1070, NLG1 |
| Gene groups (HGNC) | Neuroligins |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N2Q7](https://www.uniprot.org/uniprotkb/Q8N2Q7) (Neuroligin-1):

> Cell surface protein involved in cell-cell-interactions via its interactions with neurexin family members. Plays a role in synapse function and synaptic signal transmission, and probably mediates its effects by recruiting and clustering other synaptic proteins. May promote the initial formation of synapses, but is not essential for this. In vitro, triggers the de novo formation of presynaptic structures. May be involved in specification of excitatory synapses. Required to maintain wakefulness …

**Summary**, from NCBI Gene [22871](https://www.ncbi.nlm.nih.gov/gene/22871):

> This gene encodes a member of a family of neuronal cell surface proteins. Members of this family may act as splice site-specific ligands for beta-neurexins and may be involved in the formation and remodeling of central nervous system synapses. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14291](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14291) · Entrez [22871](https://www.ncbi.nlm.nih.gov/gene/22871) · UniProt [Q8N2Q7](https://www.uniprot.org/uniprotkb/Q8N2Q7) · Ensembl [ENSG00000169760](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169760)

## Data

Gene col 9853: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9853); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9853, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9853]; `tensor/DDL_lfc|DDL_z.npy` [9853]; `embed/gene_vectors.npy` [9853]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9853 or target_col == 9853). Every well: [[NLGN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NLGN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
