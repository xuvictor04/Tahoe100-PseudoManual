---
symbol: "RASSF8"
type: "gene"
col: 4398
ensembl_id: "ENSG00000123094"
name: "Ras association domain family member 8"
location: "12p12.1"
module: 84
arm: "+"
pooled_cpm: 241.35
n_lines_expressing: 35
n_dd_up: 3
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 11
direction_downstream: 16
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# RASSF8

*Ras association domain family member 8* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.34× (z +7.2, q 3e-10, up in 19 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A498 2.72×, J82 1.93×, A-172 2.08×, SW 900 1.87×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (RPMI-7951 2.56×, A498 2.60×, J82 2.04×; ⚠ cell-cycle shift, explains ~13% of this change); [[Harringtonine (drug)]] 0.5 µM in 2 lines (A498 2.60×, RPMI-7951 2.22×; ⚠ cell-cycle shift, explains ~0% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 1.63×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LoVo 2.30×).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.663× (z -14.9, q 0e+00, down in 26 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX1A]] (+0.58, fdr 7e-06), [[CDH13]] (+0.57, fdr 1e-05), [[AKT3]] (+0.55, fdr 3e-05); moves opposite to [[ACTR3C]] (-0.47, fdr 2e-04), [[SEC16B]] (-0.45, fdr 4e-05), [[FAM53B]] (-0.43, fdr 1e-04, ⚠ FAM53B in the vector space only through flagged drug-doses), [[DERA]] (-0.43, fdr 9e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[BRSK1]] → it (grade B ⚠); 16 go from it, the strongest it → [[TSHZ3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4398.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A498 2.72×, J82 1.93×, A-172 2.08×, SW 900 1.87×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (RPMI-7951 2.56×, A498 2.60×, J82 2.04×; ⚠ cell-cycle shift, explains ~13% of this change); [[Harringtonine (drug)]] 0.5 µM in 2 lines (A498 2.60×, RPMI-7951 2.22×; ⚠ cell-cycle shift, explains ~0% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 1.63×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LoVo 2.30×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.34×** | +7.2 | 3e-10 | 19/32 (H4, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +6.3 | 1e-07 | 6/33 (SW480, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +6.0 | 3e-07 | 21/32 (hTERT-HPNE, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.21×** | +4.9 | 1e-04 | 14/33 (A-172, H4, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +4.2 | 0.003 | 9/34 (SW480, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.17× | +3.9 | 0.010 | 14/33 (RPMI-7951, A498, …) | top dose only | composition shift |
| [[Rapamycin (drug)]] 5 µM |  | 1.11× | +3.7 | 0.014 | 3/33 (LOX-IMVI, A-172, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.15× | +3.7 | 0.018 | 8/33 (A549, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4398.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -14.9 | 0e+00 | 26/34 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.610×** | -12.6 | 5e-34 | 25/33 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.616×** | -12.4 | 7e-33 | 26/33 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.647×** | -11.1 | 2e-26 | 26/33 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.639×** | -11.0 | 4e-26 | 26/33 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.803×** | -7.9 | 2e-13 | 21/33 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.730×** | -7.7 | 8e-13 | 20/31 (A-427, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.811×** | -7.6 | 2e-12 | 16/33 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.753×** | -7.2 | 3e-11 | 22/34 (NCI-H460, C32, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.757×** | -7.1 | 7e-11 | 20/33 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.775×** | -6.3 | 2e-08 | 25/35 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.771×** | -6.1 | 4e-08 | 21/31 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.802×** | -5.6 | 8e-07 | 19/33 (HS-578T, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.796×** | -5.6 | 8e-07 | 19/32 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.813×** | -5.3 | 5e-06 | 17/33 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.872× | -4.9 | 3e-05 | 13/33 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.819×** | -4.7 | 7e-05 | 12/33 (BT-474, C32, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.704×** | -4.7 | 7e-05 | 17/34 (A-427, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.707×** | -4.6 | 9e-05 | 14/33 (C-33 A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.835× | -4.6 | 1e-04 | 10/32 (HOP62, C32, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.865× | -4.4 | 2e-04 | 13/33 (HOP62, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.731×** | -4.2 | 6e-04 | 12/32 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.734×** | -4.1 | 8e-04 | 12/33 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4398. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1,411 | 0 | 30 (21 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0922× (z -45.4) |
| [[MIA PaCa-2 (line)]] | alt | 843 | 0 | 16 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0947× (z -31.4) |
| [[HOP62 (line)]] | alt | 605 | 0 | 15 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -18.9) |
| [[C32 (line)]] | wt | 371 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -17.2) |
| [[NCI-H2030 (line)]] | alt | 373 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -21.8) |
| [[LOX-IMVI (line)]] | wt | 445 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -18.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -17.6) |
| [[SW 900 (line)]] | alt | 417 | 1 (1 ⚠) | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -15.3) |
| [[HS-578T (line)]] | alt | 227 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -22.0) |
| [[hTERT-HPNE (line)]] | wt | 283 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -12.9) |
| [[A498 (line)]] | wt | 166 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +14.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 172 | 2 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -11.5) |
| [[LoVo (line)]] | wt | 63.5 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.05 µM 2.55× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.30× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 300 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -18.7) |
| [[PANC-1 (line)]] | alt | 232 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 243 | 2 (2 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 2.56× (z +10.4) ⚠ cell-cycle shift, explains ~13% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -15.8) |
| [[SW480 (line)]] | alt | 135 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.63× (z +10.2) | [[Docetaxel (drug)]] 0.05 µM 0.516× (z -9.5) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 217 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -14.2) |
| [[A-427 (line)]] | wt | 153 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -25.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.648× (z -9.4) |
| [[BT-474 (line)]] | alt | 100 | 0 | 3 (1 ⚠) | — | [[Neratinib (drug)]] 0.05 µM 0.241× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 128 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -14.8) |
| [[SK-MEL-2 (line)]] | alt | 148 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.532× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 235 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -10.2) |
| [[SNU-1 (line)]] | wt | 81.4 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.239× (z -12.1) |
| [[C-33 A (line)]] | alt | 123 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.215× (z -8.7) |
| [[CHP-212 (line)]] | wt | 280 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -9.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[H4 (line)]] | wt | 214 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.344× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 148 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0760× (z -9.0) |
| [[A549 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.4 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 57.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 39.8 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 50.6 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 58.4 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 16.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 44.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 291 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.5 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 40.9 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 35.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.7 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 23.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4398), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX1A]] | +0.58 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[CDH13]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[AKT3]] | +0.55 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[VEGFC]] | +0.55 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ZEB1]] | +0.54 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[LRRC8C]] | +0.53 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[MTSS1]] | +0.52 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[INHBA]] | +0.52 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[SHC4]] | +0.51 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[MARCHF3]] | +0.51 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[KCNN4]] | +0.51 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[HS3ST3A1]] | +0.51 | +0.55 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR3C]] | -0.47 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[SEC16B]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[FAM53B]] ⚠ | -0.43 | -0.35 / -0.34 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[DERA]] | -0.43 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[NAXD]] | -0.42 | -0.24 / -0.38 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 5, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BRSK1]] | B | BRSK1 activity raises RASSF8's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 4.16× lower at baseline in the lines without BRSK1 | 0.015 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[CDH13]] | B | CDH13 activity raises RASSF8's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 3.16× lower at baseline in the lines without CDH13 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[HS3ST3A1]] | B | HS3ST3A1 activity raises RASSF8's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 3.21× lower at baseline in the lines without HS3ST3A1 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[TOP2A]] | B | TOP2A activity raises RASSF8's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GRAMD1B]] | B | GRAMD1B activity raises RASSF8's level | lines that do not express GRAMD1B (31) vs lines expressing it (19) | 3.09× lower at baseline in the lines without GRAMD1B | 0.097 | ⚠ within organs, on part of the lines; also absent: MAGEB2, CD38, ENSG00000253503 |
| [[RASSF8-AS1]] | C | RASSF8-AS1 activity raises RASSF8's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 5.98× lower at baseline in the lines without RASSF8-AS1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804; co-absent with the target |
| [[TTC7B]] | C | TTC7B activity raises RASSF8's level | lines that do not express TTC7B (9) vs lines expressing it (41) | 5.51× lower at baseline in the lines without TTC7B | 0.008 | ⚠ within organs, on part of the lines; also absent: SYNGR1, HDGFL3, HLTF; co-absent with the target |
| [[MMP17]] | C | MMP17 activity raises RASSF8's level | lines that do not express MMP17 (17) vs lines expressing it (33) | 3.86× lower at baseline in the lines without MMP17 | 0.015 | ⚠ within organs, on part of the lines; also absent: NOVA2, TUB, RIMKLB; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises RASSF8's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 3.36× lower at baseline in the lines without SPOCK1 | 0.025 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[FSD1L]] | C | FSD1L activity raises RASSF8's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 7.31× lower at baseline in the lines without FSD1L | 0.039 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[VEGFC]] | C | VEGFC activity raises RASSF8's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 3.70× lower at baseline in the lines without VEGFC | 0.066 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 9, C 7. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSHZ3]] | B | RASSF8 activity raises TSHZ3's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 5.77× lower at baseline in the lines without RASSF8 | 0.037 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1 |
| [[FAM53B]] | B | RASSF8 activity raises FAM53B's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 1.09× lower at baseline in the lines without RASSF8 | 0.037 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1 |
| [[LRRC8C]] | B | RASSF8 activity raises LRRC8C's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 2.69× lower at baseline in the lines without RASSF8 | 0.049 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1 |
| [[TMEM255B]] | B | RASSF8 activity raises TMEM255B's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 3.12× lower at baseline in the lines without RASSF8 | 0.058 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1 |
| [[ZEB1]] | B | RASSF8 activity raises ZEB1's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 2.87× lower at baseline in the lines without RASSF8 | 0.061 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1 |
| [[PPFIBP1]] | B | RASSF8 activity raises PPFIBP1's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 1.41× lower at baseline in the lines without RASSF8 | 0.065 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1 |
| [[CDYL2]] | B | RASSF8 activity raises CDYL2's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 1.79× lower at baseline in the lines without RASSF8 | 0.071 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1 |
| cells under [[Pitavastatin (Calcium) (drug)]] 5 µM | B | RASSF8 activity lowers the cells' numbers under Pitavastatin (Calcium) 5 µM (makes them more sensitive) | lines that do not express RASSF8 (15) vs lines expressing it (33) | the lines without RASSF8: 1.30× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1 |
| [[PDE10A]] | B | RASSF8 activity raises PDE10A's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 3.87× lower at baseline in the lines without RASSF8 | 0.090 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1 |
| [[RASSF8-AS1]] | C | RASSF8 activity raises RASSF8-AS1's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 5.48× lower at baseline in the lines without RASSF8 | 1e-05 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1; co-absent with the target |
| [[MMP17]] | C | RASSF8 activity raises MMP17's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 2.98× lower at baseline in the lines without RASSF8 | 0.003 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1; co-absent with the target |
| [[TTC7B]] | C | RASSF8 activity raises TTC7B's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 4.09× lower at baseline in the lines without RASSF8 | 0.004 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1; co-absent with the target |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.544). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.3, 14.7); signed map (20.0, 49.4). **Vector** length 118, 34.0% of its response variance represented; |z| ≥ 3 in 1,296 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +6.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +5.7 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.2 | +1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.0 | +7.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +4.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +6.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +2.4 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | -5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -5.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.1 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -12.4 |

