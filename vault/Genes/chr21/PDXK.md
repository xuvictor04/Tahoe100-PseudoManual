---
symbol: "PDXK"
type: "gene"
col: 8319
ensembl_id: "ENSG00000160209"
name: "pyridoxal kinase"
location: "21q22.3"
module: 16
arm: "-"
pooled_cpm: 130.03
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# PDXK

*pyridoxal kinase* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.29× (z +6.0, q 6e-07, up in 28 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.28× (z +6.0, q 6e-07, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.620× (z -16.1, q 0e+00, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM4B]] (+0.60, fdr 8e-06), [[PIK3C2A]] (+0.58, fdr 1e-05), [[RAB6A]] (+0.57, fdr 1e-05); moves opposite to [[DDX20]] (-0.63, fdr 7e-06), [[MTMR2]] (-0.61, fdr 1e-05), [[AASDHPPT]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NDRG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8319.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +6.0 | 6e-07 | 28/48 (SW480, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +6.0 | 6e-07 | 26/48 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +4.8 | 3e-04 | 23/48 (LOX-IMVI, A498, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 0.001 | 26/48 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.038 | 18/48 (NCI-H1792, SNU-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.17 | 12/47 (AsPC-1, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.09× | +3.1 | 0.17 | 10/49 (HS-578T, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.0 | 0.18 | 19/48 (SW480, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8319.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.620×** | -16.1 | 0e+00 | 38/48 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.550×** | -13.7 | 2e-40 | 40/48 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.641×** | -10.6 | 5e-24 | 35/48 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.762×** | -9.2 | 6e-18 | 32/48 (SW48, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.734×** | -7.4 | 2e-11 | 34/48 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **0.767×** | -6.1 | 1e-07 | 27/47 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.837× | -6.0 | 2e-07 | 22/48 (Hs 766T, SNU-423, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.647×** | -5.4 | 4e-06 | 31/48 (LS 180, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.818×** | -4.8 | 1e-04 | 26/48 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.698×** | -4.5 | 4e-04 | 24/49 (LS 180, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.831×** | -4.4 | 5e-04 | 22/48 (LS 180, SW48, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.845× | -4.0 | 0.003 | 21/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.725×** | -4.0 | 0.003 | 17/38 (NCI-H1573, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.841× | -3.9 | 0.004 | 19/47 (SW48, LS 180, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | 0.834× | -3.8 | 0.005 | 21/45 (SHP-77, LoVo, …) | inconsistent across doses | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | 0.850× | -3.7 | 0.007 | 20/48 (LoVo, J82, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.743×** | -3.7 | 0.007 | 18/49 (NCI-H1573, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.869× | -3.3 | 0.025 | 13/48 (CFPAC-1, KATO III, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.869× | -3.2 | 0.040 | 17/48 (A-172, A498, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.873× | -3.1 | 0.054 | 12/48 (HEC-1-A, C-33 A, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8319. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 218 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.467× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 202 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -29.7) |
| [[SW48 (line)]] | wt | 211 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.477× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 231 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.458× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 198 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -20.3) |
| [[MIA PaCa-2 (line)]] | alt | 178 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.353× (z -13.6) |
| [[A-427 (line)]] | wt | 58.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -25.2) |
| [[A498 (line)]] | wt | 216 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.573× (z -9.4) |
| [[KATO III (line)]] | alt | 138 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -13.5) |
| [[RKO (line)]] | wt | 89.3 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.263× (z -14.2) |
| [[SW1417 (line)]] | alt | 133 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -17.6) |
| [[A549 (line)]] | wt | 91.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 117 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -11.9) |
| [[C-33 A (line)]] | alt | 75.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -15.3) |
| [[Hs 766T (line)]] | wt | 140 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -10.5) |
| [[HT-29 (line)]] | alt | 135 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -18.5) |
| [[LoVo (line)]] | wt | 160 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.420× (z -12.1) |
| [[SW480 (line)]] | alt | 109 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.18× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 71.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.46× (z +8.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 92.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -10.2) |
| [[CHP-212 (line)]] | wt | 65.2 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.255× (z -10.1) |
| [[HCT15 (line)]] | alt | 242 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.431× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 159 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 138 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -11.4) |
| [[J82 (line)]] | alt | 78.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.608× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 148 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -22.0) |
| [[NCI-H1792 (line)]] | alt | 91.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.464× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 89.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -19.2) |
| [[NCI-H460 (line)]] | wt | 60.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.3) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H661 (line)]] | alt | 47.5 | 0 | 1 | — | [[Futibatinib (drug)]] 0.05 µM 0.0442× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 109 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.501× (z -8.5) |
| [[PANC-1 (line)]] | alt | 82.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -14.6) |
| [[SK-MEL-2 (line)]] | alt | 80.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -11.8) |
| [[SNU-1 (line)]] | wt | 79.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.326× (z -8.9) |
| [[A-172 (line)]] | wt | 263 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 173 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 134 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 149 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 81.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8319), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM4B]] | +0.60 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[PIK3C2A]] | +0.58 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[RAB6A]] | +0.57 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SLC31A1]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[RAB40C]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SLC17A5]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[P4HA1]] | +0.56 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[PRKRIP1]] | +0.56 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[RAB11FIP5]] | +0.56 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[MKNK2]] | +0.55 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[GSDMB]] | +0.55 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ARFGAP3]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX20]] | -0.63 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[MTMR2]] | -0.61 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[AASDHPPT]] | -0.60 | -0.62 / -0.53 | both halves | 1e-05 | pathway: Metabolism of vitamins and cofactors |
| [[SMARCE1]] | -0.59 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.58 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[ZNF260]] | -0.57 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[CEP41]] | -0.56 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[SENP1]] | -0.56 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[FZD6]] | -0.56 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[TRMT5]] | -0.55 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[ZNF624]] | -0.55 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[C7orf25]] | -0.55 | -0.56 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDRG1]] | B | NDRG1 activity raises PDXK's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.91× lower at baseline in the lines without NDRG1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[KCNK6]] | B | KCNK6 activity raises PDXK's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.62× lower at baseline in the lines without KCNK6 | 0.060 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.569). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-26.6, -13.7); signed map (-43.4, 14.4). **Vector** length 125, 35.9% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.4 | +4.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.5 | -4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +5.0 | +4.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +6.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.6 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +2.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.7 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.4 | -13.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.3 | -9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -10.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | -4.6 | -6.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.2 | -3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.7 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -3.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | pyridoxal kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:43,719,094-43,762,307 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PNK, PKH, FLJ21324, PRED79, FLJ31940, MGC15873; previously C21orf97, C21orf124 |
| Gene groups (HGNC) | Vitamin/cofactor kinases |
| Reactome | 5 pathways, smallest: Vitamin B6 activation to pyridoxal phosphate; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [O00764](https://www.uniprot.org/uniprotkb/O00764) (Pyridoxal kinase):

> Catalyzes the phosphorylation of the dietary vitamin B6 vitamers pyridoxal (PL), pyridoxine (PN) and pyridoxamine (PM) to form pyridoxal 5'-phosphate (PLP), pyridoxine 5'-phosphate (PNP) and pyridoxamine 5'-phosphate (PMP), respectively (Probable). PLP is the active form of vitamin B6, and acts as a cofactor for over 140 different enzymatic reactions.

**Summary**, from NCBI Gene [8566](https://www.ncbi.nlm.nih.gov/gene/8566):

> The protein encoded by this gene phosphorylates vitamin B6, a step required for the conversion of vitamin B6 to pyridoxal-5-phosphate, an important cofactor in intermediary metabolism. The encoded protein is cytoplasmic and probably acts as a homodimer. Alternatively spliced transcript variants have been described, but their biological validity has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8819](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8819) · Entrez [8566](https://www.ncbi.nlm.nih.gov/gene/8566) · UniProt [O00764](https://www.uniprot.org/uniprotkb/O00764) · Ensembl [ENSG00000160209](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160209)

## Data

Gene col 8319: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8319); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8319, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8319]; `tensor/DDL_lfc|DDL_z.npy` [8319]; `embed/gene_vectors.npy` [8319]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8319 or target_col == 8319). Every well: [[PDXK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDXK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
