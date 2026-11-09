---
symbol: "TMEM43"
type: "gene"
col: 10017
ensembl_id: "ENSG00000170876"
name: "transmembrane protein 43"
location: "3p25.1"
module: 54
arm: "-"
pooled_cpm: 35.71
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# TMEM43

*transmembrane protein 43* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.07× (z +13.1, q 1e-36, up in 37 of 46 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HS-578T 3.63×, PANC-1 2.46×, HEC-1-A 2.50×, J82 2.91×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (A-427 3.89×, HS-578T 3.33×, HEC-1-A 2.60×, PANC-1 2.28×; ⚠ toxic; transcription drop); [[Dexamethasone (drug)]] 0.5 µM in 1 line (NCI-H1573 4.73×); [[Budesonide (drug)]] 0.05 µM in 1 line (NCI-H1573 4.41×); [[Dexamethasone (drug)]] 5 µM in 1 line (NCI-H1573 4.35×).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.662× (z -7.5, q 4e-11, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZPR1]] (+0.62, fdr 1e-05), [[WDR13]] (+0.60, fdr 1e-05), [[RNH1]] (+0.58, fdr 1e-05); moves opposite to [[PTMAP2]] (-0.59, fdr 3e-05, ⚠ PTMAP2 in the vector space only through flagged drug-doses), [[TOMM7]] (-0.57, fdr 3e-05), [[ATP5ME]] (-0.56, fdr 2e-05), [[MNX1]] (-0.54, fdr 4e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TGFB1I1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10017.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HS-578T 3.63×, PANC-1 2.46×, HEC-1-A 2.50×, J82 2.91×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (A-427 3.89×, HS-578T 3.33×, HEC-1-A 2.60×, PANC-1 2.28×; ⚠ toxic; transcription drop); [[Dexamethasone (drug)]] 0.5 µM in 1 line (NCI-H1573 4.73×); [[Budesonide (drug)]] 0.05 µM in 1 line (NCI-H1573 4.41×); [[Dexamethasone (drug)]] 5 µM in 1 line (NCI-H1573 4.35×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +13.1 | 1e-36 | 37/46 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +13.1 | 1e-36 | 32/36 (A-427, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.32×** | +4.6 | 7e-04 | 21/41 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.3 | 0.003 | 22/47 (HepG2/C3A, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.2 | 0.003 | 18/48 (HOP62, SW1417, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.11 | 20/48 (NCI-H1573, AsPC-1, …) | all doses, flat | position effect removed |
| [[Omeprazole (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.11 | 5/48 (A-172, NCI-H1792, …) | inconsistent across doses |  |
| [[Econazole (drug)]] 5 µM |  | 1.19× | +3.2 | 0.11 | 17/48 (NCI-H1573, A498, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.20× | +3.1 | 0.11 | 13/47 (SW480, NCI-H23, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.11 | 18/47 (NCI-H1573, Panc 03.27, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.18× | +3.0 | 0.12 | 16/48 (NCI-H1573, NCI-H2347, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10017.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.662×** | -7.5 | 4e-11 | 33/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.672×** | -7.2 | 2e-10 | 30/48 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.767×** | -6.8 | 2e-09 | 29/47 (LOX-IMVI, A-427, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.690×** | -6.7 | 3e-09 | 33/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.715×** | -6.1 | 1e-07 | 27/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.549×** | -5.7 | 1e-06 | 26/48 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.734×** | -5.6 | 2e-06 | 29/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.806×** | -5.5 | 3e-06 | 27/48 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.745×** | -5.3 | 6e-06 | 27/48 (SW1417, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.748×** | -5.3 | 8e-06 | 26/48 (SW480, CFPAC-1, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.748×** | -5.0 | 2e-05 | 27/48 (J82, NCI-H23, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.600×** | -4.8 | 6e-05 | 23/47 (A-427, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.784×** | -4.4 | 5e-04 | 24/47 (PANC-1, RKO, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.802×** | -4.0 | 0.003 | 23/48 (hTERT-HPNE, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.808×** | -3.9 | 0.004 | 21/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.831×** | -3.2 | 0.041 | 16/48 (SW 1271, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.832×** | -3.1 | 0.067 | 14/47 (A549, LoVo, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.793×** | -3.0 | 0.081 | 10/48 (hTERT-HPNE, SW 900, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10017. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 12.3 | 6 | 0 | [[Dexamethasone (drug)]] 0.5 µM 4.73× (z +9.6) | — |
| [[A-427 (line)]] | wt | 35.4 | 1 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.89× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -16.3) ⚠ cell-cycle shift, explains ~13% of this change |
| [[HS-578T (line)]] | alt | 50.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 60.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.405× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.426× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 37.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 46.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 35.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 40.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.416× (z -11.3) |
| [[H4 (line)]] | wt | 54.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.260× (z -9.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 41.0 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.265× (z -9.5) |
| [[HOP62 (line)]] | alt | 47.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 32.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 34.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.343× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 37.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -13.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 42.0 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.5 µM 0.0757× (z -8.5) |
| [[SW1417 (line)]] | alt | 55.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10017), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZPR1]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[WDR13]] | +0.60 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[RNH1]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[PSME3]] | +0.58 | +0.39 / +0.56 | both halves | 6e-05 |  |
| [[AHNAK]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[NRAS]] | +0.57 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[POLDIP2]] | +0.57 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[GLUL]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[SHC1]] | +0.56 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[ATL3]] | +0.56 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[SMU1]] | +0.55 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[EIF4G2]] | +0.55 | +0.42 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTMAP2]] ⚠ | -0.59 | -0.44 / -0.53 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TOMM7]] | -0.57 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ATP5ME]] | -0.56 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[MNX1]] | -0.54 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[DCTN6-DT]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[RNF114]] | -0.54 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[RPL36]] | -0.53 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[C4orf48]] | -0.53 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[COX17]] | -0.53 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[COX5A]] ⚠ | -0.53 | -0.32 / -0.50 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[C19orf81]] | -0.52 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[FAM162A]] | -0.52 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[CCDC85B]] | -0.52 | -0.27 / -0.53 | both halves | 3e-04 |  |
| [[RPS26]] | -0.52 | -0.28 / -0.53 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGFB1I1]] | B | TGFB1I1 activity raises TMEM43's level | lines that do not express TGFB1I1 (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without TGFB1I1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, ENSG00000234405, TMOD1 |
| [[FSTL3]] | B | FSTL3 activity raises TMEM43's level | lines that do not express FSTL3 (7) vs lines expressing it (43) | 1.36× lower at baseline in the lines without FSTL3 | 0.071 | ⚠ within organs, on part of the lines; also absent: PDLIM2, TAGLN2, CCND1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.507). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-11.3, 7.1); signed map (12.8, -8.9). **Vector** length 98.1, 22.3% of its response variance represented; |z| ≥ 3 in 1,112 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +13.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +3.2 | +3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.0 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.8 | -5.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.6 | -5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | -2.9 | -3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -7.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.9 | -2.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 43 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:14,125,015-14,143,680 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3222, DKFZp586G1919, LUMA; previously ARVD5 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTV4](https://www.uniprot.org/uniprotkb/Q9BTV4) (Transmembrane protein 43):

