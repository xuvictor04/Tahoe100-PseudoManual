---
symbol: "CLCN6"
type: "gene"
col: 220
ensembl_id: "ENSG00000011021"
name: "Cl-/H+ antiporter 6"
location: "1p36.22"
module: 86
arm: "+"
pooled_cpm: 33.94
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# CLCN6

*Cl-/H+ antiporter 6* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.47× (z +7.8, q 3e-12, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.618× (z -9.9, q 2e-20, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LSS]] (+0.60, fdr 1e-05), [[MVK]] (+0.59, fdr 5e-05), [[RNF185]] (+0.58, fdr 1e-05); moves opposite to [[POU2F1]] (-0.49, fdr 8e-05), [[GSTCD]] (-0.49, fdr 5e-05), [[SATB2]] (-0.44, fdr 4e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 220.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +7.8 | 3e-12 | 36/48 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | **1.41×** | +7.0 | 6e-10 | 36/48 (NCI-H23, HS-578T, …) | top dose only | position effect removed |
| [[Berbamine (drug)]] 5 µM |  | **1.35×** | +6.2 | 1e-07 | 31/49 (LS 180, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.77×** | +4.3 | 0.002 | 24/48 (Hs 766T, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.76×** | +4.3 | 0.002 | 28/47 (MIA PaCa-2, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.026 | 16/48 (HS-578T, SNU-423, …) | top dose only |  |
| [[Posaconazole (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.026 | 24/48 (CFPAC-1, J82, …) | top dose only | plate-row cell shift |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.042 | 17/48 (C-33 A, LS 180, …) | top dose only | plate-row cell shift |
| [[Auranofin (drug)]] 5 µM |  | 1.23× | +3.0 | 0.17 | 16/48 (SK-MEL-2, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 220.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.618×** | -9.9 | 2e-20 | 37/48 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.522×** | -9.1 | 3e-17 | 39/48 (H4, SW48, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.538×** | -8.7 | 9e-16 | 45/48 (A-172, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.560×** | -8.4 | 5e-15 | 36/48 (A549, LS 180, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.574×** | -7.5 | 9e-12 | 28/43 (SK-MEL-2, Panc 03.27, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **0.632×** | -6.7 | 2e-09 | 34/46 (A-427, RPMI-7951, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **0.675×** | -5.5 | 3e-06 | 23/38 (KATO III, NCI-H1573, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.680×** | -5.4 | 4e-06 | 32/46 (HepG2/C3A, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.719×** | -4.6 | 2e-04 | 24/48 (A549, LS 180, …) | all doses, flat | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.824×** | -4.0 | 0.004 | 22/48 (KATO III, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.751×** | -3.9 | 0.006 | 22/47 (SW480, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~71% of this change | **0.777×** | -3.5 | 0.019 | 22/47 (SNU-423, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.845× | -3.5 | 0.021 | 15/48 (HS-578T, NCI-H1573, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.797×** | -3.3 | 0.036 | 20/47 (SW480, A549, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~79% of this change | **0.805×** | -3.2 | 0.051 | 17/47 (NCI-H460, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.805×** | -3.2 | 0.051 | 18/48 (NCI-H1573, SW 1088, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.738×** | -3.2 | 0.051 | 18/48 (MIA PaCa-2, SNU-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.811×** | -3.1 | 0.069 | 21/47 (CFPAC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 220. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 27.2 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.158× (z -12.3) |
| [[HS-578T (line)]] | alt | 59.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 53.2 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -10.2) |
| [[A-172 (line)]] | wt | 19.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +12.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -13.2) |
| [[A-427 (line)]] | wt | 41.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[H4 (line)]] | wt | 39.5 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0346× (z -16.5) |
| [[KATO III (line)]] | alt | 31.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.108× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[MIA PaCa-2 (line)]] | alt | 40.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 23.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +20.8) | — |
| [[RKO (line)]] | wt | 38.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +13.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.144× (z -14.2) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 31.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SNU-423 (line)]] | alt | 41.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +12.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.248× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~71% of this change |
| [[AsPC-1 (line)]] | alt | 29.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 58.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -10.9) |
| [[CHP-212 (line)]] | wt | 25.0 | 0 | 1 | — | [[Larotrectinib (drug)]] 0.5 µM 0.100× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 60.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0659× (z -19.4) ⚠ toxic |
| [[HOP62 (line)]] | alt | 34.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -11.3) |
| [[Hs 766T (line)]] | wt | 42.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +17.8) | — |
| [[HT-29 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[hTERT-HPNE (line)]] | wt | 34.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -8.6) |
| [[J82 (line)]] | alt | 48.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +13.3) | — |
| [[NCI-H1573 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[NCI-H1792 (line)]] | alt | 34.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[NCI-H2347 (line)]] | alt | 25.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +11.9) | — |
| [[Panc 03.27 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW48 (line)]] | wt | 28.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0635× (z -14.4) |
| [[SW480 (line)]] | alt | 30.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.360× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 220), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSS]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[MVK]] | +0.59 | +0.68 / +0.40 | both halves | 5e-05 |  |
| [[RNF185]] | +0.58 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MMAB]] | +0.58 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[AP5Z1]] | +0.57 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[HSD17B7]] | +0.56 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[TBC1D17]] | +0.55 | +0.66 / +0.37 | both halves | 8e-05 |  |
| [[AMDHD2]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[EXOC3]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[MVD]] | +0.53 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[TP53BP1]] | +0.53 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[NAGLU]] | +0.53 | +0.44 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POU2F1]] | -0.49 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[GSTCD]] | -0.49 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[SATB2]] | -0.44 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[JADE3]] | -0.44 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[TBC1D4]] | -0.44 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[CHD7]] | -0.44 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[NECTIN3]] | -0.44 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[THSD4-AS1]] | -0.43 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[SPOPL-DT]] | -0.43 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[PKD2]] | -0.43 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[ZNRF2P1]] | -0.42 | -0.39 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CLCN6's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.515). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.9, -46.4); signed map (-54.2, 31.1). **Vector** length 101, 26.0% of its response variance represented; |z| ≥ 3 in 1,003 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +3.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +5.1 | +7.0 |
|  | [[Berbamine (drug)]] 5 µM |  | +4.3 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | +3.7 | -5.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.7 | +2.4 |
|  | [[Posaconazole (drug)]] 5 µM |  | +3.6 | +3.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -9.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | Cl-/H+ antiporter 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:11,806,096-11,848,079 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CLC-6, KIAA0046, ClC-6 |
| Gene groups (HGNC) | CLC chloride channel and transporter family |
| Reactome | 6 pathways, smallest: Signaling by BRAF and RAF1 fusions; Stimuli-sensing channels; Oncogenic MAPK signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P51797](https://www.uniprot.org/uniprotkb/P51797) (H(+)/Cl(-) exchange transporter 6):

> Voltage-gated channel mediating the exchange of chloride ions against protons. Functions as antiporter and contributes to the acidification of the late endosome lumen. The CLC channel family contains both chloride channels and proton-coupled anion transporters that exchange chloride or another anion for protons. The presence of conserved gating glutamate residues is typical for family members that function as antiporters.

**Summary**, from NCBI Gene [1185](https://www.ncbi.nlm.nih.gov/gene/1185):

> This gene encodes a member of the voltage-dependent chloride channel protein family. Members of this family can function as either chloride channels or antiporters. This protein is primarily localized to late endosomes and functions as a chloride/proton antiporter. Alternate splicing results in both coding and non-coding variants. Additional alternately spliced variants have been described but their full-length structure is unknown. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:2024](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2024) · Entrez [1185](https://www.ncbi.nlm.nih.gov/gene/1185) · UniProt [P51797](https://www.uniprot.org/uniprotkb/P51797) · Ensembl [ENSG00000011021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011021)

## Data

Gene col 220: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 220); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 220, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 220]; `tensor/DDL_lfc|DDL_z.npy` [220]; `embed/gene_vectors.npy` [220]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 220 or target_col == 220). Every well: [[CLCN6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLCN6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
