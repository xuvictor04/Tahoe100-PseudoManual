---
symbol: "REPS1"
type: "gene"
col: 5727
ensembl_id: "ENSG00000135597"
name: "RALBP1 associated Eps domain containing 1"
location: "6q24.1"
module: 65
arm: "+"
pooled_cpm: 96.98
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# REPS1

*RALBP1 associated Eps domain containing 1* — 6q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.34× (z +5.1, q 2e-04, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.439× (z -14.4, q 6e-44, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.608× (z -12.2, q 3e-32, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAMK2G]] (+0.70, fdr 1e-05), [[PRMT9]] (+0.69, fdr 7e-06), [[WASF3]] (+0.68, fdr 4e-05); moves opposite to [[LINC01004]] (-0.68, fdr 1e-05), [[ATXN1L]] (-0.66, fdr 1e-05), [[AKT1S1]] (-0.66, fdr 4e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5727.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +5.1 | 2e-04 | 29/48 (SNU-423, H4, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +4.8 | 4e-04 | 28/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.27×** | +4.0 | 0.011 | 27/48 (SNU-423, MIA PaCa-2, …) | all doses, flat |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.088 | 22/48 (NCI-H1573, SW48, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.14× | +3.4 | 0.088 | 11/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | 1.42× | +3.2 | 0.12 | 22/49 (C32, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | 1.39× | +3.0 | 0.18 | 16/49 (HepG2/C3A, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.20× | +3.0 | 0.18 | 20/47 (LoVo, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5727.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.439×** | -14.4 | 6e-44 | 45/49 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.466×** | -12.8 | 5e-35 | 40/44 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.608×** | -12.2 | 3e-32 | 42/49 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.491×** | -11.5 | 3e-28 | 35/45 (SK-MEL-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.649×** | -7.5 | 6e-12 | 35/48 (LoVo, SW1417, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.696×** | -6.3 | 3e-08 | 32/48 (RPMI-7951, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -6.0 | 2e-07 | 36/48 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -5.5 | 2e-06 | 30/50 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.831×** | -4.5 | 4e-04 | 25/48 (A-172, NCI-H2347, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -4.0 | 0.004 | 0/50 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.1 | 0.090 | 18/48 (NCI-H2347, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5727. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 109 | 2 | 4 (3 ⚠) | [[Ponatinib (drug)]] 5 µM 2.41× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 131 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -18.5) |
| [[LoVo (line)]] | wt | 120 | 2 (2 ⚠) | 3 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.33× (z +10.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.306× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.447× (z -10.3) |
| [[A-172 (line)]] | wt | 69.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -11.8) |
| [[AN3 CA (line)]] | alt | 168 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -12.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 78.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 112 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.37× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -12.7) |
| [[NCI-H2030 (line)]] | alt | 130 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -8.6) |
| [[SW1417 (line)]] | alt | 164 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -10.3) |
| [[A-427 (line)]] | wt | 88.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -12.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 69.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -10.4) |
| [[LS 180 (line)]] | wt | 175 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 117 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -11.1) |
| [[SW48 (line)]] | wt | 162 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.38× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -17.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 66.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -21.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 85.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -11.1) |
| [[J82 (line)]] | alt | 56.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 91.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -8.7) ⚠ cell-cycle shift, explains ~86% of this change |
| [[NCI-H460 (line)]] | wt | 117 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -13.7) |
| [[PANC-1 (line)]] | alt | 77.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.479× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.627× (z -9.0) |
| [[RKO (line)]] | wt | 120 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 78.8 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.204× (z -13.7) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 165 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 94.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0435× (z -27.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 98.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -10.7) |
| [[SW 900 (line)]] | alt | 98.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -10.7) |
| [[SW480 (line)]] | alt | 121 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -13.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 46.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -14.6) |
| [[BT-474 (line)]] | alt | 70.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -11.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -9.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 83.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.342× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 65.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0952× (z -17.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 69.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.273× (z -10.1) ⚠ transcription drop |
| [[HCT15 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -10.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 68.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -9.0) |
| [[KATO III (line)]] | alt | 92.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 88.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 65.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -8.7) |
| [[SNU-1 (line)]] | wt | 132 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.381× (z -8.9) ⚠ cell-cycle shift, explains ~20% of this change |
| [[SW 1271 (line)]] | alt | 94.3 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.1000× (z -10.7) |
| [[A498 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 90.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5727), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMK2G]] | +0.70 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[PRMT9]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[WASF3]] | +0.68 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[MBD2]] | +0.68 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[RSAD1]] | +0.68 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[THYN1]] | +0.66 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[ARL6]] | +0.66 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[SERAC1]] | +0.66 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ATG4C]] | +0.66 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[KIF3A]] | +0.66 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.65 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[CROT]] | +0.65 | +0.50 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01004]] | -0.68 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[ATXN1L]] | -0.66 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[AKT1S1]] | -0.66 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[C1S]] | -0.65 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[KDM6B]] | -0.62 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | -0.62 | -0.63 / -0.39 | both halves | 6e-05 |  |
| [[ERCC6L2]] | -0.61 | -0.74 / -0.27 | both halves | 3e-04 |  |
| [[LINC00571]] | -0.61 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[GTF2H1]] | -0.60 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[MIRLET7IHG]] | -0.60 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[CFAP53]] | -0.60 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[GGPS1]] | -0.59 | -0.57 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises REPS1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers REPS1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ARHGAP44]] | B | ARHGAP44 activity raises REPS1's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 1.28× lower at baseline in the lines without ARHGAP44 | 0.060 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[LRP3]] | B | LRP3 activity raises REPS1's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.20× lower at baseline in the lines without LRP3 | 0.062 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[TOP2B]] | B | TOP2B activity raises REPS1's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[MIRLET7IHG]] | C | MIRLET7IHG's natural level weakens REPS1's drug response | MIRLET7IHG's natural level across 50 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.54; direction not clear | 0.050 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HACE1]] | C | HACE1 activity raises REPS1's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.56× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-2.7, -9.3); signed map (-30.7, -10.9). **Vector** length 106, 31.1% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.0 | +2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +2.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | -1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -12.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -0.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | +0.2 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | RALBP1 associated Eps domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.1 — chr6:138,903,493-138,988,261 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | EF-hand domain containing |
| Reactome | 4 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96D71](https://www.uniprot.org/uniprotkb/Q96D71) (RalBP1-associated Eps domain-containing protein 1):

> May coordinate the cellular actions of activated EGF receptors and Ral-GTPases.

**Summary**, from NCBI Gene [85021](https://www.ncbi.nlm.nih.gov/gene/85021):

> This gene encodes a signaling adaptor protein with two EH domains that interacts with proteins that participate in signaling, endocytosis and cytoskeletal changes. The encoded protein has been found in association with intersectin 1 and Src homology 3-domain growth factor receptor-bound 2-like (endophilin) interacting protein 1 when intersectin 1 was isolated from clathrin-coated pits. The encoded protein has also been shown to interact with amphiphysin, a cytoplasmic protein at the surface of …

**Accessions** — [HGNC:15578](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15578) · Entrez [85021](https://www.ncbi.nlm.nih.gov/gene/85021) · UniProt [Q96D71](https://www.uniprot.org/uniprotkb/Q96D71) · Ensembl [ENSG00000135597](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135597)

## Data

Gene col 5727: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5727); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5727, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5727]; `tensor/DDL_lfc|DDL_z.npy` [5727]; `embed/gene_vectors.npy` [5727]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5727 or target_col == 5727). Every well: [[REPS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REPS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
