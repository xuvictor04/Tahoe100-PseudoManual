---
symbol: "PCOLCE2"
type: "gene"
col: 8762
ensembl_id: "ENSG00000163710"
name: "procollagen C-endopeptidase enhancer 2"
location: "3q23"
module: 18
arm: "+"
pooled_cpm: 20.46
n_lines_expressing: 34
n_dd_up: 22
n_dd_down: 20
n_dd_up_clean: 13
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 8
direction_downstream: 1
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PCOLCE2

*procollagen C-endopeptidase enhancer 2* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.63× (z +11.2, q 3e-26, up in 16 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.265× (z -30.3, q 0e+00, down in 27 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KTN1-AS1]] (+0.59, fdr 1e-05), [[APBA2]] (+0.59, fdr 2e-05), [[GALNT14]] (+0.59, fdr 1e-05); moves opposite to [[ERBB3]] (-0.55, fdr 3e-05), [[GABARAP]] (-0.53, fdr 3e-05, ⚠ GABARAP in the vector space only through flagged drug-doses), [[PNPLA2]] (-0.52, fdr 5e-05), [[RNF5]] (-0.51, fdr 5e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TBX18]] → it (grade B ⚠); 1 goes from it, the strongest it → [[DCAF11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8762.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +11.2 | 3e-26 | 16/32 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +8.8 | 5e-16 | 14/29 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +7.8 | 9e-13 | 15/31 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +6.3 | 4e-08 | 10/23 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +5.9 | 3e-07 | 12/29 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **1.42×** | +5.7 | 1e-06 | 17/32 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.89×** | +5.4 | 6e-06 | 15/26 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.37×** | +5.1 | 2e-05 | 14/31 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +4.6 | 2e-04 | 9/31 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.22×** | +4.5 | 4e-04 | 8/31 (SW480, NCI-H1792, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.30×** | +4.0 | 0.003 | 11/32 (SW480, NCI-H1792, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.003 | 3/31 (HOP62, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.6 | 0.012 | 13/31 (SW480, J82, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.24×** | +3.5 | 0.017 | 11/31 (SW480, H4, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.16× | +3.5 | 0.021 | 9/32 (A549, NCI-H1792, …) | all doses, flat | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.031 | 9/31 (HOP62, SW480, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.038 | 3/27 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.038 | 5/29 (LoVo, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.076 | 2/29 (SW480, LoVo) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.076 | 2/31 (SW480, AsPC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.080 | 2/28 (SW480, J82) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.41×** | +2.9 | 0.089 | 7/27 (SW480, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | 1.20× | +2.9 | 0.089 | 4/31 (BT-474, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8762.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.265×** | -30.3 | 0e+00 | 27/32 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.340×** | -16.7 | 0e+00 | 25/31 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.490×** | -11.5 | 4e-28 | 20/31 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.512×** | -10.8 | 8e-25 | 21/31 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.525×** | -10.4 | 4e-23 | 22/30 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.557×** | -9.4 | 5e-19 | 24/31 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.593×** | -8.4 | 4e-15 | 21/31 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.402×** | -7.7 | 1e-12 | 20/29 (LOX-IMVI, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.632×** | -7.4 | 1e-11 | 20/31 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.627×** | -7.2 | 3e-11 | 20/28 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.444×** | -6.8 | 4e-10 | 21/32 (A-427, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.712×** | -5.4 | 2e-06 | 15/31 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.725×** | -5.2 | 1e-05 | 18/31 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.548×** | -5.1 | 2e-05 | 14/31 (LoVo, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.781×** | -4.0 | 0.003 | 15/32 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.843× | -3.9 | 0.004 | 12/32 (PANC-1, A549, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.663×** | -3.5 | 0.018 | 7/32 (HOP62, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.810×** | -3.4 | 0.023 | 9/31 (LoVo, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8762. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 43.8 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0576× (z -40.8) |
| [[A-427 (line)]] | wt | 72.7 | 0 | 11 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.326× (z -18.7) |
| [[MIA PaCa-2 (line)]] | alt | 24.1 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 65.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -23.4) |
| [[A549 (line)]] | wt | 27.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0901× (z -24.8) |
| [[PANC-1 (line)]] | alt | 24.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -25.4) |
| [[SW480 (line)]] | alt | 18.8 | 1 (1 ⚠) | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.9) ⚠ cell-cycle shift, explains ~20% of this change | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -18.2) |
| [[C32 (line)]] | wt | 20.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -14.3) |
| [[LoVo (line)]] | wt | 36.6 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -16.6) |
| [[LOX-IMVI (line)]] | wt | 28.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -19.8) |
| [[A498 (line)]] | wt | 53.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -20.6) |
| [[J82 (line)]] | alt | 26.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -21.2) |
| [[NCI-H1792 (line)]] | alt | 39.4 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -11.1) |
| [[HOP62 (line)]] | alt | 21.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -17.6) |
| [[H4 (line)]] | wt | 38.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -14.4) |
| [[HEC-1-A (line)]] | alt | 10.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -14.5) |
| [[HS-578T (line)]] | alt | 25.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -17.4) |
| [[NCI-H2030 (line)]] | alt | 37.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -18.5) |
| [[C-33 A (line)]] | alt | 9.27 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0912× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 28.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -9.4) |
| [[A-172 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.80 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8762), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KTN1-AS1]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[APBA2]] | +0.59 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[GALNT14]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[RHOBTB1]] | +0.58 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[KHDC1]] | +0.55 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[SMO]] | +0.53 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[POLR3G]] | +0.53 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[MLH3]] | +0.53 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[NT5M]] | +0.52 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[ADCY3]] | +0.51 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[DNAJC6]] | +0.51 | +0.32 / +0.45 | both halves | 2e-04 |  |
| [[CHST10]] | +0.51 | +0.53 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERBB3]] | -0.55 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[GABARAP]] ⚠ | -0.53 | -0.45 / -0.50 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PNPLA2]] | -0.52 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[RNF5]] | -0.51 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[ALDH6A1]] | -0.51 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[FOXO4]] | -0.49 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[PLAG1]] | -0.48 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[MAT2B]] | -0.48 | -0.43 / -0.46 | both halves | 4e-05 |  |
| [[C8orf82]] | -0.48 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[ABHD16A]] | -0.47 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[RORC]] | -0.47 | -0.54 / -0.28 | both halves | 3e-04 |  |
| [[AGFG2]] | -0.46 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[BAD]] | -0.46 | -0.44 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBX18]] | B | TBX18 activity raises PCOLCE2's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 2.58× lower at baseline in the lines without TBX18 | 0.012 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251 |
| [[MCOLN2]] | B | MCOLN2 activity raises PCOLCE2's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 2.93× lower at baseline in the lines without MCOLN2 | 0.028 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[P3H2-AS1]] | B | P3H2-AS1 activity raises PCOLCE2's level | lines that do not express P3H2-AS1 (30) vs lines expressing it (20) | 2.71× lower at baseline in the lines without P3H2-AS1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: P3H2, SRGN, KIRREL3 |
| [[MCOLN2]] | B | MCOLN2 activity strengthens PCOLCE2's drug response | lines that do not express MCOLN2 (8) vs lines expressing it (24) | the lines without MCOLN2 respond 0.59× as strongly (z diff +2.10); strongest at Panobinostat 5 µM: 0.76x vs 0.40x (z diff +4.9) | 0.036 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG; target measured in part of the lines; artifact flags |
| [[FBXO17]] | B | FBXO17 activity raises PCOLCE2's level | lines that do not express FBXO17 (18) vs lines expressing it (32) | 2.66× lower at baseline in the lines without FBXO17 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, MRC2, MIR130AHG |
| [[TTC7B]] | B | TTC7B activity raises PCOLCE2's level | lines that do not express TTC7B (9) vs lines expressing it (41) | 3.75× lower at baseline in the lines without TTC7B | 0.077 | ⚠ within organs, on part of the lines; also absent: SYNGR1, HDGFL3, HLTF |
| [[B4GALNT1]] | C | B4GALNT1 activity raises PCOLCE2's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 3.61× lower at baseline in the lines without B4GALNT1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1; co-absent with the target |
| [[ARHGEF25]] | C | ARHGEF25 activity raises PCOLCE2's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 3.73× lower at baseline in the lines without ARHGEF25 | 0.058 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCAF11]] | B | PCOLCE2 activity lowers DCAF11's level | lines that do not express PCOLCE2 (16) vs lines expressing it (34) | 1.44× higher at baseline in the lines without PCOLCE2 | 0.063 | ⚠ within organs, on part of the lines; also absent: WDR17, NRG1, TSHZ3 |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.483). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (21.9, -23.4); signed map (17.4, 22.3). **Vector** length 81.2, 19.6% of its response variance represented; |z| ≥ 3 in 833 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +11.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +4.7 | +4.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.5 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.2 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.6 | +1.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -16.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.4 | -6.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.4 | -10.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.3 | -5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.3 | -30.3 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -7.7 |

