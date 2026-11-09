---
symbol: "FGA"
type: "gene"
col: 10131
ensembl_id: "ENSG00000171560"
name: "fibrinogen alpha chain"
location: "4q31.3"
module: 139
arm: "+"
pooled_cpm: 7.4
n_lines_expressing: 7
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 40
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# FGA

*fibrinogen alpha chain* — 4q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.66× (z +11.1, q 1e-25, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.59× (z +7.6, q 4e-12, up in 2 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2030 0.0162×, HepG2/C3A 0.0689×, CFPAC-1 0.0290×; ⚠ cell-cycle shift, explains ~81% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H2030 0.0157×, CFPAC-1 0.00728×; ⚠ cell-cycle shift, explains ~0% of this change); [[Daptomycin (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0187×; ⚠ unreliable plate only); [[Tofacitinib (citrate) (drug)]] 5 µM in 1 line (CFPAC-1 0.0605×); [[Verteporfin (drug)]] 5 µM in 1 line (CFPAC-1 0.0203×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGG]] (+0.83, fdr 7e-06, ⚠ same locus), [[CP]] (+0.76, fdr 7e-06), [[FGB]] (+0.70, fdr 7e-06, ⚠ same locus), [[HAVCR1]] (+0.70, fdr 7e-06), [[PON3]] (+0.66, fdr 1e-05); moves opposite to [[IL23A]] (-0.48, fdr 3e-05), [[HMGA1]] (-0.47, fdr 8e-05), [[C11orf68]] (-0.45, fdr 7e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[FGB]] → it (grade C ⚠); 40 go from it, the strongest it → [[PTP4A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10131.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.66×** | +11.1 | 1e-25 | 2/3 (HepG2/C3A, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.85×** | +10.0 | 5e-21 | 2/4 (HepG2/C3A, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.26×** | +8.7 | 8e-16 | 2/3 (HepG2/C3A, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.59×** | +7.6 | 4e-12 | 2/5 (HepG2/C3A, COLO 205) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.33×** | +4.8 | 2e-04 | 1/4 (CFPAC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here); position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **2.28×** | +4.7 | 3e-04 | 3/5 (A549, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +4.4 | 9e-04 | 5/5 (HepG2/C3A, CFPAC-1, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.91×** | +4.3 | 1e-03 | 5/5 (HepG2/C3A, CFPAC-1, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +4.2 | 0.001 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.94×** | +3.7 | 0.010 | 4/5 (A549, NCI-H2030, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.92×** | +3.7 | 0.012 | 4/5 (A549, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.89×** | +3.6 | 0.014 | 4/5 (A549, NCI-H2030, …) | all doses, flat | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.44×** | +3.6 | 0.014 | 2/4 (HepG2/C3A, A549) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.91×** | +3.5 | 0.018 | 5/5 (A549, NCI-H2030, …) | all doses, flat |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.35×** | +3.4 | 0.022 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +3.4 | 0.027 | 0/5 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.27×** | +3.3 | 0.031 | 4/4 (CFPAC-1, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.74×** | +3.1 | 0.052 | 4/5 (A549, NCI-H2030, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.82×** | +3.1 | 0.052 | 4/5 (HepG2/C3A, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.75×** | +3.0 | 0.064 | 5/5 (HepG2/C3A, NCI-H2030, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.53×** | +3.0 | 0.066 | 5/5 (HepG2/C3A, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10131.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2030 0.0162×, HepG2/C3A 0.0689×, CFPAC-1 0.0290×; ⚠ cell-cycle shift, explains ~81% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H2030 0.0157×, CFPAC-1 0.00728×; ⚠ cell-cycle shift, explains ~0% of this change); [[Daptomycin (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0187×; ⚠ unreliable plate only); [[Tofacitinib (citrate) (drug)]] 5 µM in 1 line (CFPAC-1 0.0605×); [[Verteporfin (drug)]] 5 µM in 1 line (CFPAC-1 0.0203×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.519× | -3.5 | 0.21 | 0/5 | inconsistent across doses | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.552× | -3.4 | 0.21 | 1/5 (COLO 205) | top dose only | position effect removed |
| [[Fingolimod (hydrochloride) (drug)]] 0.5 µM |  | 0.573× | -3.2 | 0.24 | 0/5 | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.575× | -3.1 | 0.24 | 0/5 | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10131. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 17.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0290× (z -11.7) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Tofacitinib (citrate) (drug)]] 5 µM 0.0605× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 181 | 1 (1 ⚠) | 2 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.08× (z +11.0) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.0162× (z -25.0) ⚠ cell-cycle shift, explains ~81% of this change |
| [[HepG2_C3A (line)]] | wt | 81.2 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.82× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.0689× (z -14.8) ⚠ cell-cycle shift, explains ~81% of this change |
| [[A-172 (line)]] | wt | 0.599 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.443 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.682 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.569 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.489 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.790 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.579 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.625 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.628 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.865 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.700 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.04 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10131), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGG]] | +0.83 | +0.80 / +0.89 | both halves | 7e-06 | same gene group; pathway: HALLMARK_COAGULATION; STRING 999; ⚠ same locus (13.4 kb, same strand: neighbours can correlate without regulation) |
| [[CP]] | +0.76 | +0.68 / +0.78 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 559 |
| [[FGB]] | +0.70 | +0.64 / +0.79 | both halves | 7e-06 | same gene group; pathway: Aggregated β-amyloid interacts with fibrinogen; STRING 999; ⚠ same locus (10.3 kb: neighbours can correlate without regulation) |
| [[HAVCR1]] | +0.70 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[PON3]] | +0.66 | +0.62 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[SAA4]] | +0.65 | +0.63 / +0.67 | both halves | 7e-06 | STRING 522 |
| [[C3]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 | same gene group; pathway: HALLMARK_COAGULATION; STRING 613 |
| [[SAA2-SAA4]] | +0.65 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[STOM]] | +0.65 | +0.58 / +0.64 | both halves | 8e-06 | **novel candidate** |
| [[CD38]] | +0.64 | +0.48 / +0.61 | both halves | 2e-05 | **novel candidate** |
| [[SAA2]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 | STRING 432 |
| [[TIMD4]] | +0.63 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[SLC34A2]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[POU5F1]] | +0.61 | +0.64 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL23A]] | -0.48 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[HMGA1]] | -0.47 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[C11orf68]] | -0.45 | -0.37 / -0.39 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGB]] | C | FGB activity raises FGA's level | lines that do not express FGB (42) vs lines expressing it (8) | 7.06× lower at baseline in the lines without FGB | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2; co-absent with the target |
| [[IGFBP1]] | C | IGFBP1 activity raises FGA's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 4.07× lower at baseline in the lines without IGFBP1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2; co-absent with the target |
| [[TIMD4]] | C | TIMD4 activity raises FGA's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 4.16× lower at baseline in the lines without TIMD4 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[FGG]] | C | FGG activity raises FGA's level | lines that do not express FGG (42) vs lines expressing it (8) | 6.22× lower at baseline in the lines without FGG | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[HAVCR1]] | C | HAVCR1 activity raises FGA's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 3.62× lower at baseline in the lines without HAVCR1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[HLA-DRB1]] | C | HLA-DRB1 activity raises FGA's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 2.11× lower at baseline in the lines without HLA-DRB1 | 0.039 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP; co-absent with the target |
| [[AKR1C2]] | C | AKR1C2 activity raises FGA's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 2.79× lower at baseline in the lines without AKR1C2 | 0.040 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2; co-absent with the target |
| [[GPR141]] | C | GPR141 activity raises FGA's level | lines that do not express GPR141 (39) vs lines expressing it (11) | 2.37× lower at baseline in the lines without GPR141 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, S100A8, LINC00879; co-absent with the target |
| [[ITIH2]] | C | ITIH2 activity raises FGA's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 3.71× lower at baseline in the lines without ITIH2 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; co-absent with the target |
| [[CYP24A1]] | C | CYP24A1 activity raises FGA's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 3.72× lower at baseline in the lines without CYP24A1 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG; co-absent with the target |
| [[FXYD2]] | C | FXYD2 activity raises FGA's level | lines that do not express FXYD2 (38) vs lines expressing it (12) | 2.29× lower at baseline in the lines without FXYD2 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSCAML1, ITIH2, FGA; co-absent with the target |
| [[POU5F1]] | C | POU5F1 activity raises FGA's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 1.91× lower at baseline in the lines without POU5F1 | 0.090 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6; co-absent with the target |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 9, C 31. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTP4A1]] | B | FGA activity raises PTP4A1's level | lines that do not express FGA (43) vs lines expressing it (7) | 3.17× lower at baseline in the lines without FGA | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG |
| [[ODF3B]] | B | FGA activity raises ODF3B's level | lines that do not express FGA (43) vs lines expressing it (7) | 3.14× lower at baseline in the lines without FGA | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG |
| [[SQOR]] | B | FGA activity raises SQOR's level | lines that do not express FGA (43) vs lines expressing it (7) | 3.71× lower at baseline in the lines without FGA | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG |
| [[SAA2]] | B | FGA activity raises SAA2's level | lines that do not express FGA (43) vs lines expressing it (7) | 3.69× lower at baseline in the lines without FGA | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG |
| [[STAT3]] | B | FGA activity raises STAT3's level | lines that do not express FGA (43) vs lines expressing it (7) | 1.48× lower at baseline in the lines without FGA | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG |
| [[CARD14]] | B | FGA activity raises CARD14's level | lines that do not express FGA (43) vs lines expressing it (7) | 1.89× lower at baseline in the lines without FGA | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG |
| [[OPN3]] | B | FGA activity raises OPN3's level | lines that do not express FGA (43) vs lines expressing it (7) | 2.35× lower at baseline in the lines without FGA | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG |
| [[SQOR]] | B | FGA activity strengthens SQOR's drug response | lines that do not express FGA (36) vs lines expressing it (6) | the lines without FGA respond 0.62× as strongly (z diff +2.25); strongest at Homoharringtonine 5 µM: 0.72x vs 0.30x (z diff +6.3) | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; target measured in part of the lines; artifact flags |
| [[MTUS1]] | B | FGA activity raises MTUS1's level | lines that do not express FGA (43) vs lines expressing it (7) | 3.70× lower at baseline in the lines without FGA | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG |
| [[FGB]] | C | FGA activity raises FGB's level | lines that do not express FGA (43) vs lines expressing it (7) | 10.62× lower at baseline in the lines without FGA | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[IGFBP1]] | C | FGA activity raises IGFBP1's level | lines that do not express FGA (43) vs lines expressing it (7) | 14.32× lower at baseline in the lines without FGA | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[DSCAML1]] | C | FGA activity raises DSCAML1's level | lines that do not express FGA (43) vs lines expressing it (7) | 6.66× lower at baseline in the lines without FGA | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.8, 44.7); signed map (52.0, 26.4). **Vector** length 35.4, 15.3% of its response variance represented; |z| ≥ 3 in 261 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.3 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +1.7 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.1 | -0.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.1 | -0.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | +0.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.9 | -0.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -0.8 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | fibrinogen alpha chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.3 — chr4:154,583,126-154,590,742 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Receptor ligands; Fibrinogen C domain containing; Fibrinogen chains; Coagulation factors |
| Hallmark sets | COAGULATION |
| Reactome | 47 pathways, smallest: Aggregated β-amyloid interacts with fibrinogen; Fibrin formation; Defects of Coagulation cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [P02671](https://www.uniprot.org/uniprotkb/P02671) (Fibrinogen alpha chain):

> Cleaved by the protease thrombin to yield monomers which, together with fibrinogen beta (FGB) and fibrinogen gamma (FGG), polymerize to form an insoluble fibrin matrix. Fibrin has a major function in hemostasis as one of the primary components of blood clots. In addition, functions during the early stages of wound repair to stabilize the lesion and guide cell migration during re-epithelialization. Was originally thought to be essential for platelet aggregation, based on in vitro studies using …

**Summary**, from NCBI Gene [2243](https://www.ncbi.nlm.nih.gov/gene/2243):

> This gene encodes the alpha subunit of the coagulation factor fibrinogen, which is a component of the blood clot. Following vascular injury, the encoded preproprotein is proteolytically processed by thrombin during the conversion of fibrinogen to fibrin. Mutations in this gene lead to several disorders, including dysfibrinogenemia, hypofibrinogenemia, afibrinogenemia and renal amyloidosis. Alternative splicing results in multiple transcript variants, at least one of which encodes an isoform …

**Accessions** — [HGNC:3661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3661) · Entrez [2243](https://www.ncbi.nlm.nih.gov/gene/2243) · UniProt [P02671](https://www.uniprot.org/uniprotkb/P02671) · Ensembl [ENSG00000171560](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171560)

## Data

Gene col 10131: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10131); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10131, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10131]; `tensor/DDL_lfc|DDL_z.npy` [10131]; `embed/gene_vectors.npy` [10131]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10131 or target_col == 10131). Every well: [[FGA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
