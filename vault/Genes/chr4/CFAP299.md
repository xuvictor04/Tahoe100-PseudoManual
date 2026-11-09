---
symbol: "CFAP299"
type: "gene"
col: 12472
ensembl_id: "ENSG00000197826"
name: "cilia and flagella associated protein 299"
location: "4q21.21"
module: 116
arm: "+"
pooled_cpm: 18.56
n_lines_expressing: 23
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 9
direction_downstream: 12
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# CFAP299

*cilia and flagella associated protein 299* — 4q21.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 16.2× (z +28.7, q 0e+00, up in 18 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Dihydroartemisinin (drug)]] 5 µM: 0.670× (z -4.2, q 0.018, down in 5 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANAPC1P4]] (+0.62, fdr 1e-05), [[FGF5]] (+0.62, fdr 1e-05, ⚠ same locus), [[MIR4435-2HG]] (+0.61, fdr 1e-05), [[NTNG1]] (+0.61, fdr 3e-05); moves opposite to [[KCTD7]] (-0.53, fdr 3e-05), [[ANAPC4]] (-0.53, fdr 1e-05), [[ARNT]] (-0.52, fdr 2e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → [[ITGA6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12472.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **16.2×** | +28.7 | 0e+00 | 18/20 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **10.5×** | +24.3 | 0e+00 | 18/20 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **8.81×** | +22.5 | 0e+00 | 17/20 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.02×** | +20.3 | 0e+00 | 19/21 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.60×** | +18.7 | 0e+00 | 15/20 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.15×** | +13.7 | 2e-40 | 18/20 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.47×** | +9.3 | 9e-19 | 15/20 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.43×** | +9.1 | 4e-18 | 15/18 (SHP-77, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **5.12×** | +8.8 | 8e-17 | 16/21 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.29×** | +8.6 | 6e-16 | 7/17 (SW 900, C32, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +8.2 | 9e-15 | 10/21 (SHP-77, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.16×** | +7.6 | 1e-12 | 14/20 (LOX-IMVI, PANC-1, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.04×** | +7.1 | 6e-11 | 4/13 (RPMI-7951, H4, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +7.0 | 1e-10 | 6/16 (SW 900, HOP62, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.3 | 9e-09 | 11/21 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.84×** | +6.3 | 1e-08 | 6/20 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +6.1 | 4e-08 | 12/19 (HOP62, HS-578T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +5.2 | 5e-06 | 5/19 (HS-578T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~20% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12472.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.670×** | -4.2 | 0.018 | 5/20 (C32, NCI-H23, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.689×** | -3.9 | 0.031 | 6/20 (LOX-IMVI, H4, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.716×** | -3.5 | 0.090 | 9/20 (RKO, NCI-H2030, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.720×** | -3.4 | 0.090 | 9/20 (MIA PaCa-2, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.807× | -3.2 | 0.17 | 11/21 (PANC-1, SHP-77, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12472. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 5.86 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 51.3× (z +13.0) | [[Dihydroartemisinin (drug)]] 5 µM 0.0460× (z -10.2) |
| [[A498 (line)]] | wt | 7.32 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 36.7× (z +15.6) | — |
| [[HOP62 (line)]] | alt | 19.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 16.8× (z +14.8) | — |
| [[HS-578T (line)]] | alt | 24.6 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 10.6× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 14.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.83× (z +13.7) | — |
| [[NCI-H2030 (line)]] | alt | 7.24 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 26.5× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 6.06 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.99× (z +12.6) | — |
| [[PANC-1 (line)]] | alt | 7.15 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 29.2× (z +16.0) | — |
| [[RPMI-7951 (line)]] | alt | 14.0 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 26.6× (z +12.6) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0858× (z -9.0) |
| [[A-172 (line)]] | wt | 18.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 12.1× (z +11.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 314 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 32.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.6× (z +10.9) | — |
| [[SHP-77 (line)]] | alt | 6.89 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 31.4× (z +10.8) | — |
| [[SW 900 (line)]] | alt | 7.86 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 48.0× (z +13.0) | — |
| [[H4 (line)]] | wt | 23.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 14.8× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 69.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.8× (z +21.0) | — |
| [[RKO (line)]] | wt | 97.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +9.0) | [[Selinexor (drug)]] 5 µM 0.332× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 99.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.55× (z +8.7) | — |
| [[A-427 (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.61 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.47 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.32 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12472), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC1P4]] | +0.62 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[FGF5]] | +0.62 | +0.49 / +0.68 | both halves | 1e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[MIR4435-2HG]] | +0.61 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[NTNG1]] | +0.61 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[LTBP2]] | +0.58 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[FMN2]] | +0.57 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[NAV3]] | +0.57 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[BACH1]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[RGS4]] | +0.56 | +0.38 / +0.62 | both halves | 7e-05 |  |
| [[LINC02516]] | +0.56 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[SLIT2]] | +0.56 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ABR]] | +0.55 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[LRRIQ1]] | +0.55 | +0.69 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD7]] | -0.53 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[ANAPC4]] | -0.53 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ARNT]] | -0.52 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[PRKRA]] | -0.52 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.52 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[MAPKAPK5-AS1]] | -0.51 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[TSC22D3]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TADA1]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ZNF449]] | -0.50 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[CRLS1]] | -0.49 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[ALG9]] | -0.49 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[SLC35D1]] | -0.49 | -0.38 / -0.47 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CFAP299's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02516]] | B | LINC02516 activity raises CFAP299's level | lines that do not express LINC02516 (19) vs lines expressing it (31) | 2.29× lower at baseline in the lines without LINC02516 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADAM23, TEK, SPOCK3 |
| [[ITGA6]] | B | ITGA6 activity lowers CFAP299's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 2.73× higher at baseline in the lines without ITGA6 | 0.098 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FGF5]] | C | FGF5 activity raises CFAP299's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 4.44× lower at baseline in the lines without FGF5 | 4e-04 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702; co-absent with the target |
| [[ROBO4]] | C | ROBO4 activity raises CFAP299's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 3.43× lower at baseline in the lines without ROBO4 | 0.003 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1; co-absent with the target |
| [[CCDC190]] | C | CCDC190 activity raises CFAP299's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 3.03× lower at baseline in the lines without CCDC190 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; co-absent with the target |
| [[RGS4]] | C | RGS4 activity raises CFAP299's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 2.83× lower at baseline in the lines without RGS4 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; co-absent with the target |
| [[ADTRP]] | C | ADTRP activity raises CFAP299's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 3.19× lower at baseline in the lines without ADTRP | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2; co-absent with the target |
| [[DSCAM]] | C | DSCAM activity raises CFAP299's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 1.80× lower at baseline in the lines without DSCAM | 0.065 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA6]] | B | CFAP299 activity lowers ITGA6's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 2.65× higher at baseline in the lines without CFAP299 | 0.016 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2 |
| [[ITPR2-AS1]] | B | CFAP299 activity raises ITPR2-AS1's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 1.46× lower at baseline in the lines without CFAP299 | 0.023 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2 |
| [[LINC02516]] | B | CFAP299 activity raises LINC02516's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 1.59× lower at baseline in the lines without CFAP299 | 0.024 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2 |
| [[KBTBD8]] | B | CFAP299 activity raises KBTBD8's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 1.60× lower at baseline in the lines without CFAP299 | 0.026 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2 |
| [[CD44]] | B | CFAP299 activity raises CD44's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 3.23× lower at baseline in the lines without CFAP299 | 0.050 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2 |
| [[LTBP2]] | B | CFAP299 activity raises LTBP2's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 1.96× lower at baseline in the lines without CFAP299 | 0.063 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2 |
| [[NRXN3]] | B | CFAP299 activity lowers NRXN3's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 1.19× higher at baseline in the lines without CFAP299 | 0.068 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2 |
| [[ITPR2]] | B | CFAP299 activity raises ITPR2's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 1.56× lower at baseline in the lines without CFAP299 | 0.090 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2 |
| [[FGF5]] | C | CFAP299 activity raises FGF5's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 6.31× lower at baseline in the lines without CFAP299 | 3e-04 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2; co-absent with the target |
| [[RGS4]] | C | CFAP299 activity raises RGS4's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 2.44× lower at baseline in the lines without CFAP299 | 0.024 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2; co-absent with the target |
| [[CDH2]] | C | CFAP299 activity raises CDH2's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 5.27× lower at baseline in the lines without CFAP299 | 0.052 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2; co-absent with the target |
| [[LINC01592]] | C | CFAP299 activity raises LINC01592's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 1.61× lower at baseline in the lines without CFAP299 | 0.053 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2; co-absent with the target |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.2, 12.9); signed map (17.4, 45.2). **Vector** length 60.9, 15.7% of its response variance represented; |z| ≥ 3 in 600 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +20.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.1 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +5.0 | +8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +6.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +8.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.0 | +2.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.8 | +0.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.6 | -3.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -1.8 | -2.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 299 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.21 — chr4:80,335,730-80,963,750 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C4orf22 |
| Gene groups (HGNC) | Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6V702](https://www.uniprot.org/uniprotkb/Q6V702) (Cilia- and flagella-associated protein 299):

> May be involved in spermatogenesis.

**Summary**, from NCBI Gene [255119](https://www.ncbi.nlm.nih.gov/gene/255119):

> Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28554) · Entrez [255119](https://www.ncbi.nlm.nih.gov/gene/255119) · UniProt [Q6V702](https://www.uniprot.org/uniprotkb/Q6V702) · Ensembl [ENSG00000197826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197826)

## Data

Gene col 12472: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12472); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12472, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12472]; `tensor/DDL_lfc|DDL_z.npy` [12472]; `embed/gene_vectors.npy` [12472]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12472 or target_col == 12472). Every well: [[CFAP299 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP299.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
