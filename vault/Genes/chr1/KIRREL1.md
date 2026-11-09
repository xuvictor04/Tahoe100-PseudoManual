---
symbol: "KIRREL1"
type: "gene"
col: 11466
ensembl_id: "ENSG00000183853"
name: "kirre like nephrin family adhesion molecule 1"
location: "1q23.1"
module: 145
arm: "+"
pooled_cpm: 134.28
n_lines_expressing: 42
n_dd_up: 1
n_dd_down: 21
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# KIRREL1

*kirre like nephrin family adhesion molecule 1* — 1q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.01× (z +5.9, q 3e-06, up in 26 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-172 1.84×, SW 900 1.94×, A498 1.86×; ⚠ cell-cycle shift, explains ~47% of this change); [[Selinexor (drug)]] 5 µM in 1 line (AsPC-1 2.26×; ⚠ cell-cycle shift, explains ~86% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 1.37×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.177× (z -27.8, q 0e+00, down in 39 of 40 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEK6]] (+0.54, fdr 1e-05), [[BNC2]] (+0.53, fdr 1e-05), [[FRMD6]] (+0.48, fdr 6e-05); moves opposite to [[DNAJB9]] (-0.47, fdr 2e-04), [[PPM1B]] (-0.47, fdr 2e-04), [[MIA2]] (-0.47, fdr 4e-05).
> It is in [[Module 145]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ZNF469]] → it (grade B ⚠); 10 go from it, the strongest it → [[DPY19L2P2-1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11466.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-172 1.84×, SW 900 1.94×, A498 1.86×; ⚠ cell-cycle shift, explains ~47% of this change); [[Selinexor (drug)]] 5 µM in 1 line (AsPC-1 2.26×; ⚠ cell-cycle shift, explains ~86% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 1.37×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.01×** | +5.9 | 3e-06 | 26/41 (RPMI-7951, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.2 | 0.007 | 1/42 (NCI-H23) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11466.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.177×** | -27.8 | 0e+00 | 39/40 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.190×** | -26.7 | 0e+00 | 40/40 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.421×** | -19.7 | 0e+00 | 41/41 (AsPC-1, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.320×** | -18.3 | 0e+00 | 39/40 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.550×** | -9.2 | 3e-18 | 32/40 (SNU-423, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.593×** | -8.4 | 4e-15 | 34/40 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.603×** | -8.1 | 3e-14 | 28/40 (C32, LoVo, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.615×** | -7.5 | 3e-12 | 31/42 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.655×** | -6.6 | 3e-09 | 22/36 (HCT15, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.698×** | -5.6 | 1e-06 | 24/39 (NCI-H1573, AsPC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.789×** | -5.4 | 3e-06 | 26/40 (C32, SK-MEL-2, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.729×** | -5.1 | 2e-05 | 29/41 (C32, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.740×** | -4.8 | 5e-05 | 27/40 (LS 180, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.825×** | -4.4 | 4e-04 | 19/40 (LoVo, C32, …) | two highest doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.784×** | -3.9 | 0.003 | 22/40 (NCI-H661, SW 1088, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.698×** | -3.7 | 0.006 | 22/40 (Hs 766T, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.854× | -3.6 | 0.009 | 17/40 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.815×** | -3.1 | 0.050 | 14/40 (NCI-H23, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.702×** | -3.0 | 0.078 | 16/41 (LoVo, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11466. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 331 | 1 (1 ⚠) | 20 (6 ⚠) | [[Selinexor (drug)]] 5 µM 2.26× (z +10.8) ⚠ cell-cycle shift, explains ~86% of this change | [[Panobinostat (drug)]] 5 µM 0.0802× (z -23.5) |
| [[C32 (line)]] | wt | 627 | 0 | 13 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -21.9) |
| [[LoVo (line)]] | wt | 90.0 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0846× (z -23.6) |
| [[NCI-H1573 (line)]] | alt | 57.9 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -16.3) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.144× (z -15.4) |
| [[RKO (line)]] | wt | 128 | 0 | 8 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0837× (z -25.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.155× (z -20.7) |
| [[CFPAC-1 (line)]] | alt | 238 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -18.0) |
| [[HEC-1-A (line)]] | alt | 162 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -22.5) |
| [[LOX-IMVI (line)]] | wt | 171 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -19.2) |
| [[LS 180 (line)]] | wt | 134 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -17.9) |
| [[SNU-423 (line)]] | alt | 233 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.0866× (z -23.9) |
| [[HOP62 (line)]] | alt | 142 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.117× (z -22.5) |
| [[NCI-H2030 (line)]] | alt | 193 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -18.1) |
| [[RPMI-7951 (line)]] | alt | 234 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -18.1) |
| [[SW480 (line)]] | alt | 39.3 | 2 (2 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.185× (z -19.0) |
| [[AN3 CA (line)]] | alt | 248 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -15.0) |
| [[CHP-212 (line)]] | wt | 224 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -13.1) |
| [[Hs 766T (line)]] | wt | 107 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -19.8) |
| [[hTERT-HPNE (line)]] | wt | 217 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 145 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -22.6) |
| [[SW 900 (line)]] | alt | 102 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.1) ⚠ cell-cycle shift, explains ~47% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -12.2) |
| [[A-172 (line)]] | wt | 182 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.7) ⚠ cell-cycle shift, explains ~47% of this change | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -18.5) |
| [[A549 (line)]] | wt | 130 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0892× (z -24.2) |
| [[H4 (line)]] | wt | 147 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -11.8) |
| [[J82 (line)]] | alt | 142 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -21.1) |
| [[MIA PaCa-2 (line)]] | alt | 214 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -24.4) |
| [[NCI-H1792 (line)]] | alt | 156 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -19.2) |
| [[NCI-H23 (line)]] | alt | 127 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.236× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 109 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -14.6) |
| [[SNU-1 (line)]] | wt | 48.5 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -12.3) |
| [[SW1417 (line)]] | alt | 48.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -13.5) |
| [[A498 (line)]] | wt | 300 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.0) ⚠ cell-cycle shift, explains ~47% of this change | [[Panobinostat (drug)]] 0.5 µM 0.320× (z -11.8) |
| [[HCT15 (line)]] | alt | 50.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -11.2) |
| [[HS-578T (line)]] | alt | 128 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -17.9) |
| [[NCI-H2347 (line)]] | alt | 61.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 77.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -15.5) |
| [[PANC-1 (line)]] | alt | 118 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -15.0) |
| [[SW 1088 (line)]] | alt | 277 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0590× (z -15.0) |
| [[A-427 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.78 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 30.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.72 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 25.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11466), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEK6]] | +0.54 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[BNC2]] | +0.53 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[FRMD6]] | +0.48 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[PFKM]] | +0.48 | +0.37 / +0.45 | both halves | 8e-05 |  |
| [[ATP13A3]] | +0.44 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[PLCG1]] | +0.44 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[ASIC1]] | +0.43 | +0.46 / +0.39 | both halves | 6e-05 |  |
| [[MIR155HG]] | +0.43 | +0.38 / +0.44 | both halves | 7e-05 |  |
| [[SEPTIN3]] | +0.43 | +0.36 / +0.33 | both halves | 1e-04 |  |
| [[CGREF1]] | +0.42 | +0.43 / +0.30 | both halves | 2e-04 |  |
| [[KAT2A]] | +0.42 | +0.24 / +0.49 | both halves | 4e-04 |  |
| [[DPY19L2P2-1]] | +0.41 | +0.12 / +0.47 | ⚠ not reproduced | 0.002 |  |
| [[AKR1E2]] | +0.41 | +0.23 / +0.35 | both halves | 5e-04 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB9]] | -0.47 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[PPM1B]] | -0.47 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[MIA2]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ETFDH]] | -0.45 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[SMIM14]] | -0.45 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[CDC37L1]] | -0.45 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ANKHD1]] | -0.44 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[ZNF524]] | -0.43 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[EXPH5]] | -0.43 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[ZNRF2]] | -0.43 | -0.23 / -0.46 | both halves | 5e-04 |  |
| [[EIF2S2]] | -0.42 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[PIP5K1B]] | -0.42 | -0.40 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF469]] | B | ZNF469 activity raises KIRREL1's level | lines that do not express ZNF469 (20) vs lines expressing it (30) | 2.72× lower at baseline in the lines without ZNF469 | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC02057, IL6, TMEM158 |
| [[DPY19L2P2-1]] | B | DPY19L2P2-1 activity raises KIRREL1's level | lines that do not express DPY19L2P2-1 (17) vs lines expressing it (33) | 2.59× lower at baseline in the lines without DPY19L2P2-1 | 0.082 | ⚠ within organs, on part of the lines; also absent: RNF182, ENSG00000234405, FGF2 |
| [[BNC2]] | B | BNC2 activity raises KIRREL1's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 2.92× lower at baseline in the lines without BNC2 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[FRMD6]] | C | FRMD6 activity raises KIRREL1's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 3.61× lower at baseline in the lines without FRMD6 | 0.072 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPY19L2P2-1]] | B | KIRREL1 activity raises DPY19L2P2-1's level | lines that do not express KIRREL1 (8) vs lines expressing it (42) | 2.22× lower at baseline in the lines without KIRREL1 | 0.042 | ⚠ within organs, on part of the lines; also absent: BEX3, ARHGAP31, ROBO3 |
| [[PALM2AKAP2]] | B | KIRREL1 activity raises PALM2AKAP2's level | lines that do not express KIRREL1 (8) vs lines expressing it (42) | 4.34× lower at baseline in the lines without KIRREL1 | 0.042 | ⚠ within organs, on part of the lines; also absent: BEX3, ARHGAP31, ROBO3 |
| [[ZNRF2]] | B | KIRREL1 activity lowers ZNRF2's level | lines that do not express KIRREL1 (8) vs lines expressing it (42) | 1.75× higher at baseline in the lines without KIRREL1 | 0.064 | ⚠ within organs, on part of the lines; also absent: BEX3, ARHGAP31, ROBO3 |
| [[TMC5]] | B | KIRREL1 activity lowers TMC5's level | lines that do not express KIRREL1 (8) vs lines expressing it (42) | 5.58× higher at baseline in the lines without KIRREL1 | 0.070 | ⚠ within organs, on part of the lines; also absent: BEX3, ARHGAP31, ROBO3 |
| [[EIF5A2]] | B | KIRREL1 activity raises EIF5A2's level | lines that do not express KIRREL1 (8) vs lines expressing it (42) | 1.59× lower at baseline in the lines without KIRREL1 | 0.073 | ⚠ within organs, on part of the lines; also absent: BEX3, ARHGAP31, ROBO3 |
| [[LINC03009]] | B | KIRREL1 activity raises LINC03009's level | lines that do not express KIRREL1 (8) vs lines expressing it (42) | 1.19× lower at baseline in the lines without KIRREL1 | 0.080 | ⚠ within organs, on part of the lines; also absent: BEX3, ARHGAP31, ROBO3 |
| [[TOX3]] | B | KIRREL1 activity lowers TOX3's level | lines that do not express KIRREL1 (8) vs lines expressing it (42) | 8.08× higher at baseline in the lines without KIRREL1 | 0.083 | ⚠ within organs, on part of the lines; also absent: BEX3, ARHGAP31, ROBO3 |
| [[ATP13A3]] | B | KIRREL1 activity raises ATP13A3's level | lines that do not express KIRREL1 (8) vs lines expressing it (42) | 1.92× lower at baseline in the lines without KIRREL1 | 0.088 | ⚠ within organs, on part of the lines; also absent: BEX3, ARHGAP31, ROBO3 |
| [[GCLC]] | B | KIRREL1 activity lowers GCLC's level | lines that do not express KIRREL1 (8) vs lines expressing it (42) | 2.68× higher at baseline in the lines without KIRREL1 | 0.095 | ⚠ within organs, on part of the lines; also absent: BEX3, ARHGAP31, ROBO3 |
| [[FRMD6]] | C | KIRREL1 activity raises FRMD6's level | lines that do not express KIRREL1 (8) vs lines expressing it (42) | 4.98× lower at baseline in the lines without KIRREL1 | 0.092 | ⚠ within organs, on part of the lines; also absent: BEX3, ARHGAP31, ROBO3; co-absent with the target |

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction -0.371). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.5, 24.3); signed map (29.0, 32.9). **Vector** length 102, 30.3% of its response variance represented; |z| ≥ 3 in 1,215 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +6.4 | +2.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +5.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | +3.4 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +2.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +0.6 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | -4.7 | -5.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.7 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.6 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -5.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.3 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | kirre like nephrin family adhesion molecule 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.1 — chr1:157,993,273-158,100,262 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NEPH1; previously KIRREL |
| Gene groups (HGNC) | C2-set domain containing; I-set domain containing; Kirre like nephrin family adhesion molecules |
| Reactome | 2 pathways, smallest: Nephrin family interactions; Cell-Cell communication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96J84](https://www.uniprot.org/uniprotkb/Q96J84) (Kin of IRRE-like protein 1):

> Required for proper function of the glomerular filtration barrier. It is involved in the maintenance of a stable podocyte architecture with interdigitating foot processes connected by specialized cell-cell junctions, known as the slit diaphragm. It is a signaling protein that needs the presence of TEC kinases to fully trans-activate the transcription factor AP-1 (By similarity).

**Summary**, from NCBI Gene [55243](https://www.ncbi.nlm.nih.gov/gene/55243):

> NEPH1 is a member of the nephrin-like protein family, which includes NEPH2 (MIM 607761) and NEPH3 (MIM 607762). The cytoplasmic domains of these proteins interact with the C terminus of podocin (NPHS2; MIM 604766), and the genes are expressed in kidney podocytes, cells involved in ensuring size- and charge-selective ultrafiltration (Sellin et al., 2003 [PubMed 12424224]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:15734](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15734) · Entrez [55243](https://www.ncbi.nlm.nih.gov/gene/55243) · UniProt [Q96J84](https://www.uniprot.org/uniprotkb/Q96J84) · Ensembl [ENSG00000183853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183853)

## Data

Gene col 11466: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11466); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11466, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11466]; `tensor/DDL_lfc|DDL_z.npy` [11466]; `embed/gene_vectors.npy` [11466]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11466 or target_col == 11466). Every well: [[KIRREL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIRREL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
