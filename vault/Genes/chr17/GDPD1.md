---
symbol: "GDPD1"
type: "gene"
col: 7758
ensembl_id: "ENSG00000153982"
name: "glycerophosphodiester phosphodiesterase domain containing 1"
location: "17q22"
module: 190
arm: "+"
pooled_cpm: 10.87
n_lines_expressing: 46
n_dd_up: 36
n_dd_down: 16
n_dd_up_clean: 29
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/190"]
generated_by: "tahoemap"
---

# GDPD1

*glycerophosphodiester phosphodiesterase domain containing 1* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.03× (z +13.0, q 4e-36, up in 34 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.465× (z -10.1, q 3e-21, down in 32 of 43 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC11A2]] (+0.57, fdr 2e-05), [[SLC18B1]] (+0.54, fdr 7e-05), [[QPRT]] (+0.53, fdr 1e-05); moves opposite to [[WDR27]] (-0.54, fdr 4e-05), [[BRD9]] (-0.53, fdr 8e-05), [[ERVK13-1]] (-0.53, fdr 2e-04).
> It is in [[Module 190]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC5A4-AS1]] → it (grade B ⚠); 2 go from it, the strongest it → [[ZNF540]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7758.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.03×** | +13.0 | 4e-36 | 34/43 (A498, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.12×** | +9.8 | 2e-20 | 30/43 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.96×** | +8.8 | 3e-16 | 33/43 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +8.5 | 3e-15 | 26/43 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +8.3 | 1e-14 | 25/43 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +7.7 | 1e-12 | 22/40 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +7.2 | 4e-11 | 25/43 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +6.3 | 2e-08 | 8/14 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.40×** | +6.2 | 3e-08 | 18/43 (RKO, A498, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +6.1 | 5e-08 | 18/33 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.62×** | +6.0 | 9e-08 | 18/42 (HEC-1-A, A-427, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +5.9 | 1e-07 | 23/41 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.30×** | +5.7 | 5e-07 | 21/43 (A498, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +5.7 | 5e-07 | 14/33 (J82, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +5.6 | 1e-06 | 24/43 (KATO III, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.46×** | +5.0 | 3e-05 | 13/43 (BT-474, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.42×** | +4.5 | 2e-04 | 12/43 (KATO III, BT-474, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.40×** | +4.4 | 4e-04 | 10/43 (A549, RKO, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +4.3 | 5e-04 | 15/43 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7758.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.465×** | -10.1 | 3e-21 | 32/43 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.466×** | -10.1 | 3e-21 | 30/43 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.525×** | -8.5 | 4e-15 | 29/43 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.548×** | -7.9 | 3e-13 | 28/40 (HepG2/C3A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.384×** | -6.6 | 5e-09 | 23/43 (BT-474, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.634×** | -6.0 | 2e-07 | 23/43 (BT-474, SW480, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.428×** | -5.8 | 4e-07 | 20/37 (BT-474, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.677×** | -5.1 | 2e-05 | 18/43 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.695×** | -4.8 | 1e-04 | 20/43 (BT-474, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.705×** | -4.4 | 5e-04 | 18/36 (BT-474, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.735×** | -4.1 | 0.002 | 18/42 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.755×** | -3.7 | 0.010 | 5/43 (BT-474, NCI-H2030, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.623×** | -3.3 | 0.047 | 11/38 (KATO III, A549, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.783×** | -3.2 | 0.047 | 14/39 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.783×** | -3.2 | 0.047 | 10/43 (BT-474, NCI-H661, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7758. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 125 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -14.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.180× (z -12.1) |
| [[SW480 (line)]] | alt | 13.2 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0984× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.151× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -9.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.207× (z -9.4) ⚠ toxic |
| [[A498 (line)]] | wt | 6.72 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.47× (z +9.0) | — |
| [[A549 (line)]] | wt | 5.23 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0756× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 9.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0686× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 16.0 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.115× (z -11.2) |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0751× (z -9.2) |
| [[SNU-423 (line)]] | alt | 9.82 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.128× (z -9.7) |
| [[SW48 (line)]] | wt | 17.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0406× (z -13.4) |
| [[A-172 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7758), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC11A2]] | +0.57 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[SLC18B1]] | +0.54 | +0.38 / +0.60 | both halves | 7e-05 |  |
| [[QPRT]] | +0.53 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[LINC01012]] | +0.52 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[CIBAR1]] | +0.51 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[DSTYK]] | +0.51 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TMCC2]] | +0.50 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[CCDC126]] | +0.49 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[CDC14B]] | +0.49 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[TPD52L1]] | +0.48 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[BCAS4]] | +0.48 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[GKAP1]] | +0.48 | +0.49 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR27]] | -0.54 | -0.43 / -0.46 | both halves | 4e-05 |  |
| [[BRD9]] | -0.53 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[ERVK13-1]] | -0.53 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[TRIP13]] | -0.47 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[PPP1CA]] | -0.46 | -0.37 / -0.52 | both halves | 9e-05 |  |
| [[PDK1-AS1]] | -0.45 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[NOP9]] | -0.45 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[LARP4B]] | -0.44 | -0.27 / -0.54 | both halves | 3e-04 |  |
| [[DDX5]] | -0.44 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[CACTIN]] | -0.43 | -0.26 / -0.37 | both halves | 4e-04 |  |
| [[ATXN1L]] | -0.43 | -0.20 / -0.64 | ⚠ one half (not replicated) | 8e-04 |  |
| [[NCAPH2]] | -0.43 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[MAPK7]] | -0.42 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC5A4-AS1]] | B | SLC5A4-AS1 activity raises GDPD1's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 2.23× lower at baseline in the lines without SLC5A4-AS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF540]] | C | GDPD1 activity raises ZNF540's level | lines that do not express GDPD1 (4) vs lines expressing it (46) | 1.94× lower at baseline in the lines without GDPD1 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent; its own permutation p |
| [[ZFP14]] | C | GDPD1 activity raises ZFP14's level | lines that do not express GDPD1 (4) vs lines expressing it (46) | 1.81× lower at baseline in the lines without GDPD1 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent |

