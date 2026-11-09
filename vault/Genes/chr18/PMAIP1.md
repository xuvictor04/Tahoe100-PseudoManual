---
symbol: "PMAIP1"
type: "gene"
col: 6565
ensembl_id: "ENSG00000141682"
name: "phorbol-12-myristate-13-acetate-induced protein 1"
location: "18q21.32"
module: 68
arm: "+"
pooled_cpm: 81.65
n_lines_expressing: 46
n_dd_up: 38
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 18
direction_downstream: 12
tags: ["gene", "module/068", "written"]
generated_by: "tahoemap"
---

# PMAIP1

*phorbol-12-myristate-13-acetate-induced protein 1* — 18q21.32

> [!summary] In one line
> PMAIP1 encodes NOXA, the BH3-only protein p53 induces to neutralise MCL1 and so lower the threshold for mitochondrial apoptosis.

## What it is

NOXA is a very small BH3-only protein — a BH3 motif and a C-terminal mitochondrial-targeting segment, little else. In the BCL2 family's division of labour it is a *sensitiser*: it does not itself permeabilise the outer mitochondrial membrane, but occupies prosurvival relatives so that the direct activators can. Its defining property is selectivity. Unlike PUMA ([[BBC3]]), which engages the whole prosurvival set, NOXA binds MCL1 and A1/BFL1 and essentially ignores BCL2 and BCL-XL. Binding MCL1 also accelerates MCL1's proteasomal degradation, so NOXA removes its target rather than merely sequestering it. With MCL1 depleted, BAK and [[BAX]] are free to oligomerise, the membrane permeabilises, and the apoptosome commits the cell.

PMAIP1 is a direct p53 target with a p53 response element; mouse work combining Noxa and Puma loss showed the two together account for much of p53-dependent apoptosis, with PUMA generally the more consequential. But NOXA is not a p53-exclusive gene, and that matters more for NOXA than for most p53 targets. It is strongly induced by proteasome inhibition, by ER stress through the ATF4 ([[ATF4]]) arm of the integrated stress response, by E2F1 and deregulated MYC, and under hypoxia. The protein is short-lived and proteasome-degraded, so steady-state NOXA reflects turnover as much as transcription. Clinically the NOXA-to-MCL1 balance helps determine whether a cell depends on BCL2 or on MCL1 for survival — MCL1 dependence is a principal route to venetoclax resistance, and bortezomib's cytotoxicity runs substantially through NOXA induction.

## What is uncertain

The largest problem is structural rather than biological. A transcriptome measured at 24 h in cells still present is a survivorship-filtered sample: cells that acted on a NOXA induction are gone, so what is measured is NOXA in the survivors, and its relation to the apoptotic response actually mounted is not simple. Second, NOXA's p53-independent inducers are strong and this screen contains compounds that hit several of them — proteasome inhibitors, CDK and transcription inhibitors, ER stressors — so NOXA induction under drug exposure is weak evidence of p53 engagement on its own. Third, this is a case where mRNA is a poor proxy for function: what decides outcome is NOXA protein against MCL1 protein at the mitochondrion, and both are short-lived. Fourth, the mouse genetics do not transfer cleanly — the relative weight of Noxa and Puma differs by cell type.

## References

