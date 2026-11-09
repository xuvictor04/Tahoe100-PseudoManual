---
symbol: "LARP1B"
type: "gene"
col: 6219
ensembl_id: "ENSG00000138709"
name: "La ribonucleoprotein 1B"
location: "4q28.2"
module: 39
arm: "+"
pooled_cpm: 114.41
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# LARP1B

*La ribonucleoprotein 1B* — 4q28.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.85× (z +18.0, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.374× (z -10.6, q 2e-23, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB8A]] (+0.65, fdr 1e-05), [[HEATR5A]] (+0.62, fdr 7e-06), [[GABRR2]] (+0.59, fdr 2e-05); moves opposite to [[BCL9]] (-0.59, fdr 2e-05), [[VTA1]] (-0.57, fdr 2e-05), [[HDAC1]] (-0.55, fdr 8e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6219.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +18.0 | 0e+00 | 39/48 (NCI-H1573, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +15.7 | 0e+00 | 38/49 (AsPC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +12.5 | 2e-33 | 40/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +12.2 | 8e-32 | 39/48 (C32, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +8.9 | 7e-17 | 40/50 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +5.7 | 1e-06 | 27/48 (NCI-H1573, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.12 | 12/49 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +3.0 | 0.17 | 17/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6219.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.374×** | -10.6 | 2e-23 | 42/49 (RKO, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.762×** | -8.0 | 5e-13 | 31/48 (HOP62, SNU-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.589×** | -5.7 | 2e-06 | 33/47 (AsPC-1, SW480, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.765×** | -5.5 | 4e-06 | 32/48 (LoVo, BT-474, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.766×** | -5.5 | 4e-06 | 31/48 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.783×** | -5.1 | 4e-05 | 27/48 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.862× | -4.4 | 0.001 | 16/48 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.870× | -4.1 | 0.003 | 11/48 (A-172, PANC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.825×** | -4.0 | 0.005 | 23/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.827×** | -3.6 | 0.016 | 20/47 (hTERT-HPNE, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 0.887× | -3.5 | 0.021 | 11/48 (AsPC-1, NCI-H2030, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.728×** | -3.4 | 0.029 | 22/48 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adenine (drug)]] 5 µM |  | 0.893× | -3.3 | 0.037 | 10/48 (LoVo, HT-29, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | 0.853× | -3.3 | 0.040 | 18/48 (BT-474, NCI-H2030, …) | all doses, flat | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.854× | -3.3 | 0.040 | 19/48 (LoVo, SW480, …) | two highest doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.860× | -3.0 | 0.085 | 12/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6219. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 99.7 | 5 | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.528× (z -8.8) |
| [[LoVo (line)]] | wt | 205 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.415× (z -11.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C32 (line)]] | wt | 49.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +17.3) | — |
| [[HOP62 (line)]] | alt | 108 | 3 | 2 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +11.1) | [[Selinexor (drug)]] 5 µM 0.577× (z -9.2) |
| [[LS 180 (line)]] | wt | 111 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +12.5) | — |
| [[NCI-H460 (line)]] | wt | 98.4 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +15.6) | — |
| [[RKO (line)]] | wt | 89.2 | 4 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +17.2) | [[TAK-901 (drug)]] 5 µM 0.159× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 86.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +18.2) | — |
| [[SW1417 (line)]] | alt | 98.9 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[SW480 (line)]] | alt | 82.4 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +17.5) | [[Panobinostat (drug)]] 0.5 µM 0.504× (z -9.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 156 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +10.8) | [[Ixazomib citrate (drug)]] 5 µM 0.513× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 99.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +18.7) | — |
| [[CFPAC-1 (line)]] | alt | 81.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +17.0) | — |
| [[hTERT-HPNE (line)]] | wt | 92.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +14.1) | — |
| [[LOX-IMVI (line)]] | wt | 45.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +17.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 118 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +12.2) | — |
| [[NCI-H1573 (line)]] | alt | 160 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +18.8) | — |
| [[NCI-H23 (line)]] | alt | 58.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +13.2) | — |
| [[NCI-H2347 (line)]] | alt | 99.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.9) | — |
| [[SW 900 (line)]] | alt | 99.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +14.7) | — |
| [[A-172 (line)]] | wt | 147 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -11.4) |
| [[COLO 205 (line)]] | alt | 91.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +15.9) | — |
| [[H4 (line)]] | wt | 147 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.6) | — |
| [[HEC-1-A (line)]] | alt | 175 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.418× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.280× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 108 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +17.2) | — |
| [[Hs 766T (line)]] | wt | 90.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +12.4) | — |
| [[HS-578T (line)]] | alt | 102 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.227× (z -9.4) |
| [[KATO III (line)]] | alt | 151 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 129 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +11.5) | [[TAK-901 (drug)]] 5 µM 0.347× (z -9.1) |
| [[SNU-423 (line)]] | alt | 67.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +11.6) | — |
| [[SW48 (line)]] | wt | 91.9 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.53× (z +12.3) | — |
| [[A-427 (line)]] | wt | 114 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.83× (z +8.5) | — |
| [[A549 (line)]] | wt | 101 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.256× (z -8.6) |
| [[BT-474 (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.423× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 177 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.3) | — |
| [[NCI-H1792 (line)]] | alt | 116 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.493× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 67.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 82.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 106 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 149 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 94.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6219), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB8A]] | +0.65 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[HEATR5A]] | +0.62 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[GABRR2]] | +0.59 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[LINC02936]] | +0.58 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[PSMD6-AS2]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[MIRLET7IHG]] | +0.56 | +0.63 / +0.36 | both halves | 1e-04 |  |
| [[CDR2]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[CORIN]] | +0.56 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[PYCR2]] | +0.56 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[CYP20A1]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[MFSD2B]] | +0.54 | +0.62 / +0.38 | both halves | 7e-05 |  |
| [[ITCH]] | +0.54 | +0.34 / +0.47 | both halves | 1e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL9]] | -0.59 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[VTA1]] | -0.57 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[HDAC1]] | -0.55 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[NAA40]] | -0.54 | -0.58 / -0.28 | both halves | 3e-04 |  |
| [[TRIM32]] | -0.54 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[CSTF2]] | -0.53 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[HPSE]] | -0.53 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[AP2S1]] | -0.53 | -0.62 / -0.24 | both halves | 4e-04 |  |
| [[RPP30]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[TMEM9]] | -0.52 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[ADH5]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[SDHAF3]] | -0.51 | -0.52 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LARP1B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.455). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.6, -37.5); signed map (12.3, 1.5). **Vector** length 146, 47.1% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +12.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.7 | +12.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +18.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +15.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.2 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +1.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +2.8 | +3.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.2 | -8.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -9.3 | -10.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -9.0 | -5.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -7.8 | -3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -7.0 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.5 | -5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.3 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.9 | -3.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.3 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | La ribonucleoprotein 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.2 — chr4:128,061,286-128,222,931 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10378, DKFZp434K245, DKFZp686E0316; previously LARP2 |
| Gene groups (HGNC) | La ribonucleoproteins |
| Matched by | ensembl_id |

UniProt [Q659C4](https://www.uniprot.org/uniprotkb/Q659C4) carries no function annotation.

**Summary**, from NCBI Gene [55132](https://www.ncbi.nlm.nih.gov/gene/55132):

> This gene encodes a protein containing domains found in the La related protein of Drosophila melanogaster. La motif-containing proteins are thought to be RNA-binding proteins, where the La motif and adjacent amino acids fold into an RNA recognition motif. The La motif is also found in proteins unrelated to the La protein. Alternative splicing has been observed at this locus and multiple variants, encoding distinct isoforms, are described. Additional splice variation has been identified but the …

**Accessions** — [HGNC:24704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24704) · Entrez [55132](https://www.ncbi.nlm.nih.gov/gene/55132) · UniProt [Q659C4](https://www.uniprot.org/uniprotkb/Q659C4) · Ensembl [ENSG00000138709](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138709)

## Data

Gene col 6219: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6219); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6219, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6219]; `tensor/DDL_lfc|DDL_z.npy` [6219]; `embed/gene_vectors.npy` [6219]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6219 or target_col == 6219). Every well: [[LARP1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LARP1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
