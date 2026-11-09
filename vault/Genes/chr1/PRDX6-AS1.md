---
symbol: "PRDX6-AS1"
type: "gene"
col: 12784
ensembl_id: "ENSG00000203739"
name: "PRDX6 antisense RNA 1"
location: "1q25.1"
module: 146
arm: "+"
pooled_cpm: 21.64
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 21
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# PRDX6-AS1

*PRDX6 antisense RNA 1* — 1q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.79× (z +7.9, q 2e-12, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.440× (z -11.0, q 2e-25, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPS8-DT]] (+0.61, fdr 1e-05), [[NUDT13]] (+0.56, fdr 3e-05), [[ATP6V0D1-DT]] (+0.53, fdr 1e-05); moves opposite to [[ARID5A]] (-0.53, fdr 3e-05), [[C3orf52]] (-0.47, fdr 4e-05), [[NIPAL1]] (-0.43, fdr 2e-04).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[KATNAL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12784.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.79×** | +7.9 | 2e-12 | 39/48 (SW480, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +6.2 | 2e-07 | 25/48 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.51×** | +5.4 | 1e-05 | 27/48 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +5.2 | 4e-05 | 26/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +4.6 | 4e-04 | 25/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.60×** | +4.4 | 0.001 | 15/47 (A-172, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.25×** | +4.3 | 0.001 | 18/48 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.39×** | +4.3 | 0.001 | 19/47 (A-172, NCI-H1573, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.78×** | +4.1 | 0.003 | 18/48 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +3.8 | 0.007 | 13/48 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.008 | 15/48 (A-172, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | 1.20× | +3.5 | 0.021 | 15/48 (HT-29, KATO III, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.29×** | +3.3 | 0.038 | 19/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.25× | +3.0 | 0.10 | 2/48 (BT-474, HOP62) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12784.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.440×** | -11.0 | 2e-25 | 39/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.486×** | -9.7 | 1e-19 | 30/46 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.488×** | -9.3 | 3e-18 | 36/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.596×** | -6.9 | 6e-10 | 31/47 (Hs 766T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.614×** | -6.3 | 4e-08 | 30/46 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.634×** | -6.1 | 1e-07 | 28/47 (PANC-1, SNU-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.663×** | -5.5 | 3e-06 | 27/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.682×** | -5.1 | 2e-05 | 23/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.676×** | -5.0 | 3e-05 | 24/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.677×** | -5.0 | 3e-05 | 24/47 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.792×** | -4.4 | 6e-04 | 24/48 (MIA PaCa-2, LS 180, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.738×** | -4.0 | 0.002 | 17/48 (NCI-H460, HT-29, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.587×** | -3.7 | 0.008 | 11/46 (HCT15, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.753×** | -3.6 | 0.010 | 17/47 (H4, SW480, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.761×** | -3.6 | 0.010 | 13/47 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.784×** | -3.2 | 0.037 | 10/48 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.787×** | -3.2 | 0.041 | 16/47 (Panc 03.27, NCI-H23, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.795×** | -3.0 | 0.063 | 13/47 (NCI-H1573, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12784. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 51.8 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.238× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.242× (z -10.4) |
| [[PANC-1 (line)]] | alt | 22.7 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -12.3) |
| [[H4 (line)]] | wt | 32.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -11.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 31.3 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0524× (z -11.8) |
| [[LoVo (line)]] | wt | 16.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 22.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -14.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 31.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -13.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.182× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 12.7 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.107× (z -9.0) |
| [[Hs 766T (line)]] | wt | 42.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.203× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.218× (z -8.6) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.249× (z -9.3) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 18.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0996× (z -9.8) |
| [[A-172 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12784), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS8-DT]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[NUDT13]] | +0.56 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[ATP6V0D1-DT]] | +0.53 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[TNRC6A]] | +0.51 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[ARL6IP5]] | +0.51 | +0.36 / +0.37 | both halves | 9e-05 |  |
| [[ATP1A1-AS1]] | +0.50 | +0.53 / +0.46 | both halves | 3e-05 | same gene group |
| [[CYP39A1]] | +0.49 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[RPRD2]] | +0.49 | +0.51 / +0.38 | both halves | 6e-05 |  |
| [[ERP29]] | +0.48 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[NIFK-AS1]] | +0.48 | +0.63 / +0.33 | both halves | 1e-04 | same gene group |
| [[NUDT6]] | +0.48 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[DPH6-DT]] | +0.47 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID5A]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[C3orf52]] | -0.47 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[NIPAL1]] | -0.43 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[STK38L]] | -0.42 | -0.22 / -0.37 | both halves | 6e-04 |  |
| [[MYO1D]] | -0.42 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[C1GALT1]] | -0.42 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[R3HDM4]] | -0.42 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[RNF34]] | -0.42 | -0.33 / -0.30 | both halves | 2e-04 |  |
| [[NOTCH1]] | -0.41 | -0.34 / -0.27 | both halves | 3e-04 |  |
| [[TBILA]] | -0.41 | -0.22 / -0.47 | both halves | 6e-04 |  |
| [[FHL2]] | -0.41 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[CCNYL1]] | -0.41 | -0.34 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL2]] | B | KATNAL2 activity raises PRDX6-AS1's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.77× lower at baseline in the lines without KATNAL2 | 0.010 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[FBXO15]] | B | FBXO15 activity raises PRDX6-AS1's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without FBXO15 | 0.018 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[MYO1D]] | B | MYO1D activity lowers PRDX6-AS1's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 1.53× higher at baseline in the lines without MYO1D | 0.020 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[CCDC102B]] | B | CCDC102B activity raises PRDX6-AS1's level | lines that do not express CCDC102B (9) vs lines expressing it (41) | 1.79× lower at baseline in the lines without CCDC102B | 0.024 | ⚠ within organs, on part of the lines; also absent: SMAD9, TTC28, ITGA10; maybe low, not absent |
| [[ADGRG2]] | B | ADGRG2 activity raises PRDX6-AS1's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 1.52× lower at baseline in the lines without ADGRG2 | 0.026 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| [[DAPP1]] | B | DAPP1 activity lowers PRDX6-AS1's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 1.59× higher at baseline in the lines without DAPP1 | 0.039 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[DUSP19]] | C | DUSP19 activity raises PRDX6-AS1's level | lines that do not express DUSP19 (3) vs lines expressing it (47) | 2.14× lower at baseline in the lines without DUSP19 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |
| [[TMCC1-DT]] | C | TMCC1-DT activity raises PRDX6-AS1's level | lines that do not express TMCC1-DT (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without TMCC1-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, WWOX, DBNDD1; maybe low, not absent; its own permutation p |
| [[FHL2]] | C | FHL2 activity lowers PRDX6-AS1's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 1.88× higher at baseline in the lines without FHL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent; its own permutation p |
| [[LRRIQ3]] | C | LRRIQ3 activity raises PRDX6-AS1's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 2.02× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.417). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (1.3, 23.8); signed map (34.3, -14.8). **Vector** length 63.2, 11.5% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +7.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +4.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +5.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | -2.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -3.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.7 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | PRDX6 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q25.1 — chr1:173,417,793-173,489,407 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54870](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54870) · Entrez [101928673](https://www.ncbi.nlm.nih.gov/gene/101928673) · Ensembl [ENSG00000203739](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203739)

## Data

Gene col 12784: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12784); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12784, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12784]; `tensor/DDL_lfc|DDL_z.npy` [12784]; `embed/gene_vectors.npy` [12784]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12784 or target_col == 12784). Every well: [[PRDX6-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRDX6-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
