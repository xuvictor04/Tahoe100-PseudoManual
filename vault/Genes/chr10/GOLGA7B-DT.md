---
symbol: "GOLGA7B-DT"
type: "gene"
col: 13586
ensembl_id: "ENSG00000227356"
name: "GOLGA7B divergent transcript"
location: "10q24.2"
module: 92
arm: "+"
pooled_cpm: 2.64
n_lines_expressing: 38
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# GOLGA7B-DT

*GOLGA7B divergent transcript* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.64× (z +15.9, q 0e+00, up in 10 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.96× (z +7.4, q 1e-11, up in 16 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.626× (z -4.2, q 0.013, down in 12 of 33 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW 900 0.0329×, HOP62 0.0386×; ⚠ cell-cycle shift, explains ~42% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.143×, A549 0.114×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 0.0639×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (SHP-77 0.0664×); [[Resveratrol (drug)]] 0.05 µM in 1 line (SHP-77 0.0746×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PICART1]] (+0.63, fdr 1e-05), [[LHX1-DT]] (+0.60, fdr 1e-05), [[NOS1]] (+0.57, fdr 2e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KLKP1-1]] → it (grade B ⚠); 2 go from it, the strongest it → [[ANKRD29]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13586.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.64×** | +15.9 | 0e+00 | 10/11 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.97×** | +14.6 | 0e+00 | 4/4 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.70×** | +11.2 | 7e-27 | 5/5 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +7.4 | 1e-11 | 16/33 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.05×** | +5.6 | 2e-06 | 16/28 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.9 | 9e-05 | 5/26 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.18×** | +4.7 | 2e-04 | 4/7 (NCI-H2347, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +4.0 | 0.004 | 5/15 (CFPAC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.0 | 0.004 | 5/26 (HCT15, A-427, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.67×** | +4.0 | 0.004 | 2/19 (HOP62, C32) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.64×** | +4.0 | 0.004 | 4/6 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.42×** | +3.9 | 0.005 | 5/33 (NCI-H2347, COLO 205, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.59×** | +3.6 | 0.013 | 5/29 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +3.5 | 0.019 | 6/30 (BT-474, SW1417, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.5 | 0.019 | 4/23 (RPMI-7951, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +3.4 | 0.026 | 7/33 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.029 | 5/33 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +3.1 | 0.072 | 5/31 (A498, NCI-H1573, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13586.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW 900 0.0329×, HOP62 0.0386×; ⚠ cell-cycle shift, explains ~42% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.143×, A549 0.114×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 0.0639×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (SHP-77 0.0664×); [[Resveratrol (drug)]] 0.05 µM in 1 line (SHP-77 0.0746×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.626×** | -4.2 | 0.013 | 12/33 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.639× | -3.5 | 0.12 | 9/33 (SW480, SW48, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.700× | -3.4 | 0.12 | 9/33 (NCI-H460, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.654× | -3.3 | 0.12 | 13/32 (SW 900, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.665× | -3.2 | 0.15 | 14/32 (RPMI-7951, COLO 205, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.727× | -3.0 | 0.23 | 11/33 (SW480, C32, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13586. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 9.12 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 24.9× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 7.19 | 0 | 2 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0664× (z -9.0) |
| [[A498 (line)]] | wt | 2.15 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 3.38 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 1.81 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0386× (z -8.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW 900 (line)]] | alt | 7.64 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0329× (z -11.1) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW480 (line)]] | alt | 3.91 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0639× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.732 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.393 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.770 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.545 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.734 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.759 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.983 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.895 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.454 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.858 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13586), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PICART1]] | +0.63 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[LHX1-DT]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 | same gene group |
| [[NOS1]] | +0.57 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[TRD-AS1]] | +0.55 | +0.37 / +0.68 | both halves | 8e-05 |  |
| [[GOLGA7B]] | +0.54 | +0.53 / +0.47 | both halves | 2e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CACNA2D4]] | +0.53 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[P4HA3]] | +0.51 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[KLKP1-1]] | +0.50 | +0.28 / +0.66 | both halves | 3e-04 |  |
| [[TMEM255B]] | +0.50 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[TEX10]] | +0.50 | +0.43 / +0.50 | both halves | 4e-05 |  |
| [[BTG1-DT]] | +0.50 | +0.37 / +0.60 | both halves | 8e-05 | same gene group |
| [[GDPD4]] | +0.50 | +0.25 / +0.63 | both halves | 4e-04 |  |
| [[SCUBE1]] | +0.50 | +0.46 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLKP1-1]] | B | KLKP1-1 activity raises GOLGA7B-DT's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 1.55× lower at baseline in the lines without KLKP1-1 | 0.079 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[MILR1]] | B | MILR1 activity raises GOLGA7B-DT's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 1.60× lower at baseline in the lines without MILR1 | 0.088 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[LINC01589]] | B | LINC01589 activity raises GOLGA7B-DT's level | lines that do not express LINC01589 (23) vs lines expressing it (27) | 1.40× lower at baseline in the lines without LINC01589 | 0.098 | ⚠ within organs, on part of the lines; also absent: HNF1B, ENSG00000279806, GOLT1A |
| [[GOLGA7B]] | C | GOLGA7B activity raises GOLGA7B-DT's level | lines that do not express GOLGA7B (14) vs lines expressing it (36) | 2.52× lower at baseline in the lines without GOLGA7B | 0.006 | ⚠ within organs, on part of the lines; also absent: GOLGA7B-DT, KCNS3, ENSG00000232386; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD29]] | B | GOLGA7B-DT activity raises ANKRD29's level | lines that do not express GOLGA7B-DT (12) vs lines expressing it (38) | 2.59× lower at baseline in the lines without GOLGA7B-DT | 0.031 | ⚠ within organs, on part of the lines; also absent: GOLGA7B, BCL11B, GJB2; maybe low, not absent |
| [[GOLGA7B]] | C | GOLGA7B-DT activity raises GOLGA7B's level | lines that do not express GOLGA7B-DT (12) vs lines expressing it (38) | 3.64× lower at baseline in the lines without GOLGA7B-DT | 0.028 | ⚠ within organs, on part of the lines; also absent: GOLGA7B, BCL11B, GJB2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.466). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.7, -4.1); signed map (10.8, 37.9). **Vector** length 52.9, 8.92% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.8 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.6 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.2 | +15.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +1.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +2.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.6 | -3.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.4 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -3.4 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | GOLGA7B divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q24.2 — chr10:97,828,478-97,849,798 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LINC00866 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:45232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:45232) · Entrez [100505561](https://www.ncbi.nlm.nih.gov/gene/100505561) · Ensembl [ENSG00000227356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227356)

## Data

Gene col 13586: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13586); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13586, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13586]; `tensor/DDL_lfc|DDL_z.npy` [13586]; `embed/gene_vectors.npy` [13586]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13586 or target_col == 13586). Every well: [[GOLGA7B-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLGA7B-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
