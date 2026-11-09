---
symbol: "SP4"
type: "gene"
col: 2680
ensembl_id: "ENSG00000105866"
name: "Sp4 transcription factor"
location: "7p15.3"
module: 25
arm: "-"
pooled_cpm: 55.57
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SP4

*Sp4 transcription factor* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.36× (z +8.8, q 7e-16, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.475× (z -15.3, q 0e+00, down in 38 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.650× (z -8.9, q 1e-16, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNRC6C]] (+0.56, fdr 1e-05), [[KATNA1]] (+0.55, fdr 3e-05), [[SHOC2]] (+0.52, fdr 2e-05); moves opposite to [[PSMB2]] (-0.59, fdr 1e-05), [[USP14]] (-0.58, fdr 1e-05), [[UBQLN1]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2680.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +8.8 | 7e-16 | 25/48 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +8.4 | 1e-14 | 30/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +7.7 | 4e-12 | 30/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +7.1 | 2e-10 | 28/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +6.5 | 1e-08 | 28/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +6.4 | 2e-08 | 28/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +6.0 | 1e-07 | 26/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +5.6 | 2e-06 | 21/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +5.2 | 1e-05 | 26/48 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.25×** | +4.6 | 2e-04 | 19/48 (LOX-IMVI, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 3e-04 | 21/48 (BT-474, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.25×** | +4.4 | 5e-04 | 21/48 (A498, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.22×** | +4.0 | 0.002 | 21/48 (LoVo, SW480, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.009 | 16/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.19× | +3.6 | 0.012 | 13/48 (A-172, A498, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.022 | 12/48 (SW480, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.18× | +3.4 | 0.022 | 10/47 (J82, NCI-H2030, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.038 | 14/48 (A-172, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2680.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.475×** | -15.3 | 0e+00 | 38/49 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.493×** | -14.0 | 4e-42 | 32/42 (Hs 766T, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.522×** | -12.4 | 7e-33 | 36/44 (SNU-423, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.650×** | -8.9 | 1e-16 | 37/48 (SW480, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.703×** | -7.3 | 5e-11 | 34/48 (HOP62, SW 900, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.740×** | -6.2 | 6e-08 | 28/48 (HEC-1-A, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.596×** | -5.6 | 2e-06 | 20/37 (HEC-1-A, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.761×** | -5.4 | 5e-06 | 27/47 (A-427, C-33 A, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.769×** | -5.1 | 2e-05 | 28/48 (SW 900, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.705×** | -3.8 | 0.009 | 17/45 (SNU-423, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.844× | -3.3 | 0.048 | 17/47 (SW1417, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.899× | -3.1 | 0.089 | 17/48 (SNU-1, BT-474, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.753×** | -3.1 | 0.098 | 13/47 (PANC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2680. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 53.2 | 11 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +19.9) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -10.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 23.4 | 5 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -9.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 57.4 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -11.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 66.9 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 38.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +19.2) | [[Lonafarnib (drug)]] 5 µM 0.119× (z -9.0) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 75.9 | 0 | 4 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0636× (z -18.2) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 62.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.540× (z -9.0) |
| [[SNU-423 (line)]] | alt | 60.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -17.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 56.7 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.442× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.506× (z -9.2) |
| [[BT-474 (line)]] | alt | 75.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -10.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 66.1 | 0 | 3 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0683× (z -13.6) ⚠ toxic |
| [[HS-578T (line)]] | alt | 51.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -12.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 28.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 77.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -17.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 87.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Oxaprozin (drug)]] 0.5 µM 0.255× (z -8.7) |
| [[C-33 A (line)]] | alt | 65.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -13.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 27.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.138× (z -12.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 45.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -12.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 51.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0655× (z -22.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 72.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.345× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 64.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 40.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -12.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 94.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.158× (z -19.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -9.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 39.4 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +8.6) ⚠ cell-cycle shift, explains ~19% of this change | — |
| [[A549 (line)]] | wt | 51.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.352× (z -9.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 45.9 | 0 | 1 | — | [[Belzutifan (drug)]] 5 µM 0.112× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -10.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 33.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.193× (z -10.7) ⚠ transcription drop; cell-cycle shift, explains ~47% of this change |
| [[KATO III (line)]] | alt | 45.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -11.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 62.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.176× (z -9.2) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 79.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -18.3) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 84.8 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.129× (z -8.9) |
| [[RKO (line)]] | wt | 63.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -12.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 94.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.458× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 42.7 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.339× (z -9.2) |
| [[SW 1271 (line)]] | alt | 96.5 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0628× (z -12.8) |
| [[SW 900 (line)]] | alt | 56.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -13.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 87.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2680), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*37 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6C]] | +0.56 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[KATNA1]] | +0.55 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[SHOC2]] | +0.52 | +0.47 / +0.52 | both halves | 2e-05 | same gene group |
| [[EIF1B]] | +0.51 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[MCRIP1]] | +0.50 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[BTG1]] | +0.49 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[PPP1R13L]] | +0.49 | +0.47 / +0.34 | both halves | 1e-04 |  |
| [[PPP1R13B]] | +0.49 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[LRCH3]] | +0.49 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[AMN1]] | +0.48 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[CEP95]] | +0.48 | +0.54 / +0.33 | both halves | 1e-04 |  |
| [[C9orf40]] | +0.47 | +0.37 / +0.50 | both halves | 7e-05 |  |

## Genes that move opposite

*63 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB2]] | -0.59 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[USP14]] | -0.58 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[UBQLN1]] | -0.57 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[GPN1]] | -0.54 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[PSMD11]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[PSMD12]] | -0.52 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[GSR]] | -0.51 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[PSMA1]] | -0.51 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[GFM2]] | -0.51 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[LARP4]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[PSMD6]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[JAKMIP3]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises SP4's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.390). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.7, -14.2); signed map (-23.5, 17.7). **Vector** length 96.7, 24.0% of its response variance represented; |z| ≥ 3 in 1,153 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +8.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.6 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +1.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.5 | +1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.7 | -8.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.4 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.4 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.8 | -7.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.1 | -1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | Sp4 transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:21,428,043-21,514,822 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPR-1, HF1B, MGC130008, MGC130009 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Sp transcription factors; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02446](https://www.uniprot.org/uniprotkb/Q02446) (Transcription factor Sp4):

> Binds to GT and GC boxes promoters elements. Probable transcriptional activator.

**Summary**, from NCBI Gene [6671](https://www.ncbi.nlm.nih.gov/gene/6671):

> The protein encoded by this gene is a transcription factor that can bind to the GC promoter region of a variety of genes, including those of the photoreceptor signal transduction system. The encoded protein binds to the same sites in promoter CpG islands as does the transcription factor SP1, although its expression is much more restricted compared to that of SP1. This gene may be involved in bipolar disorder and schizophrenia. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:11209](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11209) · Entrez [6671](https://www.ncbi.nlm.nih.gov/gene/6671) · UniProt [Q02446](https://www.uniprot.org/uniprotkb/Q02446) · Ensembl [ENSG00000105866](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105866)

## Data

Gene col 2680: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2680); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2680, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2680]; `tensor/DDL_lfc|DDL_z.npy` [2680]; `embed/gene_vectors.npy` [2680]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2680 or target_col == 2680). Every well: [[SP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
