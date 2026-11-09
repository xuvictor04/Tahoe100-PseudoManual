---
symbol: "RAC1"
type: "gene"
col: 5839
ensembl_id: "ENSG00000136238"
name: "Rac family small GTPase 1"
location: "7p22.1"
module: 111
arm: "+"
pooled_cpm: 160.13
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# RAC1

*Rac family small GTPase 1* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.71× (z +10.0, q 1e-20, up in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.89× (z +6.3, q 2e-08, up in 42 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.786× (z -6.5, q 6e-08, down in 29 of 49 measured lines) ⚠ cell-cycle shift, explains ~20% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (Hs 766T 0.525×, HT-29 0.579×, AsPC-1 0.584×, NCI-H1792 0.601×; ⚠ cell-cycle shift, explains ~20% of this change); [[Homoharringtonine (drug)]] 5 µM in 4 lines (KATO III 0.593×, MIA PaCa-2 0.547×, NCI-H2030 0.505×, AN3 CA 0.434×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (AsPC-1 0.454×, PANC-1 0.531×, Hs 766T 0.513×; ⚠ cell-cycle shift, explains ~21% of this change); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (NCI-H23 0.498×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAST]] (+0.59, fdr 1e-05), [[DIAPH1]] (+0.58, fdr 2e-05), [[ABI1]] (+0.55, fdr 1e-05); moves opposite to [[CNPY2]] (-0.52, fdr 6e-05), [[COQ9]] (-0.51, fdr 3e-05), [[TM9SF1]] (-0.49, fdr 4e-04).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FGD6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5839.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +10.0 | 1e-20 | 42/49 (C-33 A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +8.5 | 8e-15 | 41/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +8.2 | 5e-14 | 33/44 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.49×** | +7.5 | 8e-12 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +6.9 | 4e-10 | 41/47 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +6.7 | 2e-09 | 35/45 (SNU-423, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +6.6 | 3e-09 | 0/50 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.89×** | +6.3 | 2e-08 | 42/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +5.2 | 1e-05 | 31/38 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +4.9 | 5e-05 | 25/49 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +4.4 | 5e-04 | 26/48 (A-427, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 8e-04 | 26/48 (LS 180, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.25×** | +4.2 | 0.001 | 28/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.003 | 27/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.23×** | +3.9 | 0.003 | 22/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.007 | 25/47 (HT-29, LS 180, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.009 | 22/48 (A-427, C32, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.017 | 20/48 (SW480, HS-578T, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.044 | 20/48 (HT-29, SW480, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.044 | 23/48 (SW480, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.34×** | +2.9 | 0.087 | 17/46 (LS 180, LoVo, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 8 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5839.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (Hs 766T 0.525×, HT-29 0.579×, AsPC-1 0.584×, NCI-H1792 0.601×; ⚠ cell-cycle shift, explains ~20% of this change); [[Homoharringtonine (drug)]] 5 µM in 4 lines (KATO III 0.593×, MIA PaCa-2 0.547×, NCI-H2030 0.505×, AN3 CA 0.434×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (AsPC-1 0.454×, PANC-1 0.531×, Hs 766T 0.513×; ⚠ cell-cycle shift, explains ~21% of this change); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (NCI-H23 0.498×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.786×** | -6.5 | 6e-08 | 29/49 (Hs 766T, HT-29, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | 0.841× | -4.6 | 1e-03 | 22/48 (H4, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.794×** | -4.4 | 0.002 | 26/48 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.830×** | -3.5 | 0.057 | 24/48 (AsPC-1, Hs 766T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.828×** | -3.4 | 0.067 | 22/48 (NCI-H23, Hs 766T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.850× | -3.1 | 0.19 | 16/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 0.849× | -3.0 | 0.19 | 18/48 (CFPAC-1, LOX-IMVI, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.854× | -3.0 | 0.19 | 22/48 (AsPC-1, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5839. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 91.1 | 7 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.20× (z +14.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 422 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.441× (z -11.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 212 | 4 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +11.2) ⚠ cell-cycle shift, explains ~34% of this change | [[Panobinostat (drug)]] 5 µM 0.531× (z -8.9) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SW480 (line)]] | alt | 129 | 5 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.21× (z +12.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 158 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.16× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 132 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +15.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.16× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 133 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.265× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 102 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +10.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 243 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -12.2) ⚠ cell-cycle shift, explains ~20% of this change |
| [[KATO III (line)]] | alt | 229 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.85× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.593× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 148 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.38× (z +11.5) ⚠ toxic | — |
| [[LS 180 (line)]] | wt | 114 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +10.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H23 (line)]] | alt | 194 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.30× (z +10.5) ⚠ toxic; transcription drop | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.498× (z -8.8) |
| [[C-33 A (line)]] | alt | 85.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +10.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 78.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.77× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 178 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -10.8) ⚠ cell-cycle shift, explains ~20% of this change |
| [[hTERT-HPNE (line)]] | wt | 109 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +8.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 151 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 124 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.44× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 212 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -8.7) ⚠ cell-cycle shift, explains ~20% of this change |
| [[NCI-H2030 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +9.1) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 136 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.31× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 145 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.45× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 202 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 243 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 85.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 193 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 113 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 137 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 132 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 91.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 165 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5839), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAST]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[DIAPH1]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 | pathway: RHO GTPase Effectors; STRING 480 |
| [[ABI1]] | +0.55 | +0.55 / +0.59 | both halves | 1e-05 | pathway: FCGR3A-mediated phagocytosis; STRING 774 |
| [[TMOD3]] | +0.54 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[RAP1GAP2]] | +0.53 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[RHOA]] | +0.52 | +0.55 / +0.48 | both halves | 2e-05 | same gene group; pathway: Beta-catenin independent WNT signaling; STRING 770 |
| [[CDC42BPB]] | +0.52 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[TMOD2]] | +0.51 | +0.38 / +0.30 | both halves | 2e-04 |  |
| [[AFDN]] | +0.51 | +0.42 / +0.52 | both halves | 4e-05 | pathway: Adherens junctions interactions |
| [[ATP2B4]] | +0.51 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[YPEL2]] | +0.51 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[PRKCI]] | +0.51 | +0.45 / +0.42 | both halves | 4e-05 | pathway: Cell junction organization; STRING 511 |

## Genes that move opposite

*25 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNPY2]] | -0.52 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[COQ9]] | -0.51 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[TM9SF1]] | -0.49 | -0.26 / -0.38 | both halves | 4e-04 |  |
| [[TM9SF4]] | -0.48 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[RPAP1]] | -0.47 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[LRRC41]] | -0.47 | -0.18 / -0.34 | ⚠ not reproduced | 9e-04 |  |
| [[FBXW9]] | -0.47 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[ZNF785]] | -0.47 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[AKAP8]] | -0.46 | -0.16 / -0.44 | ⚠ not reproduced | 0.001 |  |
| [[TMEM101]] | -0.46 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[MTRFR]] | -0.46 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[CDK12]] | -0.46 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[B9D1]] | -0.45 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[FASTKD2]] | -0.45 | -0.32 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGD6]] | B | FGD6 activity raises RAC1's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 1.33× lower at baseline in the lines without FGD6 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[RPP25]] | B | RPP25 activity raises RAC1's level | lines that do not express RPP25 (14) vs lines expressing it (36) | 1.31× lower at baseline in the lines without RPP25 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, ODF3B, EPHA10 |
| [[HDAC6]] | B | HDAC6 activity raises RAC1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[IRF6]] | B | IRF6 activity weakens RAC1's drug response | lines that do not express IRF6 (31) vs lines expressing it (19) | the lines without IRF6 respond 1.15× as strongly (z diff -0.58); strongest at Dinaciclib 5 µM: 1.75x vs 1.20x (z diff -3.5) | 0.065 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.579). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.1, 26.9); signed map (-10.4, 36.7). **Vector** length 83.7, 23.7% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +10.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +4.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.4 | -3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.2 | -1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.1 | -0.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.3 | -1.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.1 | -1.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | Rac family small GTPase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:6,374,527-6,403,967 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TC-25, p21-Rac1, Rac-1 |
| Gene groups (HGNC) | Rho family GTPases; Receptor ligands |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, COAGULATION |
| Reactome | 108 pathways, smallest: NTRK2 activates RAC1; Activated NTRK2 signals through CDK5; Activated NTRK2 signals through FYN |
| Matched by | ensembl_id |

