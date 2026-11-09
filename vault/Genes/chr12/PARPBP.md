---
symbol: "PARPBP"
type: "gene"
col: 11683
ensembl_id: "ENSG00000185480"
name: "PARP1 binding protein"
location: "12q23.2"
module: 67
arm: "+"
pooled_cpm: 42.55
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# PARPBP

*PARP1 binding protein* — 12q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (15 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.69× (z +10.9, q 8e-25, up in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Brivudine (drug)]] 5 µM: 1.45× (z +4.0, q 0.003, up in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 4.43×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 3.85×; ⚠ cell-cycle shift, explains ~89% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 3.45×; ⚠ cell-cycle shift, explains ~48% of this change).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.704× (z -9.7, q 1e-19, down in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.712× (z -9.4, q 1e-18, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PBK]] (+0.90, fdr 7e-06), [[CIT]] (+0.89, fdr 7e-06), [[BUB1B]] (+0.87, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RGS3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 17 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11683.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 4.43×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 3.85×; ⚠ cell-cycle shift, explains ~89% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 3.45×; ⚠ cell-cycle shift, explains ~48% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.69×** | +10.9 | 8e-25 | 39/48 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.65×** | +10.3 | 2e-22 | 37/48 (LoVo, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.49×** | +8.2 | 4e-14 | 33/48 (LoVo, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.38×** | +6.7 | 3e-09 | 25/47 (KATO III, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.34×** | +6.1 | 1e-07 | 24/48 (KATO III, NCI-H23, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.31×** | +5.6 | 2e-06 | 26/48 (KATO III, NCI-H23, …) | all doses, flat | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.20×** | +5.0 | 4e-05 | 20/48 (HS-578T, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.27×** | +4.9 | 7e-05 | 22/48 (NCI-H23, A549, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.26×** | +4.9 | 7e-05 | 18/47 (NCI-H23, A549, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~81% of this change | **1.24×** | +4.4 | 6e-04 | 14/47 (RPMI-7951, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.49×** | +4.3 | 7e-04 | 19/47 (J82, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.22×** | +4.1 | 0.002 | 14/48 (LoVo, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.21×** | +4.0 | 0.003 | 20/48 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.003 | 16/48 (RKO, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.20×** | +3.7 | 0.010 | 19/42 (A549, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.027 | 12/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.083 | 2/48 (LoVo, LOX-IMVI) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11683.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.704×** | -9.7 | 1e-19 | 33/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.712×** | -9.4 | 1e-18 | 26/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.644×** | -8.2 | 3e-14 | 31/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.735×** | -8.0 | 2e-13 | 29/48 (H4, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.697×** | -6.8 | 2e-09 | 30/48 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.833×** | -5.1 | 2e-05 | 22/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.778×** | -5.1 | 2e-05 | 24/48 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.782×** | -5.0 | 3e-05 | 21/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.711×** | -5.0 | 4e-05 | 18/48 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.788×** | -4.5 | 5e-04 | 20/48 (NCI-H460, SNU-1, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.811×** | -4.3 | 1e-03 | 20/48 (SW480, SNU-423, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.808×** | -4.2 | 0.001 | 16/48 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.810×** | -4.1 | 0.002 | 19/48 (NCI-H460, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Amsacrine (drug)]] 5 µM |  | 0.862× | -4.0 | 0.003 | 18/48 (LS 180, H4, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 0.874× | -3.7 | 0.009 | 14/48 (LS 180, H4, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.844× | -3.5 | 0.018 | 15/47 (NCI-H2030, H4, …) | two highest doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.847× | -3.4 | 0.024 | 21/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.857× | -3.1 | 0.045 | 12/48 (CHP-212, H4, …) | top dose only |  |
| [[Imiquimod (maleate) (drug)]] 0.05 µM |  | 0.849× | -3.1 | 0.051 | 7/47 (NCI-H1792, HepG2/C3A, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.848× | -3.1 | 0.053 | 17/47 (SNU-423, NCI-H460, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.895× | -3.0 | 0.064 | 10/48 (HCT15, A-427, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11683. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 47.8 | 0 | 6 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.166× (z -12.5) |
| [[A498 (line)]] | wt | 27.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.6) |
| [[LoVo (line)]] | wt | 33.6 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +10.9) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H460 (line)]] | wt | 52.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -11.3) |
| [[A-427 (line)]] | wt | 56.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 58.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -12.3) |
| [[KATO III (line)]] | alt | 38.8 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.43× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 49.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -12.7) |
| [[SW480 (line)]] | alt | 69.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -17.6) |
| [[A-172 (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.393× (z -9.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[AN3 CA (line)]] | alt | 80.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 72.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.234× (z -10.4) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 36.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -8.9) |
| [[LS 180 (line)]] | wt | 43.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.410× (z -8.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H23 (line)]] | alt | 73.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -9.6) |
| [[NCI-H661 (line)]] | alt | 53.5 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0701× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 44.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.612× (z -8.9) |
| [[RKO (line)]] | wt | 54.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 42.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -11.7) |
| [[SNU-1 (line)]] | wt | 67.2 | 0 | 1 | — | [[Futibatinib (drug)]] 5 µM 0.0747× (z -8.5) |
| [[A549 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11683), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBK]] | +0.90 | +0.87 / +0.89 | both halves | 7e-06 | STRING 669 |
| [[CIT]] | +0.89 | +0.86 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[BUB1B]] | +0.87 | +0.85 / +0.87 | both halves | 7e-06 | STRING 540 |
| [[NEIL3]] | +0.86 | +0.84 / +0.85 | both halves | 7e-06 | STRING 491 |
| [[CENPI]] | +0.86 | +0.84 / +0.83 | both halves | 7e-06 | STRING 710 |
| [[INCENP]] | +0.84 | +0.79 / +0.82 | both halves | 7e-06 |  |
| [[CDCA3]] | +0.84 | +0.82 / +0.80 | both halves | 7e-06 | STRING 473 |
| [[KIF18B]] | +0.83 | +0.81 / +0.81 | both halves | 7e-06 | STRING 488 |
| [[OIP5]] | +0.83 | +0.85 / +0.82 | both halves | 7e-06 | STRING 559 |
| [[KIF22]] | +0.83 | +0.85 / +0.78 | both halves | 7e-06 | STRING 437 |
| [[KIF15]] | +0.82 | +0.79 / +0.86 | both halves | 7e-06 | STRING 632 |
| [[SPC24]] | +0.82 | +0.80 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS3]] | B | RGS3 activity lowers PARPBP's level | lines that do not express RGS3 (7) vs lines expressing it (43) | 1.64× higher at baseline in the lines without RGS3 | 0.053 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises PARPBP's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.13× lower at baseline in the lines without NDC80 | 0.040 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.910). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.5, -53.6); signed map (-46.4, -40.9). **Vector** length 140, 42.5% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.79 to 12); *G2/M checkpoint* (hallmark, mean cos +0.78 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.77 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | +4.8 | +4.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.8 | +10.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.4 | +4.3 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +4.4 | +5.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.3 | +10.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.1 | +2.4 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.1 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.6 | -8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.0 | -9.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -6.9 | -9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -5.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -6.3 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -4.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.3 | -4.0 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | PARP1 binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.2 — chr12:102,120,183-102,197,520 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20641, PARI; previously C12orf48 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWS1](https://www.uniprot.org/uniprotkb/Q9NWS1) (PCNA-interacting partner):

> Required to suppress inappropriate homologous recombination, thereby playing a central role DNA repair and in the maintenance of genomic stability. Antagonizes homologous recombination by interfering with the formation of the RAD51-DNA homologous recombination structure. Binds single-strand DNA and poly(A) homopolymers. Positively regulate the poly(ADP-ribosyl)ation activity of PARP1; however such function may be indirect.

**Summary**, from NCBI Gene [55010](https://www.ncbi.nlm.nih.gov/gene/55010):

> Predicted to enable DNA binding activity. Involved in negative regulation of double-strand break repair via homologous recombination. Located in chromatin and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26074](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26074) · Entrez [55010](https://www.ncbi.nlm.nih.gov/gene/55010) · UniProt [Q9NWS1](https://www.uniprot.org/uniprotkb/Q9NWS1) · Ensembl [ENSG00000185480](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185480)

## Data

Gene col 11683: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11683); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11683, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11683]; `tensor/DDL_lfc|DDL_z.npy` [11683]; `embed/gene_vectors.npy` [11683]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11683 or target_col == 11683). Every well: [[PARPBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARPBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
