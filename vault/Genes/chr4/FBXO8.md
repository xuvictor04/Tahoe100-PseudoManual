---
symbol: "FBXO8"
type: "gene"
col: 8874
ensembl_id: "ENSG00000164117"
name: "F-box protein 8"
location: "4q34.1"
module: 130
arm: "+"
pooled_cpm: 13.71
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 22
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# FBXO8

*F-box protein 8* — 4q34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +10.8, q 1e-24, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.325× (z -15.6, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.451× (z -11.1, q 5e-26, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKN1B]] (+0.73, fdr 7e-06), [[KLHDC2]] (+0.70, fdr 7e-06), [[MAT2B]] (+0.68, fdr 7e-06); moves opposite to [[ANKS6]] (-0.68, fdr 7e-06), [[RRP7BP-1]] (-0.65, fdr 2e-05), [[PACC1]] (-0.61, fdr 1e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RANBP17]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8874.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +10.8 | 1e-24 | 33/45 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.54×** | +9.2 | 9e-18 | 37/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.4 | 2e-11 | 27/45 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.07×** | +5.3 | 2e-05 | 20/44 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.0 | 5e-05 | 22/45 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.28×** | +4.9 | 1e-04 | 22/48 (RKO, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.007 | 12/47 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.33×** | +3.7 | 0.015 | 9/48 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.020 | 7/48 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.28×** | +3.5 | 0.027 | 12/48 (COLO 205, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.027 | 14/45 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.043 | 12/46 (A549, C-33 A, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.17× | +3.2 | 0.071 | 6/48 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.24×** | +3.1 | 0.087 | 5/48 (C32, LoVo, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8874.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.325×** | -15.6 | 0e+00 | 48/48 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.451×** | -11.1 | 5e-26 | 42/47 (BT-474, HOP62, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.308×** | -8.6 | 2e-15 | 35/47 (CFPAC-1, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.353×** | -7.6 | 5e-12 | 28/43 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.361×** | -7.4 | 1e-11 | 29/46 (HT-29, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.414×** | -6.4 | 1e-08 | 27/44 (CFPAC-1, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.476×** | -5.4 | 6e-06 | 26/42 (Panc 03.27, A498, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.681×** | -5.3 | 7e-06 | 26/46 (KATO III, A-172, …) | rises with dose | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.601×** | -4.8 | 1e-04 | 19/48 (H4, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.608×** | -4.6 | 2e-04 | 22/48 (A498, SW1417, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.713×** | -4.5 | 3e-04 | 19/41 (SNU-423, SW 900, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.741×** | -4.2 | 0.002 | 19/48 (A498, SW 1088, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.743×** | -4.0 | 0.003 | 20/40 (COLO 205, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.752×** | -4.0 | 0.003 | 15/48 (CFPAC-1, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.752×** | -3.9 | 0.003 | 17/47 (SW48, COLO 205, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.749×** | -3.8 | 0.005 | 19/48 (J82, C-33 A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.768×** | -3.7 | 0.008 | 12/48 (J82, CFPAC-1, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.713×** | -3.2 | 0.045 | 13/47 (LS 180, SW48, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.716×** | -3.1 | 0.050 | 11/48 (RKO, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8874. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.50 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 9.39 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.0946× (z -10.5) |
| [[A-172 (line)]] | wt | 12.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[CFPAC-1 (line)]] | alt | 22.5 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.249× (z -10.0) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0781× (z -9.6) |
| [[LS 180 (line)]] | wt | 17.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.198× (z -9.1) |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0931× (z -10.7) |
| [[H4 (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 19.6 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.121× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 15.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.211× (z -9.6) |
| [[Hs 766T (line)]] | wt | 6.73 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.5 µM 0.0959× (z -9.2) |
| [[KATO III (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 6.85 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.107× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.265× (z -11.1) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.207× (z -9.2) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 7.48 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.177× (z -11.3) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.120× (z -10.8) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[SHP-77 (line)]] | alt | 9.56 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.128× (z -8.8) |
| [[SW48 (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0735× (z -8.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8874), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN1B]] | +0.73 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[KLHDC2]] | +0.70 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[MAT2B]] | +0.68 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[COQ6]] | +0.68 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[ZNF451]] | +0.66 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[IFT74]] | +0.66 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[MMUT]] | +0.65 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[NDUFA5]] | +0.65 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[SEPSECS]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[CYLD]] | +0.63 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[ATG2B]] | +0.63 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[BROX]] | +0.62 | +0.62 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKS6]] | -0.68 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[RRP7BP-1]] | -0.65 | -0.46 / -0.71 | both halves | 2e-05 |  |
| [[PACC1]] | -0.61 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[RRP1B]] | -0.60 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[GARNL3]] | -0.60 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[NCLN]] | -0.59 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[GMDS]] | -0.58 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[LMBR1]] | -0.58 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[POLR3G]] | -0.58 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[ARHGAP8]] | -0.58 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[PPM1F]] | -0.57 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[UBE3D]] | -0.57 | -0.41 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RANBP17]] | B | RANBP17 activity raises FBXO8's level | lines that do not express RANBP17 (10) vs lines expressing it (40) | 1.08× lower at baseline in the lines without RANBP17 | 0.055 | ⚠ within organs, on part of the lines |
| [[PCAT7]] | B | PCAT7 activity lowers FBXO8's level | lines that do not express PCAT7 (12) vs lines expressing it (38) | 1.32× higher at baseline in the lines without PCAT7 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000286850, CRACD, NFIA; maybe low, not absent |
| [[PARP11]] | C | PARP11 activity lowers FBXO8's level | lines that do not express PARP11 (3) vs lines expressing it (47) | 1.47× higher at baseline in the lines without PARP11 | 0.094 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NECAB2, FAT3, ENSG00000205890 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.0, -47.3); signed map (8.6, -26.9). **Vector** length 87.2, 17.4% of its response variance represented; |z| ≥ 3 in 1,081 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +7.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.2 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.8 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.8 | -15.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.6 | -11.1 |
|  | [[EX229 (drug)]] 5 µM |  | -5.3 | -7.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.8 | -8.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.7 | -6.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.2 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q34.1 — chr4:174,236,658-174,283,667 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBX8, FBS |
| Gene groups (HGNC) | F-boxes other; Sec7 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRD0](https://www.uniprot.org/uniprotkb/Q9NRD0) (F-box only protein 8):

> May promote guanine-nucleotide exchange on an ARF. Promotes the activation of ARF through replacement of GDP with GTP (Potential).

**Summary**, from NCBI Gene [26269](https://www.ncbi.nlm.nih.gov/gene/26269):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13587) · Entrez [26269](https://www.ncbi.nlm.nih.gov/gene/26269) · UniProt [Q9NRD0](https://www.uniprot.org/uniprotkb/Q9NRD0) · Ensembl [ENSG00000164117](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164117)

## Data

Gene col 8874: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8874); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8874, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8874]; `tensor/DDL_lfc|DDL_z.npy` [8874]; `embed/gene_vectors.npy` [8874]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8874 or target_col == 8874). Every well: [[FBXO8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
