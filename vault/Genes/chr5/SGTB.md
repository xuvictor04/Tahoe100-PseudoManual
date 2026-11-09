---
symbol: "SGTB"
type: "gene"
col: 12478
ensembl_id: "ENSG00000197860"
name: "small glutamine rich tetratricopeptide repeat co-chaperone beta"
location: "5q12.3"
module: 40
arm: "+"
pooled_cpm: 33.32
n_lines_expressing: 49
n_dd_up: 27
n_dd_down: 13
n_dd_up_clean: 24
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# SGTB

*small glutamine rich tetratricopeptide repeat co-chaperone beta* — 5q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.50× (z +15.9, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.609× (z -12.1, q 4e-31, down in 32 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.670× (z -6.9, q 1e-09, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANO10]] (+0.74, fdr 7e-06), [[ATP7B]] (+0.71, fdr 1e-05), [[NTAN1]] (+0.68, fdr 1e-05); moves opposite to [[CHTOP]] (-0.66, fdr 1e-05), [[ZFX]] (-0.64, fdr 1e-05), [[PNRC2]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ANK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12478.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.50×** | +15.9 | 0e+00 | 46/47 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.28×** | +14.3 | 5e-44 | 43/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.25×** | +14.1 | 1e-42 | 42/47 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.78×** | +10.0 | 2e-21 | 40/47 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +9.9 | 7e-21 | 37/47 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.46×** | +8.2 | 3e-14 | 39/47 (AsPC-1, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +8.0 | 1e-13 | 28/46 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.34×** | +7.1 | 6e-11 | 30/47 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +7.1 | 9e-11 | 26/47 (LoVo, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +7.0 | 2e-10 | 28/47 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.44×** | +6.3 | 1e-08 | 26/47 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +6.2 | 3e-08 | 29/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +5.8 | 3e-07 | 26/47 (LS 180, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.38×** | +5.6 | 8e-07 | 24/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +5.2 | 1e-05 | 20/47 (NCI-H460, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +5.1 | 1e-05 | 15/47 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.32×** | +4.8 | 6e-05 | 18/47 (LoVo, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12478.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.609×** | -12.1 | 4e-31 | 32/47 (LoVo, J82, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.670×** | -6.9 | 1e-09 | 32/47 (HS-578T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.896× | -6.6 | 7e-09 | 2/47 (H4, CHP-212) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.714×** | -5.8 | 8e-07 | 25/47 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.731×** | -5.4 | 6e-06 | 24/47 (HS-578T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.720×** | -5.4 | 7e-06 | 26/46 (HS-578T, LS 180, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.749×** | -4.8 | 1e-04 | 22/47 (KATO III, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.838× | -4.3 | 0.001 | 19/47 (HS-578T, Hs 766T, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.780×** | -4.3 | 0.001 | 20/47 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.782×** | -4.3 | 0.001 | 20/47 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.803×** | -3.8 | 0.007 | 21/47 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | 0.859× | -3.7 | 0.010 | 13/47 (NCI-H661, A-172, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.677×** | -3.5 | 0.018 | 19/47 (LoVo, SW 1088, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.820×** | -3.4 | 0.023 | 6/47 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.809×** | -3.4 | 0.025 | 14/46 (HS-578T, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.832×** | -3.2 | 0.050 | 14/47 (LOX-IMVI, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12478. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 35.9 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.14× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 41.2 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +11.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -12.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[PANC-1 (line)]] | alt | 35.6 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.41× (z +10.1) | — |
| [[SW480 (line)]] | alt | 29.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 26.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -14.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HCT15 (line)]] | alt | 36.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[HEC-1-A (line)]] | alt | 20.2 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.28× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 49.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.364× (z -8.9) |
| [[J82 (line)]] | alt | 53.3 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.29× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -14.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[KATO III (line)]] | alt | 16.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 24.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -16.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-1 (line)]] | wt | 28.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.127× (z -9.8) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 77.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[C-33 A (line)]] | alt | 37.0 | 0 | 1 | — | [[Sonidegib (drug)]] 5 µM 0.0864× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -8.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[COLO 205 (line)]] | alt | 9.21 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0923× (z -8.5) |
| [[H4 (line)]] | wt | 48.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HOP62 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 67.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -10.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -13.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -8.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 56.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -9.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H661 (line)]] | alt | 32.9 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.05 µM 0.0618× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 24.2 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.197× (z -9.2) |
| [[SW48 (line)]] | wt | 23.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -10.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.51 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12478), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANO10]] | +0.74 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[ATP7B]] | +0.71 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[NTAN1]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.68 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[SARS1]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[GFPT1]] | +0.67 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[AAK1]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[EIF4EBP1]] | +0.65 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[EIF4E3]] | +0.64 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.64 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[LINC00662]] | +0.64 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[COG5]] | +0.63 | +0.59 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHTOP]] | -0.66 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[ZFX]] | -0.64 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[PNRC2]] | -0.62 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[SRCAP]] | -0.61 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[ZNF644]] | -0.61 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[NFYC]] | -0.61 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[RBM23]] | -0.60 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[DCAF8]] | -0.60 | -0.58 / -0.39 | both halves | 6e-05 |  |
| [[RBM4]] | -0.59 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[PMF1]] | -0.59 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[FAM111A]] | -0.59 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[BAZ2B]] | -0.59 | -0.58 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANK2]] | B | ANK2 activity raises SGTB's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.89× lower at baseline in the lines without ANK2 | 0.009 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[TTLL7]] | B | TTLL7 activity raises SGTB's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 1.73× lower at baseline in the lines without TTLL7 | 0.029 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725 |
| [[CDA]] | B | CDA activity lowers SGTB's level | lines that do not express CDA (16) vs lines expressing it (34) | 1.40× higher at baseline in the lines without CDA | 0.040 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[FSD1L]] | C | FSD1L activity raises SGTB's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 2.41× lower at baseline in the lines without FSD1L | 0.054 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[GPD1L]] | C | GPD1L activity raises SGTB's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 1.59× lower at baseline in the lines without GPD1L | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.579). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-0.6, 2.0); signed map (-40.5, -3.8). **Vector** length 121, 32.6% of its response variance represented; |z| ≥ 3 in 1,241 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.8 | +5.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.1 | +10.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +5.6 | +4.6 |
|  | [[Artesunate (drug)]] 5 µM |  | +5.5 | +7.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.2 | +15.9 |
|  | [[Neratinib (drug)]] 5 µM |  | +4.9 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.7 | +8.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.4 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -7.6 | -12.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.6 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.3 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -4.7 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.8 | -5.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.6 | -4.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.8 | -3.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | small glutamine rich tetratricopeptide repeat co-chaperone beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.3 — chr5:65,665,928-65,723,035 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Sgt2, FLJ39002 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Small glutamine rich tetratricopeptide repeat co-chaperone family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EQ0](https://www.uniprot.org/uniprotkb/Q96EQ0) (Small glutamine-rich tetratricopeptide repeat-containing protein beta):

> Co-chaperone that binds directly to HSC70 and HSP70 and regulates their ATPase activity.

**Summary**, from NCBI Gene [54557](https://www.ncbi.nlm.nih.gov/gene/54557):

> Predicted to enable molecular adaptor activity. Predicted to be involved in post-translational protein targeting to endoplasmic reticulum membrane. Predicted to be part of TRC complex. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23567](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23567) · Entrez [54557](https://www.ncbi.nlm.nih.gov/gene/54557) · UniProt [Q96EQ0](https://www.uniprot.org/uniprotkb/Q96EQ0) · Ensembl [ENSG00000197860](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197860)

## Data

Gene col 12478: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12478); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12478, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12478]; `tensor/DDL_lfc|DDL_z.npy` [12478]; `embed/gene_vectors.npy` [12478]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12478 or target_col == 12478). Every well: [[SGTB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGTB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
