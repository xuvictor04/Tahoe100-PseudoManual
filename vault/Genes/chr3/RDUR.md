---
symbol: "RDUR"
type: "gene"
col: 13199
ensembl_id: "ENSG00000214407"
name: "RIG-I dependent antiviral response regulator RNA"
location: "3q12.3"
module: 116
arm: "+"
pooled_cpm: 7.96
n_lines_expressing: 22
n_dd_up: 43
n_dd_down: 20
n_dd_up_clean: 32
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 23
direction_downstream: 23
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# RDUR

*RIG-I dependent antiviral response regulator RNA* — 3q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.04× (z +15.7, q 0e+00, up in 9 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.558× (z -6.5, q 4e-08, down in 13 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01812]] (+0.76, fdr 7e-06), [[ZPLD1]] (+0.75, fdr 7e-06), [[MIR4280HG]] (+0.73, fdr 7e-06); moves opposite to [[MGP]] (-0.50, fdr 2e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[ENKUR]] → it (grade B ⚠); 23 go from it, the strongest it → [[ZPLD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13199.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.04×** | +15.7 | 0e+00 | 9/18 (HS-578T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.79×** | +14.5 | 6e-45 | 8/18 (hTERT-HPNE, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.44×** | +11.4 | 7e-28 | 1/6 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.04×** | +11.1 | 2e-26 | 14/18 (HT-29, hTERT-HPNE, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.99×** | +10.5 | 8e-24 | 1/5 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.89×** | +9.0 | 3e-17 | 11/18 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +8.8 | 1e-16 | 1/12 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.72×** | +7.7 | 1e-12 | 12/18 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.04×** | +7.1 | 7e-11 | 8/18 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +6.9 | 2e-10 | 7/18 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +6.2 | 3e-08 | 1/10 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.86×** | +6.2 | 3e-08 | 9/18 (RPMI-7951, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.26×** | +6.2 | 3e-08 | 11/18 (HOP62, SW 900, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.81×** | +5.9 | 1e-07 | 10/18 (HOP62, J82, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +5.6 | 8e-07 | 0/16 | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.64×** | +4.9 | 3e-05 | 8/18 (RKO, NCI-H2347, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.57×** | +4.3 | 4e-04 | 9/18 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.59×** | +4.3 | 6e-04 | 5/15 (RKO, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.004 | 6/16 (HOP62, SHP-77, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.45×** | +3.7 | 0.005 | 7/18 (HOP62, H4, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.006 | 6/15 (RPMI-7951, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13199.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.558×** | -6.5 | 4e-08 | 13/19 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.662×** | -5.1 | 8e-05 | 10/18 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.582×** | -5.0 | 1e-04 | 6/18 (RKO, HOP62, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.662×** | -4.9 | 1e-04 | 8/19 (RKO, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.623×** | -4.7 | 3e-04 | 7/19 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.628×** | -4.6 | 3e-04 | 9/18 (RKO, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.696×** | -4.3 | 0.001 | 10/18 (SK-MEL-2, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.657×** | -4.2 | 0.002 | 11/18 (RKO, HOP62, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.744×** | -4.2 | 0.002 | 9/18 (RKO, C32, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.664×** | -4.1 | 0.003 | 6/18 (LOX-IMVI, HOP62, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.658×** | -4.0 | 0.003 | 11/18 (RKO, LOX-IMVI, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.669×** | -4.0 | 0.003 | 8/18 (RKO, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.680×** | -3.8 | 0.005 | 11/19 (RKO, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.691×** | -3.7 | 0.009 | 5/18 (HOP62, H4, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.772×** | -3.6 | 0.014 | 5/18 (SK-MEL-2, RKO, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.703×** | -3.5 | 0.016 | 11/18 (H4, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13199. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 192 | 0 | 18 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0159× (z -29.0) |
| [[HOP62 (line)]] | alt | 30.1 | 0 | 5 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.122× (z -11.6) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.176× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 58.1 | 0 | 5 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0431× (z -16.0) |
| [[SK-MEL-2 (line)]] | alt | 48.0 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.100× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.153× (z -10.8) |
| [[H4 (line)]] | wt | 8.52 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0318× (z -9.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.0429× (z -8.8) |
| [[C32 (line)]] | wt | 9.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +11.4) | — |
| [[hTERT-HPNE (line)]] | wt | 3.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 57.3× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 2.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.9× (z +10.8) | — |
| [[A-172 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.850 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.823 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.759 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.683 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.750 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.682 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.863 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.967 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.981 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.700 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.715 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.701 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.794 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.09 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13199), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01812]] | +0.76 | +0.77 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ZPLD1]] | +0.75 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[MIR4280HG]] | +0.73 | +0.61 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ROBO4]] | +0.72 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[LINC02454]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[RPSAP52]] | +0.69 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[LINC01204]] | +0.69 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[FGF5]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[LINC00973]] | +0.67 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[SCHIP1]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[EVA1A]] | +0.66 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[RGS4]] | +0.66 | +0.57 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGP]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 3, C 20. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENKUR]] | B | ENKUR activity raises RDUR's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 2.05× lower at baseline in the lines without ENKUR | 0.062 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises RDUR's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers RDUR's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.0% of all compounds | 0.089 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01812]] | C | LINC01812 activity raises RDUR's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 4.50× lower at baseline in the lines without LINC01812 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622; co-absent with the target |
| [[RGS4]] | C | RGS4 activity raises RDUR's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 2.98× lower at baseline in the lines without RGS4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; co-absent with the target |
| [[LINC01592]] | C | LINC01592 activity raises RDUR's level | lines that do not express LINC01592 (35) vs lines expressing it (15) | 2.85× lower at baseline in the lines without LINC01592 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHRDL1, ESM1, CCL3; maybe low, not absent; co-absent with the target |
| [[LNCOG]] | C | LNCOG activity raises RDUR's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 3.35× lower at baseline in the lines without LNCOG | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1; co-absent with the target |
| [[CCDC190]] | C | CCDC190 activity raises RDUR's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 2.75× lower at baseline in the lines without CCDC190 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; co-absent with the target |
| [[DGKI]] | C | DGKI activity raises RDUR's level | lines that do not express DGKI (27) vs lines expressing it (23) | 2.95× lower at baseline in the lines without DGKI | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises RDUR's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.81× lower at baseline in the lines without FRMD4A | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[PDCD1LG2]] | C | PDCD1LG2 activity raises RDUR's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 2.47× lower at baseline in the lines without PDCD1LG2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L; co-absent with the target |
| [[ROBO4]] | C | ROBO4 activity raises RDUR's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.78× lower at baseline in the lines without ROBO4 | 0.018 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 10, C 13. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZPLD1]] | B | RDUR activity raises ZPLD1's level | lines that do not express RDUR (28) vs lines expressing it (22) | 2.44× lower at baseline in the lines without RDUR | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC |
| [[CA13]] | B | RDUR activity raises CA13's level | lines that do not express RDUR (28) vs lines expressing it (22) | 2.15× lower at baseline in the lines without RDUR | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC |
| [[KBTBD8]] | B | RDUR activity raises KBTBD8's level | lines that do not express RDUR (28) vs lines expressing it (22) | 1.94× lower at baseline in the lines without RDUR | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC |
| [[POU2F2]] | B | RDUR activity raises POU2F2's level | lines that do not express RDUR (28) vs lines expressing it (22) | 1.79× lower at baseline in the lines without RDUR | 0.055 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC |
| [[MGLL]] | B | RDUR activity raises MGLL's level | lines that do not express RDUR (28) vs lines expressing it (22) | 1.83× lower at baseline in the lines without RDUR | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC |
| [[PDE4DIPP2]] | B | RDUR activity raises PDE4DIPP2's level | lines that do not express RDUR (28) vs lines expressing it (22) | 2.47× lower at baseline in the lines without RDUR | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC |
| [[FMNL3]] | B | RDUR activity strengthens FMNL3's drug response | lines that do not express RDUR (23) vs lines expressing it (17) | the lines without RDUR respond 0.80× as strongly (z diff +0.81); strongest at Panobinostat 5 µM: 0.84x vs 0.47x (z diff +4.4) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC; target measured in part of the lines; artifact flags |
| [[RGMB]] | B | RDUR activity raises RGMB's level | lines that do not express RDUR (28) vs lines expressing it (22) | 1.98× lower at baseline in the lines without RDUR | 0.077 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC |
| [[ZNF697]] | B | RDUR activity raises ZNF697's level | lines that do not express RDUR (28) vs lines expressing it (22) | 2.08× lower at baseline in the lines without RDUR | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC |
| [[CD274]] | B | RDUR activity raises CD274's level | lines that do not express RDUR (28) vs lines expressing it (22) | 2.05× lower at baseline in the lines without RDUR | 0.085 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC |
| [[DGKI]] | C | RDUR activity raises DGKI's level | lines that do not express RDUR (28) vs lines expressing it (22) | 3.05× lower at baseline in the lines without RDUR | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC; co-absent with the target |
| [[SHANK1]] | C | RDUR activity raises SHANK1's level | lines that do not express RDUR (28) vs lines expressing it (22) | 3.16× lower at baseline in the lines without RDUR | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC; co-absent with the target |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.741). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.5, 11.2); signed map (15.6, 46.6). **Vector** length 73.6, 21.9% of its response variance represented; |z| ≥ 3 in 713 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +11.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +7.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +4.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.8 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -4.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.9 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | RIG-I dependent antiviral response regulator RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q12.3 — chr3:101,940,859-101,997,926 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LINC02085 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0VG73](https://www.uniprot.org/uniprotkb/Q0VG73) (Putative protein RDUR):

> Could play a role in innate immunity against viruses.

**Summary**, from NCBI Gene [152225](https://www.ncbi.nlm.nih.gov/gene/152225):

> Predicted to be involved in innate immune response. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27190](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27190) · Entrez [152225](https://www.ncbi.nlm.nih.gov/gene/152225) · UniProt [Q0VG73](https://www.uniprot.org/uniprotkb/Q0VG73) · Ensembl [ENSG00000214407](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214407)

## Data

Gene col 13199: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13199); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13199, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13199]; `tensor/DDL_lfc|DDL_z.npy` [13199]; `embed/gene_vectors.npy` [13199]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13199 or target_col == 13199). Every well: [[RDUR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RDUR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
