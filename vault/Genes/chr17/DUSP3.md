---
symbol: "DUSP3"
type: "gene"
col: 3007
ensembl_id: "ENSG00000108861"
name: "dual specificity phosphatase 3"
location: "17q21.31"
module: 138
arm: "+"
pooled_cpm: 34.09
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 13
n_dd_up_clean: 17
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# DUSP3

*dual specificity phosphatase 3* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.86× (z +9.4, q 2e-18, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.434× (z -12.7, q 4e-34, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HPS1]] (+0.67, fdr 1e-05), [[UAP1L1]] (+0.65, fdr 7e-06), [[GNPDA1]] (+0.64, fdr 1e-05); moves opposite to [[ILF2]] (-0.54, fdr 1e-05), [[ACTL6A]] (-0.53, fdr 2e-05), [[RECQL]] (-0.51, fdr 3e-05).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3007.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +9.4 | 2e-18 | 44/48 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +9.1 | 3e-17 | 32/46 (A498, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +5.0 | 1e-04 | 28/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.40×** | +4.9 | 1e-04 | 29/47 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.7 | 3e-04 | 22/40 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.4 | 0.001 | 25/47 (KATO III, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.003 | 22/48 (HT-29, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +4.1 | 0.003 | 23/47 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.009 | 22/47 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.009 | 18/48 (A498, A-427, …) | rises with dose | low cells (technical?) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.28×** | +3.8 | 0.009 | 18/47 (HT-29, COLO 205, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.015 | 20/47 (HT-29, BT-474, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **1.26×** | +3.5 | 0.018 | 19/47 (A-172, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.26×** | +3.5 | 0.018 | 19/48 (HT-29, HepG2/C3A, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.025 | 15/48 (HT-29, HOP62, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +3.4 | 0.028 | 18/48 (A549, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.031 | 16/48 (KATO III, RKO, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.031 | 17/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.031 | 18/47 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.044 | 17/47 (LOX-IMVI, AsPC-1, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.062 | 10/48 (Panc 03.27, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.063 | 15/48 (COLO 205, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.44×** | +2.9 | 0.084 | 14/47 (CFPAC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3007.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.434×** | -12.7 | 4e-34 | 45/48 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.475×** | -11.3 | 5e-27 | 46/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.512×** | -10.2 | 5e-22 | 41/48 (SNU-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.656×** | -6.4 | 2e-08 | 31/47 (BT-474, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.664×** | -6.2 | 6e-08 | 31/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.754×** | -6.1 | 1e-07 | 31/48 (SNU-1, C32, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.471×** | -6.0 | 2e-07 | 34/48 (LOX-IMVI, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.769×** | -5.6 | 1e-06 | 28/48 (SNU-1, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.561×** | -4.6 | 3e-04 | 25/48 (SHP-77, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.583×** | -4.3 | 0.001 | 21/48 (J82, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.668×** | -3.2 | 0.071 | 15/35 (SW480, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.816×** | -3.1 | 0.088 | 12/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.866× | -3.1 | 0.088 | 11/48 (HCT15, HOP62, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.810×** | -3.1 | 0.088 | 20/47 (RKO, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3007. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 34.5 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.223× (z -10.5) |
| [[A498 (line)]] | wt | 27.7 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 49.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.221× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.267× (z -11.3) |
| [[SNU-1 (line)]] | wt | 51.7 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -11.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.195× (z -10.5) |
| [[A-172 (line)]] | wt | 43.0 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.251× (z -11.2) |
| [[A-427 (line)]] | wt | 44.8 | 1 | 2 | [[Auranofin (drug)]] 5 µM 2.57× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.371× (z -9.2) |
| [[RKO (line)]] | wt | 39.0 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.292× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 68.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.302× (z -11.1) |
| [[BT-474 (line)]] | alt | 22.7 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.213× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 65.1 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.431× (z -9.5) |
| [[J82 (line)]] | alt | 45.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.362× (z -8.8) |
| [[KATO III (line)]] | alt | 27.6 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.09× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 37.7 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.355× (z -9.7) |
| [[SW480 (line)]] | alt | 26.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.82× (z +9.2) ⚠ toxic; transcription drop | [[Lonafarnib (drug)]] 5 µM 0.0845× (z -11.9) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 40.0 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0752× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 48.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -8.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LoVo (line)]] | wt | 22.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 54.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.152× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -8.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2030 (line)]] | alt | 20.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.246× (z -9.6) |
| [[SW 1271 (line)]] | alt | 65.8 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.0714× (z -9.1) |
| [[A549 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3007), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPS1]] | +0.67 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[UAP1L1]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[GNPDA1]] | +0.64 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[CLCN7]] | +0.61 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[FLCN]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[TRAPPC3]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[RRAGC-DT]] | +0.57 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[CRYM]] | +0.57 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[DEF8]] | +0.55 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[DUSP8]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SLC31A2]] | +0.54 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[CLN3]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ILF2]] | -0.54 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[ACTL6A]] | -0.53 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[RECQL]] | -0.51 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[LINC02458]] | -0.50 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[TBC1D8]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[RASA1]] | -0.49 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[SFXN2]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[ERI1]] | -0.48 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[PIBF1]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[ARHGAP1]] | -0.46 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[RTTN]] | -0.46 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[HAT1]] | -0.45 | -0.37 / -0.45 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DUSP3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.365). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.0, -31.7); signed map (5.0, -9.1). **Vector** length 103, 26.7% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.2 | +9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.3 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | +3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.0 | +2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.7 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.6 | +2.5 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -6.0 | -6.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.1 | -4.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | -12.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.6 | -6.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.3 | -11.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -2.6 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:43,766,125-43,778,977 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously VHR |
| Gene groups (HGNC) | Atypical dual specificity phosphatases |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 28 pathways, smallest: ERKs are inactivated; ERK/MAPK targets; MAPK targets/ Nuclear events mediated by MAP kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [P51452](https://www.uniprot.org/uniprotkb/P51452) (Dual specificity protein phosphatase 3):

> Shows activity both for tyrosine-protein phosphate and serine-protein phosphate, but displays a strong preference toward phosphotyrosines. Specifically dephosphorylates and inactivates ERK1 and ERK2.

**Summary**, from NCBI Gene [1845](https://www.ncbi.nlm.nih.gov/gene/1845):

> The protein encoded by this gene is a member of the dual specificity protein phosphatase subfamily. These phosphatases inactivate their target kinases by dephosphorylating both the phosphoserine/threonine and phosphotyrosine residues. They negatively regulate members of the mitogen-activated protein (MAP) kinase superfamily (MAPK/ERK, SAPK/JNK, p38), which are associated with cellular proliferation and differentiation. Different members of the family of dual specificity phosphatases show …

**Accessions** — [HGNC:3069](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3069) · Entrez [1845](https://www.ncbi.nlm.nih.gov/gene/1845) · UniProt [P51452](https://www.uniprot.org/uniprotkb/P51452) · Ensembl [ENSG00000108861](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108861)

## Data

Gene col 3007: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3007); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3007, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3007]; `tensor/DDL_lfc|DDL_z.npy` [3007]; `embed/gene_vectors.npy` [3007]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3007 or target_col == 3007). Every well: [[DUSP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
