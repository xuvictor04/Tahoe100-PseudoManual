---
symbol: "OSBPL7"
type: "gene"
col: 99
ensembl_id: "ENSG00000006025"
name: "oxysterol binding protein like 7"
location: "17q21.32"
module: 30
arm: "+"
pooled_cpm: 7.98
n_lines_expressing: 43
n_dd_up: 10
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 10
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# OSBPL7

*oxysterol binding protein like 7* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.73× (z +6.4, q 1e-07, up in 22 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.485× (z -8.1, q 3e-13, down in 26 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL17]] (+0.74, fdr 7e-06), [[NPRL2]] (+0.71, fdr 7e-06), [[RAB3A]] (+0.71, fdr 1e-05); moves opposite to [[DGKH]] (-0.67, fdr 1e-05), [[ASXL2]] (-0.66, fdr 1e-05), [[PSMD6-AS1]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 10 go from it, the strongest it → [[SFXN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 99.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.73×** | +6.4 | 1e-07 | 22/40 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +6.1 | 3e-07 | 23/39 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +4.6 | 8e-04 | 14/40 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.009 | 11/40 (NCI-H2347, SW 900, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.40×** | +3.9 | 0.010 | 17/39 (A498, C32, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.28×** | +3.9 | 0.010 | 7/40 (RKO, HCT15, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.017 | 7/39 (NCI-H2347, C32, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.39×** | +3.7 | 0.018 | 8/34 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +3.4 | 0.042 | 14/36 (A549, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.052 | 9/40 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 99.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.485×** | -8.1 | 3e-13 | 26/37 (SW 900, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.574×** | -6.2 | 1e-07 | 20/39 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -6.1 | 3e-07 | 22/39 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.640×** | -5.2 | 3e-05 | 18/40 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.732×** | -5.1 | 5e-05 | 18/41 (hTERT-HPNE, SW 900, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.656×** | -4.7 | 2e-04 | 21/36 (RPMI-7951, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.683×** | -4.3 | 0.002 | 14/19 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.717×** | -3.9 | 0.007 | 16/39 (NCI-H2347, H4, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.721×** | -3.8 | 0.008 | 18/39 (HepG2/C3A, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.727×** | -3.7 | 0.011 | 12/39 (NCI-H2347, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.813×** | -3.3 | 0.047 | 14/39 (NCI-H2347, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.763×** | -3.2 | 0.073 | 15/39 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 5 µM |  | **0.761×** | -3.1 | 0.096 | 6/39 (NCI-H460, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 99. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 22.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -13.6) ⚠ cell-cycle shift, explains ~92% of this change |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0362× (z -13.5) |
| [[SW480 (line)]] | alt | 10.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -11.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 9.16 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0914× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 9.95 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -11.6) |
| [[Hs 766T (line)]] | wt | 4.92 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0682× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[HT-29 (line)]] | alt | 6.96 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -8.6) |
| [[J82 (line)]] | alt | 5.46 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.108× (z -9.3) |
| [[KATO III (line)]] | alt | 12.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 6.74 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.143× (z -8.8) ⚠ cell-cycle shift, explains ~19% of this change |
| [[NCI-H1792 (line)]] | alt | 7.57 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[A-172 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.942 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.978 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.821 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 99), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL17]] | +0.74 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[NPRL2]] | +0.71 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[RAB3A]] | +0.71 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[MKRN2]] | +0.71 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[USP35]] | +0.70 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[TCIRG1]] | +0.70 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[PLCD1]] | +0.69 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[MAST3]] | +0.69 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[RGS14]] | +0.68 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[ELP1]] | +0.67 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[MPND]] | +0.67 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[ANO8]] | +0.66 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGKH]] | -0.67 | -0.58 / -0.51 | both halves | 1e-05 | same gene group |
| [[ASXL2]] | -0.66 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[PSMD6-AS1]] | -0.62 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[LEPROT]] | -0.62 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[ENOX2]] | -0.61 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ARAP2]] | -0.61 | -0.51 / -0.47 | both halves | 2e-05 | same gene group |
| [[BAZ1A]] | -0.60 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[WARS2-AS1]] | -0.60 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[MSRA]] | -0.60 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[CHRAC1]] | -0.59 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[ERCC6L2]] | -0.59 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[PTPRK]] | -0.59 | -0.60 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises OSBPL7's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SNHG18]] | B | SNHG18 activity raises OSBPL7's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.78× lower at baseline in the lines without SNHG18 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[PTPRK]] | B | PTPRK activity raises OSBPL7's level | lines that do not express PTPRK (6) vs lines expressing it (44) | 2.38× lower at baseline in the lines without PTPRK | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000246225, EPS8, ASPH |
| [[ARAP2]] | B | ARAP2 activity raises OSBPL7's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 2.16× lower at baseline in the lines without ARAP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[DUSP9]] | B | DUSP9 activity lowers OSBPL7's level | lines that do not express DUSP9 (17) vs lines expressing it (33) | 1.52× higher at baseline in the lines without DUSP9 | 0.078 | ⚠ within organs, on part of the lines; also absent: SLC47A1, SMO, LAMC3 |
| [[SNPH]] | B | SNPH activity raises OSBPL7's level | lines that do not express SNPH (5) vs lines expressing it (45) | 2.19× lower at baseline in the lines without SNPH | 0.098 | ⚠ within organs, on part of the lines; also absent: E2F7, SPDL1, TMOD2; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SFXN3]] | B | OSBPL7 activity raises SFXN3's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 3.01× lower at baseline in the lines without OSBPL7 | 0.021 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |
| [[ASXL2]] | B | OSBPL7 activity lowers ASXL2's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 1.54× higher at baseline in the lines without OSBPL7 | 0.035 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |
| [[TCIRG1]] | B | OSBPL7 activity raises TCIRG1's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without OSBPL7 | 0.038 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |
| [[CHRAC1]] | B | OSBPL7 activity lowers CHRAC1's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 1.43× higher at baseline in the lines without OSBPL7 | 0.050 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |
| [[ALAD]] | B | OSBPL7 activity strengthens ALAD's drug response | lines that do not express OSBPL7 (7) vs lines expressing it (41) | the lines without OSBPL7 respond 0.79× as strongly (z diff +0.64); rises at some drug-doses, falls at others (67% from rises): Adagrasib 0.05 µM: 0.92x vs 0.81x (z diff +2.5); Panobinostat 0.5 µM: 3.21x vs 4.42x (z diff +1.8); Panobinostat 5 µM: 4.04x vs 5.22x (z diff +1.5) | 0.063 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[UCKL1]] | B | OSBPL7 activity lowers UCKL1's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 1.29× higher at baseline in the lines without OSBPL7 | 0.075 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |
| [[KLHL17]] | B | OSBPL7 activity lowers KLHL17's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 1.46× higher at baseline in the lines without OSBPL7 | 0.086 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |
| [[CYB5R1]] | B | OSBPL7 activity raises CYB5R1's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 1.43× lower at baseline in the lines without OSBPL7 | 0.091 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |
| [[PLD2]] | B | OSBPL7 activity lowers PLD2's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 1.38× higher at baseline in the lines without OSBPL7 | 0.092 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |
| [[PELP1]] | B | OSBPL7 activity lowers PELP1's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 1.47× higher at baseline in the lines without OSBPL7 | 0.093 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.751). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (5.1, -5.7); signed map (-31.2, -1.0). **Vector** length 74.1, 14.6% of its response variance represented; |z| ≥ 3 in 730 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +6.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +6.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.6 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.8 | +2.0 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -3.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -5.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | oxysterol binding protein like 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:47,807,372-47,821,803 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ORP7, MGC71150 |
| Gene groups (HGNC) | Oxysterol binding proteins; Pleckstrin homology domain containing |
| Reactome | 4 pathways, smallest: Synthesis of bile acids and bile salts; Bile acid and bile salt metabolism; Metabolism of steroids |
| Matched by | ensembl_id |

UniProt [Q9BZF2](https://www.uniprot.org/uniprotkb/Q9BZF2) carries no function annotation.

**Summary**, from NCBI Gene [114881](https://www.ncbi.nlm.nih.gov/gene/114881):

> This gene encodes a member of the oxysterol-binding protein (OSBP) family, a group of intracellular lipid receptors. Like most members, the encoded protein contains an N-terminal pleckstrin homology domain and a highly conserved C-terminal OSBP-like sterol-binding domain. Two transcript variants encoding the same isoform have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16387](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16387) · Entrez [114881](https://www.ncbi.nlm.nih.gov/gene/114881) · UniProt [Q9BZF2](https://www.uniprot.org/uniprotkb/Q9BZF2) · Ensembl [ENSG00000006025](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006025)

## Data

Gene col 99: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 99); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 99, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 99]; `tensor/DDL_lfc|DDL_z.npy` [99]; `embed/gene_vectors.npy` [99]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 99 or target_col == 99). Every well: [[OSBPL7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSBPL7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
