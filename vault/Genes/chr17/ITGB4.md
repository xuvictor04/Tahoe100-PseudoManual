---
symbol: "ITGB4"
type: "gene"
col: 5325
ensembl_id: "ENSG00000132470"
name: "integrin subunit beta 4"
location: "17q25.1"
module: 31
arm: "+"
pooled_cpm: 92.2
n_lines_expressing: 25
n_dd_up: 3
n_dd_down: 59
n_dd_up_clean: 0
n_dd_down_clean: 51
in_vector_space: true
direction_upstream: 92
direction_downstream: 108
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ITGB4

*integrin subunit beta 4* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.79× (z +7.1, q 7e-10, up in 12 of 24 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 3.32×).
> Pooled over the cell lines (median), lowered significantly by 59 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.502× (z -11.7, q 4e-29, down in 22 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GNT3]] (+0.80, fdr 7e-06), [[MST1R]] (+0.78, fdr 7e-06), [[TNS4]] (+0.76, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 92 arrows point to it, the strongest [[SEPTIN9-DT]] → it (grade B ⚠); 108 go from it, the strongest it → [[ANXA11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5325.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 3.32×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +7.1 | 7e-10 | 12/24 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +6.4 | 6e-08 | 9/21 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +3.5 | 0.082 | 7/21 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 62 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 59 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5325.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.502×** | -11.7 | 4e-29 | 22/23 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.402×** | -11.0 | 1e-25 | 23/23 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.422×** | -10.4 | 5e-23 | 23/23 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.427×** | -10.2 | 2e-22 | 23/23 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.428×** | -10.2 | 2e-22 | 21/23 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.454×** | -9.5 | 2e-19 | 23/23 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.496×** | -8.4 | 3e-15 | 23/23 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.495×** | -8.0 | 9e-14 | 23/23 (KATO III, LoVo, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.512×** | -7.7 | 6e-13 | 20/23 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.526×** | -7.7 | 6e-13 | 23/23 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **0.636×** | -7.7 | 9e-13 | 18/23 (A-172, SW 900, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.519×** | -7.6 | 2e-12 | 19/23 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.542×** | -7.4 | 8e-12 | 21/23 (LoVo, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.549×** | -7.2 | 2e-11 | 19/23 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.572×** | -6.7 | 7e-10 | 22/23 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.570×** | -6.5 | 3e-09 | 19/23 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.582×** | -6.5 | 3e-09 | 20/23 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.588×** | -6.4 | 6e-09 | 17/23 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5325. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 312 | 0 | 28 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0729× (z -23.2) |
| [[SW480 (line)]] | alt | 255 | 0 | 23 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -21.9) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.134× (z -18.6) |
| [[MIA PaCa-2 (line)]] | alt | 149 | 0 | 22 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.129× (z -13.3) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.133× (z -13.1) |
| [[KATO III (line)]] | alt | 366 | 0 | 13 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -22.5) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.141× (z -18.1) |
| [[LS 180 (line)]] | wt | 276 | 0 | 13 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0885× (z -16.9) |
| [[AsPC-1 (line)]] | alt | 222 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0722× (z -21.6) |
| [[Hs 766T (line)]] | wt | 269 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -16.2) |
| [[HT-29 (line)]] | alt | 181 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -17.0) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.173× (z -15.7) |
| [[Panc 03.27 (line)]] | alt | 193 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -12.5) |
| [[HCT15 (line)]] | alt | 157 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -13.6) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.288× (z -12.8) |
| [[SW1417 (line)]] | alt | 172 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 201 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -11.9) |
| [[COLO 205 (line)]] | alt | 106 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 82.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.5) |
| [[SW 900 (line)]] | alt | 65.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -10.0) |
| [[SW 1271 (line)]] | alt | 121 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0718× (z -13.5) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.118× (z -10.9) |
| [[A-172 (line)]] | wt | 37.2 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.247× (z -11.4) |
| [[A-427 (line)]] | wt | 40.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.32× (z +9.5) | — |
| [[A549 (line)]] | wt | 56.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -8.9) ⚠ cell-cycle shift, explains ~23% of this change |
| [[A498 (line)]] | wt | 5.02 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.77 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.02 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.8 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.50 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.88 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 22.8 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 22.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.57 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.93 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.59 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.54 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.14 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.83 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.38 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 183 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5325), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GNT3]] | +0.80 | +0.84 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[MST1R]] | +0.78 | +0.76 / +0.77 | both halves | 7e-06 | same gene group; STRING 479 |
| [[TNS4]] | +0.76 | +0.78 / +0.72 | both halves | 7e-06 | STRING 558 |
| [[KIAA0040]] | +0.73 | +0.77 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[PADI1]] | +0.72 | +0.72 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[GJB3]] | +0.71 | +0.75 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[GPR35]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[TJP2]] | +0.69 | +0.69 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[HSD17B2]] | +0.69 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[KLK10]] | +0.69 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[INPP5D]] | +0.68 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ACSL5]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*92 arrows, 92 of them with an alert ⚠; grade A 0, B 16, C 76. Shown: the 12 strongest; 80 more arrows (80 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEPTIN9-DT]] | B | SEPTIN9-DT activity raises ITGB4's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 6.11× lower at baseline in the lines without SEPTIN9-DT | 0.005 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[ALS2CL]] | B | ALS2CL activity raises ITGB4's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 4.93× lower at baseline in the lines without ALS2CL | 0.015 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[EPHA2]] | B | EPHA2 activity raises ITGB4's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 5.96× lower at baseline in the lines without EPHA2 | 0.015 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[NGEF]] | B | NGEF activity raises ITGB4's level | lines that do not express NGEF (12) vs lines expressing it (38) | 6.14× lower at baseline in the lines without NGEF | 0.019 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TSPAN15, PDGFB |
| [[PTK2B]] | B | PTK2B activity raises ITGB4's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 3.52× lower at baseline in the lines without PTK2B | 0.024 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SLC16A5]] | B | SLC16A5 activity raises ITGB4's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 4.87× lower at baseline in the lines without SLC16A5 | 0.030 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[RPH3AL]] | B | RPH3AL activity raises ITGB4's level | lines that do not express RPH3AL (10) vs lines expressing it (40) | 5.24× lower at baseline in the lines without RPH3AL | 0.030 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, PATJ; maybe low, not absent |
| [[TJP2]] | B | TJP2 activity raises ITGB4's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.12× lower at baseline in the lines without TJP2 | 0.039 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[SEMA3B]] | B | SEMA3B activity raises ITGB4's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.09× lower at baseline in the lines without SEMA3B | 0.042 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[BCL2L1]] | B | BCL2L1 activity raises ITGB4's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 4.17× lower at baseline in the lines without BCL2L1 | 0.043 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises ITGB4's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.4% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds |
| [[MYEOV]] | B | MYEOV activity raises ITGB4's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 3.14× lower at baseline in the lines without MYEOV | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |

