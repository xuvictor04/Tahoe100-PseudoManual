---
symbol: "BLVRA"
type: "gene"
col: 2780
ensembl_id: "ENSG00000106605"
name: "biliverdin reductase A"
location: "7p13"
module: 159
arm: "+"
pooled_cpm: 28.45
n_lines_expressing: 45
n_dd_up: 3
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# BLVRA

*biliverdin reductase A* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.49× (z +7.0, q 2e-09, up in 36 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.332× (z -19.2, q 0e+00, down in 42 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERAC1]] (+0.73, fdr 7e-06), [[PACC1]] (+0.71, fdr 7e-06), [[TSPAN33]] (+0.71, fdr 3e-05); moves opposite to [[CYB5D1]] (-0.66, fdr 1e-05), [[PCBP1-AS1]] (-0.64, fdr 5e-05), [[USP11]] (-0.64, fdr 4e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[ARHGEF10L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2780.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +7.0 | 2e-09 | 36/43 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +5.4 | 2e-05 | 29/43 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.4 | 0.002 | 19/40 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[vincristine (drug)]] 0.5 µM |  | 1.76× | +3.3 | 0.12 | 12/42 (NCI-H460, LoVo, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.30× | +3.2 | 0.14 | 18/42 (hTERT-HPNE, J82, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.28× | +3.0 | 0.25 | 14/41 (H4, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2780.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.332×** | -19.2 | 0e+00 | 42/43 (HS-578T, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.447×** | -9.9 | 9e-21 | 33/43 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.577×** | -9.6 | 2e-19 | 34/42 (SK-MEL-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.514×** | -7.9 | 5e-13 | 33/43 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.569×** | -6.7 | 3e-09 | 28/42 (MIA PaCa-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.636×** | -5.6 | 3e-06 | 26/43 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.443×** | -5.2 | 1e-05 | 29/43 (SK-MEL-2, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.498×** | -4.5 | 5e-04 | 20/42 (Panc 03.27, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -4.4 | 7e-04 | 21/42 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.786×** | -4.2 | 0.002 | 19/43 (HOP62, Hs 766T, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.799×** | -3.9 | 0.005 | 18/43 (RPMI-7951, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.753×** | -3.5 | 0.023 | 19/43 (NCI-H2030, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.603×** | -3.3 | 0.049 | 19/42 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.607×** | -3.2 | 0.054 | 13/43 (SHP-77, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.775×** | -3.1 | 0.064 | 15/43 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.779×** | -3.1 | 0.076 | 15/43 (SW480, PANC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2780. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 32.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -20.1) |
| [[A-172 (line)]] | wt | 70.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -17.7) |
| [[A-427 (line)]] | wt | 28.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0943× (z -16.6) |
| [[HOP62 (line)]] | alt | 23.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -17.7) |
| [[KATO III (line)]] | alt | 21.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 34.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 41.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -19.2) |
| [[PANC-1 (line)]] | alt | 36.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.6) |
| [[SW48 (line)]] | wt | 33.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -11.3) |
| [[A498 (line)]] | wt | 64.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -13.5) |
| [[Hs 766T (line)]] | wt | 27.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 12.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0909× (z -12.5) |
| [[RKO (line)]] | wt | 32.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.126× (z -12.6) |
| [[RPMI-7951 (line)]] | alt | 23.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0820× (z -18.9) |
| [[SK-MEL-2 (line)]] | alt | 30.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -14.9) |
| [[SW1417 (line)]] | alt | 18.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -9.5) |
| [[SW480 (line)]] | alt | 24.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -15.2) |
| [[A549 (line)]] | wt | 33.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -9.5) |
| [[C-33 A (line)]] | alt | 24.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 28.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -8.6) |
| [[J82 (line)]] | alt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -10.8) |
| [[LoVo (line)]] | wt | 27.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0863× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -15.6) |
| [[NCI-H2030 (line)]] | alt | 62.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -19.7) |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 26.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -13.7) |
| [[SNU-423 (line)]] | alt | 29.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -11.6) |
| [[SW 900 (line)]] | alt | 31.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -9.0) |
| [[AN3 CA (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.67 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.36 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2780), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERAC1]] | +0.73 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[PACC1]] | +0.71 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[TSPAN33]] | +0.71 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[FAM241B]] | +0.65 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[EIF4E3]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CDC14B]] | +0.65 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[CCDC112]] | +0.64 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[CAMK2G]] | +0.64 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[RECK]] | +0.64 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[RBIS]] | +0.62 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[GNA12]] | +0.62 | +0.64 / +0.38 | both halves | 6e-05 |  |
| [[CRLF3]] | +0.62 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5D1]] | -0.66 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[PCBP1-AS1]] | -0.64 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[USP11]] | -0.64 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[DDX39B]] | -0.63 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[ATXN1L]] | -0.62 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[EFCAB6]] | -0.62 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[SECISBP2]] | -0.62 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[EIF4G2]] | -0.61 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[MPDU1]] | -0.61 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[HCG17]] | -0.61 | -0.61 / -0.29 | both halves | 2e-04 |  |
| [[UBE3B]] | -0.60 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[TUG1]] | -0.60 | -0.51 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises BLVRA's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EFCAB6]] | B | EFCAB6 activity raises BLVRA's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 2.43× lower at baseline in the lines without EFCAB6 | 0.037 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[CCDC69]] | B | CCDC69 activity lowers BLVRA's level | lines that do not express CCDC69 (11) vs lines expressing it (39) | 1.40× higher at baseline in the lines without CCDC69 | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TSPAN33]] | B | TSPAN33 activity raises BLVRA's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.48× lower at baseline in the lines without TSPAN33 | 0.064 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF10L]] | B | BLVRA activity lowers ARHGEF10L's level | lines that do not express BLVRA (5) vs lines expressing it (45) | 3.41× higher at baseline in the lines without BLVRA | 0.060 | ⚠ within organs, on part of the lines; also absent: GABBR1, SOAT1, DBN1; its own permutation p |
| [[RNF216]] | B | BLVRA activity raises RNF216's level | lines that do not express BLVRA (5) vs lines expressing it (45) | 1.44× lower at baseline in the lines without BLVRA | 0.067 | ⚠ within organs, on part of the lines; also absent: GABBR1, SOAT1, DBN1 |

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.798). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.4, 2.4); signed map (-38.3, -5.1). **Vector** length 88.0, 23.6% of its response variance represented; |z| ≥ 3 in 635 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.2 | +5.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.7 | +2.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.1 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.4 | -19.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -4.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | biliverdin reductase A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:43,758,680-43,807,342 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BVRA, BVRalpha; previously BLVR |
| Gene groups (HGNC) | Gfo/Idh/MocA-like oxidoreductase domain containing; Oxidoreductases |
| Hallmark sets | FATTY_ACID_METABOLISM, HEME_METABOLISM |
| Reactome | 6 pathways, smallest: Heme degradation; Metabolism of porphyrins; Cytoprotection by HMOX1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P53004](https://www.uniprot.org/uniprotkb/P53004) (Biliverdin reductase A):

> Reduces the gamma-methene bridge of the open tetrapyrrole, biliverdin IXalpha, to bilirubin with the concomitant oxidation of a NADH or NADPH cofactor. Does not reduce bilirubin IXbeta. Uses the reactants NADH or NADPH depending on the pH; NADH is used at the acidic pH range (6-6.9) and NADPH at the alkaline range (8.5-8.7). NADPH, however, is the probable reactant in biological systems.

**Summary**, from NCBI Gene [644](https://www.ncbi.nlm.nih.gov/gene/644):

> The protein encoded by this gene belongs to the biliverdin reductase family, members of which catalyze the conversion of biliverdin to bilirubin in the presence of NADPH or NADH. Mutations in this gene are associated with hyperbiliverdinemia. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:1062](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1062) · Entrez [644](https://www.ncbi.nlm.nih.gov/gene/644) · UniProt [P53004](https://www.uniprot.org/uniprotkb/P53004) · Ensembl [ENSG00000106605](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106605)

## Data

Gene col 2780: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2780); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2780, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2780]; `tensor/DDL_lfc|DDL_z.npy` [2780]; `embed/gene_vectors.npy` [2780]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2780 or target_col == 2780). Every well: [[BLVRA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLVRA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
