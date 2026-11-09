---
symbol: "BBS5"
type: "gene"
col: 8632
ensembl_id: "ENSG00000163093"
name: "Bardet-Biedl syndrome 5"
location: "2q31.1"
module: 17
arm: "+"
pooled_cpm: 8.84
n_lines_expressing: 44
n_dd_up: 18
n_dd_down: 20
n_dd_up_clean: 16
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# BBS5

*Bardet-Biedl syndrome 5* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.84× (z +9.1, q 4e-17, up in 27 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.467× (z -16.1, q 0e+00, down in 32 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS31P4]] (+0.75, fdr 7e-06), [[ZNF420]] (+0.70, fdr 7e-06), [[ZNF45]] (+0.70, fdr 7e-06); moves opposite to [[MIATNB]] (-0.63, fdr 3e-05), [[SECISBP2]] (-0.61, fdr 3e-05), [[PSMD6-AS2]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PRTG]] → it (grade B ⚠); 6 go from it, the strongest it → [[GALT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8632.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +9.1 | 4e-17 | 27/41 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +8.6 | 3e-15 | 21/41 (LOX-IMVI, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +7.8 | 1e-12 | 21/41 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +7.0 | 3e-10 | 22/41 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.51×** | +6.2 | 8e-08 | 16/39 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +5.5 | 3e-06 | 17/39 (C32, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +4.9 | 7e-05 | 11/38 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +4.9 | 8e-05 | 17/40 (Panc 03.27, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.8 | 8e-05 | 12/39 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +4.5 | 3e-04 | 15/41 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.77×** | +4.5 | 4e-04 | 13/41 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.75×** | +4.4 | 5e-04 | 10/35 (HOP62, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 6e-04 | 11/41 (C32, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.0 | 0.003 | 7/34 (A-427, SNU-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.011 | 10/41 (C32, HOP62, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.5 | 0.015 | 8/41 (Panc 03.27, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8632.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.467×** | -16.1 | 0e+00 | 32/41 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.560×** | -12.3 | 3e-32 | 30/42 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.446×** | -12.1 | 2e-31 | 32/41 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.471×** | -11.3 | 3e-27 | 31/41 (HOP62, C-33 A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.489×** | -10.7 | 1e-24 | 22/39 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.502×** | -10.3 | 5e-23 | 30/41 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.558×** | -8.7 | 2e-16 | 26/40 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.620×** | -6.9 | 4e-10 | 16/40 (AN3 CA, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.636×** | -6.5 | 5e-09 | 21/38 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.686×** | -5.7 | 9e-07 | 16/40 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.702×** | -4.9 | 5e-05 | 11/23 (C32, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.733×** | -4.5 | 3e-04 | 14/33 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.745×** | -4.4 | 5e-04 | 11/41 (H4, hTERT-HPNE, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.759×** | -4.1 | 0.001 | 19/40 (SNU-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.595×** | -4.1 | 0.002 | 13/34 (NCI-H2347, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 0.5 µM |  | **0.800×** | -3.3 | 0.027 | 4/41 (SW 1271, SNU-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **0.820×** | -3.0 | 0.088 | 7/39 (A498, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Gefitinib (drug)]] 5 µM |  | **0.821×** | -3.0 | 0.089 | 4/42 (NCI-H460, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8632. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.24 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -13.4) |
| [[HOP62 (line)]] | alt | 8.95 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.170× (z -10.2) |
| [[C-33 A (line)]] | alt | 18.0 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.165× (z -9.2) |
| [[C32 (line)]] | wt | 30.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0992× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 6.90 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.138× (z -9.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.167× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 18.0 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.226× (z -9.4) |
| [[SNU-423 (line)]] | alt | 9.92 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -9.6) |
| [[AN3 CA (line)]] | alt | 24.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -9.4) |
| [[BT-474 (line)]] | alt | 6.59 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0613× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 11.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -9.1) |
| [[H4 (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0824× (z -9.0) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 5.70 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.05 µM 0.0678× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 20.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.244× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 8.29 | 0 | 1 | — | [[PF-06260933 (drug)]] 5 µM 0.0470× (z -8.5) |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -8.7) |
| [[SHP-77 (line)]] | alt | 13.5 | 0 | 1 | — | [[PH-797804 (drug)]] 0.5 µM 0.0878× (z -8.9) |
| [[SNU-1 (line)]] | wt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0904× (z -10.6) |
| [[SW 900 (line)]] | alt | 7.41 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0964× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.678 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.749 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.880 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8632), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31P4]] | +0.75 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[ZNF420]] | +0.70 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[ZNF45]] | +0.70 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SAAL1]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TBC1D19]] | +0.69 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[WDR11]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[HARS2]] | +0.68 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[NUDT12]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[FAM133B]] | +0.68 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[PRPF39]] | +0.68 | +0.57 / +0.63 | both halves | 9e-06 | STRING 400 |
| [[TTC5]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[IRAK1BP1]] | +0.67 | +0.51 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIATNB]] | -0.63 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[SECISBP2]] | -0.61 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[PSMD6-AS2]] | -0.60 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[SPON1-AS1]] | -0.60 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[HCFC1]] | -0.60 | -0.48 / -0.46 | both halves | 2e-05 | pathway: Organelle biogenesis and maintenance |
| [[PRDM10]] | -0.59 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[SIAH2-AS1]] | -0.59 | -0.24 / -0.57 | both halves | 4e-04 |  |
| [[CCNT2-AS1]] | -0.59 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[PELO-AS1]] | -0.59 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[SLC25A53]] | -0.58 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[CFL1]] | -0.57 | -0.47 / -0.60 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRTG]] | B | PRTG activity raises BBS5's level | lines that do not express PRTG (14) vs lines expressing it (36) | 3.05× lower at baseline in the lines without PRTG | 0.007 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[MGLL]] | B | MGLL activity lowers BBS5's level | lines that do not express MGLL (14) vs lines expressing it (36) | 2.24× higher at baseline in the lines without MGLL | 0.015 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises BBS5's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00888]], [[LINC00888-1]] | B | LINC00888, LINC00888-1 activity raises BBS5's level | lines that do not express LINC00888, LINC00888-1 (7) vs lines expressing them (43) | 2.75× lower at baseline in the lines without LINC00888, LINC00888-1 | 0.018 | ⚠ within organs, on part of the lines; also absent: KIF3C, TBKBP1, GDAP1; maybe low, not absent; co-absent genes |
| [[PLEKHA6]] | B | PLEKHA6 activity lowers BBS5's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 2.38× higher at baseline in the lines without PLEKHA6 | 0.033 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[ZNF527]] | C | ZNF527 activity raises BBS5's level | lines that do not express ZNF527 (3) vs lines expressing it (47) | 3.24× lower at baseline in the lines without ZNF527 | 0.067 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALT]] | B | BBS5 activity raises GALT's level | lines that do not express BBS5 (6) vs lines expressing it (44) | 1.25× lower at baseline in the lines without BBS5 | 0.051 | ⚠ within organs, on part of the lines; also absent: GGT7, HLTF, FERMT2 |
| [[EFCAB7]] | B | BBS5 activity raises EFCAB7's level | lines that do not express BBS5 (6) vs lines expressing it (44) | 1.34× lower at baseline in the lines without BBS5 | 0.062 | ⚠ within organs, on part of the lines; also absent: GGT7, HLTF, FERMT2 |
| [[USP30]] | B | BBS5 activity raises USP30's level | lines that do not express BBS5 (6) vs lines expressing it (44) | 1.44× lower at baseline in the lines without BBS5 | 0.062 | ⚠ within organs, on part of the lines; also absent: GGT7, HLTF, FERMT2 |
| [[NPHP1]] | B | BBS5 activity raises NPHP1's level | lines that do not express BBS5 (6) vs lines expressing it (44) | 2.67× lower at baseline in the lines without BBS5 | 0.078 | ⚠ within organs, on part of the lines; also absent: GGT7, HLTF, FERMT2 |
| [[LINC00888-1]] | B | BBS5 activity raises LINC00888-1's level | lines that do not express BBS5 (6) vs lines expressing it (44) | 3.11× lower at baseline in the lines without BBS5 | 0.090 | ⚠ within organs, on part of the lines; also absent: GGT7, HLTF, FERMT2 |
| [[LINC00888]] | B | BBS5 activity raises LINC00888's level | lines that do not express BBS5 (6) vs lines expressing it (44) | 2.16× lower at baseline in the lines without BBS5 | 0.097 | ⚠ within organs, on part of the lines; also absent: GGT7, HLTF, FERMT2 |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.844). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.8, -1.3); signed map (-21.9, -16.3). **Vector** length 83.4, 16.6% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intraflagellar transport* (reactome, mean cos +0.56 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.2 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.1 | +6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.1 | +5.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.7 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.5 | -16.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.3 | -11.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.1 | -12.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -6.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | Bardet-Biedl syndrome 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:169,479,480-169,506,655 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp762I194 |
| Gene groups (HGNC) | BBSome |
| Reactome | 5 pathways, smallest: BBSome-mediated cargo-targeting to cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3I7](https://www.uniprot.org/uniprotkb/Q8N3I7) (BBSome complex member BBS5):

> The BBSome complex is thought to function as a coat complex required for sorting of specific membrane proteins to the primary cilia. The BBSome complex is required for ciliogenesis but is dispensable for centriolar satellite function. This ciliogenic function is mediated in part by the Rab8 GDP/GTP exchange factor, which localizes to the basal body and contacts the BBSome. Rab8(GTP) enters the primary cilium and promotes extension of the ciliary membrane. Firstly the BBSome associates with the …

**Summary**, from NCBI Gene [129880](https://www.ncbi.nlm.nih.gov/gene/129880):

> This gene encodes a protein that has been directly linked to Bardet-Biedl syndrome. The primary features of this syndrome include retinal dystrophy, obesity, polydactyly, renal abnormalities and learning disabilities. Experimentation in non-human eukaryotes suggests that this gene is expressed in ciliated cells and that it is required for the formation of cilia. Alternate transcriptional splice variants have been observed but have not been fully characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:970](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:970) · Entrez [129880](https://www.ncbi.nlm.nih.gov/gene/129880) · UniProt [Q8N3I7](https://www.uniprot.org/uniprotkb/Q8N3I7) · Ensembl [ENSG00000163093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163093)

## Data

Gene col 8632: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8632); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8632, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8632]; `tensor/DDL_lfc|DDL_z.npy` [8632]; `embed/gene_vectors.npy` [8632]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8632 or target_col == 8632). Every well: [[BBS5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BBS5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
