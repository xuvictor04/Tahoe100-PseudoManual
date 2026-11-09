---
symbol: "RHCE"
type: "gene"
col: 12037
ensembl_id: "ENSG00000188672"
name: "Rh blood group CcEe antigens"
location: "1p36.11"
module: 179
arm: "+"
pooled_cpm: 3.1
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 20
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# RHCE

*Rh blood group CcEe antigens* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.14× (z +27.8, q 0e+00, up in 35 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.313× (z -11.6, q 4e-28, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLT1B]] (+0.65, fdr 2e-05), [[CFAP20DC-AS1]] (+0.64, fdr 1e-05), [[CATSPER2P1]] (+0.64, fdr 4e-05); moves opposite to [[CHIC1]] (-0.55, fdr 3e-05), [[ATXN7L1]] (-0.54, fdr 3e-05), [[ZNF480]] (-0.54, fdr 2e-04).
> It sits in the **+** arm of [[Module 179]] (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12037.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.14×** | +27.8 | 0e+00 | 35/35 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.69×** | +9.5 | 5e-19 | 15/30 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +7.4 | 2e-11 | 3/8 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +7.2 | 6e-11 | 22/43 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +7.2 | 6e-11 | 1/5 (PANC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +7.1 | 1e-10 | 18/36 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.89×** | +6.4 | 1e-08 | 19/44 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +3.7 | 0.013 | 8/44 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.015 | 15/43 (A-427, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.60×** | +3.4 | 0.045 | 1/9 (PANC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.065 | 6/41 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.35× | +3.0 | 0.12 | 8/41 (SW480, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12037.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.313×** | -11.6 | 4e-28 | 34/45 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.355×** | -10.3 | 2e-22 | 23/28 (HOP62, A-427, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.379×** | -9.3 | 3e-18 | 25/39 (HOP62, NCI-H2030, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.399×** | -9.2 | 7e-18 | 24/42 (NCI-H23, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.436×** | -8.3 | 2e-14 | 24/34 (PANC-1, HS-578T, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.454×** | -7.9 | 3e-13 | 21/43 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.590×** | -7.4 | 9e-12 | 24/37 (HOP62, J82, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.486×** | -7.2 | 5e-11 | 23/41 (NCI-H2030, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.533×** | -6.3 | 2e-08 | 16/44 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.407×** | -4.7 | 2e-04 | 13/34 (HOP62, NCI-H23, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.609×** | -4.7 | 2e-04 | 16/43 (NCI-H23, HS-578T, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.649×** | -4.1 | 0.002 | 12/22 (HOP62, Hs 766T, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.677×** | -3.9 | 0.005 | 11/44 (MIA PaCa-2, SHP-77, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.696×** | -3.6 | 0.013 | 14/43 (HOP62, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.515×** | -3.5 | 0.021 | 9/27 (NCI-H1573, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Mifepristone (drug)]] 5 µM |  | **0.705×** | -3.3 | 0.028 | 8/42 (A549, SW 900, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.722×** | -3.2 | 0.038 | 14/42 (HOP62, C32, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.734×** | -3.1 | 0.065 | 4/45 (LoVo, H4, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.558×** | -3.0 | 0.068 | 8/38 (CFPAC-1, A-427, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12037. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 6.38 | 1 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.85× (z +11.6) | [[Digitoxin (drug)]] 5 µM 0.0393× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -9.4) |
| [[SW480 (line)]] | alt | 2.15 | 3 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.6× (z +14.8) | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0552× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 3.14 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.88× (z +11.1) | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0727× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 2.05 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.9× (z +11.4) | — |
| [[HS-578T (line)]] | alt | 7.20 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.30× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.0490× (z -11.7) |
| [[J82 (line)]] | alt | 3.16 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -9.8) ⚠ cell-cycle shift, explains ~77% of this change |
| [[NCI-H460 (line)]] | wt | 1.79 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.40× (z +10.8) | [[Busulfan (drug)]] 0.5 µM 0.0801× (z -8.6) |
| [[PANC-1 (line)]] | alt | 3.58 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.64× (z +10.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.0283× (z -15.2) |
| [[A-172 (line)]] | wt | 2.65 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0953× (z -9.2) ⚠ cell-cycle shift, explains ~77% of this change |
| [[KATO III (line)]] | alt | 2.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.16× (z +8.6) | — |
| [[LoVo (line)]] | wt | 3.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +11.4) | — |
| [[LS 180 (line)]] | wt | 1.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.1× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 3.29 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0523× (z -10.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 7.07 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0807× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 4.98 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0407× (z -9.9) |
| [[SNU-423 (line)]] | alt | 2.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.42× (z +8.5) | — |
| [[A-427 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.979 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12037), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLT1B]] | +0.65 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[CFAP20DC-AS1]] | +0.64 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[CATSPER2P1]] | +0.64 | +0.42 / +0.75 | both halves | 4e-05 |  |
| [[CATSPER2P1-1]] | +0.63 | +0.38 / +0.74 | both halves | 6e-05 |  |
| [[C12orf73]] | +0.61 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[ZNF710-AS1]] | +0.60 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[ING2-DT]] | +0.60 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[TMEM165]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[EOGT-DT]] | +0.59 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[HRG-AS1]] | +0.58 | +0.38 / +0.60 | both halves | 6e-05 |  |
| [[ZFC3H1]] | +0.58 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[CDC20-DT]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHIC1]] | -0.55 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[ATXN7L1]] | -0.54 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[ZNF480]] | -0.54 | -0.32 / -0.62 | both halves | 2e-04 |  |
| [[FOXRED2]] | -0.54 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[INTS7]] | -0.54 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[CRADD]] | -0.53 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[CEP295]] | -0.53 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[SERBP1]] | -0.52 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ZFP36L2]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ZNF260]] | -0.51 | -0.29 / -0.66 | both halves | 2e-04 |  |
| [[REPIN1]] | -0.51 | -0.34 / -0.61 | both halves | 1e-04 |  |
| [[RTL6]] | -0.51 | -0.36 / -0.55 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RHCE's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **+** arm (projection on the module's main direction 0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (3.6, 23.8); signed map (33.9, -4.1). **Vector** length 65.1, 10.2% of its response variance represented; |z| ≥ 3 in 1,133 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +27.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +7.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +7.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | -0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | -0.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | -0.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.3 | -9.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -11.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -8.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -4.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | Rh blood group CcEe antigens |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:25,362,249-25,430,192 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD240CE, SLC42A4; previously RH |
| Gene groups (HGNC) | Blood group antigens; CD molecules; Solute carrier family 42 |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 2 pathways, smallest: Blood group systems biosynthesis; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P18577](https://www.uniprot.org/uniprotkb/P18577) (Blood group Rh(CE) polypeptide):

> Component of the ankyrin-1 complex, a multiprotein complex involved in the stability and shape of the erythrocyte membrane. Mediates the primary membrane attachment site for ANK1 when associated with RHAG. May participate in the ammonium and carbon dioxide transport through the heterotrimer form (Probable).

**Summary**, from NCBI Gene [6006](https://www.ncbi.nlm.nih.gov/gene/6006):

> The Rh blood group system is the second most clinically significant of the blood groups, second only to ABO. It is also the most polymorphic of the blood groups, with variations due to deletions, gene conversions, and missense mutations. The Rh blood group includes this gene which encodes both the RhC and RhE antigens on a single polypeptide and a second gene which encodes the RhD protein. The classification of Rh-positive and Rh-negative individuals is determined by the presence or absence of …

**Accessions** — [HGNC:10008](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10008) · Entrez [6006](https://www.ncbi.nlm.nih.gov/gene/6006) · UniProt [P18577](https://www.uniprot.org/uniprotkb/P18577) · Ensembl [ENSG00000188672](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188672)

## Data

Gene col 12037: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12037); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12037, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12037]; `tensor/DDL_lfc|DDL_z.npy` [12037]; `embed/gene_vectors.npy` [12037]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12037 or target_col == 12037). Every well: [[RHCE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHCE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
