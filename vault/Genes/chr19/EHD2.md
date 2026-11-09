---
symbol: "EHD2"
type: "gene"
col: 356
ensembl_id: "ENSG00000024422"
name: "EH domain containing 2"
location: "19q13.33"
module: 218
arm: "+"
pooled_cpm: 61.32
n_lines_expressing: 36
n_dd_up: 0
n_dd_down: 42
n_dd_up_clean: 0
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 5
direction_downstream: 10
tags: ["gene", "module/218"]
generated_by: "tahoemap"
---

# EHD2

*EH domain containing 2* — 19q13.33

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 1 line (SW1417 3.23×).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (17 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.278× (z -30.3, q 0e+00, down in 34 of 34 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAM2]] (+0.62, fdr 2e-05), [[PORCN]] (+0.62, fdr 1e-05), [[NUMBL]] (+0.60, fdr 1e-05); moves opposite to [[HNF4G]] (-0.54, fdr 4e-05), [[MCM9]] (-0.53, fdr 4e-05), [[DPY19L1P1]] (-0.52, fdr 7e-05).
> It is in [[Module 218]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LOX]] → it (grade B ⚠); 10 go from it, the strongest it → [[NDRG1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 356.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 1 line (SW1417 3.23×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.19× | +4.2 | 0.013 | 13/34 (NCI-H2030, A549, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.25 | 15/33 (NCI-H2030, H4, …) | rises with dose | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.05 µM |  | 1.22× | +3.1 | 0.25 | 13/34 (A498, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.25 | 15/34 (RPMI-7951, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.22× | +3.0 | 0.25 | 14/33 (H4, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 356.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.278×** | -30.3 | 0e+00 | 34/34 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.399×** | -21.7 | 0e+00 | 31/34 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.377×** | -14.6 | 1e-45 | 31/34 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.418×** | -14.5 | 1e-45 | 30/34 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.459×** | -13.0 | 2e-36 | 29/34 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.480×** | -12.2 | 2e-32 | 29/34 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.450×** | -11.9 | 7e-31 | 33/33 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.468×** | -11.3 | 6e-28 | 28/33 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.486×** | -10.8 | 3e-25 | 29/34 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.502×** | -10.3 | 5e-23 | 30/35 (LOX-IMVI, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.569×** | -9.4 | 2e-19 | 25/34 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.623×** | -7.9 | 1e-13 | 26/34 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.600×** | -7.9 | 2e-13 | 23/31 (HCT15, C32, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.617×** | -7.6 | 1e-12 | 21/34 (HOP62, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **0.641×** | -7.4 | 5e-12 | 23/34 (HCT15, HOP62, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.734×** | -7.3 | 1e-11 | 21/34 (SNU-423, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.651×** | -7.1 | 3e-11 | 24/34 (LOX-IMVI, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.743×** | -7.0 | 9e-11 | 22/34 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.671×** | -6.7 | 9e-10 | 25/34 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.678×** | -6.5 | 3e-09 | 25/34 (LOX-IMVI, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.674×** | -5.9 | 8e-08 | 27/34 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.729×** | -5.3 | 3e-06 | 21/34 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.760×** | -4.1 | 9e-04 | 17/34 (hTERT-HPNE, HS-578T, …) | top dose only | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.786×** | -4.0 | 0.001 | 17/34 (NCI-H23, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.54 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 356. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 76.1 | 0 | 20 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -20.8) |
| [[C32 (line)]] | wt | 77.3 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0950× (z -26.8) |
| [[H4 (line)]] | wt | 137 | 0 | 13 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -17.4) |
| [[LOX-IMVI (line)]] | wt | 72.3 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -15.4) |
| [[NCI-H1792 (line)]] | alt | 90.5 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -25.6) |
| [[CFPAC-1 (line)]] | alt | 94.4 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -27.4) |
| [[HS-578T (line)]] | alt | 245 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 78.8 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -24.2) |
| [[A-172 (line)]] | wt | 106 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.344× (z -12.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -12.1) |
| [[hTERT-HPNE (line)]] | wt | 161 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -16.0) |
| [[RPMI-7951 (line)]] | alt | 227 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -23.1) |
| [[NCI-H1573 (line)]] | alt | 24.0 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -15.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -13.8) |
| [[PANC-1 (line)]] | alt | 49.3 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -17.4) |
| [[NCI-H2347 (line)]] | alt | 91.9 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -15.8) |
| [[SK-MEL-2 (line)]] | alt | 53.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -18.8) |
| [[SW 900 (line)]] | alt | 67.4 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -16.0) |
| [[A549 (line)]] | wt | 110 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -15.4) |
| [[SNU-423 (line)]] | alt | 71.3 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -17.6) |
| [[HCT15 (line)]] | alt | 75.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0547× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -19.3) |
| [[NCI-H23 (line)]] | alt | 23.1 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.123× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 69.9 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -26.3) |
| [[Hs 766T (line)]] | wt | 112 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -19.7) |
| [[KATO III (line)]] | alt | 59.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -22.2) |
| [[LoVo (line)]] | wt | 19.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -13.9) |
| [[HEC-1-A (line)]] | alt | 28.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -13.8) |
| [[HT-29 (line)]] | alt | 42.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -19.7) |
| [[J82 (line)]] | alt | 132 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -14.6) |
| [[SW 1088 (line)]] | alt | 160 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -11.8) |
| [[SW1417 (line)]] | alt | 16.5 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 3.23× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -12.8) |
| [[SW48 (line)]] | wt | 18.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -9.3) |
| [[A498 (line)]] | wt | 98.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -16.2) |
| [[AsPC-1 (line)]] | alt | 49.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 78.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -11.2) |
| [[A-427 (line)]] | wt | 6.76 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.20 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.10 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 54.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.27 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.72 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 356), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAM2]] | +0.62 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[PORCN]] | +0.62 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[NUMBL]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[GYS1]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[GNAI2]] | +0.56 | +0.64 / +0.36 | both halves | 9e-05 |  |
| [[TANC2]] | +0.55 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[RRAS]] | +0.55 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[TNNT1]] | +0.55 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[CA12]] | +0.54 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[WDR54]] | +0.53 | +0.59 / +0.37 | both halves | 9e-05 |  |
| [[SFXN3]] | +0.53 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[ITGA5]] | +0.53 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF4G]] | -0.54 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[MCM9]] | -0.53 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[DPY19L1P1]] | -0.52 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[SYK]] | -0.50 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[RNASEH2B]] | -0.49 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[MACROH2A2]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[VSIG10]] | -0.49 | -0.50 / -0.32 | both halves | 1e-04 |  |
| [[NAF1]] | -0.48 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[ECHDC1]] | -0.47 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[DENND11]] | -0.47 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[PAXBP1]] | -0.47 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[EPM2A]] | -0.46 | -0.48 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LOX]] | B | LOX activity raises EHD2's level | lines that do not express LOX (31) vs lines expressing it (19) | 3.84× lower at baseline in the lines without LOX | 0.022 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[CA12]] | B | CA12 activity raises EHD2's level | lines that do not express CA12 (29) vs lines expressing it (21) | 2.54× lower at baseline in the lines without CA12 | 0.040 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |
| [[TOP2A]] | B | TOP2A activity raises EHD2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LOXL2]] | B | LOXL2 activity raises EHD2's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 3.65× lower at baseline in the lines without LOXL2 | 0.081 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1 |
| [[CLDN14-AS1]] | C | CLDN14-AS1 activity raises EHD2's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 4.29× lower at baseline in the lines without CLDN14-AS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDRG1]] | B | EHD2 activity raises NDRG1's level | lines that do not express EHD2 (14) vs lines expressing it (36) | 2.86× lower at baseline in the lines without EHD2 | 0.008 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479 |
| [[RNASEH2B]] | B | EHD2 activity lowers RNASEH2B's level | lines that do not express EHD2 (14) vs lines expressing it (36) | 1.69× higher at baseline in the lines without EHD2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479 |
| [[PFKP]] | B | EHD2 activity raises PFKP's level | lines that do not express EHD2 (14) vs lines expressing it (36) | 2.12× lower at baseline in the lines without EHD2 | 0.038 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479 |
| [[ATP2B4]] | B | EHD2 activity raises ATP2B4's level | lines that do not express EHD2 (14) vs lines expressing it (36) | 3.28× lower at baseline in the lines without EHD2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479 |
| [[MCM9]] | B | EHD2 activity lowers MCM9's level | lines that do not express EHD2 (14) vs lines expressing it (36) | 1.52× higher at baseline in the lines without EHD2 | 0.069 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479 |
| [[JMJD6]] | B | EHD2 activity raises JMJD6's level | lines that do not express EHD2 (14) vs lines expressing it (36) | 1.42× lower at baseline in the lines without EHD2 | 0.079 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479 |
| [[RRAS]] | B | EHD2 activity strengthens RRAS's drug response | lines that do not express EHD2 (13) vs lines expressing it (33) | the lines without EHD2 respond 0.56× as strongly (z diff +1.31); strongest at Harringtonine 0.5 µM: 0.77x vs 0.49x (z diff +1.9) | 0.093 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479; target measured in part of the lines; artifact flags |
| [[HSPG2]] | B | EHD2 activity raises HSPG2's level | lines that do not express EHD2 (14) vs lines expressing it (36) | 1.90× lower at baseline in the lines without EHD2 | 0.098 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479 |
| [[LOX]] | B | EHD2 activity raises LOX's level | lines that do not express EHD2 (14) vs lines expressing it (36) | 4.03× lower at baseline in the lines without EHD2 | 0.0996 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479 |
| [[CLDN14-AS1]] | C | EHD2 activity raises CLDN14-AS1's level | lines that do not express EHD2 (14) vs lines expressing it (36) | 3.52× lower at baseline in the lines without EHD2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479; co-absent with the target |

