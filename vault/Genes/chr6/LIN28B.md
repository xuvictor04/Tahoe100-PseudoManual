---
symbol: "LIN28B"
type: "gene"
col: 11946
ensembl_id: "ENSG00000187772"
name: "lin-28 RNA binding posttranscriptional regulator B"
location: "6q16.3-q21"
module: 9
arm: "+"
pooled_cpm: 9.78
n_lines_expressing: 19
n_dd_up: 43
n_dd_down: 4
n_dd_up_clean: 28
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 9
direction_downstream: 6
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# LIN28B

*lin-28 RNA binding posttranscriptional regulator B* — 6q16.3-q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.09× (z +15.4, q 0e+00, up in 4 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.657× (z -6.2, q 3e-07, down in 11 of 17 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFHX4]] (+0.59, fdr 2e-05), [[LINC02438]] (+0.58, fdr 1e-05), [[FUT9]] (+0.58, fdr 1e-05); moves opposite to [[TMEM50B]] (-0.42, fdr 2e-04), [[RMC1]] (-0.40, fdr 4e-04), [[ERP44]] (-0.40, fdr 4e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[CHIC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11946.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +15.4 | 0e+00 | 4/16 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +14.9 | 0e+00 | 1/15 (HepG2/C3A) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +10.3 | 2e-22 | 2/15 (HepG2/C3A, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.90×** | +9.5 | 2e-19 | 1/16 (J82) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +9.2 | 3e-18 | 2/12 (J82, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +8.8 | 2e-16 | 8/16 (NCI-H2347, A549, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +7.2 | 3e-11 | 10/17 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +7.2 | 3e-11 | 6/16 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +7.2 | 3e-11 | 7/17 (PANC-1, CHP-212, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +6.4 | 1e-08 | 8/17 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +5.6 | 1e-06 | 6/17 (A-427, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.0 | 2e-05 | 4/17 (PANC-1, NCI-H661, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.27×** | +5.0 | 2e-05 | 6/17 (CHP-212, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +4.9 | 3e-05 | 6/17 (A549, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.51×** | +4.3 | 5e-04 | 0/12 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.2 | 7e-04 | 2/16 (J82, PANC-1) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 1e-03 | 1/17 (J82) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.9 | 0.002 | 0/17 | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.006 | 5/17 (J82, A549, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.6 | 0.008 | 2/17 (A549, LOX-IMVI) | inconsistent across doses | low cells (technical?) |
| [[Sonidegib (drug)]] 5 µM |  | **1.61×** | +3.6 | 0.008 | 0/16 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.011 | 7/17 (NCI-H23, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11946.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.657×** | -6.2 | 3e-07 | 11/17 (C-33 A, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.690×** | -5.5 | 1e-05 | 9/17 (C-33 A, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.776×** | -3.8 | 0.031 | 0/17 | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.631×** | -3.5 | 0.069 | 1/17 (LOX-IMVI) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.859× | -3.2 | 0.15 | 3/17 (C-33 A, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | 0.812× | -3.1 | 0.19 | 8/17 (SHP-77, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.816× | -3.0 | 0.19 | 0/17 | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11946. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 119 | 0 | 6 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.100× (z -15.0) |
| [[LOX-IMVI (line)]] | wt | 57.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.200× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 24.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0977× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.343× (z -9.8) |
| [[SHP-77 (line)]] | alt | 40.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -12.1) |
| [[AN3 CA (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0370× (z -17.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 49.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -10.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 7.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 5.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 25.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -9.7) |
| [[A-172 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.947 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.935 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 300 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.996 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11946), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFHX4]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[LINC02438]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[FUT9]] | +0.58 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[MMRN1]] | +0.56 | +0.33 / +0.59 | both halves | 1e-04 |  |
| [[MIR99AHG]] | +0.53 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[FIGN]] | +0.52 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[CSMD3]] | +0.51 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[ANGPT1]] | +0.51 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[LINC02484]] | +0.51 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[CHMP1B2P]] | +0.51 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ZNF804A]] | +0.51 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[LINC00470]] | +0.51 | +0.31 / +0.53 | both halves | 2e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM50B]] | -0.42 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[RMC1]] | -0.40 | -0.27 / -0.25 | both halves | 4e-04 |  |
| [[ERP44]] | -0.40 | -0.25 / -0.31 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LIN28B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.2% of all compounds | 0.095 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCNH5]] | C | KCNH5 activity raises LIN28B's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 7.64× lower at baseline in the lines without KCNH5 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises LIN28B's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 3.74× lower at baseline in the lines without FUT9 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises LIN28B's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 2.63× lower at baseline in the lines without GABRG2 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[LINC02506]] | C | LINC02506 activity raises LIN28B's level | lines that do not express LINC02506 (40) vs lines expressing it (10) | 4.92× lower at baseline in the lines without LINC02506 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC01610, ENSG00000241168; co-absent with the target |
| [[LINC02008]] | C | LINC02008 activity raises LIN28B's level | lines that do not express LINC02008 (36) vs lines expressing it (14) | 3.72× lower at baseline in the lines without LINC02008 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01242, ENSG00000260126, ENSG00000253363; co-absent with the target |
| [[LINC02484]] | C | LINC02484 activity raises LIN28B's level | lines that do not express LINC02484 (40) vs lines expressing it (10) | 7.69× lower at baseline in the lines without LINC02484 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000260126, LINC02566, ENSG00000289605; co-absent with the target |
| [[MIR548XHG]] | C | MIR548XHG activity raises LIN28B's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 2.88× lower at baseline in the lines without MIR548XHG | 0.088 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises LIN28B's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.44× lower at baseline in the lines without RUNX1T1 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHIC1]] | B | LIN28B activity raises CHIC1's level | lines that do not express LIN28B (31) vs lines expressing it (19) | 1.59× lower at baseline in the lines without LIN28B | 0.042 | ⚠ within organs, on part of the lines; also absent: LRFN5, BARX1, KCNH7 |
| [[CHMP1B2P]] | C | LIN28B activity raises CHMP1B2P's level | lines that do not express LIN28B (31) vs lines expressing it (19) | 3.76× lower at baseline in the lines without LIN28B | 0.010 | ⚠ within organs, on part of the lines; also absent: LRFN5, BARX1, KCNH7; co-absent with the target |
| [[MIR548XHG]] | C | LIN28B activity raises MIR548XHG's level | lines that do not express LIN28B (31) vs lines expressing it (19) | 2.46× lower at baseline in the lines without LIN28B | 0.025 | ⚠ within organs, on part of the lines; also absent: LRFN5, BARX1, KCNH7; co-absent with the target |
| [[LINC00470]] | C | LIN28B activity raises LINC00470's level | lines that do not express LIN28B (31) vs lines expressing it (19) | 3.40× lower at baseline in the lines without LIN28B | 0.068 | ⚠ within organs, on part of the lines; also absent: LRFN5, BARX1, KCNH7; co-absent with the target |
| [[LINC02008]] | C | LIN28B activity raises LINC02008's level | lines that do not express LIN28B (31) vs lines expressing it (19) | 3.45× lower at baseline in the lines without LIN28B | 0.084 | ⚠ within organs, on part of the lines; also absent: LRFN5, BARX1, KCNH7; co-absent with the target |
| [[GABRG2]] | C | LIN28B activity raises GABRG2's level | lines that do not express LIN28B (31) vs lines expressing it (19) | 1.90× lower at baseline in the lines without LIN28B | 0.090 | ⚠ within organs, on part of the lines; also absent: LRFN5, BARX1, KCNH7; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.513). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.7, 32.6); signed map (38.9, 35.4). **Vector** length 44.9, 11.1% of its response variance represented; |z| ≥ 3 in 385 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +14.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +10.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +5.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | +1.8 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.3 | -6.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.2 | -5.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | lin-28 RNA binding posttranscriptional regulator B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.3-q21 — chr6:104,936,616-105,083,332 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ16517, CSDD2 |
| Gene groups (HGNC) | Zinc fingers CCHC-type; Cold shock domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZN17](https://www.uniprot.org/uniprotkb/Q6ZN17) (Protein lin-28 homolog B):

> Suppressor of microRNA (miRNA) biogenesis, including that of let-7 and possibly of miR107, miR-143 and miR-200c. Binds primary let-7 transcripts (pri-let-7), including pri-let-7g and pri-let-7a-1, and sequester them in the nucleolus, away from the microprocessor complex, hence preventing their processing into mature miRNA. Does not act on pri-miR21. The repression of let-7 expression is required for normal development and contributes to maintain the pluripotent state of embryonic stem cells by …

**Summary**, from NCBI Gene [389421](https://www.ncbi.nlm.nih.gov/gene/389421):

> The protein encoded by this gene belongs to the lin-28 family, which is characterized by the presence of a cold-shock domain and a pair of CCHC zinc finger domains. This gene is highly expressed in testis, fetal liver, placenta, and in primary human tumors and cancer cell lines. It is negatively regulated by microRNAs that target sites in the 3' UTR, and overexpression of this gene in primary tumors is linked to the repression of let-7 family of microRNAs and derepression of let-7 targets, …

**Accessions** — [HGNC:32207](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32207) · Entrez [389421](https://www.ncbi.nlm.nih.gov/gene/389421) · UniProt [Q6ZN17](https://www.uniprot.org/uniprotkb/Q6ZN17) · Ensembl [ENSG00000187772](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187772)

## Data

Gene col 11946: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11946); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11946, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11946]; `tensor/DDL_lfc|DDL_z.npy` [11946]; `embed/gene_vectors.npy` [11946]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11946 or target_col == 11946). Every well: [[LIN28B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIN28B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
