---
symbol: "SOCS6"
type: "gene"
col: 9994
ensembl_id: "ENSG00000170677"
name: "suppressor of cytokine signaling 6"
location: "18q22.2"
module: 95
arm: "+"
pooled_cpm: 49.87
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# SOCS6

*suppressor of cytokine signaling 6* — 18q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.48× (z +14.1, q 2e-42, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.177× (z -37.4, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB2]] (+0.64, fdr 3e-05), [[ZNF253]] (+0.63, fdr 1e-04), [[SIAH1]] (+0.62, fdr 3e-05); moves opposite to [[ARHGEF10]] (-0.62, fdr 3e-05), [[P4HB]] (-0.59, fdr 3e-05), [[UBA6]] (-0.58, fdr 2e-04).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LINC01909]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9994.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.48×** | +14.1 | 2e-42 | 39/49 (LoVo, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.46×** | +10.2 | 5e-22 | 35/48 (SW48, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +7.0 | 5e-10 | 28/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +5.9 | 5e-07 | 24/48 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.19× | +5.2 | 2e-05 | 20/48 (SW1417, MIA PaCa-2, …) | top dose only | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +5.1 | 3e-05 | 20/48 (NCI-H2030, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +5.1 | 3e-05 | 21/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 7e-04 | 17/48 (H4, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.21×** | +4.2 | 0.002 | 21/48 (C32, J82, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.9 | 0.005 | 17/48 (H4, PANC-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.2 | 0.071 | 10/35 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.11× | +3.1 | 0.098 | 5/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9994.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.177×** | -37.4 | 0e+00 | 48/48 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.235×** | -31.3 | 0e+00 | 47/48 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.261×** | -29.1 | 0e+00 | 48/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.523×** | -12.9 | 4e-36 | 44/48 (LS 180, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.621×** | -9.9 | 5e-21 | 27/40 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.673×** | -8.5 | 1e-15 | 31/47 (MIA PaCa-2, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.769×** | -7.9 | 3e-13 | 31/48 (SW1417, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.701×** | -7.7 | 1e-12 | 27/48 (SW48, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.606×** | -5.7 | 1e-06 | 24/48 (HepG2/C3A, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.803×** | -4.4 | 7e-04 | 20/43 (RPMI-7951, A498, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.955× | -3.3 | 0.051 | 2/49 (MIA PaCa-2, NCI-H23) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.856× | -3.2 | 0.061 | 14/48 (MIA PaCa-2, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9994. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 190 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0534× (z -30.3) |
| [[LS 180 (line)]] | wt | 105 | 2 | 7 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 6.65× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.0649× (z -33.2) |
| [[A498 (line)]] | wt | 47.7 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.106× (z -22.8) |
| [[SW1417 (line)]] | alt | 83.2 | 2 | 5 | [[PH-797804 (drug)]] 5 µM 5.76× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.161× (z -19.5) |
| [[SW480 (line)]] | alt | 22.5 | 2 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.46× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.147× (z -21.4) |
| [[HepG2_C3A (line)]] | wt | 90.6 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.95× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.0877× (z -20.9) |
| [[LoVo (line)]] | wt | 63.5 | 2 | 4 | [[TAK-901 (drug)]] 5 µM 8.11× (z +12.2) | [[Belinostat (drug)]] 5 µM 0.137× (z -22.0) |
| [[SW48 (line)]] | wt | 87.4 | 3 | 3 | [[PH-797804 (drug)]] 5 µM 20.8× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -15.1) |
| [[A549 (line)]] | wt | 66.4 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -17.7) |
| [[KATO III (line)]] | alt | 73.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0738× (z -24.5) |
| [[NCI-H2347 (line)]] | alt | 49.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.164× (z -19.6) |
| [[PANC-1 (line)]] | alt | 44.4 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.85× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.126× (z -17.8) |
| [[A-172 (line)]] | wt | 30.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.146× (z -16.2) |
| [[AsPC-1 (line)]] | alt | 51.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0992× (z -19.6) |
| [[C-33 A (line)]] | alt | 56.5 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.223× (z -13.0) |
| [[C32 (line)]] | wt | 46.6 | 2 | 2 | [[PH-797804 (drug)]] 5 µM 16.2× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.285× (z -9.3) |
| [[COLO 205 (line)]] | alt | 54.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0823× (z -19.0) |
| [[Hs 766T (line)]] | wt | 69.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0790× (z -22.6) |
| [[HT-29 (line)]] | alt | 40.9 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -16.4) |
| [[RPMI-7951 (line)]] | alt | 46.8 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0486× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0993× (z -15.8) |
| [[SHP-77 (line)]] | alt | 33.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.233× (z -11.0) |
| [[BT-474 (line)]] | alt | 45.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 29.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -15.1) |
| [[HEC-1-A (line)]] | alt | 43.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -13.8) |
| [[HOP62 (line)]] | alt | 15.0 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.193× (z -11.0) |
| [[HS-578T (line)]] | alt | 29.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -15.0) |
| [[J82 (line)]] | alt | 31.7 | 1 (1 ⚠) | 2 | [[Niclosamide (olamine) (drug)]] 5 µM 2.78× (z +8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.200× (z -14.2) |
| [[NCI-H1573 (line)]] | alt | 35.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 75.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -15.8) |
| [[NCI-H2030 (line)]] | alt | 47.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.263× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 62.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -19.6) |
| [[Panc 03.27 (line)]] | alt | 48.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -19.3) |
| [[RKO (line)]] | wt | 41.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -13.1) |
| [[SNU-423 (line)]] | alt | 34.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0487× (z -20.6) |
| [[AN3 CA (line)]] | alt | 53.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 31.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 23.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 46.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -11.3) |
| [[CHP-212 (line)]] | wt | 39.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -8.7) |
| [[H4 (line)]] | wt | 32.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.172× (z -9.8) |
| [[SNU-1 (line)]] | wt | 40.4 | 0 | 1 | — | [[Capmatinib (drug)]] 5 µM 0.0778× (z -8.8) |
| [[A-427 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9994), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB2]] | +0.64 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[ZNF253]] | +0.63 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[SIAH1]] | +0.62 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[INO80D]] | +0.62 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[POLR3C]] | +0.62 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[LINC01909]] | +0.60 | +0.41 / +0.51 | both halves | 4e-05 | ⚠ same locus (5.2 kb, same strand: neighbours can correlate without regulation) |
| [[RNF115]] | +0.60 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[PRR3]] | +0.60 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[FOXG1]] | +0.59 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[IDNK]] | +0.59 | +0.43 / +0.34 | both halves | 1e-04 |  |
| [[SMAD1]] | +0.59 | +0.47 / +0.37 | both halves | 9e-05 |  |
| [[CCNT2]] | +0.59 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[TIGD6]] | +0.59 | +0.35 / +0.40 | both halves | 1e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF10]] | -0.62 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[P4HB]] | -0.59 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[UBA6]] | -0.58 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[SEC22B]] | -0.56 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[ATG16L2]] | -0.55 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[GNAI2]] | -0.55 | -0.31 / -0.26 | both halves | 3e-04 |  |
| [[TTC3]] | -0.54 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[KIAA1328]] | -0.53 | -0.33 / -0.28 | both halves | 3e-04 |  |
| [[TMEM184B]] | -0.53 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[PRKCZ]] | -0.53 | -0.36 / -0.26 | both halves | 4e-04 |  |
| [[CDK18]] | -0.53 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[NGLY1]] | -0.53 | -0.41 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises SOCS6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises SOCS6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC01909]] | C | LINC01909's natural level strengthens SOCS6's drug response | LINC01909's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.72; direction not clear | 0.051 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01909]] | C | SOCS6's natural level strengthens LINC01909's drug response | SOCS6's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.64; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (0.8, 8.2); signed map (25.4, -18.7). **Vector** length 101, 25.6% of its response variance represented; |z| ≥ 3 in 1,160 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +10.1 | -1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +6.8 | +5.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.8 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.2 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +10.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.8 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +2.4 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.9 | -37.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.8 | -29.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.6 | -31.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.9 | -12.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.9 | -1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | suppressor of cytokine signaling 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q22.2 — chr18:70,289,045-70,330,199 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CIS4, SSI4, HSPC060, STATI4, STAI4, Cish4; previously SOCS4 |
| Gene groups (HGNC) | SH2 domain containing; Suppressors of cytokine signaling |
| Reactome | 7 pathways, smallest: Negative regulation of FLT3; Regulation of KIT signaling; FLT3 Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O14544](https://www.uniprot.org/uniprotkb/O14544) (Suppressor of cytokine signaling 6):

> SOCS family proteins form part of a classical negative feedback system that regulates cytokine signal transduction. May be a substrate recognition component of a SCF-like ECS (Elongin BC-CUL2/5-SOCS-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins (By similarity). Regulates KIT degradation by ubiquitination of the tyrosine-phosphorylated receptor.

**Summary**, from NCBI Gene [9306](https://www.ncbi.nlm.nih.gov/gene/9306):

> The protein encoded by this gene contains a SH2 domain and a CIS homolog domain. The protein thus belongs to the cytokine-induced STAT inhibitor (CIS), also known as suppressor of cytokine signaling (SOCS) or STAT-induced STAT inhibitor (SSI), protein family. CIS family members are known to be cytokine-inducible negative regulators of cytokine signaling. The expression of this gene can be induced by GM-CSF and EPO in hematopoietic cells. A high expression level of this gene was found in …

**Accessions** — [HGNC:16833](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16833) · Entrez [9306](https://www.ncbi.nlm.nih.gov/gene/9306) · UniProt [O14544](https://www.uniprot.org/uniprotkb/O14544) · Ensembl [ENSG00000170677](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170677)

## Data

Gene col 9994: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9994); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9994, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9994]; `tensor/DDL_lfc|DDL_z.npy` [9994]; `embed/gene_vectors.npy` [9994]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9994 or target_col == 9994). Every well: [[SOCS6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOCS6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
