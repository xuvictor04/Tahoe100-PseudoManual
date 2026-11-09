---
symbol: "SH3BP2"
type: "gene"
col: 1495
ensembl_id: "ENSG00000087266"
name: "SH3 domain binding protein 2"
location: "4p16.3"
module: 2
arm: "+"
pooled_cpm: 41.62
n_lines_expressing: 42
n_dd_up: 0
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 11
direction_downstream: 9
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# SH3BP2

*SH3 domain binding protein 2* — 4p16.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 1 line (A498 2.79×; ⚠ cell-cycle shift, explains ~43% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 3.85×; ⚠ cell-cycle shift, explains ~58% of this change).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.606× (z -11.1, q 7e-26, down in 31 of 41 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INF2]] (+0.65, fdr 9e-06), [[SLC17A9]] (+0.58, fdr 1e-05), [[AHDC1]] (+0.56, fdr 4e-05); moves opposite to [[ATE1]] (-0.48, fdr 1e-04), [[SMIM10L1]] (-0.47, fdr 6e-05), [[ARID2]] (-0.46, fdr 4e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[ADAM8]] → it (grade B ⚠); 9 go from it, the strongest it → [[MLPH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1495.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 1 line (A498 2.79×; ⚠ cell-cycle shift, explains ~43% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 3.85×; ⚠ cell-cycle shift, explains ~58% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.36× | +3.5 | 0.25 | 7/40 (LoVo, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.23× | +3.3 | 0.28 | 19/39 (SW48, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 1.21× | +3.1 | 0.42 | 6/40 (CFPAC-1, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1495.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.606×** | -11.1 | 7e-26 | 31/41 (Panc 03.27, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.577×** | -8.6 | 2e-15 | 29/39 (Hs 766T, A549, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.582×** | -8.5 | 3e-15 | 25/40 (H4, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.614×** | -7.6 | 3e-12 | 26/40 (AsPC-1, A-172, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.617×** | -7.6 | 4e-12 | 23/40 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.720×** | -7.3 | 4e-11 | 27/40 (A549, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.416×** | -7.2 | 5e-11 | 27/41 (CFPAC-1, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.652×** | -6.7 | 1e-09 | 26/40 (H4, LoVo, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.647×** | -6.6 | 3e-09 | 25/40 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.658×** | -6.3 | 2e-08 | 23/38 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.470×** | -6.2 | 3e-08 | 24/39 (HOP62, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.678×** | -6.1 | 6e-08 | 25/40 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.680×** | -6.0 | 6e-08 | 27/40 (COLO 205, AsPC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.766×** | -5.9 | 2e-07 | 22/39 (Hs 766T, COLO 205, …) | two highest doses | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.690×** | -5.8 | 2e-07 | 23/40 (AsPC-1, HT-29, …) | two highest doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.795×** | -5.1 | 1e-05 | 24/40 (A-172, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.725×** | -5.0 | 1e-05 | 21/40 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.775×** | -4.0 | 0.002 | 17/40 (Hs 766T, HCT15, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.798×** | -3.5 | 0.010 | 16/41 (BT-474, J82, …) | top dose only |  |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.816×** | -3.2 | 0.035 | 10/39 (BT-474, HepG2/C3A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **0.820×** | -3.1 | 0.042 | 12/41 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | **0.831×** | -2.9 | 0.082 | 8/40 (SK-MEL-2, AsPC-1, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.832×** | -2.9 | 0.082 | 10/40 (RKO, BT-474, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1495. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 80.0 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -18.3) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -17.1) |
| [[Hs 766T (line)]] | wt | 78.9 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -20.4) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -16.1) |
| [[HT-29 (line)]] | alt | 144 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -18.0) |
| [[A-172 (line)]] | wt | 149 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.463× (z -8.9) |
| [[A549 (line)]] | wt | 15.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -13.1) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.222× (z -13.1) |
| [[AsPC-1 (line)]] | alt | 70.3 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -14.7) |
| [[H4 (line)]] | wt | 52.2 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.5) ⚠ cell-cycle shift, explains ~58% of this change |
| [[HCT15 (line)]] | alt | 103 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -13.3) |
| [[HOP62 (line)]] | alt | 78.8 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -14.6) |
| [[Panc 03.27 (line)]] | alt | 56.5 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -18.5) |
| [[J82 (line)]] | alt | 72.3 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -11.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.9) |
| [[PANC-1 (line)]] | alt | 54.6 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.294× (z -12.0) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.451× (z -11.4) |
| [[COLO 205 (line)]] | alt | 70.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -19.5) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -13.3) |
| [[SW 1088 (line)]] | alt | 99.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0912× (z -13.2) |
| [[A498 (line)]] | wt | 88.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.79× (z +10.0) ⚠ cell-cycle shift, explains ~43% of this change | [[Dinaciclib (drug)]] 5 µM 0.270× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 76.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Radotinib (drug)]] 0.5 µM 0.195× (z -8.8) |
| [[KATO III (line)]] | alt | 66.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -14.7) |
| [[LoVo (line)]] | wt | 25.4 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.300× (z -9.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[RKO (line)]] | wt | 23.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -10.9) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 30.3 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0527× (z -14.6) ⚠ toxic; cell-cycle shift, explains ~94% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -8.9) |
| [[SNU-423 (line)]] | alt | 33.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -14.4) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 42.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 22.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +9.9) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[LS 180 (line)]] | wt | 41.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -8.7) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -9.6) |
| [[SW480 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -11.3) ⚠ cell-cycle shift, explains ~58% of this change |
| [[A-427 (line)]] | wt | 7.28 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.36 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.95 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.05 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.21 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.26 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1495), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INF2]] | +0.65 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[SLC17A9]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.56 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[TPCN2]] | +0.56 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[NCOR2]] | +0.56 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[EPS8L2]] | +0.54 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[TCIRG1]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[PLEKHO2]] | +0.52 | +0.46 / +0.39 | both halves | 6e-05 | same gene group |
| [[SYTL1]] | +0.52 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[ARHGAP45]] | +0.52 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[PLXNA3]] | +0.52 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[TNKS1BP1]] | +0.51 | +0.43 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATE1]] | -0.48 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[SMIM10L1]] | -0.47 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[ARID2]] | -0.46 | -0.38 / -0.25 | both halves | 4e-04 |  |
| [[MACROH2A2]] | -0.45 | -0.49 / -0.25 | both halves | 4e-04 |  |
| [[TCF12]] | -0.44 | -0.50 / -0.21 | both halves | 6e-04 |  |
| [[DPY19L1P1]] | -0.44 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[RMDN2]] | -0.43 | -0.49 / -0.21 | both halves | 7e-04 |  |
| [[CASD1]] | -0.43 | -0.44 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM8]] | B | ADAM8 activity raises SH3BP2's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 2.42× lower at baseline in the lines without ADAM8 | 6e-04 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[EPS8L2]] | B | EPS8L2 activity raises SH3BP2's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 2.15× lower at baseline in the lines without EPS8L2 | 0.010 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[ALS2CL]] | B | ALS2CL activity raises SH3BP2's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 1.69× lower at baseline in the lines without ALS2CL | 0.020 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[P2RY2]] | B | P2RY2 activity raises SH3BP2's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 1.87× lower at baseline in the lines without P2RY2 | 0.030 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[TOP2A]] | B | TOP2A activity raises SH3BP2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PTK6]] | B | PTK6 activity raises SH3BP2's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 1.61× lower at baseline in the lines without PTK6 | 0.041 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[PRSS8]] | B | PRSS8 activity raises SH3BP2's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 1.83× lower at baseline in the lines without PRSS8 | 0.048 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[SEMA3B]] | B | SEMA3B activity raises SH3BP2's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.23× lower at baseline in the lines without SEMA3B | 0.058 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[SLCO4A1]] | B | SLCO4A1 activity raises SH3BP2's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 2.89× lower at baseline in the lines without SLCO4A1 | 0.075 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[PKP3]] | B | PKP3 activity raises SH3BP2's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 1.50× lower at baseline in the lines without PKP3 | 0.081 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent |
| [[CRACR2B]] | B | CRACR2B activity raises SH3BP2's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 1.37× lower at baseline in the lines without CRACR2B | 0.089 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLPH]] | B | SH3BP2 activity raises MLPH's level | lines that do not express SH3BP2 (8) vs lines expressing it (42) | 2.88× lower at baseline in the lines without SH3BP2 | 0.023 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[INF2]] | B | SH3BP2 activity raises INF2's level | lines that do not express SH3BP2 (8) vs lines expressing it (42) | 1.98× lower at baseline in the lines without SH3BP2 | 0.025 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[EPS8L2]] | B | SH3BP2 activity raises EPS8L2's level | lines that do not express SH3BP2 (8) vs lines expressing it (42) | 2.93× lower at baseline in the lines without SH3BP2 | 0.057 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SEPTIN9]] | B | SH3BP2 activity raises SEPTIN9's level | lines that do not express SH3BP2 (8) vs lines expressing it (42) | 1.91× lower at baseline in the lines without SH3BP2 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ALS2CL]] | B | SH3BP2 activity raises ALS2CL's level | lines that do not express SH3BP2 (8) vs lines expressing it (42) | 2.11× lower at baseline in the lines without SH3BP2 | 0.067 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ADAM8]] | B | SH3BP2 activity raises ADAM8's level | lines that do not express SH3BP2 (8) vs lines expressing it (42) | 2.26× lower at baseline in the lines without SH3BP2 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[C15orf39]] | B | SH3BP2 activity raises C15orf39's level | lines that do not express SH3BP2 (8) vs lines expressing it (42) | 1.69× lower at baseline in the lines without SH3BP2 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IFITM10]] | B | SH3BP2 activity raises IFITM10's level | lines that do not express SH3BP2 (8) vs lines expressing it (42) | 2.11× lower at baseline in the lines without SH3BP2 | 0.090 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAPK11]] | B | SH3BP2 activity lowers MAPK11's level | lines that do not express SH3BP2 (8) vs lines expressing it (42) | 1.40× higher at baseline in the lines without SH3BP2 | 0.090 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.471). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (14.7, -4.7); signed map (-11.7, 30.4). **Vector** length 100, 24.9% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +3.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.9 | +0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | -0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +2.6 | -5.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.3 | +2.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.1 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | -0.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.8 | -7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.4 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -5.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.0 | -7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -6.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -2.3 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.1 | -3.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:2,793,023-2,841,291 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RES4-23, CRBM |
| Gene groups (HGNC) | Pleckstrin homology domain containing; SH2 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P78314](https://www.uniprot.org/uniprotkb/P78314) (SH3 domain-binding protein 2):

> Adapter protein, which binds differentially to the SH3 domains of certain proteins of signal transduction pathways. Binds to phosphatidylinositols; linking the hemopoietic tyrosine kinase fes to the cytoplasmic membrane in a phosphorylation dependent mechanism.

**Summary**, from NCBI Gene [6452](https://www.ncbi.nlm.nih.gov/gene/6452):

> The protein encoded by this gene has an N-terminal pleckstrin homology (PH) domain, an SH3-binding proline-rich region, and a C-terminal SH2 domain. The protein binds to the SH3 domains of several proteins including the ABL1 and SYK protein tyrosine kinases , and functions as a cytoplasmic adaptor protein to positively regulate transcriptional activity in T, natural killer (NK), and basophilic cells. Mutations in this gene result in cherubism. Multiple transcript variants encoding different …

**Accessions** — [HGNC:10825](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10825) · Entrez [6452](https://www.ncbi.nlm.nih.gov/gene/6452) · UniProt [P78314](https://www.uniprot.org/uniprotkb/P78314) · Ensembl [ENSG00000087266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087266)

## Data

Gene col 1495: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1495); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1495, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1495]; `tensor/DDL_lfc|DDL_z.npy` [1495]; `embed/gene_vectors.npy` [1495]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1495 or target_col == 1495). Every well: [[SH3BP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3BP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
