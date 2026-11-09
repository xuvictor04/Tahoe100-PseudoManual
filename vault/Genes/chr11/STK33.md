---
symbol: "STK33"
type: "gene"
col: 5063
ensembl_id: "ENSG00000130413"
name: "serine/threonine kinase 33"
location: "11p15.4"
module: 16
arm: "+"
pooled_cpm: 16.25
n_lines_expressing: 32
n_dd_up: 39
n_dd_down: 4
n_dd_up_clean: 33
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 9
direction_downstream: 5
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# STK33

*serine/threonine kinase 33* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.71× (z +21.7, q 0e+00, up in 17 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.462× (z -9.1, q 8e-17, down in 24 of 29 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R9A]] (+0.60, fdr 1e-05), [[SLC25A12]] (+0.60, fdr 1e-05), [[FTCDNL1]] (+0.60, fdr 7e-06); moves opposite to [[MBOAT7]] (-0.61, fdr 1e-05), [[TNXB]] (-0.55, fdr 7e-05), [[HOOK3]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[SMIM10]] → it (grade B ⚠); 5 go from it, the strongest it → [[GPR143]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5063.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.71×** | +21.7 | 0e+00 | 17/27 (BT-474, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.66×** | +16.2 | 0e+00 | 26/28 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.49×** | +15.0 | 0e+00 | 17/27 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.46×** | +14.5 | 3e-45 | 28/29 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.93×** | +12.6 | 4e-34 | 25/28 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.39×** | +10.2 | 2e-22 | 18/26 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.25×** | +9.4 | 3e-19 | 22/28 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.29×** | +8.3 | 6e-15 | 22/29 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +8.2 | 2e-14 | 22/29 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.53×** | +7.0 | 2e-10 | 18/29 (A549, HOP62, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.5 | 4e-09 | 8/30 (A-172, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.72×** | +6.3 | 1e-08 | 21/29 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +5.8 | 4e-07 | 3/24 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +5.1 | 1e-05 | 6/17 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.56×** | +5.0 | 2e-05 | 13/28 (SW480, NCI-H2347, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.22×** | +4.9 | 4e-05 | 21/28 (PANC-1, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.5 | 2e-04 | 6/26 (BT-474, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +4.3 | 5e-04 | 14/28 (SW480, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5063.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.462×** | -9.1 | 8e-17 | 24/29 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -6.5 | 2e-08 | 20/26 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.662×** | -4.8 | 2e-04 | 14/28 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.690×** | -4.4 | 0.002 | 17/28 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.826× | -3.2 | 0.17 | 5/29 (SNU-1, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5063. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 18.8 | 5 | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 10.5× (z +15.4) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.139× (z -13.0) |
| [[A-427 (line)]] | wt | 26.3 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +8.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.183× (z -11.7) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -10.3) |
| [[LoVo (line)]] | wt | 26.8 | 1 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.41× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.149× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -13.2) |
| [[SHP-77 (line)]] | alt | 48.9 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0939× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.154× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 98.7 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.302× (z -12.7) |
| [[SW480 (line)]] | alt | 30.9 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -15.9) |
| [[HOP62 (line)]] | alt | 8.17 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +14.6) | — |
| [[LS 180 (line)]] | wt | 26.4 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.89× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.141× (z -11.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 16.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.91× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +9.9) | — |
| [[HCT15 (line)]] | alt | 4.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 48.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 9.56 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.16× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 31.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 10.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.85× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 32.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -9.6) |
| [[A-172 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.84 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5063), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R9A]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SLC25A12]] | +0.60 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[FTCDNL1]] | +0.60 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[PAK1IP1]] | +0.57 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[TIGD2]] | +0.56 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[RNF180]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[PCLO]] | +0.56 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[DHFR2]] | +0.55 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[WDR17]] | +0.54 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[COMMD8]] | +0.54 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[FANCF]] | +0.54 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[CYP2U1]] | +0.54 | +0.64 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBOAT7]] | -0.61 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[TNXB]] | -0.55 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[HOOK3]] | -0.53 | -0.63 / -0.49 | both halves | 2e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.52 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[ZCCHC17]] | -0.52 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[DONSON]] | -0.50 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[CCDC168]] | -0.50 | -0.45 / -0.25 | both halves | 4e-04 |  |
| [[FBH1]] | -0.50 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[NFATC2IP]] | -0.50 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[UFD1]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TULP3]] | -0.50 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[SWI5]] | -0.49 | -0.50 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMIM10]] | B | SMIM10 activity raises STK33's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 1.92× lower at baseline in the lines without SMIM10 | 0.014 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[ACOXL]] | B | ACOXL activity raises STK33's level | lines that do not express ACOXL (28) vs lines expressing it (22) | 1.88× lower at baseline in the lines without ACOXL | 0.033 | ⚠ within organs, on part of the lines; also absent: ILDR1, PRKCH-AS1, LRRN1; maybe low, not absent |
| [[PRTG]] | B | PRTG activity raises STK33's level | lines that do not express PRTG (14) vs lines expressing it (36) | 1.78× lower at baseline in the lines without PRTG | 0.044 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[PCLO]] | B | PCLO activity raises STK33's level | lines that do not express PCLO (15) vs lines expressing it (35) | 2.25× lower at baseline in the lines without PCLO | 0.045 | ⚠ within organs, on part of the lines; also absent: POPDC3, WIPF1, WDR17 |
| [[ST6GALNAC5]] | B | ST6GALNAC5 activity raises STK33's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 2.20× lower at baseline in the lines without ST6GALNAC5 | 0.048 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8 |
| [[STK32A]] | B | STK32A activity raises STK33's level | lines that do not express STK32A (23) vs lines expressing it (27) | 2.03× lower at baseline in the lines without STK32A | 0.059 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[WDR17]] | B | WDR17 activity raises STK33's level | lines that do not express WDR17 (16) vs lines expressing it (34) | 1.91× lower at baseline in the lines without WDR17 | 0.061 | ⚠ within organs, on part of the lines; also absent: WIPF1, AFAP1L1, SGCE |
| [[LINC02832]] | B | LINC02832 activity raises STK33's level | lines that do not express LINC02832 (26) vs lines expressing it (24) | 1.78× lower at baseline in the lines without LINC02832 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000235337, ENSG00000288902, ENSG00000239498 |
| [[LINC00923]] | B | LINC00923 activity raises STK33's level | lines that do not express LINC00923 (33) vs lines expressing it (17) | 2.08× lower at baseline in the lines without LINC00923 | 0.097 | ⚠ within organs, on part of the lines; also absent: TM4SF4, SLC25A24P1, ENSG00000283633 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR143]] | B | STK33 activity raises GPR143's level | lines that do not express STK33 (18) vs lines expressing it (32) | 1.88× lower at baseline in the lines without STK33 | 0.021 | ⚠ within organs, on part of the lines; also absent: SDK1, PGBD5, NID1; maybe low, not absent |
| [[ACOXL]] | B | STK33 activity raises ACOXL's level | lines that do not express STK33 (18) vs lines expressing it (32) | 2.28× lower at baseline in the lines without STK33 | 0.024 | ⚠ within organs, on part of the lines; also absent: SDK1, PGBD5, NID1; maybe low, not absent |
| [[SMIM10]] | B | STK33 activity raises SMIM10's level | lines that do not express STK33 (18) vs lines expressing it (32) | 1.57× lower at baseline in the lines without STK33 | 0.033 | ⚠ within organs, on part of the lines; also absent: SDK1, PGBD5, NID1; maybe low, not absent |
| [[ZNF385B]] | B | STK33 activity raises ZNF385B's level | lines that do not express STK33 (18) vs lines expressing it (32) | 1.67× lower at baseline in the lines without STK33 | 0.048 | ⚠ within organs, on part of the lines; also absent: SDK1, PGBD5, NID1; maybe low, not absent |
| [[STK32A]] | B | STK33 activity raises STK32A's level | lines that do not express STK33 (18) vs lines expressing it (32) | 1.87× lower at baseline in the lines without STK33 | 0.082 | ⚠ within organs, on part of the lines; also absent: SDK1, PGBD5, NID1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.477). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-19.9, 5.5); signed map (35.6, -11.5). **Vector** length 62.3, 13.7% of its response variance represented; |z| ≥ 3 in 755 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +16.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +5.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +4.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +4.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -9.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -3.0 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:8,391,868-8,594,289 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | STK33 family kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYT3](https://www.uniprot.org/uniprotkb/Q9BYT3) (Serine/threonine-protein kinase 33):

> Serine/threonine protein kinase required for spermatid differentiation and male fertility. Promotes sperm flagella assembly during spermatogenesis by mediating phosphorylation of fibrous sheath proteins AKAP3 and AKAP4 (By similarity). Also phosphorylates vimentin/VIM, thereby regulating the dynamic behavior of the intermediate filament cytoskeleton (By similarity).

**Summary**, from NCBI Gene [65975](https://www.ncbi.nlm.nih.gov/gene/65975):

> Enables protein serine/threonine kinase activity. Involved in negative regulation of protein metabolic process; peptidyl-threonine phosphorylation; and spermatogenesis. Predicted to be located in manchette. Predicted to be active in cytoplasm and nucleus. Implicated in colorectal cancer; depressive disorder; and spermatogenic failure 93. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14568](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14568) · Entrez [65975](https://www.ncbi.nlm.nih.gov/gene/65975) · UniProt [Q9BYT3](https://www.uniprot.org/uniprotkb/Q9BYT3) · Ensembl [ENSG00000130413](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130413)

## Data

Gene col 5063: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5063); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5063, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5063]; `tensor/DDL_lfc|DDL_z.npy` [5063]; `embed/gene_vectors.npy` [5063]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5063 or target_col == 5063). Every well: [[STK33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
