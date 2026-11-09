---
symbol: "PLEKHG6"
type: "gene"
col: 169
ensembl_id: "ENSG00000008323"
name: "pleckstrin homology and RhoGEF domain containing G6"
location: "12p13.31"
module: 44
arm: "+"
pooled_cpm: 6.95
n_lines_expressing: 24
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 119
direction_downstream: 133
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# PLEKHG6

*pleckstrin homology and RhoGEF domain containing G6* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.52× (z +10.0, q 1e-20, up in 0 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.46× (z +5.9, q 6e-07, up in 6 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.582× (z -6.1, q 6e-07, down in 12 of 21 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.646× (z -4.9, q 3e-04, down in 15 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TJP3]] (+0.82, fdr 7e-06), [[MUC3A]] (+0.81, fdr 7e-06), [[PRR15L]] (+0.79, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 119 arrows point to it, the strongest [[C4orf19]] → it (grade B ⚠); 133 go from it, the strongest it → [[KIAA1522]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 169.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.52×** | +10.0 | 1e-20 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.93×** | +7.4 | 5e-11 | 2/14 (NCI-H1573, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +5.9 | 6e-07 | 6/20 (HEC-1-A, BT-474, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +5.6 | 3e-06 | 14/21 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +4.5 | 9e-04 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.3 | 0.002 | 1/20 (HEC-1-A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 0.002 | 11/21 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +4.2 | 0.002 | 2/19 (SW48, NCI-H1573) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.1 | 0.002 | 4/17 (CFPAC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.4 | 0.035 | 0/15 | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.36×** | +3.4 | 0.035 | 9/21 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.058 | 3/20 (AsPC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.082 | 4/20 (NCI-H1573, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.082 | 3/21 (LoVo, SW1417, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.090 | 1/19 (HepG2/C3A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.090 | 3/21 (NCI-H23, SW1417, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 169.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.582×** | -6.1 | 6e-07 | 12/21 (HT-29, SW1417, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.646×** | -4.9 | 3e-04 | 15/21 (LS 180, AsPC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.719×** | -3.7 | 0.039 | 12/21 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.738×** | -3.4 | 0.087 | 10/21 (AsPC-1, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 0.751× | -3.2 | 0.15 | 7/21 (HT-29, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 169. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 45.5 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -15.8) |
| [[KATO III (line)]] | alt | 32.8 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -14.3) |
| [[LoVo (line)]] | wt | 19.2 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 17.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -10.9) |
| [[LS 180 (line)]] | wt | 18.9 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.171× (z -10.1) |
| [[SW1417 (line)]] | alt | 24.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -10.2) |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0437× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.142× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 16.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -10.6) |
| [[A-172 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.880 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.834 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 169), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TJP3]] | +0.82 | +0.73 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[MUC3A]] | +0.81 | +0.70 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[PRR15L]] | +0.79 | +0.69 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[CYP4F12]] | +0.78 | +0.69 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[MUC13]] | +0.75 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[LGALS4]] | +0.75 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[CLIC5]] | +0.75 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[TMPRSS2]] | +0.74 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[POF1B]] | +0.74 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[GCNT3]] | +0.74 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[CLDN3]] | +0.74 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[PRR15]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*119 arrows, 119 of them with an alert ⚠; grade A 0, B 11, C 108. Shown: the 12 strongest; 107 more arrows (107 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C4orf19]] | B | C4orf19 activity raises PLEKHG6's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 2.46× lower at baseline in the lines without C4orf19 | 0.007 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[PLSCR4]] | B | PLSCR4 activity raises PLEKHG6's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.65× lower at baseline in the lines without PLSCR4 | 0.035 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[PLEKHG1]] | B | PLEKHG1 activity raises PLEKHG6's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 1.95× lower at baseline in the lines without PLEKHG1 | 0.037 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[CDC42EP5]] | B | CDC42EP5 activity raises PLEKHG6's level | lines that do not express CDC42EP5 (11) vs lines expressing it (39) | 2.78× lower at baseline in the lines without CDC42EP5 | 0.047 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LRP4]] | B | LRP4 activity lowers PLEKHG6's level | lines that do not express LRP4 (16) vs lines expressing it (34) | 1.83× higher at baseline in the lines without LRP4 | 0.049 | ⚠ within organs, on part of the lines |
| [[ATP8B1]] | B | ATP8B1 activity raises PLEKHG6's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.45× lower at baseline in the lines without ATP8B1 | 0.056 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[LNX1]] | B | LNX1 activity raises PLEKHG6's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 1.96× lower at baseline in the lines without LNX1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[GAREM1]] | B | GAREM1 activity raises PLEKHG6's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 2.51× lower at baseline in the lines without GAREM1 | 0.062 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises PLEKHG6's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.38× lower at baseline in the lines without ELF3-AS1 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[CRACR2B]] | B | CRACR2B activity raises PLEKHG6's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 2.45× lower at baseline in the lines without CRACR2B | 0.064 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[IGSF9]] | B | IGSF9 activity raises PLEKHG6's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 2.01× lower at baseline in the lines without IGSF9 | 0.098 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[ST14]] | C | ST14 activity raises PLEKHG6's level | lines that do not express ST14 (32) vs lines expressing it (18) | 5.08× lower at baseline in the lines without ST14 | 4e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |

### Downstream of this gene

*133 arrows, 133 of them with an alert ⚠; grade A 0, B 37, C 96. Shown: the 12 strongest; 121 more arrows (121 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA1522]] | B | PLEKHG6 activity raises KIAA1522's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 3.36× lower at baseline in the lines without PLEKHG6 | 0.001 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[ARHGEF16]] | B | PLEKHG6 activity raises ARHGEF16's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 3.46× lower at baseline in the lines without PLEKHG6 | 0.001 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[ELF3-AS1]] | B | PLEKHG6 activity raises ELF3-AS1's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 3.48× lower at baseline in the lines without PLEKHG6 | 0.002 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[RSPH1]] | B | PLEKHG6 activity raises RSPH1's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 2.17× lower at baseline in the lines without PLEKHG6 | 0.002 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[PLS1]] | B | PLEKHG6 activity raises PLS1's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 3.84× lower at baseline in the lines without PLEKHG6 | 0.005 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[DLG3]] | B | PLEKHG6 activity raises DLG3's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 3.16× lower at baseline in the lines without PLEKHG6 | 0.005 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[MROH7]] | B | PLEKHG6 activity raises MROH7's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 2.49× lower at baseline in the lines without PLEKHG6 | 0.006 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[IGSF9]] | B | PLEKHG6 activity raises IGSF9's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 1.96× lower at baseline in the lines without PLEKHG6 | 0.008 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[PLEKHA7]] | B | PLEKHG6 activity raises PLEKHA7's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 2.82× lower at baseline in the lines without PLEKHG6 | 0.009 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[LNX1]] | B | PLEKHG6 activity raises LNX1's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 3.95× lower at baseline in the lines without PLEKHG6 | 0.010 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[GAREM1]] | B | PLEKHG6 activity raises GAREM1's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 2.97× lower at baseline in the lines without PLEKHG6 | 0.018 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[C4orf19]] | B | PLEKHG6 activity raises C4orf19's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 2.26× lower at baseline in the lines without PLEKHG6 | 0.021 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.840). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.5, 52.7); signed map (61.9, 5.1). **Vector** length 62.0, 17.6% of its response variance represented; |z| ≥ 3 in 422 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.63 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.63 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.63 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +10.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.2 | +0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +3.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -6.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -4.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology and RhoGEF domain containing G6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,310,436-6,328,506 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10665, MYOGEF, ARHGEF46 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Reactome | 5 pathways, smallest: RHOA GTPase cycle; RAC1 GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3KR16](https://www.uniprot.org/uniprotkb/Q3KR16) (Pleckstrin homology domain-containing family G member 6):

> Guanine nucleotide exchange factor activating the small GTPase RHOA, which, in turn, induces myosin filament formation. Also activates RHOG. Does not activate RAC1, or to a much lower extent than RHOA and RHOG. Part of a functional unit, involving PLEKHG6, MYH10 and RHOA, at the cleavage furrow to advance furrow ingression during cytokinesis. In epithelial cells, required for the formation of microvilli and membrane ruffles on the apical pole. Along with EZR, required for normal …

**Summary**, from NCBI Gene [55200](https://www.ncbi.nlm.nih.gov/gene/55200):

> Predicted to enable guanyl-nucleotide exchange factor activity. Predicted to be involved in regulation of small GTPase mediated signal transduction. Located in cell junction. Implicated in cystic fibrosis. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25562](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25562) · Entrez [55200](https://www.ncbi.nlm.nih.gov/gene/55200) · UniProt [Q3KR16](https://www.uniprot.org/uniprotkb/Q3KR16) · Ensembl [ENSG00000008323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008323)

## Data

Gene col 169: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 169); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 169, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 169]; `tensor/DDL_lfc|DDL_z.npy` [169]; `embed/gene_vectors.npy` [169]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 169 or target_col == 169). Every well: [[PLEKHG6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHG6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
