---
symbol: "NFATC2IP"
type: "gene"
col: 10772
ensembl_id: "ENSG00000176953"
name: "nuclear factor of activated T cells 2 interacting protein"
location: "16p11.2"
module: 28
arm: "-"
pooled_cpm: 65.37
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# NFATC2IP

*nuclear factor of activated T cells 2 interacting protein* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.95× (z +11.4, q 3e-27, up in 43 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.29× (z +4.4, q 9e-04, up in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LoVo 3.53×, RKO 2.62×, PANC-1 1.95×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 3.09×, SK-MEL-2 2.89×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 2.07×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.454× (z -18.9, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIN52]] (+0.63, fdr 1e-05), [[TPTEP2-CSNK1E]] (+0.60, fdr 1e-05), [[PITPNA]] (+0.59, fdr 1e-05); moves opposite to [[CLCN3]] (-0.60, fdr 1e-05), [[CDC73]] (-0.58, fdr 2e-04), [[PABIR1]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10772.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LoVo 3.53×, RKO 2.62×, PANC-1 1.95×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 3.09×, SK-MEL-2 2.89×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 2.07×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.95×** | +11.4 | 3e-27 | 43/49 (LoVo, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.67×** | +8.4 | 2e-14 | 33/43 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.47×** | +6.5 | 1e-08 | 40/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.47×** | +6.0 | 2e-07 | 28/45 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.23×** | +5.1 | 4e-05 | 24/48 (PANC-1, SW 900, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.34×** | +5.0 | 6e-05 | 34/48 (PANC-1, SW480, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.4 | 9e-04 | 25/48 (HS-578T, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.26×** | +4.0 | 0.005 | 26/48 (SW480, HS-578T, …) | two highest doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **1.26×** | +3.9 | 0.007 | 24/47 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.8 | 0.007 | 18/48 (BT-474, SW1417, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.25×** | +3.7 | 0.013 | 20/49 (SNU-423, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.23×** | +3.4 | 0.028 | 21/48 (SW 900, HS-578T, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | 1.20× | +3.1 | 0.083 | 18/48 (HCT15, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.083 | 18/48 (CFPAC-1, SHP-77, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.32× | +3.0 | 0.10 | 10/48 (COLO 205, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10772.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.454×** | -18.9 | 0e+00 | 45/48 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.565×** | -9.7 | 1e-19 | 35/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.722×** | -7.8 | 1e-12 | 37/48 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.472×** | -6.6 | 4e-09 | 39/49 (LoVo, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.478×** | -6.5 | 8e-09 | 41/48 (SNU-423, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.677×** | -6.3 | 2e-08 | 35/48 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.707×** | -5.9 | 4e-07 | 40/48 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -5.2 | 1e-05 | 4/49 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.845× | -3.9 | 0.007 | 22/48 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 0.862× | -3.5 | 0.024 | 14/48 (hTERT-HPNE, SNU-1, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.814×** | -3.5 | 0.029 | 17/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.879× | -3.0 | 0.11 | 20/48 (A-427, SNU-1, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10772. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 56.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -16.3) |
| [[NCI-H460 (line)]] | wt | 54.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -20.5) |
| [[PANC-1 (line)]] | alt | 68.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.95× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -13.3) |
| [[RKO (line)]] | wt | 81.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -12.9) |
| [[A-172 (line)]] | wt | 86.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -14.2) |
| [[A-427 (line)]] | wt | 118 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -26.8) |
| [[A549 (line)]] | wt | 53.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -15.7) |
| [[HEC-1-A (line)]] | alt | 71.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -15.0) |
| [[MIA PaCa-2 (line)]] | alt | 93.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -16.2) |
| [[NCI-H1573 (line)]] | alt | 58.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 64.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 106 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -15.2) |
| [[SK-MEL-2 (line)]] | alt | 64.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -9.6) |
| [[A498 (line)]] | wt | 71.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.551× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 175 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -16.3) |
| [[CFPAC-1 (line)]] | alt | 45.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -12.9) |
| [[COLO 205 (line)]] | alt | 48.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.0) |
| [[HCT15 (line)]] | alt | 68.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -12.7) |
| [[HOP62 (line)]] | alt | 44.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -9.7) |
| [[Hs 766T (line)]] | wt | 85.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -8.7) |
| [[HS-578T (line)]] | alt | 37.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 48.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.2) |
| [[KATO III (line)]] | alt | 74.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -12.3) |
| [[LS 180 (line)]] | wt | 55.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 55.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -17.6) |
| [[Panc 03.27 (line)]] | alt | 45.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -12.3) |
| [[SNU-1 (line)]] | wt | 58.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -8.5) |
| [[SNU-423 (line)]] | alt | 52.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -9.9) |
| [[SW 900 (line)]] | alt | 43.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -9.2) |
| [[SW48 (line)]] | wt | 60.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -10.4) |
| [[SW480 (line)]] | alt | 59.9 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.07× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[AN3 CA (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 102 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10772), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN52]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[PITPNA]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ASB16-AS1]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[SFI1]] | +0.58 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[SLC38A9]] | +0.58 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[CBFB]] | +0.58 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[NFATC2IP-AS1]] | +0.57 | +0.67 / +0.43 | both halves | 3e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[STARD3]] | +0.57 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[ARPC5L]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ZMYND19]] | +0.55 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[MROH1]] | +0.55 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[GATD1-DT]] | +0.55 | +0.42 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLCN3]] | -0.60 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[CDC73]] | -0.58 | -0.31 / -0.57 | both halves | 2e-04 | same gene group |
| [[PABIR1]] | -0.57 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[RBM7]] | -0.57 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[ECH1]] | -0.57 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[KBTBD7]] | -0.56 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[TTC5]] | -0.56 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[COMMD8]] | -0.56 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[DUSP19]] | -0.56 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[MSRB2]] | -0.56 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[NUDT12]] | -0.55 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[FANCF]] | -0.54 | -0.54 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NFATC2IP's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAPK14]] | B | MAPK14 activity raises NFATC2IP's level | compounds that target MAPK14: 2 of 2 lower it (PH-797804, Ralimetinib dimesylate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SYTL2]] | B | SYTL2 activity lowers NFATC2IP's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 1.54× higher at baseline in the lines without SYTL2 | 0.087 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **-** arm (projection on the module's main direction -0.514). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.0, 1.0); signed map (-45.4, 0.8). **Vector** length 110, 32.2% of its response variance represented; |z| ≥ 3 in 894 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +7.0 | +5.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +6.5 | +6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | +2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.9 | +4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +5.0 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.3 | +0.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.1 | +1.2 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +2.0 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.4 | -18.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.4 | -9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -7.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.0 | -5.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -6.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.9 | -2.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | nuclear factor of activated T cells 2 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:28,950,807-28,967,092 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14639, NIP45, RAD60, ESC2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCF5](https://www.uniprot.org/uniprotkb/Q8NCF5) (NFATC2-interacting protein):

> In T-helper 2 (Th2) cells, regulates the magnitude of NFAT-driven transcription of a specific subset of cytokine genes, including IL3, IL4, IL5 and IL13, but not IL2. Recruits PRMT1 to the IL4 promoter; this leads to enhancement of histone H4 'Arg-3'-methylation and facilitates subsequent histone acetylation at the IL4 locus, thus promotes robust cytokine expression (By similarity). Down-regulates formation of poly-SUMO chains by UBE2I/UBC9 (By similarity).

**Summary**, from NCBI Gene [84901](https://www.ncbi.nlm.nih.gov/gene/84901):

> Predicted to be involved in positive regulation of transcription by RNA polymerase II. Predicted to be located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25906](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25906) · Entrez [84901](https://www.ncbi.nlm.nih.gov/gene/84901) · UniProt [Q8NCF5](https://www.uniprot.org/uniprotkb/Q8NCF5) · Ensembl [ENSG00000176953](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176953)

## Data

Gene col 10772: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10772); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10772, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10772]; `tensor/DDL_lfc|DDL_z.npy` [10772]; `embed/gene_vectors.npy` [10772]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10772 or target_col == 10772). Every well: [[NFATC2IP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFATC2IP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
