---
symbol: "RAP2C-AS1"
type: "gene"
col: 13839
ensembl_id: "ENSG00000232160"
name: "RAP2C antisense RNA 1"
location: "Xq26.2"
module: 10
arm: "+"
pooled_cpm: 8.76
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 10
n_dd_up_clean: 25
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# RAP2C-AS1

*RAP2C antisense RNA 1* — Xq26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.14× (z +19.3, q 0e+00, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.486× (z -6.0, q 9e-07, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00667]] (+0.80, fdr 7e-06), [[TAFA2]] (+0.76, fdr 7e-06), [[PDCL3P4]] (+0.75, fdr 1e-05); moves opposite to [[GPR89B]] (-0.72, fdr 1e-05), [[CCDC134]] (-0.69, fdr 1e-05), [[GPR89A]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13839.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.14×** | +19.3 | 0e+00 | 41/43 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.54×** | +11.0 | 1e-25 | 31/43 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.43×** | +9.9 | 8e-21 | 36/41 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.30×** | +6.9 | 5e-10 | 26/41 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +6.8 | 2e-09 | 29/44 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +6.5 | 9e-09 | 23/36 (AsPC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.68×** | +6.1 | 6e-08 | 28/47 (LS 180, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.22×** | +6.1 | 6e-08 | 13/20 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.05×** | +6.0 | 1e-07 | 32/47 (A498, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +5.7 | 6e-07 | 7/14 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.91×** | +5.4 | 4e-06 | 31/47 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.95×** | +4.7 | 1e-04 | 22/45 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.4 | 5e-04 | 22/48 (A498, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.69×** | +4.2 | 9e-04 | 19/46 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +3.8 | 0.005 | 13/46 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.006 | 18/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +3.7 | 0.006 | 16/47 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.53×** | +3.6 | 0.011 | 13/45 (SW480, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13839.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.486×** | -6.0 | 9e-07 | 29/47 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.508×** | -5.7 | 4e-06 | 27/43 (SHP-77, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.569×** | -4.7 | 5e-04 | 26/47 (RPMI-7951, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.580×** | -4.6 | 7e-04 | 23/46 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.628×** | -3.9 | 0.011 | 21/46 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.618×** | -3.8 | 0.014 | 23/45 (HS-578T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.644×** | -3.7 | 0.020 | 17/48 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.661×** | -3.5 | 0.038 | 16/46 (NCI-H23, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.480×** | -3.2 | 0.078 | 7/44 (NCI-H23, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.683×** | -3.2 | 0.078 | 18/47 (SK-MEL-2, HCT15, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13839. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 5.19 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.105× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 25.9 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +9.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0873× (z -12.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -8.8) |
| [[PANC-1 (line)]] | alt | 5.69 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +11.2) | [[Digitoxin (drug)]] 0.05 µM 0.114× (z -9.9) |
| [[A-172 (line)]] | wt | 5.51 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +9.3) | [[Malotilate (drug)]] 0.05 µM 0.0795× (z -9.0) |
| [[HOP62 (line)]] | alt | 12.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.03× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 5.09 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.71× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 6.65 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.47× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.0777× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 6.55 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.73× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.0638× (z -10.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 5.35 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.51× (z +8.5) | [[Hesperidin (drug)]] 0.5 µM 0.0607× (z -8.9) |
| [[A-427 (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 4.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +13.8) | — |
| [[AsPC-1 (line)]] | alt | 2.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 4.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +11.9) | — |
| [[HCT15 (line)]] | alt | 6.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 7.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.08× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 5.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.31× (z +12.7) | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0667× (z -11.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 55.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.168× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 3.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 3.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +10.6) | — |
| [[SW48 (line)]] | wt | 6.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +8.7) | — |
| [[SW480 (line)]] | alt | 6.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.57× (z +11.2) | — |
| [[A549 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13839), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00667]] | +0.80 | +0.82 / +0.63 | both halves | 7e-06 |  |
| [[TAFA2]] | +0.76 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[PDCL3P4]] | +0.75 | +0.85 / +0.49 | both halves | 1e-05 |  |
| [[WAC-AS1]] | +0.74 | +0.80 / +0.58 | both halves | 8e-06 | same gene group |
| [[PCNX4-DT]] | +0.73 | +0.81 / +0.52 | both halves | 1e-05 |  |
| [[LEKR1]] | +0.72 | +0.82 / +0.38 | both halves | 6e-05 |  |
| [[ZBED5-AS1]] | +0.71 | +0.75 / +0.50 | both halves | 1e-05 | same gene group |
| [[RNF32]] | +0.71 | +0.77 / +0.48 | both halves | 2e-05 |  |
| [[MAD2L1-DT]] | +0.70 | +0.82 / +0.37 | both halves | 8e-05 |  |
| [[CFAP418-AS1]] | +0.69 | +0.70 / +0.48 | both halves | 2e-05 | same gene group |
| [[TMEM232]] | +0.68 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[F8]] | +0.68 | +0.77 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR89B]] | -0.72 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[CCDC134]] | -0.69 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[GPR89A]] | -0.65 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[L2HGDH]] | -0.65 | -0.66 / -0.37 | both halves | 8e-05 |  |
| [[PHKA2]] | -0.64 | -0.72 / -0.37 | both halves | 8e-05 |  |
| [[KLHL8]] | -0.64 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[SMYD4]] | -0.63 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[MAST3]] | -0.61 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[FAM118A]] | -0.60 | -0.61 / -0.36 | both halves | 9e-05 |  |
| [[NBPF3]] | -0.59 | -0.64 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RAP2C-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises RAP2C-AS1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[C5]] | C | C5 activity raises RAP2C-AS1's level | lines that do not express C5 (4) vs lines expressing it (46) | 1.98× lower at baseline in the lines without C5 | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLSPN, PRDM6, TCF19; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.798). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.4, 15.3); signed map (28.6, -11.0). **Vector** length 81.0, 16.7% of its response variance represented; |z| ≥ 3 in 1,123 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +19.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.9 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +1.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.4 | -3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | +3.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.1 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -2.5 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.8 | -2.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | RAP2C antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq26.2 — chrX:132,217,053-132,432,862 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40957](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40957) · Entrez [101928578](https://www.ncbi.nlm.nih.gov/gene/101928578) · Ensembl [ENSG00000232160](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232160)

## Data

Gene col 13839: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13839); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13839, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13839]; `tensor/DDL_lfc|DDL_z.npy` [13839]; `embed/gene_vectors.npy` [13839]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13839 or target_col == 13839). Every well: [[RAP2C-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAP2C-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
