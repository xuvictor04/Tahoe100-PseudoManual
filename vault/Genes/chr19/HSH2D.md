---
symbol: "HSH2D"
type: "gene"
col: 12265
ensembl_id: "ENSG00000196684"
name: "hematopoietic SH2 domain containing"
location: "19p13.11"
module: 8
arm: "+"
pooled_cpm: 23.71
n_lines_expressing: 23
n_dd_up: 2
n_dd_down: 17
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 111
direction_downstream: 126
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# HSH2D

*hematopoietic SH2 domain containing* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +9.6, q 7e-19, up in 2 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.519× (z -8.2, q 2e-13, down in 19 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LGALS9]] (+0.75, fdr 7e-06), [[TC2N]] (+0.70, fdr 7e-06), [[ADGRF1]] (+0.69, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 111 arrows point to it, the strongest [[SLC44A3-AS1]] → it (grade B ⚠); 126 go from it, the strongest it → [[SLC44A3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12265.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +9.6 | 7e-19 | 2/20 (SW 900, SW480) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +5.0 | 1e-04 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.49× | +3.4 | 0.13 | 5/21 (SW480, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.30× | +3.3 | 0.13 | 2/21 (A-427, SK-MEL-2) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12265.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.519×** | -8.2 | 2e-13 | 19/21 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.569×** | -7.0 | 5e-10 | 19/21 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.571×** | -7.0 | 5e-10 | 19/21 (LoVo, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.602×** | -6.3 | 3e-08 | 17/21 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.611×** | -6.1 | 9e-08 | 19/21 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.674×** | -4.7 | 2e-04 | 16/21 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.713×** | -4.2 | 0.002 | 14/20 (HCT15, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.720×** | -4.1 | 0.003 | 15/21 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.723×** | -4.0 | 0.003 | 11/21 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.807×** | -3.8 | 0.009 | 12/21 (Panc 03.27, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.741×** | -3.7 | 0.009 | 8/21 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -3.7 | 0.009 | 15/21 (Panc 03.27, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.742×** | -3.7 | 0.009 | 13/21 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.730×** | -3.7 | 0.009 | 16/21 (LoVo, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.586×** | -3.5 | 0.019 | 12/22 (LoVo, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.828×** | -3.3 | 0.033 | 15/22 (LoVo, COLO 205, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.784×** | -3.0 | 0.085 | 8/21 (AsPC-1, NCI-H2347, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12265. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 125 | 0 | 22 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0410× (z -31.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.132× (z -19.9) |
| [[COLO 205 (line)]] | alt | 146 | 0 | 13 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0668× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -13.9) |
| [[Panc 03.27 (line)]] | alt | 122 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0549× (z -27.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -19.8) |
| [[CFPAC-1 (line)]] | alt | 93.5 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -16.8) |
| [[NCI-H2347 (line)]] | alt | 91.3 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -17.3) |
| [[SW1417 (line)]] | alt | 40.7 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -13.1) |
| [[KATO III (line)]] | alt | 36.4 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -10.6) |
| [[LS 180 (line)]] | wt | 47.7 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 32.2 | 0 | 4 (2 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.106× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 19.1 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0234× (z -22.8) |
| [[AsPC-1 (line)]] | alt | 31.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.170× (z -10.4) |
| [[HCT15 (line)]] | alt | 59.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 39.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 20.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -13.7) |
| [[A-172 (line)]] | wt | 3.74 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.09 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.73 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.65 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.57 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.48 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.07 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.99 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.29 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.52 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.82 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12265), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LGALS9]] | +0.75 | +0.72 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[TC2N]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[ADGRF1]] | +0.69 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[C6orf132]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[ST14]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.66 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[INAVA]] | +0.66 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[FAM83E]] | +0.66 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[SLC44A4]] | +0.66 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[RNF183]] | +0.66 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[TMC4]] | +0.66 | +0.77 / +0.53 | both halves | 1e-05 |  |
| [[SIDT1]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*111 arrows, 111 of them with an alert ⚠; grade A 0, B 15, C 96. Shown: the 12 strongest; 99 more arrows (99 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises HSH2D's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 3.20× lower at baseline in the lines without SLC44A3-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[SRMS]] | B | SRMS activity raises HSH2D's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.67× lower at baseline in the lines without SRMS | 0.008 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[EPS8L1]] | B | EPS8L1 activity raises HSH2D's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.97× lower at baseline in the lines without EPS8L1 | 0.011 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[SLC44A3]] | B | SLC44A3 activity raises HSH2D's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.04× lower at baseline in the lines without SLC44A3 | 0.013 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[SPATA6L]] | B | SPATA6L activity raises HSH2D's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 3.06× lower at baseline in the lines without SPATA6L | 0.037 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[EPSTI1]] | B | EPSTI1 activity raises HSH2D's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.19× lower at baseline in the lines without EPSTI1 | 0.038 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[ADGRF4]] | B | ADGRF4 activity raises HSH2D's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 2.50× lower at baseline in the lines without ADGRF4 | 0.045 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[PLEKHG1]] | B | PLEKHG1 activity raises HSH2D's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.49× lower at baseline in the lines without PLEKHG1 | 0.047 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[STS]] | B | STS activity raises HSH2D's level | lines that do not express STS (11) vs lines expressing it (39) | 2.44× lower at baseline in the lines without STS | 0.061 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[TNFSF10]] | B | TNFSF10 activity raises HSH2D's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 2.11× lower at baseline in the lines without TNFSF10 | 0.066 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[FBXO39]] | B | FBXO39 activity raises HSH2D's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 1.44× lower at baseline in the lines without FBXO39 | 0.073 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[BATF2]] | B | BATF2 activity raises HSH2D's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.32× lower at baseline in the lines without BATF2 | 0.082 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |

