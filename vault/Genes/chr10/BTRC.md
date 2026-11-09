---
symbol: "BTRC"
type: "gene"
col: 9251
ensembl_id: "ENSG00000166167"
name: "beta-transducin repeat containing E3 ubiquitin protein ligase"
location: "10q24.32"
module: 40
arm: "+"
pooled_cpm: 136.03
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# BTRC

*beta-transducin repeat containing E3 ubiquitin protein ligase* — 10q24.32

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (SW480 1.76×, HEC-1-A 1.87×, A549 1.91×, BT-474 1.95×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 1.77×, BT-474 2.09×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.16×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.337× (z -23.2, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.765× (z -5.7, q 9e-07, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (H4 0.0194×, NCI-H23 0.0934×, NCI-H460 0.193×, A549 0.132×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.208×, HCT15 0.136×, PANC-1 0.298×, NCI-H2030 0.179×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HOP62 0.185×, A-172 0.234×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (A-172 0.431×, MIA PaCa-2 0.527×); [[Rosiglitazone (drug)]] 0.05 µM in 1 line (SW 1088 0.118×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFT20]] (+0.68, fdr 7e-06), [[PMM1]] (+0.61, fdr 1e-05), [[ICAM3]] (+0.61, fdr 2e-05); moves opposite to [[NCR3LG1]] (-0.58, fdr 1e-05), [[RAB4A-AS1]] (-0.56, fdr 1e-05), [[ZNF121]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9251.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (SW480 1.76×, HEC-1-A 1.87×, A549 1.91×, BT-474 1.95×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 1.77×, BT-474 2.09×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.16×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.4 | 4e-05 | 22/48 (SW480, HEC-1-A, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.23× | +3.5 | 0.12 | 22/48 (SK-MEL-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.0 | 0.33 | 17/48 (A-427, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.0 | 0.33 | 20/48 (SW480, BT-474, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9251.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (H4 0.0194×, NCI-H23 0.0934×, NCI-H460 0.193×, A549 0.132×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.208×, HCT15 0.136×, PANC-1 0.298×, NCI-H2030 0.179×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HOP62 0.185×, A-172 0.234×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (A-172 0.431×, MIA PaCa-2 0.527×); [[Rosiglitazone (drug)]] 0.05 µM in 1 line (SW 1088 0.118×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.337×** | -23.2 | 0e+00 | 47/49 (NCI-H1573, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.356×** | -21.2 | 0e+00 | 41/44 (H4, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.378×** | -19.2 | 0e+00 | 43/45 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **0.702×** | -7.6 | 5e-12 | 41/48 (HOP62, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.750×** | -5.9 | 3e-07 | 35/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.765×** | -5.7 | 9e-07 | 29/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.801×** | -4.8 | 2e-04 | 28/48 (hTERT-HPNE, AsPC-1, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.895× | -3.4 | 0.054 | 2/48 (SK-MEL-2, RPMI-7951) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.845× | -3.3 | 0.055 | 18/47 (A-172, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.710×** | -3.2 | 0.063 | 16/48 (AsPC-1, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -3.2 | 0.063 | 13/49 (C32, LOX-IMVI, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.863× | -3.2 | 0.073 | 18/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9251. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 150 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.431× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 126 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -12.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 127 | 2 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.318× (z -16.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 146 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -17.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 185 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -19.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 158 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -11.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 227 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0194× (z -34.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 103 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.194× (z -21.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 223 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -20.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 157 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -17.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 135 | 1 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +14.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.527× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 124 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -18.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 97.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -14.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 145 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.132× (z -24.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 98.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -9.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 133 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -13.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 139 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -15.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 160 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -13.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 139 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 164 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -21.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 184 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -19.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 154 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -25.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 129 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -14.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 133 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -19.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 148 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -15.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 140 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -18.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -16.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0842× (z -15.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 169 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -21.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -17.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.405× (z -10.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.415× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 137 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0934× (z -29.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 140 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.427× (z -8.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 96.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -10.7) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 113 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -11.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 239 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -9.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -18.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -9.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 165 | 0 | 1 | — | [[Rosiglitazone (drug)]] 0.05 µM 0.118× (z -9.0) |
| [[SW 900 (line)]] | alt | 181 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.424× (z -9.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 165 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -9.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 105 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9251), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT20]] | +0.68 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[PMM1]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ICAM3]] | +0.61 | +0.48 / +0.55 | both halves | 2e-05 | pathway: C-type lectin receptors (CLRs) |
| [[MXD4]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[CDK7]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 | pathway: G2/M Transition |
| [[WDR83OS]] ⚠ | +0.60 | +0.57 / +0.50 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[OST4]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 | pathway: Co-inhibition by PD-1 |
| [[RABAC1]] | +0.60 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[TULP3]] | +0.59 | +0.58 / +0.57 | both halves | 9e-06 | pathway: Hedgehog 'off' state |
| [[PMS2P4-1]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ZNHIT1]] | +0.59 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[YIPF2]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[KLHDC10]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCR3LG1]] | -0.58 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[RAB4A-AS1]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[ZNF121]] | -0.52 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[TMEM185B]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ZNF300]] | -0.50 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[MAT2A]] | -0.50 | -0.36 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-3.2, -54.9); signed map (-44.8, 16.4). **Vector** length 87.6, 25.5% of its response variance represented; |z| ≥ 3 in 834 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.9 | +2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.7 | +3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | -0.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.4 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.3 | +1.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.3 | +0.3 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | +1.2 | +0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.4 | -19.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | beta-transducin repeat containing E3 ubiquitin protein ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:101,354,033-101,557,321 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bTrCP, betaTrCP, FBXW1A, Fwd1, beta-TrCP1, bTrCP1 |
| Gene groups (HGNC) | WD repeat domain containing; F-box and WD repeat domain containing |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 80 pathways, smallest: Prolactin receptor signaling; MAP3K8 (TPL2)-dependent MAPK1/3 activation; Vpu mediated degradation of CD4 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y297](https://www.uniprot.org/uniprotkb/Q9Y297) (F-box/WD repeat-containing protein 1A):

> Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Recognizes and binds to phosphorylated target proteins. SCF(BTRC) mediates the ubiquitination of CTNNB1 and participates in Wnt signaling. SCF(BTRC) mediates the ubiquitination of phosphorylated NFKB1, ATF4, CDC25A, DLG1, FBXO5, PER1, SMAD3, SMAD4, SNAI1 and probably NFKB2. SCF(BTRC) mediates the …

**Summary**, from NCBI Gene [8945](https://www.ncbi.nlm.nih.gov/gene/8945):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:1144](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1144) · Entrez [8945](https://www.ncbi.nlm.nih.gov/gene/8945) · UniProt [Q9Y297](https://www.uniprot.org/uniprotkb/Q9Y297) · Ensembl [ENSG00000166167](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166167)

## Data

Gene col 9251: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9251); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9251, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9251]; `tensor/DDL_lfc|DDL_z.npy` [9251]; `embed/gene_vectors.npy` [9251]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9251 or target_col == 9251). Every well: [[BTRC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTRC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
