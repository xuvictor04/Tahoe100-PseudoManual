---
symbol: "NPRL2"
type: "gene"
col: 3547
ensembl_id: "ENSG00000114388"
name: "NPR2 like, GATOR1 complex subunit"
location: "3p21.31"
module: 40
arm: "+"
pooled_cpm: 10.05
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# NPRL2

*NPR2 like, GATOR1 complex subunit* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.31× (z +10.6, q 3e-23, up in 36 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.37× (z +9.8, q 3e-20, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.490× (z -8.1, q 2e-13, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YIPF2]] (+0.80, fdr 7e-06), [[LCMT1]] (+0.78, fdr 7e-06), [[MRPL55]] (+0.75, fdr 7e-06); moves opposite to [[TCF12]] (-0.67, fdr 1e-05), [[TRIP12]] (-0.64, fdr 1e-05), [[PRRC2B]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SNHG18]] → it (grade B ⚠); 1 goes from it, the strongest it → [[YIPF2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3547.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.31×** | +10.6 | 3e-23 | 36/48 (HOP62, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.37×** | +9.8 | 3e-20 | 38/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.24×** | +9.2 | 9e-18 | 38/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.94×** | +7.5 | 7e-12 | 36/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.33× | +3.3 | 0.12 | 12/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.45× | +3.0 | 0.21 | 8/41 (HEC-1-A, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.45× | +3.0 | 0.21 | 9/41 (MIA PaCa-2, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3547.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.490×** | -8.1 | 2e-13 | 30/48 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.492×** | -8.1 | 2e-13 | 30/45 (HS-578T, H4, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.505×** | -7.8 | 1e-12 | 30/46 (SW 900, H4, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.511×** | -7.6 | 3e-12 | 27/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.530×** | -7.0 | 4e-10 | 28/47 (A498, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.672×** | -6.4 | 1e-08 | 22/45 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.617×** | -5.5 | 3e-06 | 23/34 (HS-578T, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.613×** | -5.4 | 6e-06 | 22/43 (hTERT-HPNE, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.628×** | -5.3 | 8e-06 | 24/47 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.664×** | -4.7 | 2e-04 | 22/47 (HEC-1-A, NCI-H2030, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.678×** | -4.4 | 5e-04 | 17/44 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -4.2 | 0.001 | 16/46 (RPMI-7951, H4, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.702×** | -4.0 | 0.002 | 17/47 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.733×** | -3.5 | 0.016 | 15/48 (HS-578T, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.564×** | -3.4 | 0.024 | 14/47 (Hs 766T, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.746×** | -3.3 | 0.029 | 12/48 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.750×** | -3.3 | 0.034 | 17/47 (HS-578T, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.752×** | -3.1 | 0.055 | 18/45 (SNU-1, COLO 205, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.762×** | -3.1 | 0.058 | 10/48 (CHP-212, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3547. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 20.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0808× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -11.6) |
| [[A498 (line)]] | wt | 18.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.211× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 14.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0698× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 0.05 µM 0.0592× (z -9.6) |
| [[SW480 (line)]] | alt | 10.9 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 4.18× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.161× (z -12.6) |
| [[A-172 (line)]] | wt | 10.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.264× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 8.75 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -9.6) |
| [[HOP62 (line)]] | alt | 8.15 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -8.8) |
| [[KATO III (line)]] | alt | 9.81 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.125× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 8.44 | 0 | 2 (1 ⚠) | — | [[Cepharanthine (drug)]] 0.5 µM 0.150× (z -8.9) |
| [[SNU-423 (line)]] | alt | 9.47 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -9.4) |
| [[C32 (line)]] | wt | 5.59 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0654× (z -9.1) ⚠ cell-cycle shift, explains ~8% of this change |
| [[H4 (line)]] | wt | 16.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0530× (z -10.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -9.2) |
| [[J82 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0472× (z -15.7) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0400× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~15% of this change |
| [[Panc 03.27 (line)]] | alt | 6.93 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0876× (z -10.4) |
| [[PANC-1 (line)]] | alt | 8.56 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0891× (z -10.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 9.38 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0972× (z -10.4) |
| [[A-427 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3547), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIPF2]] | +0.80 | +0.83 / +0.72 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.78 | +0.73 / +0.64 | both halves | 7e-06 | STRING 584 |
| [[MRPL55]] | +0.75 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[SDHAP1-1]] | +0.75 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[MED8]] | +0.74 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[BET1L]] | +0.73 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.72 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[OXNAD1]] | +0.72 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[C1orf174]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[COG6]] | +0.72 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[OSBPL7]] | +0.71 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ARFGAP1]] | +0.71 | +0.67 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF12]] | -0.67 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[TRIP12]] | -0.64 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[PRRC2B]] | -0.63 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[CACNA2D1]] | -0.63 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[ATE1]] | -0.63 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ARAP2]] | -0.61 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.61 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[CUEDC1]] | -0.61 | -0.57 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNHG18]] | B | SNHG18 activity raises NPRL2's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.36× lower at baseline in the lines without SNHG18 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[HDAC6]] | B | HDAC6 activity lowers NPRL2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[WLS]] | B | WLS activity raises NPRL2's level | lines that do not express WLS (7) vs lines expressing it (43) | 1.43× lower at baseline in the lines without WLS | 0.049 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PLPP4]] | B | PLPP4 activity raises NPRL2's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 1.28× lower at baseline in the lines without PLPP4 | 0.087 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YIPF2]] | C | NPRL2's natural level strengthens YIPF2's drug response | NPRL2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.04; direction clear | 0.043 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.795). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (0.9, -17.2); signed map (-36.8, 2.4). **Vector** length 96.9, 20.9% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +9.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.1 | +9.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.9 | +7.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.0 | +2.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.0 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +1.7 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.4 | -5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.2 | -0.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -6.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -0.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.7 | -2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | NPR2 like, GATOR1 complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:50,347,330-50,350,826 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NPR2L, NPR2; previously TUSC4 |
| Gene groups (HGNC) | GATOR1 subcomplex |
| Reactome | 4 pathways, smallest: Amino acids regulate mTORC1; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WTW4](https://www.uniprot.org/uniprotkb/Q8WTW4) (GATOR1 complex protein NPRL2):

> Catalytic component of the GATOR1 complex, a multiprotein complex that functions as an inhibitor of the amino acid-sensing branch of the mTORC1 pathway. In response to amino acid depletion, the GATOR1 complex has GTPase activating protein (GAP) activity and strongly increases GTP hydrolysis by RagA/RRAGA (or RagB/RRAGB) within heterodimeric Rag complexes, thereby turning them into their inactive GDP-bound form, releasing mTORC1 from lysosomal surface and inhibiting mTORC1 signaling. In the …

**Summary**, from NCBI Gene [10641](https://www.ncbi.nlm.nih.gov/gene/10641):

> Enables GTPase activator activity. Involved in cellular response to amino acid starvation; negative regulation of TORC1 signaling; and negative regulation of kinase activity. Part of GATOR1 complex. Is active in lysosomal membrane. Implicated in familial focal epilepsy with variable foci 2. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24969](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24969) · Entrez [10641](https://www.ncbi.nlm.nih.gov/gene/10641) · UniProt [Q8WTW4](https://www.uniprot.org/uniprotkb/Q8WTW4) · Ensembl [ENSG00000114388](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114388)

## Data

Gene col 3547: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3547); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3547, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3547]; `tensor/DDL_lfc|DDL_z.npy` [3547]; `embed/gene_vectors.npy` [3547]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3547 or target_col == 3547). Every well: [[NPRL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPRL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
