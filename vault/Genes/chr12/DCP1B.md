---
symbol: "DCP1B"
type: "gene"
col: 7481
ensembl_id: "ENSG00000151065"
name: "decapping mRNA 1B"
location: "12p13.33"
module: 62
arm: "+"
pooled_cpm: 22.33
n_lines_expressing: 47
n_dd_up: 8
n_dd_down: 24
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# DCP1B

*decapping mRNA 1B* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.83× (z +6.9, q 4e-09, up in 28 of 39 measured lines) ⚠ toxic. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.72× (z +6.4, q 3e-08, up in 32 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (16 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.282× (z -15.0, q 0e+00, down in 42 of 45 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.339× (z -11.7, q 2e-29, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MDM2]] (+0.74, fdr 7e-06), [[ANKRA2]] (+0.73, fdr 7e-06), [[EDA2R]] (+0.69, fdr 1e-05); moves opposite to [[CAPZB]] (-0.59, fdr 1e-05), [[DIAPH1]] (-0.56, fdr 3e-05), [[EML4]] (-0.54, fdr 4e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[THBS4]] → it (grade B ⚠); 6 go from it, the strongest it → [[ACAD11]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7481.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +6.9 | 4e-09 | 28/39 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.72×** | +6.4 | 3e-08 | 32/45 (LoVo, H4, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.48×** | +6.4 | 3e-08 | 28/45 (A498, RKO, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +5.1 | 5e-05 | 24/45 (A-427, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.34×** | +3.5 | 0.049 | 19/45 (A549, SNU-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.049 | 17/44 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.34×** | +3.4 | 0.054 | 17/44 (LoVo, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.056 | 17/44 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.30× | +3.1 | 0.12 | 12/45 (KATO III, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 17 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7481.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.282×** | -15.0 | 0e+00 | 42/45 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.312×** | -13.8 | 7e-41 | 39/44 (H4, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.339×** | -11.7 | 2e-29 | 41/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.466×** | -9.1 | 2e-17 | 40/45 (H4, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.434×** | -9.1 | 2e-17 | 38/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.459×** | -8.9 | 6e-17 | 32/40 (hTERT-HPNE, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.515×** | -7.9 | 3e-13 | 37/45 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.499×** | -7.5 | 3e-12 | 36/45 (LoVo, H4, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **0.534×** | -7.5 | 6e-12 | 29/40 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.527×** | -7.3 | 2e-11 | 22/30 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.544×** | -7.2 | 2e-11 | 34/45 (C32, SNU-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.533×** | -6.8 | 4e-10 | 32/45 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.613×** | -5.8 | 3e-07 | 25/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.410×** | -5.5 | 1e-06 | 29/45 (SK-MEL-2, SNU-423, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.622×** | -5.2 | 7e-06 | 19/34 (hTERT-HPNE, SW480, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.516×** | -4.1 | 0.001 | 22/43 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.711×** | -3.8 | 0.004 | 20/44 (RPMI-7951, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.689×** | -3.2 | 0.040 | 16/44 (HCT15, H4, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.714×** | -2.9 | 0.094 | 12/45 (SW 1271, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7481. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 39.2 | 0 | 11 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0503× (z -24.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.137× (z -15.1) |
| [[H4 (line)]] | wt | 75.4 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0162× (z -26.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.184× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 28.6 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.237× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 34.5 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0662× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[NCI-H460 (line)]] | wt | 26.6 | 1 | 4 (4 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.204× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 13.4 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0737× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.146× (z -12.2) |
| [[A-427 (line)]] | wt | 24.2 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.68× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.0829× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HOP62 (line)]] | alt | 40.3 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 49.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.270× (z -9.5) |
| [[LS 180 (line)]] | wt | 39.0 | 1 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0232× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[SNU-1 (line)]] | wt | 31.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0884× (z -11.3) |
| [[C32 (line)]] | wt | 28.4 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.119× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.187× (z -9.8) |
| [[SNU-423 (line)]] | alt | 19.3 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -11.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[COLO 205 (line)]] | alt | 16.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0811× (z -10.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.118× (z -9.4) |
| [[HCT15 (line)]] | alt | 22.6 | 0 | 2 (1 ⚠) | — | [[Saquinavir (drug)]] 0.5 µM 0.104× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 19.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[KATO III (line)]] | alt | 20.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[LoVo (line)]] | wt | 30.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.209× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 45.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.260× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW 900 (line)]] | alt | 28.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.170× (z -9.2) |
| [[A549 (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 54.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0721× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[HepG2_C3A (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.101× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.238× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -9.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.254× (z -8.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 25.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.68× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.16 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.33 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7481), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDM2]] | +0.74 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[ANKRA2]] | +0.73 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[EDA2R]] | +0.69 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[RPS27L]] | +0.68 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[ACTA2]] | +0.68 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ZNF79]] | +0.67 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[FDXR]] | +0.67 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[FAS]] | +0.67 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[XPC]] | +0.66 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[TMEM68]] | +0.66 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[RWDD3]] | +0.66 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[SPATA18]] | +0.65 | +0.46 / +0.67 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPZB]] | -0.59 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[DIAPH1]] | -0.56 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[EML4]] | -0.54 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[PLXND1]] | -0.54 | -0.56 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS4]] | B | THBS4 activity raises DCP1B's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 2.10× lower at baseline in the lines without THBS4 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DCP1B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DRAM1]] | B | DRAM1 activity raises DCP1B's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 2.20× lower at baseline in the lines without DRAM1 | 0.043 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[FAS]] | B | FAS activity raises DCP1B's level | lines that do not express FAS (8) vs lines expressing it (42) | 1.72× lower at baseline in the lines without FAS | 0.050 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| [[TP53INP1]] | B | TP53INP1 activity raises DCP1B's level | lines that do not express TP53INP1 (7) vs lines expressing it (43) | 1.79× lower at baseline in the lines without TP53INP1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379; maybe low, not absent |
| [[TOP2B]] | B | TOP2B activity lowers DCP1B's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACAD11]] | C | DCP1B activity raises ACAD11's level | lines that do not express DCP1B (3) vs lines expressing it (47) | 2.55× lower at baseline in the lines without DCP1B | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPRASP3, DISC1, ITGA2B; maybe low, not absent; its own permutation p |
| [[ZNF197]] | C | DCP1B activity raises ZNF197's level | lines that do not express DCP1B (3) vs lines expressing it (47) | 1.81× lower at baseline in the lines without DCP1B | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPRASP3, DISC1, ITGA2B; maybe low, not absent; its own permutation p |
| [[C3orf38]] | C | DCP1B activity raises C3orf38's level | lines that do not express DCP1B (3) vs lines expressing it (47) | 1.91× lower at baseline in the lines without DCP1B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPRASP3, DISC1, ITGA2B; maybe low, not absent; its own permutation p |
| [[AMZ2P1]] | C | DCP1B activity raises AMZ2P1's level | lines that do not express DCP1B (3) vs lines expressing it (47) | 1.78× lower at baseline in the lines without DCP1B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPRASP3, DISC1, ITGA2B; maybe low, not absent; its own permutation p |
| [[TATDN3]] | C | DCP1B activity raises TATDN3's level | lines that do not express DCP1B (3) vs lines expressing it (47) | 1.60× lower at baseline in the lines without DCP1B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPRASP3, DISC1, ITGA2B; maybe low, not absent; its own permutation p |
| [[KLHL12]] | C | DCP1B activity raises KLHL12's level | lines that do not express DCP1B (3) vs lines expressing it (47) | 1.33× lower at baseline in the lines without DCP1B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPRASP3, DISC1, ITGA2B; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.738). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.5, 35.6); signed map (41.5, -24.4). **Vector** length 101, 27.4% of its response variance represented; |z| ≥ 3 in 1,267 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *p53 pathway* (hallmark, mean cos +0.52 to 26); *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.57 to 6); *apoptosis* (hallmark, mean cos +0.53 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.8 | +6.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +6.1 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | +1.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.9 | +5.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +4.0 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +6.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +1.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | +3.1 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -5.4 | -7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -5.1 | -6.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | -4.6 | -4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.8 | -3.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | -3.6 | -8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -7.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.5 | -1.9 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -1.5 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -2.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | decapping mRNA 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:1,946,053-2,004,535 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31638 |
| Gene groups (HGNC) | RNA decapping and exonuclease complex subunits |
| Reactome | 3 pathways, smallest: mRNA decay by 5' to 3' exoribonuclease; Deadenylation-dependent mRNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZD4](https://www.uniprot.org/uniprotkb/Q8IZD4) (mRNA-decapping enzyme 1B):

> May play a role in the degradation of mRNAs, both in normal mRNA turnover and in nonsense-mediated mRNA decay. May remove the 7-methyl guanine cap structure from mRNA molecules, yielding a 5'-phosphorylated mRNA fragment and 7m-GDP (By similarity).

**Summary**, from NCBI Gene [196513](https://www.ncbi.nlm.nih.gov/gene/196513):

> This gene encodes a member of a family of proteins that function in removing the 5' cap from mRNAs, which is a step in regulated mRNA decay. This protein localizes to cytoplasmic foci which are the site of mRNA breakdown and turnover. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:24451](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24451) · Entrez [196513](https://www.ncbi.nlm.nih.gov/gene/196513) · UniProt [Q8IZD4](https://www.uniprot.org/uniprotkb/Q8IZD4) · Ensembl [ENSG00000151065](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151065)

## Data

Gene col 7481: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7481); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7481, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7481]; `tensor/DDL_lfc|DDL_z.npy` [7481]; `embed/gene_vectors.npy` [7481]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7481 or target_col == 7481). Every well: [[DCP1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCP1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
