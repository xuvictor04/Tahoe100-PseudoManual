---
symbol: "MXRA8"
type: "gene"
col: 8533
ensembl_id: "ENSG00000162576"
name: "matrix remodeling associated 8"
location: "1p36.33"
module: 66
arm: "+"
pooled_cpm: 2.78
n_lines_expressing: 17
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 15
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# MXRA8

*matrix remodeling associated 8* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.26× (z +12.8, q 6e-35, up in 5 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.15× (z +7.9, q 6e-13, up in 3 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Pexidartinib (hydrochloride) (drug)]] 5 µM: 0.504× (z -4.8, q 8e-04, down in 1 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYL9]] (+0.73, fdr 7e-06), [[OLFML2A]] (+0.70, fdr 1e-05), [[POSTN]] (+0.64, fdr 3e-05); moves opposite to [[GSTO1]] (-0.53, fdr 4e-05), [[TM4SF19]] (-0.50, fdr 6e-05), [[FBXO45]] (-0.48, fdr 1e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HHIPL2]] → it (grade B ⚠); 15 go from it, the strongest it → [[CLSTN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8533.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.26×** | +12.8 | 6e-35 | 5/5 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.29×** | +12.1 | 2e-31 | 7/7 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.31×** | +9.8 | 2e-20 | 5/5 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +7.9 | 6e-13 | 3/8 (HS-578T, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +6.5 | 1e-08 | 0/9 | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +5.4 | 6e-06 | 3/5 (HepG2/C3A, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.95×** | +4.9 | 9e-05 | 3/7 (CFPAC-1, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.57×** | +4.8 | 9e-05 | 0/10 | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +4.7 | 1e-04 | 3/7 (PANC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +3.9 | 0.005 | 0/7 | top dose only | cell-cycle shift (explains ~16% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.41×** | +3.3 | 0.042 | 2/5 (HS-578T, hTERT-HPNE) | top dose only | noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.58×** | +3.3 | 0.043 | 1/8 (CHP-212) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.62×** | +3.2 | 0.056 | 5/8 (CHP-212, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.86×** | +3.2 | 0.056 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +3.2 | 0.059 | 0/9 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.82×** | +3.1 | 0.069 | 4/5 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.56×** | +3.0 | 0.095 | 0/8 | inconsistent across doses |  |
| [[Isocorydine (drug)]] 5 µM |  | **1.33×** | +2.9 | 0.095 | 0/13 | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.76×** | +2.9 | 0.095 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.55×** | +2.9 | 0.095 | 1/7 (CHP-212) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8533.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.504×** | -4.8 | 8e-04 | 1/12 (RPMI-7951) | inconsistent across doses | position effect removed |
| [[Ciclopirox (drug)]] 0.5 µM |  | **0.601×** | -3.7 | 0.054 | 0/12 | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.626× | -3.4 | 0.11 | 5/11 (HepG2/C3A, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8533. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.66× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 34.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 0.377 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.356 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.256 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.721 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.691 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.437 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.765 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.441 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.290 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.810 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.293 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.371 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8533), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYL9]] | +0.73 | +0.71 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[OLFML2A]] | +0.70 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[POSTN]] | +0.64 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[LUM]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[SAMD11]] | +0.60 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[COL3A1]] | +0.59 | +0.47 / +0.58 | both halves | 2e-05 | STRING 423 |
| [[HHIPL2]] | +0.59 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[EFEMP1]] | +0.59 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[NME4]] | +0.57 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[COL5A2]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[NREP]] | +0.56 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ATP6AP1]] | +0.55 | +0.49 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSTO1]] | -0.53 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[TM4SF19]] | -0.50 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[FBXO45]] | -0.48 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[EFL1]] | -0.47 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[NLRP3]] | -0.47 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[PWP2]] | -0.47 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[SMG9]] | -0.45 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[ARHGAP22]] | -0.45 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[LINC02454]] | -0.45 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[TM4SF19-DYNLT2B]] | -0.45 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[DDX50]] | -0.45 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[CFAP298]] | -0.44 | -0.22 / -0.48 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HHIPL2]] | B | HHIPL2 activity raises MXRA8's level | lines that do not express HHIPL2 (14) vs lines expressing it (36) | 1.74× lower at baseline in the lines without HHIPL2 | 0.087 | ⚠ within organs, on part of the lines; also absent: PRKD1, BNIP3, SPART; maybe low, not absent |
| [[THY1]] | C | THY1 activity raises MXRA8's level | lines that do not express THY1 (38) vs lines expressing it (12) | 2.64× lower at baseline in the lines without THY1 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[COL3A1]] | C | COL3A1 activity raises MXRA8's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 2.06× lower at baseline in the lines without COL3A1 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 11, C 4. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLSTN1]] | B | MXRA8 activity raises CLSTN1's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 1.24× lower at baseline in the lines without MXRA8 | 0.021 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[MYL9]] | B | MXRA8 activity raises MYL9's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 3.44× lower at baseline in the lines without MXRA8 | 0.022 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[MATN3]] | B | MXRA8 activity raises MATN3's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 2.33× lower at baseline in the lines without MXRA8 | 0.025 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[PCOLCE]] | B | MXRA8 activity raises PCOLCE's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 2.73× lower at baseline in the lines without MXRA8 | 0.032 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[FLJ12825]] | B | MXRA8 activity raises FLJ12825's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 1.89× lower at baseline in the lines without MXRA8 | 0.047 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[HOXC4]] | B | MXRA8 activity raises HOXC4's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 1.77× lower at baseline in the lines without MXRA8 | 0.055 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[ROBO1]] | B | MXRA8 activity raises ROBO1's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 3.05× lower at baseline in the lines without MXRA8 | 0.062 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[DDOST]] | B | MXRA8 activity raises DDOST's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 1.32× lower at baseline in the lines without MXRA8 | 0.063 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[TGFBI]] | B | MXRA8 activity raises TGFBI's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 3.02× lower at baseline in the lines without MXRA8 | 0.064 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[NREP]] | B | MXRA8 activity raises NREP's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 2.57× lower at baseline in the lines without MXRA8 | 0.085 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[BEND6]] | B | MXRA8 activity raises BEND6's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 1.83× lower at baseline in the lines without MXRA8 | 0.098 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[RFX8]] | C | MXRA8 activity raises RFX8's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 3.83× lower at baseline in the lines without MXRA8 | 0.021 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.643). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (57.1, 22.9); signed map (43.9, 22.1). **Vector** length 23.1, 4.53% of its response variance represented; |z| ≥ 3 in 290 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *angiogenesis* (hallmark, mean cos +0.55 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.4 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.2 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.1 | +12.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.0 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +0.9 | +0.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +0.9 | +2.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.8 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | +1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -0.7 | +0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.6 | +0.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.5 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | matrix remodeling associated 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,352,689-1,361,777 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp586E2023 |
| Gene groups (HGNC) | V-set domain containing |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRK3](https://www.uniprot.org/uniprotkb/Q9BRK3) (Matrix remodeling-associated protein 8):

> Transmembrane protein which can modulate activity of various signaling pathways, probably via binding to integrin ITGAV:ITGB3. Mediates heterophilic cell-cell interactions in vitro (By similarity). Inhibits osteoclastogenesis downstream of TNFSF11/RANKL and CSF1, where it may function by attenuating signaling via integrin ITGB3 and MAP kinase p38 (By similarity). Plays a role in cartilage formation where it promotes proliferation and maturation of growth plate chondrocytes (By similarity). …

**Summary**, from NCBI Gene [54587](https://www.ncbi.nlm.nih.gov/gene/54587):

> Predicted to be involved in establishment of glial blood-brain barrier. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7542](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7542) · Entrez [54587](https://www.ncbi.nlm.nih.gov/gene/54587) · UniProt [Q9BRK3](https://www.uniprot.org/uniprotkb/Q9BRK3) · Ensembl [ENSG00000162576](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162576)

## Data

Gene col 8533: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8533); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8533, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8533]; `tensor/DDL_lfc|DDL_z.npy` [8533]; `embed/gene_vectors.npy` [8533]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8533 or target_col == 8533). Every well: [[MXRA8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MXRA8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
