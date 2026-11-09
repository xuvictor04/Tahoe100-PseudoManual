---
symbol: "TAMM41"
type: "gene"
col: 6893
ensembl_id: "ENSG00000144559"
name: "TAM41 mitochondrial translocator assembly and maintenance homolog"
location: "3p25.2"
module: 33
arm: "+"
pooled_cpm: 28.4
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 28
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# TAMM41

*TAM41 mitochondrial translocator assembly and maintenance homolog* — 3p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 1.80× (z +4.4, q 0.005, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.225× (z -30.5, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUDCD3]] (+0.75, fdr 7e-06), [[MRPS31P4]] (+0.75, fdr 7e-06), [[GEMIN5]] (+0.75, fdr 7e-06); moves opposite to [[FBXL19-AS1]] (-0.64, fdr 4e-04), [[C2]] (-0.62, fdr 5e-05), [[STARD4-AS1]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6893.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +4.4 | 0.005 | 25/46 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | 1.27× | +3.5 | 0.12 | 17/48 (A-427, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.22 | 15/48 (SW 900, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | 1.24× | +3.1 | 0.22 | 15/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.29× | +3.1 | 0.22 | 6/48 (SW480, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.23× | +3.0 | 0.22 | 10/48 (SW480, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6893.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.225×** | -30.5 | 0e+00 | 47/48 (MIA PaCa-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.237×** | -20.8 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.289×** | -18.0 | 0e+00 | 46/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.317×** | -16.6 | 0e+00 | 46/48 (A-172, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.320×** | -16.5 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.480×** | -15.0 | 0e+00 | 36/47 (SNU-423, A549, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.358×** | -14.3 | 3e-44 | 43/48 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.359×** | -14.3 | 3e-44 | 44/47 (H4, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.447×** | -11.6 | 2e-29 | 43/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.571×** | -11.5 | 1e-28 | 39/48 (A-172, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.457×** | -11.3 | 5e-28 | 35/44 (SK-MEL-2, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.448×** | -11.2 | 3e-27 | 25/34 (HOP62, Panc 03.27, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.456×** | -10.9 | 4e-26 | 40/47 (NCI-H1792, A498, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.444×** | -10.9 | 7e-26 | 30/39 (MIA PaCa-2, A-172, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.475×** | -10.8 | 2e-25 | 43/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.506×** | -9.8 | 2e-21 | 41/48 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.701×** | -4.8 | 4e-05 | 28/48 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.795×** | -3.3 | 0.021 | 18/48 (J82, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.735×** | -3.2 | 0.033 | 17/46 (COLO 205, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.678×** | -2.9 | 0.071 | 16/47 (SNU-1, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.760×** | -2.8 | 0.096 | 11/48 (PANC-1, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6893. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 22.1 | 0 | 16 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -20.1) |
| [[HOP62 (line)]] | alt | 56.1 | 0 | 15 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -27.4) |
| [[SW480 (line)]] | alt | 39.1 | 0 | 13 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0856× (z -26.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0993× (z -24.7) |
| [[A-172 (line)]] | wt | 38.3 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0690× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -19.2) |
| [[LOX-IMVI (line)]] | wt | 33.7 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -16.3) |
| [[SNU-423 (line)]] | alt | 32.6 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -20.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -19.6) |
| [[NCI-H460 (line)]] | wt | 19.8 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -18.0) |
| [[RPMI-7951 (line)]] | alt | 40.3 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0447× (z -30.5) |
| [[H4 (line)]] | wt | 46.1 | 0 | 9 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0398× (z -18.9) |
| [[HEC-1-A (line)]] | alt | 42.3 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -22.3) |
| [[NCI-H1792 (line)]] | alt | 51.5 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -19.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.116× (z -17.4) |
| [[SK-MEL-2 (line)]] | alt | 41.7 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.121× (z -16.1) |
| [[HS-578T (line)]] | alt | 30.7 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -18.4) |
| [[J82 (line)]] | alt | 21.4 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -19.2) |
| [[C32 (line)]] | wt | 23.2 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -16.2) |
| [[MIA PaCa-2 (line)]] | alt | 31.5 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0322× (z -36.0) |
| [[NCI-H2030 (line)]] | alt | 23.0 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 22.8 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -17.5) |
| [[HCT15 (line)]] | alt | 36.3 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0281× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0597× (z -16.9) |
| [[KATO III (line)]] | alt | 26.5 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.110× (z -15.7) |
| [[Panc 03.27 (line)]] | alt | 32.8 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -24.9) |
| [[SW1417 (line)]] | alt | 32.8 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -20.8) |
| [[A549 (line)]] | wt | 37.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -20.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -17.8) |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 5 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.112× (z -12.7) |
| [[hTERT-HPNE (line)]] | wt | 23.7 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -15.8) |
| [[LoVo (line)]] | wt | 28.0 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -19.2) |
| [[LS 180 (line)]] | wt | 26.9 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -17.5) |
| [[NCI-H23 (line)]] | alt | 33.8 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -13.6) |
| [[RKO (line)]] | wt | 25.3 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0391× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -15.9) |
| [[A498 (line)]] | wt | 16.6 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -19.6) |
| [[C-33 A (line)]] | alt | 29.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -9.6) |
| [[SHP-77 (line)]] | alt | 23.9 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.136× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 19.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -16.2) |
| [[NCI-H2347 (line)]] | alt | 22.6 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -15.7) |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0814× (z -13.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -9.9) |
| [[SW48 (line)]] | wt | 31.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -12.7) |
| [[A-427 (line)]] | wt | 27.6 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.257× (z -10.2) |
| [[Hs 766T (line)]] | wt | 23.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -11.6) |
| [[HT-29 (line)]] | alt | 9.01 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0514× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -8.8) |
| [[SNU-1 (line)]] | wt | 25.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0656× (z -13.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 33.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -9.2) |
| [[COLO 205 (line)]] | alt | 18.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0629× (z -11.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6893), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDCD3]] | +0.75 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[MRPS31P4]] | +0.75 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[GEMIN5]] | +0.75 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[ORC5]] | +0.74 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[DDX55]] | +0.73 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[NARS2]] | +0.73 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[RMND1]] | +0.73 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[THOC1]] | +0.72 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[TTC26]] | +0.71 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[COG2]] | +0.71 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[RAD17]] | +0.69 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[ELP1]] | +0.69 | +0.62 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL19-AS1]] | -0.64 | -0.58 / -0.25 | both halves | 4e-04 |  |
| [[C2]] | -0.62 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[STARD4-AS1]] | -0.60 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[KANSL1L]] | -0.60 | -0.56 / -0.21 | both halves | 6e-04 |  |
| [[PHF8]] | -0.59 | -0.49 / -0.23 | both halves | 5e-04 |  |
| [[ARSB]] | -0.59 | -0.51 / -0.29 | both halves | 3e-04 |  |
| [[CCNT2-AS1]] | -0.59 | -0.50 / -0.37 | both halves | 9e-05 |  |
| [[SRSF5]] | -0.59 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[CCDC90B-AS1]] | -0.58 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[EFCAB5]] | -0.58 | -0.46 / -0.24 | both halves | 4e-04 |  |
| [[SLC25A53]] | -0.57 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[C2orf88]] | -0.57 | -0.37 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TAMM41's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.687). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.4, -2.6); signed map (-21.8, -15.4). **Vector** length 93.9, 26.7% of its response variance represented; |z| ≥ 3 in 1,278 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +7.7 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.1 | +4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.6 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.4 | +3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | -0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.4 | -30.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -14.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.0 | -16.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.8 | -11.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -14.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -0.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | TAM41 mitochondrial translocator assembly and maintenance homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.2 — chr3:11,790,442-11,846,919 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC16471, DKFZp434E0519; previously C3orf31 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BW9](https://www.uniprot.org/uniprotkb/Q96BW9) (Phosphatidate cytidylyltransferase, mitochondrial):

> Catalyzes the conversion of phosphatidic acid (PA) to CDP-diacylglycerol (CDP-DAG), an essential intermediate in the synthesis of phosphatidylglycerol, cardiolipin and phosphatidylinositol.

**Summary**, from NCBI Gene [132001](https://www.ncbi.nlm.nih.gov/gene/132001):

> Predicted to enable phosphatidate cytidylyltransferase activity. Predicted to be involved in CDP-diacylglycerol biosynthetic process and cardiolipin biosynthetic process. Is active in mitochondrion. Implicated in combined oxidative phosphorylation deficiency 56. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25187) · Entrez [132001](https://www.ncbi.nlm.nih.gov/gene/132001) · UniProt [Q96BW9](https://www.uniprot.org/uniprotkb/Q96BW9) · Ensembl [ENSG00000144559](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144559)

## Data

Gene col 6893: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6893); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6893, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6893]; `tensor/DDL_lfc|DDL_z.npy` [6893]; `embed/gene_vectors.npy` [6893]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6893 or target_col == 6893). Every well: [[TAMM41 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAMM41.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
