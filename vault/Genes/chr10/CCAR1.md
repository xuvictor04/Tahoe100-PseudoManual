---
symbol: "CCAR1"
type: "gene"
col: 686
ensembl_id: "ENSG00000060339"
name: "cell division cycle and apoptosis regulator 1"
location: "10q21.3"
module: 46
arm: "+"
pooled_cpm: 142.84
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# CCAR1

*cell division cycle and apoptosis regulator 1* — 10q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.38× (z +27.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.581× (z -12.0, q 1e-30, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPAP2]] (+0.73, fdr 7e-06), [[TRIP11]] (+0.71, fdr 1e-05), [[GABPB2]] (+0.70, fdr 1e-05); moves opposite to [[IGSF8]] (-0.66, fdr 1e-04), [[ST6GALNAC4]] (-0.65, fdr 5e-05), [[AIF1L]] (-0.63, fdr 6e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SEPTIN3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 686.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.38×** | +27.1 | 0e+00 | 48/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.59×** | +21.1 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.17×** | +16.5 | 0e+00 | 46/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +12.6 | 2e-34 | 44/49 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.73×** | +12.2 | 6e-32 | 45/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.72×** | +12.1 | 1e-31 | 46/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +9.9 | 3e-21 | 36/44 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.54×** | +8.8 | 7e-17 | 43/47 (LS 180, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +7.6 | 1e-12 | 29/49 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +6.9 | 3e-10 | 30/45 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.9 | 4e-05 | 16/48 (A498, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.24×** | +4.8 | 8e-05 | 26/48 (HT-29, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.7 | 1e-04 | 15/48 (SW1417, A-427, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.23×** | +4.6 | 2e-04 | 27/48 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.5 | 2e-04 | 28/50 (A-427, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.23×** | +4.5 | 2e-04 | 27/48 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.22×** | +4.5 | 3e-04 | 27/48 (NCI-H1573, SW480, …) | top dose only |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.012 | 22/48 (MIA PaCa-2, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.036 | 21/48 (LoVo, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.038 | 16/49 (NCI-H460, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 686.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.581×** | -12.0 | 1e-30 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.640×** | -9.9 | 2e-20 | 46/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.642×** | -9.8 | 2e-20 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.765×** | -5.9 | 4e-07 | 35/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.845× | -5.2 | 2e-05 | 22/48 (SW480, LoVo, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -4.6 | 3e-04 | 1/50 (SW 1271) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.829×** | -4.1 | 0.003 | 25/49 (CHP-212, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.719×** | -3.8 | 0.009 | 26/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.842× | -3.8 | 0.009 | 16/48 (C32, J82, …) | two highest doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.853× | -3.2 | 0.067 | 12/48 (SW1417, C32, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.870× | -3.1 | 0.11 | 5/48 (BT-474, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 686. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 230 | 6 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +22.8) | [[Panobinostat (drug)]] 5 µM 0.381× (z -18.2) |
| [[LoVo (line)]] | wt | 148 | 6 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +21.8) | [[Panobinostat (drug)]] 5 µM 0.435× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 180 | 6 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +25.8) | [[Panobinostat (drug)]] 5 µM 0.441× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 133 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +22.5) | — |
| [[PANC-1 (line)]] | alt | 189 | 7 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +34.6) | [[Panobinostat (drug)]] 5 µM 0.558× (z -9.8) |
| [[LS 180 (line)]] | wt | 118 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +15.3) | — |
| [[NCI-H460 (line)]] | wt | 178 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +22.2) | [[Panobinostat (drug)]] 5 µM 0.446× (z -13.8) |
| [[A-172 (line)]] | wt | 148 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +22.1) | — |
| [[A498 (line)]] | wt | 130 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +23.3) | — |
| [[A549 (line)]] | wt | 138 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +22.5) | [[Panobinostat (drug)]] 5 µM 0.477× (z -10.1) |
| [[COLO 205 (line)]] | alt | 94.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +15.5) | — |
| [[KATO III (line)]] | alt | 116 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +15.3) | — |
| [[NCI-H1573 (line)]] | alt | 124 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +21.3) | — |
| [[Panc 03.27 (line)]] | alt | 158 | 4 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.7) | [[Panobinostat (drug)]] 5 µM 0.474× (z -10.6) |
| [[C-33 A (line)]] | alt | 201 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.57× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -10.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 114 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +15.3) | — |
| [[NCI-H1792 (line)]] | alt | 129 | 3 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 3.04× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.451× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 157 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +20.2) | [[Panobinostat (drug)]] 5 µM 0.456× (z -11.3) |
| [[SW1417 (line)]] | alt | 121 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.506× (z -10.4) |
| [[SW48 (line)]] | wt | 198 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +17.4) | — |
| [[CFPAC-1 (line)]] | alt | 104 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +16.8) | — |
| [[HepG2_C3A (line)]] | wt | 135 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +17.5) | — |
| [[Hs 766T (line)]] | wt | 112 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +17.4) | — |
| [[HT-29 (line)]] | alt | 132 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +16.6) | — |
| [[LOX-IMVI (line)]] | wt | 112 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +12.4) | — |
| [[RKO (line)]] | wt | 166 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.2) | — |
| [[SW 900 (line)]] | alt | 160 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +15.8) | [[Panobinostat (drug)]] 5 µM 0.512× (z -9.0) |
| [[A-427 (line)]] | wt | 159 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +15.8) | — |
| [[CHP-212 (line)]] | wt | 201 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.292× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 202 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +18.9) | — |
| [[HS-578T (line)]] | alt | 82.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.0) | — |
| [[NCI-H2347 (line)]] | alt | 126 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +20.5) | — |
| [[SNU-423 (line)]] | alt | 138 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +18.8) | — |
| [[AsPC-1 (line)]] | alt | 87.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +13.6) | — |
| [[C32 (line)]] | wt | 111 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.7) | — |
| [[H4 (line)]] | wt | 101 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 165 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.6) | — |
| [[RPMI-7951 (line)]] | alt | 128 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +18.3) | — |
| [[SNU-1 (line)]] | wt | 171 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.51× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -13.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 142 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.8) | — |
| [[J82 (line)]] | alt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 112 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +9.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 147 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 686), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPAP2]] | +0.73 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.71 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[GABPB2]] | +0.70 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[THOC7]] | +0.70 | +0.63 / +0.66 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TCEAL4]] | +0.70 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[RAD52]] | +0.69 | +0.75 / +0.45 | both halves | 3e-05 |  |
| [[ZNF764]] | +0.69 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[RC3H2]] | +0.69 | +0.68 / +0.48 | both halves | 2e-05 | same gene group |
| [[FBXW4]] | +0.69 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[BDP1]] | +0.69 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[TIMMDC1]] | +0.69 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[AIMP1]] | +0.68 | +0.70 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGSF8]] | -0.66 | -0.66 / -0.34 | both halves | 1e-04 |  |
| [[ST6GALNAC4]] | -0.65 | -0.63 / -0.39 | both halves | 5e-05 |  |
| [[AIF1L]] | -0.63 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[RIMS3]] | -0.62 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[GPRIN1]] | -0.62 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[SIPA1]] | -0.61 | -0.52 / -0.43 | both halves | 3e-05 | same gene group |
| [[SMG1P2]] | -0.61 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[TPST2]] | -0.61 | -0.62 / -0.37 | both halves | 8e-05 | same gene group |
| [[SPTLC2]] | -0.61 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[LPCAT4]] | -0.61 | -0.60 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEPTIN3]] | B | SEPTIN3 activity raises CCAR1's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 1.26× lower at baseline in the lines without SEPTIN3 | 0.013 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CCAR1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises CCAR1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RAB39A]] | B | RAB39A activity raises CCAR1's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 1.14× lower at baseline in the lines without RAB39A | 0.088 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent |
| [[VASH2]] | B | VASH2 activity raises CCAR1's level | lines that do not express VASH2 (9) vs lines expressing it (41) | 1.27× lower at baseline in the lines without VASH2 | 0.091 | ⚠ within organs, on part of the lines; also absent: WNT9A, STOX1, ZNF254; maybe low, not absent |
| [[PODXL2]] | B | PODXL2 activity raises CCAR1's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.21× lower at baseline in the lines without PODXL2 | 0.098 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.586). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.8, 7.9); signed map (13.2, -26.2). **Vector** length 136, 47.2% of its response variance represented; |z| ≥ 3 in 1,141 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.6 | +21.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +10.6 | +27.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +9.2 | +12.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.8 | +16.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.3 | +12.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.9 | +8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.7 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +1.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -9.7 | -9.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -9.3 | -12.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -8.9 | -9.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.9 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.5 | -5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | +1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle and apoptosis regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.3 — chr10:68,721,012-68,792,377 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CARP1, CARP-1, uc.285+, FLJ10590 |
| Gene groups (HGNC) | Spliceosomal A complex; MicroRNA protein coding host genes; Small nucleolar RNA protein coding host genes |
| Reactome | 9 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IX12](https://www.uniprot.org/uniprotkb/Q8IX12) (Cell division cycle and apoptosis regulator protein 1):

> Associates with components of the Mediator and p160 coactivator complexes that play a role as intermediaries transducing regulatory signals from upstream transcriptional activator proteins to basal transcription machinery at the core promoter. Recruited to endogenous nuclear receptor target genes in response to the appropriate hormone. Also functions as a p53 coactivator. May thus play an important role in transcriptional regulation (By similarity). May be involved in apoptosis signaling in the …

**Summary**, from NCBI Gene [55749](https://www.ncbi.nlm.nih.gov/gene/55749):

> Enables RNA polymerase II cis-regulatory region sequence-specific DNA binding activity; transcription coactivator activity; and transcription corepressor activity. Involved in positive regulation of cell migration and positive regulation of cell population proliferation. Acts upstream of or within positive regulation of apoptotic process. Located in Golgi apparatus; nuclear envelope lumen; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24236](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24236) · Entrez [55749](https://www.ncbi.nlm.nih.gov/gene/55749) · UniProt [Q8IX12](https://www.uniprot.org/uniprotkb/Q8IX12) · Ensembl [ENSG00000060339](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000060339)

## Data

Gene col 686: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 686); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 686, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 686]; `tensor/DDL_lfc|DDL_z.npy` [686]; `embed/gene_vectors.npy` [686]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 686 or target_col == 686). Every well: [[CCAR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCAR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
