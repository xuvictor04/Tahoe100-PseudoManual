---
symbol: "CDK6-AS1"
type: "gene"
col: 14153
ensembl_id: "ENSG00000237819"
name: "CDK6 antisense RNA 1"
location: "7q21.2"
module: 80
arm: "+"
pooled_cpm: 2.15
n_lines_expressing: 44
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 8
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# CDK6-AS1

*CDK6 antisense RNA 1* — 7q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 13.6× (z +32.9, q 0e+00, up in 24 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.431× (z -7.5, q 3e-11, down in 19 of 37 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01829]] (+0.73, fdr 1e-05), [[WAKMAR2]] (+0.73, fdr 1e-05), [[ZNF341-AS1]] (+0.73, fdr 1e-05); moves opposite to [[PLA2G12A]] (-0.64, fdr 2e-05), [[IFT172]] (-0.64, fdr 3e-05), [[ALAD]] (-0.62, fdr 3e-04).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[ACTR3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14153.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **13.6×** | +32.9 | 0e+00 | 24/24 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.65×** | +11.1 | 5e-26 | 16/26 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.61×** | +11.0 | 8e-26 | 13/17 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.56×** | +10.9 | 2e-25 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.95×** | +8.4 | 6e-15 | 11/37 (A-172, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +7.7 | 2e-12 | 13/26 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +7.4 | 1e-11 | 1/4 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +6.6 | 2e-09 | 2/11 (SW480, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +5.7 | 6e-07 | 11/23 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +5.3 | 5e-06 | 2/8 (NCI-H460, A-172) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.71×** | +4.8 | 9e-05 | 9/34 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +4.3 | 7e-04 | 11/30 (A-172, HS-578T, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.27×** | +3.8 | 0.006 | 1/3 (NCI-H460) | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.012 | 1/16 (HOP62) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.016 | 4/28 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.030 | 6/36 (A-427, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.037 | 1/24 (SK-MEL-2) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.062 | 1/10 (J82) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14153.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.431×** | -7.5 | 3e-11 | 19/37 (LOX-IMVI, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.492×** | -6.3 | 6e-08 | 17/35 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.600×** | -4.6 | 9e-04 | 14/34 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.640×** | -4.0 | 0.009 | 8/38 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.742×** | -3.8 | 0.017 | 9/33 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.655×** | -3.5 | 0.042 | 7/36 (HepG2/C3A, J82, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 5 µM |  | 0.696× | -3.1 | 0.15 | 4/35 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.714× | -3.0 | 0.18 | 9/36 (RKO, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14153. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 3.33 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +12.3) | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0650× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 18.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0618× (z -15.1) |
| [[SW480 (line)]] | alt | 2.43 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.81× (z +11.6) | [[Thymol (drug)]] 0.5 µM 0.101× (z -8.7) |
| [[A-172 (line)]] | wt | 4.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +13.8) | — |
| [[A498 (line)]] | wt | 1.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 76.1× (z +15.9) | — |
| [[CFPAC-1 (line)]] | alt | 3.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.0× (z +14.8) | — |
| [[HEC-1-A (line)]] | alt | 0.672 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 31.1× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 5.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +11.8) | — |
| [[HS-578T (line)]] | alt | 1.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.9× (z +10.9) | — |
| [[J82 (line)]] | alt | 2.32 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.0350× (z -9.2) |
| [[LoVo (line)]] | wt | 1.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.9× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 2.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.0× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 1.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.4× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 1.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.9× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 1.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 1.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.0× (z +10.8) | — |
| [[A-427 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.953 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.903 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.627 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.722 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.584 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.785 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.956 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14153), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01829]] | +0.73 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[WAKMAR2]] | +0.73 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[ZNF341-AS1]] | +0.73 | +0.57 / +0.58 | both halves | 1e-05 | same gene group |
| [[PBLD]] | +0.72 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[CPEB2-DT]] | +0.72 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[CCDC26]] | +0.71 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[CIBAR1-DT]] | +0.70 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[DENND5B-AS1]] | +0.69 | +0.63 / +0.45 | both halves | 3e-05 | same gene group |
| [[LPXN]] | +0.69 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[LINC00393]] | +0.69 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[EFCAB5]] | +0.67 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[LINC00863]] | +0.67 | +0.58 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLA2G12A]] | -0.64 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[IFT172]] | -0.64 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[ALAD]] | -0.62 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[CAMK2G]] | -0.61 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[MAST3]] | -0.60 | -0.46 / -0.26 | both halves | 4e-04 |  |
| [[MPP1]] | -0.60 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[IQSEC2]] | -0.59 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[WRAP73]] | -0.59 | -0.38 / -0.37 | both halves | 9e-05 |  |
| [[RSAD1]] | -0.59 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[COMMD2]] | -0.58 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[CEP131]] | -0.58 | -0.37 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CDK6-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises CDK6-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CFAP58]] | B | CFAP58 activity raises CDK6-AS1's level | lines that do not express CFAP58 (6) vs lines expressing it (44) | 1.51× lower at baseline in the lines without CFAP58 | 0.068 | ⚠ within organs, on part of the lines; also absent: MINDY4, ENSG00000286162, MPP4; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACTR3-AS1]] | B | CDK6-AS1 activity raises ACTR3-AS1's level | lines that do not express CDK6-AS1 (6) vs lines expressing it (44) | 1.89× lower at baseline in the lines without CDK6-AS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: PLS3, CDK6, UACA; maybe low, not absent |
| [[POC1B-AS1]] | B | CDK6-AS1 activity raises POC1B-AS1's level | lines that do not express CDK6-AS1 (6) vs lines expressing it (44) | 1.53× lower at baseline in the lines without CDK6-AS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: PLS3, CDK6, UACA; maybe low, not absent |
| [[CCT6B]] | B | CDK6-AS1 activity raises CCT6B's level | lines that do not express CDK6-AS1 (6) vs lines expressing it (44) | 1.31× lower at baseline in the lines without CDK6-AS1 | 0.066 | ⚠ within organs, on part of the lines; also absent: PLS3, CDK6, UACA; maybe low, not absent |
| [[STARD13-AS]] | B | CDK6-AS1 activity raises STARD13-AS's level | lines that do not express CDK6-AS1 (6) vs lines expressing it (44) | 1.32× lower at baseline in the lines without CDK6-AS1 | 0.070 | ⚠ within organs, on part of the lines; also absent: PLS3, CDK6, UACA; maybe low, not absent |
| [[CFAP58]] | B | CDK6-AS1 activity raises CFAP58's level | lines that do not express CDK6-AS1 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without CDK6-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: PLS3, CDK6, UACA; maybe low, not absent |
| [[SMIM15-AS1]] | B | CDK6-AS1 activity raises SMIM15-AS1's level | lines that do not express CDK6-AS1 (6) vs lines expressing it (44) | 1.20× lower at baseline in the lines without CDK6-AS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: PLS3, CDK6, UACA; maybe low, not absent |
| [[LRRC37A3]] | B | CDK6-AS1 activity raises LRRC37A3's level | lines that do not express CDK6-AS1 (6) vs lines expressing it (44) | 1.32× lower at baseline in the lines without CDK6-AS1 | 0.090 | ⚠ within organs, on part of the lines; also absent: PLS3, CDK6, UACA; maybe low, not absent |
| [[HAS2]] | B | CDK6-AS1 activity raises HAS2's level | lines that do not express CDK6-AS1 (6) vs lines expressing it (44) | 4.02× lower at baseline in the lines without CDK6-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: PLS3, CDK6, UACA; maybe low, not absent |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.778). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.8, 11.8); signed map (22.2, -5.2). **Vector** length 56.7, 9.51% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +32.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +8.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +7.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +11.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +4.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +2.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.6 | -6.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.6 | -4.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.4 | -7.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.8 | -4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -3.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | CDK6 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q21.2 — chr7:92,836,367-92,917,188 (+) |
| Ensembl biotype | lncRNA |
| Also known as | BALR-2, AC002454.1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40141](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40141) · Entrez [101927497](https://www.ncbi.nlm.nih.gov/gene/101927497) · Ensembl [ENSG00000237819](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237819)

## Data

Gene col 14153: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14153); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14153, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14153]; `tensor/DDL_lfc|DDL_z.npy` [14153]; `embed/gene_vectors.npy` [14153]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14153 or target_col == 14153). Every well: [[CDK6-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK6-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
