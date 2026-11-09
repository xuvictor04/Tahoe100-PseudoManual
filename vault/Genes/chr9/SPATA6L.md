---
symbol: "SPATA6L"
type: "gene"
col: 2794
ensembl_id: "ENSG00000106686"
name: "spermatogenesis associated 6 like"
location: "9p24.2-p24.1"
module: 8
arm: "+"
pooled_cpm: 17.58
n_lines_expressing: 35
n_dd_up: 20
n_dd_down: 18
n_dd_up_clean: 15
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 53
direction_downstream: 53
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SPATA6L

*spermatogenesis associated 6 like* — 9p24.2-p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.77× (z +8.1, q 1e-13, up in 19 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.396× (z -13.4, q 6e-38, down in 26 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.417× (z -12.6, q 4e-34, down in 28 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAAH2]] (+0.75, fdr 7e-06), [[BCL2L15]] (+0.74, fdr 7e-06), [[SAMD12-AS1]] (+0.70, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 53 arrows point to it, the strongest [[SPINT1]] → it (grade B ⚠); 53 go from it, the strongest it → [[XDH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2794.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +8.1 | 1e-13 | 19/31 (LOX-IMVI, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +8.1 | 1e-13 | 10/31 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +6.5 | 1e-08 | 4/18 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.7 | 2e-06 | 14/32 (J82, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.5 | 4e-06 | 3/28 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +4.9 | 1e-04 | 11/32 (HEC-1-A, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.41×** | +4.6 | 3e-04 | 13/32 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.35×** | +4.1 | 0.003 | 7/32 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.003 | 7/31 (hTERT-HPNE, HEC-1-A, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.003 | 12/30 (KATO III, A549, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.008 | 12/32 (HEC-1-A, AsPC-1, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.29×** | +3.5 | 0.021 | 7/31 (HepG2/C3A, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.021 | 7/31 (KATO III, LoVo, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +3.4 | 0.024 | 3/21 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.024 | 6/33 (SW1417, RKO, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.58×** | +3.4 | 0.024 | 9/31 (HEC-1-A, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.055 | 8/32 (J82, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.073 | 11/33 (HEC-1-A, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.088 | 13/32 (HEC-1-A, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2794.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.396×** | -13.4 | 6e-38 | 26/31 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.417×** | -12.6 | 4e-34 | 28/32 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.513×** | -9.6 | 1e-19 | 26/32 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.562×** | -8.3 | 1e-14 | 23/32 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.609×** | -7.2 | 8e-11 | 20/32 (KATO III, Panc 03.27, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.635×** | -6.3 | 3e-08 | 19/28 (COLO 205, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.457×** | -5.9 | 3e-07 | 17/31 (KATO III, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.716×** | -4.9 | 8e-05 | 16/30 (COLO 205, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.725×** | -4.5 | 4e-04 | 14/31 (COLO 205, AsPC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.766×** | -3.9 | 0.006 | 14/31 (SW480, A549, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.781×** | -3.6 | 0.016 | 12/32 (CFPAC-1, SW480, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.624×** | -3.6 | 0.016 | 11/30 (CFPAC-1, A549, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.783×** | -3.6 | 0.016 | 17/32 (KATO III, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.632×** | -3.5 | 0.021 | 15/31 (HCT15, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.635×** | -3.4 | 0.022 | 15/31 (Panc 03.27, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.792×** | -3.4 | 0.024 | 7/30 (CFPAC-1, Panc 03.27, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.796×** | -3.3 | 0.030 | 11/32 (NCI-H2030, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2794. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 249 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0482× (z -37.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -19.7) |
| [[KATO III (line)]] | alt | 85.3 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -25.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -16.0) |
| [[HT-29 (line)]] | alt | 77.7 | 0 | 11 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.166× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -11.1) |
| [[SW480 (line)]] | alt | 32.2 | 0 | 11 (9 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.173× (z -16.0) |
| [[Panc 03.27 (line)]] | alt | 32.3 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0772× (z -16.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 28.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -12.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 25.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -17.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -10.2) |
| [[HCT15 (line)]] | alt | 46.6 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 34.6 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0775× (z -12.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 43.6 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.185× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[HEC-1-A (line)]] | alt | 20.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -11.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 14.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -13.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 21.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -12.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 6.11 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0654× (z -8.5) |
| [[J82 (line)]] | alt | 6.52 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0784× (z -11.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 5.09 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0853× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 29.2 | 0 | 1 | — | [[Relugolix (drug)]] 5 µM 0.170× (z -13.2) |
| [[SW 900 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0579× (z -13.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.70 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[NCI-H23 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.40 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 20.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2794), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAAH2]] | +0.75 | +0.66 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[BCL2L15]] | +0.74 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[SAMD12-AS1]] | +0.70 | +0.65 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ARHGEF38]] | +0.69 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[ADCY4]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[PROM1]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[MUC20]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[PLCH1]] | +0.68 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[PRSS51]] | +0.67 | +0.58 / +0.62 | both halves | 8e-06 | **novel candidate** |
| [[TOX3]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[PTPN22]] | +0.65 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[POF1B]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 50, C 3. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPINT1]] | B | SPINT1 activity raises SPATA6L's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 3.80× lower at baseline in the lines without SPINT1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[HSH2D]] | B | HSH2D activity raises SPATA6L's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 3.66× lower at baseline in the lines without HSH2D | 0.004 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[MMP7]] | B | MMP7 activity raises SPATA6L's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.67× lower at baseline in the lines without MMP7 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[TMEM45B]] | B | TMEM45B activity raises SPATA6L's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 3.95× lower at baseline in the lines without TMEM45B | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[DSCAML1]] | B | DSCAML1 activity raises SPATA6L's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.05× lower at baseline in the lines without DSCAML1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[TOX3]] | B | TOX3 activity raises SPATA6L's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 3.26× lower at baseline in the lines without TOX3 | 0.011 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[HNF4G]] | B | HNF4G activity raises SPATA6L's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 2.99× lower at baseline in the lines without HNF4G | 0.012 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[LINC03040]] | B | LINC03040 activity raises SPATA6L's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 3.50× lower at baseline in the lines without LINC03040 | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[SLC44A4]] | B | SLC44A4 activity raises SPATA6L's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 4.29× lower at baseline in the lines without SLC44A4 | 0.013 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[MROH3P]] | B | MROH3P activity raises SPATA6L's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 3.61× lower at baseline in the lines without MROH3P | 0.013 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[RNF183]] | B | RNF183 activity raises SPATA6L's level | lines that do not express RNF183 (36) vs lines expressing it (14) | 3.51× lower at baseline in the lines without RNF183 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, LINC02964, VIL1 |
| [[CATSPERB]] | B | CATSPERB activity raises SPATA6L's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 3.25× lower at baseline in the lines without CATSPERB | 0.017 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |

### Downstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 49, C 4. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XDH]] | B | SPATA6L activity raises XDH's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 3.40× lower at baseline in the lines without SPATA6L | 0.006 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[MTUS1]] | B | SPATA6L activity raises MTUS1's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 3.22× lower at baseline in the lines without SPATA6L | 0.012 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[SAMD12-AS1]] | B | SPATA6L activity raises SAMD12-AS1's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 2.82× lower at baseline in the lines without SPATA6L | 0.016 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[MROH3P]] | B | SPATA6L activity raises MROH3P's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 3.10× lower at baseline in the lines without SPATA6L | 0.022 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[HPGD]] | B | SPATA6L activity raises HPGD's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 3.12× lower at baseline in the lines without SPATA6L | 0.022 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[SAMD12]] | B | SPATA6L activity raises SAMD12's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 3.87× lower at baseline in the lines without SPATA6L | 0.025 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[SGPP2]] | B | SPATA6L activity raises SGPP2's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 4.14× lower at baseline in the lines without SPATA6L | 0.025 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[SPINT1]] | B | SPATA6L activity raises SPINT1's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 5.30× lower at baseline in the lines without SPATA6L | 0.032 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[FRK]] | B | SPATA6L activity raises FRK's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 2.98× lower at baseline in the lines without SPATA6L | 0.032 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[TMEM45B]] | B | SPATA6L activity raises TMEM45B's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 4.98× lower at baseline in the lines without SPATA6L | 0.032 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[SYK]] | B | SPATA6L activity raises SYK's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 3.67× lower at baseline in the lines without SPATA6L | 0.034 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[ADCY4]] | B | SPATA6L activity raises ADCY4's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 2.21× lower at baseline in the lines without SPATA6L | 0.035 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.791). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.3, 52.7); signed map (59.7, 1.0). **Vector** length 82.9, 20.6% of its response variance represented; |z| ≥ 3 in 843 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | -1.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.4 | -7.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.9 | -2.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -1.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.5 | -2.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Tomivosertib (drug)]] 5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis associated 6 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.2-p24.1 — chr9:4,553,386-4,666,674 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10058; previously C9orf68 |
| Matched by | ensembl_id |

UniProt [Q8N4H0](https://www.uniprot.org/uniprotkb/Q8N4H0) carries no function annotation.

**Summary**, from NCBI Gene [55064](https://www.ncbi.nlm.nih.gov/gene/55064):

> Predicted to enable myosin light chain binding activity. Predicted to be involved in spermatogenesis. Predicted to be located in sperm head-tail coupling apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25472](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25472) · Entrez [55064](https://www.ncbi.nlm.nih.gov/gene/55064) · UniProt [Q8N4H0](https://www.uniprot.org/uniprotkb/Q8N4H0) · Ensembl [ENSG00000106686](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106686)

## Data

Gene col 2794: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2794); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2794, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2794]; `tensor/DDL_lfc|DDL_z.npy` [2794]; `embed/gene_vectors.npy` [2794]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2794 or target_col == 2794). Every well: [[SPATA6L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATA6L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
