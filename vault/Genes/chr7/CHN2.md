---
symbol: "CHN2"
type: "gene"
col: 2716
ensembl_id: "ENSG00000106069"
name: "chimerin 2"
location: "7p14.3"
module: 8
arm: "+"
pooled_cpm: 36.76
n_lines_expressing: 30
n_dd_up: 21
n_dd_down: 22
n_dd_up_clean: 16
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 36
direction_downstream: 34
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# CHN2

*chimerin 2* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.91× (z +13.9, q 5e-41, up in 17 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.591× (z -8.0, q 7e-13, down in 20 of 28 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.618× (z -7.3, q 5e-11, down in 20 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF43]] (+0.67, fdr 7e-06), [[POF1B]] (+0.65, fdr 1e-05), [[LINC02253]] (+0.64, fdr 1e-05); moves opposite to [[ITGB1BP1]] (-0.55, fdr 1e-05), [[SERPINB6]] (-0.50, fdr 3e-05), [[CCM2]] (-0.50, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 36 arrows point to it, the strongest [[PELI2]] → it (grade B ⚠); 34 go from it, the strongest it → [[PELI2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2716.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +13.9 | 5e-41 | 17/28 (LS 180, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.73×** | +11.8 | 1e-29 | 24/28 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +8.1 | 1e-13 | 15/26 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +7.2 | 8e-11 | 2/22 (NCI-H23, C32) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +5.2 | 2e-05 | 13/27 (J82, H4, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +4.9 | 8e-05 | 15/28 (J82, RKO, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.9 | 9e-05 | 5/28 (J82, HT-29, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.36×** | +4.7 | 2e-04 | 19/27 (RKO, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 7e-04 | 14/27 (SW 900, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +4.3 | 0.001 | 11/27 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.47×** | +4.2 | 0.002 | 1/25 (H4) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.003 | 11/29 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.008 | 9/28 (LoVo, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.013 | 4/28 (J82, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.014 | 6/27 (H4, LOX-IMVI, …) | top dose only |  |
| [[Penfluridol (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.043 | 3/27 (J82, LOX-IMVI, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.15× | +3.1 | 0.063 | 3/28 (KATO III, SW480, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.075 | 5/27 (SW1417, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2716.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.591×** | -8.0 | 7e-13 | 20/28 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.598×** | -7.8 | 2e-12 | 21/27 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.618×** | -7.3 | 5e-11 | 20/27 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.759×** | -5.9 | 4e-07 | 19/28 (SW 900, Panc 03.27, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.691×** | -5.6 | 2e-06 | 16/26 (Panc 03.27, SW 900, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.703×** | -5.1 | 3e-05 | 15/27 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.538×** | -4.9 | 6e-05 | 17/29 (LoVo, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.714×** | -4.9 | 6e-05 | 13/28 (Panc 03.27, HT-29, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.744×** | -4.5 | 4e-04 | 12/27 (SW480, KATO III, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.755×** | -4.3 | 0.001 | 14/27 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.756×** | -4.2 | 0.001 | 16/27 (H4, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.763×** | -4.1 | 0.002 | 20/27 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.765×** | -4.1 | 0.002 | 17/27 (Panc 03.27, H4, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.767×** | -4.0 | 0.002 | 15/27 (SW 900, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.770×** | -4.0 | 0.003 | 18/27 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.781×** | -3.5 | 0.012 | 16/27 (COLO 205, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.864× | -3.1 | 0.047 | 14/28 (HEC-1-A, COLO 205, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.678×** | -3.1 | 0.053 | 12/27 (LoVo, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fulvestrant (drug)]] 0.05 µM |  | **0.817×** | -3.1 | 0.054 | 2/27 (RKO, J82) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2716. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 84.9 | 0 | 30 (15 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0868× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.123× (z -15.2) |
| [[KATO III (line)]] | alt | 243 | 0 | 14 (13 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -20.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.133× (z -19.4) |
| [[LoVo (line)]] | wt | 66.0 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -21.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.327× (z -11.4) |
| [[COLO 205 (line)]] | alt | 147 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -20.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.272× (z -11.2) |
| [[SW480 (line)]] | alt | 89.8 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.259× (z -12.1) |
| [[LS 180 (line)]] | wt | 36.1 | 2 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.62× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -11.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 29.9 | 1 (1 ⚠) | 4 (4 ⚠) | [[Selinexor (drug)]] 5 µM 5.08× (z +12.9) ⚠ cell-cycle shift, explains ~26% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.102× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[SHP-77 (line)]] | alt | 102 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.364× (z -8.6) |
| [[RKO (line)]] | wt | 28.8 | 1 (1 ⚠) | 3 (3 ⚠) | [[Selinexor (drug)]] 5 µM 3.51× (z +9.9) ⚠ cell-cycle shift, explains ~26% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0831× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 120 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -14.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 28.7 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 3.50× (z +10.1) ⚠ cell-cycle shift, explains ~26% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -10.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[H4 (line)]] | wt | 41.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 51.9 | 0 | 2 (1 ⚠) | — | [[Peretinoin (drug)]] 5 µM 0.254× (z -9.3) |
| [[SW 900 (line)]] | alt | 56.4 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0654× (z -10.1) ⚠ toxic · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.425× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 61.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 68.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 13.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LOX-IMVI (line)]] | wt | 13.8 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.48× (z +8.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW1417 (line)]] | alt | 64.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -9.1) ⚠ cell-cycle shift, explains ~9% of this change |
| [[A-172 (line)]] | wt | 7.63 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.40 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.71 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.19 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.50 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.99 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.24 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.78 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.88 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.36 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.85 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.40 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2716), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF43]] | +0.67 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[POF1B]] | +0.65 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[LINC02253]] | +0.64 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[TOX3]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ARHGEF38]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[AXIN2]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[DLEU1]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[ANK3]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[PROM1]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[EPS8L3]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[FRK]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 | same gene group |
| [[MIR4713HG]] | +0.59 | +0.50 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB1BP1]] | -0.55 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[SERPINB6]] | -0.50 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[CCM2]] | -0.50 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[RHCE]] | -0.49 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[SRR]] | -0.49 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[DNAAF9]] | -0.49 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[LINC02614]] | -0.48 | -0.40 / -0.48 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 17, C 19. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PELI2]] | B | PELI2 activity raises CHN2's level | lines that do not express PELI2 (16) vs lines expressing it (34) | 2.31× lower at baseline in the lines without PELI2 | 0.002 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28 |
| [[RASSF6]] | B | RASSF6 activity raises CHN2's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 3.76× lower at baseline in the lines without RASSF6 | 0.005 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[FRMD4B]] | B | FRMD4B activity raises CHN2's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 3.06× lower at baseline in the lines without FRMD4B | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[ARHGEF38]] | B | ARHGEF38 activity raises CHN2's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 3.78× lower at baseline in the lines without ARHGEF38 | 0.024 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[PPARGC1A]] | B | PPARGC1A activity raises CHN2's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 2.46× lower at baseline in the lines without PPARGC1A | 0.029 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[MANSC1]] | B | MANSC1 activity raises CHN2's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 3.12× lower at baseline in the lines without MANSC1 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[GCNT3]] | B | GCNT3 activity raises CHN2's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 4.05× lower at baseline in the lines without GCNT3 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[FAAH2]] | B | FAAH2 activity raises CHN2's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 3.24× lower at baseline in the lines without FAAH2 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[RAPGEF5]] | B | RAPGEF5 activity raises CHN2's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 3.00× lower at baseline in the lines without RAPGEF5 | 0.055 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[IGFL2-AS1]] | B | IGFL2-AS1 activity raises CHN2's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 3.00× lower at baseline in the lines without IGFL2-AS1 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises CHN2's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.08× lower at baseline in the lines without TMPRSS2 | 0.063 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[GDA]] | B | GDA activity raises CHN2's level | lines that do not express GDA (35) vs lines expressing it (15) | 3.39× lower at baseline in the lines without GDA | 0.067 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4 |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 18, C 16. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PELI2]] | B | CHN2 activity raises PELI2's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 3.49× lower at baseline in the lines without CHN2 | 0.002 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[CLDN10-AS1]] | B | CHN2 activity raises CLDN10-AS1's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 2.34× lower at baseline in the lines without CHN2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[MGST2]] | B | CHN2 activity strengthens MGST2's drug response | lines that do not express CHN2 (15) vs lines expressing it (23) | the lines without CHN2 respond 0.62× as strongly (z diff +2.10); strongest at Panobinostat 5 µM: 0.43x vs 0.22x (z diff +3.9) | 0.019 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15; target measured in part of the lines; artifact flags |
| [[RPH3AL]] | B | CHN2 activity raises RPH3AL's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 1.89× lower at baseline in the lines without CHN2 | 0.020 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[DLEU1]] | B | CHN2 activity raises DLEU1's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 3.09× lower at baseline in the lines without CHN2 | 0.020 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[RAPGEF5]] | B | CHN2 activity raises RAPGEF5's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 3.79× lower at baseline in the lines without CHN2 | 0.039 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[FRMD4B]] | B | CHN2 activity raises FRMD4B's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 2.29× lower at baseline in the lines without CHN2 | 0.049 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[GDA]] | B | CHN2 activity raises GDA's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 2.31× lower at baseline in the lines without CHN2 | 0.050 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[RASSF6]] | B | CHN2 activity raises RASSF6's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 2.59× lower at baseline in the lines without CHN2 | 0.056 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[TPD52L1]] | B | CHN2 activity raises TPD52L1's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 1.92× lower at baseline in the lines without CHN2 | 0.067 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[MGST2]] | B | CHN2 activity raises MGST2's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 2.12× lower at baseline in the lines without CHN2 | 0.068 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[MYRIP]] | B | CHN2 activity raises MYRIP's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 1.89× lower at baseline in the lines without CHN2 | 0.069 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.581). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.4, 49.8); signed map (58.1, 4.0). **Vector** length 91.0, 25.0% of its response variance represented; |z| ≥ 3 in 908 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +7.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.0 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | +0.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +4.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.3 | +1.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +3.6 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -4.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.0 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | -5.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -5.1 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.7 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.6 | -5.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.3 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | chimerin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:29,146,547-29,514,328 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARHGAP3, RhoGAP3 |
| Gene groups (HGNC) | Rho GTPase activating proteins; SH2 domain containing |
| Reactome | 4 pathways, smallest: RAC1 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [P52757](https://www.uniprot.org/uniprotkb/P52757) (Beta-chimaerin):

> GTPase-activating protein for p21-rac. Insufficient expression of beta-2 chimaerin is expected to lead to higher Rac activity and could therefore play a role in the progression from low-grade to high-grade tumors.

**Summary**, from NCBI Gene [1124](https://www.ncbi.nlm.nih.gov/gene/1124):

> This gene encodes a guanosine triphosphate (GTP)-metabolizing protein that contains a phorbol-ester/diacylglycerol (DAG)-type zinc finger, a Rho-GAP domain, and an SH2 domain. The encoded protein translocates from the cytosol to the Golgi apparatus membrane upon binding by diacylglycerol (DAG). Activity of this protein is important in cell proliferation and migration, and expression changes in this gene have been detected in cancers. A mutation in this gene has also been associated with …

**Accessions** — [HGNC:1944](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1944) · Entrez [1124](https://www.ncbi.nlm.nih.gov/gene/1124) · UniProt [P52757](https://www.uniprot.org/uniprotkb/P52757) · Ensembl [ENSG00000106069](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106069)

## Data

Gene col 2716: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2716); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2716, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2716]; `tensor/DDL_lfc|DDL_z.npy` [2716]; `embed/gene_vectors.npy` [2716]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2716 or target_col == 2716). Every well: [[CHN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
