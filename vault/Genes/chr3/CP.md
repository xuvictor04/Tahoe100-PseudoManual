---
symbol: "CP"
type: "gene"
col: 516
ensembl_id: "ENSG00000047457"
name: "ceruloplasmin"
location: "3q24-q25.1"
module: 167
arm: "+"
pooled_cpm: 44.72
n_lines_expressing: 11
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 25
direction_downstream: 43
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# CP

*ceruloplasmin* — 3q24-q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.59× (z +8.5, q 8e-15, up in 1 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.65× (z +6.3, q 4e-08, up in 2 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.647× (z -5.5, q 2e-05, down in 9 of 9 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD38]] (+0.83, fdr 7e-06), [[FGA]] (+0.76, fdr 7e-06), [[IGFBP1]] (+0.69, fdr 7e-06); moves opposite to [[B4GALT6]] (-0.44, fdr 3e-05), [[ATP13A2]] (-0.44, fdr 4e-05), [[GALNT6]] (-0.43, fdr 6e-05).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[MX1]] → it (grade B ⚠); 43 go from it, the strongest it → [[FBXO39]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 516.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.59×** | +8.5 | 8e-15 | 1/10 (SW 1088) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +8.2 | 5e-14 | 1/8 (HepG2/C3A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.54×** | +7.7 | 2e-12 | 0/8 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +6.3 | 4e-08 | 2/10 (NCI-H1573, HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.78×** | +6.1 | 1e-07 | 8/9 (NCI-H1573, A549, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.25×** | +5.2 | 2e-05 | 7/9 (A498, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.59×** | +5.0 | 4e-05 | 8/9 (NCI-H1573, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.49×** | +4.9 | 7e-05 | 9/10 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.75×** | +4.8 | 1e-04 | 9/10 (NCI-H1573, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +4.2 | 0.002 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Alpelisib (drug)]] 5 µM |  | **2.43×** | +4.0 | 0.003 | 8/9 (NCI-H1573, A498, …) | top dose only | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.008 | 7/9 (SW 900, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.79×** | +3.7 | 0.009 | 5/9 (NCI-H1573, A498, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.009 | 8/10 (NCI-H1573, A549, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.010 | 7/8 (NCI-H1573, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.020 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.042 | 8/10 (NCI-H1573, A549, …) | two highest doses | cell-cycle shift (explains ~19% here); noisy plate (z scaled); position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.064 | 7/9 (SW 900, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.087 | 4/9 (A498, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 516.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.647×** | -5.5 | 2e-05 | 9/9 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.555×** | -5.3 | 4e-05 | 9/9 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.576×** | -4.9 | 1e-04 | 9/9 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.569×** | -4.9 | 2e-04 | 9/9 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.616×** | -4.3 | 0.002 | 7/9 (HepG2/C3A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.628×** | -4.2 | 0.003 | 8/9 (SNU-423, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.677×** | -3.5 | 0.038 | 4/9 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 516. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 558 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0400× (z -19.2) |
| [[A549 (line)]] | wt | 93.6 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0452× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 71.2 | 2 | 4 (2 ⚠) | [[Trametinib (drug)]] 0.5 µM 8.88× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -11.1) |
| [[SNU-423 (line)]] | alt | 62.1 | 0 | 5 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.101× (z -11.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.212× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 43.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0719× (z -16.2) |
| [[HepG2_C3A (line)]] | wt | 438 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0831× (z -19.2) |
| [[SW 900 (line)]] | alt | 38.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0703× (z -14.2) |
| [[A498 (line)]] | wt | 332 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -11.7) |
| [[A-172 (line)]] | wt | 4.82 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.62 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.55 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.89 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.64 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.15 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.31 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.85 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.08 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.62 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.69 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.70 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.27 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.55 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.69 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.41 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.65 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.71 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.73 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.45 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.81 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.65 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.01 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.47 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.61 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.79 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.30 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.02 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.49 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 516), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD38]] | +0.83 | +0.76 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[FGA]] | +0.76 | +0.68 / +0.78 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 559 |
| [[IGFBP1]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[TIMD4]] | +0.68 | +0.59 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[C1R]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT; STRING 401 |
| [[SLC16A7]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 | pathway: SLC-mediated transmembrane transport |
| [[RHEX]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[HAVCR1]] | +0.62 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ITIH2]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 | pathway: Post-translational protein phosphorylation; STRING 669 |
| [[CFH]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT; STRING 616 |
| [[C3]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT; STRING 751 |
| [[SAA2-SAA4]] | +0.61 | +0.48 / +0.65 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B4GALT6]] | -0.44 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[ATP13A2]] | -0.44 | -0.41 / -0.43 | both halves | 4e-05 | STRING 401 |
| [[GALNT6]] | -0.43 | -0.43 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 6, C 19. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MX1]] | B | MX1 activity raises CP's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.46× lower at baseline in the lines without MX1 | 0.041 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[TRIM22]] | B | TRIM22 activity raises CP's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.54× lower at baseline in the lines without TRIM22 | 0.049 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[HDAC6]] | B | HDAC6 activity raises CP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PIK3CA]] | B | PIK3CA activity lowers CP's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[TOP2A]] | B | TOP2A activity lowers CP's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GBP2]] | B | GBP2 activity raises CP's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.40× lower at baseline in the lines without GBP2 | 0.095 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[ITIH2]] | C | ITIH2 activity raises CP's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 6.54× lower at baseline in the lines without ITIH2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; co-absent with the target |
| [[DSCAML1]] | C | DSCAML1 activity raises CP's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 4.20× lower at baseline in the lines without DSCAML1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG; co-absent with the target |
| [[C3]] | C | C3 activity raises CP's level | lines that do not express C3 (32) vs lines expressing it (18) | 4.42× lower at baseline in the lines without C3 | 0.013 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11; co-absent with the target |
| [[FGA]] | C | FGA activity raises CP's level | lines that do not express FGA (43) vs lines expressing it (7) | 6.18× lower at baseline in the lines without FGA | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[FGB]] | C | FGB activity raises CP's level | lines that do not express FGB (42) vs lines expressing it (8) | 4.94× lower at baseline in the lines without FGB | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2; co-absent with the target |
| [[RHEX]] | C | RHEX activity raises CP's level | lines that do not express RHEX (43) vs lines expressing it (7) | 7.54× lower at baseline in the lines without RHEX | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB; co-absent with the target |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 18, C 25. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO39]] | B | CP activity raises FBXO39's level | lines that do not express CP (39) vs lines expressing it (11) | 2.25× lower at baseline in the lines without CP | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[ODF3B]] | B | CP activity raises ODF3B's level | lines that do not express CP (39) vs lines expressing it (11) | 2.28× lower at baseline in the lines without CP | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[GBP2]] | B | CP activity raises GBP2's level | lines that do not express CP (39) vs lines expressing it (11) | 2.96× lower at baseline in the lines without CP | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[TYMP]] | B | CP activity raises TYMP's level | lines that do not express CP (39) vs lines expressing it (11) | 3.91× lower at baseline in the lines without CP | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[SOD2]] | B | CP activity raises SOD2's level | lines that do not express CP (39) vs lines expressing it (11) | 3.15× lower at baseline in the lines without CP | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[NAMPT]] | B | CP activity raises NAMPT's level | lines that do not express CP (39) vs lines expressing it (11) | 2.29× lower at baseline in the lines without CP | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[FTH1]] | B | CP activity raises FTH1's level | lines that do not express CP (39) vs lines expressing it (11) | 2.04× lower at baseline in the lines without CP | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[MX1]] | B | CP activity raises MX1's level | lines that do not express CP (39) vs lines expressing it (11) | 3.25× lower at baseline in the lines without CP | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[RBPMS]] | B | CP activity raises RBPMS's level | lines that do not express CP (39) vs lines expressing it (11) | 2.55× lower at baseline in the lines without CP | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[ABCC6]] | B | CP activity raises ABCC6's level | lines that do not express CP (39) vs lines expressing it (11) | 1.84× lower at baseline in the lines without CP | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[CFB]] | B | CP activity raises CFB's level | lines that do not express CP (39) vs lines expressing it (11) | 3.69× lower at baseline in the lines without CP | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[TYMP]] | B | CP activity strengthens TYMP's drug response | lines that do not express CP (20) vs lines expressing it (9) | the lines without CP respond 0.60× as strongly (z diff +2.42); strongest at Panobinostat 5 µM: 0.61x vs 0.27x (z diff +4.5) | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.788). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.0, 44.7); signed map (52.0, 26.4). **Vector** length 68.4, 33.1% of its response variance represented; |z| ≥ 3 in 434 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +8.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.6 | +3.7 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.8 | -1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.7 | +0.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ceruloplasmin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q24-q25.1 — chr3:149,162,410-149,221,829 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AB073614 |
| Gene groups (HGNC) | Multicopper ferroxidase family |
| Hallmark sets | COMPLEMENT, HYPOXIA |
| Reactome | 8 pathways, smallest: Metal ion SLC transporters; Iron uptake and transport; SLC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [P00450](https://www.uniprot.org/uniprotkb/P00450) (Ceruloplasmin):

> Multifunctional blue, copper-binding (6-7 atoms per molecule) glycoprotein. It has ferroxidase activity oxidizing Fe(2+) to Fe(3+) without releasing radical oxygen species. It is involved in iron transport across the cell membrane. Copper ions provide a large number of enzymatic activities. Oxidizes highly toxic ferrous ions to the ferric state for further incorporation onto apo-transferrins, catalyzes Cu(+) oxidation and promotes the oxidation of biogenic amines such as norepinephrin and …

**Summary**, from NCBI Gene [1356](https://www.ncbi.nlm.nih.gov/gene/1356):

> The protein encoded by this gene is a metalloprotein that binds most of the copper in plasma and is involved in the peroxidation of Fe(II)transferrin to Fe(III) transferrin. Mutations in this gene cause aceruloplasminemia, which results in iron accumulation and tissue damage, and is associated with diabetes and neurologic abnormalities. Two transcript variants, one protein-coding and the other not protein-coding, have been found for this gene. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:2295](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2295) · Entrez [1356](https://www.ncbi.nlm.nih.gov/gene/1356) · UniProt [P00450](https://www.uniprot.org/uniprotkb/P00450) · Ensembl [ENSG00000047457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047457)

## Data

Gene col 516: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 516); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 516, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 516]; `tensor/DDL_lfc|DDL_z.npy` [516]; `embed/gene_vectors.npy` [516]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 516 or target_col == 516). Every well: [[CP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
