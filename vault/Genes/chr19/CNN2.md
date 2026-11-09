---
symbol: "CNN2"
type: "gene"
col: 755
ensembl_id: "ENSG00000064666"
name: "calponin 2"
location: "19p13.3"
module: 111
arm: "+"
pooled_cpm: 54.08
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 31
n_dd_up_clean: 3
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# CNN2

*calponin 2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.04× (z +17.8, q 0e+00, up in 42 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.56× (z +7.1, q 1e-10, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.540× (z -13.9, q 5e-41, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPZB]] (+0.60, fdr 1e-05), [[TPM4]] (+0.58, fdr 2e-05), [[NCOR2]] (+0.57, fdr 1e-05); moves opposite to [[LINC00944]] (-0.59, fdr 1e-04), [[RPP38]] (-0.57, fdr 3e-05), [[LINC02100]] (-0.56, fdr 2e-04).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 755.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.04×** | +17.8 | 0e+00 | 42/47 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +15.9 | 0e+00 | 38/40 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +11.4 | 7e-28 | 36/43 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +7.1 | 1e-10 | 31/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.38×** | +5.2 | 3e-05 | 32/45 (SW1417, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.0 | 5e-05 | 0/48 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.005 | 26/47 (MIA PaCa-2, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.27×** | +3.8 | 0.009 | 18/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.040 | 12/47 (Hs 766T, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 755.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.540×** | -13.9 | 5e-41 | 36/47 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.476×** | -11.8 | 9e-30 | 39/47 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -8.1 | 1e-13 | 31/47 (C-33 A, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.639×** | -7.1 | 2e-10 | 36/47 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.657×** | -6.4 | 2e-08 | 34/46 (NCI-H23, C-33 A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.679×** | -5.9 | 3e-07 | 29/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.698×** | -5.7 | 9e-07 | 32/47 (J82, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.714×** | -5.4 | 6e-06 | 32/47 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.717×** | -5.3 | 8e-06 | 27/47 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.724×** | -5.1 | 2e-05 | 31/47 (MIA PaCa-2, C32, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.527×** | -5.0 | 3e-05 | 35/47 (AN3 CA, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.731×** | -5.0 | 3e-05 | 27/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.536×** | -4.9 | 4e-05 | 28/48 (NCI-H23, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.804×** | -4.9 | 4e-05 | 30/47 (Hs 766T, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.724×** | -4.8 | 5e-05 | 28/47 (HT-29, LOX-IMVI, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.735×** | -4.7 | 9e-05 | 29/47 (C-33 A, J82, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.751×** | -4.5 | 2e-04 | 23/47 (C-33 A, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 755. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 36.0 | 1 (1 ⚠) | 9 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.28× (z +10.3) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.0290× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -12.0) |
| [[C-33 A (line)]] | alt | 230 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -20.7) |
| [[LoVo (line)]] | wt | 47.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -15.7) |
| [[MIA PaCa-2 (line)]] | alt | 40.5 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.71× (z +12.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 41.1 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -13.7) |
| [[NCI-H23 (line)]] | alt | 92.2 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -23.3) |
| [[HT-29 (line)]] | alt | 73.1 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +10.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -13.0) |
| [[J82 (line)]] | alt | 60.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -10.8) |
| [[PANC-1 (line)]] | alt | 44.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.369× (z -9.8) |
| [[SNU-423 (line)]] | alt | 53.8 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.90× (z +14.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 50.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +17.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 26.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +12.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 38.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 46.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.8) |
| [[COLO 205 (line)]] | alt | 36.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 100 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +12.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -9.9) |
| [[Hs 766T (line)]] | wt | 92.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 84.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -14.5) |
| [[SW 900 (line)]] | alt | 43.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.90× (z +9.5) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.166× (z -12.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -10.9) |
| [[SW480 (line)]] | alt | 77.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +13.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -12.5) |
| [[A-427 (line)]] | wt | 66.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +14.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 43.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -16.4) |
| [[HCT15 (line)]] | alt | 72.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +9.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -18.4) |
| [[HepG2_C3A (line)]] | wt | 81.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -16.1) |
| [[HOP62 (line)]] | alt | 30.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 40.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +11.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 62.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 19.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.24× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 26.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -9.7) |
| [[A-172 (line)]] | wt | 58.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +12.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 75.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -10.0) |
| [[KATO III (line)]] | alt | 36.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 72.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 88.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +12.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 57.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.337× (z -8.5) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 42.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 57.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -8.9) |
| [[SW1417 (line)]] | alt | 74.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +13.4) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 755), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPZB]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[TPM4]] | +0.58 | +0.60 / +0.47 | both halves | 2e-05 | STRING 507 |
| [[NCOR2]] | +0.57 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[CADM4]] | +0.56 | +0.23 / +0.43 | both halves | 5e-04 |  |
| [[KHDRBS1]] | +0.55 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[KANK2]] | +0.55 | +0.44 / +0.33 | both halves | 1e-04 |  |
| [[RSU1]] | +0.55 | +0.48 / +0.32 | both halves | 2e-04 | pathway: HALLMARK_APICAL_JUNCTION |
| [[INTS1]] | +0.55 | +0.41 / +0.40 | both halves | 4e-05 |  |
| [[SORT1]] | +0.53 | +0.40 / +0.35 | both halves | 1e-04 |  |
| [[CEP131]] | +0.53 | +0.39 / +0.19 | ⚠ not reproduced | 8e-04 |  |
| [[PLXND1]] | +0.52 | +0.46 / +0.35 | both halves | 1e-04 |  |
| [[MAPKAPK2]] | +0.52 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[APMAP]] | +0.52 | +0.49 / +0.25 | both halves | 4e-04 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00944]] | -0.59 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[RPP38]] | -0.57 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[LINC02100]] | -0.56 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[DGLUCY]] | -0.54 | -0.48 / -0.37 | both halves | 7e-05 |  |
| [[ZCCHC10]] | -0.54 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[ZC3HC1]] | -0.54 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[COA6]] | -0.54 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[NSMCE1-DT]] | -0.53 | -0.54 / -0.28 | both halves | 3e-04 |  |
| [[PHF11]] | -0.53 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[PIGP]] | -0.53 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[ATF5]] | -0.53 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[BCDIN3D]] | -0.53 | -0.50 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CNN2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.1, 5.3); signed map (-9.3, 36.1). **Vector** length 102, 28.6% of its response variance represented; |z| ≥ 3 in 1,128 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +7.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +2.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | +4.3 | +3.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +0.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.3 | +1.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.8 | +1.2 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.6 | +0.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.3 | -4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -11.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -3.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | calponin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,026,586-1,039,068 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Calponin family |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 7 pathways, smallest: Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; Interleukin-12 signaling; Interleukin-12 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99439](https://www.uniprot.org/uniprotkb/Q99439) (Calponin-2):

> Thin filament-associated protein that is implicated in the regulation and modulation of smooth muscle contraction. It is capable of binding to actin, calmodulin and tropomyosin. The interaction of calponin with actin inhibits the actomyosin Mg-ATPase activity.

**Summary**, from NCBI Gene [1265](https://www.ncbi.nlm.nih.gov/gene/1265):

> The protein encoded by this gene, which can bind actin, calmodulin, troponin C, and tropomyosin, may function in the structural organization of actin filaments. The encoded protein could play a role in smooth muscle contraction and cell adhesion. Several pseudogenes of this gene have been identified, and are present on chromosomes 1, 2, 3, 6, 9, 11, 13, 15, 16, 21 and 22. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:2156](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2156) · Entrez [1265](https://www.ncbi.nlm.nih.gov/gene/1265) · UniProt [Q99439](https://www.uniprot.org/uniprotkb/Q99439) · Ensembl [ENSG00000064666](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064666)

## Data

Gene col 755: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 755); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 755, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 755]; `tensor/DDL_lfc|DDL_z.npy` [755]; `embed/gene_vectors.npy` [755]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 755 or target_col == 755). Every well: [[CNN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