> May have an important role in maintaining nuclear envelope structure by organizing protein complexes at the inner nuclear membrane. Required for retaining emerin at the inner nuclear membrane (By similarity). Plays a role in the modulation of innate immune signaling through the cGAS-STING pathway by interacting with RNF26. In addition, functions as a critical signaling component in mediating NF-kappa-B activation by acting downstream of EGFR and upstream of CARD10. Contributes to passive …

**Summary**, from NCBI Gene [79188](https://www.ncbi.nlm.nih.gov/gene/79188):

> This gene belongs to the TMEM43 family. Defects in this gene are the cause of familial arrhythmogenic right ventricular dysplasia type 5 (ARVD5), also known as arrhythmogenic right ventricular cardiomyopathy type 5 (ARVC5). Arrhythmogenic right ventricular dysplasia is an inherited disorder, often involving both ventricles, and is characterized by ventricular tachycardia, heart failure, sudden cardiac death, and fibrofatty replacement of cardiomyocytes. This gene contains a response element for …

**Accessions** — [HGNC:28472](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28472) · Entrez [79188](https://www.ncbi.nlm.nih.gov/gene/79188) · UniProt [Q9BTV4](https://www.uniprot.org/uniprotkb/Q9BTV4) · Ensembl [ENSG00000170876](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170876)

## Data

Gene col 10017: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10017); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10017, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10017]; `tensor/DDL_lfc|DDL_z.npy` [10017]; `embed/gene_vectors.npy` [10017]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10017 or target_col == 10017). Every well: [[TMEM43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
