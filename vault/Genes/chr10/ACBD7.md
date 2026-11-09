---
symbol: "ACBD7"
type: "gene"
col: 10700
ensembl_id: "ENSG00000176244"
name: "acyl-CoA binding domain containing 7"
location: "10p13"
module: 22
arm: "+"
pooled_cpm: 4.02
n_lines_expressing: 46
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 17
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# ACBD7

*acyl-CoA binding domain containing 7* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.72× (z +20.2, q 0e+00, up in 41 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.471× (z -8.0, q 1e-12, down in 24 of 41 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.670× (z -4.2, q 0.003, down in 9 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTTG1]] (+0.73, fdr 7e-06), [[NEK2]] (+0.73, fdr 7e-06), [[UBE2S]] (+0.71, fdr 7e-06); moves opposite to [[UQCC1]] (-0.54, fdr 4e-05), [[QRSL1]] (-0.54, fdr 6e-05), [[COA6]] (-0.53, fdr 9e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MAN1C1]] → it (grade B ⚠); 17 go from it, the strongest it → [[PIMREG]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10700.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **6.72×** | +20.2 | 0e+00 | 41/41 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.60×** | +20.0 | 0e+00 | 40/40 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.12×** | +15.0 | 0e+00 | 38/41 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.44×** | +13.4 | 1e-38 | 24/31 (SW1417, HOP62, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.46×** | +12.7 | 1e-34 | 8/8 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.14×** | +12.2 | 5e-32 | 13/15 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +11.8 | 4e-30 | 24/32 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.74×** | +10.7 | 8e-25 | 35/41 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.49×** | +9.0 | 2e-17 | 7/10 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +8.3 | 5e-15 | 23/40 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **2.05×** | +7.6 | 1e-12 | 11/20 (SW480, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +5.8 | 3e-07 | 13/36 (SK-MEL-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.8 | 9e-05 | 15/41 (MIA PaCa-2, HEC-1-A, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.31×** | +4.6 | 1e-04 | 12/37 (HT-29, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.003 | 8/40 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.46×** | +3.7 | 0.006 | 5/30 (J82, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.035 | 7/38 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10700.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.471×** | -8.0 | 1e-12 | 24/41 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.574×** | -5.5 | 8e-06 | 18/37 (SK-MEL-2, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.603×** | -5.3 | 2e-05 | 17/40 (HOP62, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.670×** | -4.2 | 0.003 | 9/38 (SW480, HT-29, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.902× | -3.8 | 0.016 | 11/43 (MIA PaCa-2, C-33 A, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.782×** | -3.7 | 0.024 | 9/41 (BT-474, SW 900, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.545×** | -3.4 | 0.064 | 7/28 (HT-29, SW480, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | 0.571× | -3.1 | 0.14 | 9/32 (PANC-1, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Gemfibrozil (drug)]] 5 µM |  | 0.817× | -3.0 | 0.15 | 6/40 (BT-474, LoVo, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.671× | -3.0 | 0.15 | 3/41 (AN3 CA, SW480, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10700. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.8 | 4 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.59× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.41× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.321× (z -8.5) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 1.83 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 13.1× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 4.92 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0516× (z -11.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 3.74 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0911× (z -8.7) ⚠ cell-cycle shift, explains ~23% of this change |
| [[PANC-1 (line)]] | alt | 3.75 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.140× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 7.31 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0835× (z -9.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SNU-423 (line)]] | alt | 3.21 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.05 µM 0.0587× (z -8.5) |
| [[SW1417 (line)]] | alt | 9.22 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.54× (z +9.2) | — |
| [[A-172 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.720 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10700), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTTG1]] | +0.73 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[NEK2]] | +0.73 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[UBE2S]] | +0.71 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[PIMREG]] | +0.69 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[KIF20A]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[NCAPD2]] | +0.69 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[CDKN3]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[PIF1]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[DLGAP5]] | +0.67 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[CDCA2]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[PRR11]] | +0.67 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[GPSM2]] | +0.67 | +0.49 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCC1]] | -0.54 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[QRSL1]] | -0.54 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[COA6]] | -0.53 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[DNAJC2]] | -0.52 | -0.43 / -0.45 | both halves | 4e-05 |  |
| [[SLC25A17]] | -0.51 | -0.41 / -0.39 | both halves | 5e-05 | pathway: Fatty acid metabolism |
| [[APTX]] | -0.50 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[SLC38A6]] | -0.50 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAN1C1]] | B | MAN1C1 activity raises ACBD7's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without MAN1C1 | 0.049 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[PIMREG]] | B | PIMREG activity raises ACBD7's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.79× lower at baseline in the lines without PIMREG | 0.063 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises ACBD7's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers ACBD7's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[RNF157]] | C | RNF157 activity raises ACBD7's level | lines that do not express RNF157 (3) vs lines expressing it (47) | 2.38× lower at baseline in the lines without RNF157 | 0.073 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF10L, TEX14, ARSG; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises ACBD7's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.62× lower at baseline in the lines without AURKB | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 0, C 17. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | C | ACBD7 activity raises PIMREG's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 2.78× lower at baseline in the lines without ACBD7 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[CENPF]] | C | ACBD7 activity raises CENPF's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 2.19× lower at baseline in the lines without ACBD7 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[AURKB]] | C | ACBD7 activity raises AURKB's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 2.05× lower at baseline in the lines without ACBD7 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[PTTG1]] | C | ACBD7 activity raises PTTG1's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without ACBD7 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[PSRC1]] | C | ACBD7 activity raises PSRC1's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without ACBD7 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[GAS2L3]] | C | ACBD7 activity raises GAS2L3's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.70× lower at baseline in the lines without ACBD7 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[FAM83D]] | C | ACBD7 activity raises FAM83D's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.68× lower at baseline in the lines without ACBD7 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[CDKN3]] | C | ACBD7 activity raises CDKN3's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.73× lower at baseline in the lines without ACBD7 | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent |
| [[CDCA8]] | C | ACBD7 activity raises CDCA8's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.56× lower at baseline in the lines without ACBD7 | 0.080 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent |
| [[PIF1]] | C | ACBD7 activity raises PIF1's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.92× lower at baseline in the lines without ACBD7 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[DLGAP5]] | C | ACBD7 activity raises DLGAP5's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.79× lower at baseline in the lines without ACBD7 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[NUF2]] | C | ACBD7 activity raises NUF2's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.65× lower at baseline in the lines without ACBD7 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.7, -58.2); signed map (-52.1, -41.1). **Vector** length 60.3, 9.55% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.50 to 60); *DREAM G2/M down* (control, mean cos +0.59 to 28); *mitotic spindle* (hallmark, mean cos +0.50 to 38).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +12.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +8.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +20.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.7 | +13.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.2 | +2.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.0 | +1.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.3 | -5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.6 | -5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA binding domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:15,075,475-15,088,776 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38219, bA455B2.2 |
| Reactome | 3 pathways, smallest: Mitochondrial Fatty Acid Beta-Oxidation; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6N7](https://www.uniprot.org/uniprotkb/Q8N6N7) (Acyl-CoA-binding domain-containing protein 7):

> Binds medium- and long-chain acyl-CoA esters.

**Summary**, from NCBI Gene [414149](https://www.ncbi.nlm.nih.gov/gene/414149):

> Predicted to enable fatty-acyl-CoA binding activity. Predicted to be involved in fatty acid metabolic process. Predicted to act upstream of or within several processes, including energy homeostasis; leptin-mediated signaling pathway; and response to food. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17715](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17715) · Entrez [414149](https://www.ncbi.nlm.nih.gov/gene/414149) · UniProt [Q8N6N7](https://www.uniprot.org/uniprotkb/Q8N6N7) · Ensembl [ENSG00000176244](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176244)

## Data

Gene col 10700: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10700); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10700, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10700]; `tensor/DDL_lfc|DDL_z.npy` [10700]; `embed/gene_vectors.npy` [10700]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10700 or target_col == 10700). Every well: [[ACBD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACBD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
