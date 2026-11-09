---
symbol: "RAVER2"
type: "gene"
col: 8520
ensembl_id: "ENSG00000162437"
name: "ribonucleoprotein, PTB binding 2"
location: "1p31.3"
module: 146
arm: "+"
pooled_cpm: 34.46
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 22
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# RAVER2

*ribonucleoprotein, PTB binding 2* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.46× (z +7.6, q 8e-12, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.424× (z -17.2, q 0e+00, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MBOAT1]] (+0.68, fdr 7e-06), [[TPD52L1]] (+0.67, fdr 7e-06), [[OSBPL1A]] (+0.66, fdr 7e-06); moves opposite to [[GPATCH2L]] (-0.58, fdr 7e-06), [[DRAP1]] (-0.57, fdr 1e-05), [[SLC12A4]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SLC5A4-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8520.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +7.6 | 8e-12 | 33/46 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.31×** | +7.6 | 8e-12 | 24/46 (A498, J82, …) | rises with dose | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | **1.71×** | +5.6 | 4e-06 | 22/43 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +5.5 | 5e-06 | 18/45 (HOP62, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +4.3 | 0.002 | 14/44 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +4.0 | 0.005 | 14/46 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.005 | 11/46 (NCI-H2030, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.006 | 11/45 (KATO III, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.007 | 9/47 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.007 | 9/45 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.14× | +3.7 | 0.011 | 5/46 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.021 | 8/45 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.18× | +3.4 | 0.034 | 12/46 (NCI-H1792, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.2 | 0.049 | 8/46 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.049 | 11/45 (NCI-H2030, A-427, …) | top dose only |  |
| [[Bentamapimod (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.059 | 3/46 (A498, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.059 | 6/46 (NCI-H1573, KATO III, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.077 | 8/46 (HT-29, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8520.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.424×** | -17.2 | 0e+00 | 40/46 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.552×** | -16.8 | 0e+00 | 38/46 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.471×** | -15.0 | 0e+00 | 38/46 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.516×** | -13.3 | 6e-38 | 33/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.615×** | -9.7 | 2e-20 | 26/46 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.649×** | -8.3 | 8e-15 | 26/46 (RKO, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.664×** | -8.2 | 2e-14 | 27/44 (RKO, HCT15, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.699×** | -7.2 | 5e-11 | 22/45 (LoVo, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.726×** | -6.4 | 1e-08 | 28/46 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.731×** | -6.3 | 2e-08 | 22/46 (NCI-H1573, RKO, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.808×** | -6.1 | 7e-08 | 20/45 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -5.8 | 3e-07 | 26/44 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.766×** | -5.3 | 4e-06 | 26/45 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.836× | -5.1 | 1e-05 | 20/46 (SNU-1, RKO, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.776×** | -4.9 | 4e-05 | 20/46 (SNU-1, LoVo, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.872× | -3.9 | 0.003 | 14/46 (HT-29, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.828×** | -3.8 | 0.004 | 15/45 (H4, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.834× | -3.6 | 0.007 | 10/45 (KATO III, LoVo, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.763×** | -3.6 | 0.008 | 16/43 (HT-29, HCT15, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.845× | -3.4 | 0.016 | 17/45 (HT-29, SNU-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.853× | -3.2 | 0.029 | 10/45 (H4, KATO III, …) | all doses, flat |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.739×** | -3.2 | 0.031 | 11/43 (C32, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.858× | -3.1 | 0.041 | 18/46 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8520. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 31.1 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -15.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -11.6) |
| [[SW480 (line)]] | alt | 42.2 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.174× (z -21.3) |
| [[MIA PaCa-2 (line)]] | alt | 56.3 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -15.0) |
| [[LoVo (line)]] | wt | 68.0 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -18.1) |
| [[Panc 03.27 (line)]] | alt | 44.9 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -14.6) |
| [[RKO (line)]] | wt | 47.3 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0655× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0849× (z -19.5) |
| [[KATO III (line)]] | alt | 48.2 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -14.8) |
| [[C-33 A (line)]] | alt | 93.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -14.5) |
| [[HCT15 (line)]] | alt | 54.6 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0993× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.286× (z -8.9) |
| [[PANC-1 (line)]] | alt | 32.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -15.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -11.8) |
| [[SHP-77 (line)]] | alt | 48.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.320× (z -9.5) |
| [[A-427 (line)]] | wt | 48.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0969× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.319× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 81.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -15.7) |
| [[HT-29 (line)]] | alt | 35.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -14.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.295× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 32.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -17.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.297× (z -9.8) |
| [[LS 180 (line)]] | wt | 72.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -20.3) |
| [[SNU-1 (line)]] | wt | 65.5 | 0 | 3 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.339× (z -11.6) |
| [[SW1417 (line)]] | alt | 52.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.264× (z -13.3) |
| [[SW48 (line)]] | wt | 71.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -11.2) |
| [[A549 (line)]] | wt | 27.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -9.1) |
| [[AN3 CA (line)]] | alt | 87.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 35.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -14.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 34.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -12.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 17.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.266× (z -9.4) |
| [[H4 (line)]] | wt | 33.6 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.183× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -11.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 25.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -8.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.11 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8520), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBOAT1]] | +0.68 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[TPD52L1]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[OSBPL1A]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[STEAP2]] | +0.63 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[ZNF618]] | +0.63 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[PLBD1]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ALDH5A1]] | +0.61 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[USP46]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[FUT10]] | +0.61 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SMG7]] | +0.60 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[SLC35G1]] | +0.60 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[CHPT1]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH2L]] | -0.58 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[DRAP1]] | -0.57 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[SLC12A4]] | -0.56 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[LUCAT1]] | -0.56 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[TUT7]] | -0.56 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[ADGRL1-AS1]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[PDLIM7]] | -0.54 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[DLGAP4]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[KCTD11]] | -0.54 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[C11orf91]] | -0.54 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[MYL12A]] | -0.53 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[KIAA0319L]] | -0.53 | -0.53 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC5A4-AS1]] | B | SLC5A4-AS1 activity raises RAVER2's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 2.34× lower at baseline in the lines without SLC5A4-AS1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[FAXC]] | B | FAXC activity raises RAVER2's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without FAXC | 0.017 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[TLCD4]] | B | TLCD4 activity raises RAVER2's level | lines that do not express TLCD4 (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without TLCD4 | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent |
| [[NFIA]] | B | NFIA activity raises RAVER2's level | lines that do not express NFIA (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without NFIA | 0.098 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[ZBED3]] | C | ZBED3 activity raises RAVER2's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 2.99× lower at baseline in the lines without ZBED3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.731). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-10.8, 13.1); signed map (14.7, -45.3). **Vector** length 106, 27.2% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +6.8 | +7.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +6.6 | +7.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.7 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.6 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.2 | +4.0 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +3.2 | +3.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.1 | +3.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.1 | +3.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -9.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -15.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.2 | -17.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -3.1 | -6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -5.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -7.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ribonucleoprotein, PTB binding 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:64,745,075-64,833,232 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1579, FLJ10770 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCJ3](https://www.uniprot.org/uniprotkb/Q9HCJ3) (Ribonucleoprotein PTB-binding 2):

> May bind single-stranded nucleic acids.

**Summary**, from NCBI Gene [55225](https://www.ncbi.nlm.nih.gov/gene/55225):

> Enables RNA binding activity. Predicted to be located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25577](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25577) · Entrez [55225](https://www.ncbi.nlm.nih.gov/gene/55225) · UniProt [Q9HCJ3](https://www.uniprot.org/uniprotkb/Q9HCJ3) · Ensembl [ENSG00000162437](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162437)

## Data

Gene col 8520: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8520); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8520, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8520]; `tensor/DDL_lfc|DDL_z.npy` [8520]; `embed/gene_vectors.npy` [8520]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8520 or target_col == 8520). Every well: [[RAVER2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAVER2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
