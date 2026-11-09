---
symbol: "ASAP2"
type: "gene"
col: 7553
ensembl_id: "ENSG00000151693"
name: "ArfGAP with SH3 domain, ankyrin repeat and PH domain 2"
location: "2p25.1"
module: 193
arm: "+"
pooled_cpm: 245.02
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 43
n_dd_up_clean: 2
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/193"]
generated_by: "tahoemap"
---

# ASAP2

*ArfGAP with SH3 domain, ankyrin repeat and PH domain 2* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 1.37× (z +5.2, q 9e-05, up in 31 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[BAY1125976 (drug)]] 5 µM: 1.66× (z +4.4, q 0.003, up in 29 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 1 line (MIA PaCa-2 9.35×); [[Daptomycin (drug)]] 5 µM in 1 line (NCI-H1573 2.48×; ⚠ unreliable plate only); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SW48 2.53×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (NCI-H1573 2.36×).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.531× (z -14.8, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELK3]] (+0.73, fdr 7e-06), [[PXN]] (+0.72, fdr 7e-06), [[DOCK5]] (+0.71, fdr 7e-06); moves opposite to [[CCL28]] (-0.60, fdr 2e-05), [[DNAJC27]] (-0.60, fdr 1e-05), [[YY1AP1]] (-0.57, fdr 1e-05).
> It is in [[Module 193]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[SLCO4A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7553.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 1 line (MIA PaCa-2 9.35×); [[Daptomycin (drug)]] 5 µM in 1 line (NCI-H1573 2.48×; ⚠ unreliable plate only); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SW48 2.53×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (NCI-H1573 2.36×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.37×** | +5.2 | 9e-05 | 31/46 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.66×** | +4.4 | 0.003 | 29/46 (SW480, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.30×** | +4.1 | 0.007 | 23/46 (NCI-H1573, SHP-77, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.26×** | +3.9 | 0.014 | 25/45 (SW 900, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.015 | 27/45 (NCI-H1573, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7553.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.531×** | -14.8 | 0e+00 | 42/47 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.518×** | -10.5 | 4e-23 | 39/45 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.570×** | -9.3 | 3e-18 | 40/46 (HEC-1-A, SW480, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.689×** | -8.7 | 5e-16 | 30/46 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.592×** | -8.7 | 5e-16 | 38/46 (PANC-1, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.696×** | -8.4 | 3e-15 | 35/46 (RKO, NCI-H23, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.676×** | -7.9 | 3e-13 | 37/46 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.600×** | -7.8 | 4e-13 | 28/43 (HepG2/C3A, SW48, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.690×** | -7.3 | 1e-11 | 35/46 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.642×** | -7.3 | 1e-11 | 31/47 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.631×** | -7.3 | 1e-11 | 33/46 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.648×** | -7.2 | 4e-11 | 37/46 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.714×** | -6.5 | 3e-09 | 29/47 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -6.3 | 9e-09 | 33/46 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.675×** | -6.2 | 2e-08 | 37/46 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.724×** | -6.2 | 2e-08 | 33/48 (AsPC-1, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.707×** | -5.7 | 4e-07 | 31/46 (HEC-1-A, RKO, …) | top dose only | cell-cycle shift (explains ~18% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7553. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 616 | 0 | 23 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -18.2) |
| [[HEC-1-A (line)]] | alt | 354 | 0 | 23 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -19.7) |
| [[RKO (line)]] | wt | 339 | 0 | 23 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0772× (z -22.3) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.233× (z -18.6) |
| [[SW480 (line)]] | alt | 373 | 0 | 22 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -15.6) |
| [[NCI-H23 (line)]] | alt | 141 | 0 | 17 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -20.8) |
| [[HepG2_C3A (line)]] | wt | 472 | 0 | 14 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 426 | 1 | 12 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 9.35× (z +11.3) | [[Adagrasib (drug)]] 0.05 µM 0.530× (z -21.5) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -19.1) |
| [[LoVo (line)]] | wt | 253 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -13.9) |
| [[PANC-1 (line)]] | alt | 556 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -23.5) |
| [[HOP62 (line)]] | alt | 317 | 0 | 8 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.652× (z -15.6) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 394 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -14.6) |
| [[Hs 766T (line)]] | wt | 409 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -12.9) |
| [[KATO III (line)]] | alt | 439 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -16.3) |
| [[LS 180 (line)]] | wt | 264 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 264 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.187× (z -13.9) |
| [[J82 (line)]] | alt | 106 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 150 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -12.9) |
| [[SK-MEL-2 (line)]] | alt | 209 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -9.2) |
| [[BT-474 (line)]] | alt | 139 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.276× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HT-29 (line)]] | alt | 389 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 104 | 2 (1 ⚠) | 1 | [[Daptomycin (drug)]] 5 µM 2.48× (z +9.1) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.36× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 193 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -12.8) |
| [[A-427 (line)]] | wt | 93.4 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.382× (z -11.6) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.465× (z -8.9) |
| [[SW1417 (line)]] | alt | 160 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.382× (z -11.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -8.6) |
| [[SW48 (line)]] | wt | 165 | 1 | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.53× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -11.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 183 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -14.5) |
| [[A498 (line)]] | wt | 174 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -9.8) |
| [[HCT15 (line)]] | alt | 250 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -11.8) |
| [[HS-578T (line)]] | alt | 171 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -15.0) |
| [[NCI-H2347 (line)]] | alt | 86.2 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.476× (z -9.3) |
| [[SW 1088 (line)]] | alt | 170 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0802× (z -11.3) |
| [[SW 1271 (line)]] | alt | 262 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -9.2) |
| [[A549 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 145 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 50.8 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.1 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 120 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 84.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7553), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELK3]] | +0.73 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[PXN]] | +0.72 | +0.73 / +0.71 | both halves | 7e-06 | STRING 836 |
| [[DOCK5]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 | same gene group |
| [[THSD4]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[ACOT7]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[ITGA6]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[ASAP1]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 | same gene group; STRING 907 |
| [[CAPRIN2]] | +0.65 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[DLC1]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[BCAR3]] | +0.65 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[NIBAN2]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[MICAL2]] | +0.65 | +0.63 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCL28]] | -0.60 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[DNAJC27]] | -0.60 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[YY1AP1]] | -0.57 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[TET2]] | -0.56 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[TENT5A]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[SPACA9]] | -0.53 | -0.55 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLCO4A1]] | B | SLCO4A1 activity raises ASAP2's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 2.02× lower at baseline in the lines without SLCO4A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises ASAP2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 7.0% of all compounds | 0.030 | ⚠ off-target possible; 4 compounds |
| [[S100A16]] | B | S100A16 activity raises ASAP2's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 2.18× lower at baseline in the lines without S100A16 | 0.041 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[ARHGAP29]] | B | ARHGAP29 activity raises ASAP2's level | lines that do not express ARHGAP29 (10) vs lines expressing it (40) | 2.09× lower at baseline in the lines without ARHGAP29 | 0.049 | ⚠ within organs, on part of the lines; also absent: HTATIP2, CTSZ, TBILA |
| [[LINC00707]] | B | LINC00707 activity raises ASAP2's level | lines that do not express LINC00707 (26) vs lines expressing it (24) | 1.39× lower at baseline in the lines without LINC00707 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000285845, ENSG00000285743, LINP1 |
| [[BCL2L1]] | B | BCL2L1 activity raises ASAP2's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 2.38× lower at baseline in the lines without BCL2L1 | 0.057 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[TNFRSF10A]] | B | TNFRSF10A activity raises ASAP2's level | lines that do not express TNFRSF10A (10) vs lines expressing it (40) | 1.76× lower at baseline in the lines without TNFRSF10A | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, SLC16A5, CDCP1 |
| [[TOR4A]] | B | TOR4A activity raises ASAP2's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 1.90× lower at baseline in the lines without TOR4A | 0.097 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 193]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.7, 7.3); signed map (7.9, 44.3). **Vector** length 142, 53.1% of its response variance represented; |z| ≥ 3 in 1,870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +7.1 | +5.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.0 | +3.8 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +5.9 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.8 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.3 | +2.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.8 | +4.4 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -9.5 | -7.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -9.0 | -8.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -8.6 | -6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -8.2 | -6.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -7.9 | -6.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -7.8 | -7.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.6 | -7.3 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with SH3 domain, ankyrin repeat and PH domain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:9,206,765-9,405,683 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0400, PAP, SHAG1, CENTB3; previously DDEF2 |
| Gene groups (HGNC) | ArfGAPs; Ankyrin repeat domain containing; BAR-PH domain containing; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O43150](https://www.uniprot.org/uniprotkb/O43150) (Arf-GAP with SH3 domain, ANK repeat and PH domain-containing protein 2):

> Activates the small GTPases ARF1, ARF5 and ARF6. Regulates the formation of post-Golgi vesicles and modulates constitutive secretion. Modulates phagocytosis mediated by Fc gamma receptor and ARF6. Modulates PXN recruitment to focal contacts and cell migration.

**Summary**, from NCBI Gene [8853](https://www.ncbi.nlm.nih.gov/gene/8853):

> This gene encodes a multidomain protein containing an N-terminal alpha-helical region with a coiled-coil motif, followed by a pleckstrin homology (PH) domain, an Arf-GAP domain, an ankyrin homology region, a proline-rich region, and a C-terminal Src homology 3 (SH3) domain. The protein localizes in the Golgi apparatus and at the plasma membrane, where it colocalizes with protein tyrosine kinase 2-beta (PYK2). The encoded protein forms a stable complex with PYK2 in vivo. This interaction appears …

**Accessions** — [HGNC:2721](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2721) · Entrez [8853](https://www.ncbi.nlm.nih.gov/gene/8853) · UniProt [O43150](https://www.uniprot.org/uniprotkb/O43150) · Ensembl [ENSG00000151693](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151693)

## Data

Gene col 7553: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7553); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7553, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7553]; `tensor/DDL_lfc|DDL_z.npy` [7553]; `embed/gene_vectors.npy` [7553]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7553 or target_col == 7553). Every well: [[ASAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
