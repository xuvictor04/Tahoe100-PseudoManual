---
symbol: "IQCJ-SCHIP1"
type: "gene"
col: 16010
ensembl_id: "ENSG00000283154"
name: "IQCJ-SCHIP1 readthrough"
location: "3q25.32-q25.33"
module: 151
arm: "+"
pooled_cpm: 120.36
n_lines_expressing: 43
n_dd_up: 1
n_dd_down: 27
n_dd_up_clean: 1
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 22
direction_downstream: 2
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# IQCJ-SCHIP1

*IQCJ-SCHIP1 readthrough* — 3q25.32-q25.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +6.1, q 6e-07, up in 23 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H460 3.16×, J82 4.02×, HCT15 3.39×, LoVo 2.63×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW480 2.13×, NCI-H460 2.12×, COLO 205 3.72×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 2.56×; ⚠ cell-cycle shift, explains ~30% of this change).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.446× (z -9.0, q 1e-16, down in 29 of 40 measured lines) ⚠ toxic. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.658× (z -6.9, q 1e-09, down in 30 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCHIP1]] (+0.88, fdr 7e-06, ⚠ same locus), [[MIR100HG]] (+0.65, fdr 7e-06), [[CSMD2]] (+0.65, fdr 1e-05), [[SYNJ2]] (+0.64, fdr 7e-06); moves opposite to [[DYNC2LI1]] (-0.53, fdr 4e-05), [[TRAPPC11]] (-0.53, fdr 5e-05), [[FPGT]] (-0.52, fdr 2e-05).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[ADAMTS6]] → it (grade B ⚠); 2 go from it, the strongest it → [[C2orf92]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16010.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H460 3.16×, J82 4.02×, HCT15 3.39×, LoVo 2.63×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW480 2.13×, NCI-H460 2.12×, COLO 205 3.72×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 2.56×; ⚠ cell-cycle shift, explains ~30% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.1 | 6e-07 | 23/42 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.23× | +3.3 | 0.25 | 22/41 (NCI-H2347, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16010.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.446×** | -9.0 | 1e-16 | 29/40 (RKO, SW 1271, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.508×** | -7.5 | 2e-11 | 34/42 (HOP62, H4, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.658×** | -6.9 | 1e-09 | 30/41 (RKO, SW48, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.575×** | -6.2 | 9e-08 | 26/37 (H4, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.609×** | -5.8 | 9e-07 | 30/41 (SW480, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.617×** | -5.2 | 2e-05 | 30/38 (HEC-1-A, RKO, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.643×** | -4.9 | 7e-05 | 24/41 (RKO, SNU-423, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.675×** | -4.6 | 4e-04 | 28/41 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.682×** | -4.4 | 5e-04 | 27/41 (RKO, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.695×** | -4.2 | 0.001 | 23/41 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.704×** | -4.1 | 0.002 | 22/41 (NCI-H1792, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.704×** | -3.9 | 0.004 | 23/41 (NCI-H1792, COLO 205, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.524×** | -3.9 | 0.004 | 23/40 (RKO, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.717×** | -3.7 | 0.008 | 22/40 (RKO, SNU-423, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.733×** | -3.5 | 0.019 | 21/42 (SNU-423, H4, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.746×** | -3.4 | 0.023 | 24/41 (SNU-423, H4, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.736×** | -3.4 | 0.023 | 20/41 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.737×** | -3.4 | 0.023 | 24/42 (SK-MEL-2, RKO, …) | two highest doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.743×** | -3.3 | 0.027 | 21/42 (H4, HS-578T, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.757×** | -3.2 | 0.035 | 22/42 (HOP62, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.758×** | -3.2 | 0.035 | 22/41 (RKO, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.747×** | -3.2 | 0.035 | 21/41 (SNU-423, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16010. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 403 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -17.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.151× (z -14.4) |
| [[SNU-423 (line)]] | alt | 775 | 0 | 12 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 135 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.306× (z -10.1) |
| [[H4 (line)]] | wt | 251 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0231× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 0.215× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 145 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.280× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.286× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 200 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.219× (z -13.5) |
| [[A-172 (line)]] | wt | 133 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.450× (z -8.5) |
| [[HOP62 (line)]] | alt | 223 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.308× (z -8.8) |
| [[J82 (line)]] | alt | 250 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +14.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.242× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 107 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.298× (z -10.2) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 73.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.2) | — |
| [[A498 (line)]] | wt | 162 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -9.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 175 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -10.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 126 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.385× (z -8.6) |
| [[PANC-1 (line)]] | alt | 50.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.319× (z -9.6) |
| [[SW480 (line)]] | alt | 74.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +10.4) | [[Docetaxel (drug)]] 0.05 µM 0.402× (z -8.9) ⚠ transcription drop |
| [[A-427 (line)]] | wt | 97.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -9.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 68.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.212× (z -9.9) |
| [[C-33 A (line)]] | alt | 77.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -12.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 44.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.396× (z -8.8) |
| [[COLO 205 (line)]] | alt | 37.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 35.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -18.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 152 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -8.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 70.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 142 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 346 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.156× (z -10.1) |
| [[SW 1271 (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0724× (z -11.5) ⚠ toxic |
| [[SW48 (line)]] | wt | 122 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.270× (z -9.2) |
| [[A549 (line)]] | wt | 95.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.9 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 27.7 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 82.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 152 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 94.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 85.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16010), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCHIP1]] | +0.88 | +0.86 / +0.89 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[MIR100HG]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[CSMD2]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[SYNJ2]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[CD44]] | +0.64 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[SAMD3]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SLC4A7]] | +0.63 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[RPSAP52]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[CYTOR]] | +0.62 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[BACH1]] | +0.62 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[LRRC8C]] | +0.61 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[SIGLEC15]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[KPNA4]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC2LI1]] | -0.53 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[TRAPPC11]] | -0.53 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[FPGT]] | -0.52 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[EDN2]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[NTPCR]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[EXD2]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[FLVCR2]] | -0.50 | -0.43 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 20, C 2. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTS6]] | B | ADAMTS6 activity strengthens IQCJ-SCHIP1's drug response | lines that do not express ADAMTS6 (20) vs lines expressing it (22) | the lines without ADAMTS6 respond 0.70× as strongly (z diff +1.77); strongest at Dinaciclib 5 µM: 0.71x vs 0.30x (z diff +4.9) | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; target measured in part of the lines; artifact flags |
| [[HHIP]] | B | HHIP activity strengthens IQCJ-SCHIP1's drug response | lines that do not express HHIP (27) vs lines expressing it (15) | the lines without HHIP respond 0.80× as strongly (z diff +1.40); strongest at Dinaciclib 5 µM: 0.61x vs 0.27x (z diff +3.5) | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LINC01204]] | B | LINC01204 activity raises IQCJ-SCHIP1's level | lines that do not express LINC01204 (22) vs lines expressing it (28) | 2.37× lower at baseline in the lines without LINC01204 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC00460, WNT5A, LNCOG; maybe low, not absent |
| [[ROBO4]] | B | ROBO4 activity raises IQCJ-SCHIP1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.63× lower at baseline in the lines without ROBO4 | 0.013 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[VEPH1]] | B | VEPH1 activity raises IQCJ-SCHIP1's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 2.88× lower at baseline in the lines without VEPH1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC |
| [[LINC03041]] | B | LINC03041 activity raises IQCJ-SCHIP1's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 3.07× lower at baseline in the lines without LINC03041 | 0.017 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[FLI1]] | B | FLI1 activity raises IQCJ-SCHIP1's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 2.59× lower at baseline in the lines without FLI1 | 0.034 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615 |
| [[FRMD4A]] | B | FRMD4A activity raises IQCJ-SCHIP1's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.68× lower at baseline in the lines without FRMD4A | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[FLI1]] | B | FLI1 activity strengthens IQCJ-SCHIP1's drug response | lines that do not express FLI1 (24) vs lines expressing it (18) | the lines without FLI1 respond 0.66× as strongly (z diff +1.59); strongest at Dinaciclib 5 µM: 0.64x vs 0.29x (z diff +4.3) | 0.049 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615; target measured in part of the lines; artifact flags |
| [[LINC03041]] | B | LINC03041 activity strengthens IQCJ-SCHIP1's drug response | lines that do not express LINC03041 (11) vs lines expressing it (31) | the lines without LINC03041 respond 0.70× as strongly (z diff +1.49); strongest at Dinaciclib 5 µM: 0.81x vs 0.38x (z diff +4.6) | 0.063 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LINC00702]] | B | LINC00702 activity raises IQCJ-SCHIP1's level | lines that do not express LINC00702 (25) vs lines expressing it (25) | 2.51× lower at baseline in the lines without LINC00702 | 0.066 | ⚠ within organs, on part of the lines; also absent: FGF5, ENSG00000253553, LNCOG |
| [[HHIP]] | B | HHIP activity raises IQCJ-SCHIP1's level | lines that do not express HHIP (33) vs lines expressing it (17) | 1.89× lower at baseline in the lines without HHIP | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C2orf92]] | B | IQCJ-SCHIP1 activity raises C2orf92's level | lines that do not express IQCJ-SCHIP1 (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without IQCJ-SCHIP1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SCHIP1, ENSG00000281091, NPL; maybe low, not absent; its own permutation p |
| [[SCHIP1]] | C | IQCJ-SCHIP1 activity raises SCHIP1's level | lines that do not express IQCJ-SCHIP1 (7) vs lines expressing it (43) | 5.18× lower at baseline in the lines without IQCJ-SCHIP1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SCHIP1, ENSG00000281091, NPL; maybe low, not absent; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.749). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.4, 9.9); signed map (13.6, 47.4). **Vector** length 131, 42.8% of its response variance represented; |z| ≥ 3 in 1,294 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.7 | +2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.6 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.7 | -6.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.4 | -4.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -1.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.4 | -2.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -4.2 | -3.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.1 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.0 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | IQCJ-SCHIP1 readthrough |
| Locus type | readthrough (other) |
| Location | 3q25.32-q25.33 — chr3:158,962,235-159,897,358 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [B3KU38](https://www.uniprot.org/uniprotkb/B3KU38) (IQCJ-SCHIP1 readthrough transcript protein):

> May play a role in action potential conduction in myelinated cells through the organization of molecular complexes at nodes of Ranvier and axon initial segments. May also play a role in axon outgrowth and guidance (By similarity).

**Summary**, from NCBI Gene [100505385](https://www.ncbi.nlm.nih.gov/gene/100505385):

> This locus represents naturally occurring read-through transcription from the neighboring IQ motif containing J (IQCJ) and schwannomin interacting protein 1 (SCHIP1) genes. Alternative splicing results in multiple transcript variants that are composed of in-frame exons from each individual gene. The resulting fusion products are thought to be components of the multimolecular complexes of axon initial segments and nodes of Ranvier, and they may play a role in calcium-mediated responses. …

**Accessions** — [HGNC:38842](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:38842) · Entrez [100505385](https://www.ncbi.nlm.nih.gov/gene/100505385) · UniProt [B3KU38](https://www.uniprot.org/uniprotkb/B3KU38) · Ensembl [ENSG00000283154](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000283154)

## Data

Gene col 16010: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16010); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16010, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16010]; `tensor/DDL_lfc|DDL_z.npy` [16010]; `embed/gene_vectors.npy` [16010]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16010 or target_col == 16010). Every well: [[IQCJ-SCHIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQCJ-SCHIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
