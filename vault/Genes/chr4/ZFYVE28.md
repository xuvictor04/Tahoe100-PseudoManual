---
symbol: "ZFYVE28"
type: "gene"
col: 8274
ensembl_id: "ENSG00000159733"
name: "zinc finger FYVE-type containing 28"
location: "4p16.3"
module: 136
arm: "+"
pooled_cpm: 84.39
n_lines_expressing: 46
n_dd_up: 10
n_dd_down: 43
n_dd_up_clean: 10
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# ZFYVE28

*zinc finger FYVE-type containing 28* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.50× (z +7.6, q 2e-11, up in 34 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.274× (z -34.2, q 0e+00, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HK1]] (+0.78, fdr 7e-06), [[CSNK1E]] (+0.74, fdr 7e-06), [[RASA3]] (+0.73, fdr 7e-06); moves opposite to [[CTSO]] (-0.68, fdr 2e-05), [[AHI1-DT]] (-0.65, fdr 2e-04), [[DECR1]] (-0.65, fdr 4e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PMP22]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZNRF1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8274.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +7.6 | 2e-11 | 34/44 (LS 180, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +5.7 | 4e-06 | 30/44 (AsPC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +5.6 | 5e-06 | 28/44 (LS 180, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.2 | 2e-05 | 25/44 (LS 180, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +5.2 | 2e-05 | 24/44 (LS 180, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +5.1 | 4e-05 | 24/44 (LS 180, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +5.0 | 6e-05 | 24/45 (LS 180, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +4.2 | 0.002 | 21/45 (LS 180, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.006 | 16/44 (RKO, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.096 | 17/43 (hTERT-HPNE, SW48, …) | rises with dose | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.096 | 11/44 (SW480, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.096 | 7/45 (LOX-IMVI, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.096 | 8/44 (LoVo, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8274.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.274×** | -34.2 | 0e+00 | 42/44 (NCI-H23, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.269×** | -24.6 | 0e+00 | 43/44 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.282×** | -22.7 | 0e+00 | 42/44 (C32, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.348×** | -19.7 | 0e+00 | 37/45 (SK-MEL-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.372×** | -17.8 | 0e+00 | 40/43 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.575×** | -14.6 | 0e+00 | 34/45 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.439×** | -14.2 | 5e-44 | 33/41 (KATO III, SW48, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.484×** | -13.6 | 5e-40 | 35/44 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -13.3 | 2e-38 | 31/40 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.500×** | -12.9 | 1e-36 | 38/44 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.284×** | -12.3 | 5e-33 | 41/45 (RKO, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.546×** | -11.3 | 6e-28 | 31/44 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.535×** | -11.2 | 1e-27 | 33/44 (SK-MEL-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.544×** | -10.9 | 3e-26 | 32/43 (LoVo, C32, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.596×** | -9.3 | 6e-19 | 31/46 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.722×** | -8.6 | 3e-16 | 29/44 (C32, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.431×** | -8.2 | 7e-15 | 34/44 (SNU-1, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.773×** | -5.9 | 1e-07 | 24/44 (C32, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.744×** | -5.5 | 8e-07 | 25/44 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.746×** | -5.3 | 3e-06 | 26/44 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.597×** | -5.0 | 9e-06 | 24/44 (SK-MEL-2, C32, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8274. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 221 | 0 | 33 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -29.5) |
| [[NCI-H460 (line)]] | wt | 130 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -25.5) |
| [[LOX-IMVI (line)]] | wt | 155 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -25.1) |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -22.8) |
| [[KATO III (line)]] | alt | 125 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -22.9) |
| [[SNU-1 (line)]] | wt | 107 | 0 | 12 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.147× (z -15.8) |
| [[J82 (line)]] | alt | 62.1 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -21.6) |
| [[LoVo (line)]] | wt | 118 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.361× (z -19.0) |
| [[NCI-H23 (line)]] | alt | 72.3 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0786× (z -36.6) |
| [[RPMI-7951 (line)]] | alt | 101 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.290× (z -15.7) |
| [[SW480 (line)]] | alt | 126 | 0 | 11 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -14.5) |
| [[H4 (line)]] | wt | 212 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.200× (z -13.4) |
| [[LS 180 (line)]] | wt | 62.9 | 5 | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.00× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -16.5) |
| [[RKO (line)]] | wt | 141 | 0 | 10 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0512× (z -33.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -16.5) |
| [[SK-MEL-2 (line)]] | alt | 85.2 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -27.0) |
| [[HOP62 (line)]] | alt | 65.6 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -15.7) |
| [[Hs 766T (line)]] | wt | 93.4 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -21.3) |
| [[PANC-1 (line)]] | alt | 129 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -22.3) |
| [[SW 900 (line)]] | alt | 201 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -20.0) |
| [[C-33 A (line)]] | alt | 104 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 63.4 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0391× (z -27.3) |
| [[NCI-H1573 (line)]] | alt | 78.6 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -26.1) |
| [[NCI-H1792 (line)]] | alt | 157 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -22.3) |
| [[A498 (line)]] | wt | 43.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -19.8) |
| [[NCI-H2030 (line)]] | alt | 49.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -15.3) |
| [[A-172 (line)]] | wt | 48.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -22.6) |
| [[HS-578T (line)]] | alt | 35.4 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.177× (z -12.6) |
| [[SW48 (line)]] | wt | 89.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0829× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.310× (z -12.4) |
| [[A-427 (line)]] | wt | 48.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.57× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -12.8) |
| [[A549 (line)]] | wt | 47.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -25.7) |
| [[AsPC-1 (line)]] | alt | 46.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -22.3) |
| [[SNU-423 (line)]] | alt | 53.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -17.7) |
| [[AN3 CA (line)]] | alt | 107 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -14.2) |
| [[BT-474 (line)]] | alt | 26.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -12.5) |
| [[COLO 205 (line)]] | alt | 105 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -10.4) |
| [[HCT15 (line)]] | alt | 81.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -17.9) |
| [[hTERT-HPNE (line)]] | wt | 44.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.249× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 42.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -13.2) |
| [[SW 1271 (line)]] | alt | 150 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0481× (z -14.1) |
| [[SW1417 (line)]] | alt | 33.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -8.8) |
| [[CHP-212 (line)]] | wt | 99.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 15.5 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 18.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8274), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HK1]] | +0.78 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[CSNK1E]] | +0.74 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[RASA3]] | +0.73 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[PAQR5]] | +0.72 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[SH2B2]] | +0.70 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[HPCAL1]] | +0.69 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[MAP2K1]] | +0.69 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[NIBAN2]] | +0.69 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[FLNB]] | +0.68 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[SLC2A3]] | +0.67 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.67 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[ETV5]] | +0.66 | +0.60 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSO]] | -0.68 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[AHI1-DT]] | -0.65 | -0.65 / -0.31 | both halves | 2e-04 |  |
| [[DECR1]] | -0.65 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[NNT]] | -0.64 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ZXDA]] | -0.62 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[TAPBPL]] | -0.60 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[GAS2]] | -0.60 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[GALNT7-DT]] | -0.60 | -0.56 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[CASC9]] | -0.59 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[MED12]] | -0.59 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[ARFGAP2]] | -0.59 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[MR1]] | -0.59 | -0.61 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[EIF1B-AS1]] | -0.58 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[HFE]] | -0.58 | -0.42 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMP22]] | B | PMP22 activity raises ZFYVE28's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 2.40× lower at baseline in the lines without PMP22 | 0.030 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ZFYVE28's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers ZFYVE28's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNRF1]] | C | ZFYVE28 activity raises ZNRF1's level | lines that do not express ZFYVE28 (4) vs lines expressing it (46) | 1.80× lower at baseline in the lines without ZFYVE28 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.792). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.3, 2.4); signed map (0.8, 49.7). **Vector** length 121, 39.0% of its response variance represented; |z| ≥ 3 in 1,720 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +8.9 | +5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.8 | +7.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +7.7 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.4 | +5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.9 | +5.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.6 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | -2.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.4 | +1.2 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -7.4 | -5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.1 | -17.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -6.8 | -4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -14.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.6 | -5.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -6.1 | -3.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -5.9 | -3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger FYVE-type containing 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:2,269,582-2,418,651 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1643, lst-2 |
| Gene groups (HGNC) | Zinc fingers FYVE-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCC9](https://www.uniprot.org/uniprotkb/Q9HCC9) (Lateral signaling target protein 2 homolog):

> Negative regulator of epidermal growth factor receptor (EGFR) signaling. Acts by promoting EGFR degradation in endosomes when not monoubiquitinated.

**Summary**, from NCBI Gene [57732](https://www.ncbi.nlm.nih.gov/gene/57732):

> Enables phosphatidylinositol-3-phosphate binding activity. Involved in negative regulation of epidermal growth factor-activated receptor activity. Located in cytosol and early endosome membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29334](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29334) · Entrez [57732](https://www.ncbi.nlm.nih.gov/gene/57732) · UniProt [Q9HCC9](https://www.uniprot.org/uniprotkb/Q9HCC9) · Ensembl [ENSG00000159733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159733)

## Data

Gene col 8274: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8274); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8274, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8274]; `tensor/DDL_lfc|DDL_z.npy` [8274]; `embed/gene_vectors.npy` [8274]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8274 or target_col == 8274). Every well: [[ZFYVE28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFYVE28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
