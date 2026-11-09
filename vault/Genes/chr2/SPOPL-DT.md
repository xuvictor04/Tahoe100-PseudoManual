---
symbol: "SPOPL-DT"
type: "gene"
col: 13622
ensembl_id: "ENSG00000228043"
name: "SPOPL divergent transcript"
location: "2q22.1"
module: 5
arm: "+"
pooled_cpm: 26.49
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 15
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SPOPL-DT

*SPOPL divergent transcript* — 2q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +8.3, q 5e-14, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.337× (z -11.4, q 1e-27, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENOX2]] (+0.78, fdr 7e-06), [[PRMT3]] (+0.71, fdr 7e-06), [[PRDM5]] (+0.69, fdr 1e-05); moves opposite to [[DBP]] (-0.64, fdr 1e-05), [[RAB3A]] (-0.63, fdr 1e-04), [[TBC1D17]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13622.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +8.3 | 5e-14 | 35/46 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +7.7 | 3e-12 | 33/46 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.78×** | +6.1 | 2e-07 | 34/46 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.53×** | +4.3 | 0.002 | 24/46 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.50×** | +4.3 | 0.002 | 24/46 (HEC-1-A, AsPC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.004 | 23/47 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.015 | 19/47 (CFPAC-1, A-427, …) | rises with dose |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.088 | 8/47 (A498, A-427, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 1.34× | +3.1 | 0.14 | 15/46 (PANC-1, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13622.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.337×** | -11.4 | 1e-27 | 42/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.345×** | -11.2 | 1e-26 | 38/46 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.532×** | -9.4 | 1e-18 | 32/46 (NCI-H460, MIA PaCa-2, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.405×** | -9.1 | 8e-18 | 31/45 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.218×** | -8.4 | 6e-15 | 36/47 (PANC-1, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.222×** | -8.3 | 1e-14 | 35/45 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.459×** | -7.9 | 3e-13 | 31/45 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.496×** | -7.4 | 1e-11 | 32/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.537×** | -6.6 | 4e-09 | 32/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.636×** | -4.8 | 1e-04 | 31/47 (NCI-H2030, AN3 CA, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.647×** | -4.6 | 2e-04 | 25/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.662×** | -4.3 | 7e-04 | 21/40 (A-427, NCI-H23, …) | inconsistent across doses | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.656×** | -4.2 | 0.001 | 24/47 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.472×** | -4.1 | 0.001 | 29/44 (NCI-H460, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.557×** | -3.2 | 0.048 | 17/28 (HEC-1-A, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.69 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13622. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 35.0 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -23.4) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.133× (z -15.2) |
| [[PANC-1 (line)]] | alt | 52.7 | 0 | 12 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0934× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -19.4) |
| [[A-427 (line)]] | wt | 56.5 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0415× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 38.7 | 1 | 8 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -13.9) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.103× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 55.6 | 0 | 8 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.115× (z -15.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -11.9) |
| [[SW480 (line)]] | alt | 25.4 | 1 | 5 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -14.1) |
| [[A-172 (line)]] | wt | 23.7 | 3 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +19.9) ⚠ cell-cycle shift, explains ~71% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -9.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 26.4 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -17.7) ⚠ cell-cycle shift, explains ~71% of this change |
| [[J82 (line)]] | alt | 27.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -11.9) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 27.4 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0475× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 33.1 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0755× (z -22.8) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0266× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 38.9 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.113× (z -14.4) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.0556× (z -10.4) |
| [[A498 (line)]] | wt | 32.2 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -16.6) ⚠ cell-cycle shift, explains ~71% of this change |
| [[LoVo (line)]] | wt | 15.6 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.117× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 14.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -13.2) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -9.7) |
| [[SW48 (line)]] | wt | 26.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -10.7) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.112× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 42.8 | 0 | 2 (1 ⚠) | — | [[Decitabine (drug)]] 0.5 µM 0.137× (z -11.2) |
| [[HOP62 (line)]] | alt | 16.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0233× (z -21.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 33.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.127× (z -13.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 21.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.109× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 16.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.204× (z -8.8) |
| [[RKO (line)]] | wt | 26.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -11.8) ⚠ cell-cycle shift, explains ~71% of this change |
| [[SW1417 (line)]] | alt | 25.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -10.8) ⚠ cell-cycle shift, explains ~71% of this change |
| [[C32 (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -8.7) ⚠ cell-cycle shift, explains ~71% of this change |
| [[KATO III (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.226× (z -9.0) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.127× (z -9.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 9.34 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0617× (z -11.0) |
| [[SNU-1 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0846× (z -9.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 37.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0392× (z -9.0) |
| [[AN3 CA (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13622), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOX2]] | +0.78 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[PRMT3]] | +0.71 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[PRDM5]] | +0.69 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[GABPB1-AS1]] | +0.67 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[IRAK1]] | +0.67 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | +0.66 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[EPM2A]] | +0.66 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[E2F3]] | +0.65 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[ATR]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[ALG8]] | +0.64 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[NUP50-DT]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 | same gene group |
| [[BEND3]] | +0.63 | +0.52 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DBP]] | -0.64 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[RAB3A]] | -0.63 | -0.64 / -0.36 | both halves | 1e-04 |  |
| [[TBC1D17]] | -0.62 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[MAPK3]] | -0.61 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[CAT]] | -0.61 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ALAD]] | -0.61 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[PNKD]] | -0.60 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[BAD]] | -0.59 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[SLC25A23]] | -0.58 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[GALM]] | -0.57 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[PLEKHH3]] | -0.57 | -0.58 / -0.37 | both halves | 7e-05 |  |
| [[BAZ2A]] | -0.56 | -0.60 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SPOPL-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers SPOPL-DT's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.675). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (8.0, -7.1); signed map (1.2, -51.4). **Vector** length 93.2, 25.0% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.0 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +1.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -4.5 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -4.3 | -9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | +1.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.8 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -8.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.3 | -1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | SPOPL divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q22.1 — chr2:138,418,284-138,501,698 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55802](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55802) · Entrez [105373637](https://www.ncbi.nlm.nih.gov/gene/105373637) · Ensembl [ENSG00000228043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228043)

## Data

Gene col 13622: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13622); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13622, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13622]; `tensor/DDL_lfc|DDL_z.npy` [13622]; `embed/gene_vectors.npy` [13622]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13622 or target_col == 13622). Every well: [[SPOPL-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPOPL-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
