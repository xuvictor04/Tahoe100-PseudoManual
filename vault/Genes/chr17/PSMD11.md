---
symbol: "PSMD11"
type: "gene"
col: 2985
ensembl_id: "ENSG00000108671"
name: "proteasome 26S subunit, non-ATPase 11"
location: "17q11.2"
module: 117
arm: "+"
pooled_cpm: 99.87
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# PSMD11

*proteasome 26S subunit, non-ATPase 11* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.84× (z +28.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.810× (z -6.3, q 2e-07, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.447×; ⚠ cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 1 line (Hs 766T 0.472×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDE]] (+0.77, fdr 7e-06), [[PSMD1]] (+0.77, fdr 7e-06), [[PSMC3]] (+0.77, fdr 7e-06); moves opposite to [[B3GAT3]] (-0.68, fdr 1e-05), [[MINDY2]] (-0.68, fdr 7e-06), [[COMMD6]] (-0.66, fdr 7e-06).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NMRAL2P-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2985.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.84×** | +28.5 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.82×** | +27.1 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.91×** | +21.4 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +18.1 | 0e+00 | 43/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.99×** | +14.6 | 0e+00 | 47/48 (C32, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.90×** | +13.6 | 3e-40 | 42/49 (A549, SW480, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +12.9 | 4e-36 | 44/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.84×** | +12.9 | 4e-36 | 44/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +12.8 | 2e-35 | 45/47 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.14×** | +11.5 | 6e-29 | 47/49 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.74×** | +11.2 | 2e-27 | 44/45 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +11.2 | 3e-27 | 41/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.68×** | +11.0 | 2e-26 | 41/48 (SW480, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +10.0 | 9e-22 | 37/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.62×** | +9.9 | 2e-21 | 31/44 (A549, SW480, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.19×** | +8.7 | 1e-16 | 42/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +8.5 | 4e-16 | 40/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +7.9 | 6e-14 | 30/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +4.9 | 3e-05 | 28/48 (LS 180, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +4.1 | 1e-03 | 12/48 (SNU-1, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2985.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.447×; ⚠ cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 1 line (Hs 766T 0.472×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.810×** | -6.3 | 2e-07 | 31/48 (KATO III, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -4.7 | 8e-04 | 2/50 (NCI-H661, SW 1088) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.816×** | -4.3 | 0.003 | 28/49 (KATO III, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.831×** | -3.9 | 0.012 | 18/49 (H4, NCI-H2122, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.839× | -3.7 | 0.022 | 21/48 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.847× | -3.5 | 0.035 | 18/48 (KATO III, NCI-H460, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.5 | 0.035 | 20/48 (KATO III, NCI-H460, …) | all doses, flat |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.851× | -3.4 | 0.046 | 13/49 (A-172, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2985. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 110 | 18 (6 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.11× (z +21.7) | — |
| [[NCI-H1792 (line)]] | alt | 68.2 | 14 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +17.8) | — |
| [[SW480 (line)]] | alt | 97.4 | 14 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.99× (z +22.2) | — |
| [[LoVo (line)]] | wt | 79.3 | 12 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.54× (z +19.8) | — |
| [[NCI-H460 (line)]] | wt | 113 | 12 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.24× (z +19.7) | — |
| [[A498 (line)]] | wt | 122 | 11 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.92× (z +17.1) | — |
| [[A549 (line)]] | wt | 110 | 10 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.56× (z +16.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 91.3 | 10 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.23× (z +16.0) | — |
| [[NCI-H1573 (line)]] | alt | 83.1 | 10 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.60× (z +20.5) | — |
| [[LOX-IMVI (line)]] | wt | 85.7 | 8 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.86× (z +17.8) | — |
| [[LS 180 (line)]] | wt | 89.1 | 8 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.72× (z +17.2) | — |
| [[NCI-H23 (line)]] | alt | 130 | 8 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.8) | — |
| [[COLO 205 (line)]] | alt | 69.0 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.51× (z +16.4) | — |
| [[HOP62 (line)]] | alt | 78.6 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.94× (z +17.3) | — |
| [[NCI-H2030 (line)]] | alt | 170 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.24× (z +15.5) | — |
| [[SNU-423 (line)]] | alt | 75.6 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.14× (z +14.3) | — |
| [[A-172 (line)]] | wt | 158 | 6 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.55× (z +16.7) | — |
| [[CFPAC-1 (line)]] | alt | 49.1 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.57× (z +14.9) | — |
| [[HCT15 (line)]] | alt | 77.5 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.86× (z +13.4) | — |
| [[J82 (line)]] | alt | 94.2 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.77× (z +12.5) | — |
| [[KATO III (line)]] | alt | 129 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.58× (z +16.7) | — |
| [[C32 (line)]] | wt | 81.0 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.91× (z +16.9) | — |
| [[HEC-1-A (line)]] | alt | 88.3 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.42× (z +17.0) | — |
| [[Hs 766T (line)]] | wt | 44.2 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.93× (z +14.0) | [[Selinexor (drug)]] 5 µM 0.472× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 120 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.22× (z +17.2) | — |
| [[SK-MEL-2 (line)]] | alt | 84.7 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.58× (z +14.0) | — |
| [[SNU-1 (line)]] | wt | 110 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.21× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 163 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.06× (z +14.0) | — |
| [[AsPC-1 (line)]] | alt | 43.6 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.15× (z +12.1) | — |
| [[BT-474 (line)]] | alt | 117 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.74× (z +10.8) | — |
| [[HS-578T (line)]] | alt | 74.9 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.98× (z +13.9) | — |
| [[hTERT-HPNE (line)]] | wt | 65.8 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.99× (z +15.1) | — |
| [[Panc 03.27 (line)]] | alt | 115 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.49× (z +15.6) | — |
| [[RKO (line)]] | wt | 114 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.45× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 74.2 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.48× (z +11.7) | — |
| [[C-33 A (line)]] | alt | 106 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.10× (z +11.2) | — |
| [[H4 (line)]] | wt | 87.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.38× (z +13.8) | — |
| [[HepG2_C3A (line)]] | wt | 97.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.53× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 114 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 73.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.19× (z +14.8) | — |
| [[SHP-77 (line)]] | alt | 109 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.88× (z +12.5) | — |
| [[SW1417 (line)]] | alt | 98.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.68× (z +11.6) | — |
| [[SW48 (line)]] | wt | 147 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.67× (z +12.4) | — |
| [[AN3 CA (line)]] | alt | 138 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.02× (z +9.8) | — |
| [[CHP-212 (line)]] | wt | 88.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 113 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2985), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDE]] | +0.77 | +0.75 / +0.74 | both halves | 7e-06 | pathway: Deubiquitination |
| [[PSMD1]] | +0.77 | +0.76 / +0.83 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMC3]] | +0.77 | +0.72 / +0.75 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMC5]] | +0.76 | +0.79 / +0.70 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PPP2CA]] | +0.74 | +0.74 / +0.68 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[PSMB2]] | +0.72 | +0.67 / +0.77 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[UBQLN1]] | +0.71 | +0.60 / +0.73 | both halves | 7e-06 | STRING 594 |
| [[PSMD6]] | +0.70 | +0.72 / +0.69 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[EWSR1]] | +0.69 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[ALOX12P2-1]] | +0.68 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[HTATIP2]] | +0.67 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[FECH]] | +0.67 | +0.66 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GAT3]] | -0.68 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[MINDY2]] | -0.68 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[COMMD6]] | -0.66 | -0.59 / -0.66 | both halves | 7e-06 | pathway: Neddylation |
| [[NDUFA2]] | -0.65 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[AFMID]] | -0.64 | -0.59 / -0.60 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives |
| [[TMSB10]] | -0.63 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[KLHL28]] | -0.62 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[IMP3]] | -0.62 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[ANKRD37]] | -0.61 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[SEC22A]] | -0.61 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[ARID3A]] | -0.60 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[GPR157]] | -0.60 | -0.47 / -0.61 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMRAL2P-1]] | B | NMRAL2P-1 activity lowers PSMD11's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.24× higher at baseline in the lines without NMRAL2P-1 | 0.079 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[ME1]] | C | ME1 activity weakens PSMD11's drug response | lines that do not express ME1 (11) vs lines expressing it (38) | the lines without ME1 respond 0.82× as strongly (z diff +0.02); strongest at Ixazomib citrate 0.5 µM: 3.72x vs 3.82x (z diff -2.3) | 0.089 | ⚠ within organs, on part of the lines; target measured in part of the lines; both ways; rests on the correction; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-22.6, -10.1); signed map (-6.5, -36.2). **Vector** length 97.0, 32.6% of its response variance represented; |z| ≥ 3 in 1,362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +9.5 | +28.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.4 | +27.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.8 | +21.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +7.3 | +13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +7.2 | +9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +14.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.6 | +11.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -3.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -6.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -3.6 | +11.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | +0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.9 | -0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, non-ATPase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:32,444,379-32,483,319 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S9, p44.5, MGC3844, Rpn6 |
| Gene groups (HGNC) | Proteasome |
| Reactome | 170 pathways, smallest: Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC); Cross-presentation of soluble exogenous antigens (endosomes) |
| Matched by | ensembl_id |

**Function**, from UniProt [O00231](https://www.uniprot.org/uniprotkb/O00231) (26S proteasome non-ATPase regulatory subunit 11):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair. In the complex, …

**Summary**, from NCBI Gene [5717](https://www.ncbi.nlm.nih.gov/gene/5717):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9556](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9556) · Entrez [5717](https://www.ncbi.nlm.nih.gov/gene/5717) · UniProt [O00231](https://www.uniprot.org/uniprotkb/O00231) · Ensembl [ENSG00000108671](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108671)

## Data

Gene col 2985: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2985); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2985, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2985]; `tensor/DDL_lfc|DDL_z.npy` [2985]; `embed/gene_vectors.npy` [2985]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2985 or target_col == 2985). Every well: [[PSMD11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
