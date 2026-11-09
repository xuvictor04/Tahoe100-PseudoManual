---
symbol: "BCAR3"
type: "gene"
col: 6093
ensembl_id: "ENSG00000137936"
name: "BCAR3 adaptor protein, NSP family member"
location: "1p22.1"
module: 147
arm: "+"
pooled_cpm: 213.78
n_lines_expressing: 41
n_dd_up: 3
n_dd_down: 37
n_dd_up_clean: 2
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 9
direction_downstream: 22
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# BCAR3

*BCAR3 adaptor protein, NSP family member* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.23× (z +4.3, q 0.010, up in 17 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (C32 3.09×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (Hs 766T 7.37×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.228× (z -21.3, q 0e+00, down in 39 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELK3]] (+0.76, fdr 7e-06), [[SMURF2]] (+0.68, fdr 7e-06), [[THSD4]] (+0.68, fdr 7e-06); moves opposite to [[BTN3A1]] (-0.59, fdr 1e-05), [[BTN3A3]] (-0.56, fdr 2e-05), [[BTN3A2]] (-0.54, fdr 2e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CDCP1]] → it (grade B ⚠); 22 go from it, the strongest it → [[ACTN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6093.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (C32 3.09×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (Hs 766T 7.37×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +4.3 | 0.010 | 17/40 (SW480, C32, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +3.9 | 0.023 | 21/39 (HT-29, NCI-H1792, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.040 | 20/38 (HT-29, RPMI-7951, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.18× | +3.3 | 0.13 | 15/39 (A-172, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6093.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.228×** | -21.3 | 0e+00 | 39/39 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.244×** | -20.3 | 0e+00 | 39/39 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.332×** | -15.9 | 0e+00 | 39/39 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.464×** | -15.6 | 0e+00 | 35/39 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.518×** | -13.4 | 6e-39 | 33/40 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.503×** | -9.5 | 2e-19 | 30/39 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.614×** | -7.0 | 2e-10 | 27/39 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.616×** | -7.0 | 2e-10 | 29/40 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.605×** | -6.9 | 2e-10 | 24/35 (HepG2/C3A, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.641×** | -6.2 | 4e-08 | 30/39 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.664×** | -5.9 | 2e-07 | 34/39 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.659×** | -5.8 | 3e-07 | 30/41 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.770×** | -5.3 | 5e-06 | 22/39 (NCI-H2347, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.745×** | -5.2 | 6e-06 | 26/39 (AsPC-1, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.714×** | -4.8 | 5e-05 | 27/40 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.719×** | -4.7 | 7e-05 | 28/39 (AsPC-1, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.731×** | -4.5 | 2e-04 | 25/39 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.767×** | -4.3 | 6e-04 | 26/39 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.774×** | -4.2 | 9e-04 | 27/40 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6093. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 331 | 0 | 21 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -22.2) |
| [[AsPC-1 (line)]] | alt | 391 | 0 | 18 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0719× (z -25.5) |
| [[NCI-H460 (line)]] | wt | 310 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -27.9) |
| [[CFPAC-1 (line)]] | alt | 409 | 0 | 14 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -21.1) |
| [[NCI-H1573 (line)]] | alt | 613 | 0 | 13 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0898× (z -34.1) |
| [[LOX-IMVI (line)]] | wt | 284 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.126× (z -16.7) |
| [[MIA PaCa-2 (line)]] | alt | 876 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -21.8) |
| [[NCI-H2030 (line)]] | alt | 312 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -26.2) |
| [[NCI-H23 (line)]] | alt | 152 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -25.5) |
| [[NCI-H2347 (line)]] | alt | 193 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -17.5) |
| [[Hs 766T (line)]] | wt | 504 | 1 (1 ⚠) | 8 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.37× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.0957× (z -19.5) |
| [[RKO (line)]] | wt | 141 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -19.1) |
| [[HOP62 (line)]] | alt | 167 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -19.4) |
| [[Panc 03.27 (line)]] | alt | 499 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0907× (z -19.5) |
| [[PANC-1 (line)]] | alt | 137 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -21.7) |
| [[A549 (line)]] | wt | 167 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -20.4) |
| [[BT-474 (line)]] | alt | 184 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -18.5) |
| [[SNU-423 (line)]] | alt | 263 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -14.5) |
| [[SW1417 (line)]] | alt | 170 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.185× (z -18.3) |
| [[SW48 (line)]] | wt | 186 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -15.2) |
| [[HepG2_C3A (line)]] | wt | 221 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -13.5) |
| [[A-172 (line)]] | wt | 123 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -17.4) |
| [[HS-578T (line)]] | alt | 188 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -16.0) |
| [[HT-29 (line)]] | alt | 171 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -12.1) |
| [[J82 (line)]] | alt | 235 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -15.0) |
| [[LoVo (line)]] | wt | 98.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 94.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -18.6) |
| [[SW480 (line)]] | alt | 139 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -16.1) |
| [[A498 (line)]] | wt | 104 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -17.8) |
| [[H4 (line)]] | wt | 111 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -11.3) |
| [[SW 900 (line)]] | alt | 90.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 106 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.299× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 116 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -10.2) |
| [[SNU-1 (line)]] | wt | 67.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -11.1) |
| [[SW 1271 (line)]] | alt | 235 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0857× (z -10.6) |
| [[C32 (line)]] | wt | 70.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A-427 (line)]] | wt | 49.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 48.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 42.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 52.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 41.6 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 48.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.4 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 243 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6093), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELK3]] | +0.76 | +0.80 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[SMURF2]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_TGF_BETA_SIGNALING |
| [[THSD4]] | +0.68 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[BCL2L1]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[ASAP2]] | +0.65 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[DOCK5]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[LINC00941]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[CAPRIN2]] | +0.64 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[MICAL2]] | +0.64 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[MAP4K4]] | +0.64 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[HMGA2]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[ITGB5]] | +0.63 | +0.65 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN3A1]] | -0.59 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[BTN3A3]] | -0.56 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[BTN3A2]] | -0.54 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[TNFRSF14]] | -0.54 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[TBC1D8B]] | -0.53 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[TLR3]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[UFSP2]] | -0.51 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[GBP2]] | -0.51 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[PLAAT4]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[CCL28]] | -0.50 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[CFAP36]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[TMPRSS3]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCP1]] | B | CDCP1 activity raises BCAR3's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.89× lower at baseline in the lines without CDCP1 | 0.017 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[NTSR1]] | B | NTSR1 activity raises BCAR3's level | lines that do not express NTSR1 (26) vs lines expressing it (24) | 1.78× lower at baseline in the lines without NTSR1 | 0.020 | ⚠ within organs, on part of the lines; also absent: TNFRSF6B, LINC02432, COL17A1 |
| [[TOR4A]] | B | TOR4A activity raises BCAR3's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 1.86× lower at baseline in the lines without TOR4A | 0.021 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[MGLL]] | B | MGLL activity raises BCAR3's level | lines that do not express MGLL (14) vs lines expressing it (36) | 1.93× lower at baseline in the lines without MGLL | 0.022 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[ITGB1-DT]] | B | ITGB1-DT activity raises BCAR3's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 2.45× lower at baseline in the lines without ITGB1-DT | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[S100A16]] | B | S100A16 activity raises BCAR3's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 2.47× lower at baseline in the lines without S100A16 | 0.043 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[BCL2L1]] | B | BCL2L1 activity raises BCAR3's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 2.04× lower at baseline in the lines without BCL2L1 | 0.071 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[SPRY4-AS1]] | C | SPRY4-AS1 activity raises BCAR3's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 3.34× lower at baseline in the lines without SPRY4-AS1 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent |
| [[KIFC3]] | C | KIFC3 activity raises BCAR3's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 3.14× lower at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 20, C 2. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACTN1]] | B | BCAR3 activity raises ACTN1's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 2.37× lower at baseline in the lines without BCAR3 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[KIFC3]] | B | BCAR3 activity raises KIFC3's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 2.62× lower at baseline in the lines without BCAR3 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[MYEOV]] | B | BCAR3 activity raises MYEOV's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 2.44× lower at baseline in the lines without BCAR3 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[OSR2]] | B | BCAR3 activity lowers OSR2's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 2.12× higher at baseline in the lines without BCAR3 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[ABTB3]] | B | BCAR3 activity raises ABTB3's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 3.46× lower at baseline in the lines without BCAR3 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[FHOD3]] | B | BCAR3 activity raises FHOD3's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 2.71× lower at baseline in the lines without BCAR3 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[DOCK4]] | B | BCAR3 activity raises DOCK4's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 2.58× lower at baseline in the lines without BCAR3 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[ASAP1]] | B | BCAR3 activity raises ASAP1's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 1.79× lower at baseline in the lines without BCAR3 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[LINC-PINT]] | B | BCAR3 activity raises LINC-PINT's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 1.57× lower at baseline in the lines without BCAR3 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[MAMLD1]] | B | BCAR3 activity raises MAMLD1's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 3.57× lower at baseline in the lines without BCAR3 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[CDCP1]] | B | BCAR3 activity raises CDCP1's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 2.28× lower at baseline in the lines without BCAR3 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[FOSL1]] | B | BCAR3 activity raises FOSL1's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 2.61× lower at baseline in the lines without BCAR3 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.763). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.0, 7.6); signed map (8.4, 45.0). **Vector** length 116, 41.4% of its response variance represented; |z| ≥ 3 in 1,399 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.9 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.5 | +4.3 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.4 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.4 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.8 | +3.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.3 | +1.7 |
|  | [[vincristine (drug)]] 5 µM |  | +2.8 | +1.5 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -6.5 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.4 | -5.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.3 | -4.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -6.0 | -4.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.9 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.7 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | BCAR3 adaptor protein, NSP family member |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:93,561,741-93,847,150 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NSP2, SH2D3B, AND-34, MIG7 |
| Gene groups (HGNC) | SH2 domain containing; NSP adaptor proteins |
| Hallmark sets | TGF_BETA_SIGNALING, BILE_ACID_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [O75815](https://www.uniprot.org/uniprotkb/O75815) (Breast cancer anti-estrogen resistance protein 3):

> Acts as an adapter protein downstream of several growth factor receptors to promote cell proliferation, migration, and redistribution of actin fibers. Specifically involved in INS/insulin signaling pathway by mediating MAPK1/ERK2-MAPK3/ERK1 activation and DNA synthesis. Promotes insulin-mediated membrane ruffling (By similarity). In response to vasoconstrictor peptide EDN1, involved in the activation of RAP1 downstream of PTK2B via interaction with phosphorylated BCAR1. Inhibits cell migration …

**Summary**, from NCBI Gene [8412](https://www.ncbi.nlm.nih.gov/gene/8412):

> Breast tumors are initially dependent on estrogens for growth and progression and can be inhibited by anti-estrogens such as tamoxifen. However, breast cancers progress to become anti-estrogen resistant. Breast cancer anti-estrogen resistance gene 3 was identified in the search for genes involved in the development of estrogen resistance. The gene encodes a component of intracellular signal transduction that causes estrogen-independent proliferation in human breast cancer cells. The protein …

**Accessions** — [HGNC:973](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:973) · Entrez [8412](https://www.ncbi.nlm.nih.gov/gene/8412) · UniProt [O75815](https://www.uniprot.org/uniprotkb/O75815) · Ensembl [ENSG00000137936](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137936)

## Data

Gene col 6093: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6093); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6093, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6093]; `tensor/DDL_lfc|DDL_z.npy` [6093]; `embed/gene_vectors.npy` [6093]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6093 or target_col == 6093). Every well: [[BCAR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCAR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
