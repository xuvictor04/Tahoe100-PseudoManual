---
symbol: "SERINC2"
type: "gene"
col: 9665
ensembl_id: "ENSG00000168528"
name: "serine incorporator 2"
location: "1p35.2"
module: 34
arm: "+"
pooled_cpm: 39.36
n_lines_expressing: 44
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 15
direction_downstream: 2
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# SERINC2

*serine incorporator 2* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.79× (z +10.0, q 1e-20, up in 25 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.32× (z +4.5, q 8e-04, up in 15 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.517× (z -15.9, q 0e+00, down in 30 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYTH1]] (+0.65, fdr 1e-05), [[TINAGL1]] (+0.64, fdr 8e-06), [[F11R]] (+0.61, fdr 1e-05); moves opposite to [[RBM26]] (-0.60, fdr 1e-05), [[ZZZ3]] (-0.59, fdr 6e-05), [[QSER1]] (-0.57, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TINAGL1]] → it (grade B ⚠); 2 go from it, the strongest it → [[ZZZ3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9665.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +10.0 | 1e-20 | 25/35 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +7.0 | 5e-10 | 18/32 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +6.7 | 3e-09 | 20/31 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.32×** | +4.5 | 8e-04 | 15/41 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 0.003 | 18/40 (HCT15, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.004 | 10/42 (HT-29, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.9 | 0.007 | 11/31 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.9 | 0.007 | 0/43 | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.40×** | +3.8 | 0.008 | 11/40 (NCI-H2347, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.028 | 11/39 (BT-474, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.054 | 14/41 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.20×** | +3.1 | 0.083 | 13/38 (SW 900, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 5 µM |  | 1.14× | +3.1 | 0.094 | 11/43 (LS 180, SW1417, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.13× | +3.0 | 0.094 | 4/42 (CFPAC-1, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9665.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.517×** | -15.9 | 0e+00 | 30/41 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.573×** | -9.5 | 5e-19 | 29/40 (Panc 03.27, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.636×** | -7.4 | 2e-11 | 24/42 (SK-MEL-2, LoVo, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.485×** | -6.5 | 1e-08 | 26/43 (CFPAC-1, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.787×** | -5.8 | 8e-07 | 20/42 (SK-MEL-2, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.536×** | -5.6 | 2e-06 | 21/38 (LoVo, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.732×** | -5.3 | 8e-06 | 20/42 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.758×** | -4.2 | 0.002 | 14/41 (LoVo, HCT15, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.786×** | -3.9 | 0.006 | 18/41 (SK-MEL-2, LoVo, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.798×** | -3.9 | 0.007 | 9/42 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.658×** | -3.7 | 0.010 | 13/39 (HOP62, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.800×** | -3.7 | 0.012 | 17/39 (HepG2/C3A, HT-29, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.818×** | -3.4 | 0.027 | 15/41 (LoVo, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.816×** | -3.3 | 0.034 | 14/41 (LoVo, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.836× | -3.1 | 0.082 | 13/42 (HepG2/C3A, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.838× | -3.0 | 0.087 | 10/41 (LoVo, SW480, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.838× | -3.0 | 0.087 | 14/41 (A498, J82, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9665. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 126 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -16.9) |
| [[HOP62 (line)]] | alt | 123 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -11.3) |
| [[A549 (line)]] | wt | 44.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -19.4) |
| [[HepG2_C3A (line)]] | wt | 117 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.324× (z -12.9) |
| [[HT-29 (line)]] | alt | 64.0 | 2 (1 ⚠) | 1 | [[Daptomycin (drug)]] 0.5 µM 2.33× (z +8.8) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.80× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 45.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.74× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0972× (z -11.3) |
| [[SW480 (line)]] | alt | 34.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +11.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -8.8) ⚠ cell-cycle shift, explains ~13% of this change |
| [[A-172 (line)]] | wt | 35.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 104 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -9.2) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.529× (z -9.1) |
| [[J82 (line)]] | alt | 39.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -17.8) |
| [[NCI-H1573 (line)]] | alt | 36.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -16.6) |
| [[NCI-H1792 (line)]] | alt | 27.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -11.1) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 39.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -12.4) |
| [[SW1417 (line)]] | alt | 91.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.441× (z -9.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[BT-474 (line)]] | alt | 48.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 71.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -18.6) |
| [[HEC-1-A (line)]] | alt | 52.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -9.2) |
| [[HS-578T (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0756× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~14% of this change |
| [[KATO III (line)]] | alt | 56.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.495× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 14.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 52.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -10.2) |
| [[PANC-1 (line)]] | alt | 16.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -9.0) |
| [[A-427 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.64 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.44 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 90.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9665), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYTH1]] | +0.65 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[TINAGL1]] | +0.64 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[F11R]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PPARD]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[TMEM184B]] | +0.58 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[RUBCN]] | +0.57 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[RHOC]] | +0.56 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[FA2H]] | +0.56 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[TTC9]] | +0.56 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[PLEKHM1P1]] | +0.56 | +0.60 / +0.38 | both halves | 7e-05 |  |
| [[CAP1]] | +0.55 | +0.56 / +0.40 | both halves | 4e-05 |  |
| [[MAP3K9]] | +0.54 | +0.45 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM26]] | -0.60 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[ZZZ3]] | -0.59 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[QSER1]] | -0.57 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[LUC7L2]] | -0.54 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[DHRS4L2]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[RPRD2]] | -0.51 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[USP24]] | -0.51 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[CC2D2A]] | -0.50 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[SMARCAD1]] | -0.50 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[BCLAF1]] | -0.48 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[ZNF644]] | -0.47 | -0.45 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TINAGL1]] | B | TINAGL1 activity raises SERINC2's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.96× lower at baseline in the lines without TINAGL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[WNT7B]] | B | WNT7B activity raises SERINC2's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 2.34× lower at baseline in the lines without WNT7B | 0.008 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[SEMA3B]] | B | SEMA3B activity raises SERINC2's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.18× lower at baseline in the lines without SEMA3B | 0.011 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[FA2H]] | B | FA2H activity raises SERINC2's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.59× lower at baseline in the lines without FA2H | 0.014 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[LAMA3]] | B | LAMA3 activity raises SERINC2's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.74× lower at baseline in the lines without LAMA3 | 0.025 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[FAM83A]] | B | FAM83A activity raises SERINC2's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 2.12× lower at baseline in the lines without FAM83A | 0.026 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[MYO5B]] | B | MYO5B activity raises SERINC2's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without MYO5B | 0.035 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[LAMC2]] | B | LAMC2 activity raises SERINC2's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without LAMC2 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[PTK2B]] | B | PTK2B activity raises SERINC2's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 2.46× lower at baseline in the lines without PTK2B | 0.054 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAP3K9]] | B | MAP3K9 activity raises SERINC2's level | lines that do not express MAP3K9 (8) vs lines expressing it (42) | 2.91× lower at baseline in the lines without MAP3K9 | 0.057 | ⚠ within organs, on part of the lines; also absent: CDKN1C, DAPK2, PRKCZ; maybe low, not absent |
| [[JUP]] | B | JUP activity raises SERINC2's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.39× lower at baseline in the lines without JUP | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[CRYBG2]] | B | CRYBG2 activity raises SERINC2's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.20× lower at baseline in the lines without CRYBG2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZZZ3]] | B | SERINC2 activity lowers ZZZ3's level | lines that do not express SERINC2 (6) vs lines expressing it (44) | 1.19× higher at baseline in the lines without SERINC2 | 0.074 | ⚠ within organs, on part of the lines; also absent: SLC9A3, TESK2, LITAF |
| [[CYB5R3]] | B | SERINC2 activity raises CYB5R3's level | lines that do not express SERINC2 (6) vs lines expressing it (44) | 1.49× lower at baseline in the lines without SERINC2 | 0.080 | ⚠ within organs, on part of the lines; also absent: SLC9A3, TESK2, LITAF |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.605). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.6, 0.3); signed map (-5.0, 40.1). **Vector** length 92.2, 20.4% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +10.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | -0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +3.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +4.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.4 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +0.6 |
| fall | [[NG25 (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -15.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.1 | -7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | serine incorporator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:31,409,565-31,434,680 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FKSG84, PRO0899, TDE2; previously TDE2L |
| Reactome | 2 pathways, smallest: Serine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SA4](https://www.uniprot.org/uniprotkb/Q96SA4) (Serine incorporator 2):

> Non-ATP-dependent, non-specific lipid transporter for phosphatidylserine, phosphatidylcholine, and phosphatidylethanolamine. Functions as a scramblase that flips lipids in both directions across the membrane. In contrast to SERINC3 and SERINC5, has no effect on HIV-1 particles infectivity.

**Summary**, from NCBI Gene [347735](https://www.ncbi.nlm.nih.gov/gene/347735):

> Enables phospholipid scramblase activity. Involved in plasma membrane phospholipid scrambling. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23231](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23231) · Entrez [347735](https://www.ncbi.nlm.nih.gov/gene/347735) · UniProt [Q96SA4](https://www.uniprot.org/uniprotkb/Q96SA4) · Ensembl [ENSG00000168528](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168528)

## Data

Gene col 9665: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9665); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9665, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9665]; `tensor/DDL_lfc|DDL_z.npy` [9665]; `embed/gene_vectors.npy` [9665]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9665 or target_col == 9665). Every well: [[SERINC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERINC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