## What is on record

|  |  |
|---|---|
| Name | procollagen C-endopeptidase enhancer 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:142,815,922-142,889,206 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PCPE2 |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 3 pathways, smallest: Collagen biosynthesis and modifying enzymes; Collagen formation; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKZ9](https://www.uniprot.org/uniprotkb/Q9UKZ9) (Procollagen C-endopeptidase enhancer 2):

> Binds to the C-terminal propeptide of types I and II procollagens and may enhance the cleavage of that propeptide by BMP1.

**Summary**, from NCBI Gene [26577](https://www.ncbi.nlm.nih.gov/gene/26577):

> Enables collagen binding activity; heparin binding activity; and peptidase activator activity. Predicted to act upstream of or within cellular response to leukemia inhibitory factor. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:8739](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8739) · Entrez [26577](https://www.ncbi.nlm.nih.gov/gene/26577) · UniProt [Q9UKZ9](https://www.uniprot.org/uniprotkb/Q9UKZ9) · Ensembl [ENSG00000163710](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163710)

## Data

Gene col 8762: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8762); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8762, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8762]; `tensor/DDL_lfc|DDL_z.npy` [8762]; `embed/gene_vectors.npy` [8762]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8762 or target_col == 8762). Every well: [[PCOLCE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCOLCE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