### Downstream of this gene

*126 arrows, 126 of them with an alert ⚠; grade A 0, B 38, C 88. Shown: the 12 strongest; 114 more arrows (114 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3-AS1]] | B | HSH2D activity raises SLC44A3-AS1's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 4.14× lower at baseline in the lines without HSH2D | 3e-04 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[SLC44A3]] | B | HSH2D activity raises SLC44A3's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 3.77× lower at baseline in the lines without HSH2D | 3e-04 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[EPS8L1]] | B | HSH2D activity raises EPS8L1's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 3.73× lower at baseline in the lines without HSH2D | 0.001 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[ITPKC]] | B | HSH2D activity raises ITPKC's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 2.81× lower at baseline in the lines without HSH2D | 0.004 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[SPATA6L]] | B | HSH2D activity raises SPATA6L's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 3.66× lower at baseline in the lines without HSH2D | 0.004 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[STS]] | B | HSH2D activity raises STS's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 2.28× lower at baseline in the lines without HSH2D | 0.006 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[TMEM51-AS1]] | B | HSH2D activity raises TMEM51-AS1's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 2.46× lower at baseline in the lines without HSH2D | 0.007 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[FAM83E]] | B | HSH2D activity raises FAM83E's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 2.99× lower at baseline in the lines without HSH2D | 0.008 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[TLDC2]] | B | HSH2D activity raises TLDC2's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 2.19× lower at baseline in the lines without HSH2D | 0.012 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[ADGRF4]] | B | HSH2D activity raises ADGRF4's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 2.14× lower at baseline in the lines without HSH2D | 0.014 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[DTX2]] | B | HSH2D activity raises DTX2's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 1.79× lower at baseline in the lines without HSH2D | 0.016 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | HSH2D activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express HSH2D (27) vs lines expressing it (21) | the lines without HSH2D: 1.19× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.8, 54.9); signed map (59.2, 5.9). **Vector** length 89.8, 31.8% of its response variance represented; |z| ≥ 3 in 590 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +0.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +9.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +0.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.6 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +0.8 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.6 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -7.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | hematopoietic SH2 domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:16,134,028-16,158,575 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ALX, HSH2, FLJ14886 |
| Gene groups (HGNC) | SH2 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JZ2](https://www.uniprot.org/uniprotkb/Q96JZ2) (Hematopoietic SH2 domain-containing protein):

> May be a modulator of the apoptotic response through its ability to affect mitochondrial stability (By similarity). Adapter protein involved in tyrosine kinase and CD28 signaling. Seems to affect CD28-mediated activation of the RE/AP element of the interleukin-2 promoter.

**Summary**, from NCBI Gene [84941](https://www.ncbi.nlm.nih.gov/gene/84941):

> T-cell activation requires 2 signals: recognition of antigen by the T-cell receptor (see TCR; MIM 186880) and a costimulatory signal provided primarily by CD28 (MIM 186760) in naive T cells. HSH2 is a target of both of these signaling pathways (Greene et al., 2003 [PubMed 12960172]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24920](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24920) · Entrez [84941](https://www.ncbi.nlm.nih.gov/gene/84941) · UniProt [Q96JZ2](https://www.uniprot.org/uniprotkb/Q96JZ2) · Ensembl [ENSG00000196684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196684)

## Data

Gene col 12265: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12265); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12265, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12265]; `tensor/DDL_lfc|DDL_z.npy` [12265]; `embed/gene_vectors.npy` [12265]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12265 or target_col == 12265). Every well: [[HSH2D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSH2D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