### Downstream of this gene

*108 arrows, 108 of them with an alert ⚠; grade A 0, B 50, C 58. Shown: the 12 strongest; 96 more arrows (96 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA11]] | B | ITGB4 activity raises ANXA11's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 3.16× lower at baseline in the lines without ITGB4 | 3e-04 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[LMO7]] | B | ITGB4 activity raises LMO7's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 4.75× lower at baseline in the lines without ITGB4 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[NGEF]] | B | ITGB4 activity raises NGEF's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 3.57× lower at baseline in the lines without ITGB4 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[EZR]] | B | ITGB4 activity raises EZR's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 3.01× lower at baseline in the lines without ITGB4 | 6e-04 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[ARHGAP27]] | B | ITGB4 activity raises ARHGAP27's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 2.90× lower at baseline in the lines without ITGB4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[BCL2L1]] | B | ITGB4 activity raises BCL2L1's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 3.29× lower at baseline in the lines without ITGB4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[PTK2B]] | B | ITGB4 activity raises PTK2B's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 2.89× lower at baseline in the lines without ITGB4 | 0.002 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[PKP3]] | B | ITGB4 activity raises PKP3's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 3.65× lower at baseline in the lines without ITGB4 | 0.002 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[ADAP1]] | B | ITGB4 activity raises ADAP1's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 2.89× lower at baseline in the lines without ITGB4 | 0.002 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[KRT8]] | B | ITGB4 activity raises KRT8's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 4.00× lower at baseline in the lines without ITGB4 | 0.003 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[KLF3]] | B | ITGB4 activity raises KLF3's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 2.16× lower at baseline in the lines without ITGB4 | 0.004 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[TMC6]] | B | ITGB4 activity raises TMC6's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 3.63× lower at baseline in the lines without ITGB4 | 0.004 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.759). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.8, 51.5); signed map (4.3, 37.9). **Vector** length 118, 43.8% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +3.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.6 | -11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | -11.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.5 | +2.1 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +1.5 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +1.0 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -4.6 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -7.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.1 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.8 | -5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -3.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.6 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit beta 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,721,328-75,757,818 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD104 |
| Gene groups (HGNC) | CD molecules; Fibronectin type III domain containing; Integrin beta subunits |
| Hallmark sets | MYOGENESIS, APICAL_JUNCTION, P53_PATHWAY |
| Reactome | 9 pathways, smallest: Type I hemidesmosome assembly; Syndecan interactions; Laminin interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P16144](https://www.uniprot.org/uniprotkb/P16144) (Integrin beta-4):

> Integrin alpha-6/beta-4 is a receptor for laminin. Plays a critical structural role in the hemidesmosome of epithelial cells. Is required for the regulation of keratinocyte polarity and motility. ITGA6:ITGB4 binds to NRG1 (via EGF domain) and this binding is essential for NRG1-ERBB signaling. ITGA6:ITGB4 binds to IGF1 and this binding is essential for IGF1 signaling. ITGA6:ITGB4 binds to IGF2 and this binding is essential for IGF2 signaling.

**Summary**, from NCBI Gene [3691](https://www.ncbi.nlm.nih.gov/gene/3691):

> Integrins are heterodimers comprised of alpha and beta subunits, that are noncovalently associated transmembrane glycoprotein receptors. Different combinations of alpha and beta polypeptides form complexes that vary in their ligand-binding specificities. Integrins mediate cell-matrix or cell-cell adhesion, and transduced signals that regulate gene expression and cell growth. This gene encodes the integrin beta 4 subunit, a receptor for the laminins. This subunit tends to associate with alpha 6 …

**Accessions** — [HGNC:6158](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6158) · Entrez [3691](https://www.ncbi.nlm.nih.gov/gene/3691) · UniProt [P16144](https://www.uniprot.org/uniprotkb/P16144) · Ensembl [ENSG00000132470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132470)

## Data

Gene col 5325: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5325); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5325, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5325]; `tensor/DDL_lfc|DDL_z.npy` [5325]; `embed/gene_vectors.npy` [5325]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5325 or target_col == 5325). Every well: [[ITGB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
