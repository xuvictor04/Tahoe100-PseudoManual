---
symbol: "GPR39"
type: "gene"
col: 11463
ensembl_id: "ENSG00000183840"
name: "G protein-coupled receptor 39"
location: "2q21.2"
module: 120
arm: "+"
pooled_cpm: 68.89
n_lines_expressing: 39
n_dd_up: 2
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 18
direction_downstream: 30
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# GPR39

*G protein-coupled receptor 39* — 2q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.85× (z +6.1, q 6e-07, up in 23 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 6 lines (COLO 205 8.53×, HOP62 5.78×, LOX-IMVI 5.15×, NCI-H23 4.15×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (AsPC-1 5.14×, LOX-IMVI 5.75×, HOP62 4.16×, HS-578T 4.83×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (NCI-H460 2.70×).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.444× (z -7.1, q 9e-10, down in 24 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.628× (z -6.4, q 2e-08, down in 24 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAV3]] (+0.61, fdr 7e-06), [[AMIGO2]] (+0.61, fdr 1e-05), [[SLC22A3]] (+0.60, fdr 1e-05); moves opposite to [[ARNT]] (-0.58, fdr 1e-05), [[SSBP2]] (-0.56, fdr 1e-05), [[SLC19A2]] (-0.54, fdr 1e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[IL31RA]] → it (grade B ⚠); 30 go from it, the strongest it → [[FLYWCH2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11463.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 6 lines (COLO 205 8.53×, HOP62 5.78×, LOX-IMVI 5.15×, NCI-H23 4.15×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (AsPC-1 5.14×, LOX-IMVI 5.75×, HOP62 4.16×, HS-578T 4.83×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (NCI-H460 2.70×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +6.1 | 6e-07 | 23/37 (COLO 205, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.57×** | +4.5 | 0.002 | 24/37 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.38× | +3.1 | 0.39 | 16/37 (NCI-H2347, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11463.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.444×** | -7.1 | 9e-10 | 24/38 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.490×** | -6.7 | 4e-09 | 21/34 (LoVo, H4, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -6.4 | 2e-08 | 24/37 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.525×** | -6.3 | 3e-08 | 29/37 (HEC-1-A, SNU-423, …) | two highest doses | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.606×** | -4.9 | 1e-04 | 24/37 (HEC-1-A, Panc 03.27, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.587×** | -4.8 | 1e-04 | 22/34 (LoVo, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.635×** | -4.5 | 7e-04 | 21/36 (LS 180, LoVo, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.638×** | -4.4 | 7e-04 | 23/37 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.629×** | -4.4 | 8e-04 | 22/36 (HepG2/C3A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.644×** | -4.3 | 9e-04 | 23/37 (HEC-1-A, LS 180, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.654×** | -4.0 | 0.003 | 22/37 (SNU-423, H4, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.674×** | -3.9 | 0.005 | 25/36 (KATO III, H4, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -3.5 | 0.017 | 20/38 (HEC-1-A, SW48, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.775×** | -3.5 | 0.018 | 21/37 (SNU-423, H4, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | **0.798×** | -3.1 | 0.073 | 19/38 (HS-578T, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11463. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 117 | 1 (1 ⚠) | 19 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Betamethasone dipropionate (drug)]] 5 µM 0.179× (z -12.8) |
| [[LoVo (line)]] | wt | 102 | 0 | 14 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0492× (z -22.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -9.3) |
| [[LS 180 (line)]] | wt | 141 | 0 | 11 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0623× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.216× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 232 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -17.6) |
| [[SW480 (line)]] | alt | 77.1 | 0 | 9 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -14.7) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -10.6) |
| [[HOP62 (line)]] | alt | 50.6 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.78× (z +12.1) | [[Budesonide (drug)]] 0.05 µM 0.251× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 141 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.279× (z -10.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.286× (z -10.0) |
| [[A498 (line)]] | wt | 86.7 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -9.0) |
| [[A549 (line)]] | wt | 112 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 91.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +16.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.76× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 67.9 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.137× (z -10.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -8.9) |
| [[HS-578T (line)]] | alt | 48.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.12× (z +9.8) | — |
| [[KATO III (line)]] | alt | 38.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 66.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +16.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.15× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 134 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.210× (z -9.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 117 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.15× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0858× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 55.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 76.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -9.5) |
| [[COLO 205 (line)]] | alt | 66.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.53× (z +12.4) | — |
| [[H4 (line)]] | wt | 83.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0757× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 69.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 21.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.70× (z +9.4) | — |
| [[SW48 (line)]] | wt | 98.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -9.9) |
| [[A-172 (line)]] | wt | 8.51 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.89 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.78 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.80 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.87 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.66 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 76.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11463), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAV3]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[AMIGO2]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SLC22A3]] | +0.60 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[RASGRF2]] | +0.60 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[SYNJ2]] | +0.59 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[FAT1]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SH3RF1]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[CCND1]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ENC1]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[LINC00973]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[SH3D19]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ME3]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARNT]] | -0.58 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[SSBP2]] | -0.56 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[SLC19A2]] | -0.54 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[CBLB]] | -0.51 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[FLYWCH2]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[TSC22D3]] | -0.50 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[MAX]] | -0.50 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[ELF2]] | -0.50 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[PPOX]] | -0.50 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[CNOT8]] | -0.49 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[EZH1]] | -0.48 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[UGP2]] | -0.48 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 15, C 3. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL31RA]] | B | IL31RA activity raises GPR39's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without IL31RA | 0.010 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1 |
| [[SLC35F3]] | B | SLC35F3 activity raises GPR39's level | lines that do not express SLC35F3 (27) vs lines expressing it (23) | 2.43× lower at baseline in the lines without SLC35F3 | 0.011 | ⚠ within organs, on part of the lines; also absent: RHCG, THBD, NR2E3 |
| [[LINC00707]] | B | LINC00707 activity raises GPR39's level | lines that do not express LINC00707 (26) vs lines expressing it (24) | 2.00× lower at baseline in the lines without LINC00707 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000285845, ENSG00000285743, LINP1 |
| [[PPP1R1C]] | B | PPP1R1C activity raises GPR39's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 2.74× lower at baseline in the lines without PPP1R1C | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[PCED1B]] | B | PCED1B activity raises GPR39's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 3.09× lower at baseline in the lines without PCED1B | 0.020 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[LINC01589]] | B | LINC01589 activity raises GPR39's level | lines that do not express LINC01589 (23) vs lines expressing it (27) | 3.06× lower at baseline in the lines without LINC01589 | 0.021 | ⚠ within organs, on part of the lines; also absent: HNF1B, ENSG00000279806, GOLT1A |
| [[B3GALT5]] | B | B3GALT5 activity raises GPR39's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 2.48× lower at baseline in the lines without B3GALT5 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1 |
| [[ITGA6]] | B | ITGA6 activity raises GPR39's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 2.35× lower at baseline in the lines without ITGA6 | 0.041 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SHH]] | B | SHH activity raises GPR39's level | lines that do not express SHH (29) vs lines expressing it (21) | 2.52× lower at baseline in the lines without SHH | 0.044 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[LAMA3]] | B | LAMA3 activity raises GPR39's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.76× lower at baseline in the lines without LAMA3 | 0.049 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[AMIGO2]] | B | AMIGO2 activity raises GPR39's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 2.93× lower at baseline in the lines without AMIGO2 | 0.049 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[SLC22A3]] | B | SLC22A3 activity raises GPR39's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.38× lower at baseline in the lines without SLC22A3 | 0.052 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 27, C 3. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLYWCH2]] | B | GPR39 activity lowers FLYWCH2's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 1.48× higher at baseline in the lines without GPR39 | 0.003 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[ITGA6]] | B | GPR39 activity raises ITGA6's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 2.66× lower at baseline in the lines without GPR39 | 0.003 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[FOSL1]] | B | GPR39 activity raises FOSL1's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 2.34× lower at baseline in the lines without GPR39 | 0.006 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[LAMA3]] | B | GPR39 activity raises LAMA3's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 5.12× lower at baseline in the lines without GPR39 | 0.011 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[PCED1B]] | B | GPR39 activity raises PCED1B's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 3.88× lower at baseline in the lines without GPR39 | 0.011 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[SYNJ2]] | B | GPR39 activity raises SYNJ2's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 2.23× lower at baseline in the lines without GPR39 | 0.016 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[SLC35F3]] | B | GPR39 activity raises SLC35F3's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 2.87× lower at baseline in the lines without GPR39 | 0.030 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[PLEKHA6]] | B | GPR39 activity raises PLEKHA6's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 2.87× lower at baseline in the lines without GPR39 | 0.034 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | GPR39 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express GPR39 (11) vs lines expressing it (37) | the lines without GPR39: 0.80× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[ANKRD20A5P]] | B | GPR39 activity raises ANKRD20A5P's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 3.26× lower at baseline in the lines without GPR39 | 0.044 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[CXCL8]] | B | GPR39 activity raises CXCL8's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 2.88× lower at baseline in the lines without GPR39 | 0.052 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[MAMLD1]] | B | GPR39 activity raises MAMLD1's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 1.80× lower at baseline in the lines without GPR39 | 0.057 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.6, 13.8); signed map (15.3, 42.1). **Vector** length 125, 40.3% of its response variance represented; |z| ≥ 3 in 1,075 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +6.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.4 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +4.5 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -4.5 | -3.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -4.1 | -4.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -4.0 | -4.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.9 | -2.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -3.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor 39 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.2 — chr2:132,416,805-132,646,582 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZnR |
| Gene groups (HGNC) | G protein-coupled receptors, Class A orphans |
| Reactome | 6 pathways, smallest: G alpha (s) signalling events; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [O43194](https://www.uniprot.org/uniprotkb/O43194) (G protein-coupled receptor 39):

> Zinc-sensing receptor that can sense changes in extracellular Zn(2+), mediate Zn(2+) signal transmission, and participates in the regulation of numerous physiological processes including glucose homeostasis regulation, gastrointestinal mobility, hormone secretion and cell death. Activation by Zn(2+) in keratinocytes increases the intracellular concentration of Ca(2+) and activates the ERK/MAPK and PI3K/AKT signaling pathways leading to epithelial repair. Plays an essential role in normal wound …

**Summary**, from NCBI Gene [2863](https://www.ncbi.nlm.nih.gov/gene/2863):

> This gene is a member of the ghrelin receptor family and encodes a rhodopsin-type G-protein-coupled receptor (GPCR). The encoded protein is involved in zinc-dependent signaling in epithelial tissue in intestines, prostate and salivary glands. The protein may also be involved in the pathophysiology of depression. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:4496](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4496) · Entrez [2863](https://www.ncbi.nlm.nih.gov/gene/2863) · UniProt [O43194](https://www.uniprot.org/uniprotkb/O43194) · Ensembl [ENSG00000183840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183840)

## Data

Gene col 11463: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11463); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11463, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11463]; `tensor/DDL_lfc|DDL_z.npy` [11463]; `embed/gene_vectors.npy` [11463]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11463 or target_col == 11463). Every well: [[GPR39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPR39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
