---
symbol: "PKP4"
type: "gene"
col: 6861
ensembl_id: "ENSG00000144283"
name: "plakophilin 4"
location: "2q24.1"
module: 5
arm: "+"
pooled_cpm: 193.01
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PKP4

*plakophilin 4* — 2q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.42× (z +11.2, q 3e-26, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.751× (z -9.2, q 2e-17, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATR]] (+0.63, fdr 7e-06), [[SLFNL1-AS1]] (+0.62, fdr 1e-05), [[CTPS1]] (+0.61, fdr 1e-05); moves opposite to [[USP30]] (-0.62, fdr 1e-05), [[FRG1JP]] (-0.60, fdr 1e-05), [[CLIP3]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CXCL5]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NSD2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6861.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +11.2 | 3e-26 | 32/48 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +9.1 | 3e-17 | 26/49 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +8.2 | 4e-14 | 35/48 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +7.7 | 2e-12 | 36/48 (A-172, A549, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.35×** | +6.7 | 2e-09 | 35/47 (NCI-H460, A-172, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.35×** | +6.6 | 3e-09 | 31/48 (NCI-H460, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +6.0 | 1e-07 | 25/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.26×** | +5.2 | 1e-05 | 26/48 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.24×** | +4.9 | 7e-05 | 27/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.21×** | +4.3 | 0.001 | 23/48 (A-172, RPMI-7951, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.9 | 0.005 | 22/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.18× | +3.7 | 0.010 | 19/48 (A-172, SW 900, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | 1.18× | +3.7 | 0.010 | 22/47 (HOP62, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 1.16× | +3.4 | 0.029 | 20/48 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.037 | 22/49 (NCI-H460, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.2 | 0.043 | 13/48 (NCI-H2347, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6861.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.751×** | -9.2 | 2e-17 | 29/48 (RKO, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.671×** | -9.1 | 3e-17 | 35/48 (SW48, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.750×** | -6.5 | 1e-08 | 35/48 (A-427, RKO, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.804×** | -5.0 | 9e-05 | 27/49 (LoVo, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.821×** | -4.5 | 7e-04 | 29/49 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.826×** | -4.4 | 0.001 | 23/48 (COLO 205, SW 1088, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -4.1 | 0.003 | 23/48 (SW48, SNU-1, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.892× | -3.7 | 0.015 | 10/48 (CFPAC-1, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.853× | -3.5 | 0.031 | 19/44 (C-33 A, LoVo, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.856× | -3.4 | 0.045 | 20/48 (SNU-1, SW48, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.864× | -3.3 | 0.045 | 19/48 (SW48, LoVo, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.866× | -3.3 | 0.049 | 20/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 0.910× | -3.1 | 0.095 | 9/48 (HepG2/C3A, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6861. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 142 | 12 (8 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +18.6) | [[Selinexor (drug)]] 5 µM 0.541× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 120 | 10 (7 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +25.1) | — |
| [[A-427 (line)]] | wt | 224 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +11.4) | [[Auranofin (drug)]] 5 µM 0.424× (z -13.6) |
| [[C32 (line)]] | wt | 248 | 0 | 6 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.402× (z -9.7) |
| [[LoVo (line)]] | wt | 215 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.55× (z +9.9) | [[Auranofin (drug)]] 5 µM 0.416× (z -14.1) |
| [[SW48 (line)]] | wt | 299 | 0 | 6 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.181× (z -17.1) |
| [[HOP62 (line)]] | alt | 112 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +15.6) | — |
| [[LOX-IMVI (line)]] | wt | 196 | 1 (1 ⚠) | 4 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +10.5) ⚠ cell-cycle shift, explains ~22% of this change | [[Homoharringtonine (drug)]] 5 µM 0.586× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 97.2 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +16.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 146 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.7) | — |
| [[RKO (line)]] | wt | 237 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.388× (z -15.4) |
| [[SNU-1 (line)]] | wt | 227 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.509× (z -9.3) |
| [[SW480 (line)]] | alt | 288 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.64× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.470× (z -14.3) |
| [[A498 (line)]] | wt | 213 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.52× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -11.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 102 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +15.2) | — |
| [[NCI-H1573 (line)]] | alt | 130 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.606× (z -10.6) |
| [[SW 900 (line)]] | alt | 185 | 3 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +10.0) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.1) | — |
| [[C-33 A (line)]] | alt | 233 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 58.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +10.5) | — |
| [[H4 (line)]] | wt | 142 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +18.0) | — |
| [[HepG2_C3A (line)]] | wt | 329 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 163 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.442× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 233 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.492× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.519× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 89.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.8) | — |
| [[RPMI-7951 (line)]] | alt | 97.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +12.4) | — |
| [[SK-MEL-2 (line)]] | alt | 265 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.495× (z -10.6) |
| [[SNU-423 (line)]] | alt | 95.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.7) | — |
| [[A549 (line)]] | wt | 168 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 249 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.5) | — |
| [[CHP-212 (line)]] | wt | 141 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.270× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 235 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.488× (z -10.2) |
| [[HS-578T (line)]] | alt | 133 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 389 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.385× (z -13.1) |
| [[LS 180 (line)]] | wt | 228 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.377× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 220 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.645× (z -8.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 224 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 94.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 266 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 413 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6861), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATR]] | +0.63 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[SLFNL1-AS1]] | +0.62 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[CTPS1]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[ADGRA3]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[NSD2]] | +0.60 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[STK39]] | +0.60 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[EIF4G3]] | +0.60 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[EHBP1]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[SNRPB]] | +0.60 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ZNF704]] | +0.60 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[R3HDM1]] | +0.59 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[PSPC1]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP30]] | -0.62 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[FRG1JP]] | -0.60 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[CLIP3]] | -0.59 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[VPS37D]] | -0.59 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[SECISBP2L]] | -0.59 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[BCAS2]] | -0.57 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[PRKAB2]] | -0.57 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[PLCD1]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[IL17RC]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[THAP8]] | -0.55 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[CGRRF1]] | -0.54 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[TMEM9]] | -0.54 | -0.49 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL5]] | B | CXCL5 activity strengthens PKP4's drug response | lines that do not express CXCL5 (35) vs lines expressing it (14) | the lines without CXCL5 respond 0.78× as strongly (z diff +0.94); strongest at Homoharringtonine 5 µM: 1.22x vs 1.87x (z diff +5.7) | 0.033 | ⚠ within organs, on part of the lines; also absent: ANXA10, IRAK3, TRBC2; target measured in part of the lines; both ways; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers PKP4's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GNG2]] | B | GNG2 activity strengthens PKP4's drug response | lines that do not express GNG2 (22) vs lines expressing it (27) | the lines without GNG2 respond 0.76× as strongly (z diff +0.86); strongest at Idarubicin (hydrochloride) 5 µM: 1.09x vs 1.53x (z diff +4.2) | 0.081 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT; target measured in part of the lines; artifact flags |
| [[MTHFD1L]] | C | MTHFD1L activity raises PKP4's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 2.32× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NSD2]] | C | PKP4's natural level strengthens NSD2's drug response | PKP4's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.04; direction not clear | 0.076 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.524). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-1.4, -32.8); signed map (4.5, -50.9). **Vector** length 147, 49.7% of its response variance represented; |z| ≥ 3 in 1,395 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +8.5 | +8.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +8.3 | +7.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +8.0 | +6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | +5.9 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.4 | +5.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.9 | +1.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | +3.7 | +2.0 |
|  | [[Acetohexamide (drug)]] 5 µM |  | +3.0 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +6.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.8 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.8 | -9.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -8.6 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.9 | -9.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | -6.0 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -3.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -4.9 | -4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | plakophilin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.1 — chr2:158,456,952-158,682,879 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p0071 |
| Gene groups (HGNC) | Armadillo repeat containing; p120 catenin family |
| Reactome | 8 pathways, smallest: Formation of the cornified envelope; Keratinization; RND1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99569](https://www.uniprot.org/uniprotkb/Q99569) (Plakophilin-4):

> Plays a role as a regulator of Rho activity during cytokinesis. May play a role in junctional plaques.

**Summary**, from NCBI Gene [8502](https://www.ncbi.nlm.nih.gov/gene/8502):

> Armadillo-like proteins are characterized by a series of armadillo repeats, first defined in the Drosophila 'armadillo' gene product, that are typically 42 to 45 amino acids in length. These proteins can be divided into subfamilies based on their number of repeats, their overall sequence similarity, and the dispersion of the repeats throughout their sequences. Members of the p120(ctn)/plakophilin subfamily of Armadillo-like proteins, including CTNND1, CTNND2, PKP1, PKP2, PKP4, and ARVCF. PKP4 …

**Accessions** — [HGNC:9026](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9026) · Entrez [8502](https://www.ncbi.nlm.nih.gov/gene/8502) · UniProt [Q99569](https://www.uniprot.org/uniprotkb/Q99569) · Ensembl [ENSG00000144283](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144283)

## Data

Gene col 6861: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6861); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6861, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6861]; `tensor/DDL_lfc|DDL_z.npy` [6861]; `embed/gene_vectors.npy` [6861]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6861 or target_col == 6861). Every well: [[PKP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
