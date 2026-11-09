---
symbol: "STEAP3"
type: "gene"
col: 3621
ensembl_id: "ENSG00000115107"
name: "STEAP3 metalloreductase"
location: "2q14.2"
module: 104
arm: "+"
pooled_cpm: 29.75
n_lines_expressing: 44
n_dd_up: 3
n_dd_down: 35
n_dd_up_clean: 2
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# STEAP3

*STEAP3 metalloreductase* — 2q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.14× (z +5.1, q 2e-04, up in 9 of 42 measured lines) ⚠ position not correctable. The strongest without an alert is [[Budesonide (drug)]] 0.5 µM: 1.41× (z +3.9, q 0.017, up in 17 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.69×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.193× (z -26.4, q 0e+00, down in 40 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANPEP]] (+0.58, fdr 1e-05), [[APEH]] (+0.56, fdr 3e-05), [[TRAM2]] (+0.56, fdr 4e-05); moves opposite to [[GPRC5C]] (-0.56, fdr 4e-05), [[FCGBP]] (-0.55, fdr 4e-05), [[TMC4]] (-0.54, fdr 1e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LDLRAD3]] → it (grade B ⚠); 4 go from it, the strongest it → [[RHBDL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3621.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.69×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +5.1 | 2e-04 | 9/42 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +4.0 | 0.017 | 11/27 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.017 | 17/41 (LOX-IMVI, SW 900, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.066 | 18/41 (HOP62, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Econazole (drug)]] 5 µM |  | 1.33× | +3.2 | 0.12 | 13/42 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.32× | +3.2 | 0.12 | 12/42 (SW 900, HOP62, …) | two highest doses | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | 1.32× | +3.2 | 0.12 | 18/42 (LOX-IMVI, SW 900, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.33× | +3.1 | 0.12 | 14/40 (NCI-H2030, SNU-423, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.35× | +3.1 | 0.12 | 13/40 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.33× | +3.1 | 0.12 | 12/42 (hTERT-HPNE, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3621.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.193×** | -26.4 | 0e+00 | 40/41 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.320×** | -18.3 | 0e+00 | 35/38 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.243×** | -15.5 | 0e+00 | 40/41 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.288×** | -14.1 | 3e-43 | 36/42 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.315×** | -13.1 | 3e-37 | 32/38 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.353×** | -11.8 | 3e-30 | 32/42 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.450×** | -9.1 | 1e-17 | 30/42 (HOP62, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.456×** | -8.9 | 3e-17 | 32/42 (PANC-1, A549, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.471×** | -8.2 | 1e-14 | 32/42 (C32, PANC-1, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.500×** | -7.9 | 2e-13 | 30/42 (PANC-1, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.518×** | -7.2 | 4e-11 | 21/36 (MIA PaCa-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.546×** | -6.9 | 3e-10 | 28/42 (PANC-1, A549, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.337×** | -6.5 | 4e-09 | 30/42 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.571×** | -6.4 | 7e-09 | 25/42 (PANC-1, SW 1271, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.571×** | -6.4 | 7e-09 | 29/42 (hTERT-HPNE, HOP62, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.520×** | -6.3 | 1e-08 | 25/41 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.683×** | -6.1 | 3e-08 | 27/42 (RPMI-7951, COLO 205, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.599×** | -5.8 | 2e-07 | 26/42 (LoVo, SNU-423, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.429×** | -5.0 | 1e-05 | 23/39 (C32, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.661×** | -4.7 | 6e-05 | 23/42 (A-172, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.692×** | -4.2 | 6e-04 | 22/41 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.718×** | -3.6 | 0.007 | 21/41 (A-172, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3621. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 103 | 0 | 21 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0360× (z -40.4) |
| [[NCI-H1573 (line)]] | alt | 64.4 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0306× (z -27.7) |
| [[A549 (line)]] | wt | 91.9 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0294× (z -30.7) |
| [[NCI-H460 (line)]] | wt | 28.1 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0889× (z -21.9) |
| [[C32 (line)]] | wt | 28.7 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.0664× (z -19.5) |
| [[NCI-H23 (line)]] | alt | 54.5 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0429× (z -27.7) |
| [[HOP62 (line)]] | alt | 19.6 | 1 (1 ⚠) | 7 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.69× (z +10.1) ⚠ position not correctable | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.130× (z -11.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -11.0) |
| [[COLO 205 (line)]] | alt | 35.2 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -12.8) |
| [[A-172 (line)]] | wt | 97.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -18.7) |
| [[LOX-IMVI (line)]] | wt | 42.4 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 17.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -14.3) |
| [[HS-578T (line)]] | alt | 41.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -17.0) |
| [[hTERT-HPNE (line)]] | wt | 47.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -13.2) |
| [[SW 1271 (line)]] | alt | 109 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0957× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 24.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -16.2) |
| [[RKO (line)]] | wt | 18.5 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.0942× (z -11.9) |
| [[SNU-423 (line)]] | alt | 35.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0998× (z -19.9) |
| [[SW 900 (line)]] | alt | 30.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -14.8) |
| [[H4 (line)]] | wt | 25.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0682× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -9.3) |
| [[LoVo (line)]] | wt | 14.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 44.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0523× (z -27.9) |
| [[RPMI-7951 (line)]] | alt | 25.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.1000× (z -16.5) |
| [[SW48 (line)]] | wt | 25.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -14.0) |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -15.0) |
| [[J82 (line)]] | alt | 10.0 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.139× (z -9.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.288× (z -8.8) |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 26.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -16.9) |
| [[SK-MEL-2 (line)]] | alt | 9.85 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0550× (z -11.2) |
| [[SW480 (line)]] | alt | 9.98 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -12.8) |
| [[A-427 (line)]] | wt | 12.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.167× (z -9.3) |
| [[BT-474 (line)]] | alt | 14.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 9.84 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -9.7) |
| [[SW1417 (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -9.0) |
| [[A498 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.80 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.70 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.43 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.71 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3621), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANPEP]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[APEH]] | +0.56 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[TRAM2]] | +0.56 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[JCAD]] | +0.56 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[CPNE7]] | +0.55 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[USP31]] | +0.55 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[E2F4]] | +0.55 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[LDLRAD3]] | +0.55 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[TATDN2]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[MLX]] | +0.54 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[MAPKAPK3]] | +0.53 | +0.46 / +0.49 | both halves | 3e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[AFAP1L1]] | +0.53 | +0.59 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRC5C]] | -0.56 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[FCGBP]] | -0.55 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[TMC4]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[TMPRSS3]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[BCL2L14]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 | pathway: TP53 Regulates Transcription of Cell Death Genes |
| [[ARID4B]] | -0.51 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[SLC44A3]] | -0.51 | -0.61 / -0.37 | both halves | 7e-05 |  |
| [[C11orf52]] | -0.51 | -0.54 / -0.30 | both halves | 2e-04 |  |
| [[ADGRF1]] | -0.50 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[RAMP1]] | -0.49 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[SAMD12-AS1]] | -0.49 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[PTPRR]] | -0.48 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LDLRAD3]] | B | LDLRAD3 activity raises STEAP3's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 2.65× lower at baseline in the lines without LDLRAD3 | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises STEAP3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TRIM2]] | B | TRIM2 activity lowers STEAP3's level | lines that do not express TRIM2 (15) vs lines expressing it (35) | 1.67× higher at baseline in the lines without TRIM2 | 0.062 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |
| [[CLMP]] | B | CLMP activity raises STEAP3's level | lines that do not express CLMP (25) vs lines expressing it (25) | 2.27× lower at baseline in the lines without CLMP | 0.083 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[CLMP]] | B | CLMP activity strengthens STEAP3's drug response | lines that do not express CLMP (20) vs lines expressing it (22) | the lines without CLMP respond 0.71× as strongly (z diff +1.51); strongest at Digitoxin 5 µM: 0.46x vs 0.23x (z diff +2.9) | 0.089 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10; target measured in part of the lines; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHBDL2]] | B | STEAP3 activity lowers RHBDL2's level | lines that do not express STEAP3 (6) vs lines expressing it (44) | 1.85× higher at baseline in the lines without STEAP3 | 0.023 | ⚠ within organs, on part of the lines; also absent: GPR155; maybe low, not absent |
| [[RCL1]] | B | STEAP3 activity raises RCL1's level | lines that do not express STEAP3 (6) vs lines expressing it (44) | 1.25× lower at baseline in the lines without STEAP3 | 0.054 | ⚠ within organs, on part of the lines; also absent: GPR155; maybe low, not absent |
| [[LDLRAD3]] | B | STEAP3 activity raises LDLRAD3's level | lines that do not express STEAP3 (6) vs lines expressing it (44) | 2.87× lower at baseline in the lines without STEAP3 | 0.055 | ⚠ within organs, on part of the lines; also absent: GPR155; maybe low, not absent |
| [[TMC4]] | B | STEAP3 activity lowers TMC4's level | lines that do not express STEAP3 (6) vs lines expressing it (44) | 3.54× higher at baseline in the lines without STEAP3 | 0.066 | ⚠ within organs, on part of the lines; also absent: GPR155; maybe low, not absent |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.528). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.3, 14.3); signed map (-27.5, 41.5). **Vector** length 88.1, 22.3% of its response variance represented; |z| ≥ 3 in 1,345 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.1 | +3.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +2.7 | -7.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.7 | +3.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.5 | +3.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.4 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -18.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.9 | -6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.4 | -26.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.2 | -0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | STEAP3 metalloreductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.2 — chr2:119,223,831-119,265,652 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TSAP6, dudlin-2, STMP3 |
| Gene groups (HGNC) | STEAP family; Flavoproteins |
| Hallmark sets | P53_PATHWAY |
| Reactome | 14 pathways, smallest: TP53 Regulates Transcription of Genes Involved in Cytochrome C Release; Transferrin endocytosis and recycling; TP53 Regulates Transcription of Cell Death Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q658P3](https://www.uniprot.org/uniprotkb/Q658P3) (Metalloreductase STEAP3):

> Integral membrane protein that functions as a NADPH-dependent ferric-chelate reductase, using NADPH from one side of the membrane to reduce a Fe(3+) chelate that is bound on the other side of the membrane. Mediates sequential transmembrane electron transfer from NADPH to FAD and onto heme, and finally to the Fe(3+) chelate (By similarity). Can also reduce Cu(2+) to Cu(1+) (By similarity). Mediates efficient transferrin-dependent iron uptake in erythroid cells (By similarity). May play a role …

**Summary**, from NCBI Gene [55240](https://www.ncbi.nlm.nih.gov/gene/55240):

> This gene encodes a multipass membrane protein that functions as an iron transporter. The encoded protein can reduce both iron (Fe3+) and copper (Cu2+) cations. This protein may mediate downstream responses to p53, including promoting apoptosis. Deficiency in this gene can cause anemia. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:24592](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24592) · Entrez [55240](https://www.ncbi.nlm.nih.gov/gene/55240) · UniProt [Q658P3](https://www.uniprot.org/uniprotkb/Q658P3) · Ensembl [ENSG00000115107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115107)

## Data

Gene col 3621: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3621); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3621, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3621]; `tensor/DDL_lfc|DDL_z.npy` [3621]; `embed/gene_vectors.npy` [3621]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3621 or target_col == 3621). Every well: [[STEAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STEAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
