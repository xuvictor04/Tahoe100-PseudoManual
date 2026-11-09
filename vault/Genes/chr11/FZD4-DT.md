---
symbol: "FZD4-DT"
type: "gene"
col: 14464
ensembl_id: "ENSG00000246523"
name: "FZD4 divergent transcript"
location: "11q14.2"
module: 10
arm: "+"
pooled_cpm: 4.84
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 27
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# FZD4-DT

*FZD4 divergent transcript* — 11q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.72× (z +9.1, q 7e-17, up in 7 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.34× (z +3.9, q 0.012, up in 15 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.231× (z -13.8, q 3e-40, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF236-DT]] (+0.59, fdr 1e-05), [[FAM66C]] (+0.57, fdr 4e-05), [[PICART1]] (+0.57, fdr 3e-05); moves opposite to [[SKIC8]] (-0.50, fdr 7e-05), [[MRPL2]] (-0.47, fdr 5e-05), [[MRPL17]] (-0.44, fdr 4e-04).
> It sits in the **+** arm of [[Module 010]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14464.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +9.1 | 7e-17 | 7/10 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +6.0 | 6e-07 | 6/15 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.49×** | +5.3 | 2e-05 | 16/47 (AsPC-1, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +3.9 | 0.012 | 10/23 (AsPC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.012 | 15/38 (Hs 766T, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.050 | 10/45 (C32, NCI-H2030, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.050 | 11/46 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.065 | 9/44 (KATO III, SNU-1, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.38× | +3.0 | 0.15 | 8/43 (KATO III, HEC-1-A, …) | top dose only | position effect removed |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.43× | +3.0 | 0.15 | 5/45 (NCI-H1573, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14464.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.231×** | -13.8 | 3e-40 | 38/46 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.401×** | -8.6 | 3e-15 | 23/38 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.431×** | -7.9 | 5e-13 | 27/45 (A-427, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.444×** | -7.6 | 4e-12 | 29/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.459×** | -7.3 | 3e-11 | 29/45 (PANC-1, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.593×** | -6.9 | 4e-10 | 24/40 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.478×** | -6.7 | 2e-09 | 25/43 (A-427, A498, …) | two highest doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.498×** | -6.5 | 4e-09 | 18/37 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.506×** | -6.4 | 1e-08 | 25/45 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.541×** | -5.8 | 5e-07 | 21/45 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.568×** | -5.3 | 6e-06 | 21/45 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.340×** | -5.3 | 6e-06 | 18/45 (MIA PaCa-2, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.562×** | -4.8 | 5e-05 | 15/47 (NCI-H2030, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.594×** | -4.6 | 2e-04 | 18/44 (SNU-423, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.607×** | -4.5 | 3e-04 | 11/30 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.402×** | -4.5 | 3e-04 | 12/42 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.418×** | -4.3 | 6e-04 | 19/38 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.544×** | -4.1 | 0.001 | 14/47 (SNU-1, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.657×** | -3.9 | 0.002 | 16/43 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.664×** | -3.6 | 0.008 | 13/44 (LoVo, SNU-1, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 5 µM |  | **0.761×** | -3.6 | 0.008 | 9/46 (Hs 766T, SW48, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.696×** | -3.4 | 0.018 | 6/46 (NCI-H661, A549, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.514×** | -3.3 | 0.026 | 13/35 (NCI-H23, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.736×** | -2.9 | 0.085 | 10/38 (LOX-IMVI, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14464. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 9.57 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0442× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 9.97 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0766× (z -10.8) |
| [[PANC-1 (line)]] | alt | 5.46 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0955× (z -11.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -8.6) |
| [[A498 (line)]] | wt | 2.29 | 0 | 2 (1 ⚠) | — | [[Diphenhydramine (drug)]] 5 µM 0.0416× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 7.75 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -10.0) ⚠ cell-cycle shift, explains ~84% of this change |
| [[Hs 766T (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HS-578T (line)]] | alt | 5.31 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0501× (z -9.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 3.84 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0628× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 5.06 | 0 | 1 | — | [[Bestatin (drug)]] 0.05 µM 0.0649× (z -8.5) |
| [[SNU-423 (line)]] | alt | 5.60 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0677× (z -9.2) |
| [[A-172 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.959 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14464), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF236-DT]] | +0.59 | +0.54 / +0.52 | both halves | 1e-05 | same gene group |
| [[FAM66C]] | +0.57 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[PICART1]] | +0.57 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[PJVK]] | +0.55 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[TMEM139-AS1]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[GEMIN7-AS1]] | +0.54 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[GALC]] | +0.54 | +0.39 / +0.48 | both halves | 6e-05 |  |
| [[CATSPERE]] | +0.53 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[SUMO2P17]] | +0.53 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[CRTC3-AS1]] | +0.53 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[LINC00466]] | +0.53 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[H3-3A-DT]] | +0.52 | +0.46 / +0.47 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKIC8]] | -0.50 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[MRPL2]] | -0.47 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[MRPL17]] | -0.44 | -0.26 / -0.44 | both halves | 4e-04 |  |
| [[USP28]] | -0.44 | -0.35 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.459). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.7, 29.5); signed map (38.0, -9.2). **Vector** length 48.9, 6.01% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +9.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +3.5 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +1.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.0 | +2.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +0.9 | +2.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +0.8 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.7 | -7.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -4.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -4.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -1.2 | -3.2 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.1 | -3.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | FZD4 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q14.2 — chr11:86,955,616-87,021,909 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54219](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54219) · Entrez [100506368](https://www.ncbi.nlm.nih.gov/gene/100506368) · Ensembl [ENSG00000246523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246523)

## Data

Gene col 14464: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14464); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14464, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14464]; `tensor/DDL_lfc|DDL_z.npy` [14464]; `embed/gene_vectors.npy` [14464]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14464 or target_col == 14464). Every well: [[FZD4-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FZD4-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
