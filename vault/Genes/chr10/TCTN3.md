---
symbol: "TCTN3"
type: "gene"
col: 4146
ensembl_id: "ENSG00000119977"
name: "tectonic family member 3"
location: "10q24.1"
module: 15
arm: "+"
pooled_cpm: 27.48
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 10
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# TCTN3

*tectonic family member 3* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.26× (z +19.4, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.702× (z -8.4, q 2e-14, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP133]] (+0.65, fdr 7e-06), [[NUDT2]] (+0.63, fdr 1e-05), [[CEP43]] (+0.63, fdr 1e-05); moves opposite to [[ALAS1]] (-0.59, fdr 1e-05), [[NPL]] (-0.58, fdr 5e-05), [[SSUH2]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SRCIN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4146.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.26×** | +19.4 | 0e+00 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +18.9 | 0e+00 | 40/48 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.00×** | +16.5 | 0e+00 | 44/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.12×** | +14.5 | 1e-45 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.49×** | +9.1 | 1e-17 | 28/46 (NCI-H2030, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.43×** | +8.1 | 4e-14 | 29/46 (SW480, NCI-H460, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.38×** | +7.4 | 2e-11 | 26/48 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +7.2 | 6e-11 | 28/48 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.23×** | +7.0 | 1e-10 | 24/48 (SNU-423, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +5.1 | 2e-05 | 23/47 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +5.0 | 2e-05 | 17/48 (SNU-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +5.0 | 3e-05 | 14/48 (PANC-1, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.20× | +4.3 | 7e-04 | 15/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.19× | +4.2 | 0.001 | 9/48 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.22×** | +3.9 | 0.004 | 10/48 (SNU-1, C-33 A, …) | two highest doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.004 | 8/46 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +3.9 | 0.004 | 11/47 (SHP-77, NCI-H1573, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.005 | 9/48 (NCI-H1573, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.042 | 6/48 (LoVo, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.050 | 4/48 (SW480, LoVo, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4146.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.702×** | -8.4 | 2e-14 | 28/48 (LoVo, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.735×** | -7.0 | 7e-10 | 26/48 (AN3 CA, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.769×** | -6.2 | 8e-08 | 21/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.780×** | -5.9 | 5e-07 | 24/48 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.625×** | -5.8 | 6e-07 | 21/46 (NCI-H2347, SW480, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.635×** | -5.6 | 2e-06 | 16/48 (SW480, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.861× | -5.0 | 4e-05 | 20/48 (HOP62, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.817×** | -4.8 | 1e-04 | 11/47 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.822×** | -4.6 | 2e-04 | 17/47 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.699×** | -4.4 | 5e-04 | 13/47 (LOX-IMVI, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.803×** | -4.2 | 0.001 | 16/48 (NCI-H460, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 0.881× | -4.2 | 0.001 | 18/48 (HOP62, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.851× | -3.8 | 0.006 | 17/48 (SW1417, C32, …) | all doses, stronger at high dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.899× | -3.6 | 0.015 | 10/48 (PANC-1, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.861× | -3.5 | 0.015 | 10/48 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Cyclosporin A (drug)]] 5 µM |  | 0.866× | -3.4 | 0.021 | 4/48 (KATO III, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4146. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 39.6 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +12.4) | [[Harringtonine (drug)]] 5 µM 0.502× (z -8.6) |
| [[HOP62 (line)]] | alt | 39.4 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -12.9) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.391× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 17.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.48× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 24.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.99× (z +9.1) | — |
| [[LoVo (line)]] | wt | 34.3 | 1 | 1 | [[Cobimetinib (drug)]] 5 µM 2.52× (z +9.4) | [[Auranofin (drug)]] 5 µM 0.435× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 27.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 21.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 37.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -8.7) ⚠ cell-cycle shift, explains ~67% of this change |
| [[SW480 (line)]] | alt | 26.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.60× (z +10.8) | — |
| [[A-172 (line)]] | wt | 21.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +8.5) | — |
| [[A498 (line)]] | wt | 29.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -8.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[A549 (line)]] | wt | 20.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 58.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.124× (z -10.6) |
| [[C-33 A (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 30.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 20.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.70× (z +8.5) | — |
| [[KATO III (line)]] | alt | 23.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.91× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 22.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 23.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.24× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 16.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 13.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.11× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 28.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.24× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 25.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -10.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[A-427 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4146), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP133]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[NUDT2]] | +0.63 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CEP43]] | +0.63 | +0.61 / +0.54 | both halves | 1e-05 | pathway: Anchoring of the basal body to the plasma membrane |
| [[ARMC10]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[CDADC1]] | +0.62 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[EEF1AKMT2]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[DGCR2]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[CA5B]] | +0.59 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[SMARCD2]] | +0.58 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[MLEC]] | +0.57 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[TAF11]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[TMEM231]] | +0.57 | +0.37 / +0.67 | both halves | 9e-05 | STRING 880 |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALAS1]] | -0.59 | -0.66 / -0.56 | both halves | 1e-05 | pathway: Organelle biogenesis and maintenance |
| [[NPL]] | -0.58 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[SSUH2]] | -0.58 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[MTNR1A]] | -0.57 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[GLRX2]] | -0.56 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[NCF2]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[SCUBE2]] | -0.55 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[LINC02901]] | -0.54 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[LINC00243]] | -0.54 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[LINC01933]] | -0.54 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[PHEX]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[CCDC136]] | -0.53 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRCIN1]] | B | SRCIN1 activity raises TCTN3's level | lines that do not express SRCIN1 (9) vs lines expressing it (41) | 1.29× lower at baseline in the lines without SRCIN1 | 0.094 | ⚠ within organs, on part of the lines; also absent: TSPAN33, PRKN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.382). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.4, 23.6); signed map (-40.6, -22.4). **Vector** length 85.8, 17.9% of its response variance represented; |z| ≥ 3 in 990 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +18.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.3 | +5.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +4.2 | +3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.5 | +1.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.5 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.9 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.7 | -8.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.6 | -7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -6.3 | -5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -6.3 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.0 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | tectonic family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:95,659,823-95,694,143 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564D116, TECT3, JBTS18; previously C10orf61 |
| Gene groups (HGNC) | Tectonic proteins |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NUS6](https://www.uniprot.org/uniprotkb/Q6NUS6) (Tectonic-3):

> Part of the tectonic-like complex which is required for tissue-specific ciliogenesis and may regulate ciliary membrane composition (By similarity). May be involved in apoptosis regulation. Necessary for signal transduction through the sonic hedgehog (Shh) signaling pathway.

**Summary**, from NCBI Gene [26123](https://www.ncbi.nlm.nih.gov/gene/26123):

> This gene encodes a member of the tectonic gene family which functions in Hedgehog signal transduction and development of the neural tube. Mutations in this gene have been associated with Orofaciodigital Syndrome IV and Joubert Syndrom 18. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Sep 2012]

**Accessions** — [HGNC:24519](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24519) · Entrez [26123](https://www.ncbi.nlm.nih.gov/gene/26123) · UniProt [Q6NUS6](https://www.uniprot.org/uniprotkb/Q6NUS6) · Ensembl [ENSG00000119977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119977)

## Data

Gene col 4146: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4146); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4146, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4146]; `tensor/DDL_lfc|DDL_z.npy` [4146]; `embed/gene_vectors.npy` [4146]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4146 or target_col == 4146). Every well: [[TCTN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCTN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
