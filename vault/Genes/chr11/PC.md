---
symbol: "PC"
type: "gene"
col: 10408
ensembl_id: "ENSG00000173599"
name: "pyruvate carboxylase"
location: "11q13.2"
module: 136
arm: "+"
pooled_cpm: 24.01
n_lines_expressing: 46
n_dd_up: 14
n_dd_down: 30
n_dd_up_clean: 14
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# PC

*pyruvate carboxylase* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 6.17× (z +23.8, q 0e+00, up in 43 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.511× (z -8.8, q 1e-15, down in 32 of 42 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMOX]] (+0.61, fdr 1e-05), [[GNAI2]] (+0.59, fdr 6e-05), [[EPOR]] (+0.59, fdr 1e-05); moves opposite to [[GAS2]] (-0.55, fdr 4e-04), [[NIPAL2]] (-0.55, fdr 2e-04), [[KLHL42]] (-0.54, fdr 1e-04).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[EPAS1]] → it (grade B ⚠); 3 go from it, the strongest it → [[NSMAF]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10408.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **6.17×** | +23.8 | 0e+00 | 43/44 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.79×** | +20.5 | 0e+00 | 42/44 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.91×** | +17.8 | 0e+00 | 40/43 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.90×** | +8.4 | 5e-15 | 34/44 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +7.8 | 6e-13 | 23/41 (LoVo, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +6.9 | 7e-10 | 24/44 (SW 900, BT-474, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.12×** | +5.1 | 2e-05 | 23/44 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.8 | 1e-04 | 14/44 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.42×** | +4.6 | 3e-04 | 18/43 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.004 | 19/42 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.014 | 17/42 (NCI-H2030, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.033 | 17/43 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.58×** | +3.1 | 0.075 | 9/41 (HCT15, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.094 | 10/43 (NCI-H1573, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10408.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.511×** | -8.8 | 1e-15 | 32/42 (A549, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.523×** | -8.1 | 1e-13 | 26/39 (NCI-H1792, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.570×** | -7.3 | 5e-11 | 30/43 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.575×** | -7.2 | 8e-11 | 27/43 (A549, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.638×** | -5.8 | 6e-07 | 22/43 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.675×** | -5.1 | 3e-05 | 26/43 (LOX-IMVI, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.673×** | -4.9 | 1e-04 | 24/43 (A549, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.697×** | -4.7 | 2e-04 | 21/43 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.703×** | -4.6 | 3e-04 | 22/44 (PANC-1, NCI-H460, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.709×** | -4.5 | 4e-04 | 18/43 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.534×** | -4.3 | 1e-03 | 20/40 (RPMI-7951, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.793×** | -4.3 | 1e-03 | 13/44 (CFPAC-1, A549, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.734×** | -4.0 | 0.002 | 19/43 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.574×** | -3.8 | 0.006 | 14/40 (NCI-H460, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.741×** | -3.7 | 0.007 | 17/39 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.753×** | -3.7 | 0.008 | 21/43 (J82, RPMI-7951, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.582×** | -3.7 | 0.008 | 17/44 (A549, HCT15, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.824×** | -3.5 | 0.012 | 17/44 (SNU-423, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Megestrol (drug)]] 5 µM |  | 0.839× | -3.2 | 0.036 | 14/44 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.633×** | -3.1 | 0.044 | 16/41 (A549, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10408. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 54.4 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.169× (z -12.3) |
| [[NCI-H1792 (line)]] | alt | 147 | 0 | 7 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.150× (z -15.2) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.308× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 45.5 | 1 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.84× (z +8.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.190× (z -13.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.347× (z -8.7) |
| [[PANC-1 (line)]] | alt | 18.3 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 6.32× (z +14.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -10.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.324× (z -8.9) |
| [[SW480 (line)]] | alt | 16.1 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 10.7× (z +18.7) | — |
| [[NCI-H2030 (line)]] | alt | 75.6 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0656× (z -17.6) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.283× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 18.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 13.3× (z +13.5) | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[BT-474 (line)]] | alt | 13.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 11.0× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 22.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.14× (z +14.1) | — |
| [[LoVo (line)]] | wt | 7.23 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 12.7× (z +13.9) | — |
| [[NCI-H1573 (line)]] | alt | 33.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.29× (z +13.4) | — |
| [[SNU-423 (line)]] | alt | 39.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.258× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 15.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.58× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 16.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.98× (z +13.5) | — |
| [[KATO III (line)]] | alt | 15.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 17.2× (z +15.1) | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.18× (z +9.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0370× (z -15.0) ⚠ toxic · without an alert: [[5-Azacytidine (drug)]] 5 µM 0.129× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 12.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.57× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 10.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 16.4× (z +14.2) | — |
| [[A-172 (line)]] | wt | 15.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.56× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.177× (z -8.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 21.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.72× (z +11.4) | — |
| [[J82 (line)]] | alt | 23.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.85× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 8.23× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 23.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.18× (z +10.1) | — |
| [[A-427 (line)]] | wt | 7.02 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 11.2× (z +10.4) | — |
| [[H4 (line)]] | wt | 13.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 11.4× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 33.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.76× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 15.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.77× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 23.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[LS 180 (line)]] | wt | 19.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.42× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 14.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.84× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 28.5 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0407× (z -9.5) |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.190× (z -9.7) |
| [[A498 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.43 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.56 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.48 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.06 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10408), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMOX]] | +0.61 | +0.52 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[GNAI2]] | +0.59 | +0.48 / +0.38 | both halves | 6e-05 | same gene group |
| [[EPOR]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[PLPPR2]] | +0.57 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[EFEMP2]] | +0.56 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[PCBP3]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[LOXL2]] | +0.55 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[DNAAF3]] | +0.53 | +0.37 / +0.41 | both halves | 9e-05 |  |
| [[PAG1]] | +0.53 | +0.31 / +0.41 | both halves | 2e-04 |  |
| [[PORCN]] | +0.52 | +0.40 / +0.34 | both halves | 1e-04 |  |
| [[SLC6A6]] | +0.52 | +0.33 / +0.46 | both halves | 1e-04 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[CYB5R3]] | +0.52 | +0.36 / +0.40 | both halves | 1e-04 | pathway: Metabolism of vitamins and cofactors |

## Genes that move opposite

*36 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAS2]] | -0.55 | -0.37 / -0.24 | both halves | 4e-04 |  |
| [[NIPAL2]] | -0.55 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[KLHL42]] | -0.54 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[HNF4G]] | -0.54 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[ITPKB]] | -0.52 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[OTUD4]] | -0.52 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[RAB11FIP2]] | -0.51 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[PHACTR2]] | -0.51 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[SYK]] | -0.51 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[MVB12B]] | -0.50 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[SMAD1]] | -0.49 | -0.24 / -0.37 | both halves | 5e-04 |  |
| [[UFL1-AS1]] | -0.49 | -0.35 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPAS1]] | B | EPAS1 activity raises PC's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 2.86× lower at baseline in the lines without EPAS1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[HPCAL1]] | B | HPCAL1 activity raises PC's level | lines that do not express HPCAL1 (6) vs lines expressing it (44) | 2.86× lower at baseline in the lines without HPCAL1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SHB, ARMCX3, ECE1; maybe low, not absent |
| [[LINC00887]] | B | LINC00887 activity raises PC's level | lines that do not express LINC00887 (8) vs lines expressing it (42) | 1.73× lower at baseline in the lines without LINC00887 | 0.073 | ⚠ within organs, on part of the lines; also absent: LINC02036, STAMBPL1, CFAP45; maybe low, not absent |
| [[SMOX]] | B | SMOX activity raises PC's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.06× lower at baseline in the lines without SMOX | 0.078 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NSMAF]] | C | PC activity lowers NSMAF's level | lines that do not express PC (4) vs lines expressing it (46) | 2.48× higher at baseline in the lines without PC | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP1, ANKEF1, ZFAND4; maybe low, not absent; its own permutation p |
| [[OTUD4]] | C | PC activity lowers OTUD4's level | lines that do not express PC (4) vs lines expressing it (46) | 1.68× higher at baseline in the lines without PC | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP1, ANKEF1, ZFAND4; maybe low, not absent; its own permutation p |
| [[EPAS1]] | C | PC activity raises EPAS1's level | lines that do not express PC (4) vs lines expressing it (46) | 5.20× lower at baseline in the lines without PC | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP1, ANKEF1, ZFAND4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.9, -1.8); signed map (-24.1, 25.5). **Vector** length 92.1, 22.1% of its response variance represented; |z| ≥ 3 in 1,316 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +20.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +23.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.4 | +17.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +6.9 |
|  | [[Posaconazole (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.6 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.7 | -3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -4.8 | +1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -8.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.7 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -7.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | +0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | pyruvate carboxylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,848,417-66,958,386 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PCB |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Pyruvate carboxylase family; ATP-grasp fold containing |
| Hallmark sets | MYOGENESIS, XENOBIOTIC_METABOLISM, HEME_METABOLISM, GLYCOLYSIS |
| Reactome | 12 pathways, smallest: Defective HLCS causes multiple carboxylase deficiency; Defects in biotin (Btn) metabolism; Biotin transport and metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P11498](https://www.uniprot.org/uniprotkb/P11498) (Pyruvate carboxylase, mitochondrial):

> Pyruvate carboxylase catalyzes a 2-step reaction, involving the ATP-dependent carboxylation of the covalently attached biotin in the first step and the transfer of the carboxyl group to pyruvate in the second. Catalyzes in a tissue specific manner, the initial reactions of glucose (liver, kidney) and lipid (adipose tissue, liver, brain) synthesis from pyruvate.

**Summary**, from NCBI Gene [5091](https://www.ncbi.nlm.nih.gov/gene/5091):

> This gene encodes pyruvate carboxylase, which requires biotin and ATP to catalyse the carboxylation of pyruvate to oxaloacetate. The active enzyme is a homotetramer arranged in a tetrahedron which is located exclusively in the mitochondrial matrix. Pyruvate carboxylase is involved in gluconeogenesis, lipogenesis, insulin secretion and synthesis of the neurotransmitter glutamate. Mutations in this gene have been associated with pyruvate carboxylase deficiency. Alternatively spliced transcript …

**Accessions** — [HGNC:8636](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8636) · Entrez [5091](https://www.ncbi.nlm.nih.gov/gene/5091) · UniProt [P11498](https://www.uniprot.org/uniprotkb/P11498) · Ensembl [ENSG00000173599](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173599)

## Data

Gene col 10408: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10408); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10408, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10408]; `tensor/DDL_lfc|DDL_z.npy` [10408]; `embed/gene_vectors.npy` [10408]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10408 or target_col == 10408). Every well: [[PC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
