---
symbol: "ABLIM1"
type: "gene"
col: 1782
ensembl_id: "ENSG00000099204"
name: "actin binding LIM protein 1"
location: "10q25.3"
module: 66
arm: "+"
pooled_cpm: 151.95
n_lines_expressing: 36
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 9
direction_downstream: 2
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# ABLIM1

*actin binding LIM protein 1* — 10q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.87× (z +13.8, q 2e-40, up in 28 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.55× (z +13.6, q 5e-40, up in 32 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.694× (z -11.4, q 2e-27, down in 25 of 35 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASEF]] (+0.63, fdr 7e-06), [[SEMA3C]] (+0.62, fdr 1e-05), [[SEMA3E]] (+0.59, fdr 2e-05); moves opposite to [[IL17RA]] (-0.62, fdr 1e-05), [[ZNF500]] (-0.59, fdr 2e-05), [[EIF4ENIF1]] (-0.58, fdr 2e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CD24]] → it (grade B ⚠); 2 go from it, the strongest it → [[STON2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1782.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +13.8 | 2e-40 | 28/35 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +13.7 | 2e-40 | 23/31 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +13.6 | 5e-40 | 32/34 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +10.6 | 6e-24 | 24/33 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +9.8 | 2e-20 | 27/35 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.24×** | +4.8 | 1e-04 | 19/34 (HepG2/C3A, PANC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.003 | 14/35 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.17× | +3.7 | 0.014 | 14/36 (NCI-H460, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.6 | 0.021 | 16/34 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +3.2 | 0.087 | 14/33 (KATO III, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.087 | 12/34 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.096 | 9/35 (NCI-H1792, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.096 | 9/34 (LoVo, A549, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.15× | +3.0 | 0.10 | 14/34 (PANC-1, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1782.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.694×** | -11.4 | 2e-27 | 25/35 (COLO 205, HT-29, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.765×** | -5.9 | 9e-07 | 21/34 (NCI-H23, HCT15, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.766×** | -5.6 | 5e-06 | 20/34 (HepG2/C3A, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.790×** | -5.2 | 3e-05 | 16/34 (LS 180, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.793×** | -5.1 | 3e-05 | 19/34 (SW480, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.794×** | -5.1 | 3e-05 | 22/34 (LS 180, A549, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.795×** | -5.1 | 3e-05 | 18/35 (CFPAC-1, RKO, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.672×** | -4.6 | 3e-04 | 18/34 (RKO, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.819×** | -4.2 | 0.001 | 17/34 (SW480, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.835× | -4.0 | 0.004 | 16/34 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.881× | -4.0 | 0.004 | 10/35 (A549, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.832×** | -3.9 | 0.004 | 15/34 (HT-29, SW480, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.844× | -3.7 | 0.008 | 17/34 (LS 180, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.893× | -3.6 | 0.015 | 7/34 (Hs 766T, NCI-H1573, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.857× | -3.4 | 0.025 | 15/34 (CHP-212, CFPAC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.811×** | -3.3 | 0.035 | 9/34 (LS 180, HCT15, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.866× | -3.2 | 0.045 | 14/34 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.872× | -3.0 | 0.074 | 11/34 (NCI-H23, LS 180, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.772×** | -3.0 | 0.079 | 13/34 (LoVo, SW480, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.875× | -3.0 | 0.083 | 10/34 (SW480, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1782. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 382 | 1 (1 ⚠) | 11 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +8.6) ⚠ cell-cycle shift, explains ~25% of this change | [[Clobetasol propionate (drug)]] 0.5 µM 0.318× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 306 | 8 (2 ⚠) | 2 (1 ⚠) | [[Binimetinib (drug)]] 5 µM 3.37× (z +12.9) | [[Selinexor (drug)]] 5 µM 0.496× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 227 | 6 (5 ⚠) | 1 | [[Digitoxin (drug)]] 0.5 µM 3.24× (z +12.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.86× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 182 | 3 (3 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 133 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +9.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -9.5) |
| [[SW480 (line)]] | alt | 218 | 1 (1 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.32× (z +9.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -14.0) |
| [[LS 180 (line)]] | wt | 407 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -12.7) |
| [[NCI-H2030 (line)]] | alt | 126 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -20.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 85.9 | 4 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.27× (z +12.9) | — |
| [[Panc 03.27 (line)]] | alt | 95.6 | 3 (2 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 2.21× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -9.2) |
| [[RKO (line)]] | wt | 100 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +12.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -11.3) |
| [[SNU-1 (line)]] | wt | 97.5 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.259× (z -10.8) ⚠ cell-cycle shift, explains ~5% of this change |
| [[CFPAC-1 (line)]] | alt | 108 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 2.32× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -8.8) |
| [[HCT15 (line)]] | alt | 228 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 86.3 | 0 | 3 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.352× (z -11.0) ⚠ cell-cycle shift, explains ~17% of this change |
| [[PANC-1 (line)]] | alt | 245 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 2.00× (z +8.9) | — |
| [[A498 (line)]] | wt | 153 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +9.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[AsPC-1 (line)]] | alt | 156 | 1 (1 ⚠) | 1 | [[Trametinib (drug)]] 5 µM 2.54× (z +9.2) ⚠ cell-cycle shift, explains ~12% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -11.4) |
| [[COLO 205 (line)]] | alt | 402 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -15.9) |
| [[HT-29 (line)]] | alt | 327 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -15.2) |
| [[KATO III (line)]] | alt | 300 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 1.87× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 127 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.15× (z +12.3) | — |
| [[SW1417 (line)]] | alt | 111 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.70× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -10.4) |
| [[SW48 (line)]] | wt | 110 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 2.73× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 211 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 42.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.45× (z +9.6) | — |
| [[LoVo (line)]] | wt | 259 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 43.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 126 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 122 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.82× (z +9.0) | — |
| [[A-172 (line)]] | wt | 26.2 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 24.7 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 91.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.4 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 20.7 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 33.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 17.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 28.7 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 163 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1782), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASEF]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[SEMA3C]] | +0.62 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SEMA3E]] | +0.59 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[AKR1B1]] | +0.58 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[YWHAZ]] | +0.57 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[FAT1]] | +0.57 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[COBL]] | +0.57 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[AHR]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SLC12A2]] | +0.56 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[ALCAM]] | +0.56 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[ARHGAP42]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[RFK]] | +0.54 | +0.40 / +0.54 | both halves | 5e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL17RA]] | -0.62 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[ZNF500]] | -0.59 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[EIF4ENIF1]] | -0.58 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[ZNF251]] | -0.56 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[BRPF1]] | -0.55 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[SCNM1]] | -0.54 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[C19orf25]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[BAHD1]] | -0.54 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[TPRN]] | -0.53 | -0.19 / -0.57 | ⚠ one half (not replicated) | 8e-04 |  |
| [[WDR53]] | -0.53 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[ZMYND19]] | -0.53 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[MEF2B]] | -0.52 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[CCNQ]] | -0.52 | -0.32 / -0.61 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD24]] | B | CD24 activity raises ABLIM1's level | lines that do not express CD24 (24) vs lines expressing it (26) | 3.27× lower at baseline in the lines without CD24 | 0.001 | ⚠ within organs, on part of the lines; also absent: FOXQ1, RNF223, SPNS2 |
| [[STON2]] | B | STON2 activity raises ABLIM1's level | lines that do not express STON2 (19) vs lines expressing it (31) | 2.37× lower at baseline in the lines without STON2 | 0.003 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[PLS1]] | B | PLS1 activity raises ABLIM1's level | lines that do not express PLS1 (14) vs lines expressing it (36) | 3.69× lower at baseline in the lines without PLS1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |
| [[ATP1B1]] | B | ATP1B1 activity raises ABLIM1's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 2.66× lower at baseline in the lines without ATP1B1 | 0.020 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[CDH17]] | B | CDH17 activity raises ABLIM1's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 3.75× lower at baseline in the lines without CDH17 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[AHR]] | B | AHR activity raises ABLIM1's level | lines that do not express AHR (7) vs lines expressing it (43) | 2.20× lower at baseline in the lines without AHR | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[MET]] | B | MET activity raises ABLIM1's level | lines that do not express MET (9) vs lines expressing it (41) | 2.49× lower at baseline in the lines without MET | 0.057 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[EHF]] | B | EHF activity raises ABLIM1's level | lines that do not express EHF (27) vs lines expressing it (23) | 2.55× lower at baseline in the lines without EHF | 0.093 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[ARAP2]] | B | ARAP2 activity raises ABLIM1's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 2.45× lower at baseline in the lines without ARAP2 | 0.095 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STON2]] | B | ABLIM1 activity raises STON2's level | lines that do not express ABLIM1 (14) vs lines expressing it (36) | 1.98× lower at baseline in the lines without ABLIM1 | 0.055 | ⚠ within organs, on part of the lines; also absent: EVPL, NUP62CL, CCDC68 |
| [[PRPSAP1]] | B | ABLIM1 activity lowers PRPSAP1's level | lines that do not express ABLIM1 (14) vs lines expressing it (36) | 1.28× higher at baseline in the lines without ABLIM1 | 0.086 | ⚠ within organs, on part of the lines; also absent: EVPL, NUP62CL, CCDC68 |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.0, 19.9); signed map (48.3, 19.0). **Vector** length 116, 29.9% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.7 | +13.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.1 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.9 | +10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.7 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +13.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.1 | +2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -11.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.5 | -5.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.1 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.0 | -4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.0 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | actin binding LIM protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.3 — chr10:114,431,112-114,768,061 (-) |
| Ensembl biotype | protein_coding |
| Also known as | abLIM, limatin; previously LIMAB1, ABLIM |
| Gene groups (HGNC) | LIM domain containing |
| Hallmark sets | MYOGENESIS, ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: DCC mediated attractive signaling; Netrin-1 signaling; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [O14639](https://www.uniprot.org/uniprotkb/O14639) (Actin-binding LIM protein 1):

> May act as scaffold protein (By similarity). May play a role in the development of the retina. Has been suggested to play a role in axon guidance.

**Summary**, from NCBI Gene [3983](https://www.ncbi.nlm.nih.gov/gene/3983):

> This gene encodes a LIM zinc-binding domain-containing protein that binds to actin filaments and mediates interactions between actin and cytoplasmic targets. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jun 2017]

**Accessions** — [HGNC:78](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:78) · Entrez [3983](https://www.ncbi.nlm.nih.gov/gene/3983) · UniProt [O14639](https://www.uniprot.org/uniprotkb/O14639) · Ensembl [ENSG00000099204](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099204)

## Data

Gene col 1782: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1782); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1782, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1782]; `tensor/DDL_lfc|DDL_z.npy` [1782]; `embed/gene_vectors.npy` [1782]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1782 or target_col == 1782). Every well: [[ABLIM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABLIM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
