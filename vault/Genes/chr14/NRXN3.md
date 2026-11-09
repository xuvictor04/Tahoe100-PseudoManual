---
symbol: "NRXN3"
type: "gene"
col: 328
ensembl_id: "ENSG00000021645"
name: "neurexin 3"
location: "14q24.3-q31.1"
module: 19
arm: "+"
pooled_cpm: 54.69
n_lines_expressing: 27
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 8
direction_downstream: 9
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# NRXN3

*neurexin 3* — 14q24.3-q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.31× (z +34.4, q 0e+00, up in 25 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.708× (z -5.8, q 4e-06, down in 12 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTN1]] (+0.66, fdr 7e-06), [[UNC5D]] (+0.63, fdr 1e-05), [[NCAM1]] (+0.63, fdr 1e-05); moves opposite to [[ORAI3]] (-0.49, fdr 1e-04), [[FAM185A]] (-0.46, fdr 5e-04), [[TCEANC2]] (-0.45, fdr 2e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[XACT]] → it (grade B ⚠); 9 go from it, the strongest it → [[EBF2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 328.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.31×** | +34.4 | 0e+00 | 25/25 (SW480, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +23.4 | 0e+00 | 13/25 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +17.1 | 0e+00 | 18/25 (SNU-423, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.76×** | +16.9 | 0e+00 | 24/25 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.55×** | +15.6 | 0e+00 | 23/25 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.54×** | +15.5 | 0e+00 | 21/25 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +14.5 | 1e-45 | 9/24 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.11×** | +12.4 | 1e-33 | 22/25 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +12.1 | 6e-32 | 10/22 (H4, SW1417, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +11.6 | 1e-29 | 8/23 (NCI-H2030, SW1417, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +11.6 | 1e-29 | 20/25 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.93×** | +10.9 | 5e-26 | 8/25 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +8.6 | 5e-16 | 6/26 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +6.1 | 4e-08 | 6/25 (HOP62, BT-474, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.97×** | +5.9 | 1e-07 | 19/25 (NCI-H23, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +5.3 | 4e-06 | 13/25 (SNU-423, HS-578T, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.001 | 1/25 (A498) | rises with dose | position effect removed |
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | 1.19× | +4.0 | 0.002 | 4/25 (NCI-H2030, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 328.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.708×** | -5.8 | 4e-06 | 12/24 (H4, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.729×** | -5.3 | 4e-05 | 13/25 (NCI-H1573, SW 1088, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.836× | -4.2 | 0.004 | 16/25 (J82, A549, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.784×** | -3.9 | 0.013 | 9/24 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.850× | -3.8 | 0.014 | 11/25 (A498, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.816×** | -3.4 | 0.061 | 10/25 (H4, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.819×** | -3.3 | 0.064 | 15/25 (J82, NCI-H1573, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.820×** | -3.3 | 0.064 | 9/25 (NCI-H1573, CFPAC-1, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.688×** | -3.3 | 0.069 | 8/25 (LS 180, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.820×** | -3.2 | 0.080 | 14/24 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.831× | -3.1 | 0.10 | 10/25 (A549, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 328. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 289 | 2 (1 ⚠) | 7 (5 ⚠) | [[Selinexor (drug)]] 5 µM 2.47× (z +10.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 2.26× (z +8.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 107 | 1 | 7 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.64× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Triamcinolone (drug)]] 0.5 µM 0.248× (z -9.7) |
| [[SNU-423 (line)]] | alt | 84.5 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +23.2) | — |
| [[SW480 (line)]] | alt | 14.7 | 8 | 0 | [[Tucidinostat (drug)]] 5 µM 19.2× (z +30.0) | — |
| [[C32 (line)]] | wt | 75.0 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 7.25× (z +14.5) | — |
| [[HOP62 (line)]] | alt | 19.3 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 4.84× (z +13.0) | — |
| [[LoVo (line)]] | wt | 168 | 4 (1 ⚠) | 1 (1 ⚠) | [[Binimetinib (drug)]] 5 µM 2.68× (z +9.3) | [[Harringtonine (drug)]] 0.5 µM 0.367× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 421 | 2 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.25× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.181× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 22.9 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 8.56× (z +15.6) | — |
| [[A549 (line)]] | wt | 63.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.160× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 0.166× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 17.8 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 13.2× (z +18.0) | — |
| [[H4 (line)]] | wt | 103 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0664× (z -13.2) |
| [[HS-578T (line)]] | alt | 43.9 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 5.50× (z +16.4) | — |
| [[SHP-77 (line)]] | alt | 16.4 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 10.5× (z +14.5) | — |
| [[SW1417 (line)]] | alt | 18.6 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 13.1× (z +16.6) | — |
| [[A498 (line)]] | wt | 18.8 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.67× (z +11.5) | — |
| [[BT-474 (line)]] | alt | 61.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +14.4) | — |
| [[CFPAC-1 (line)]] | alt | 17.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.37× (z +9.4) | — |
| [[SW 1088 (line)]] | alt | 1,061 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -11.8) |
| [[A-172 (line)]] | wt | 29.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +14.8) | — |
| [[J82 (line)]] | alt | 157 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 138 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.244× (z -9.7) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 141 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.08× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 16.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.80× (z +11.8) | — |
| [[AN3 CA (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.60 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.42 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.50 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.28 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.12 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.45 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.80 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.35 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.02 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.11 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.96 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.63 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.74 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.56 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 328), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTN1]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[UNC5D]] | +0.63 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[NCAM1]] | +0.63 | +0.49 / +0.56 | both halves | 1e-05 | STRING 538 |
| [[NTRK3]] | +0.57 | +0.59 / +0.58 | both halves | 7e-06 | pathway: Neuronal System |
| [[NCAM2]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ELOVL2]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[RAB3C]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PDE1C]] | +0.55 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[FSTL5]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[FREM2]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CA8]] | +0.54 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[ERBB4]] | +0.54 | +0.56 / +0.52 | both halves | 1e-05 | pathway: Neuronal System |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORAI3]] | -0.49 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[FAM185A]] | -0.46 | -0.23 / -0.43 | both halves | 5e-04 |  |
| [[TCEANC2]] | -0.45 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[ZNF343]] | -0.44 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[WASH2P-1]] | -0.44 | -0.25 / -0.40 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XACT]] | B | XACT activity raises NRXN3's level | lines that do not express XACT (30) vs lines expressing it (20) | 2.90× lower at baseline in the lines without XACT | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438 |
| [[KLHL13]] | B | KLHL13 activity raises NRXN3's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 2.45× lower at baseline in the lines without KLHL13 | 0.013 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4 |
| [[EBF2]] | B | EBF2 activity raises NRXN3's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 2.71× lower at baseline in the lines without EBF2 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[ATP1A3]] | B | ATP1A3 activity lowers NRXN3's level | lines that do not express ATP1A3 (12) vs lines expressing it (38) | 1.57× higher at baseline in the lines without ATP1A3 | 0.057 | ⚠ within organs, on part of the lines; also absent: KIF26A; maybe low, not absent |
| [[CFAP299]] | B | CFAP299 activity lowers NRXN3's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 1.19× higher at baseline in the lines without CFAP299 | 0.068 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2 |
| [[XYLT1]] | B | XYLT1 activity raises NRXN3's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 2.96× lower at baseline in the lines without XYLT1 | 0.092 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805 |
| [[UNC5D]] | C | UNC5D activity raises NRXN3's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 4.45× lower at baseline in the lines without UNC5D | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |
| [[COL4A4]] | C | COL4A4 activity raises NRXN3's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 3.39× lower at baseline in the lines without COL4A4 | 0.061 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EBF2]] | B | NRXN3 activity raises EBF2's level | lines that do not express NRXN3 (23) vs lines expressing it (27) | 1.88× lower at baseline in the lines without NRXN3 | 0.010 | ⚠ within organs, on part of the lines; also absent: RGS7, FGF13, ENSG00000255983 |
| [[KLHL13]] | B | NRXN3 activity raises KLHL13's level | lines that do not express NRXN3 (23) vs lines expressing it (27) | 1.46× lower at baseline in the lines without NRXN3 | 0.044 | ⚠ within organs, on part of the lines; also absent: RGS7, FGF13, ENSG00000255983 |
| [[LGSN]] | C | NRXN3 activity raises LGSN's level | lines that do not express NRXN3 (23) vs lines expressing it (27) | 2.26× lower at baseline in the lines without NRXN3 | 0.022 | ⚠ within organs, on part of the lines; also absent: RGS7, FGF13, ENSG00000255983; co-absent with the target |
| [[NCKAP5]] | C | NRXN3 activity raises NCKAP5's level | lines that do not express NRXN3 (23) vs lines expressing it (27) | 2.73× lower at baseline in the lines without NRXN3 | 0.040 | ⚠ within organs, on part of the lines; also absent: RGS7, FGF13, ENSG00000255983; co-absent with the target |
| [[CA8]] | C | NRXN3 activity raises CA8's level | lines that do not express NRXN3 (23) vs lines expressing it (27) | 2.98× lower at baseline in the lines without NRXN3 | 0.064 | ⚠ within organs, on part of the lines; also absent: RGS7, FGF13, ENSG00000255983; co-absent with the target |
| [[VAV3]] | C | NRXN3 activity raises VAV3's level | lines that do not express NRXN3 (23) vs lines expressing it (27) | 2.77× lower at baseline in the lines without NRXN3 | 0.065 | ⚠ within organs, on part of the lines; also absent: RGS7, FGF13, ENSG00000255983; co-absent with the target |
| [[EYA2]] | C | NRXN3 activity raises EYA2's level | lines that do not express NRXN3 (23) vs lines expressing it (27) | 2.14× lower at baseline in the lines without NRXN3 | 0.069 | ⚠ within organs, on part of the lines; also absent: RGS7, FGF13, ENSG00000255983; co-absent with the target |
| [[COL4A3]] | C | NRXN3 activity raises COL4A3's level | lines that do not express NRXN3 (23) vs lines expressing it (27) | 2.13× lower at baseline in the lines without NRXN3 | 0.069 | ⚠ within organs, on part of the lines; also absent: RGS7, FGF13, ENSG00000255983; co-absent with the target |
| [[FSTL5]] | C | NRXN3 activity raises FSTL5's level | lines that do not express NRXN3 (23) vs lines expressing it (27) | 2.38× lower at baseline in the lines without NRXN3 | 0.097 | ⚠ within organs, on part of the lines; also absent: RGS7, FGF13, ENSG00000255983; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.511). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.7, 32.4); signed map (39.8, 46.2). **Vector** length 91.5, 23.8% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +12.1 | +34.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.0 | +14.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.3 | +16.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.8 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.3 | +11.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +5.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.3 | -5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.1 | -4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.8 | +0.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.5 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -2.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | neurexin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3-q31.1 — chr14:78,170,373-79,868,291 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0743; previously C14orf60 |
| Gene groups (HGNC) | Neurexins |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HDB5](https://www.uniprot.org/uniprotkb/Q9HDB5) (Neurexin-3-beta):

> Neuronal cell surface protein that may be involved in cell recognition and cell adhesion. May mediate intracellular signaling (By similarity). Functions as part of a trans-synaptic complex by binding to cerebellins and postsynaptic GRID1. This interaction helps regulate the activity of NMDA and AMPA receptors at hippocampal synapses without affecting synapse formation. NRXN3B-CBLN2-GRID1 complex transduce presynaptic signals into postsynaptic AMPAR response (By similarity).

**Summary**, from NCBI Gene [9369](https://www.ncbi.nlm.nih.gov/gene/9369):

> This gene encodes a member of a family of proteins that function in the nervous system as receptors and cell adhesion molecules. Extensive alternative splicing and the use of alternative promoters results in multiple transcript variants and protein isoforms for this gene, but the full-length nature of many of these variants has not been determined. Transcripts that initiate from an upstream promoter encode alpha isoforms, which contain epidermal growth factor-like (EGF-like) sequences and …

**Accessions** — [HGNC:8010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8010) · Entrez [9369](https://www.ncbi.nlm.nih.gov/gene/9369) · UniProt [Q9HDB5](https://www.uniprot.org/uniprotkb/Q9HDB5) · Ensembl [ENSG00000021645](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000021645)

## Data

Gene col 328: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 328); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 328, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 328]; `tensor/DDL_lfc|DDL_z.npy` [328]; `embed/gene_vectors.npy` [328]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 328 or target_col == 328). Every well: [[NRXN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRXN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
