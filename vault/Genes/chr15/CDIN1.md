---
symbol: "CDIN1"
type: "gene"
col: 11773
ensembl_id: "ENSG00000186073"
name: "CDAN1 interacting nuclease 1"
location: "15q14"
module: 4
arm: "+"
pooled_cpm: 68.28
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CDIN1

*CDAN1 interacting nuclease 1* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.29× (z +4.7, q 0.002, up in 25 of 48 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H2347 3.22×; ⚠ unreliable plate only).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.314× (z -29.5, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VWA8]] (+0.80, fdr 7e-06), [[CHCHD6]] (+0.74, fdr 7e-06), [[NAA25]] (+0.74, fdr 7e-06); moves opposite to [[ZNF490]] (-0.65, fdr 1e-05), [[FAM117A]] (-0.62, fdr 1e-05), [[SLC35F5]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC5A4-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11773.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H2347 3.22×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.7 | 0.002 | 25/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.15× | +3.6 | 0.096 | 17/48 (NCI-H1792, NCI-H1573, …) | top dose only | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.28 | 14/48 (LS 180, Hs 766T, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.1 | 0.28 | 15/48 (SW1417, LS 180, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.20× | +3.0 | 0.28 | 12/50 (LS 180, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 15 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11773.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.314×** | -29.5 | 0e+00 | 45/48 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.426×** | -21.7 | 0e+00 | 46/49 (SW1417, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.388×** | -17.0 | 0e+00 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.452×** | -14.3 | 4e-44 | 38/48 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.481×** | -13.1 | 2e-37 | 45/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.475×** | -12.9 | 5e-36 | 39/48 (NCI-H460, NCI-H23, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.474×** | -12.4 | 2e-33 | 35/45 (A-427, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.457×** | -12.3 | 5e-33 | 38/47 (Panc 03.27, C32, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.529×** | -11.0 | 3e-26 | 30/43 (HEC-1-A, Panc 03.27, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.555×** | -10.2 | 2e-22 | 34/47 (LOX-IMVI, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.572×** | -10.0 | 6e-22 | 34/48 (NCI-H23, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.574×** | -10.0 | 9e-22 | 39/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.359×** | -9.6 | 3e-20 | 36/49 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.631×** | -8.3 | 6e-15 | 36/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **0.641×** | -8.0 | 5e-14 | 37/46 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -8.0 | 5e-14 | 32/50 (HEC-1-A, HT-29, …) | top dose only | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11773. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 74.4 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -20.7) |
| [[NCI-H460 (line)]] | wt | 83.5 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -26.2) |
| [[PANC-1 (line)]] | alt | 97.4 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -29.2) |
| [[MIA PaCa-2 (line)]] | alt | 81.2 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -20.2) |
| [[SW480 (line)]] | alt | 67.7 | 0 | 12 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -18.1) |
| [[RKO (line)]] | wt | 80.1 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -14.4) |
| [[HEC-1-A (line)]] | alt | 82.5 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -25.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.303× (z -20.5) |
| [[HT-29 (line)]] | alt | 86.4 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -18.8) |
| [[KATO III (line)]] | alt | 97.3 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.351× (z -15.1) |
| [[LoVo (line)]] | wt | 87.3 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -27.0) |
| [[NCI-H23 (line)]] | alt | 85.4 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -34.2) |
| [[SW48 (line)]] | wt | 108 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -15.7) |
| [[C32 (line)]] | wt | 56.7 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -23.1) |
| [[J82 (line)]] | alt | 73.4 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -24.8) |
| [[NCI-H1573 (line)]] | alt | 56.3 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -24.1) |
| [[NCI-H2030 (line)]] | alt | 83.1 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -18.1) |
| [[A498 (line)]] | wt | 88.5 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -28.1) |
| [[SK-MEL-2 (line)]] | alt | 93.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -20.3) |
| [[SNU-1 (line)]] | wt | 57.2 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.322× (z -11.2) |
| [[A-172 (line)]] | wt | 54.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -15.4) |
| [[A-427 (line)]] | wt | 55.6 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.369× (z -10.0) |
| [[LS 180 (line)]] | wt | 85.3 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.425× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 68.7 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0842× (z -22.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.237× (z -19.4) |
| [[COLO 205 (line)]] | alt | 38.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -13.7) |
| [[SNU-423 (line)]] | alt | 32.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -12.0) |
| [[A549 (line)]] | wt | 49.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -14.9) |
| [[C-33 A (line)]] | alt | 109 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -13.7) |
| [[Hs 766T (line)]] | wt | 81.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.246× (z -14.9) |
| [[SW1417 (line)]] | alt | 92.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -19.3) |
| [[BT-474 (line)]] | alt | 54.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -12.9) |
| [[H4 (line)]] | wt | 37.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -13.0) |
| [[HepG2_C3A (line)]] | wt | 42.1 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.104× (z -13.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.314× (z -10.3) |
| [[HOP62 (line)]] | alt | 42.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -16.8) |
| [[HS-578T (line)]] | alt | 32.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 39.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 62.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -15.1) |
| [[SHP-77 (line)]] | alt | 53.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.302× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 24.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 49.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -12.6) |
| [[HCT15 (line)]] | alt | 56.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 86.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -14.2) |
| [[NCI-H2347 (line)]] | alt | 19.4 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.22× (z +9.4) ⚠ unreliable plate only | — |
| [[SW 1271 (line)]] | alt | 47.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0670× (z -8.5) |
| [[SW 900 (line)]] | alt | 33.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -9.6) |
| [[AN3 CA (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11773), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VWA8]] | +0.80 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.74 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[NAA25]] | +0.74 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[MIPOL1]] | +0.73 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.68 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[MINDY4]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[DPH6]] | +0.67 | +0.68 / +0.68 | both halves | 7e-06 | STRING 494 |
| [[POLR3B]] | +0.67 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[CLASP2]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[FXN]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[PTPN4]] | +0.65 | +0.57 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF490]] | -0.65 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.62 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[SLC35F5]] | -0.58 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[MEX3C]] | -0.57 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[STXBP2]] | -0.56 | -0.51 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC5A4-AS1]] | B | SLC5A4-AS1 activity raises CDIN1's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.49× lower at baseline in the lines without SLC5A4-AS1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[ENTPD1-AS1]] | C | ENTPD1-AS1 activity raises CDIN1's level | lines that do not express ENTPD1-AS1 (3) vs lines expressing it (47) | 1.72× lower at baseline in the lines without ENTPD1-AS1 | 0.090 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRIQ3, WDR35, ENSG00000287400; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.9, -34.3); signed map (-12.9, -51.1). **Vector** length 103, 31.9% of its response variance represented; |z| ≥ 3 in 1,231 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.8 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +6.4 | +0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.2 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | -0.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.5 | +2.4 |
|  | [[EX229 (drug)]] 5 µM |  | +4.1 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.5 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.5 | +1.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.0 | -21.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.3 | -29.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -8.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.3 | -12.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -10.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -0.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.1 | -0.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.8 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | CDAN1 interacting nuclease 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:36,579,626-36,810,248 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HH114, MGC11326, FLJ22851; previously C15orf41 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2V0](https://www.uniprot.org/uniprotkb/Q9Y2V0) (CDAN1-interacting nuclease 1):

> Plays a role in erythroid cell differentiation.

**Summary**, from NCBI Gene [84529](https://www.ncbi.nlm.nih.gov/gene/84529):

> This gene encodes a protein with two predicted helix-turn-helix domains. Mutations in this gene were found in families with congenital dyserythropoietic anemia type Ib. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:26929](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26929) · Entrez [84529](https://www.ncbi.nlm.nih.gov/gene/84529) · UniProt [Q9Y2V0](https://www.uniprot.org/uniprotkb/Q9Y2V0) · Ensembl [ENSG00000186073](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186073)

## Data

Gene col 11773: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11773); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11773, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11773]; `tensor/DDL_lfc|DDL_z.npy` [11773]; `embed/gene_vectors.npy` [11773]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11773 or target_col == 11773). Every well: [[CDIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
