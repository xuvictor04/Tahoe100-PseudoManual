---
symbol: "XXYLT1"
type: "gene"
col: 10448
ensembl_id: "ENSG00000173950"
name: "xyloside xylosyltransferase 1"
location: "3q29"
module: 5
arm: "+"
pooled_cpm: 34.24
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# XXYLT1

*xyloside xylosyltransferase 1* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.52× (z +7.4, q 6e-11, up in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.23× (z +3.5, q 0.031, up in 9 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.478× (z -12.7, q 5e-34, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLFNL1-AS1]] (+0.68, fdr 7e-06), [[RAN]] (+0.62, fdr 1e-05), [[EEF1AKMT1]] (+0.60, fdr 7e-06); moves opposite to [[SECISBP2L]] (-0.62, fdr 7e-06), [[RAB13]] (-0.60, fdr 3e-05), [[ABCA5]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10448.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.52×** | +7.4 | 6e-11 | 28/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **1.32×** | +4.7 | 7e-04 | 22/45 (SK-MEL-2, H4, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.19× | +4.4 | 0.002 | 19/47 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.28×** | +4.2 | 0.003 | 17/47 (HepG2/C3A, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.23×** | +3.7 | 0.026 | 20/48 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.33×** | +3.6 | 0.026 | 13/47 (NCI-H1573, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.031 | 9/48 (RKO, SK-MEL-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.037 | 11/47 (HEC-1-A, HepG2/C3A, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.054 | 5/48 (LS 180, J82, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.14× | +3.3 | 0.062 | 4/48 (SNU-1, LS 180, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +3.2 | 0.066 | 15/48 (SNU-1, HEC-1-A, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.1 | 0.089 | 10/47 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.18× | +3.0 | 0.11 | 4/48 (SW480, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10448.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.478×** | -12.7 | 5e-34 | 38/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.583×** | -9.2 | 7e-18 | 35/47 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.636×** | -8.1 | 1e-13 | 29/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.640×** | -7.9 | 3e-13 | 30/46 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -6.5 | 8e-09 | 27/48 (PANC-1, J82, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.743×** | -5.3 | 1e-05 | 24/48 (J82, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.582×** | -5.0 | 4e-05 | 24/48 (MIA PaCa-2, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.586×** | -5.0 | 4e-05 | 25/46 (HCT15, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.696×** | -4.6 | 2e-04 | 21/44 (AN3 CA, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.780×** | -4.4 | 5e-04 | 21/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.777×** | -4.2 | 0.002 | 18/42 (HCT15, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.857× | -3.9 | 0.005 | 23/48 (SW1417, A549, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.719×** | -3.1 | 0.087 | 13/48 (SK-MEL-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.787×** | -3.0 | 0.087 | 14/48 (HEC-1-A, CFPAC-1, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.0 | 0.087 | 13/48 (J82, SK-MEL-2, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.840× | -3.0 | 0.099 | 13/48 (HS-578T, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10448. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.1 | 0 | 9 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.125× (z -20.8) |
| [[NCI-H1573 (line)]] | alt | 31.5 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.185× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -11.3) |
| [[PANC-1 (line)]] | alt | 44.5 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.277× (z -15.1) |
| [[BT-474 (line)]] | alt | 42.2 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.275× (z -9.0) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -8.7) |
| [[LoVo (line)]] | wt | 35.5 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.213× (z -14.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 54.8 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.257× (z -13.5) |
| [[A-427 (line)]] | wt | 50.1 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -14.4) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.222× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 40.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.353× (z -11.3) |
| [[A549 (line)]] | wt | 20.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -13.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.234× (z -10.0) |
| [[AN3 CA (line)]] | alt | 75.9 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0976× (z -11.6) |
| [[J82 (line)]] | alt | 41.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.342× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.357× (z -8.5) |
| [[LS 180 (line)]] | wt | 41.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.336× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 42.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.291× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 114 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.241× (z -17.1) |
| [[SW1417 (line)]] | alt | 37.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -13.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.300× (z -9.4) |
| [[SW480 (line)]] | alt | 52.0 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -12.1) |
| [[A498 (line)]] | wt | 21.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.248× (z -9.9) |
| [[C-33 A (line)]] | alt | 28.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.179× (z -9.8) ⚠ toxic |
| [[C32 (line)]] | wt | 58.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0969× (z -9.1) ⚠ toxic |
| [[HCT15 (line)]] | alt | 41.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -12.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 40.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 41.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.219× (z -11.3) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0841× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 25.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -8.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 18.3 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.190× (z -9.0) |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.210× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10448), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLFNL1-AS1]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[RAN]] | +0.62 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[EEF1AKMT1]] | +0.60 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[NOP2]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[MAD1L1]] | +0.60 | +0.52 / +0.64 | both halves | 1e-05 | same gene group |
| [[WDR4]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CTPS1]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[LRP8]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[PUS1]] | +0.58 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[BEND3]] | +0.58 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[EIPR1]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ADAT1]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SECISBP2L]] | -0.62 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[RAB13]] | -0.60 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[ABCA5]] | -0.59 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[KBTBD3]] | -0.59 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[PLAG1]] | -0.55 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[BAZ2A]] | -0.55 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[JAK1]] | -0.55 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[SH3GLB1]] | -0.54 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.52 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[UBE2B]] | -0.51 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[CPEB3]] | -0.51 | -0.50 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers XXYLT1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MTHFD1L]] | C | MTHFD1L activity raises XXYLT1's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 2.13× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[KIAA1549]] | C | KIAA1549 activity raises XXYLT1's level | lines that do not express KIAA1549 (4) vs lines expressing it (46) | 1.63× lower at baseline in the lines without KIAA1549 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HHAT, WHRN, GNAL; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.634). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-3.8, -36.2); signed map (1.1, -52.4). **Vector** length 90.7, 20.1% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.0 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | +2.8 | +4.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -12.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.2 | -5.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.7 | -9.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.4 | -3.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.3 | +0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | xyloside xylosyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:195,068,284-195,271,159 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35155; previously C3orf21 |
| Gene groups (HGNC) | Glycosyltransferase family 8; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBI6](https://www.uniprot.org/uniprotkb/Q8NBI6) (Xyloside xylosyltransferase 1):

> Alpha-1,3-xylosyltransferase, which elongates the O-linked xylose-glucose disaccharide attached to EGF-like repeats in the extracellular domain of target proteins by catalyzing the addition of the second xylose. Known targets include Notch proteins and coagulation factors, such as F9.

**Summary**, from NCBI Gene [152002](https://www.ncbi.nlm.nih.gov/gene/152002):

> Enables magnesium ion binding activity; manganese ion binding activity; and xylosyl alpha-1,3-xylosyltransferase activity. Involved in protein O-linked glycosylation via glucose. Located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26639](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26639) · Entrez [152002](https://www.ncbi.nlm.nih.gov/gene/152002) · UniProt [Q8NBI6](https://www.uniprot.org/uniprotkb/Q8NBI6) · Ensembl [ENSG00000173950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173950)

## Data

Gene col 10448: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10448); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10448, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10448]; `tensor/DDL_lfc|DDL_z.npy` [10448]; `embed/gene_vectors.npy` [10448]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10448 or target_col == 10448). Every well: [[XXYLT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XXYLT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
