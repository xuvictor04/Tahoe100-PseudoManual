---
symbol: "FBLN7"
type: "gene"
col: 6849
ensembl_id: "ENSG00000144152"
name: "fibulin 7"
location: "2q13"
module: 13
arm: "+"
pooled_cpm: 10.19
n_lines_expressing: 42
n_dd_up: 9
n_dd_down: 30
n_dd_up_clean: 4
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# FBLN7

*fibulin 7* — 2q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.61× (z +16.6, q 0e+00, up in 26 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.469× (z -13.1, q 2e-36, down in 23 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESR2]] (+0.63, fdr 3e-05), [[SYNDIG1]] (+0.60, fdr 8e-06), [[PECAM1]] (+0.59, fdr 1e-05); moves opposite to [[MAP9]] (-0.46, fdr 3e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[GPR173]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6849.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +16.6 | 0e+00 | 26/33 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +9.4 | 1e-18 | 11/22 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +8.4 | 1e-14 | 3/15 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.0 | 3e-07 | 17/32 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +5.7 | 2e-06 | 3/16 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.4 | 8e-06 | 9/33 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.006 | 8/35 (PANC-1, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.33×** | +3.5 | 0.032 | 5/36 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.4 | 0.039 | 5/32 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.30× | +3.1 | 0.12 | 6/36 (HCT15, NCI-H460, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.28× | +3.0 | 0.13 | 3/37 (LOX-IMVI, CFPAC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6849.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.469×** | -13.1 | 2e-36 | 23/35 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.395×** | -10.9 | 2e-25 | 25/36 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.510×** | -8.2 | 3e-14 | 26/39 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.526×** | -7.9 | 5e-13 | 23/34 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.532×** | -7.7 | 1e-12 | 21/37 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.572×** | -6.8 | 8e-10 | 19/39 (NCI-H1792, NCI-H23, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.582×** | -6.6 | 3e-09 | 18/36 (RPMI-7951, SW 900, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.591×** | -6.4 | 9e-09 | 21/38 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.608×** | -6.1 | 7e-08 | 20/38 (NCI-H1792, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.642×** | -5.4 | 3e-06 | 19/38 (RPMI-7951, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.484×** | -4.6 | 2e-04 | 16/36 (SHP-77, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.765×** | -4.6 | 2e-04 | 13/39 (SW 1271, SNU-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.705×** | -4.3 | 8e-04 | 14/39 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.525×** | -4.1 | 0.002 | 9/31 (NCI-H2030, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.716×** | -4.1 | 0.002 | 13/39 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.717×** | -4.1 | 0.002 | 18/37 (RPMI-7951, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.740×** | -3.7 | 0.008 | 8/39 (A-172, BT-474, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6849. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 90.9 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -23.3) |
| [[HOP62 (line)]] | alt | 32.7 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0978× (z -19.9) |
| [[NCI-H1792 (line)]] | alt | 36.4 | 0 | 10 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0191× (z -25.7) ⚠ toxic; cell-cycle shift, explains ~22% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.101× (z -14.9) |
| [[HS-578T (line)]] | alt | 80.5 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -16.5) |
| [[J82 (line)]] | alt | 16.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -17.1) |
| [[A-172 (line)]] | wt | 16.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0933× (z -11.5) |
| [[SHP-77 (line)]] | alt | 38.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -10.6) |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 2.94 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.13× (z +11.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.107× (z -8.9) ⚠ cell-cycle shift, explains ~24% of this change |
| [[SK-MEL-2 (line)]] | alt | 7.41 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 3.05 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0418× (z -10.7) |
| [[SNU-423 (line)]] | alt | 7.12 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -9.3) |
| [[HCT15 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.121× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~22% of this change |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 2.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.71× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 5.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +8.6) | — |
| [[A-427 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6849), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESR2]] | +0.63 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[SYNDIG1]] | +0.60 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[PECAM1]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[C2orf92]] | +0.59 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[ITGA11]] | +0.59 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[C9]] | +0.59 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[APCDD1L]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ADORA1]] | +0.57 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[MEI1]] | +0.57 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[PLXNA4]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[CCDC168]] | +0.57 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[AMZ1]] | +0.56 | +0.40 / +0.64 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP9]] | -0.46 | -0.28 / -0.45 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR173]] | B | GPR173 activity raises FBLN7's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 2.44× lower at baseline in the lines without GPR173 | 0.003 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2 |
| [[ITGA11]] | B | ITGA11 activity raises FBLN7's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.97× lower at baseline in the lines without ITGA11 | 0.005 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[TOP2A]] | B | TOP2A activity lowers FBLN7's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HTR1F]] | B | HTR1F activity raises FBLN7's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 2.23× lower at baseline in the lines without HTR1F | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| [[AK5]] | B | AK5 activity raises FBLN7's level | lines that do not express AK5 (25) vs lines expressing it (25) | 2.01× lower at baseline in the lines without AK5 | 0.079 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent |
| [[GPR173]] | B | GPR173 activity strengthens FBLN7's drug response | lines that do not express GPR173 (22) vs lines expressing it (17) | the lines without GPR173 respond 0.76× as strongly (z diff +0.85); strongest at Harringtonine 5 µM: 0.43x vs 0.19x (z diff +4.0) | 0.086 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2; target measured in part of the lines; artifact flags |
| [[COL5A1]] | B | COL5A1 activity raises FBLN7's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 1.98× lower at baseline in the lines without COL5A1 | 0.096 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.584). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.1, 15.6); signed map (23.5, 46.5). **Vector** length 75.5, 14.3% of its response variance represented; |z| ≥ 3 in 1,001 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +16.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +2.9 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -4.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -2.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.2 | -4.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -6.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | fibulin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q13 — chr2:112,138,385-112,188,218 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37440, TM14 |
| Gene groups (HGNC) | Fibulins; Sushi domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53RD9](https://www.uniprot.org/uniprotkb/Q53RD9) (Fibulin-7):

> An adhesion molecule that interacts with extracellular matrix molecules in developing teeth and may play important roles in differentiation and maintenance of odontoblasts as well as in dentin formation.

**Summary**, from NCBI Gene [129804](https://www.ncbi.nlm.nih.gov/gene/129804):

> Predicted to enable calcium ion binding activity; heparan sulfate proteoglycan binding activity; and heparin binding activity. Predicted to be involved in cell adhesion. Located in focal adhesion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26740) · Entrez [129804](https://www.ncbi.nlm.nih.gov/gene/129804) · UniProt [Q53RD9](https://www.uniprot.org/uniprotkb/Q53RD9) · Ensembl [ENSG00000144152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144152)

## Data

Gene col 6849: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6849); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6849, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6849]; `tensor/DDL_lfc|DDL_z.npy` [6849]; `embed/gene_vectors.npy` [6849]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6849 or target_col == 6849). Every well: [[FBLN7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBLN7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
