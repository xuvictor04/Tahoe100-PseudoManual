---
symbol: "MTURN"
type: "gene"
col: 11101
ensembl_id: "ENSG00000180354"
name: "maturin, neural progenitor differentiation regulator homolog"
location: "7p14.3"
module: 69
arm: "+"
pooled_cpm: 21.89
n_lines_expressing: 48
n_dd_up: 23
n_dd_down: 29
n_dd_up_clean: 14
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# MTURN

*maturin, neural progenitor differentiation regulator homolog* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.55× (z +9.7, q 2e-19, up in 32 of 46 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.41× (z +7.6, q 4e-12, up in 24 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.259× (z -21.1, q 0e+00, down in 46 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.258× (z -11.1, q 5e-26, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HECA]] (+0.68, fdr 7e-06), [[WDTC1]] (+0.62, fdr 1e-05), [[KLHL24]] (+0.61, fdr 1e-05); moves opposite to [[TAF2]] (-0.51, fdr 1e-05), [[THADA]] (-0.48, fdr 3e-05), [[INTS7]] (-0.46, fdr 6e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GAS6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11101.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.55×** | +9.7 | 2e-19 | 32/46 (PANC-1, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.64×** | +7.7 | 3e-12 | 32/46 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +7.6 | 4e-12 | 24/45 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.59×** | +7.3 | 5e-11 | 39/46 (PANC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.45×** | +5.8 | 9e-07 | 30/46 (SW1417, C-33 A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +5.3 | 1e-05 | 24/44 (PANC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.43×** | +5.1 | 2e-05 | 23/46 (NCI-H460, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +5.1 | 2e-05 | 21/46 (RPMI-7951, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +4.6 | 3e-04 | 20/46 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +4.3 | 9e-04 | 16/35 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.002 | 15/46 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.29×** | +4.0 | 0.003 | 13/46 (A498, SNU-423, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.29×** | +3.9 | 0.004 | 18/44 (HS-578T, RPMI-7951, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.19× | +3.9 | 0.004 | 17/46 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.28×** | +3.7 | 0.007 | 14/45 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.030 | 11/46 (J82, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.034 | 15/45 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.062 | 9/46 (A498, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.1 | 0.062 | 10/46 (HT-29, hTERT-HPNE, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +3.0 | 0.067 | 8/46 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.067 | 14/45 (J82, NCI-H460, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.073 | 14/44 (PANC-1, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11101.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.259×** | -21.1 | 0e+00 | 46/46 (SW1417, SW480, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.258×** | -11.1 | 5e-26 | 37/45 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.269×** | -10.7 | 1e-24 | 41/46 (Hs 766T, HCT15, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.297×** | -9.9 | 5e-21 | 39/44 (MIA PaCa-2, SW48, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.330×** | -9.1 | 2e-17 | 38/44 (hTERT-HPNE, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.362×** | -8.3 | 1e-14 | 34/46 (Hs 766T, SW 900, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.584×** | -7.9 | 2e-13 | 31/46 (SW48, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.612×** | -7.7 | 1e-12 | 31/46 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.394×** | -7.6 | 2e-12 | 29/42 (NCI-H1792, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.405×** | -7.4 | 9e-12 | 34/42 (AsPC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.629×** | -7.3 | 2e-11 | 26/45 (SNU-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.458×** | -6.4 | 8e-09 | 27/45 (KATO III, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.500×** | -6.2 | 2e-08 | 26/46 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.690×** | -5.8 | 3e-07 | 22/45 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.739×** | -4.5 | 3e-04 | 20/46 (A-172, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.622×** | -4.3 | 6e-04 | 16/46 (A498, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11101. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 29.7 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.147× (z -13.4) ⚠ unreliable plate only · without an alert: [[Belzutifan (drug)]] 5 µM 0.0272× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 32.4 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.153× (z -13.7) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -10.1) |
| [[SW480 (line)]] | alt | 22.8 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.198× (z -14.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.313× (z -10.2) |
| [[PANC-1 (line)]] | alt | 9.43 | 1 (1 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.87× (z +12.7) ⚠ cell-cycle shift, explains ~39% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.215× (z -10.3) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -9.4) |
| [[A-172 (line)]] | wt | 37.5 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.178× (z -12.1) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 22.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.44× (z +8.7) ⚠ cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -14.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 28.6 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.242× (z -11.5) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.126× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 14.3 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0985× (z -12.8) ⚠ cell-cycle shift, explains ~77% of this change |
| [[NCI-H23 (line)]] | alt | 24.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -18.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 31.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -11.4) |
| [[SW1417 (line)]] | alt | 30.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.04× (z +8.5) ⚠ cell-cycle shift, explains ~39% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.178× (z -14.5) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.173× (z -9.7) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 9.55 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0803× (z -10.6) |
| [[H4 (line)]] | wt | 29.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.183× (z -8.6) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 22.4 | 0 | 1 | — | [[Abemaciclib (drug)]] 5 µM 0.0360× (z -9.3) |
| [[Hs 766T (line)]] | wt | 35.4 | 0 | 1 | — | [[Abemaciclib (drug)]] 5 µM 0.0333× (z -11.4) |
| [[HS-578T (line)]] | alt | 23.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.237× (z -9.2) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.179× (z -11.5) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 30.1 | 0 | 1 | — | [[c-Kit-IN-1 (drug)]] 5 µM 0.0210× (z -12.1) |
| [[KATO III (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.235× (z -10.2) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.211× (z -10.7) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.310× (z -8.7) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 40.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.197× (z -9.4) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 49.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.145× (z -12.7) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.85 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11101), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HECA]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[WDTC1]] | +0.62 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[KLHL24]] | +0.61 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[VAT1]] | +0.60 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ZBTB10]] | +0.58 | +0.39 / +0.64 | both halves | 6e-05 |  |
| [[ZDHHC2]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[CREBRF]] | +0.57 | +0.39 / +0.66 | both halves | 5e-05 |  |
| [[GARRE1]] | +0.57 | +0.37 / +0.66 | both halves | 8e-05 |  |
| [[ELF2]] | +0.56 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[EZH1]] | +0.56 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[FBXO25]] | +0.56 | +0.43 / +0.71 | both halves | 3e-05 |  |
| [[PIK3CA]] | +0.56 | +0.61 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF2]] | -0.51 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[THADA]] | -0.48 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[INTS7]] | -0.46 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[THUMPD3]] | -0.46 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[MED1]] | -0.46 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[PSMD1]] | -0.45 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[FADD]] | -0.45 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[ZNF41]] | -0.45 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[PRH1]] | -0.45 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[FTSJ3]] | -0.44 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[EVA1A-AS]] | -0.44 | -0.30 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAS6]] | B | GAS6 activity raises MTURN's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without GAS6 | 0.093 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.8, -45.5); signed map (-16.9, 10.3). **Vector** length 118, 31.1% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +7.9 | +9.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +6.4 | +7.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.2 | +5.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.1 | +7.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.4 | +3.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +5.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.9 | +1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.2 | -21.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.6 | -9.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.8 | -10.7 |
|  | [[EX229 (drug)]] 5 µM |  | -6.7 | -11.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.2 | -9.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | -5.0 | -7.4 |

## What is on record

|  |  |
|---|---|
| Name | maturin, neural progenitor differentiation regulator homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:30,134,986-30,162,762 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25903, Ells1; previously C7orf41 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3F0](https://www.uniprot.org/uniprotkb/Q8N3F0) (Maturin):

> Promotes megakaryocyte differentiation by enhancing ERK and JNK signaling as well as up-regulating RUNX1 and FLI1 expression. Represses NF-kappa-B transcriptional activity by inhibiting phosphorylation of RELA at 'Ser-536'. May be involved in early neuronal development (By similarity).

**Summary**, from NCBI Gene [222166](https://www.ncbi.nlm.nih.gov/gene/222166):

> Involved in positive regulation of ERK1 and ERK2 cascade; positive regulation of JNK cascade; and positive regulation of megakaryocyte differentiation. Located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25457](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25457) · Entrez [222166](https://www.ncbi.nlm.nih.gov/gene/222166) · UniProt [Q8N3F0](https://www.uniprot.org/uniprotkb/Q8N3F0) · Ensembl [ENSG00000180354](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180354)

## Data

Gene col 11101: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11101); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11101, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11101]; `tensor/DDL_lfc|DDL_z.npy` [11101]; `embed/gene_vectors.npy` [11101]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11101 or target_col == 11101). Every well: [[MTURN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTURN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
