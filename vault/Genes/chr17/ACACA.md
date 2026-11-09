---
symbol: "ACACA"
type: "gene"
col: 15916
ensembl_id: "ENSG00000278540"
name: "acetyl-CoA carboxylase alpha"
location: "17q12"
module: 18
arm: "+"
pooled_cpm: 150.8
n_lines_expressing: 49
n_dd_up: 30
n_dd_down: 4
n_dd_up_clean: 20
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ACACA

*acetyl-CoA carboxylase alpha* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.83× (z +10.7, q 6e-24, up in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Cepharanthine (drug)]] 5 µM: 1.53× (z +10.6, q 8e-24, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.686× (z -6.4, q 9e-08, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FASN]] (+0.67, fdr 7e-06), [[LRP8]] (+0.66, fdr 7e-06), [[LETM1]] (+0.64, fdr 7e-06); moves opposite to [[SLU7]] (-0.53, fdr 1e-05), [[GCC2]] (-0.51, fdr 1e-05), [[MYNN]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TSEN2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15916.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.83×** | +10.7 | 6e-24 | 36/47 (Panc 03.27, A549, …) | all doses, stronger at high dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.53×** | +10.6 | 8e-24 | 45/47 (A549, HT-29, …) | top dose only |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **1.76×** | +10.0 | 4e-21 | 42/47 (SW480, COLO 205, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.61×** | +8.4 | 8e-15 | 34/47 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Berbamine (drug)]] 5 µM |  | **1.39×** | +8.2 | 2e-14 | 38/48 (A549, HT-29, …) | rises with dose |  |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.56×** | +7.8 | 5e-13 | 38/47 (COLO 205, SW480, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +7.5 | 4e-12 | 35/47 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +7.5 | 5e-12 | 33/46 (NCI-H1792, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.48×** | +6.9 | 3e-10 | 30/47 (NCI-H460, A549, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.47×** | +6.8 | 6e-10 | 33/47 (HT-29, C-33 A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.47×** | +6.8 | 7e-10 | 29/47 (A549, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.40×** | +5.5 | 2e-06 | 25/44 (RPMI-7951, NCI-H23, …) | inconsistent across doses | composition shift |
| [[Bexarotene (drug)]] 5 µM |  | **1.35×** | +5.3 | 4e-06 | 28/47 (HT-29, SW1417, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +5.3 | 4e-06 | 31/46 (A549, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +5.3 | 5e-06 | 28/47 (MIA PaCa-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.34×** | +5.1 | 1e-05 | 34/47 (NCI-H1573, COLO 205, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.69×** | +4.9 | 4e-05 | 30/47 (NCI-H460, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.66×** | +4.7 | 9e-05 | 29/47 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | **1.20×** | +4.6 | 1e-04 | 21/48 (HT-29, C-33 A, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.65×** | +4.6 | 1e-04 | 33/47 (NCI-H460, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.31×** | +4.5 | 1e-04 | 28/47 (A549, COLO 205, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.62×** | +4.4 | 2e-04 | 32/47 (NCI-H460, A549, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15916.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.686×** | -6.4 | 9e-08 | 32/47 (PANC-1, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.841× | -4.3 | 0.004 | 19/47 (KATO III, LS 180, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.731×** | -3.9 | 0.015 | 24/47 (BT-474, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clotrimazole (drug)]] 5 µM |  | 0.860× | -3.8 | 0.022 | 20/48 (HT-29, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 0.862× | -3.7 | 0.022 | 23/47 (PANC-1, BT-474, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.822×** | -3.5 | 0.051 | 22/47 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.829×** | -3.3 | 0.076 | 21/47 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Bergenin (drug)]] 5 µM |  | 0.886× | -3.0 | 0.17 | 8/48 (COLO 205, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15916. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 293 | 7 | 1 | [[Cepharanthine (drug)]] 5 µM 2.69× (z +12.9) | [[Auranofin (drug)]] 5 µM 0.334× (z -10.3) |
| [[A549 (line)]] | wt | 137 | 7 (5 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 2.49× (z +14.8) | — |
| [[C-33 A (line)]] | alt | 325 | 5 | 2 (2 ⚠) | [[Bexarotene (drug)]] 0.5 µM 2.32× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 267 | 6 (1 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.78× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 85.7 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.26× (z +10.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Bexarotene (drug)]] 0.5 µM 2.75× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 113 | 3 (1 ⚠) | 1 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.09× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[NCI-H2347 (line)]] | alt | 68.1 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +11.2) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 155 | 4 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.51× (z +10.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.27× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 109 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.02× (z +12.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[PANC-1 (line)]] | alt | 142 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -14.4) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.335× (z -12.9) |
| [[A-172 (line)]] | wt | 107 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.55× (z +10.1) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[COLO 205 (line)]] | alt | 82.5 | 3 | 0 | [[Bexarotene (drug)]] 0.5 µM 5.80× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 266 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.407× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.502× (z -9.5) |
| [[J82 (line)]] | alt | 158 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -11.9) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.406× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 273 | 1 | 2 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 1.63× (z +9.7) | [[Harringtonine (drug)]] 5 µM 0.478× (z -9.9) |
| [[SW480 (line)]] | alt | 150 | 3 | 0 | [[Bexarotene (drug)]] 0.5 µM 2.64× (z +13.2) | — |
| [[A-427 (line)]] | wt | 183 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -16.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.482× (z -9.1) |
| [[BT-474 (line)]] | alt | 996 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -12.0) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.430× (z -9.5) |
| [[C32 (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -11.2) ⚠ cell-cycle shift, explains ~87% of this change |
| [[RPMI-7951 (line)]] | alt | 66.2 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +9.2) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 141 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.340× (z -12.1) |
| [[SNU-1 (line)]] | wt | 242 | 1 | 1 (1 ⚠) | [[Bexarotene (drug)]] 0.5 µM 2.29× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SW1417 (line)]] | alt | 115 | 2 | 0 | [[Bexarotene (drug)]] 0.5 µM 2.21× (z +9.7) | — |
| [[A498 (line)]] | wt | 147 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 1.89× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 38.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.90× (z +9.4) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HepG2_C3A (line)]] | wt | 87.1 | 1 | 0 | [[Bexarotene (drug)]] 0.5 µM 3.00× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 102 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 2.10× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 71.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.82× (z +8.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1573 (line)]] | alt | 49.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[SHP-77 (line)]] | alt | 147 | 1 | 0 | [[Bexarotene (drug)]] 0.5 µM 2.93× (z +11.4) | — |
| [[AN3 CA (line)]] | alt | 257 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 209 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 90.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 109 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 241 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 182 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15916), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FASN]] | +0.67 | +0.64 / +0.70 | both halves | 7e-06 | pathway: Activation of gene expression by SREBF (SREBP); STRING 998 |
| [[LRP8]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 | pathway: Metabolism of vitamins and cofactors |
| [[LETM1]] | +0.64 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[DHCR24]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 459 |
| [[DHCR7]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 435 |
| [[ABCC4]] | +0.59 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[PCSK9]] | +0.59 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[UCK2]] | +0.59 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[SLC29A2]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[MDN1]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[NAA25]] | +0.58 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[RAP1GDS1]] | +0.57 | +0.49 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLU7]] | -0.53 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[GCC2]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[MYNN]] | -0.50 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[PPP1R11]] | -0.50 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[KLHL28]] | -0.50 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[BET1]] | -0.50 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ZNF490]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[NECAP2]] | -0.50 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[NOSIP]] | -0.50 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[FAM161B]] | -0.50 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[ZNF160]] | -0.50 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[PPIL4]] | -0.50 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSEN2]] | C | TSEN2 activity raises ACACA's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.97× lower at baseline in the lines without TSEN2 | 0.080 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.600). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (20.3, -49.8); signed map (-50.9, 32.7). **Vector** length 153, 52.0% of its response variance represented; |z| ≥ 3 in 1,510 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.3 | +7.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +8.7 | +10.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +8.1 | +7.5 |
|  | [[Berbamine (drug)]] 5 µM |  | +6.8 | +8.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.6 | +5.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +5.4 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.3 | +5.3 |
|  | [[EX229 (drug)]] 5 µM |  | +4.7 | +4.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.7 | -6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -6.7 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.1 | -0.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.7 | -3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -2.6 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -2.4 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | acetyl-CoA carboxylase alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:37,084,992-37,406,836 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ACC1, ACC-alpha, ACCA, ACCalpha, ACACalpha, Acac1, hACC1; previously ACAC, ACC |
| Gene groups (HGNC) | Acetyl-CoA carboxylase family; ATP-grasp fold containing |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, MTORC1_SIGNALING |
| Reactome | 16 pathways, smallest: ChREBP activates metabolic gene expression; Defective HLCS causes multiple carboxylase deficiency; Defects in biotin (Btn) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13085](https://www.uniprot.org/uniprotkb/Q13085) (Acetyl-CoA carboxylase 1):

> Cytosolic enzyme that catalyzes the carboxylation of acetyl-CoA to malonyl-CoA, the first and rate-limiting step of de novo fatty acid biosynthesis. This is a 2 steps reaction starting with the ATP-dependent carboxylation of the biotin carried by the biotin carboxyl carrier (BCC) domain followed by the transfer of the carboxyl group from carboxylated biotin to acetyl-CoA.

**Summary**, from NCBI Gene [31](https://www.ncbi.nlm.nih.gov/gene/31):

> Acetyl-CoA carboxylase (ACC) is a complex multifunctional enzyme system. ACC is a biotin-containing enzyme which catalyzes the carboxylation of acetyl-CoA to malonyl-CoA, the rate-limiting step in fatty acid synthesis. There are two ACC forms, alpha and beta, encoded by two different genes. ACC-alpha is highly enriched in lipogenic tissues. The enzyme is under long term control at the transcriptional and translational levels and under short term regulation by the …

**Accessions** — [HGNC:84](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:84) · Entrez [31](https://www.ncbi.nlm.nih.gov/gene/31) · UniProt [Q13085](https://www.uniprot.org/uniprotkb/Q13085) · Ensembl [ENSG00000278540](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000278540)

## Data

Gene col 15916: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15916); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15916, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15916]; `tensor/DDL_lfc|DDL_z.npy` [15916]; `embed/gene_vectors.npy` [15916]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15916 or target_col == 15916). Every well: [[ACACA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACACA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
