---
symbol: "SH3GL3"
type: "gene"
col: 6437
ensembl_id: "ENSG00000140600"
name: "SH3 domain containing GRB2 like 3, endophilin A3"
location: "15q25.2"
module: 134
arm: "+"
pooled_cpm: 12.08
n_lines_expressing: 29
n_dd_up: 13
n_dd_down: 26
n_dd_up_clean: 12
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# SH3GL3

*SH3 domain containing GRB2 like 3, endophilin A3* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.10× (z +15.8, q 0e+00, up in 26 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.250× (z -13.7, q 5e-40, down in 24 of 26 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.567× (z -7.9, q 4e-13, down in 17 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C7orf57]] (+0.69, fdr 1e-05), [[ANKRD37]] (+0.68, fdr 1e-05), [[MAPT]] (+0.66, fdr 1e-05); moves opposite to [[ERMAP]] (-0.61, fdr 5e-05), [[CLHC1]] (-0.60, fdr 4e-05), [[EXOSC10]] (-0.59, fdr 3e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SLC1A1]] → it (grade B ⚠); 8 go from it, the strongest it → [[MAST1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6437.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.10×** | +15.8 | 0e+00 | 26/26 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **4.28×** | +14.4 | 2e-44 | 24/26 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.27×** | +14.4 | 2e-44 | 24/26 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.14×** | +14.1 | 1e-42 | 24/26 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.65×** | +12.8 | 2e-35 | 24/26 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.85×** | +10.4 | 3e-23 | 24/25 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.48×** | +9.0 | 2e-17 | 20/25 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +7.5 | 5e-12 | 13/24 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.94×** | +7.1 | 8e-11 | 21/25 (A498, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.38×** | +4.5 | 4e-04 | 10/18 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.03×** | +3.7 | 0.013 | 8/24 (HOP62, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.44×** | +3.6 | 0.014 | 8/26 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.083 | 8/26 (HOP62, J82, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6437.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.250×** | -13.7 | 5e-40 | 24/26 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.374×** | -9.7 | 6e-20 | 18/22 (A-172, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.567×** | -7.9 | 4e-13 | 17/25 (A-172, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.262×** | -6.9 | 6e-10 | 20/25 (HEC-1-A, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.287×** | -6.5 | 1e-08 | 16/25 (HEC-1-A, A498, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.291×** | -6.4 | 2e-08 | 18/25 (HEC-1-A, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.512×** | -6.1 | 7e-08 | 14/18 (J82, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belzutifan (drug)]] 5 µM |  | **0.349×** | -5.4 | 4e-06 | 18/22 (HEC-1-A, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.368×** | -5.2 | 1e-05 | 16/23 (A-172, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.586×** | -5.1 | 2e-05 | 9/14 (HEC-1-A, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.427×** | -4.4 | 5e-04 | 13/25 (HEC-1-A, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.659×** | -4.1 | 0.002 | 13/26 (HOP62, BT-474, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.599×** | -3.6 | 0.013 | 5/26 (HEC-1-A, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.703×** | -3.5 | 0.019 | 9/26 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.694×** | -3.5 | 0.019 | 14/24 (NCI-H1792, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.710×** | -3.4 | 0.024 | 12/26 (A-172, HOP62, …) | rises with dose |  |
| [[Megestrol (drug)]] 5 µM |  | **0.797×** | -3.2 | 0.049 | 11/27 (A498, A-172, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.801×** | -3.1 | 0.061 | 9/26 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.714×** | -3.1 | 0.062 | 10/25 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.735×** | -3.0 | 0.065 | 8/26 (A-172, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6437. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 77.8 | 0 | 10 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0646× (z -24.2) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0762× (z -11.9) |
| [[A549 (line)]] | wt | 10.7 | 6 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 6.30× (z +11.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.123× (z -9.1) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 7.21 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 8.81× (z +14.2) | — |
| [[NCI-H1573 (line)]] | alt | 7.91 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 8.77× (z +12.9) | — |
| [[Panc 03.27 (line)]] | alt | 6.67 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 15.6× (z +10.1) | — |
| [[A-172 (line)]] | wt | 48.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0250× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.211× (z -12.4) |
| [[A498 (line)]] | wt | 15.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 8.92× (z +13.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.196× (z -9.9) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 20.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -11.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 50.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0182× (z -25.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 31.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0620× (z -14.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 8.90 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 8.38× (z +10.2) | [[Cepharanthine (drug)]] 0.5 µM 0.0751× (z -8.8) |
| [[HOP62 (line)]] | alt | 18.1 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.83× (z +8.5) | [[Clobetasol propionate (drug)]] 0.05 µM 0.129× (z -9.9) |
| [[SW 900 (line)]] | alt | 12.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.20× (z +9.3) | — |
| [[A-427 (line)]] | wt | 11.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0981× (z -10.9) |
| [[BT-474 (line)]] | alt | 10.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.08× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 46.1 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.182× (z -8.9) |
| [[H4 (line)]] | wt | 30.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0690× (z -10.5) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 8.17 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0682× (z -9.5) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 26.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.91× (z +8.6) | — |
| [[SW 1271 (line)]] | alt | 72.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0449× (z -10.2) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.987 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.921 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.764 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.990 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.867 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6437), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C7orf57]] | +0.69 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ANKRD37]] | +0.68 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[MAPT]] | +0.66 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[NDRG1]] | +0.64 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[SLC2A3]] | +0.64 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[SUSD4]] | +0.64 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[FAM117B]] | +0.64 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[TNFRSF11A]] | +0.63 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[KIAA1958]] | +0.63 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[DTNA]] | +0.62 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[SGSM1]] | +0.62 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[GPR160]] | +0.62 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERMAP]] | -0.61 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[CLHC1]] | -0.60 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[EXOSC10]] | -0.59 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[MCPH1]] | -0.59 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[EFCAB2]] | -0.59 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[CARD8]] | -0.59 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[VPS35L]] | -0.58 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[GTF3C6]] | -0.58 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[MTHFSD]] | -0.58 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[SENP6]] | -0.57 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[FIZ1]] | -0.57 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[DHRS4]] | -0.56 | -0.36 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC1A1]] | B | SLC1A1 activity raises SH3GL3's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 3.06× lower at baseline in the lines without SLC1A1 | 0.014 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[CALB2]] | B | CALB2 activity raises SH3GL3's level | lines that do not express CALB2 (23) vs lines expressing it (27) | 1.97× lower at baseline in the lines without CALB2 | 0.027 | ⚠ within organs, on part of the lines; also absent: CSF2, LINC02577, AADACP1 |
| [[TNIK]] | B | TNIK activity raises SH3GL3's level | lines that do not express TNIK (11) vs lines expressing it (39) | 2.48× lower at baseline in the lines without TNIK | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE |
| [[CRTAC1]] | B | CRTAC1 activity strengthens SH3GL3's drug response | lines that do not express CRTAC1 (10) vs lines expressing it (16) | the lines without CRTAC1 respond 0.67× as strongly (z diff +1.92); strongest at Panobinostat 5 µM: 2.78x vs 6.70x (z diff +3.2) | 0.071 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2; target measured in part of the lines; artifact flags |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAST1]] | B | SH3GL3 activity lowers MAST1's level | lines that do not express SH3GL3 (21) vs lines expressing it (29) | 1.20× higher at baseline in the lines without SH3GL3 | 0.019 | ⚠ within organs, on part of the lines; also absent: S1PR3, SPANXA2-OT1, SALL1 |
| [[LPCAT2]] | B | SH3GL3 activity raises LPCAT2's level | lines that do not express SH3GL3 (21) vs lines expressing it (29) | 1.47× lower at baseline in the lines without SH3GL3 | 0.027 | ⚠ within organs, on part of the lines; also absent: S1PR3, SPANXA2-OT1, SALL1 |
| [[SLC1A1]] | B | SH3GL3 activity raises SLC1A1's level | lines that do not express SH3GL3 (21) vs lines expressing it (29) | 1.79× lower at baseline in the lines without SH3GL3 | 0.033 | ⚠ within organs, on part of the lines; also absent: S1PR3, SPANXA2-OT1, SALL1 |
| [[WSCD1]] | B | SH3GL3 activity raises WSCD1's level | lines that do not express SH3GL3 (21) vs lines expressing it (29) | 1.66× lower at baseline in the lines without SH3GL3 | 0.059 | ⚠ within organs, on part of the lines; also absent: S1PR3, SPANXA2-OT1, SALL1 |
| [[RGS9]] | B | SH3GL3 activity raises RGS9's level | lines that do not express SH3GL3 (21) vs lines expressing it (29) | 1.90× lower at baseline in the lines without SH3GL3 | 0.080 | ⚠ within organs, on part of the lines; also absent: S1PR3, SPANXA2-OT1, SALL1 |
| [[VPS33A]] | B | SH3GL3 activity lowers VPS33A's level | lines that do not express SH3GL3 (21) vs lines expressing it (29) | 1.17× higher at baseline in the lines without SH3GL3 | 0.082 | ⚠ within organs, on part of the lines; also absent: S1PR3, SPANXA2-OT1, SALL1 |
| cells under [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM | B | SH3GL3 activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 0.5 µM (protects the cells) | lines that do not express SH3GL3 (21) vs lines expressing it (27) | the lines without SH3GL3: 0.91× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: S1PR3, SPANXA2-OT1, SALL1 |
| [[MARCHF3]] | B | SH3GL3 activity raises MARCHF3's level | lines that do not express SH3GL3 (21) vs lines expressing it (29) | 1.38× lower at baseline in the lines without SH3GL3 | 0.097 | ⚠ within organs, on part of the lines; also absent: S1PR3, SPANXA2-OT1, SALL1 |

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.3, -12.0); signed map (-28.4, 27.7). **Vector** length 82.4, 22.4% of its response variance represented; |z| ≥ 3 in 763 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +15.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.7 | +10.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.9 | +12.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +14.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.7 | +9.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +7.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.9 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +0.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.6 | -7.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -13.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.4 | -6.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -4.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.7 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -6.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.2 | -5.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -6.5 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain containing GRB2 like 3, endophilin A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:83,447,228-83,618,743 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SH3D2C, SH3P13, CNSA3, EEN-B2, HsT19371 |
| Gene groups (HGNC) | N-BAR domain containing; SH3 domain containing |
| Reactome | 16 pathways, smallest: InlB-mediated entry of Listeria monocytogenes into host cell; Listeria monocytogenes entry into host cells; Negative regulation of MET activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99963](https://www.uniprot.org/uniprotkb/Q99963) (Endophilin-A3):

> Implicated in endocytosis. May recruit other proteins to membranes with high curvature (By similarity).

**Summary**, from NCBI Gene [6457](https://www.ncbi.nlm.nih.gov/gene/6457):

> Enables identical protein binding activity. Predicted to be involved in endocytosis and membrane organization. Predicted to be located in acrosomal vesicle and early endosome membrane. Predicted to be part of early endosome. Predicted to be active in several cellular components, including cytosol; glutamatergic synapse; and presynapse. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10832](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10832) · Entrez [6457](https://www.ncbi.nlm.nih.gov/gene/6457) · UniProt [Q99963](https://www.uniprot.org/uniprotkb/Q99963) · Ensembl [ENSG00000140600](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140600)

## Data

Gene col 6437: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6437); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6437, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6437]; `tensor/DDL_lfc|DDL_z.npy` [6437]; `embed/gene_vectors.npy` [6437]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6437 or target_col == 6437). Every well: [[SH3GL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3GL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
