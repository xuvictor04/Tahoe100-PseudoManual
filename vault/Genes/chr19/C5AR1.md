---
symbol: "C5AR1"
type: "gene"
col: 12394
ensembl_id: "ENSG00000197405"
name: "complement C5a receptor 1"
location: "19q13.32"
module: 38
arm: "+"
pooled_cpm: 12.82
n_lines_expressing: 47
n_dd_up: 19
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# C5AR1

*complement C5a receptor 1* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.87× (z +11.9, q 4e-30, up in 36 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.243× (z -11.4, q 3e-27, down in 34 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C19orf38]] (+0.76, fdr 7e-06), [[PILRA]] (+0.73, fdr 7e-06), [[GARIN1A]] (+0.73, fdr 7e-06); moves opposite to [[BTBD3]] (-0.58, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[PYGM]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12394.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.87×** | +11.9 | 4e-30 | 36/40 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +6.6 | 1e-08 | 24/42 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.29×** | +6.1 | 2e-07 | 16/29 (HEC-1-A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +6.0 | 3e-07 | 29/39 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +5.7 | 2e-06 | 31/44 (A-172, SW1417, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +5.5 | 3e-06 | 8/24 (SW1417, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +5.5 | 4e-06 | 15/30 (HEC-1-A, SW1417, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **1.96×** | +5.4 | 5e-06 | 25/45 (HT-29, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +4.4 | 6e-04 | 17/45 (hTERT-HPNE, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.79×** | +4.1 | 0.002 | 20/45 (KATO III, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.65×** | +4.0 | 0.003 | 16/42 (SW1417, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.68×** | +4.0 | 0.003 | 18/40 (SW480, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +3.9 | 0.004 | 18/41 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.030 | 14/45 (HOP62, A498, …) | rises with dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.59×** | +3.4 | 0.030 | 16/45 (A549, A498, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.54×** | +3.1 | 0.066 | 16/42 (A549, A498, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +2.9 | 0.091 | 15/40 (NCI-H460, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12394.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.243×** | -11.4 | 3e-27 | 34/42 (KATO III, HT-29, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.267×** | -9.4 | 1e-18 | 34/45 (HT-29, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.334×** | -8.8 | 2e-16 | 31/42 (A-427, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.303×** | -8.5 | 2e-15 | 36/39 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.253×** | -5.8 | 8e-07 | 30/42 (AsPC-1, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.534×** | -5.0 | 4e-05 | 21/41 (KATO III, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.506×** | -4.9 | 9e-05 | 22/44 (RPMI-7951, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.517×** | -4.8 | 1e-04 | 27/43 (SW 900, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.334×** | -4.6 | 3e-04 | 25/40 (SW 900, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.339×** | -4.6 | 3e-04 | 21/38 (A-427, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.702×** | -4.0 | 0.003 | 20/43 (AsPC-1, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.627×** | -3.8 | 0.008 | 19/41 (AsPC-1, SW480, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.05 µM |  | **0.656×** | -3.4 | 0.029 | 17/41 (SW 900, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.665×** | -3.1 | 0.069 | 16/41 (HT-29, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.762×** | -3.1 | 0.069 | 13/43 (CFPAC-1, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12394. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 36.1 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0681× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0985× (z -12.7) |
| [[PANC-1 (line)]] | alt | 12.7 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +8.5) | [[Digitoxin (drug)]] 0.5 µM 0.143× (z -9.9) |
| [[SW1417 (line)]] | alt | 18.1 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.75× (z +9.9) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.0344× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.158× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 20.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 8.45 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0640× (z -9.4) |
| [[SW480 (line)]] | alt | 10.3 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.117× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.195× (z -8.9) |
| [[H4 (line)]] | wt | 32.3 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0773× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 15.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0526× (z -11.6) |
| [[A-172 (line)]] | wt | 5.73 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0612× (z -8.8) |
| [[A-427 (line)]] | wt | 13.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0245× (z -14.8) |
| [[BT-474 (line)]] | alt | 17.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0565× (z -12.4) |
| [[HCT15 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0600× (z -10.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 23.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -10.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 7.08 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0756× (z -8.6) |
| [[KATO III (line)]] | alt | 13.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0373× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 6.49 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0724× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 5.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.84× (z +11.9) | — |
| [[RKO (line)]] | wt | 7.45 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.103× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0527× (z -9.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 6.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0852× (z -9.0) |
| [[A498 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12394), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C19orf38]] | +0.76 | +0.79 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PILRA]] | +0.73 | +0.78 / +0.66 | both halves | 7e-06 | STRING 462 |
| [[GARIN1A]] | +0.73 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[AVIL]] | +0.71 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[USP50]] | +0.70 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.70 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[VWCE]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[PPIEL]] | +0.68 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[HCLS1]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PPIEL-1]] | +0.66 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[C3orf20]] | +0.66 | +0.72 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTBD3]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers C5AR1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PTPN6]] | B | PTPN6 activity raises C5AR1's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.93× lower at baseline in the lines without PTPN6 | 0.034 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[MROH3P]] | B | MROH3P activity raises C5AR1's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 1.50× lower at baseline in the lines without MROH3P | 0.049 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[C21orf91-OT1]] | B | C21orf91-OT1 activity raises C5AR1's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 1.90× lower at baseline in the lines without C21orf91-OT1 | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[BTG3-AS1]] | B | BTG3-AS1 activity raises C5AR1's level | lines that do not express BTG3-AS1 (7) vs lines expressing it (43) | 1.22× lower at baseline in the lines without BTG3-AS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: DUSP8, USP43, EFNA2; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYGM]] | C | C5AR1 activity raises PYGM's level | lines that do not express C5AR1 (3) vs lines expressing it (47) | 2.04× lower at baseline in the lines without C5AR1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FARP1, PER3, NECAB2; maybe low, not absent; its own permutation p |
| [[EPHX3]] | C | C5AR1 activity raises EPHX3's level | lines that do not express C5AR1 (3) vs lines expressing it (47) | 1.85× lower at baseline in the lines without C5AR1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FARP1, PER3, NECAB2; maybe low, not absent; its own permutation p |
| [[FAM209A]] | C | C5AR1 activity raises FAM209A's level | lines that do not express C5AR1 (3) vs lines expressing it (47) | 1.24× lower at baseline in the lines without C5AR1 | 0.068 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FARP1, PER3, NECAB2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.8, -16.2); signed map (16.0, 10.6). **Vector** length 101, 25.4% of its response variance represented; |z| ≥ 3 in 1,307 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.9 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +1.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.9 | -11.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.2 | -8.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -4.1 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.0 | -4.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | +0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -1.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | complement C5a receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:47,290,023-47,322,066 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C5A, C5AR, CD88; previously C5R1 |
| Gene groups (HGNC) | Complement component GPCRs; CD molecules; Complement system regulators and receptors |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 10 pathways, smallest: Regulation of Complement cascade; Complement cascade; Peptide ligand-binding receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P21730](https://www.uniprot.org/uniprotkb/P21730) (C5a anaphylatoxin chemotactic receptor 1):

> Receptor for the chemotactic and inflammatory peptide anaphylatoxin C5a, stimulating chemotaxis, granule enzyme release, intracellular calcium release and superoxide anion production. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as adenylate cyclase. C5AR1 is coupled to G(i)/G(o) (GNAI1 or GNAO1) G alpha proteins and mediates inhibition of adenylate cyclase. The …

**Summary**, from NCBI Gene [728](https://www.ncbi.nlm.nih.gov/gene/728):

> Enables G protein-coupled receptor activity and complement component C5a receptor activity. Involved in several processes, including G protein-coupled receptor signaling pathway; mRNA transcription by RNA polymerase II; and positive regulation of ERK1 and ERK2 cascade. Located in apical part of cell and basolateral plasma membrane. Is active in plasma membrane. Biomarker of Alzheimer's disease; asthma; chronic obstructive pulmonary disease; rhinitis; and severe acute respiratory syndrome. …

**Accessions** — [HGNC:1338](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1338) · Entrez [728](https://www.ncbi.nlm.nih.gov/gene/728) · UniProt [P21730](https://www.uniprot.org/uniprotkb/P21730) · Ensembl [ENSG00000197405](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197405)

## Data

Gene col 12394: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12394); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12394, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12394]; `tensor/DDL_lfc|DDL_z.npy` [12394]; `embed/gene_vectors.npy` [12394]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12394 or target_col == 12394). Every well: [[C5AR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C5AR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
