---
symbol: "DTWD2"
type: "gene"
col: 9819
ensembl_id: "ENSG00000169570"
name: "DTW motif tRNA-uridine aminocarboxypropyltransferase 2"
location: "5q23.1"
module: 4
arm: "+"
pooled_cpm: 21.66
n_lines_expressing: 48
n_dd_up: 14
n_dd_down: 35
n_dd_up_clean: 10
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# DTWD2

*DTW motif tRNA-uridine aminocarboxypropyltransferase 2* — 5q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.52× (z +5.9, q 1e-06, up in 29 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.395× (z -19.4, q 0e+00, down in 37 of 45 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.399× (z -19.1, q 0e+00, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPA2]] (+0.64, fdr 1e-05), [[LHPP]] (+0.62, fdr 1e-05), [[MRPL19]] (+0.60, fdr 1e-05); moves opposite to [[PPP1R13L]] (-0.59, fdr 7e-06), [[SLC10A3]] (-0.56, fdr 4e-05), [[CATSPERG]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SLC5A4-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9819.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +5.9 | 1e-06 | 29/45 (HEC-1-A, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +5.9 | 1e-06 | 26/45 (H4, LOX-IMVI, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +4.7 | 5e-04 | 22/45 (SW480, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.004 | 15/46 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.32×** | +4.1 | 0.004 | 14/46 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.004 | 17/45 (PANC-1, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.30×** | +3.9 | 0.009 | 14/45 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.21×** | +3.8 | 0.011 | 16/46 (C32, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +3.7 | 0.012 | 15/46 (C32, SW480, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.29×** | +3.7 | 0.012 | 12/41 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.022 | 9/46 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.4 | 0.037 | 14/29 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.17× | +3.3 | 0.037 | 9/46 (LoVo, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Encorafenib (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.037 | 6/46 (C32, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.058 | 12/45 (HOP62, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9819.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.395×** | -19.4 | 0e+00 | 37/45 (NCI-H1792, PANC-1, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.399×** | -19.1 | 0e+00 | 41/45 (C32, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.453×** | -11.7 | 4e-29 | 36/44 (PANC-1, HCT15, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.457×** | -11.5 | 1e-28 | 35/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.481×** | -10.4 | 4e-23 | 32/45 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.547×** | -8.5 | 1e-15 | 33/45 (C32, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.589×** | -7.8 | 5e-13 | 29/45 (HEC-1-A, J82, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.600×** | -7.5 | 4e-12 | 27/45 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.603×** | -7.5 | 6e-12 | 26/44 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.601×** | -7.2 | 3e-11 | 26/45 (NCI-H1792, PANC-1, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.714×** | -7.0 | 1e-10 | 28/46 (SNU-423, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.638×** | -6.6 | 2e-09 | 27/45 (PANC-1, SNU-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.751×** | -6.0 | 1e-07 | 27/46 (CHP-212, NCI-H661, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.678×** | -5.7 | 4e-07 | 25/45 (SW48, C32, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.684×** | -5.6 | 8e-07 | 24/45 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.597×** | -5.4 | 2e-06 | 22/45 (SK-MEL-2, BT-474, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.705×** | -5.1 | 8e-06 | 21/45 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.705×** | -5.1 | 8e-06 | 20/45 (C32, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.724×** | -4.8 | 5e-05 | 20/45 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.734×** | -4.4 | 3e-04 | 21/45 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.735×** | -4.4 | 3e-04 | 16/46 (NCI-H23, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9819. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.6 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -21.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.165× (z -13.9) |
| [[PANC-1 (line)]] | alt | 19.7 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -26.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -19.0) |
| [[C32 (line)]] | wt | 85.5 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -23.2) |
| [[LoVo (line)]] | wt | 51.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -18.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -16.9) |
| [[NCI-H1573 (line)]] | alt | 36.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -17.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -17.4) |
| [[SNU-1 (line)]] | wt | 35.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0992× (z -13.1) |
| [[HT-29 (line)]] | alt | 19.4 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0819× (z -14.5) |
| [[LS 180 (line)]] | wt | 36.2 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -14.5) |
| [[NCI-H1792 (line)]] | alt | 33.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0765× (z -26.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 46.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -14.2) |
| [[SNU-423 (line)]] | alt | 13.1 | 0 | 3 (1 ⚠) | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.106× (z -11.4) |
| [[SW480 (line)]] | alt | 21.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -13.1) |
| [[C-33 A (line)]] | alt | 46.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -9.3) |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0583× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Palmatine (chloride) (drug)]] 0.5 µM 0.0880× (z -11.5) |
| [[HS-578T (line)]] | alt | 15.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 24.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -13.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -13.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 34.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -19.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -18.5) |
| [[NCI-H23 (line)]] | alt | 18.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -15.0) |
| [[SK-MEL-2 (line)]] | alt | 31.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0745× (z -24.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 36.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -11.1) |
| [[A-172 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.288× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 23.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -11.8) |
| [[A498 (line)]] | wt | 15.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -8.5) |
| [[COLO 205 (line)]] | alt | 25.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 24.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -9.3) |
| [[HOP62 (line)]] | alt | 9.43 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -8.6) |
| [[RKO (line)]] | wt | 18.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0936× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 9.75 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0807× (z -12.6) ⚠ toxic; cell-cycle shift, explains ~46% of this change |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -9.1) |
| [[A549 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.41 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9819), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPA2]] | +0.64 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[LHPP]] | +0.62 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[MRPL19]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[TSEN15]] | +0.59 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[HSD17B4]] | +0.58 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[SSX2IP]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[MRPL42]] | +0.56 | +0.39 / +0.58 | both halves | 6e-05 |  |
| [[NBN]] | +0.56 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[FXN]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[RAD23B]] | +0.55 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[EHMT2]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[HEATR3]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R13L]] | -0.59 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[SLC10A3]] | -0.56 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[CATSPERG]] | -0.54 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[ELL]] | -0.53 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[ZNF324]] | -0.51 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[TTLL3]] | -0.51 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[TRNAU1AP]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[TRPC1]] | -0.50 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[TNFAIP1]] | -0.49 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[TOB2]] | -0.48 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[C11orf91]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PRPSAP1]] | -0.48 | -0.33 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC5A4-AS1]] | B | SLC5A4-AS1 activity raises DTWD2's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.95× lower at baseline in the lines without SLC5A4-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[PIR]] | B | PIR activity raises DTWD2's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.60× lower at baseline in the lines without PIR | 0.042 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises DTWD2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers DTWD2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.406). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-27.8, -15.3); signed map (-16.9, -44.8). **Vector** length 93.8, 22.5% of its response variance represented; |z| ≥ 3 in 1,182 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.6 | +0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +5.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -19.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -8.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.5 | -7.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -5.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.3 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | DTW motif tRNA-uridine aminocarboxypropyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.1 — chr5:118,836,074-118,988,547 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33977 |
| Gene groups (HGNC) | DTW motif tRNA-uridine aminocarboxypropyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBA8](https://www.uniprot.org/uniprotkb/Q8NBA8) (tRNA-uridine aminocarboxypropyltransferase 2):

> Catalyzes the formation of 3-(3-amino-3-carboxypropyl)uridine (acp3U) at position 20a in the D-loop of several cytoplasmic tRNAs (acp3U(20a)). Also has a weak activity to form acp3U at position 20 in the D-loop of tRNAs (acp3U(20)). Involved in glycoRNA biosynthesis by mediating formation of acp3U, which acts as an attachment site for N-glycans on tRNAs. GlycoRNAs consist of RNAs modified with secretory N-glycans that are presented on the cell surface.

**Summary**, from NCBI Gene [285605](https://www.ncbi.nlm.nih.gov/gene/285605):

> Enables tRNA-uridine aminocarboxypropyltransferase activity. Involved in glycoRNA biosynthetic process and tRNA modification. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19334](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19334) · Entrez [285605](https://www.ncbi.nlm.nih.gov/gene/285605) · UniProt [Q8NBA8](https://www.uniprot.org/uniprotkb/Q8NBA8) · Ensembl [ENSG00000169570](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169570)

## Data

Gene col 9819: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9819); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9819, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9819]; `tensor/DDL_lfc|DDL_z.npy` [9819]; `embed/gene_vectors.npy` [9819]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9819 or target_col == 9819). Every well: [[DTWD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DTWD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
