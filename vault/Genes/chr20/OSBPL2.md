---
symbol: "OSBPL2"
type: "gene"
col: 5100
ensembl_id: "ENSG00000130703"
name: "oxysterol binding protein like 2"
location: "20q13.33"
module: 41
arm: "+"
pooled_cpm: 94.07
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# OSBPL2

*oxysterol binding protein like 2* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.31× (z +5.2, q 1e-04, up in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 2.10×, NCI-H23 1.90×; ⚠ cell-cycle shift, explains ~30% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 2.33×, HOP62 2.23×).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.579× (z -9.8, q 8e-20, down in 37 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.631× (z -8.6, q 2e-15, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA2]] (+0.73, fdr 7e-06), [[WIPI1]] (+0.71, fdr 7e-06), [[OSBP]] (+0.70, fdr 7e-06); moves opposite to [[DHX9]] (-0.58, fdr 1e-05), [[UTP20]] (-0.57, fdr 1e-05), [[VMA21]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5100.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 2.10×, NCI-H23 1.90×; ⚠ cell-cycle shift, explains ~30% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 2.33×, HOP62 2.23×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +5.2 | 1e-04 | 27/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.23×** | +3.8 | 0.044 | 23/48 (PANC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.39× | +3.3 | 0.13 | 22/48 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 1.38× | +3.3 | 0.13 | 20/49 (COLO 205, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 1.36× | +3.1 | 0.18 | 18/48 (CFPAC-1, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.18 | 20/48 (HepG2/C3A, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5100.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.579×** | -9.8 | 8e-20 | 37/45 (KATO III, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.632×** | -8.9 | 2e-16 | 34/49 (SNU-1, NCI-H1573, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.631×** | -8.6 | 2e-15 | 34/48 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.734×** | -8.4 | 5e-15 | 30/48 (HS-578T, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.642×** | -8.3 | 2e-14 | 26/44 (SW 900, A549, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.668×** | -7.8 | 6e-13 | 41/48 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.784×** | -6.6 | 3e-09 | 31/48 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.723×** | -6.0 | 1e-07 | 31/47 (RKO, CHP-212, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.552×** | -6.0 | 1e-07 | 36/48 (AsPC-1, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.727×** | -5.9 | 2e-07 | 33/48 (LS 180, NCI-H1573, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.604×** | -5.1 | 2e-05 | 37/48 (AsPC-1, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.614×** | -4.9 | 4e-05 | 31/48 (AsPC-1, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.617×** | -4.9 | 5e-05 | 31/48 (AsPC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.781×** | -4.8 | 8e-05 | 27/48 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.787×** | -4.6 | 1e-04 | 30/48 (NCI-H1573, Panc 03.27, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.646×** | -4.4 | 3e-04 | 25/48 (AsPC-1, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.853× | -4.3 | 5e-04 | 19/48 (A498, Hs 766T, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.854× | -3.0 | 0.055 | 13/48 (KATO III, LoVo, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.856× | -3.0 | 0.060 | 21/48 (Hs 766T, A549, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.857× | -3.0 | 0.063 | 18/49 (MIA PaCa-2, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5100. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 174 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -16.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-733 (drug)]] 5 µM 0.194× (z -10.8) |
| [[A498 (line)]] | wt | 116 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.439× (z -10.8) |
| [[HS-578T (line)]] | alt | 98.5 | 0 | 6 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.456× (z -13.3) |
| [[HT-29 (line)]] | alt | 154 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.514× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 90.1 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -14.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A549 (line)]] | wt | 64.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 119 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW 900 (line)]] | alt | 100 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW1417 (line)]] | alt | 203 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.475× (z -11.7) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.352× (z -8.5) |
| [[HOP62 (line)]] | alt | 74.6 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.422× (z -8.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 186 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -14.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 100 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.420× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.604× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 106 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.572× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 106 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.1) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H2347 (line)]] | alt | 88.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -10.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 68.7 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.454× (z -9.1) |
| [[A-427 (line)]] | wt | 58.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[CHP-212 (line)]] | wt | 48.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0956× (z -9.9) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 160 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -10.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.400× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H460 (line)]] | wt | 46.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -12.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 93.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.283× (z -13.2) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 89.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -10.5) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SNU-1 (line)]] | wt | 75.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 91.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +10.3) | — |
| [[AN3 CA (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 76.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 97.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 73.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5100), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA2]] | +0.73 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[WIPI1]] | +0.71 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[OSBP]] | +0.70 | +0.73 / +0.66 | both halves | 7e-06 | same gene group; pathway: Bile acid and bile salt metabolism |
| [[YIPF2]] | +0.70 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[IFT20]] | +0.68 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[ERLEC1]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[SYVN1]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[BET1L]] | +0.66 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[RAB5A]] | +0.66 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[SPSB3]] | +0.66 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[ZCCHC17]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[LINC01881]] | +0.65 | +0.54 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX9]] | -0.58 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[UTP20]] | -0.57 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[VMA21]] | -0.56 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[SMG7]] | -0.56 | -0.38 / -0.55 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.697). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (9.4, -35.5); signed map (-47.4, 12.9). **Vector** length 118, 35.8% of its response variance represented; |z| ≥ 3 in 1,118 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ER to Golgi Anterograde Transport* (reactome, mean cos +0.51 to 8); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +6.1 | -3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.4 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +1.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | -1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +3.7 | -8.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +0.6 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.8 | +0.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.4 | +0.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.3 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.4 | -7.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.7 | -8.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.3 | -8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.5 | -5.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.1 | -4.9 |
|  | [[EX229 (drug)]] 5 µM |  | -5.1 | -4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.7 | -4.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.5 | -6.0 |

