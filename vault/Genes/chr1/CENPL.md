---
symbol: "CENPL"
type: "gene"
col: 4179
ensembl_id: "ENSG00000120334"
name: "centromere protein L"
location: "1q25.1"
module: 83
arm: "+"
pooled_cpm: 20.17
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 11
n_dd_up_clean: 17
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# CENPL

*centromere protein L* — 1q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.21× (z +32.6, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.627× (z -9.2, q 1e-17, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GEN1]] (+0.69, fdr 7e-06), [[ZNF253]] (+0.69, fdr 3e-05), [[ZNF85]] (+0.68, fdr 1e-05); moves opposite to [[STX7]] (-0.64, fdr 5e-05), [[SERAC1]] (-0.62, fdr 5e-05), [[SLC23A2]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4179.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.21×** | +32.6 | 0e+00 | 45/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +21.9 | 0e+00 | 43/47 (LOX-IMVI, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.18×** | +15.4 | 0e+00 | 41/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.14×** | +14.4 | 4e-45 | 42/48 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +14.0 | 3e-42 | 37/46 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.97×** | +13.4 | 6e-39 | 40/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +12.5 | 4e-34 | 36/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.75×** | +11.1 | 1e-26 | 39/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.59×** | +9.2 | 2e-18 | 33/47 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.39×** | +9.0 | 2e-17 | 33/48 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.57×** | +8.3 | 8e-15 | 22/38 (LoVo, SW480, …) | inconsistent across doses | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +6.5 | 3e-09 | 1/48 (NCI-H2030) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.84×** | +6.3 | 1e-08 | 19/46 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +6.1 | 5e-08 | 25/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +6.0 | 1e-07 | 21/48 (NCI-H2347, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.56×** | +4.6 | 1e-04 | 12/47 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.003 | 15/47 (SW480, CFPAC-1, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.009 | 4/47 (MIA PaCa-2, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.021 | 6/48 (RKO, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.028 | 4/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4179.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.627×** | -9.2 | 1e-17 | 30/48 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.632×** | -9.1 | 3e-17 | 29/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.731×** | -8.8 | 3e-16 | 30/48 (Hs 766T, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.725×** | -6.4 | 3e-08 | 22/47 (PANC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.759×** | -5.5 | 5e-06 | 22/47 (Hs 766T, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.785×** | -4.6 | 3e-04 | 14/47 (A498, CHP-212, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.804×** | -4.3 | 0.001 | 9/47 (A-427, A498, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.805×** | -4.1 | 0.002 | 12/47 (COLO 205, SNU-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.813×** | -4.1 | 0.002 | 13/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.816×** | -3.9 | 0.006 | 10/46 (AN3 CA, RPMI-7951, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.828×** | -3.7 | 0.010 | 13/48 (NCI-H1573, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.841× | -3.4 | 0.027 | 13/47 (LS 180, SNU-1, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.873× | -3.1 | 0.094 | 10/48 (A-427, SW48, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4179. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 15.1 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +13.3) | — |
| [[NCI-H460 (line)]] | wt | 24.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +20.8) | — |
| [[HEC-1-A (line)]] | alt | 19.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +15.2) | — |
| [[PANC-1 (line)]] | alt | 26.6 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.367× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.403× (z -9.8) |
| [[SW480 (line)]] | alt | 19.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.7) | — |
| [[A498 (line)]] | wt | 29.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 11.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +13.2) | — |
| [[COLO 205 (line)]] | alt | 9.84 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +9.0) | [[Megestrol (drug)]] 0.5 µM 0.0741× (z -9.7) |
| [[HOP62 (line)]] | alt | 19.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 16.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +14.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 12.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.74× (z +15.9) | — |
| [[NCI-H23 (line)]] | alt | 27.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +14.0) | — |
| [[NCI-H2347 (line)]] | alt | 18.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +14.7) | — |
| [[Panc 03.27 (line)]] | alt | 13.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +10.4) | — |
| [[RKO (line)]] | wt | 26.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +14.3) | — |
| [[RPMI-7951 (line)]] | alt | 20.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 15.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +14.7) | — |
| [[SW 900 (line)]] | alt | 25.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +11.5) | — |
| [[A-172 (line)]] | wt | 25.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.7) | — |
| [[A-427 (line)]] | wt | 49.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.456× (z -10.9) |
| [[A549 (line)]] | wt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +14.1) | — |
| [[AsPC-1 (line)]] | alt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +12.5) | — |
| [[BT-474 (line)]] | alt | 26.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +13.1) | — |
| [[C32 (line)]] | wt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.75× (z +15.1) | — |
| [[H4 (line)]] | wt | 19.3 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.104× (z -10.8) |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.175× (z -8.8) |
| [[Hs 766T (line)]] | wt | 29.6 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.295× (z -8.7) |
| [[HS-578T (line)]] | alt | 15.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +13.5) | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.43× (z +12.6) | — |
| [[J82 (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +15.5) | — |
| [[KATO III (line)]] | alt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 15.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +15.6) | — |
| [[NCI-H2030 (line)]] | alt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 15.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +10.7) | — |
| [[SW48 (line)]] | wt | 12.4 | 0 | 1 | — | [[Talc (drug)]] 0.5 µM 0.0550× (z -11.2) |
| [[AN3 CA (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4179), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEN1]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[ZNF253]] | +0.69 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[ZNF85]] | +0.68 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[ZNF93]] | +0.68 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ZNF689]] | +0.68 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[IGF2BP1]] | +0.67 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[ZNF100]] | +0.67 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[DNAAF10]] | +0.67 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[ZNF724]] | +0.65 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[ZBTB2]] | +0.65 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[MSANTD2]] | +0.65 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[PCBP1-AS1]] | +0.65 | +0.55 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX7]] | -0.64 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[SERAC1]] | -0.62 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[SLC23A2]] | -0.61 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[KCTD17]] | -0.58 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[ARRB2]] | -0.57 | -0.38 / -0.26 | both halves | 3e-04 |  |
| [[PLA2G12A]] | -0.57 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[ST6GALNAC4]] | -0.57 | -0.57 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[OSBPL9]] | -0.57 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[EDF1]] | -0.56 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[CAMSAP1]] | -0.56 | -0.54 / -0.28 | both halves | 3e-04 |  |
| [[SGSM1]] | -0.56 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[BTBD9]] | -0.55 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[NDRG3]] | -0.55 | -0.47 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CENPL's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CENPL's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises CENPL's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.683). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-44.5, -47.2); signed map (17.0, -19.3). **Vector** length 93.7, 21.8% of its response variance represented; |z| ≥ 3 in 1,130 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +21.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.7 | +32.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +12.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +15.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +4.3 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +6.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.9 | +0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | -0.5 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.5 | -9.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.4 | -9.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.9 | -6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -8.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | -4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | +3.9 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.1 — chr1:173,799,550-173,824,883 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ383J4.3, FLJ31044; previously C1orf155 |
| Gene groups (HGNC) | Constitutive centromere associated network |
| Reactome | 20 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N0S6](https://www.uniprot.org/uniprotkb/Q8N0S6) (Centromere protein L):

> Component of the CENPA-CAD (nucleosome distal) complex, a complex recruited to centromeres which is involved in assembly of kinetochore proteins, mitotic progression and chromosome segregation. May be involved in incorporation of newly synthesized CENPA into centromeres via its interaction with the CENPA-NAC complex.

**Summary**, from NCBI Gene [91687](https://www.ncbi.nlm.nih.gov/gene/91687):

> CENPL is a subunit of a CENPH (MIM 605607)-CENPI (MIM 300065)-associated centromeric complex that targets CENPA (MIM 117139) to centromeres and is required for proper kinetochore function and mitotic progression (Okada et al., 2006) [PubMed 16622420].[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:17879](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17879) · Entrez [91687](https://www.ncbi.nlm.nih.gov/gene/91687) · UniProt [Q8N0S6](https://www.uniprot.org/uniprotkb/Q8N0S6) · Ensembl [ENSG00000120334](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120334)

## Data

Gene col 4179: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4179); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4179, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4179]; `tensor/DDL_lfc|DDL_z.npy` [4179]; `embed/gene_vectors.npy` [4179]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4179 or target_col == 4179). Every well: [[CENPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
