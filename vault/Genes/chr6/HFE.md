---
symbol: "HFE"
type: "gene"
col: 214
ensembl_id: "ENSG00000010704"
name: "homeostatic iron regulator"
location: "6p22.2"
module: 46
arm: "+"
pooled_cpm: 6.64
n_lines_expressing: 45
n_dd_up: 13
n_dd_down: 33
n_dd_up_clean: 10
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# HFE

*homeostatic iron regulator* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +10.5, q 4e-23, up in 27 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.282× (z -13.1, q 1e-36, down in 40 of 42 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASD1]] (+0.69, fdr 2e-05), [[PNISR-AS1]] (+0.67, fdr 3e-05), [[DECR1]] (+0.67, fdr 4e-05); moves opposite to [[SPIRE1]] (-0.63, fdr 3e-05), [[TMEM120B]] (-0.61, fdr 6e-05), [[GPSM1]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CTSO]] → it (grade B ⚠); 2 go from it, the strongest it → [[BANK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 214.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +10.5 | 4e-23 | 27/41 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.69×** | +9.9 | 1e-20 | 10/12 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +6.7 | 3e-09 | 20/29 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.69×** | +5.2 | 2e-05 | 19/40 (A549, MIA PaCa-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.57×** | +4.7 | 3e-04 | 14/41 (NCI-H2030, AsPC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +4.2 | 0.002 | 13/22 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.005 | 10/43 (HOP62, AsPC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.006 | 13/40 (AsPC-1, A498, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.007 | 16/43 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.036 | 8/43 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.050 | 11/43 (LS 180, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.053 | 9/43 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.054 | 7/42 (AsPC-1, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 5 with an alert ⚠; shown: the 15 strongest. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 214.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.282×** | -13.1 | 1e-36 | 40/42 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.287×** | -12.9 | 7e-36 | 38/42 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.288×** | -12.9 | 8e-36 | 36/43 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.429×** | -8.8 | 2e-16 | 30/40 (NCI-H460, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.449×** | -8.3 | 1e-14 | 33/43 (NCI-H23, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.506×** | -7.1 | 2e-10 | 28/43 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.628×** | -6.8 | 8e-10 | 26/40 (NCI-H460, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.521×** | -6.8 | 1e-09 | 25/42 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.670×** | -5.9 | 3e-07 | 26/43 (Panc 03.27, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.599×** | -5.3 | 7e-06 | 22/41 (SNU-1, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.607×** | -5.2 | 1e-05 | 17/39 (HT-29, SW 900, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.608×** | -5.2 | 1e-05 | 21/39 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.612×** | -5.1 | 2e-05 | 20/41 (NCI-H460, RKO, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.625×** | -4.9 | 5e-05 | 19/41 (Hs 766T, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.434×** | -4.5 | 2e-04 | 16/37 (NCI-H1792, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 214. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.99 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 5.50× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0981× (z -12.9) |
| [[COLO 205 (line)]] | alt | 8.85 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0510× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 5.87 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0602× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 17.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -11.5) |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0636× (z -9.4) |
| [[SNU-423 (line)]] | alt | 9.41 | 0 | 2 | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0729× (z -10.7) |
| [[SW480 (line)]] | alt | 4.84 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.1000× (z -11.4) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.144× (z -9.5) |
| [[A-427 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.129× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~45% of this change |
| [[C-33 A (line)]] | alt | 9.79 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0900× (z -8.6) |
| [[C32 (line)]] | wt | 2.71 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0487× (z -8.5) |
| [[HCT15 (line)]] | alt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -8.6) |
| [[HT-29 (line)]] | alt | 8.22 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.138× (z -8.7) |
| [[KATO III (line)]] | alt | 8.19 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0844× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 3.43 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0683× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 5.79 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0831× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 9.31 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -8.9) |
| [[A-172 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.585 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.766 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.661 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 214), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASD1]] | +0.69 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[PNISR-AS1]] | +0.67 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[DECR1]] | +0.67 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[TET2]] | +0.66 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[PDIA3P1]] | +0.66 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[C5orf15]] | +0.65 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[VPS52]] | +0.65 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[NNT]] | +0.64 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[NXT2]] | +0.64 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[TGFB3]] | +0.64 | +0.37 / +0.53 | both halves | 9e-05 |  |
| [[TAPBPL]] | +0.63 | +0.37 / +0.57 | both halves | 9e-05 | same gene group |
| [[DHRS4]] | +0.63 | +0.53 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPIRE1]] | -0.63 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[TMEM120B]] | -0.61 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[GPSM1]] | -0.60 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[CSGALNACT2]] | -0.60 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[GPR157]] | -0.59 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[FANCE]] | -0.59 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[PUSL1]] | -0.59 | -0.44 / -0.26 | both halves | 4e-04 |  |
| [[DVL1]] | -0.59 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[TMEM184B]] | -0.59 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[ZFYVE28]] | -0.58 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[SPATA2L]] | -0.58 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[ZXDC]] | -0.58 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSO]] | B | CTSO activity raises HFE's level | lines that do not express CTSO (8) vs lines expressing it (42) | 1.32× lower at baseline in the lines without CTSO | 0.009 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |
| [[MAP2K1]] | B | MAP2K1 activity lowers HFE's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[MAP2K2]] | B | MAP2K2 activity lowers HFE's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BANK1]] | B | HFE activity lowers BANK1's level | lines that do not express HFE (5) vs lines expressing it (45) | 1.48× higher at baseline in the lines without HFE | 0.060 | ⚠ within organs, on part of the lines; also absent: HOXA-AS2, PIM1, CBR1; its own permutation p |
| [[AP5M1]] | B | HFE activity lowers AP5M1's level | lines that do not express HFE (5) vs lines expressing it (45) | 1.36× higher at baseline in the lines without HFE | 0.067 | ⚠ within organs, on part of the lines; also absent: HOXA-AS2, PIM1, CBR1 |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.703). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.2, 12.4); signed map (25.4, -21.1). **Vector** length 75.8, 14.7% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +5.2 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.3 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | -1.6 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.9 | -13.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -12.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.5 | -12.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.0 | -8.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | homeostatic iron regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.2 — chr6:26,087,226-26,098,343 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HLA-H, HFE1 |
| Gene groups (HGNC) | C1-set domain containing |
| Reactome | 3 pathways, smallest: Transferrin endocytosis and recycling; Iron uptake and transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q30201](https://www.uniprot.org/uniprotkb/Q30201) (Hereditary hemochromatosis protein):

> Binds to transferrin receptor (TFR) and reduces its affinity for iron-loaded transferrin.

**Summary**, from NCBI Gene [3077](https://www.ncbi.nlm.nih.gov/gene/3077):

> The protein encoded by this gene is a membrane protein that is similar to MHC class I-type proteins and associates with beta2-microglobulin (beta2M). It is thought that this protein functions to regulate iron absorption by regulating the interaction of the transferrin receptor with transferrin. The iron storage disorder, hereditary haemochromatosis, is a recessive genetic disorder that results from defects in this gene. [provided by RefSeq, May 2022]

**Accessions** — [HGNC:4886](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4886) · Entrez [3077](https://www.ncbi.nlm.nih.gov/gene/3077) · UniProt [Q30201](https://www.uniprot.org/uniprotkb/Q30201) · Ensembl [ENSG00000010704](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010704)

## Data

Gene col 214: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 214); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 214, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 214]; `tensor/DDL_lfc|DDL_z.npy` [214]; `embed/gene_vectors.npy` [214]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 214 or target_col == 214). Every well: [[HFE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HFE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
