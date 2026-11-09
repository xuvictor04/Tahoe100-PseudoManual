---
symbol: "RABL2A"
type: "gene"
col: 6847
ensembl_id: "ENSG00000144134"
name: "RAB, member of RAS oncogene family like 2A"
location: "2q14.1"
module: 15
arm: "+"
pooled_cpm: 6.89
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 15
n_dd_up_clean: 14
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# RABL2A

*RAB, member of RAS oncogene family like 2A* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.90× (z +18.0, q 0e+00, up in 40 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.552× (z -7.0, q 7e-10, down in 24 of 47 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.554× (z -7.0, q 7e-10, down in 21 of 46 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RABL2B]] (+0.91, fdr 7e-06), [[EFCAB6]] (+0.75, fdr 7e-06), [[AK8]] (+0.68, fdr 7e-06); moves opposite to [[FCHO1]] (-0.57, fdr 4e-05), [[CBR1]] (-0.57, fdr 6e-05), [[ATP1A3]] (-0.56, fdr 0.004, ⚠ one half only (not replicated)), [[CAMK2G]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6847.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.90×** | +18.0 | 0e+00 | 40/42 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.93×** | +12.3 | 1e-32 | 36/39 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.89×** | +10.8 | 8e-25 | 37/47 (A-172, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +7.7 | 2e-12 | 22/39 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +7.0 | 2e-10 | 27/47 (HEC-1-A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.81×** | +6.8 | 9e-10 | 17/33 (HOP62, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +6.3 | 2e-08 | 11/20 (A498, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +5.8 | 5e-07 | 20/46 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.34×** | +4.9 | 5e-05 | 19/47 (LS 180, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.51×** | +4.9 | 5e-05 | 15/46 (C32, RKO, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.37×** | +3.8 | 0.008 | 5/44 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +3.7 | 0.011 | 3/10 (J82, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.019 | 9/40 (A549, A-172, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.038 | 15/45 (H4, SK-MEL-2, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.041 | 5/46 (RPMI-7951, SW 900, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.045 | 12/47 (SW 900, HT-29, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.050 | 5/46 (HT-29, LoVo, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.050 | 7/46 (A-172, SK-MEL-2, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.062 | 5/41 (LS 180, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.062 | 7/38 (A498, LoVo, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6847.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.552×** | -7.0 | 7e-10 | 24/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.554×** | -7.0 | 7e-10 | 21/46 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.562×** | -6.8 | 2e-09 | 25/41 (PANC-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.724×** | -5.4 | 9e-06 | 23/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.644×** | -5.2 | 2e-05 | 18/45 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.645×** | -5.2 | 2e-05 | 19/45 (Panc 03.27, hTERT-HPNE, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.676×** | -4.6 | 3e-04 | 18/46 (SW480, HEC-1-A, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.704×** | -4.1 | 0.002 | 16/45 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.724×** | -3.8 | 0.008 | 17/45 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.716×** | -3.8 | 0.008 | 14/36 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.731×** | -3.7 | 0.011 | 16/47 (HS-578T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.738×** | -3.6 | 0.016 | 7/47 (NCI-H1573, NCI-H460, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.740×** | -3.4 | 0.033 | 11/43 (HS-578T, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.756×** | -3.3 | 0.039 | 4/46 (SW 1271, A498, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.827×** | -3.2 | 0.058 | 5/46 (NCI-H1573, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6847. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 7.64 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 10.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +13.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 6.44 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +9.0) | — |
| [[SW480 (line)]] | alt | 9.44 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +10.4) | — |
| [[A549 (line)]] | wt | 8.08 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0850× (z -10.3) |
| [[HS-578T (line)]] | alt | 5.60 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0739× (z -9.5) |
| [[HT-29 (line)]] | alt | 5.26 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0945× (z -9.1) |
| [[LoVo (line)]] | wt | 6.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 4.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 9.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 6.99 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0867× (z -9.0) |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0748× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 6.64 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0996× (z -9.1) |
| [[SW 900 (line)]] | alt | 4.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.81× (z +8.7) | — |
| [[A-172 (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6847), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABL2B]] | +0.91 | +0.88 / +0.88 | both halves | 7e-06 | same gene group; STRING 454 |
| [[EFCAB6]] | +0.75 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[AK8]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[LENG8-AS1]] | +0.67 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ZNF213-AS1]] | +0.66 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[PBLD]] | +0.65 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[SENP8]] | +0.64 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[UBE3B]] | +0.63 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[ATXN1L]] | +0.63 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[FAM174B]] | +0.63 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[PACRGL]] | +0.62 | +0.63 / +0.38 | both halves | 6e-05 |  |
| [[PRPF18]] | +0.62 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHO1]] | -0.57 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[CBR1]] | -0.57 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[ATP1A3]] | -0.56 | -0.08 / -0.56 | ⚠ one half (not replicated) | 0.004 |  |
| [[CAMK2G]] | -0.56 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[CCDC112]] | -0.55 | -0.19 / -0.46 | ⚠ not reproduced | 8e-04 |  |
| [[RPAP3]] | -0.55 | -0.13 / -0.51 | ⚠ one half (not replicated) | 0.002 |  |
| [[PRKAR2B]] | -0.54 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[HMGN3]] | -0.54 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[CCDC134]] | -0.54 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[BLVRA]] | -0.54 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[RSAD1]] | -0.54 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[CPOX]] | -0.53 | -0.64 / -0.29 | both halves | 2e-04 |  |
| [[CDC14B]] | -0.53 | -0.53 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RABL2A's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.5% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[FBXL13]] | C | FBXL13 activity raises RABL2A's level | lines that do not express FBXL13 (4) vs lines expressing it (46) | 1.54× lower at baseline in the lines without FBXL13 | 0.0999 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXO38-DT, MIAT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.628). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (4.1, 20.3); signed map (29.9, -12.4). **Vector** length 63.2, 9.51% of its response variance represented; |z| ≥ 3 in 1,122 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +18.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +12.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +10.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +3.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.4 | +2.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.4 | +3.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.2 | +0.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.7 | -3.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -5.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | RAB, member of RAS oncogene family like 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:113,627,229-113,643,396 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB like GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBK7](https://www.uniprot.org/uniprotkb/Q9UBK7) (Rab-like protein 2A):

> Small GTPase that plays an essential role in male fertility, sperm intra-flagellar transport, and tail assembly. Binds, in a GTP-regulated manner, to a specific set of effector proteins including key proteins involved in cilia development and function and delivers them into the growing sperm tail.

**Summary**, from NCBI Gene [11159](https://www.ncbi.nlm.nih.gov/gene/11159):

> This gene is a member of the RAB gene family which belongs to the RAS GTPase superfamily. The proteins in the family of RAS-related signaling molecules are small GTP-binding proteins that play important roles in the regulation of exocytotic and endocytotic pathways. This gene maps to the site of an ancestral telomere fusion event and may be a subtelomeric gene. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Apr 2015]

**Accessions** — [HGNC:9799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9799) · Entrez [11159](https://www.ncbi.nlm.nih.gov/gene/11159) · UniProt [Q9UBK7](https://www.uniprot.org/uniprotkb/Q9UBK7) · Ensembl [ENSG00000144134](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144134)

## Data

Gene col 6847: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6847); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6847, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6847]; `tensor/DDL_lfc|DDL_z.npy` [6847]; `embed/gene_vectors.npy` [6847]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6847 or target_col == 6847). Every well: [[RABL2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RABL2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
