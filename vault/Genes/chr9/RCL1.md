---
symbol: "RCL1"
type: "gene"
col: 4163
ensembl_id: "ENSG00000120158"
name: "RNA terminal phosphate cyclase like 1"
location: "9p24.1"
module: 33
arm: "+"
pooled_cpm: 35.97
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 19
n_dd_up_clean: 23
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# RCL1

*RNA terminal phosphate cyclase like 1* — 9p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.84× (z +10.5, q 8e-23, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.586× (z -13.0, q 1e-35, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR1B]] (+0.72, fdr 7e-06), [[NLE1]] (+0.72, fdr 7e-06), [[LDLRAD3]] (+0.69, fdr 7e-06); moves opposite to [[SMIM14]] (-0.56, fdr 1e-05), [[NPHS1]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4163.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +10.5 | 8e-23 | 42/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +10.1 | 2e-21 | 40/48 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +8.6 | 2e-15 | 39/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.52×** | +8.3 | 2e-14 | 37/47 (RKO, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +7.9 | 3e-13 | 29/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +7.4 | 1e-11 | 28/45 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +7.0 | 2e-10 | 30/46 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +7.0 | 2e-10 | 29/48 (HT-29, NCI-H460, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +6.7 | 1e-09 | 24/48 (Hs 766T, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.88×** | +5.7 | 9e-07 | 28/48 (HepG2/C3A, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +5.2 | 1e-05 | 25/48 (COLO 205, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.34×** | +5.0 | 2e-05 | 24/47 (J82, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +4.8 | 6e-05 | 24/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.5 | 3e-04 | 16/32 (A-427, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.5 | 3e-04 | 19/43 (NCI-H460, HT-29, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +4.2 | 9e-04 | 19/48 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.0 | 0.002 | 20/48 (SK-MEL-2, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +3.9 | 0.003 | 18/48 (J82, HT-29, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.005 | 11/48 (J82, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.005 | 20/48 (Panc 03.27, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.006 | 12/47 (NCI-H460, HT-29, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4163.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.586×** | -13.0 | 1e-35 | 36/48 (RKO, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.494×** | -12.1 | 3e-31 | 32/44 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.552×** | -9.8 | 2e-20 | 25/38 (HepG2/C3A, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.682×** | -6.3 | 4e-08 | 28/46 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -5.3 | 1e-05 | 26/48 (SW48, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.749×** | -5.0 | 6e-05 | 22/48 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.795×** | -4.6 | 3e-04 | 21/48 (SW480, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.778×** | -4.3 | 1e-03 | 23/48 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.780×** | -4.3 | 0.001 | 18/47 (SW480, SW48, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.769×** | -4.3 | 0.001 | 20/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.784×** | -4.2 | 0.001 | 15/48 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.818×** | -4.0 | 0.003 | 20/48 (SW480, C-33 A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.789×** | -3.9 | 0.004 | 23/46 (SW48, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.827×** | -3.8 | 0.007 | 17/48 (SW480, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.796×** | -3.6 | 0.011 | 14/42 (SNU-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.807×** | -3.6 | 0.013 | 15/47 (A498, SW480, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.814×** | -3.6 | 0.013 | 10/48 (SW1417, LOX-IMVI, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.821×** | -3.1 | 0.048 | 16/46 (HOP62, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.834× | -3.1 | 0.048 | 14/47 (KATO III, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4163. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 45.0 | 8 | 1 | [[Clobetasol propionate (drug)]] 0.5 µM 3.60× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -8.8) |
| [[SW 900 (line)]] | alt | 47.1 | 5 | 1 | [[Budesonide (drug)]] 5 µM 3.78× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -8.8) |
| [[SW48 (line)]] | wt | 92.8 | 0 | 6 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -13.0) |
| [[A498 (line)]] | wt | 45.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 68.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0462× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -10.9) |
| [[PANC-1 (line)]] | alt | 29.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -9.5) |
| [[SNU-423 (line)]] | alt | 67.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -12.7) |
| [[SW480 (line)]] | alt | 54.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -9.3) |
| [[A-427 (line)]] | wt | 28.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -14.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 36.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0664× (z -19.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 31.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -12.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 67.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -13.9) |
| [[SNU-1 (line)]] | wt | 58.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -12.1) |
| [[AN3 CA (line)]] | alt | 85.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -11.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0829× (z -9.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 22.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -9.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 49.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 12.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.72× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 24.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.41× (z +9.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 35.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 49.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -12.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4163), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1B]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 | STRING 665 |
| [[NLE1]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 | STRING 836 |
| [[LDLRAD3]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 | same gene group |
| [[MDN1]] | +0.68 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SNHG17]] | +0.68 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[WDR3]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 998 |
| [[EXOSC5]] | +0.68 | +0.67 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 880 |
| [[NOL10]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 | STRING 991 |
| [[TSEN2]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[POLR3H]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[TMCO6]] | +0.66 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[URB2]] | +0.66 | +0.69 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM14]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[NPHS1]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises RCL1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[STEAP3]] | B | STEAP3 activity raises RCL1's level | lines that do not express STEAP3 (6) vs lines expressing it (44) | 1.25× lower at baseline in the lines without STEAP3 | 0.054 | ⚠ within organs, on part of the lines; also absent: GPR155; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises RCL1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SH3RF3]] | B | SH3RF3 activity raises RCL1's level | lines that do not express SH3RF3 (14) vs lines expressing it (36) | 1.06× lower at baseline in the lines without SH3RF3 | 0.076 | ⚠ within organs, on part of the lines; also absent: DCLK2, OSBPL6, FHL1 |
| [[ALDH1B1]] | C | ALDH1B1 activity raises RCL1's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 2.62× lower at baseline in the lines without ALDH1B1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent; its own permutation p |
| [[USP31]] | C | USP31 activity raises RCL1's level | lines that do not express USP31 (3) vs lines expressing it (47) | 2.27× lower at baseline in the lines without USP31 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.759). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.6, -41.5); signed map (-7.8, -52.0). **Vector** length 116, 33.3% of its response variance represented; |z| ≥ 3 in 1,233 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +7.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +10.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.6 | +4.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.6 | +7.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.4 | +2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.8 | +3.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.6 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.6 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.3 | -13.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | +2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.7 | -6.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -5.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.6 | -4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.6 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | RNA terminal phosphate cyclase like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.1 — chr9:4,792,944-4,885,917 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPCL1, RNAC |
| Gene groups (HGNC) | SSU processome; MicroRNA protein coding host genes |
| Hallmark sets | MYC_TARGETS_V2, HEME_METABOLISM |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2P8](https://www.uniprot.org/uniprotkb/Q9Y2P8) (RNA 3'-terminal phosphate cyclase-like protein):

> As part of the small subunit (SSU) processome, it plays a role in 40S-ribosomal-subunit biogenesis in the early pre-rRNA processing steps at sites A0, A1 and A2 that are required for proper maturation of the 18S RNA (By similarity). Activates BMS1 by promoting GDP/GTP exchange (By similarity). Does not have cyclase activity (By similarity).

**Summary**, from NCBI Gene [10171](https://www.ncbi.nlm.nih.gov/gene/10171):

> Predicted to enable RNA endonuclease activity. Involved in ribosomal small subunit biogenesis. Part of small-subunit processome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17687](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17687) · Entrez [10171](https://www.ncbi.nlm.nih.gov/gene/10171) · UniProt [Q9Y2P8](https://www.uniprot.org/uniprotkb/Q9Y2P8) · Ensembl [ENSG00000120158](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120158)

## Data

Gene col 4163: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4163); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4163, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4163]; `tensor/DDL_lfc|DDL_z.npy` [4163]; `embed/gene_vectors.npy` [4163]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4163 or target_col == 4163). Every well: [[RCL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RCL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
