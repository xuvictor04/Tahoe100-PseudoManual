---
symbol: "MAGT1"
type: "gene"
col: 2220
ensembl_id: "ENSG00000102158"
name: "magnesium transporter 1"
location: "Xq21.1"
module: 42
arm: "+"
pooled_cpm: 139.85
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# MAGT1

*magnesium transporter 1* — Xq21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.07× (z +15.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.799× (z -4.9, q 4e-04, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CALR]] (+0.66, fdr 7e-06), [[COPE]] (+0.66, fdr 1e-05), [[P4HB]] (+0.63, fdr 1e-05); moves opposite to [[MRM1]] (-0.64, fdr 1e-05), [[KLHL42]] (-0.61, fdr 1e-05), [[TFAP4]] (-0.60, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[AGR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2220.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.07×** | +15.8 | 0e+00 | 47/48 (SNU-423, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +14.2 | 2e-43 | 46/48 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.91×** | +14.1 | 1e-42 | 46/48 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +12.4 | 6e-33 | 38/49 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +9.9 | 5e-21 | 29/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +7.8 | 5e-13 | 36/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.44×** | +7.7 | 2e-12 | 30/44 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +7.2 | 4e-11 | 35/48 (SNU-423, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.35×** | +6.1 | 9e-08 | 30/45 (A498, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.26×** | +5.0 | 3e-05 | 27/48 (SNU-423, LOX-IMVI, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +4.8 | 8e-05 | 33/49 (LOX-IMVI, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.6 | 2e-04 | 18/48 (SNU-423, Hs 766T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.25×** | +4.6 | 2e-04 | 27/48 (PANC-1, AsPC-1, …) | top dose only | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.23×** | +4.3 | 8e-04 | 25/50 (HOP62, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.20× | +3.9 | 0.003 | 20/48 (LOX-IMVI, SNU-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2220.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.799×** | -4.9 | 4e-04 | 28/48 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.856× | -4.8 | 4e-04 | 16/48 (RPMI-7951, CFPAC-1, …) | rises with dose |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.870× | -4.3 | 0.003 | 15/48 (NCI-H1573, H4, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.827×** | -4.2 | 0.004 | 24/48 (A549, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.831×** | -3.8 | 0.019 | 23/47 (hTERT-HPNE, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.844× | -3.6 | 0.028 | 22/47 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.845× | -3.6 | 0.028 | 22/47 (C-33 A, J82, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.851× | -3.5 | 0.028 | 17/48 (J82, Hs 766T, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.853× | -3.5 | 0.029 | 19/48 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.899× | -3.3 | 0.050 | 16/49 (SW480, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.824×** | -3.2 | 0.058 | 18/48 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.902× | -3.2 | 0.058 | 9/48 (HS-578T, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.906× | -3.1 | 0.085 | 13/48 (NCI-H1573, HS-578T, …) | top dose only | low cells (technical?) |
| [[Radotinib (drug)]] 0.5 µM |  | 0.872× | -3.0 | 0.11 | 17/48 (PANC-1, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2220. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 122 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +19.5) | — |
| [[NCI-H460 (line)]] | wt | 155 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +13.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 130 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.9) | — |
| [[SNU-423 (line)]] | alt | 221 | 7 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.78× (z +15.3) | — |
| [[A498 (line)]] | wt | 128 | 6 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.03× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 149 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.26× (z +11.4) | — |
| [[J82 (line)]] | alt | 129 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +12.3) | — |
| [[LOX-IMVI (line)]] | wt | 93.3 | 5 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.77× (z +13.6) | — |
| [[SW480 (line)]] | alt | 159 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 120 | 4 | 0 | [[Belinostat (drug)]] 5 µM 2.66× (z +12.2) | — |
| [[HS-578T (line)]] | alt | 133 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.11× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 145 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 121 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.78× (z +11.0) | — |
| [[A-427 (line)]] | wt | 96.0 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 2.08× (z +9.4) | — |
| [[A549 (line)]] | wt | 150 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 163 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.45× (z +11.0) | — |
| [[RKO (line)]] | wt | 103 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.30× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 177 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +18.2) | — |
| [[C-33 A (line)]] | alt | 73.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +9.7) ⚠ toxic; transcription drop | [[Niclosamide (olamine) (drug)]] 5 µM 0.306× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 107 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.97× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HepG2_C3A (line)]] | wt | 88.1 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.36× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 115 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.24× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 82.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +9.1) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 117 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.49× (z +8.9) | — |
| [[KATO III (line)]] | alt | 238 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.475× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 68.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 98.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.5) | — |
| [[SNU-1 (line)]] | wt | 89.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 180 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 80.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2220), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALR]] | +0.66 | +0.60 / +0.60 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[COPE]] | +0.66 | +0.66 / +0.52 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[P4HB]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 | pathway: Dengue Virus Genome Translation and Replication |
| [[MANF]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[PDIA4]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 | STRING 472 |
| [[CHP1]] | +0.61 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[SEC31A]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[DAP]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[CALU]] | +0.60 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[LMAN1]] | +0.59 | +0.55 / +0.49 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[SPAG9]] | +0.58 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[TMED9]] | +0.58 | +0.55 / +0.45 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRM1]] | -0.64 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[KLHL42]] | -0.61 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[TFAP4]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[NUDT19]] | -0.57 | -0.47 / -0.57 | both halves | 2e-05 | pathway: Protein localization |
| [[QTRT2]] | -0.57 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[PATZ1]] | -0.56 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[TGFBRAP1]] | -0.55 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[C1orf109]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ZNF746]] | -0.55 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[ZNF665]] | -0.54 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[ZBTB24]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ZNF282]] | -0.54 | -0.41 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGR2]] | B | AGR2 activity raises MAGT1's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.34× lower at baseline in the lines without AGR2 | 0.067 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.8, -31.2); signed map (-54.5, 9.0). **Vector** length 133, 43.4% of its response variance represented; |z| ≥ 3 in 1,122 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.54 to 11); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.52 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +12.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +14.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.4 | +14.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.3 | +15.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +3.5 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +4.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.8 | +1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +2.2 | +1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +2.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -7.5 | -3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.4 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.4 | -4.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -5.3 | -3.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.2 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -1.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.1 | -4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.1 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | magnesium transporter 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.1 — chrX:77,825,747-77,899,271 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp564K142, IAP, OST3B, MRX95, SLC58A1 |
| Gene groups (HGNC) | Oligosaccharyltransferase complex subunits; Solute carrier family 58 |
| Reactome | 22 pathways, smallest: PD-L1(CD274) glycosylation and translocation to plasma membrane; Miscellaneous transport and binding events; Maturation of spike protein_9694548 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0U3](https://www.uniprot.org/uniprotkb/Q9H0U3) (Dolichyl-diphosphooligosaccharide--protein glycosyltransferase subunit MAGT1):

> Accessory component of the STT3B-containing form of the N-oligosaccharyl transferase (OST) complex which catalyzes the transfer of a high mannose oligosaccharide from a lipid-linked oligosaccharide donor to an asparagine residue within an Asn-Xaa-Ser/Thr consensus motif in nascent polypeptide chains. Involved in N-glycosylation of STT3B-dependent substrates. Specifically required for the glycosylation of a subset of acceptor sites that are near cysteine residues; in this function seems to act …

**Summary**, from NCBI Gene [84061](https://www.ncbi.nlm.nih.gov/gene/84061):

> This gene encodes a ubiquitously expressed magnesium cation transporter protein that localizes to the cell membrane. This protein also associates with N-oligosaccharyl transferase and therefore may have a role in N-glycosylation. Mutations in this gene cause a form of X-linked intellectual disability (XLID). This gene may have multiple in-frame translation initiation sites, one of which would encode a shorter protein with an N-terminus containing a signal peptide at amino acids 1-29. [provided …

**Accessions** — [HGNC:28880](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28880) · Entrez [84061](https://www.ncbi.nlm.nih.gov/gene/84061) · UniProt [Q9H0U3](https://www.uniprot.org/uniprotkb/Q9H0U3) · Ensembl [ENSG00000102158](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102158)

## Data

Gene col 2220: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2220); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2220, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2220]; `tensor/DDL_lfc|DDL_z.npy` [2220]; `embed/gene_vectors.npy` [2220]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2220 or target_col == 2220). Every well: [[MAGT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAGT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
