---
symbol: "OPA1"
type: "gene"
col: 12699
ensembl_id: "ENSG00000198836"
name: "OPA1 mitochondrial dynamin like GTPase"
location: "3q29"
module: 25
arm: "+"
pooled_cpm: 174.21
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# OPA1

*OPA1 mitochondrial dynamin like GTPase* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.71× (z +13.2, q 4e-37, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.637× (z -15.8, q 0e+00, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP14]] (+0.76, fdr 7e-06), [[NDRG3]] (+0.72, fdr 7e-06), [[API5]] (+0.72, fdr 1e-05); moves opposite to [[ERF]] (-0.71, fdr 7e-06), [[TNRC6C]] (-0.68, fdr 7e-06), [[MAD2L1BP]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ANXA6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12699.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +13.2 | 4e-37 | 47/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +9.9 | 1e-20 | 41/48 (A498, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.00×** | +9.8 | 3e-20 | 44/49 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +9.7 | 7e-20 | 46/48 (A498, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.55×** | +8.3 | 1e-14 | 39/48 (PANC-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +7.4 | 2e-11 | 32/48 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +6.6 | 4e-09 | 28/45 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +6.2 | 4e-08 | 30/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +5.9 | 2e-07 | 31/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 8e-06 | 36/49 (RKO, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.23×** | +4.9 | 6e-05 | 23/44 (NCI-H1792, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.22×** | +4.8 | 7e-05 | 26/48 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | 1.20× | +4.4 | 5e-04 | 22/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | 1.18× | +4.1 | 0.002 | 20/49 (SHP-77, NCI-H1792, …) | all doses, flat | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.003 | 26/48 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.7 | 0.006 | 20/48 (A498, SHP-77, …) | top dose only |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.040 | 9/48 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.09× | +3.0 | 0.054 | 5/49 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.066 | 14/48 (SW48, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12699.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -15.8 | 0e+00 | 39/49 (Panc 03.27, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.750×** | -6.9 | 2e-09 | 32/48 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.842× | -6.0 | 3e-07 | 24/48 (HOP62, SW1417, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.793×** | -5.7 | 1e-06 | 30/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.810×** | -5.2 | 2e-05 | 27/48 (RPMI-7951, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.796×** | -3.9 | 0.010 | 29/47 (SW1417, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.903× | -3.6 | 0.025 | 6/48 (HS-578T, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.863× | -3.5 | 0.030 | 21/48 (SNU-423, LOX-IMVI, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.817×** | -3.5 | 0.033 | 20/48 (SW480, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.817×** | -3.4 | 0.033 | 20/48 (HOP62, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.821×** | -3.4 | 0.040 | 22/48 (BT-474, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.878× | -3.2 | 0.059 | 9/48 (NCI-H460, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -3.2 | 0.062 | 17/50 (LS 180, NCI-H2347, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.835× | -3.1 | 0.085 | 14/48 (RPMI-7951, SNU-423, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12699. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 135 | 7 (5 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 1.93× (z +11.0) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.74× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.645× (z -10.5) |
| [[PANC-1 (line)]] | alt | 228 | 5 | 2 | [[Ixazomib citrate (drug)]] 5 µM 1.94× (z +12.3) | [[Harringtonine (drug)]] 5 µM 0.530× (z -11.5) |
| [[A498 (line)]] | wt | 148 | 4 | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.08× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 221 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 1.99× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.17× (z +9.4) | [[Harringtonine (drug)]] 5 µM 0.541× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 131 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 139 | 2 | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 2.00× (z +10.6) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.631× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 183 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.30× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -14.8) |
| [[RKO (line)]] | wt | 234 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 1.99× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -17.3) |
| [[A549 (line)]] | wt | 111 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 1.96× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 218 | 2 | 1 | [[TAK-901 (drug)]] 0.05 µM 1.92× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.642× (z -9.1) |
| [[LS 180 (line)]] | wt | 165 | 2 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 1.93× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 210 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 1.96× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -12.7) |
| [[SW1417 (line)]] | alt | 242 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -14.3) |
| [[A-172 (line)]] | wt | 159 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.80× (z +9.0) | — |
| [[A-427 (line)]] | wt | 152 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.83× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 173 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.02× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -9.5) |
| [[HT-29 (line)]] | alt | 120 | 1 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 1.82× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -11.8) |
| [[KATO III (line)]] | alt | 226 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -12.6) |
| [[LoVo (line)]] | wt | 122 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 1.72× (z +8.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -16.4) |
| [[RPMI-7951 (line)]] | alt | 180 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.84× (z +8.6) | [[Docetaxel (drug)]] 0.05 µM 0.518× (z -9.3) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 132 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -11.3) |
| [[SW48 (line)]] | wt | 205 | 1 | 1 | [[TAK-901 (drug)]] 0.05 µM 2.11× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -15.5) |
| [[SW480 (line)]] | alt | 292 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.25× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -15.4) |
| [[AsPC-1 (line)]] | alt | 118 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -10.4) |
| [[BT-474 (line)]] | alt | 203 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -14.4) |
| [[C32 (line)]] | wt | 158 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.16× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 139 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -14.3) |
| [[CHP-212 (line)]] | wt | 194 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -12.8) |
| [[COLO 205 (line)]] | alt | 176 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 118 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -9.0) |
| [[Hs 766T (line)]] | wt | 123 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.13× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 170 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.88× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 168 | 1 | 0 | [[Digitoxin (drug)]] 0.5 µM 1.87× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 202 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 229 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -19.0) |
| [[SHP-77 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[AN3 CA (line)]] | alt | 192 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 226 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 127 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 245 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 151 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12699), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP14]] | +0.76 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[NDRG3]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[API5]] | +0.72 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[ANAPC10]] | +0.68 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[GFM2]] | +0.67 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[AGO1]] | +0.67 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[VTI1B]] | +0.67 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[PRDX3]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 541 |
| [[TTC14]] | +0.66 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[MRPL42]] | +0.65 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[UBQLN1]] | +0.65 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[HERC2]] | +0.65 | +0.61 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERF]] | -0.71 | -0.73 / -0.66 | both halves | 7e-06 |  |
| [[TNRC6C]] | -0.68 | -0.71 / -0.66 | both halves | 7e-06 |  |
| [[MAD2L1BP]] | -0.65 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[SIX5]] | -0.65 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[HIVEP1]] | -0.64 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[TOPORS]] | -0.64 | -0.49 / -0.68 | both halves | 1e-05 |  |
| [[POLR1H]] | -0.64 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[UNK]] | -0.63 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[FOXA2]] | -0.63 | -0.47 / -0.72 | both halves | 2e-05 |  |
| [[ZCCHC3]] | -0.62 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[EGLN2]] | -0.62 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[BOLA1]] | -0.62 | -0.56 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA6]] | B | ANXA6 activity raises OPA1's level | lines that do not express ANXA6 (8) vs lines expressing it (42) | 1.20× lower at baseline in the lines without ANXA6 | 0.059 | ⚠ within organs, on part of the lines; also absent: KATNAL1, PHC1, FAM171A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.3, -14.4); signed map (-31.2, -27.1). **Vector** length 115, 36.1% of its response variance represented; |z| ≥ 3 in 1,164 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.1 | +13.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.6 | +9.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.4 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +5.7 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +6.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.1 | +5.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.9 | -15.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.8 | -6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.3 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | +1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | OPA1 mitochondrial dynamin like GTPase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:193,593,144-193,697,811 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NTG, KIAA0567, FLJ12460, NPG, MGM1 |
| Gene groups (HGNC) | Dynamin superfamily |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Regulation of Apoptosis; Mitochondrial protein degradation; Apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [O60313](https://www.uniprot.org/uniprotkb/O60313) (Dynamin-like GTPase OPA1, mitochondrial):

> Dynamin-related GTPase that is essential for normal mitochondrial morphology by mediating fusion of the mitochondrial inner membranes, regulating cristae morphology and maintaining respiratory chain function. Exists in two forms: the transmembrane, long form (Dynamin-like GTPase OPA1, long form; L-OPA1), which is tethered to the inner mitochondrial membrane, and the short soluble form (Dynamin-like GTPase OPA1, short form; S-OPA1), which results from proteolytic cleavage and localizes in the …

**Summary**, from NCBI Gene [4976](https://www.ncbi.nlm.nih.gov/gene/4976):

> The protein encoded by this gene is a nuclear-encoded mitochondrial protein with similarity to dynamin-related GTPases. The encoded protein localizes to the inner mitochondrial membrane and helps regulate mitochondrial stability and energy output. This protein also sequesters cytochrome c. Mutations in this gene have been associated with optic atrophy type 1, which is a dominantly inherited optic neuropathy resulting in progressive loss of visual acuity, leading in many cases to legal …

**Accessions** — [HGNC:8140](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8140) · Entrez [4976](https://www.ncbi.nlm.nih.gov/gene/4976) · UniProt [O60313](https://www.uniprot.org/uniprotkb/O60313) · Ensembl [ENSG00000198836](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198836)

## Data

Gene col 12699: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12699); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12699, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12699]; `tensor/DDL_lfc|DDL_z.npy` [12699]; `embed/gene_vectors.npy` [12699]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12699 or target_col == 12699). Every well: [[OPA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OPA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
