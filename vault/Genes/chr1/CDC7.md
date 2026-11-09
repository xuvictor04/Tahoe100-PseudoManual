---
symbol: "CDC7"
type: "gene"
col: 1777
ensembl_id: "ENSG00000097046"
name: "cell division cycle 7"
location: "1p22.1"
module: 6
arm: "+"
pooled_cpm: 16.77
n_lines_expressing: 48
n_dd_up: 30
n_dd_down: 34
n_dd_up_clean: 9
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CDC7

*cell division cycle 7* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (21 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.09× (z +14.9, q 0e+00, up in 19 of 24 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.56× (z +8.3, q 5e-15, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.577× (z -7.6, q 2e-11, down in 25 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXO1]] (+0.85, fdr 7e-06), [[WDR76]] (+0.84, fdr 7e-06), [[E2F8]] (+0.83, fdr 7e-06); moves opposite to [[ATP6V1G1]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 23 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1777.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **3.09×** | +14.9 | 0e+00 | 19/24 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **2.56×** | +12.9 | 1e-35 | 31/39 (HepG2/C3A, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **2.07×** | +9.6 | 2e-19 | 32/41 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.96×** | +9.3 | 2e-18 | 31/45 (HepG2/C3A, LoVo, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.92×** | +9.0 | 3e-17 | 27/45 (NCI-H1573, A498, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.91×** | +8.9 | 4e-17 | 31/45 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.91×** | +8.9 | 4e-17 | 27/45 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +8.3 | 5e-15 | 37/46 (SHP-77, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **1.92×** | +8.3 | 6e-15 | 20/32 (HepG2/C3A, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.81×** | +8.1 | 2e-14 | 27/45 (SW480, LoVo, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +6.1 | 5e-08 | 23/45 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +5.1 | 2e-05 | 17/44 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +4.0 | 0.002 | 18/44 (PANC-1, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.23×** | +4.0 | 0.002 | 19/45 (NCI-H1792, CFPAC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.01×** | +4.0 | 0.002 | 4/46 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.84×** | +3.5 | 0.013 | 6/43 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.013 | 15/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.022 | 7/46 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.024 | 7/42 (SW1417, C32, …) | all doses, flat | low cells (technical?) |
| [[Busulfan (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.057 | 2/45 (Hs 766T, NCI-H1792) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +2.9 | 0.070 | 7/45 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1777.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.577×** | -7.6 | 2e-11 | 25/44 (SW48, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.588×** | -6.9 | 2e-09 | 26/44 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.699×** | -6.5 | 1e-08 | 26/46 (SNU-1, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.670×** | -5.5 | 5e-06 | 22/45 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.676×** | -5.2 | 3e-05 | 18/45 (NCI-H2030, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.764×** | -5.1 | 4e-05 | 23/44 (A-427, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.693×** | -5.0 | 4e-05 | 24/45 (H4, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.763×** | -5.0 | 4e-05 | 23/46 (HCT15, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.694×** | -4.7 | 1e-04 | 23/46 (HS-578T, Panc 03.27, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.782×** | -4.5 | 3e-04 | 21/46 (KATO III, A-427, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.729×** | -4.3 | 8e-04 | 20/43 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.644×** | -4.3 | 8e-04 | 16/46 (SW480, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.801×** | -4.2 | 0.001 | 16/46 (KATO III, HCT15, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.739×** | -4.1 | 0.001 | 15/45 (RKO, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.742×** | -4.1 | 0.002 | 21/45 (C32, C-33 A, …) | top dose only |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.659×** | -4.1 | 0.002 | 13/46 (HEC-1-A, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.744×** | -4.1 | 0.002 | 13/45 (SK-MEL-2, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.757×** | -3.8 | 0.004 | 10/46 (AN3 CA, KATO III, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.772×** | -3.6 | 0.010 | 16/45 (HEC-1-A, SK-MEL-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.552×** | -3.4 | 0.017 | 13/45 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.555×** | -3.4 | 0.018 | 14/43 (A-427, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | **0.777×** | -3.3 | 0.021 | 15/45 (Hs 766T, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.11 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1777. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 84.5 | 7 (6 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 19.8× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 12.2× (z +12.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.147× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~48% of this change |
| [[A-427 (line)]] | wt | 42.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -14.9) |
| [[C-33 A (line)]] | alt | 82.5 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.376× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 34.9 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.270× (z -9.4) |
| [[PANC-1 (line)]] | alt | 28.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.77× (z +9.0) ⚠ toxic; cell-cycle shift, explains ~48% of this change | [[Bortezomib (drug)]] 0.05 µM 0.356× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 21.9 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.193× (z -10.3) |
| [[SW480 (line)]] | alt | 24.8 | 1 (1 ⚠) | 1 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.69× (z +11.1) ⚠ toxic; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.3) |
| [[A498 (line)]] | wt | 8.43 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.195× (z -10.1) ⚠ cell-cycle shift, explains ~56% of this change |
| [[C32 (line)]] | wt | 26.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.169× (z -10.7) |
| [[H4 (line)]] | wt | 9.41 | 0 | 1 | — | [[Entrectinib (drug)]] 5 µM 0.0489× (z -9.8) |
| [[HCT15 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.136× (z -11.5) ⚠ cell-cycle shift, explains ~56% of this change |
| [[J82 (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 6.37 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[NCI-H460 (line)]] | wt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.13× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[A-172 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.94 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1777), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXO1]] | +0.85 | +0.80 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 692 |
| [[WDR76]] | +0.84 | +0.79 / +0.83 | both halves | 7e-06 |  |
| [[E2F8]] | +0.83 | +0.83 / +0.81 | both halves | 7e-06 |  |
| [[MCM10]] | +0.83 | +0.79 / +0.84 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 989 |
| [[GINS1]] | +0.82 | +0.79 / +0.81 | both halves | 7e-06 | pathway: DNA Replication; STRING 510 |
| [[UHRF1]] | +0.82 | +0.80 / +0.79 | both halves | 7e-06 |  |
| [[HELLS]] | +0.82 | +0.81 / +0.81 | both halves | 7e-06 |  |
| [[DTL]] | +0.82 | +0.80 / +0.82 | both halves | 7e-06 | STRING 578 |
| [[WDHD1]] | +0.81 | +0.78 / +0.82 | both halves | 7e-06 | STRING 794 |
| [[DSCC1]] | +0.81 | +0.75 / +0.82 | both halves | 7e-06 |  |
| [[CLSPN]] | +0.81 | +0.76 / +0.81 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 940 |
| [[E2F2]] | +0.81 | +0.80 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1G1]] | -0.67 | -0.59 / -0.69 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CDC7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity lowers CDC7's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CDC25A]] | B | CDC25A activity raises CDC7's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.61× lower at baseline in the lines without CDC25A | 0.087 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[BRME1]] | C | BRME1 activity raises CDC7's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 2.77× lower at baseline in the lines without BRME1 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.850). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.2, -44.1); signed map (-36.8, -44.7). **Vector** length 110, 28.4% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.63 to 65); *DNA strand elongation* (reactome, mean cos +0.67 to 28); *E2F G1/S* (control, mean cos +0.65 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +6.2 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +8.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | +3.4 | +9.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.3 | +1.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.1 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +1.8 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.0 | -6.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -5.0 | -5.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -4.6 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -4.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.7 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -4.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:91,500,851-91,525,764 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Hsk1, huCdc7, HsCdc7; previously CDC7L1 |
| Gene groups (HGNC) | CDC7 kinase family |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 11 pathways, smallest: Activation of the pre-replicative complex; Transcriptional Regulation by E2F6; Activation of ATR in response to replication stress |
| Matched by | ensembl_id |

**Function**, from UniProt [O00311](https://www.uniprot.org/uniprotkb/O00311) (Cell division cycle 7-related protein kinase):

> Kinase involved in initiation of DNA replication. Phosphorylates critical substrates that regulate the G1/S phase transition and initiation of DNA replication, such as MCM proteins and CLASPIN.

**Summary**, from NCBI Gene [8317](https://www.ncbi.nlm.nih.gov/gene/8317):

> This gene encodes a cell division cycle protein with kinase activity that is critical for the G1/S transition. The yeast homolog is also essential for initiation of DNA replication as cell division occurs. Overexpression of this gene product may be associated with neoplastic transformation for some tumors. Multiple alternatively spliced transcript variants that encode the same protein have been detected. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:1745](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1745) · Entrez [8317](https://www.ncbi.nlm.nih.gov/gene/8317) · UniProt [O00311](https://www.uniprot.org/uniprotkb/O00311) · Ensembl [ENSG00000097046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000097046)

## Data

Gene col 1777: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1777); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1777, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1777]; `tensor/DDL_lfc|DDL_z.npy` [1777]; `embed/gene_vectors.npy` [1777]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1777 or target_col == 1777). Every well: [[CDC7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
