---
symbol: "LRIG1"
type: "gene"
col: 6926
ensembl_id: "ENSG00000144749"
name: "leucine rich repeats and immunoglobulin like domains 1"
location: "3p14.1"
module: 13
arm: "+"
pooled_cpm: 44.04
n_lines_expressing: 39
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 13
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 21
direction_downstream: 7
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# LRIG1

*leucine rich repeats and immunoglobulin like domains 1* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.64× (z +12.3, q 8e-32, up in 20 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.618× (z -8.5, q 1e-14, down in 26 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CADM1]] (+0.68, fdr 7e-06), [[LFNG]] (+0.58, fdr 1e-04), [[GDNF]] (+0.53, fdr 1e-05); moves opposite to [[STXBP5]] (-0.51, fdr 2e-05), [[LINC00607]] (-0.48, fdr 8e-05), [[HECTD1]] (-0.46, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[TNS1]] → it (grade B ⚠); 7 go from it, the strongest it → [[ADAMTS9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6926.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +12.3 | 8e-32 | 20/37 (Panc 03.27, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +10.4 | 8e-23 | 19/37 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +9.2 | 5e-18 | 16/37 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.13×** | +7.0 | 5e-10 | 21/38 (BT-474, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +5.4 | 8e-06 | 13/37 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.74×** | +5.1 | 3e-05 | 14/35 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +5.0 | 5e-05 | 13/38 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.32×** | +4.9 | 5e-05 | 13/37 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.9 | 6e-05 | 14/37 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +4.3 | 9e-04 | 16/35 (HS-578T, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.005 | 12/37 (NCI-H2347, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.9 | 0.005 | 12/33 (Panc 03.27, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.068 | 3/36 (HT-29, SNU-423, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.075 | 5/35 (NCI-H2347, SW1417, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6926.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.618×** | -8.5 | 1e-14 | 26/37 (SW480, hTERT-HPNE, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.630×** | -8.1 | 1e-13 | 22/36 (hTERT-HPNE, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.636×** | -7.7 | 4e-12 | 20/33 (hTERT-HPNE, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.661×** | -7.0 | 4e-10 | 19/29 (SHP-77, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.679×** | -6.3 | 3e-08 | 19/30 (HEC-1-A, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Belzutifan (drug)]] 5 µM |  | **0.602×** | -4.7 | 3e-04 | 15/35 (BT-474, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.781×** | -4.3 | 0.001 | 18/37 (SW480, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.793×** | -4.1 | 0.003 | 16/36 (hTERT-HPNE, HS-578T, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 5 µM |  | 0.852× | -4.0 | 0.004 | 13/38 (A549, H4, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.802×** | -3.9 | 0.006 | 15/37 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.804×** | -3.7 | 0.012 | 17/37 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.814×** | -3.6 | 0.014 | 16/36 (HS-578T, H4, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.815×** | -3.6 | 0.014 | 10/37 (A-172, RPMI-7951, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.816×** | -3.6 | 0.014 | 17/37 (hTERT-HPNE, HS-578T, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.832×** | -3.2 | 0.043 | 17/37 (HS-578T, H4, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.832×** | -3.2 | 0.043 | 15/37 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.824×** | -3.1 | 0.054 | 14/34 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.836× | -3.1 | 0.054 | 13/37 (NCI-H1573, hTERT-HPNE, …) | two highest doses |  |
| [[Rosiglitazone (drug)]] 5 µM |  | 0.840× | -3.0 | 0.091 | 5/34 (LS 180, J82, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.840× | -2.9 | 0.091 | 7/37 (HepG2/C3A, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6926. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 269 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.155× (z -12.6) |
| [[HOP62 (line)]] | alt | 96.1 | 0 | 11 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.272× (z -9.9) |
| [[HS-578T (line)]] | alt | 169 | 0 | 11 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.210× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 30.7 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0689× (z -21.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 83.9 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.282× (z -13.4) |
| [[A-172 (line)]] | wt | 77.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.287× (z -9.5) |
| [[CHP-212 (line)]] | wt | 45.3 | 0 | 3 (1 ⚠) | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0509× (z -11.8) |
| [[LoVo (line)]] | wt | 14.7 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.44× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 169 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.223× (z -11.0) |
| [[SHP-77 (line)]] | alt | 132 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.345× (z -9.7) |
| [[BT-474 (line)]] | alt | 85.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 84.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -12.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -12.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 58.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.189× (z -9.7) |
| [[J82 (line)]] | alt | 52.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -11.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -9.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 31.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +11.7) | — |
| [[RKO (line)]] | wt | 21.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 91.5 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.210× (z -11.3) |
| [[SW1417 (line)]] | alt | 74.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -8.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 40.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -9.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 8.02 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.86 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.31 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.80 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.07 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6926), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CADM1]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[LFNG]] | +0.58 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[GDNF]] | +0.53 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[LINC01411]] | +0.50 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[SPOCK1]] | +0.50 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[NR3C2]] | +0.50 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[SOX9]] | +0.50 | +0.55 / +0.44 | both halves | 3e-05 | STRING 559 |
| [[CA8]] | +0.49 | +0.32 / +0.43 | both halves | 2e-04 |  |
| [[KIRREL3]] | +0.49 | +0.40 / +0.43 | both halves | 4e-05 | same gene group |
| [[CDON]] | +0.49 | +0.45 / +0.46 | both halves | 3e-05 | same gene group |
| [[LINC01605]] | +0.48 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[SIRLNT]] | +0.48 | +0.51 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STXBP5]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[LINC00607]] | -0.48 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[HECTD1]] | -0.46 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[STXBP5-AS1]] | -0.46 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[HSD11B1]] | -0.45 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[B3GNT5]] | -0.45 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[ITGA10]] | -0.45 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[ADPRHL1]] | -0.43 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[TRABD2B]] | -0.43 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[IL1RL1]] | -0.43 | -0.39 / -0.37 | both halves | 8e-05 | same gene group; pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[DAAM2]] | -0.42 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[FKBP5]] | -0.42 | -0.48 / -0.30 | both halves | 2e-04 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 21, C 0. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNS1]] | B | TNS1 activity raises LRIG1's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.90× lower at baseline in the lines without TNS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[LINC01411]] | B | LINC01411 activity raises LRIG1's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 3.01× lower at baseline in the lines without LINC01411 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032 |
| [[GDNF]] | B | GDNF activity raises LRIG1's level | lines that do not express GDNF (38) vs lines expressing it (12) | 2.76× lower at baseline in the lines without GDNF | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[SYNDIG1]] | B | SYNDIG1 activity raises LRIG1's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 2.50× lower at baseline in the lines without SYNDIG1 | 0.013 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1 |
| [[TMEM200A]] | B | TMEM200A activity raises LRIG1's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 2.73× lower at baseline in the lines without TMEM200A | 0.014 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615 |
| [[LINC01605]] | B | LINC01605 activity raises LRIG1's level | lines that do not express LINC01605 (27) vs lines expressing it (23) | 2.33× lower at baseline in the lines without LINC01605 | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC00460, LINC01133, PTPRR |
| [[ADAMTS9]] | B | ADAMTS9 activity raises LRIG1's level | lines that do not express ADAMTS9 (18) vs lines expressing it (32) | 2.39× lower at baseline in the lines without ADAMTS9 | 0.021 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2 |
| [[BDKRB2]] | B | BDKRB2 activity raises LRIG1's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 3.02× lower at baseline in the lines without BDKRB2 | 0.023 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[BAALC]] | B | BAALC activity raises LRIG1's level | lines that do not express BAALC (32) vs lines expressing it (18) | 1.86× lower at baseline in the lines without BAALC | 0.029 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers LRIG1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[ADGRG1]] | B | ADGRG1 activity raises LRIG1's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 2.63× lower at baseline in the lines without ADGRG1 | 0.039 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[HSD11B1]] | B | HSD11B1 activity raises LRIG1's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 1.75× lower at baseline in the lines without HSD11B1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTS9]] | B | LRIG1 activity raises ADAMTS9's level | lines that do not express LRIG1 (11) vs lines expressing it (39) | 3.52× lower at baseline in the lines without LRIG1 | 0.029 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TMEM200A]] | B | LRIG1 activity raises TMEM200A's level | lines that do not express LRIG1 (11) vs lines expressing it (39) | 3.16× lower at baseline in the lines without LRIG1 | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TNS1]] | B | LRIG1 activity raises TNS1's level | lines that do not express LRIG1 (11) vs lines expressing it (39) | 3.95× lower at baseline in the lines without LRIG1 | 0.045 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ATP8B1]] | B | LRIG1 activity raises ATP8B1's level | lines that do not express LRIG1 (11) vs lines expressing it (39) | 2.45× lower at baseline in the lines without LRIG1 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HSD11B1]] | B | LRIG1 activity raises HSD11B1's level | lines that do not express LRIG1 (11) vs lines expressing it (39) | 1.80× lower at baseline in the lines without LRIG1 | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NR3C2]] | B | LRIG1 activity raises NR3C2's level | lines that do not express LRIG1 (11) vs lines expressing it (39) | 2.36× lower at baseline in the lines without LRIG1 | 0.084 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GPR68]] | B | LRIG1 activity raises GPR68's level | lines that do not express LRIG1 (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without LRIG1 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.391). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.9, -3.7); signed map (-4.3, 29.1). **Vector** length 107, 28.2% of its response variance represented; |z| ≥ 3 in 1,003 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | -8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | -7.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.9 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.7 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | -0.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.9 | +0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | -1.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -4.1 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.0 | -0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.9 | -1.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.9 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -3.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeats and immunoglobulin like domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.1 — chr3:66,378,797-66,501,263 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LIG-1, DKFZP586O1624, LIG1 |
| Gene groups (HGNC) | I-set domain containing |
| Hallmark sets | IL2_STAT5_SIGNALING, ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: Negative regulation of MET activity; Signaling by EGFR; Signaling by MET |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JA1](https://www.uniprot.org/uniprotkb/Q96JA1) (Leucine-rich repeats and immunoglobulin-like domains protein 1):

> Acts as a feedback negative regulator of signaling by receptor tyrosine kinases, through a mechanism that involves enhancement of receptor ubiquitination and accelerated intracellular degradation.

**Summary**, from NCBI Gene [26018](https://www.ncbi.nlm.nih.gov/gene/26018):

> Predicted to enable signaling receptor activity. Predicted to be involved in sensory perception of sound. Predicted to act upstream of or within hair cycle process; innervation; and otolith morphogenesis. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17360](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17360) · Entrez [26018](https://www.ncbi.nlm.nih.gov/gene/26018) · UniProt [Q96JA1](https://www.uniprot.org/uniprotkb/Q96JA1) · Ensembl [ENSG00000144749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144749)

## Data

Gene col 6926: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6926); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6926, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6926]; `tensor/DDL_lfc|DDL_z.npy` [6926]; `embed/gene_vectors.npy` [6926]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6926 or target_col == 6926). Every well: [[LRIG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRIG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