## What is on record

|  |  |
|---|---|
| Name | oxysterol binding protein like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:62,231,922-62,296,213 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0772, ORP-2, DFNA67 |
| Gene groups (HGNC) | Oxysterol binding proteins |
| Reactome | 4 pathways, smallest: Synthesis of bile acids and bile salts; Bile acid and bile salt metabolism; Metabolism of steroids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1P3](https://www.uniprot.org/uniprotkb/Q9H1P3) (Oxysterol-binding protein-related protein 2):

> Intracellular transport protein that binds sterols and phospholipids and mediates lipid transport between intracellular compartments. Increases plasma membrane cholesterol levels and decreases phosphatidylinositol-4,5-bisphosphate levels in the cell membrane. Exhibits strong binding to phosphatidic acid and weak binding to phosphatidylinositol 3-phosphate. Binds cholesterol, dehydroergosterol, 22(R)-hydroxycholesterol and 25-hydroxycholesterol (in vitro). In conjunction with PLCB3, it may …

**Summary**, from NCBI Gene [9885](https://www.ncbi.nlm.nih.gov/gene/9885):

> This gene encodes a member of the oxysterol-binding protein (OSBP) family, a group of intracellular lipid receptors. Most members contain an N-terminal pleckstrin homology domain and a highly conserved C-terminal OSBP-like sterol-binding domain, although the encoded protein contains only the sterol-binding domain. In vitro studies have shown that the encoded protein can bind strongly to phosphatic acid and weakly to phosphatidylinositol 3-phosphate, but cannot bind to 25-hydroxycholesterol. The …

**Accessions** — [HGNC:15761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15761) · Entrez [9885](https://www.ncbi.nlm.nih.gov/gene/9885) · UniProt [Q9H1P3](https://www.uniprot.org/uniprotkb/Q9H1P3) · Ensembl [ENSG00000130703](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130703)

## Data

Gene col 5100: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5100); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5100, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5100]; `tensor/DDL_lfc|DDL_z.npy` [5100]; `embed/gene_vectors.npy` [5100]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5100 or target_col == 5100). Every well: [[OSBPL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSBPL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
