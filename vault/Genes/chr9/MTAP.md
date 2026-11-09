---
symbol: "MTAP"
type: "gene"
col: 1814
ensembl_id: "ENSG00000099810"
name: "methylthioadenosine phosphorylase"
location: "9p21.3"
module: 4
arm: "+"
pooled_cpm: 129.88
n_lines_expressing: 44
n_dd_up: 0
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MTAP

*methylthioadenosine phosphorylase* — 9p21.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Belinostat (drug)]] 5 µM in 2 lines (HOP62 3.13×, HS-578T 3.43×; ⚠ cell-cycle shift, explains ~40% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (HOP62 2.87×, HS-578T 3.22×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 2.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.413× (z -13.5, q 9e-39, down in 39 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA5]] (+0.69, fdr 7e-06), [[POLR1A]] (+0.67, fdr 7e-06), [[CCT2]] (+0.66, fdr 7e-06); moves opposite to [[KLC4]] (-0.61, fdr 1e-05), [[YY1AP1]] (-0.61, fdr 2e-05), [[LINC02256]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1814.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Belinostat (drug)]] 5 µM in 2 lines (HOP62 3.13×, HS-578T 3.43×; ⚠ cell-cycle shift, explains ~40% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (HOP62 2.87×, HS-578T 3.22×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 2.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.26× | +3.5 | 0.19 | 18/42 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.25× | +3.4 | 0.19 | 19/42 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.23× | +3.2 | 0.21 | 19/42 (HEC-1-A, LS 180, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.21 | 16/42 (HS-578T, NCI-H1573, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.22× | +3.1 | 0.21 | 17/42 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.23× | +3.1 | 0.21 | 21/42 (NCI-H2347, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1814.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.413×** | -13.5 | 9e-39 | 39/42 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.538×** | -13.3 | 4e-38 | 33/42 (A-427, SK-MEL-2, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.507×** | -10.3 | 9e-23 | 37/42 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.632×** | -9.9 | 8e-21 | 34/43 (RKO, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.648×** | -6.4 | 2e-08 | 28/42 (A-427, NCI-H23, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.461×** | -6.2 | 6e-08 | 35/43 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.661×** | -6.1 | 1e-07 | 25/42 (SHP-77, C-33 A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.691×** | -5.6 | 1e-06 | 25/42 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.721×** | -5.0 | 4e-05 | 24/42 (RKO, SNU-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.722×** | -5.0 | 4e-05 | 26/42 (A-427, RKO, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM |  | **0.804×** | -4.7 | 1e-04 | 25/42 (RKO, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.752×** | -4.3 | 7e-04 | 25/42 (A-427, LoVo, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **0.807×** | -3.3 | 0.048 | 18/42 (SNU-1, KATO III, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.784×** | -3.2 | 0.048 | 21/42 (NCI-H2030, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1814. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 492 | 0 | 17 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -36.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.342× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 239 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -17.0) |
| [[RKO (line)]] | wt | 358 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -21.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -18.4) |
| [[SW480 (line)]] | alt | 200 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -18.1) |
| [[NCI-H460 (line)]] | wt | 158 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -21.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -13.2) |
| [[LoVo (line)]] | wt | 231 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -16.0) |
| [[C-33 A (line)]] | alt | 182 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.276× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.343× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 185 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -18.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -11.2) |
| [[KATO III (line)]] | alt | 177 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -15.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.419× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 162 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -27.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -17.8) |
| [[SNU-1 (line)]] | wt | 137 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -14.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -12.5) |
| [[SW48 (line)]] | wt | 387 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 96.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.212× (z -11.2) |
| [[HS-578T (line)]] | alt | 46.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[J82 (line)]] | alt | 178 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.340× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 77.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.91× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -13.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H23 (line)]] | alt | 92.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -17.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.406× (z -8.5) |
| [[SHP-77 (line)]] | alt | 139 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.324× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.326× (z -12.2) |
| [[SW1417 (line)]] | alt | 110 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -14.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -13.2) |
| [[A498 (line)]] | wt | 198 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -13.5) |
| [[AsPC-1 (line)]] | alt | 82.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.305× (z -9.7) |
| [[CHP-212 (line)]] | wt | 146 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[COLO 205 (line)]] | alt | 142 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.280× (z -12.9) |
| [[HOP62 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.13× (z +10.4) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[LS 180 (line)]] | wt | 163 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.379× (z -10.2) |
| [[A549 (line)]] | wt | 40.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -9.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HCT15 (line)]] | alt | 126 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -8.5) |
| [[Hs 766T (line)]] | wt | 213 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -13.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2030 (line)]] | alt | 87.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -13.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H661 (line)]] | alt | 53.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0644× (z -9.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 123 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 125 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.78 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1814), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA5]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[CCT2]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[WDR4]] | +0.65 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[EIPR1]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[DDX10]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[SNRPD1]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.63 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[CTPS1]] | +0.63 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[AATF]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[CCT5]] | +0.62 | +0.65 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLC4]] | -0.61 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[YY1AP1]] | -0.61 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[LINC02256]] | -0.61 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[THAP8]] | -0.60 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[DNAJC27]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[VPS37D]] | -0.58 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[ZNF654]] | -0.58 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[ANG]] | -0.58 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.58 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[SAP30-DT]] | -0.57 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[GOLGA8N]] | -0.57 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[PHPT1]] | -0.57 | -0.53 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.719). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-12.9, -35.1); signed map (-5.0, -47.6). **Vector** length 124, 39.0% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.56 to 4); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.52 to 5); *Cooperation of Prefoldin and TriC/CCT  in actin and tubulin folding* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.6 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.5 | +3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.8 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.8 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.6 | +2.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.8 | +3.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.7 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -9.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.4 | -0.3 |
|  | [[Artesunate (drug)]] 5 µM |  | -4.2 | -4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.0 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.8 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | methylthioadenosine phosphorylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.3 — chr9:21,802,636-21,937,651 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MSAP, c86fus |
| Reactome | 8 pathways, smallest: Methionine salvage pathway; Sulfur amino acid metabolism; Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13126](https://www.uniprot.org/uniprotkb/Q13126) (S-methyl-5'-thioadenosine phosphorylase):

> Catalyzes the phosphorolytic cleavage of S-methyl-5'-thioadenosine (MTA) to adenine and 5-methylthioribose1-phosphate. Involved in the breakdown of MTA, a major by-product of polyamine biosynthesis. Responsible for the first step in the methionine salvage pathway after MTA has been generated from S-adenosylmethionine. Has broad substrate specificity with 6-aminopurine nucleosides as preferred substrates.

**Summary**, from NCBI Gene [4507](https://www.ncbi.nlm.nih.gov/gene/4507):

> This gene encodes an enzyme that plays a major role in polyamine metabolism and is important for the salvage pathway of both adenine and methionine. The encoded enzyme is deficient in many cancers. Multiple alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Sep 2021]

**Accessions** — [HGNC:7413](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7413) · Entrez [4507](https://www.ncbi.nlm.nih.gov/gene/4507) · UniProt [Q13126](https://www.uniprot.org/uniprotkb/Q13126) · Ensembl [ENSG00000099810](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099810)

## Data

Gene col 1814: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1814); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1814, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1814]; `tensor/DDL_lfc|DDL_z.npy` [1814]; `embed/gene_vectors.npy` [1814]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1814 or target_col == 1814). Every well: [[MTAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
