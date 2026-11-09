---
symbol: "CDK2AP1"
type: "gene"
col: 3220
ensembl_id: "ENSG00000111328"
name: "cyclin dependent kinase 2 associated protein 1"
location: "12q24.31"
module: 15
arm: "+"
pooled_cpm: 26.03
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# CDK2AP1

*cyclin dependent kinase 2 associated protein 1* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.93× (z +17.1, q 0e+00, up in 42 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +11.2, q 1e-26, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.435× (z -10.4, q 2e-22, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYB561A3]] (+0.67, fdr 3e-05), [[LAMTOR5-AS1]] (+0.67, fdr 7e-05), [[LDB1]] (+0.66, fdr 1e-05); moves opposite to [[PUS3]] (-0.64, fdr 1e-05), [[POLM]] (-0.63, fdr 5e-05), [[CEP290]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3220.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.93×** | +17.1 | 0e+00 | 42/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.52×** | +15.1 | 0e+00 | 37/37 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +11.2 | 1e-26 | 43/48 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.54×** | +10.8 | 5e-25 | 38/43 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.5 | 1e-08 | 33/48 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.62×** | +6.1 | 1e-07 | 30/46 (NCI-H2030, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +5.4 | 5e-06 | 29/45 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.1 | 2e-05 | 28/47 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +4.4 | 6e-04 | 27/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.34×** | +3.7 | 0.011 | 22/47 (SW480, SW1417, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.012 | 19/48 (SW1417, SNU-423, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **1.33×** | +3.4 | 0.028 | 23/47 (NCI-H1792, HOP62, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.27× | +3.0 | 0.12 | 15/47 (NCI-H2030, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3220.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.435×** | -10.4 | 2e-22 | 41/48 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.439×** | -10.3 | 3e-22 | 43/48 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.601×** | -8.9 | 8e-17 | 40/48 (A-427, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.494×** | -8.8 | 2e-16 | 44/48 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.550×** | -7.4 | 1e-11 | 40/48 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.715×** | -5.9 | 4e-07 | 34/48 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.666×** | -5.0 | 4e-05 | 29/48 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.695×** | -4.5 | 5e-04 | 27/47 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.467×** | -4.3 | 9e-04 | 24/48 (C32, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.709×** | -4.1 | 0.002 | 24/48 (A-427, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.726×** | -4.0 | 0.004 | 25/47 (LoVo, HS-578T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.743×** | -3.7 | 0.011 | 19/48 (C32, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.769×** | -3.2 | 0.051 | 19/48 (SK-MEL-2, LS 180, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.772×** | -3.2 | 0.052 | 17/47 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **0.772×** | -3.2 | 0.052 | 15/48 (NCI-H1573, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3220. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 97.8 | 2 (2 ⚠) | 7 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +9.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.206× (z -12.6) |
| [[LoVo (line)]] | wt | 30.8 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 5.42× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.231× (z -12.0) |
| [[KATO III (line)]] | alt | 21.8 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 6.12× (z +12.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 50.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 11.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.72× (z +13.6) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.240× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.212× (z -9.0) |
| [[A-427 (line)]] | wt | 39.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -13.1) |
| [[AsPC-1 (line)]] | alt | 20.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -13.1) |
| [[HOP62 (line)]] | alt | 24.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.02× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 23.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 25.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -12.1) |
| [[LS 180 (line)]] | wt | 22.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.95× (z +12.6) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.239× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 25.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -12.4) |
| [[PANC-1 (line)]] | alt | 33.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +14.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 11.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.90× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +9.0) | — |
| [[SW480 (line)]] | alt | 13.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.82× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +8.6) | — |
| [[A-172 (line)]] | wt | 35.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +8.6) | — |
| [[A498 (line)]] | wt | 27.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +12.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 14.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.28× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +11.3) | — |
| [[C-33 A (line)]] | alt | 36.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -9.8) |
| [[J82 (line)]] | alt | 27.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 17.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.86× (z +12.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 33.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 12.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.35× (z +10.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.193× (z -9.2) |
| [[SHP-77 (line)]] | alt | 29.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.76× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 18.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 30.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 26.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +9.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 15.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 27.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -11.3) |
| [[SW 900 (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.84× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 28.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -9.7) |
| [[AN3 CA (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3220), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB561A3]] | +0.67 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[LAMTOR5-AS1]] | +0.67 | +0.37 / +0.51 | both halves | 7e-05 |  |
| [[LDB1]] | +0.66 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[SUMO3]] | +0.66 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[BCL2L2-PABPN1]] | +0.65 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[PRDM10]] | +0.64 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[GNAS]] | +0.64 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[CRPPA]] | +0.63 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[PDIA3P1]] | +0.62 | +0.45 / +0.38 | both halves | 7e-05 |  |
| [[PNISR-AS1]] | +0.62 | +0.20 / +0.52 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ANP32A]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SAP30L-AS1]] | +0.62 | +0.36 / +0.37 | both halves | 1e-04 |  |
| [[C5orf15]] | +0.61 | +0.38 / +0.47 | both halves | 7e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS3]] | -0.64 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[POLM]] | -0.63 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[CEP290]] | -0.61 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[TBC1D25]] | -0.59 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[NOL7]] ⚠ | -0.58 | -0.48 / -0.46 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CINP]] | -0.58 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[DHRS2]] | -0.58 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[DDX19B]] | -0.57 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[MPHOSPH10]] | -0.57 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[GPATCH11]] | -0.56 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[COMMD2]] | -0.56 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[KRI1]] | -0.56 | -0.32 / -0.61 | both halves | 1e-04 |  |
| [[CCDC112]] | -0.56 | -0.23 / -0.52 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CDK2AP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FSTL1]] | B | FSTL1 activity raises CDK2AP1's level | lines that do not express FSTL1 (21) vs lines expressing it (29) | 1.00× lower at baseline in the lines without FSTL1 | 0.057 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ABI3BP, TFPI2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.527). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-4.0, 22.1); signed map (30.4, -22.2). **Vector** length 88.0, 23.0% of its response variance represented; |z| ≥ 3 in 934 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +11.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | -0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.1 | -0.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.7 | -0.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.7 | -10.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.4 | -3.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.2 | -10.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.2 | -8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 2 associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:123,250,112-123,272,334 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DORC1, doc-1, DOC1, ST19, p12DOC-1 |
| Gene groups (HGNC) | NuRD complex subunits |
| Reactome | 6 pathways, smallest: Interaction of NuRD complexes with transcription factors; NuRD complex assembly; CHD3, CHD4, CHD5 subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [O14519](https://www.uniprot.org/uniprotkb/O14519) (Cyclin-dependent kinase 2-associated protein 1):

> Inhibitor of cyclin-dependent kinase CDK2 (By similarity). Also acts as a component of the histone deacetylase NuRD complex which participates in the remodeling of chromatin.

**Summary**, from NCBI Gene [8099](https://www.ncbi.nlm.nih.gov/gene/8099):

> The protein encoded by this gene is a cyclin-dependent kinase 2 (CDK2) -associated protein which is thought to negatively regulate CDK2 activity by sequestering monomeric CDK2, and targeting CDK2 for proteolysis. This protein was found to also interact with DNA polymerase alpha/primase and mediate the phosphorylation of the large p180 subunit, which suggests a regulatory role in DNA replication during the S-phase of the cell cycle. This protein also forms a core subunit of the nucleosome …

**Accessions** — [HGNC:14002](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14002) · Entrez [8099](https://www.ncbi.nlm.nih.gov/gene/8099) · UniProt [O14519](https://www.uniprot.org/uniprotkb/O14519) · Ensembl [ENSG00000111328](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111328)

## Data

Gene col 3220: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3220); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3220, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3220]; `tensor/DDL_lfc|DDL_z.npy` [3220]; `embed/gene_vectors.npy` [3220]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3220 or target_col == 3220). Every well: [[CDK2AP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK2AP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
