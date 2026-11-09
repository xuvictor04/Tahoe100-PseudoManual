---
symbol: "GPD1L"
type: "gene"
col: 7647
ensembl_id: "ENSG00000152642"
name: "glycerol-3-phosphate dehydrogenase 1 like"
location: "3p22.3"
module: 188
arm: "+"
pooled_cpm: 9.39
n_lines_expressing: 46
n_dd_up: 26
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 15
tags: ["gene", "module/188"]
generated_by: "tahoemap"
---

# GPD1L

*glycerol-3-phosphate dehydrogenase 1 like* — 3p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.69× (z +15.7, q 0e+00, up in 42 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.494× (z -12.0, q 1e-30, down in 28 of 41 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.521× (z -7.9, q 6e-13, down in 28 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAR1]] (+0.74, fdr 7e-06), [[METAP1]] (+0.69, fdr 9e-06), [[RPIA]] (+0.69, fdr 7e-06); moves opposite to [[OFD1]] (-0.70, fdr 7e-06), [[RBBP6]] (-0.68, fdr 7e-06), [[ZNF764]] (-0.66, fdr 2e-05).
> It is in [[Module 188]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[WASF3]] → it (grade B ⚠); 15 go from it, the strongest it → [[AKAP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7647.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.69×** | +15.7 | 0e+00 | 42/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.46×** | +15.0 | 0e+00 | 41/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.29×** | +14.3 | 3e-44 | 37/43 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.44×** | +10.8 | 8e-25 | 38/43 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.04×** | +8.6 | 1e-15 | 20/31 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +8.2 | 3e-14 | 10/16 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.82×** | +7.2 | 4e-11 | 29/43 (NCI-H1792, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +7.2 | 5e-11 | 16/25 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.06×** | +7.0 | 1e-10 | 31/44 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +6.6 | 2e-09 | 22/44 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +6.2 | 4e-08 | 24/40 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +5.3 | 6e-06 | 15/32 (NCI-H1792, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.36×** | +5.2 | 7e-06 | 16/39 (LS 180, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +5.0 | 2e-05 | 21/43 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.002 | 14/44 (NCI-H1792, NCI-H2347, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.004 | 13/43 (NCI-H1792, COLO 205, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.006 | 12/42 (BT-474, NCI-H1792, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.016 | 10/39 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.033 | 9/41 (SHP-77, SNU-423, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.060 | 4/43 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **1.27×** | +2.8 | 0.096 | 4/43 (A498, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7647.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.494×** | -12.0 | 1e-30 | 28/41 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.517×** | -8.0 | 5e-13 | 25/40 (HT-29, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.521×** | -7.9 | 6e-13 | 28/43 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.614×** | -5.9 | 5e-07 | 22/42 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.621×** | -5.5 | 4e-06 | 22/41 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.682×** | -4.6 | 4e-04 | 19/38 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.693×** | -4.4 | 7e-04 | 18/42 (SW1417, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.721×** | -3.9 | 0.006 | 14/42 (SW48, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.726×** | -3.9 | 0.007 | 14/42 (PANC-1, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.764×** | -3.3 | 0.065 | 16/43 (A498, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7647. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.41 | 2 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 4.81× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -17.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A498 (line)]] | wt | 14.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -17.3) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.185× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 8.34 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0716× (z -18.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SW480 (line)]] | alt | 11.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.24× (z +11.8) | — |
| [[KATO III (line)]] | alt | 14.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -12.5) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.156× (z -10.9) |
| [[SW48 (line)]] | wt | 27.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -11.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HCT15 (line)]] | alt | 9.28 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0669× (z -9.5) ⚠ toxic; unreliable plate only |
| [[HS-578T (line)]] | alt | 8.10 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -10.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HT-29 (line)]] | alt | 7.30 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0540× (z -12.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -11.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LS 180 (line)]] | wt | 21.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +11.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H460 (line)]] | wt | 5.77 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +8.9) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[RKO (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0950× (z -10.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -9.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7647), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAR1]] | +0.74 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[METAP1]] | +0.69 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[RPIA]] | +0.69 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CCNY]] | +0.68 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[SKP2]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[KDM1A]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[TBC1D24]] | +0.67 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MRS2]] | +0.66 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[GTPBP3]] | +0.66 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[GCSH]] | +0.66 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ZDHHC8]] | +0.65 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[DFFB]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OFD1]] | -0.70 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[RBBP6]] | -0.68 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[ZNF764]] | -0.66 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[SON]] | -0.64 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[HELQ]] | -0.63 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[TOPORS]] | -0.63 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[BPTF]] | -0.62 | -0.62 / -0.46 | both halves | 2e-05 |  |
| [[BOLA1]] | -0.61 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[ANGPT2]] | -0.61 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[ERCC6L2]] | -0.61 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[MRPL45P2]] | -0.61 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[TUT7]] | -0.61 | -0.54 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WASF3]] | B | WASF3 activity lowers GPD1L's level | lines that do not express WASF3 (21) vs lines expressing it (29) | 1.68× higher at baseline in the lines without WASF3 | 0.057 | ⚠ within organs, on part of the lines; also absent: SDC2, COL4A4, IGF2BP1 |
| [[PSAT1]] | B | PSAT1 activity raises GPD1L's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.86× lower at baseline in the lines without PSAT1 | 0.095 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKAP1]] | C | GPD1L activity raises AKAP1's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 2.34× lower at baseline in the lines without GPD1L | 0.008 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[MTRR]] | C | GPD1L activity raises MTRR's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 1.49× lower at baseline in the lines without GPD1L | 0.034 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[GTPBP3]] | C | GPD1L activity raises GTPBP3's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 2.02× lower at baseline in the lines without GPD1L | 0.035 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[CCDC88C]] | C | GPD1L activity raises CCDC88C's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 2.13× lower at baseline in the lines without GPD1L | 0.036 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[SDHAF3]] | C | GPD1L activity raises SDHAF3's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 1.93× lower at baseline in the lines without GPD1L | 0.042 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[ASIC1]] | C | GPD1L activity raises ASIC1's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 2.16× lower at baseline in the lines without GPD1L | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[SKP2]] | C | GPD1L activity raises SKP2's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 2.19× lower at baseline in the lines without GPD1L | 0.055 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[SARS1]] | C | GPD1L activity raises SARS1's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 1.69× lower at baseline in the lines without GPD1L | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[PPARGC1B]] | C | GPD1L activity raises PPARGC1B's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 2.71× lower at baseline in the lines without GPD1L | 0.061 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[IDH1]] | C | GPD1L activity raises IDH1's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 1.86× lower at baseline in the lines without GPD1L | 0.065 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[PCCB]] | C | GPD1L activity raises PCCB's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 1.87× lower at baseline in the lines without GPD1L | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[NDRG3]] | C | GPD1L activity raises NDRG3's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 1.80× lower at baseline in the lines without GPD1L | 0.092 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.799). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.1, -12.8); signed map (-40.6, -14.4). **Vector** length 89.0, 18.4% of its response variance represented; |z| ≥ 3 in 1,081 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.6 | +5.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +8.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +7.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +7.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -8.6 | -12.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -5.6 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -4.8 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | -7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -1.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.5 | -0.7 |
|  | [[Thymol (drug)]] 5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | glycerol-3-phosphate dehydrogenase 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.3 — chr3:32,105,689-32,168,709 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0089 |
| Gene groups (HGNC) | Glycerol-3-phosphate dehydrogenases |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 4 pathways, smallest: Synthesis of PA; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N335](https://www.uniprot.org/uniprotkb/Q8N335) (Glycerol-3-phosphate dehydrogenase 1-like protein):

> Plays a role in regulating cardiac sodium current; decreased enzymatic activity with resulting increased levels of glycerol 3-phosphate activating the DPD1L-dependent SCN5A phosphorylation pathway, may ultimately lead to decreased sodium current; cardiac sodium current may also be reduced due to alterations of NAD(H) balance induced by DPD1L.

**Summary**, from NCBI Gene [23171](https://www.ncbi.nlm.nih.gov/gene/23171):

> The protein encoded by this gene catalyzes the conversion of sn-glycerol 3-phosphate to glycerone phosphate. The encoded protein is found in the cytoplasm, associated with the plasma membrane, where it binds the sodium channel, voltage-gated, type V, alpha subunit (SCN5A). Defects in this gene are a cause of Brugada syndrome type 2 (BRS2) as well as sudden infant death syndrome (SIDS). [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:28956](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28956) · Entrez [23171](https://www.ncbi.nlm.nih.gov/gene/23171) · UniProt [Q8N335](https://www.uniprot.org/uniprotkb/Q8N335) · Ensembl [ENSG00000152642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152642)

## Data

Gene col 7647: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7647); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7647, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7647]; `tensor/DDL_lfc|DDL_z.npy` [7647]; `embed/gene_vectors.npy` [7647]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7647 or target_col == 7647). Every well: [[GPD1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPD1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