## What is on record

|  |  |
|---|---|
| Name | Ras association domain family member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:25,958,232-26,079,892 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HoJ-1; previously C12orf2 |
| Gene groups (HGNC) | Ras association domain family |
| Matched by | ensembl_id |

UniProt [Q8NHQ8](https://www.uniprot.org/uniprotkb/Q8NHQ8) carries no function annotation.

**Summary**, from NCBI Gene [11228](https://www.ncbi.nlm.nih.gov/gene/11228):

> This gene encodes a member of the Ras-assocation domain family (RASSF) of tumor suppressor proteins. This gene is essential for maintaining adherens junction function in epithelial cells and has a role in epithelial cell migration. It is a lung tumor suppressor gene candidate. A chromosomal translocation t(12;22)(p11.2;q13.3) leading to the fusion of this gene and the FBLN1 gene is found in a complex type of synpolydactyly. Multiple alternatively spliced transcript variants encoding different …

**Accessions** — [HGNC:13232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13232) · Entrez [11228](https://www.ncbi.nlm.nih.gov/gene/11228) · UniProt [Q8NHQ8](https://www.uniprot.org/uniprotkb/Q8NHQ8) · Ensembl [ENSG00000123094](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123094)

## Data

Gene col 4398: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4398); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4398, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4398]; `tensor/DDL_lfc|DDL_z.npy` [4398]; `embed/gene_vectors.npy` [4398]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4398 or target_col == 4398). Every well: [[RASSF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASSF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
