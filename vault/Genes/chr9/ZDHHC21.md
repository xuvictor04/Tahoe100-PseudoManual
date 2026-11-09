---
symbol: "ZDHHC21"
type: "gene"
col: 10660
ensembl_id: "ENSG00000175893"
name: "zDHHC palmitoyltransferase 21"
location: "9p22.3"
module: 25
arm: "+"
pooled_cpm: 44.14
n_lines_expressing: 48
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# ZDHHC21

*zDHHC palmitoyltransferase 21* — 9p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.41× (z +5.5, q 2e-05, up in 24 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.23× (z +4.6, q 0.001, up in 24 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 3.13×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.408× (z -20.0, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGPS]] (+0.76, fdr 7e-06), [[IPO8]] (+0.71, fdr 7e-06), [[SSX2IP]] (+0.70, fdr 7e-06); moves opposite to [[STX5]] (-0.67, fdr 7e-06), [[INAFM1]] (-0.63, fdr 7e-06), [[MIA]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10660.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 3.13×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +5.5 | 2e-05 | 24/44 (hTERT-HPNE, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.6 | 0.001 | 24/46 (A498, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.22×** | +4.4 | 0.002 | 24/46 (LS 180, HT-29, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.1 | 0.007 | 21/41 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.21× | +3.0 | 0.27 | 15/46 (SW48, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10660.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.408×** | -20.0 | 0e+00 | 45/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.444×** | -12.8 | 3e-35 | 40/44 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.455×** | -12.4 | 3e-33 | 43/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.664×** | -9.1 | 8e-18 | 35/46 (LoVo, HS-578T, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.567×** | -9.0 | 3e-17 | 36/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.572×** | -8.8 | 1e-16 | 37/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -4.8 | 1e-04 | 24/45 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.731×** | -4.8 | 1e-04 | 28/44 (J82, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **0.743×** | -4.7 | 2e-04 | 22/44 (LS 180, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.765×** | -4.2 | 0.001 | 22/46 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.769×** | -4.0 | 0.003 | 24/47 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.709×** | -3.9 | 0.005 | 26/44 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.778×** | -3.8 | 0.006 | 23/45 (RPMI-7951, SHP-77, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.789×** | -3.7 | 0.007 | 21/45 (HepG2/C3A, NCI-H661, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.861× | -3.3 | 0.032 | 13/46 (SW 1271, LS 180, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.828×** | -3.0 | 0.099 | 15/46 (RKO, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10660. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 45.8 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -15.6) |
| [[PANC-1 (line)]] | alt | 28.4 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -17.3) |
| [[J82 (line)]] | alt | 73.5 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -16.3) |
| [[LoVo (line)]] | wt | 32.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -18.2) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -14.9) |
| [[LS 180 (line)]] | wt | 78.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -8.8) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 34.0 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -17.7) |
| [[HS-578T (line)]] | alt | 53.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -17.2) |
| [[LOX-IMVI (line)]] | wt | 61.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 44.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 37.8 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -13.3) |
| [[A549 (line)]] | wt | 51.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -14.7) |
| [[hTERT-HPNE (line)]] | wt | 38.2 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.179× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 47.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -17.3) |
| [[NCI-H1573 (line)]] | alt | 36.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.13× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -12.2) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H2030 (line)]] | alt | 31.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -10.5) |
| [[RKO (line)]] | wt | 76.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 55.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -13.8) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 62.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -12.9) |
| [[SNU-1 (line)]] | wt | 118 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -15.4) |
| [[SW1417 (line)]] | alt | 50.2 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.336× (z -10.8) |
| [[SW48 (line)]] | wt | 101 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -13.9) |
| [[C32 (line)]] | wt | 20.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -10.1) |
| [[COLO 205 (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -9.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 32.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -15.4) |
| [[HCT15 (line)]] | alt | 99.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 92.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.179× (z -9.2) ⚠ cell-cycle shift, explains ~16% of this change |
| [[HOP62 (line)]] | alt | 18.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -8.8) |
| [[Hs 766T (line)]] | wt | 24.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -10.2) |
| [[HT-29 (line)]] | alt | 42.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 33.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -8.7) |
| [[NCI-H661 (line)]] | alt | 47.5 | 0 | 1 | — | [[Budesonide (drug)]] 0.5 µM 0.0793× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 56.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -11.4) |
| [[SHP-77 (line)]] | alt | 73.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -9.6) |
| [[SW 900 (line)]] | alt | 49.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -9.2) |
| [[A-172 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10660), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGPS]] | +0.76 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[IPO8]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[SSX2IP]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[GMFB]] | +0.69 | +0.48 / +0.79 | both halves | 2e-05 |  |
| [[FAM98B]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[OCRL]] | +0.68 | +0.43 / +0.73 | both halves | 3e-05 |  |
| [[DHX9]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[DLD]] | +0.66 | +0.55 / +0.68 | both halves | 1e-05 | pathway: Signaling by Nuclear Receptors |
| [[MOCS2]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[COMMD8]] | +0.64 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ALKBH8]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[IMPACT]] | +0.63 | +0.48 / +0.66 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX5]] | -0.67 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.63 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[MIA]] | -0.62 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[TMEM258]] | -0.60 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[FBXL12]] | -0.60 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[GUCA1B]] | -0.60 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.59 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[TESK2]] | -0.59 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[ZNF324]] | -0.58 | -0.36 / -0.69 | both halves | 1e-04 |  |
| [[ZBTB7A]] | -0.58 | -0.41 / -0.65 | both halves | 4e-05 |  |
| [[MTRFR]] | -0.58 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[NARF]] | -0.57 | -0.41 / -0.63 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ZDHHC21's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-25.8, -35.2); signed map (-16.8, -43.6). **Vector** length 102, 26.2% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +5.9 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.9 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +0.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.1 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.7 | -20.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.3 | -8.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -12.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | -12.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -3.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.7 | -2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.3 | -2.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.2 | -1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p22.3 — chr9:14,611,071-14,693,432 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC097, DNZ1, DHHC21 |
| Gene groups (HGNC) | Zinc fingers DHHC-type |
| Reactome | 5 pathways, smallest: eNOS activation; Metabolism of nitric oxide: NOS3 activation and regulation; Extra-nuclear estrogen signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVQ6](https://www.uniprot.org/uniprotkb/Q8IVQ6) (Palmitoyltransferase ZDHHC21):

> Palmitoyltransferase that catalyzes the addition of palmitate onto various protein substrates. Palmitoylates sex steroid hormone receptors, including ESR1, PGR and AR, thereby regulating their targeting to the plasma membrane. This affects rapid intracellular signaling by sex hormones via ERK and AKT kinases and the generation of cAMP, but does not affect that mediated by their nuclear receptor. Palmitoylates FYN, regulates its localization in hair follicles and plays a key role in epidermal …

**Summary**, from NCBI Gene [340481](https://www.ncbi.nlm.nih.gov/gene/340481):

> Enables protein-cysteine S-palmitoyltransferase activity. Involved in peptidyl-L-cysteine S-palmitoylation. Located in Golgi apparatus and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20750](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20750) · Entrez [340481](https://www.ncbi.nlm.nih.gov/gene/340481) · UniProt [Q8IVQ6](https://www.uniprot.org/uniprotkb/Q8IVQ6) · Ensembl [ENSG00000175893](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175893)

## Data

Gene col 10660: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10660); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10660, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10660]; `tensor/DDL_lfc|DDL_z.npy` [10660]; `embed/gene_vectors.npy` [10660]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10660 or target_col == 10660). Every well: [[ZDHHC21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
