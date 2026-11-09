---
symbol: "PABPC4"
type: "gene"
col: 1633
ensembl_id: "ENSG00000090621"
name: "poly(A) binding protein cytoplasmic 4"
location: "1p34.3"
module: 18
arm: "+"
pooled_cpm: 128.66
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PABPC4

*poly(A) binding protein cytoplasmic 4* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.38× (z +16.8, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.46× (z +6.0, q 2e-07, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.765× (z -4.1, q 0.024, down in 31 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.745×, NCI-H23 0.805×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.550×, CHP-212 0.358×; ⚠ cell-cycle shift, explains ~53% of this change); [[Monocrotaline (drug)]] 5 µM in 1 line (SW 1088 0.0865×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPM1]] (+0.56, fdr 1e-05), [[MTA1]] (+0.55, fdr 1e-05), [[PABPC1]] (+0.55, fdr 1e-05); moves opposite to [[MRPL13]] (-0.49, fdr 3e-05), [[UBA3]] (-0.48, fdr 4e-05), [[GPKOW]] (-0.48, fdr 3e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1633.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.38×** | +16.8 | 0e+00 | 48/49 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.00×** | +16.8 | 0e+00 | 44/44 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +12.6 | 2e-34 | 45/45 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +7.4 | 2e-11 | 41/47 (HepG2/C3A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.37×** | +7.1 | 2e-10 | 30/48 (AsPC-1, SK-MEL-2, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +6.0 | 2e-07 | 30/48 (AsPC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +5.6 | 2e-06 | 38/48 (AsPC-1, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.40×** | +5.3 | 7e-06 | 35/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.41×** | +5.2 | 1e-05 | 36/47 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +4.8 | 9e-05 | 30/48 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.35×** | +4.8 | 9e-05 | 35/48 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.22×** | +4.4 | 5e-04 | 23/49 (NCI-H2347, A549, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.31×** | +4.3 | 8e-04 | 27/48 (AsPC-1, NCI-H460, …) | rises with dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.61×** | +4.0 | 0.003 | 36/48 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.031 | 27/49 (Panc 03.27, A-172, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.037 | 27/48 (NCI-H1573, A498, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.038 | 25/48 (BT-474, NCI-H1573, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.038 | 28/48 (AsPC-1, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.049 | 26/48 (SW 900, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.079 | 22/48 (NCI-H23, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.083 | 22/49 (SW 900, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1633.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.745×, NCI-H23 0.805×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.550×, CHP-212 0.358×; ⚠ cell-cycle shift, explains ~53% of this change); [[Monocrotaline (drug)]] 5 µM in 1 line (SW 1088 0.0865×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.765×** | -4.1 | 0.024 | 31/47 (SK-MEL-2, HS-578T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.860× | -3.3 | 0.26 | 19/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.804× | -3.2 | 0.26 | 24/47 (LS 180, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -3.0 | 0.37 | 4/50 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1633. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 87.9 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +23.5) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.62× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 82.0 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +17.3) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H460 (line)]] | wt | 123 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +15.3) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 75.5 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +14.8) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +9.4) | — |
| [[C32 (line)]] | wt | 127 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +12.7) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 153 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.5) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[Hs 766T (line)]] | wt | 114 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.41× (z +13.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 124 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 133 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +11.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 82.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +13.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 118 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +12.9) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.5 µM 0.439× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 65.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +13.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 94.6 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +16.3) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H2030 (line)]] | alt | 131 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +11.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 143 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +13.4) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 119 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.58× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.34× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 117 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +17.5) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[A498 (line)]] | wt | 129 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +15.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 94.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +12.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 170 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 109 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +11.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 111 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +13.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 146 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +14.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 133 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +12.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 194 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +13.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 79.1 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +11.7) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[PANC-1 (line)]] | alt | 190 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +15.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 150 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +14.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 78.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 140 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +16.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 101 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.45× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -8.7) ⚠ cell-cycle shift, explains ~53% of this change |
| [[H4 (line)]] | wt | 131 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 170 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +11.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 150 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.4) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H23 (line)]] | alt | 182 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 90.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +12.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 142 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +12.2) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 175 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +9.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 56.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.7) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[RKO (line)]] | wt | 212 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -9.7) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SNU-1 (line)]] | wt | 150 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 1 | — | [[Monocrotaline (drug)]] 5 µM 0.0865× (z -9.2) |
| [[SW1417 (line)]] | alt | 128 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 184 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1633), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPM1]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[MTA1]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[PABPC1]] | +0.55 | +0.50 / +0.57 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 870 |
| [[TOP1MT]] | +0.54 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[PPIEL]] | +0.54 | +0.62 / +0.54 | both halves | 1e-05 | ⚠ **readthrough risk**: PPIEL lies 2.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[TXLNG]] | +0.53 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[RPS9]] | +0.52 | +0.37 / +0.57 | both halves | 9e-05 |  |
| [[CPNE7]] | +0.51 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[AHCY]] | +0.51 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[PCBP2]] | +0.49 | +0.42 / +0.47 | both halves | 4e-05 | STRING 406 |
| [[SNHG16]] | +0.49 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[DANCR]] | +0.49 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[NCL]] | +0.49 | +0.50 / +0.49 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*32 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL13]] | -0.49 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[UBA3]] | -0.48 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[GPKOW]] | -0.48 | -0.27 / -0.59 | both halves | 3e-04 |  |
| [[PDZD11]] | -0.47 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[TMEM179B]] | -0.47 | -0.25 / -0.44 | both halves | 4e-04 |  |
| [[MRPL28]] | -0.46 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[UQCR10]] ⚠ | -0.45 | -0.43 / -0.41 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5IF1]] | -0.45 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[RNF181]] | -0.45 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[PIN1]] | -0.45 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[CAVIN3]] | -0.45 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[ATG4A]] | -0.45 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[CCDC167]] | -0.45 | -0.44 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.374). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-25.5, -38.7); signed map (-1.0, -56.6). **Vector** length 90.0, 27.8% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +4.7 | +7.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.8 | +4.0 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.3 | +0.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.6 | -0.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.4 | -0.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.3 | +3.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.6 | -1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.5 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | poly(A) binding protein cytoplasmic 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:39,560,709-39,576,790 (-) |
| Ensembl biotype | protein_coding |
| Also known as | iPABP, APP-1 |
| Gene groups (HGNC) | RNA binding motif containing; Small nucleolar RNA protein coding host genes |
| Hallmark sets | MYC_TARGETS_V1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13310](https://www.uniprot.org/uniprotkb/Q13310) (Polyadenylate-binding protein 4):

> Binds the poly(A) tail of mRNA. Binds to SMIM26 mRNA and plays a role in its post-transcriptional regulation. May be involved in cytoplasmic regulatory processes of mRNA metabolism. Can probably bind to cytoplasmic RNA sequences other than poly(A) in vivo (By similarity).

**Summary**, from NCBI Gene [8761](https://www.ncbi.nlm.nih.gov/gene/8761):

> Poly(A)-binding proteins (PABPs) bind to the poly(A) tail present at the 3-prime ends of most eukaryotic mRNAs. PABPC4 or IPABP (inducible PABP) was isolated as an activation-induced T-cell mRNA encoding a protein. Activation of T cells increased PABPC4 mRNA levels in T cells approximately 5-fold. PABPC4 contains 4 RNA-binding domains and proline-rich C terminus. PABPC4 is localized primarily to the cytoplasm. It is suggested that PABPC4 might be necessary for regulation of stability of labile …

**Accessions** — [HGNC:8557](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8557) · Entrez [8761](https://www.ncbi.nlm.nih.gov/gene/8761) · UniProt [Q13310](https://www.uniprot.org/uniprotkb/Q13310) · Ensembl [ENSG00000090621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090621)

## Data

Gene col 1633: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1633); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1633, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1633]; `tensor/DDL_lfc|DDL_z.npy` [1633]; `embed/gene_vectors.npy` [1633]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1633 or target_col == 1633). Every well: [[PABPC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PABPC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
