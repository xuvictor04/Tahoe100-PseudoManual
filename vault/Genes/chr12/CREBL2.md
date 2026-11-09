---
symbol: "CREBL2"
type: "gene"
col: 3212
ensembl_id: "ENSG00000111269"
name: "cAMP responsive element binding protein like 2"
location: "12p13.1"
module: 130
arm: "+"
pooled_cpm: 20.68
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 21
n_dd_up_clean: 12
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# CREBL2

*cAMP responsive element binding protein like 2* — 12p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.28× (z +15.0, q 0e+00, up in 23 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.35× (z +5.7, q 1e-06, up in 19 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.433× (z -16.0, q 0e+00, down in 42 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.622× (z -9.1, q 2e-17, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BROX]] (+0.65, fdr 1e-05), [[CCDC50]] (+0.63, fdr 2e-05), [[ATG2B]] (+0.63, fdr 1e-05); moves opposite to [[MYO19]] (-0.54, fdr 1e-05), [[MRPS12]] (-0.53, fdr 3e-05), [[NR2C2AP]] (-0.53, fdr 3e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KLHL5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3212.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +15.0 | 0e+00 | 23/30 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +13.7 | 2e-40 | 35/41 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.35×** | +8.1 | 7e-14 | 28/48 (RKO, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +6.5 | 2e-08 | 3/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +6.4 | 2e-08 | 20/37 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +5.7 | 1e-06 | 19/48 (LoVo, KATO III, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.32×** | +5.3 | 1e-05 | 21/48 (NCI-H1573, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +5.1 | 3e-05 | 19/47 (A-172, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | 1.19× | +4.6 | 2e-04 | 15/48 (J82, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +4.6 | 2e-04 | 15/48 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 0.001 | 10/46 (PANC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 0.001 | 11/47 (HOP62, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.29×** | +4.2 | 0.001 | 13/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.54×** | +4.1 | 0.002 | 8/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.002 | 9/47 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.003 | 13/48 (HEC-1-A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.010 | 6/47 (NCI-H460, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.012 | 2/48 (LoVo, NCI-H2347) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.023 | 7/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.029 | 2/48 (NCI-H23, PANC-1) | rises with dose | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.029 | 2/48 (KATO III, PANC-1) | rises with dose | noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.035 | 10/46 (Hs 766T, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3212.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.433×** | -16.0 | 0e+00 | 42/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.552×** | -11.3 | 2e-27 | 33/47 (LOX-IMVI, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.591×** | -10.0 | 2e-21 | 34/48 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.622×** | -9.1 | 2e-17 | 32/47 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.429×** | -8.1 | 9e-14 | 35/47 (MIA PaCa-2, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.658×** | -8.0 | 1e-13 | 28/47 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.670×** | -7.6 | 2e-12 | 28/47 (SW 900, PANC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.502×** | -6.6 | 3e-09 | 25/46 (SK-MEL-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.724×** | -6.2 | 4e-08 | 25/47 (SW480, SNU-423, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.524×** | -6.2 | 4e-08 | 25/45 (NCI-H1792, SW480, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.527×** | -6.1 | 5e-08 | 26/46 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.807×** | -5.8 | 3e-07 | 21/47 (A549, NCI-H1792, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.564×** | -5.5 | 2e-06 | 21/46 (NCI-H1792, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.769×** | -4.8 | 8e-05 | 18/48 (SK-MEL-2, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.706×** | -4.7 | 8e-05 | 18/48 (NCI-H1792, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.749×** | -3.9 | 0.003 | 9/48 (HEC-1-A, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.753×** | -3.9 | 0.003 | 12/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.773×** | -3.5 | 0.013 | 14/48 (NCI-H1792, SNU-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | 0.888× | -3.2 | 0.031 | 7/48 (A-427, COLO 205, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.839× | -3.2 | 0.036 | 17/47 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3212. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.62× (z +11.8) ⚠ position not correctable | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.126× (z -14.7) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 38.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 36.7 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.264× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~59% of this change |
| [[C32 (line)]] | wt | 22.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 20.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +9.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 15.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.2) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.305× (z -10.4) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 37.1 | 0 | 2 | — | [[c-Kit-IN-1 (drug)]] 5 µM 0.100× (z -8.6) |
| [[SW480 (line)]] | alt | 30.6 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.344× (z -10.8) ⚠ unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.369× (z -10.1) |
| [[A-427 (line)]] | wt | 33.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0802× (z -10.5) ⚠ toxic |
| [[A549 (line)]] | wt | 42.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -9.1) ⚠ cell-cycle shift, explains ~17% of this change |
| [[COLO 205 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[H4 (line)]] | wt | 17.9 | 0 | 1 | — | [[Bimiralisib (drug)]] 0.5 µM 0.0688× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.288× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H2030 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0587× (z -8.9) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.225× (z -11.0) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.127× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 37.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.296× (z -8.8) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3212), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BROX]] | +0.65 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[CCDC50]] | +0.63 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[ATG2B]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[PCMTD2]] | +0.62 | +0.33 / +0.67 | both halves | 1e-04 |  |
| [[TAB3]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[CHMP4B]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[MAT2B]] | +0.61 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[HINT3]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[WDTC1]] | +0.59 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[SCRN3]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PLEKHA3]] | +0.58 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[ACADM]] | +0.57 | +0.47 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO19]] | -0.54 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[MRPS12]] | -0.53 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[NR2C2AP]] | -0.53 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[RABEPK]] | -0.51 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[MAD1L1]] | -0.50 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ATP5MC1]] | -0.50 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[EEF1AKMT4]] | -0.48 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[AMD1]] | -0.48 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[POLG]] | -0.47 | -0.29 / -0.58 | both halves | 3e-04 |  |
| [[ZMYND19]] | -0.47 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[IL9RP3]] | -0.47 | -0.21 / -0.53 | both halves | 7e-04 |  |
| [[NOP16]] | -0.46 | -0.28 / -0.52 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL5]] | B | KLHL5 activity raises CREBL2's level | lines that do not express KLHL5 (7) vs lines expressing it (43) | 1.40× lower at baseline in the lines without KLHL5 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.424). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.8, -22.0); signed map (9.1, -27.4). **Vector** length 86.2, 17.5% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +13.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.4 | +8.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +1.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +5.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.9 | +4.6 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.8 | +2.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.5 | -16.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -5.4 | -5.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.6 | -6.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.5 | -6.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -8.1 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -5.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.9 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | cAMP responsive element binding protein like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.1 — chr12:12,611,827-12,645,108 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Basic leucine zipper proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O60519](https://www.uniprot.org/uniprotkb/O60519) (cAMP-responsive element-binding protein-like 2):

> Probable regulator of CREB1 transcriptional activity which is involved in adipose cells differentiation. May also play a regulatory role in the cell cycle. Identification in a chromosomal region frequently deleted in various cancers suggests that it might act as a tumor suppressor.

**Summary**, from NCBI Gene [1389](https://www.ncbi.nlm.nih.gov/gene/1389):

> cAMP response element (CRE)-binding protein-like-2 (CREBL2) was identified in a search to find genes in a commonly deleted region on chromosome 12p13 flanked by ETV6 and CDKN1B genes, frequently associated with hematopoietic malignancies, as well as breast, non-small-cell lung and ovarian cancers. CREBL2 shares a 41% identity with CRE-binding protein (CREB) over a 48-base long region which encodes the bZip domain of CREB. The bZip domain consists of about 30 amino acids rich in basic residues …

**Accessions** — [HGNC:2350](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2350) · Entrez [1389](https://www.ncbi.nlm.nih.gov/gene/1389) · UniProt [O60519](https://www.uniprot.org/uniprotkb/O60519) · Ensembl [ENSG00000111269](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111269)

## Data

Gene col 3212: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3212); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3212, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3212]; `tensor/DDL_lfc|DDL_z.npy` [3212]; `embed/gene_vectors.npy` [3212]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3212 or target_col == 3212). Every well: [[CREBL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CREBL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