- Oda et al., 2000, Science — identified Noxa as a BH3-only p53 target and candidate mediator of p53-induced apoptosis.
- Villunger et al., 2003, Science — Puma and Noxa together mediate much of the p53- and drug-induced apoptotic response in mouse cells.
- Chen et al., 2005, Molecular Cell — Noxa selectively targets Mcl-1 while Puma engages all prosurvival relatives, giving the BH3-only proteins complementary function.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.83× (z +29.2, q 0e+00, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 0.05 µM: 0.786× (z -4.4, q 0.007, down in 24 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.409×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLFN5]] (+0.65, fdr 1e-05), [[ISG20]] (+0.64, fdr 7e-06), [[LPXN]] (+0.61, fdr 2e-05); moves opposite to [[WDR5]] (-0.57, fdr 1e-05), [[MMS19]] (-0.57, fdr 2e-05), [[PHKA2]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[SLIT2]] → it (grade B ⚠); 12 go from it, the strongest it → [[JUN]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6565.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.83×** | +29.2 | 0e+00 | 42/44 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.14×** | +20.6 | 0e+00 | 43/44 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.90×** | +17.8 | 0e+00 | 43/44 (C32, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.25×** | +15.4 | 0e+00 | 39/44 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +11.1 | 1e-26 | 40/44 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +11.0 | 2e-26 | 32/45 (A549, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.24×** | +10.6 | 3e-24 | 38/44 (NCI-H460, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.07×** | +9.5 | 1e-19 | 39/44 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.06×** | +9.5 | 2e-19 | 35/44 (SW480, SNU-423, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **2.06×** | +9.1 | 5e-18 | 40/44 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.74×** | +7.2 | 2e-11 | 27/44 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +6.8 | 4e-10 | 31/44 (CFPAC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.62×** | +6.3 | 1e-08 | 36/44 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.57×** | +5.4 | 2e-06 | 29/40 (NCI-H460, J82, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.49×** | +5.2 | 6e-06 | 25/44 (J82, NCI-H1573, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +5.1 | 9e-06 | 27/44 (A-427, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +5.0 | 2e-05 | 25/44 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.46×** | +4.9 | 2e-05 | 28/44 (HEC-1-A, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.7 | 9e-05 | 24/44 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 2e-04 | 24/44 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +4.3 | 4e-04 | 24/44 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.006 | 22/45 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.006 | 23/44 (AsPC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6565.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.409×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | **0.786×** | -4.4 | 0.007 | 24/44 (C32, NCI-H23, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.762×** | -3.6 | 0.096 | 22/44 (CHP-212, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.781× | -3.3 | 0.15 | 19/44 (A-172, HS-578T, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.787× | -3.2 | 0.15 | 21/44 (HOP62, NCI-H460, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | 0.633× | -3.2 | 0.15 | 17/43 (H4, A549, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.782× | -3.1 | 0.15 | 17/44 (C32, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.790× | -3.1 | 0.15 | 18/44 (HS-578T, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6565. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 90.5 | 15 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.48× (z +24.2) | — |
| [[NCI-H460 (line)]] | wt | 193 | 14 (8 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 11.7× (z +17.1) | — |
| [[HEC-1-A (line)]] | alt | 40.7 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +19.5) | — |
| [[LoVo (line)]] | wt | 98.1 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +22.9) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 109 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.43× (z +19.3) | — |
| [[NCI-H1573 (line)]] | alt | 62.0 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +15.9) | — |
| [[BT-474 (line)]] | alt | 39.6 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +18.5) | — |
| [[C32 (line)]] | wt | 70.3 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +24.5) | — |
| [[CFPAC-1 (line)]] | alt | 83.3 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.77× (z +27.1) | — |
| [[HOP62 (line)]] | alt | 87.7 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.48× (z +23.9) | — |
| [[Hs 766T (line)]] | wt | 151 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.93× (z +17.3) | — |
| [[hTERT-HPNE (line)]] | wt | 219 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.43× (z +21.5) | — |
| [[NCI-H2347 (line)]] | alt | 159 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +18.5) | — |
| [[SW 900 (line)]] | alt | 101 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +14.3) | — |
| [[A549 (line)]] | wt | 43.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +18.4) | — |
| [[NCI-H1792 (line)]] | alt | 107 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.15× (z +25.0) | — |
| [[NCI-H2030 (line)]] | alt | 40.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.90× (z +17.4) | — |
| [[SNU-423 (line)]] | alt | 74.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +21.8) | — |
| [[A498 (line)]] | wt | 108 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +19.9) | — |
| [[AsPC-1 (line)]] | alt | 42.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +23.4) | — |
| [[LOX-IMVI (line)]] | wt | 107 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +12.1) | — |
| [[PANC-1 (line)]] | alt | 30.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.67× (z +25.2) | — |
| [[SK-MEL-2 (line)]] | alt | 43.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +14.5) | — |
| [[SW48 (line)]] | wt | 55.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +13.7) | — |
| [[HS-578T (line)]] | alt | 70.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +13.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 27.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.82× (z +17.1) | — |
| [[Panc 03.27 (line)]] | alt | 125 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +21.8) | — |
| [[RKO (line)]] | wt | 47.0 | 3 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.42× (z +11.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +11.0) | — |
| [[RPMI-7951 (line)]] | alt | 61.5 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 8.00× (z +11.9) | — |
| [[SW1417 (line)]] | alt | 136 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.8) | — |
| [[HT-29 (line)]] | alt | 56.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +11.2) | — |
| [[A-427 (line)]] | wt | 28.3 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.99× (z +9.2) ⚠ toxic | — |
| [[COLO 205 (line)]] | alt | 70.8 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 5.22× (z +9.2) | — |
| [[KATO III (line)]] | alt | 33.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.22× (z +11.0) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 34.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +10.5) | — |
| [[SW480 (line)]] | alt | 60.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.15× (z +13.5) | — |
| [[A-172 (line)]] | wt | 92.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 86.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 272 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 121 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6565), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLFN5]] | +0.65 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ISG20]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS |
| [[LPXN]] | +0.61 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[C21orf91]] | +0.61 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[HCP5]] | +0.60 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[LINC00944]] | +0.58 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[PLA2G4C]] | +0.57 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[ZBTB21]] | +0.57 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[LACC1]] | +0.56 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[CTSS]] | +0.56 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[ATF3]] | +0.56 | +0.55 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS; STRING 579 |
| [[LINC00705]] | +0.56 | +0.31 / +0.45 | both halves | 2e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR5]] | -0.57 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[MMS19]] | -0.57 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[PHKA2]] | -0.56 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[SLC9A6]] | -0.53 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[ZDHHC8]] | -0.51 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[BRF1]] | -0.51 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[ANKRD27]] | -0.50 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[ELP1]] | -0.50 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[RPA1]] | -0.50 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[MTMR12]] | -0.49 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[VPS26B]] | -0.49 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[TAF5L]] | -0.49 | -0.43 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 17, C 1. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLIT2]] | B | SLIT2 activity raises PMAIP1's level | lines that do not express SLIT2 (20) vs lines expressing it (30) | 1.97× lower at baseline in the lines without SLIT2 | 7e-04 | ⚠ within organs, on part of the lines; also absent: CHSY3, MOXD1, IDO1 |
| [[DUSP10]] | B | DUSP10 activity raises PMAIP1's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 2.37× lower at baseline in the lines without DUSP10 | 0.003 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[TLE4]] | B | TLE4 activity raises PMAIP1's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 2.62× lower at baseline in the lines without TLE4 | 0.010 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |
| [[IL7R]] | B | IL7R activity raises PMAIP1's level | lines that do not express IL7R (30) vs lines expressing it (20) | 2.05× lower at baseline in the lines without IL7R | 0.010 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1 |
| [[KITLG]] | B | KITLG activity raises PMAIP1's level | lines that do not express KITLG (10) vs lines expressing it (40) | 2.53× lower at baseline in the lines without KITLG | 0.013 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[PLSCR2]] | B | PLSCR2 activity raises PMAIP1's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 2.83× lower at baseline in the lines without PLSCR2 | 0.023 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |
| [[LINC00944]] | B | LINC00944 activity raises PMAIP1's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 1.86× lower at baseline in the lines without LINC00944 | 0.031 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |
| [[TOP2A]] | B | TOP2A activity lowers PMAIP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CXCL1]] | B | CXCL1 activity raises PMAIP1's level | lines that do not express CXCL1 (17) vs lines expressing it (33) | 1.75× lower at baseline in the lines without CXCL1 | 0.054 | ⚠ within organs, on part of the lines; also absent: CCL20, CDCP1, C15orf48 |
| [[CDC42EP3]] | B | CDC42EP3 activity raises PMAIP1's level | lines that do not express CDC42EP3 (8) vs lines expressing it (42) | 2.95× lower at baseline in the lines without CDC42EP3 | 0.057 | ⚠ within organs, on part of the lines; also absent: CCDC110, C3orf52, KLF12 |
| [[RND3]] | B | RND3 activity raises PMAIP1's level | lines that do not express RND3 (5) vs lines expressing it (45) | 3.32× lower at baseline in the lines without RND3 | 0.060 | ⚠ within organs, on part of the lines; also absent: GULP1, SFXN3, GALNT7; its own permutation p |
| [[SAMD9]] | B | SAMD9 activity raises PMAIP1's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.01× lower at baseline in the lines without SAMD9 | 0.067 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JUN]] | C | PMAIP1 activity weakens JUN's drug response | lines that do not express PMAIP1 (4) vs lines expressing it (45) | the lines without PMAIP1 respond 0.89× as strongly (z diff -2.27); strongest at Harringtonine 5 µM: 7.71x vs 11x (z diff -3.7) | 5e-04 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent; target measured in part of the lines; rests on the correction; artifact flags |
| [[ISG20]] | C | PMAIP1 activity raises ISG20's level | lines that do not express PMAIP1 (4) vs lines expressing it (46) | 3.48× lower at baseline in the lines without PMAIP1 | 0.010 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent; co-absent with the target |
| [[CDKN1A]] | C | PMAIP1 activity raises CDKN1A's level | lines that do not express PMAIP1 (4) vs lines expressing it (46) | 3.78× lower at baseline in the lines without PMAIP1 | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent |
| [[LACC1]] | C | PMAIP1 activity raises LACC1's level | lines that do not express PMAIP1 (4) vs lines expressing it (46) | 3.33× lower at baseline in the lines without PMAIP1 | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent |
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM | C | PMAIP1 activity raises the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (protects the cells) | lines that do not express PMAIP1 (4) vs lines expressing it (44) | the lines without PMAIP1: 0.77× the cells of the other lines | 0.022 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent |
| [[SLIT2]] | C | PMAIP1 activity strengthens SLIT2's drug response | lines that do not express PMAIP1 (3) vs lines expressing it (27) | the lines without PMAIP1 respond the other way (z diff +4.65); strongest at Idarubicin (hydrochloride) 5 µM: 0.98x vs 5.05x (z diff +8.3) | 0.025 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |
| cells under [[Pemigatinib (drug)]] 5 µM | C | PMAIP1 activity raises the cells' numbers under Pemigatinib 5 µM (protects the cells) | lines that do not express PMAIP1 (4) vs lines expressing it (44) | the lines without PMAIP1: 0.72× the cells of the other lines | 0.033 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent |
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | PMAIP1 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express PMAIP1 (4) vs lines expressing it (44) | the lines without PMAIP1: 0.76× the cells of the other lines | 0.036 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent |
| cells under [[olaparib (drug)]] 5 µM | C | PMAIP1 activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express PMAIP1 (4) vs lines expressing it (44) | the lines without PMAIP1: 1.54× the cells of the other lines | 0.036 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent |
| cells under [[Irinotecan (drug)]] 0.5 µM | C | PMAIP1 activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express PMAIP1 (4) vs lines expressing it (44) | the lines without PMAIP1: 0.73× the cells of the other lines | 0.059 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent |
| cells under [[Methylprednisolone succinate (drug)]] 0.5 µM | C | PMAIP1 activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express PMAIP1 (4) vs lines expressing it (44) | the lines without PMAIP1: 1.41× the cells of the other lines | 0.079 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent |
| [[SLIT2]] | C | PMAIP1 activity lowers SLIT2's level | lines that do not express PMAIP1 (4) vs lines expressing it (46) | 6.52× higher at baseline in the lines without PMAIP1 | 0.094 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.529). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (18.2, 10.1); signed map (25.9, 4.1). **Vector** length 112, 37.0% of its response variance represented; |z| ≥ 3 in 1,322 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.7 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.3 | +3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +15.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +5.3 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +9.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.6 | +4.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.2 | +3.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -0.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.4 | -3.6 |
|  | [[NG25 (drug)]] 5 µM |  | -4.4 | -3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -0.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.6 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.1 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.1 | -1.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.0 | -2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | phorbol-12-myristate-13-acetate-induced protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.32 — chr18:59,899,996-59,904,305 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APR, NOXA |
| Gene groups (HGNC) | BCL2 homology region 3 (BH3) only |
| Hallmark sets | APOPTOSIS, ESTROGEN_RESPONSE_EARLY |
| Reactome | 9 pathways, smallest: Activation of NOXA and translocation to mitochondria; BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members; TP53 Regulates Transcription of Genes Involved in Cytochrome C Release |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13794](https://www.uniprot.org/uniprotkb/Q13794) (Phorbol-12-myristate-13-acetate-induced protein 1):

> Promotes activation of caspases and apoptosis. Promotes mitochondrial membrane changes and efflux of apoptogenic proteins from the mitochondria. Contributes to p53/TP53-dependent apoptosis after radiation exposure. Promotes proteasomal degradation of MCL1. Competes with BAK1 for binding to MCL1 and can displace BAK1 from its binding site on MCL1 (By similarity). Competes with BIM/BCL2L11 for binding to MCL1 and can displace BIM/BCL2L11 from its binding site on MCL1.

**Summary**, from NCBI Gene [5366](https://www.ncbi.nlm.nih.gov/gene/5366):

> This gene belongs to a pro-apoptotic subfamily within the BCL-2 protein family, referred to as the BCL-2 homology domain 3 (BH3)-only subfamily, which determine whether a cell commits to apoptosis. In response to death-inducing stimuli, BH3-only members inhibit the anti-apoptotic BCL-2 family members, which under steady-state conditions keep the multi-BH domain proteins BAX and BAK, in an inactive state. [provided by RefSeq, Aug 2020]

**Accessions** — [HGNC:9108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9108) · Entrez [5366](https://www.ncbi.nlm.nih.gov/gene/5366) · UniProt [Q13794](https://www.uniprot.org/uniprotkb/Q13794) · Ensembl [ENSG00000141682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141682)

## Data

Gene col 6565: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6565); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6565, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6565]; `tensor/DDL_lfc|DDL_z.npy` [6565]; `embed/gene_vectors.npy` [6565]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6565 or target_col == 6565). Every well: [[PMAIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/PMAIP1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
