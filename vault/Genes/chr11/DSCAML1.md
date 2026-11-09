---
symbol: "DSCAML1"
type: "gene"
col: 10790
ensembl_id: "ENSG00000177103"
name: "DS cell adhesion molecule like 1"
location: "11q23.3"
module: 8
arm: "+"
pooled_cpm: 15.66
n_lines_expressing: 13
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 25
direction_downstream: 40
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# DSCAML1

*DS cell adhesion molecule like 1* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.74× (z +15.0, q 0e+00, up in 2 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.668× (z -4.3, q 0.005, down in 7 of 10 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FXYD2]] (+0.77, fdr 7e-06, ⚠ same locus), [[RHEX]] (+0.67, fdr 7e-06), [[ITIH2]] (+0.62, fdr 1e-05), [[TIMD4]] (+0.62, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 40 go from it, the strongest it → [[GAL3ST1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10790.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.74×** | +15.0 | 0e+00 | 2/10 (SW480, HepG2/C3A) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.88×** | +11.1 | 3e-26 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +9.5 | 4e-19 | 1/6 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +8.8 | 2e-16 | 4/10 (HepG2/C3A, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +8.7 | 3e-16 | 2/10 (SW480, BT-474) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +8.1 | 8e-14 | 1/6 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.68×** | +5.4 | 5e-06 | 3/10 (COLO 205, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +5.3 | 9e-06 | 1/10 (SW480) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +5.2 | 1e-05 | 1/10 (SW480) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +5.1 | 2e-05 | 3/10 (HepG2/C3A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.6 | 2e-04 | 3/11 (A498, HepG2/C3A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +4.5 | 3e-04 | 2/10 (SW480, SHP-77) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.41×** | +3.6 | 0.017 | 0/10 | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.018 | 1/10 (COLO 205) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.019 | 2/9 (HepG2/C3A, A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Demeclocycline (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.031 | 4/10 (HEC-1-A, SHP-77, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.042 | 4/10 (A498, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.047 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.054 | 0/10 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10790.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.668×** | -4.3 | 0.005 | 7/10 (CFPAC-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.754×** | -4.3 | 0.005 | 4/10 (A549, A498, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.688×** | -3.8 | 0.024 | 3/10 (CFPAC-1, SW480, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.749× | -3.1 | 0.28 | 3/10 (CFPAC-1, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10790. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 286 | 2 (1 ⚠) | 12 (7 ⚠) | [[Selinexor (drug)]] 5 µM 3.06× (z +10.9) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Osimertinib (mesylate) (drug)]] 5 µM 3.71× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.0435× (z -30.4) |
| [[A549 (line)]] | wt | 53.9 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0859× (z -15.6) |
| [[CFPAC-1 (line)]] | alt | 65.3 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 191 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0650× (z -15.1) |
| [[SW480 (line)]] | alt | 8.89 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.19× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.136× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 9.39 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0970× (z -9.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.01 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10790), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FXYD2]] | +0.77 | +0.84 / +0.64 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[RHEX]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ITIH2]] | +0.62 | +0.57 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[TIMD4]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 | same gene group |
| [[IGFBP1]] | +0.58 | +0.46 / +0.50 | both halves | 3e-05 | **novel candidate** |
| [[POU5F1]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[ARSL]] | +0.55 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[EPCAM-DT]] | +0.55 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[UNC5CL]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[SLC15A1]] | +0.52 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[HNF1A-AS1]] | +0.52 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[SMIM2-AS1]] | +0.52 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[PAX8]] | +0.51 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 1, C 24. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DSCAML1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FGA]] | C | FGA activity raises DSCAML1's level | lines that do not express FGA (43) vs lines expressing it (7) | 6.66× lower at baseline in the lines without FGA | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[FXYD2]] | C | FXYD2 activity raises DSCAML1's level | lines that do not express FXYD2 (38) vs lines expressing it (12) | 5.77× lower at baseline in the lines without FXYD2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSCAML1, ITIH2, FGA; co-absent with the target |
| [[F5]] | C | F5 activity raises DSCAML1's level | lines that do not express F5 (39) vs lines expressing it (11) | 4.08× lower at baseline in the lines without F5 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPX2, FGA, CPLX2; co-absent with the target |
| [[ITIH2]] | C | ITIH2 activity raises DSCAML1's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 5.79× lower at baseline in the lines without ITIH2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; co-absent with the target |
| [[HNF1A-AS1]] | C | HNF1A-AS1 activity raises DSCAML1's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 3.02× lower at baseline in the lines without HNF1A-AS1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent; co-absent with the target |
| [[KRT23]] | C | KRT23 activity raises DSCAML1's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 3.04× lower at baseline in the lines without KRT23 | 0.012 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP; co-absent with the target |
| [[SERPINA5]] | C | SERPINA5 activity raises DSCAML1's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 3.29× lower at baseline in the lines without SERPINA5 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546; co-absent with the target |
| [[IGFBP1]] | C | IGFBP1 activity raises DSCAML1's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 2.77× lower at baseline in the lines without IGFBP1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2; co-absent with the target |
| [[SGPP2]] | C | SGPP2 activity raises DSCAML1's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 2.44× lower at baseline in the lines without SGPP2 | 0.032 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4; co-absent with the target |
| [[PCK1]] | C | PCK1 activity raises DSCAML1's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 2.44× lower at baseline in the lines without PCK1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2; co-absent with the target |
| [[DCDC2]] | C | DCDC2 activity raises DSCAML1's level | lines that do not express DCDC2 (25) vs lines expressing it (25) | 2.42× lower at baseline in the lines without DCDC2 | 0.040 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1; co-absent with the target |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 17, C 23. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAL3ST1]] | B | DSCAML1 activity raises GAL3ST1's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.14× lower at baseline in the lines without DSCAML1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[SPATA6L]] | B | DSCAML1 activity raises SPATA6L's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.05× lower at baseline in the lines without DSCAML1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[LASTR]] | B | DSCAML1 activity raises LASTR's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 1.85× lower at baseline in the lines without DSCAML1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[BCL2L15]] | B | DSCAML1 activity raises BCL2L15's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 1.40× lower at baseline in the lines without DSCAML1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[PDE11A]] | B | DSCAML1 activity raises PDE11A's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.42× lower at baseline in the lines without DSCAML1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[ALG1L9P]] | B | DSCAML1 activity raises ALG1L9P's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 1.50× lower at baseline in the lines without DSCAML1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[LINC02656]] | B | DSCAML1 activity raises LINC02656's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 1.67× lower at baseline in the lines without DSCAML1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[STS]] | B | DSCAML1 activity raises STS's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.65× lower at baseline in the lines without DSCAML1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[HGD]] | B | DSCAML1 activity raises HGD's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.96× lower at baseline in the lines without DSCAML1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[CCDC162P]] | B | DSCAML1 activity raises CCDC162P's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.01× lower at baseline in the lines without DSCAML1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[RPH3AL]] | B | DSCAML1 activity raises RPH3AL's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.33× lower at baseline in the lines without DSCAML1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[UNC5CL]] | B | DSCAML1 activity raises UNC5CL's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 1.66× lower at baseline in the lines without DSCAML1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.462). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.7, 44.5); signed map (52.2, 26.9). **Vector** length 51.1, 18.8% of its response variance represented; |z| ≥ 3 in 383 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +1.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +5.4 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | DS cell adhesion molecule like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:117,427,772-117,817,525 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1132 |
| Gene groups (HGNC) | Fibronectin type III domain containing; V-set domain containing; I-set domain containing; Ig-like cell adhesion molecule family |
| Reactome | 4 pathways, smallest: DSCAM interactions; Netrin-1 signaling; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TD84](https://www.uniprot.org/uniprotkb/Q8TD84) (Cell adhesion molecule DSCAML1):

> Cell adhesion molecule that plays a role in neuronal self-avoidance. Promotes repulsion between specific neuronal processes of either the same cell or the same subtype of cells. Promotes both isoneuronal self-avoidance for creating an orderly neurite arborization in retinal rod bipolar cells and heteroneuronal self-avoidance to maintain mosaic spacing between AII amacrine cells (By similarity). Adhesion molecule that promotes lamina-specific synaptic connections in the retina: expressed in …

**Summary**, from NCBI Gene [57453](https://www.ncbi.nlm.nih.gov/gene/57453):

> The protein encoded by this gene is a member of the Ig superfamily of cell adhesion molecules and is involved in neuronal differentiation. The encoded membrane-bound protein localizes to the cell surface, where it forms aggregates that repel neuronal processes of the same cell type. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:14656](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14656) · Entrez [57453](https://www.ncbi.nlm.nih.gov/gene/57453) · UniProt [Q8TD84](https://www.uniprot.org/uniprotkb/Q8TD84) · Ensembl [ENSG00000177103](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177103)

## Data

Gene col 10790: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10790); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10790, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10790]; `tensor/DDL_lfc|DDL_z.npy` [10790]; `embed/gene_vectors.npy` [10790]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10790 or target_col == 10790). Every well: [[DSCAML1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DSCAML1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