## Where it sits

- **Module**: [[Module 190]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.509). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.8, 12.3); signed map (-26.1, -4.4). **Vector** length 68.7, 12.2% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +13.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +5.7 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.0 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +2.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.0 | -4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | glycerophosphodiester phosphodiesterase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:59,220,467-59,275,970 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37451, GDE4 |
| Reactome | 4 pathways, smallest: Glycerophospholipid catabolism; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N9F7](https://www.uniprot.org/uniprotkb/Q8N9F7) (Lysophospholipase D GDPD1):

> Hydrolyzes lysoglycerophospholipids to produce lysophosphatidic acid (LPA) and the corresponding amines. Shows a preference for 1-O-alkyl-sn-glycero-3-phosphocholine (lyso-PAF), lysophosphatidylethanolamine (lyso-PE) and lysophosphatidylcholine (lyso-PC). May be involved in bioactive N-acylethanolamine biosynthesis from both N-acyl-lysoplasmenylethanolamin (N-acyl-lysoPlsEt) and N-acyl-lysophosphatidylethanolamin (N-acyl-lysoPE). In addition, hydrolyzes glycerophospho-N-acylethanolamine to …

**Summary**, from NCBI Gene [284161](https://www.ncbi.nlm.nih.gov/gene/284161):

> This gene encodes a member of the glycerophosphodiester phosphodiesterase family of enzymes that catalyze the hydrolysis of deacylated glycerophospholipids to glycerol phosphate and alcohol. The encoded protein is localized to the cytoplasm and concentrates near the perinuclear region. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:20883](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20883) · Entrez [284161](https://www.ncbi.nlm.nih.gov/gene/284161) · UniProt [Q8N9F7](https://www.uniprot.org/uniprotkb/Q8N9F7) · Ensembl [ENSG00000153982](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153982)

## Data

Gene col 7758: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7758); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7758, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7758]; `tensor/DDL_lfc|DDL_z.npy` [7758]; `embed/gene_vectors.npy` [7758]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7758 or target_col == 7758). Every well: [[GDPD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GDPD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
