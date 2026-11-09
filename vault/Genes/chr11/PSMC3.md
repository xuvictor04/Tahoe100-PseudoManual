---
symbol: "PSMC3"
type: "gene"
col: 9207
ensembl_id: "ENSG00000165916"
name: "proteasome 26S subunit, ATPase 3"
location: "11p11.2"
module: 215
arm: "+"
pooled_cpm: 40.77
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/215"]
generated_by: "tahoemap"
---

# PSMC3

*proteasome 26S subunit, ATPase 3* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.66× (z +16.5, q 0e+00, up in 44 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 2.57× (z +12.0, q 3e-31, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.738× (z -5.5, q 2e-05, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.109×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMC5]] (+0.81, fdr 7e-06), [[PSMD11]] (+0.77, fdr 7e-06), [[PDAP1]] (+0.76, fdr 7e-06); moves opposite to [[MHENCR]] (-0.73, fdr 7e-06), [[SNHG19]] (-0.71, fdr 7e-06), [[SNHG25]] (-0.68, fdr 7e-06).
> It is in [[Module 215]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9207.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.66×** | +16.5 | 0e+00 | 44/45 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.46×** | +15.2 | 0e+00 | 36/38 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.88×** | +12.5 | 2e-33 | 41/42 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.57×** | +12.0 | 3e-31 | 47/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.53×** | +11.8 | 3e-30 | 48/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.24×** | +9.5 | 3e-19 | 40/48 (A498, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.11×** | +8.6 | 8e-16 | 47/48 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.98×** | +8.4 | 4e-15 | 43/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.55×** | +7.9 | 2e-13 | 40/48 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +7.2 | 3e-11 | 39/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.75×** | +7.2 | 4e-11 | 42/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +6.2 | 3e-08 | 37/48 (C32, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +5.3 | 6e-06 | 35/48 (PANC-1, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **1.43×** | +4.5 | 2e-04 | 32/46 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.3 | 7e-04 | 28/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.014 | 21/48 (CFPAC-1, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.026 | 20/47 (LOX-IMVI, SW48, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9207.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.109×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.738×** | -5.5 | 2e-05 | 38/48 (LS 180, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.687×** | -4.8 | 4e-04 | 29/48 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9207. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 41.6 | 9 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 38.9 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.32× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 37.2 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.68× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.51× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 55.4 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.21× (z +9.8) | — |
| [[SW480 (line)]] | alt | 43.8 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.98× (z +10.6) | — |
| [[A498 (line)]] | wt | 65.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 36.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.79× (z +8.6) | — |
| [[J82 (line)]] | alt | 70.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 48.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.18× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LoVo (line)]] | wt | 30.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 31.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 26.2 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.21× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 56.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H460 (line)]] | wt | 27.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 45.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.62× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 64.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A549 (line)]] | wt | 35.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[C32 (line)]] | wt | 28.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[CFPAC-1 (line)]] | alt | 37.6 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.41× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 34.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.15× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 35.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 46.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 34.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.59× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 21.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.09× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW 900 (line)]] | alt | 17.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.30× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-427 (line)]] | wt | 54.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 47.8 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.109× (z -10.1) |
| [[COLO 205 (line)]] | alt | 23.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.74× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 48.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.00× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 35.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H23 (line)]] | alt | 43.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[RPMI-7951 (line)]] | alt | 40.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.75× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 35.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW1417 (line)]] | alt | 44.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AsPC-1 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9207), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMC5]] | +0.81 | +0.86 / +0.73 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMD11]] | +0.77 | +0.72 / +0.75 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PDAP1]] | +0.76 | +0.77 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[PSMD6]] | +0.71 | +0.79 / +0.61 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[HSPB8]] | +0.69 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[CCT7]] | +0.66 | +0.70 / +0.60 | both halves | 7e-06 | STRING 798 |
| [[DPP3]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 | pathway: Cellular response to chemical stress |
| [[RNF6]] | +0.66 | +0.70 / +0.56 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[PSMD4]] | +0.65 | +0.73 / +0.55 | both halves | 1e-05 | same gene group; pathway: Proteasome assembly; STRING 999 |
| [[PSMD12]] | +0.65 | +0.69 / +0.60 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[ALOX12P2-1]] | +0.65 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[HUWE1]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 437 |

## Genes that move opposite

*37 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MHENCR]] | -0.73 | -0.67 / -0.71 | both halves | 7e-06 |  |
| [[SNHG19]] | -0.71 | -0.63 / -0.71 | both halves | 7e-06 |  |
| [[SNHG25]] | -0.68 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[COMMD6]] | -0.66 | -0.60 / -0.65 | both halves | 7e-06 | pathway: Neddylation |
| [[TMSB10]] | -0.64 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[B3GAT3]] | -0.64 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[METRN]] | -0.64 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[MINCR]] | -0.63 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[RPLP2]] | -0.63 | -0.57 / -0.62 | both halves | 8e-06 | pathway: Metabolism of amino acids and derivatives |
| [[TBC1D22A-DT]] | -0.63 | -0.54 / -0.70 | both halves | 1e-05 |  |
| [[RPL37A]] ⚠ | -0.62 | -0.52 / -0.65 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives; ⚠ in the vector space only through flagged drug-doses |
| [[CSKMT]] | -0.62 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | -0.62 | -0.49 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 215]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.822). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.6, -10.0); signed map (-6.5, -36.5). **Vector** length 86.0, 23.8% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.1 | +12.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.0 | +11.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.0 | +8.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.9 | +8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +5.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.6 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.5 | -4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | -3.2 | +4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | +0.8 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.5 | -0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, ATPase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:47,418,769-47,426,473 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TBP1, TBP-1, RPT5 |
| Gene groups (HGNC) | AAA ATPases; Proteasome |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 170 pathways, smallest: Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC); Cross-presentation of soluble exogenous antigens (endosomes) |
| Matched by | ensembl_id |

**Function**, from UniProt [P17980](https://www.uniprot.org/uniprotkb/P17980) (26S proteasome regulatory subunit 6A):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair. PSMC3 belongs to …

**Summary**, from NCBI Gene [5702](https://www.ncbi.nlm.nih.gov/gene/5702):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9549](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9549) · Entrez [5702](https://www.ncbi.nlm.nih.gov/gene/5702) · UniProt [P17980](https://www.uniprot.org/uniprotkb/P17980) · Ensembl [ENSG00000165916](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165916)

## Data

Gene col 9207: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9207); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9207, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9207]; `tensor/DDL_lfc|DDL_z.npy` [9207]; `embed/gene_vectors.npy` [9207]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9207 or target_col == 9207). Every well: [[PSMC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