## Where it sits

- **Module**: [[Module 218]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.0, -1.4); signed map (-22.9, 25.0). **Vector** length 101, 30.4% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.5 | -13.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.7 | -14.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.2 | -12.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -1.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.4 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +3.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.5 | -11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -30.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -14.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.1 | -10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | -2.8 | -7.4 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -2.3 | -4.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.2 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -1.8 | -1.7 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | EH domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:47,713,422-47,743,134 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PAST2 |
| Gene groups (HGNC) | EF-hand domain containing |
| Reactome | 2 pathways, smallest: Factors involved in megakaryocyte development and platelet production; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZN4](https://www.uniprot.org/uniprotkb/Q9NZN4) (EH domain-containing protein 2):

> ATP- and membrane-binding protein that controls membrane reorganization/tubulation upon ATP hydrolysis (By similarity). Plays a role in membrane trafficking between the plasma membrane and endosomes. Important for the internalization of GLUT4. Required for fusion of myoblasts to skeletal muscle myotubes. Required for normal translocation of FER1L5 to the plasma membrane (By similarity). Regulates the equilibrium between cell surface-associated and cell surface-dissociated caveolae by …

**Summary**, from NCBI Gene [30846](https://www.ncbi.nlm.nih.gov/gene/30846):

> This gene encodes a member of the EH domain-containing protein family. These proteins are characterized by a C-terminal EF-hand domain, a nucleotide-binding consensus site at the N terminus and a bipartite nuclear localization signal. The encoded protein interacts with the actin cytoskeleton through an N-terminal domain and also binds to an EH domain-binding protein through the C-terminal EH domain. This interaction appears to connect clathrin-dependent endocytosis to actin, suggesting that …

**Accessions** — [HGNC:3243](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3243) · Entrez [30846](https://www.ncbi.nlm.nih.gov/gene/30846) · UniProt [Q9NZN4](https://www.uniprot.org/uniprotkb/Q9NZN4) · Ensembl [ENSG00000024422](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000024422)

## Data

Gene col 356: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 356); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 356, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 356]; `tensor/DDL_lfc|DDL_z.npy` [356]; `embed/gene_vectors.npy` [356]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 356 or target_col == 356). Every well: [[EHD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EHD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