**Function**, from UniProt [P63000](https://www.uniprot.org/uniprotkb/P63000) (Ras-related C3 botulinum toxin substrate 1):

> Plasma membrane-associated small GTPase which cycles between active GTP-bound and inactive GDP-bound states. In its active state, binds to a variety of effector proteins to regulate cellular responses such as secretory processes, phagocytosis of apoptotic cells, epithelial cell polarization, neurons adhesion, migration and differentiation, and growth-factor induced formation of membrane ruffles. Rac1 p21/rho GDI heterodimer is the active component of the cytosolic factor sigma 1, which is …

**Summary**, from NCBI Gene [5879](https://www.ncbi.nlm.nih.gov/gene/5879):

> The protein encoded by this gene is a GTPase which belongs to the RAS superfamily of small GTP-binding proteins. Members of this superfamily appear to regulate a diverse array of cellular events, including the control of cell growth, cytoskeletal reorganization, and the activation of protein kinases. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:9801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9801) · Entrez [5879](https://www.ncbi.nlm.nih.gov/gene/5879) · UniProt [P63000](https://www.uniprot.org/uniprotkb/P63000) · Ensembl [ENSG00000136238](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136238)

## Data

Gene col 5839: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5839); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5839, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5839]; `tensor/DDL_lfc|DDL_z.npy` [5839]; `embed/gene_vectors.npy` [5839]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5839 or target_col == 5839). Every well: [[RAC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
