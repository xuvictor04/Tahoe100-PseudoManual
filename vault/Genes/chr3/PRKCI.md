---
symbol: "PRKCI"
type: "gene"
col: 8717
ensembl_id: "ENSG00000163558"
name: "protein kinase C iota"
location: "3q26.2"
module: 23
arm: "-"
pooled_cpm: 144.27
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# PRKCI

*protein kinase C iota* — 3q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.39× (z +8.7, q 2e-15, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.546× (z -22.7, q 0e+00, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RTN3]] (+0.66, fdr 7e-06), [[CAST]] (+0.63, fdr 1e-05), [[CDA]] (+0.62, fdr 2e-05); moves opposite to [[ZNF689]] (-0.62, fdr 1e-05), [[SCGB2B2]] (-0.60, fdr 3e-05), [[LINS1]] (-0.59, fdr 3e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8717.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +8.7 | 2e-15 | 28/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +7.3 | 7e-11 | 28/47 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +7.2 | 7e-11 | 29/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +7.2 | 7e-11 | 30/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +6.0 | 2e-07 | 19/49 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.25×** | +5.9 | 3e-07 | 26/49 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.22×** | +5.3 | 1e-05 | 25/48 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +5.2 | 2e-05 | 26/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +5.0 | 3e-05 | 22/48 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +5.0 | 4e-05 | 17/48 (PANC-1, H4, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.19× | +4.7 | 1e-04 | 19/49 (SW1417, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.6 | 2e-04 | 22/48 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.1 | 0.002 | 14/48 (PANC-1, SW1417, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.17× | +4.0 | 0.002 | 17/48 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.023 | 15/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.14× | +3.4 | 0.023 | 12/47 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.13× | +3.1 | 0.067 | 7/48 (HS-578T, HOP62, …) | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.12× | +3.0 | 0.071 | 6/48 (SK-MEL-2, H4, …) | inconsistent across doses | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8717.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.546×** | -22.7 | 0e+00 | 45/49 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.889× | -10.9 | 4e-25 | 6/50 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.824×** | -7.2 | 9e-11 | 22/48 (SW1417, CFPAC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -7.2 | 1e-10 | 31/48 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.765×** | -6.8 | 9e-10 | 30/50 (SW480, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.806×** | -5.5 | 4e-06 | 26/48 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.836× | -4.7 | 2e-04 | 22/48 (AsPC-1, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | 0.839× | -4.5 | 6e-04 | 23/47 (RKO, CFPAC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~4% of this change | 0.850× | -4.3 | 0.001 | 19/48 (MIA PaCa-2, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.907× | -3.6 | 0.016 | 2/48 (NCI-H460, Hs 766T) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | 0.800× | -3.0 | 0.14 | 11/48 (LoVo, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8717. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 100 | 8 (6 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.72× (z +18.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +16.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 182 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -18.0) |
| [[PANC-1 (line)]] | alt | 106 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.79× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 174 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -27.2) |
| [[AsPC-1 (line)]] | alt | 148 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -20.0) |
| [[LS 180 (line)]] | wt | 127 | 3 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.01× (z +9.6) | — |
| [[RKO (line)]] | wt | 181 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.324× (z -15.2) ⚠ toxic; cell-cycle shift, explains ~23% of this change |
| [[SK-MEL-2 (line)]] | alt | 156 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -11.2) |
| [[BT-474 (line)]] | alt | 140 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 1.99× (z +8.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 187 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -23.1) |
| [[HOP62 (line)]] | alt | 147 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -13.2) |
| [[HS-578T (line)]] | alt | 155 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -14.2) |
| [[LoVo (line)]] | wt | 130 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.21× (z +12.8) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -20.8) |
| [[MIA PaCa-2 (line)]] | alt | 205 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.03× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -19.6) |
| [[NCI-H23 (line)]] | alt | 61.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 92.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.13× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -14.1) |
| [[SNU-423 (line)]] | alt | 116 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -14.1) |
| [[SW1417 (line)]] | alt | 156 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -16.4) |
| [[A-427 (line)]] | wt | 337 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.643× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 117 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -10.5) |
| [[AN3 CA (line)]] | alt | 159 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -19.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 93.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -15.2) |
| [[H4 (line)]] | wt | 155 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 81.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -11.9) |
| [[Hs 766T (line)]] | wt | 102 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -10.5) |
| [[HT-29 (line)]] | alt | 205 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -11.9) |
| [[J82 (line)]] | alt | 209 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -12.5) |
| [[KATO III (line)]] | alt | 128 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 95.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 106 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -15.6) |
| [[Panc 03.27 (line)]] | alt | 216 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -16.2) |
| [[SW 900 (line)]] | alt | 98.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -9.9) |
| [[SW48 (line)]] | wt | 172 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +11.2) | — |
| [[A-172 (line)]] | wt | 166 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 196 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 63.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 212 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 101 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 193 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8717), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTN3]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[CAST]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CDA]] | +0.62 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[LLGL2]] | +0.61 | +0.47 / +0.41 | both halves | 4e-05 | STRING 996 |
| [[OSBPL9]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[KRAS]] | +0.57 | +0.59 / +0.48 | both halves | 2e-05 | STRING 524 |
| [[SOAT1]] | +0.57 | +0.36 / +0.59 | both halves | 9e-05 |  |
| [[STX7]] | +0.57 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[SERAC1]] | +0.55 | +0.55 / +0.38 | both halves | 6e-05 |  |
| [[RALGPS2]] | +0.55 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[AP2A2]] | +0.54 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[LPCAT2]] | +0.54 | +0.46 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF689]] | -0.62 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[SCGB2B2]] | -0.60 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[LINS1]] | -0.59 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[KIAA0753]] | -0.57 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[SON]] | -0.56 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[RECQL5]] | -0.55 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[KBTBD4]] | -0.55 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[TSSC4]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[UBE3B]] | -0.54 | -0.54 / -0.32 | both halves | 1e-04 |  |
| [[PEF1]] | -0.54 | -0.55 / -0.29 | both halves | 2e-04 |  |
| [[TYSND1]] | -0.54 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[ARMC5]] | -0.53 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PRKCI's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 1.4% of all compounds | 0.004 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity raises PRKCI's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.373). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-8.6, 7.2); signed map (-18.3, 28.3). **Vector** length 118, 33.5% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +11.0 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +10.8 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.5 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +7.1 | +4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.1 | +6.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.9 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.1 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.0 | +1.6 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.4 | -2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -22.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.1 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -7.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -5.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase C iota |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.2 — chr3:170,222,424-170,305,977 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PKCλ/ι, PKCλ, PKCι, PKCI; previously DXS1179E |
| Gene groups (HGNC) | Protein kinase C family |
| Reactome | 15 pathways, smallest: p75NTR recruits signalling complexes; p75NTR signals via NF-kB; Tight junction interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P41743](https://www.uniprot.org/uniprotkb/P41743) (Protein kinase C iota type):

> Calcium- and diacylglycerol-independent serine/ threonine-protein kinase that plays a general protective role against apoptotic stimuli, is involved in NF-kappa-B activation, cell survival, differentiation and polarity, and contributes to the regulation of microtubule dynamics in the early secretory pathway. Is necessary for BCR-ABL oncogene-mediated resistance to apoptotic drug in leukemia cells, protecting leukemia cells against drug-induced apoptosis. In cultured neurons, prevents amyloid …

**Summary**, from NCBI Gene [5584](https://www.ncbi.nlm.nih.gov/gene/5584):

> This gene encodes a member of the protein kinase C (PKC) family of serine/threonine protein kinases. The PKC family comprises at least eight members, which are differentially expressed and are involved in a wide variety of cellular processes. This protein kinase is calcium-independent and phospholipid-dependent. It is not activated by phorbolesters or diacylglycerol. This kinase can be recruited to vesicle tubular clusters (VTCs) by direct interaction with the small GTPase RAB2, where this …

**Accessions** — [HGNC:9404](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9404) · Entrez [5584](https://www.ncbi.nlm.nih.gov/gene/5584) · UniProt [P41743](https://www.uniprot.org/uniprotkb/P41743) · Ensembl [ENSG00000163558](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163558)

## Data

Gene col 8717: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8717); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8717, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8717]; `tensor/DDL_lfc|DDL_z.npy` [8717]; `embed/gene_vectors.npy` [8717]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8717 or target_col == 8717). Every well: [[PRKCI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKCI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
