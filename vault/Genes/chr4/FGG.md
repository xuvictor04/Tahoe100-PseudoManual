---
symbol: "FGG"
type: "gene"
col: 10130
ensembl_id: "ENSG00000171557"
name: "fibrinogen gamma chain"
location: "4q32.1"
module: 155
arm: "+"
pooled_cpm: 7.43
n_lines_expressing: 8
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 27
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# FGG

*fibrinogen gamma chain* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.81× (z +9.4, q 4e-18, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.33× (z +6.4, q 3e-08, up in 2 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.0982×, HepG2/C3A 0.128×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.104×, NCI-H2030 0.173×; ⚠ cell-cycle shift, explains ~0% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H2030 0.173×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGB]] (+0.91, fdr 7e-06, ⚠ same locus), [[FGA]] (+0.83, fdr 7e-06, ⚠ same locus), [[SERPINB3]] (+0.71, fdr 7e-06), [[SERPINB4]] (+0.69, fdr 7e-06), [[P2RY6]] (+0.67, fdr 7e-06); moves opposite to [[ARHGEF2]] (-0.44, fdr 1e-04).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FGB]] → it (grade C ⚠); 27 go from it, the strongest it → [[MTUS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10130.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.81×** | +9.4 | 4e-18 | 3/5 (HepG2/C3A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.14×** | +9.2 | 8e-18 | 2/3 (HepG2/C3A, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.01×** | +6.8 | 1e-09 | 2/4 (NCI-H2030, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +6.4 | 3e-08 | 2/5 (HepG2/C3A, NCI-H2030) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +4.7 | 3e-04 | 4/6 (HepG2/C3A, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.20×** | +4.2 | 0.003 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.69×** | +3.8 | 0.013 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.61×** | +3.7 | 0.018 | 3/5 (HepG2/C3A, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.49×** | +3.5 | 0.032 | 4/6 (CFPAC-1, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.94×** | +3.4 | 0.045 | 4/6 (HepG2/C3A, NCI-H2030, …) | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.057 | 0/6 | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +3.2 | 0.061 | 0/6 | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.82× | +3.0 | 0.10 | 4/6 (HepG2/C3A, NCI-H2030, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.81× | +3.0 | 0.10 | 1/5 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10130.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.0982×, HepG2/C3A 0.128×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.104×, NCI-H2030 0.173×; ⚠ cell-cycle shift, explains ~0% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H2030 0.173×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | 0.483× | -3.6 | 0.18 | 0/6 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10130. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 195 | 1 (1 ⚠) | 3 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.71× (z +10.3) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.0982× (z -17.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.173× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 81.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -12.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.484 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.807 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.566 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.661 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.479 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.758 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.504 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.551 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.588 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.492 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10130), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGB]] | +0.91 | +0.88 / +0.92 | both halves | 7e-06 | same gene group; pathway: Aggregated β-amyloid interacts with fibrinogen; STRING 999; ⚠ same locus (31.3 kb: neighbours can correlate without regulation) |
| [[FGA]] | +0.83 | +0.80 / +0.89 | both halves | 7e-06 | same gene group; pathway: HALLMARK_COAGULATION; STRING 999; ⚠ same locus (13.4 kb, same strand: neighbours can correlate without regulation) |
| [[SERPINB3]] | +0.71 | +0.59 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB4]] | +0.69 | +0.59 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[P2RY6]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[S100A9]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 | pathway: Antigen processing-Cross presentation; STRING 617 |
| [[STOM]] | +0.61 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[AGT]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 | STRING 432 |
| [[SERPINA3]] | +0.59 | +0.56 / +0.63 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation; STRING 499 |
| [[C3]] | +0.58 | +0.48 / +0.61 | both halves | 2e-05 | same gene group; pathway: HALLMARK_COAGULATION; STRING 465 |
| [[SERPINA1]] | +0.58 | +0.46 / +0.58 | both halves | 3e-05 | pathway: HALLMARK_COAGULATION; STRING 886 |
| [[BCL6]] | +0.58 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[SECTM1]] | +0.58 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[CP]] | +0.58 | +0.48 / +0.67 | both halves | 2e-05 | pathway: Post-translational protein phosphorylation; STRING 463 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF2]] | -0.44 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGB]] | C | FGB activity raises FGG's level | lines that do not express FGB (42) vs lines expressing it (8) | 6.65× lower at baseline in the lines without FGB | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2; co-absent with the target |
| [[FGA]] | C | FGA activity raises FGG's level | lines that do not express FGA (43) vs lines expressing it (7) | 6.52× lower at baseline in the lines without FGA | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[TIMD4]] | C | TIMD4 activity raises FGG's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 3.39× lower at baseline in the lines without TIMD4 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[HAVCR1]] | C | HAVCR1 activity raises FGG's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 2.99× lower at baseline in the lines without HAVCR1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[AKR1C2]] | C | AKR1C2 activity raises FGG's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 2.37× lower at baseline in the lines without AKR1C2 | 0.087 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 5, C 22. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTUS1]] | B | FGG activity raises MTUS1's level | lines that do not express FGG (42) vs lines expressing it (8) | 3.88× lower at baseline in the lines without FGG | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB |
| [[PTP4A1]] | B | FGG activity raises PTP4A1's level | lines that do not express FGG (42) vs lines expressing it (8) | 2.96× lower at baseline in the lines without FGG | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB |
| [[ATAD3C]] | B | FGG activity raises ATAD3C's level | lines that do not express FGG (42) vs lines expressing it (8) | 1.86× lower at baseline in the lines without FGG | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB |
| [[IFITM2]] | B | FGG activity raises IFITM2's level | lines that do not express FGG (42) vs lines expressing it (8) | 2.33× lower at baseline in the lines without FGG | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB |
| [[OPN3]] | B | FGG activity raises OPN3's level | lines that do not express FGG (42) vs lines expressing it (8) | 2.52× lower at baseline in the lines without FGG | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB |
| [[FGB]] | C | FGG activity raises FGB's level | lines that do not express FGG (42) vs lines expressing it (8) | 10.94× lower at baseline in the lines without FGG | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[HLA-DRB1]] | C | FGG activity raises HLA-DRB1's level | lines that do not express FGG (42) vs lines expressing it (8) | 2.73× lower at baseline in the lines without FGG | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[HAVCR1]] | C | FGG activity raises HAVCR1's level | lines that do not express FGG (42) vs lines expressing it (8) | 3.33× lower at baseline in the lines without FGG | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[FGA]] | C | FGG activity raises FGA's level | lines that do not express FGG (42) vs lines expressing it (8) | 6.22× lower at baseline in the lines without FGG | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[RHEX]] | C | FGG activity raises RHEX's level | lines that do not express FGG (42) vs lines expressing it (8) | 1.89× lower at baseline in the lines without FGG | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[IGFBP1]] | C | FGG activity raises IGFBP1's level | lines that do not express FGG (42) vs lines expressing it (8) | 7.25× lower at baseline in the lines without FGG | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[TIMD4]] | C | FGG activity raises TIMD4's level | lines that do not express FGG (42) vs lines expressing it (8) | 2.03× lower at baseline in the lines without FGG | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.5, 47.7); signed map (54.0, 25.0). **Vector** length 32.9, 12.7% of its response variance represented; |z| ≥ 3 in 281 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.4 | +6.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.3 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.2 | +3.4 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.0 | -1.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -0.9 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | fibrinogen gamma chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.1 — chr4:154,604,134-154,612,967 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Receptor ligands; Fibrinogen C domain containing; Fibrinogen chains; Coagulation factors |
| Hallmark sets | COAGULATION |
| Reactome | 46 pathways, smallest: Aggregated β-amyloid interacts with fibrinogen; Fibrin formation; Defects of Coagulation cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [P02679](https://www.uniprot.org/uniprotkb/P02679) (Fibrinogen gamma chain):

> Together with fibrinogen alpha (FGA) and fibrinogen beta (FGB), polymerizes to form an insoluble fibrin matrix. Has a major function in hemostasis as one of the primary components of blood clots. In addition, functions during the early stages of wound repair to stabilize the lesion and guide cell migration during re-epithelialization. Was originally thought to be essential for platelet aggregation, based on in vitro studies using anticoagulated blood. However, subsequent studies have shown that …

**Summary**, from NCBI Gene [2266](https://www.ncbi.nlm.nih.gov/gene/2266):

> The protein encoded by this gene is the gamma component of fibrinogen, a blood-borne glycoprotein comprised of three pairs of nonidentical polypeptide chains. Following vascular injury, fibrinogen is cleaved by thrombin to form fibrin which is the most abundant component of blood clots. In addition, various cleavage products of fibrinogen and fibrin regulate cell adhesion and spreading, display vasoconstrictor and chemotactic activities, and are mitogens for several cell types. Mutations in …

**Accessions** — [HGNC:3694](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3694) · Entrez [2266](https://www.ncbi.nlm.nih.gov/gene/2266) · UniProt [P02679](https://www.uniprot.org/uniprotkb/P02679) · Ensembl [ENSG00000171557](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171557)

## Data

Gene col 10130: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10130); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10130, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10130]; `tensor/DDL_lfc|DDL_z.npy` [10130]; `embed/gene_vectors.npy` [10130]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10130 or target_col == 10130). Every well: [[FGG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
