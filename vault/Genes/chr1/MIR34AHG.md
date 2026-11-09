---
symbol: "MIR34AHG"
type: "gene"
col: 13654
ensembl_id: "ENSG00000228526"
name: "MIR34A host gene"
location: "1p36.22"
module: 62
arm: "+"
pooled_cpm: 43.06
n_lines_expressing: 35
n_dd_up: 3
n_dd_down: 23
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# MIR34AHG

*MIR34A host gene* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.48× (z +7.0, q 1e-09, up in 17 of 33 measured lines) ⚠ cell-cycle shift, explains ~67% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.26× (z +4.1, q 0.008, up in 13 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 5 lines (LoVo 4.24×, NCI-H460 2.68×, A498 2.51×, LOX-IMVI 2.78×, …; ⚠ cell-cycle shift, explains ~67% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 3.24×, RKO 6.01×, LS 180 2.83×, SW48 2.68×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 4 lines (LoVo 4.40×, RKO 10.0×, SW48 4.89×, NCI-H460 2.98×; ⚠ cell-cycle shift, explains ~57% of this change); [[Amsacrine (drug)]] 5 µM in 1 line (RKO 4.22×).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.204× (z -19.8, q 0e+00, down in 33 of 33 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FDXR]] (+0.71, fdr 1e-05), [[GRIN2C]] (+0.66, fdr 5e-05), [[DCP1B]] (+0.64, fdr 4e-05); moves opposite to [[SERBP1]] (-0.50, fdr 3e-05), [[RABGAP1L]] (-0.49, fdr 4e-05), [[PPP3CA]] (-0.49, fdr 3e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TP53INP1]] → it (grade B ⚠); 2 go from it, the strongest it → [[PHLDA3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13654.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 5 lines (LoVo 4.24×, NCI-H460 2.68×, A498 2.51×, LOX-IMVI 2.78×, …; ⚠ cell-cycle shift, explains ~67% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 3.24×, RKO 6.01×, LS 180 2.83×, SW48 2.68×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 4 lines (LoVo 4.40×, RKO 10.0×, SW48 4.89×, NCI-H460 2.98×; ⚠ cell-cycle shift, explains ~57% of this change); [[Amsacrine (drug)]] 5 µM in 1 line (RKO 4.22×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.48×** | +7.0 | 1e-09 | 17/33 (LoVo, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.43×** | +4.5 | 0.002 | 19/33 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.008 | 13/34 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.27× | +3.3 | 0.15 | 17/34 (LoVo, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.26 | 10/33 (BT-474, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13654.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.204×** | -19.8 | 0e+00 | 33/33 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.250×** | -17.2 | 0e+00 | 32/33 (A549, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.205×** | -15.9 | 0e+00 | 33/33 (A549, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.407×** | -11.2 | 9e-27 | 31/33 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.540×** | -10.8 | 4e-25 | 28/33 (HOP62, RPMI-7951, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.455×** | -9.4 | 6e-19 | 23/33 (C32, HOP62, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.469×** | -9.0 | 2e-17 | 28/33 (HOP62, COLO 205, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.484×** | -8.6 | 4e-16 | 20/25 (NCI-H2347, HepG2/C3A, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.506×** | -8.4 | 2e-15 | 27/33 (C32, RPMI-7951, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.514×** | -6.7 | 2e-09 | 30/33 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | **0.649×** | -5.3 | 5e-06 | 20/32 (NCI-H2347, RPMI-7951, …) | rises with dose | composition shift |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.654×** | -5.2 | 8e-06 | 21/33 (NCI-H23, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.894× | -4.9 | 4e-05 | 3/34 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.794×** | -4.0 | 0.003 | 21/33 (C32, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.726×** | -3.9 | 0.003 | 17/33 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.728×** | -3.8 | 0.006 | 16/33 (NCI-H1792, C32, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.580×** | -3.5 | 0.014 | 15/34 (A549, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.761×** | -3.4 | 0.022 | 12/34 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.774×** | -3.1 | 0.043 | 12/33 (SW480, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13654. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 184 | 0 | 43 (15 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0485× (z -26.0) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0475× (z -18.5) |
| [[RPMI-7951 (line)]] | alt | 210 | 0 | 18 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0355× (z -23.8) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0482× (z -15.3) |
| [[NCI-H2347 (line)]] | alt | 106 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0427× (z -29.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0996× (z -22.7) |
| [[COLO 205 (line)]] | alt | 84.9 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0738× (z -18.8) |
| [[C32 (line)]] | wt | 117 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -20.4) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0885× (z -19.6) |
| [[LoVo (line)]] | wt | 56.3 | 4 (3 ⚠) | 4 | [[Selinexor (drug)]] 5 µM 4.24× (z +15.4) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.0719× (z -19.7) |
| [[LOX-IMVI (line)]] | wt | 38.5 | 1 (1 ⚠) | 6 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.78× (z +10.3) ⚠ cell-cycle shift, explains ~67% of this change | [[Panobinostat (drug)]] 5 µM 0.0992× (z -16.4) |
| [[A-427 (line)]] | wt | 80.0 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.123× (z -18.1) |
| [[A498 (line)]] | wt | 41.4 | 1 (1 ⚠) | 5 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.51× (z +11.1) ⚠ cell-cycle shift, explains ~67% of this change | [[Panobinostat (drug)]] 5 µM 0.118× (z -18.2) |
| [[LS 180 (line)]] | wt | 74.5 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.0707× (z -16.4) |
| [[NCI-H460 (line)]] | wt | 67.0 | 2 (2 ⚠) | 4 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.68× (z +11.4) ⚠ cell-cycle shift, explains ~67% of this change | [[Panobinostat (drug)]] 5 µM 0.0909× (z -19.6) |
| [[SW48 (line)]] | wt | 94.9 | 2 (1 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 4.89× (z +9.7) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.0690× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0951× (z -14.3) |
| [[A549 (line)]] | wt | 69.2 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0766× (z -21.8) |
| [[HepG2_C3A (line)]] | wt | 162 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0485× (z -23.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.152× (z -15.3) |
| [[hTERT-HPNE (line)]] | wt | 110 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -13.4) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0934× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 29.8 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.134× (z -12.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.283× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 31.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -11.8) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.223× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 84.4 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -17.2) |
| [[RKO (line)]] | wt | 20.1 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.01× (z +11.8) | — |
| [[CFPAC-1 (line)]] | alt | 23.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -15.1) ⚠ cell-cycle shift, explains ~60% of this change |
| [[BT-474 (line)]] | alt | 53.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -10.1) |
| [[J82 (line)]] | alt | 21.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 4.05× (z +8.5) ⚠ cell-cycle shift, explains ~51% of this change | [[Panobinostat (drug)]] 5 µM 0.214× (z -9.5) |
| [[SW480 (line)]] | alt | 17.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -11.1) |
| [[HCT15 (line)]] | alt | 19.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.1000× (z -10.3) |
| [[HT-29 (line)]] | alt | 16.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.189× (z -9.1) |
| [[SW 900 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0635× (z -13.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 3.53 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.06 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.83 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.72 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.67 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.48 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.83 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.00 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.75 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.76 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13654), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FDXR]] | +0.71 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[GRIN2C]] | +0.66 | +0.39 / +0.65 | both halves | 5e-05 |  |
| [[DCP1B]] | +0.64 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[DDB2]] | +0.64 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[MDM2]] | +0.64 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[ZNF79]] | +0.63 | +0.37 / +0.64 | both halves | 7e-05 |  |
| [[POMZP3]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ACTA2]] | +0.62 | +0.31 / +0.66 | both halves | 2e-04 |  |
| [[ANKRA2]] | +0.61 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[PURPL]] | +0.61 | +0.36 / +0.60 | both halves | 9e-05 |  |
| [[PHLDA3]] | +0.60 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[PINCR]] | +0.60 | +0.33 / +0.59 | both halves | 1e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERBP1]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[RABGAP1L]] | -0.49 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[PPP3CA]] | -0.49 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[DIAPH2]] | -0.47 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[SLC38A2]] | -0.45 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[JPH1]] | -0.43 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[DDX10]] | -0.43 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[MTAP]] | -0.43 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[ANKRD28]] | -0.42 | -0.29 / -0.34 | both halves | 3e-04 |  |
| [[EHBP1]] | -0.41 | -0.40 / -0.40 | both halves | 4e-05 |  |
| [[DGKD]] | -0.41 | -0.17 / -0.35 | ⚠ not reproduced | 0.001 |  |
| [[AIG1]] | -0.41 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[XRN2]] | -0.41 | -0.41 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53INP1]] | B | TP53INP1 activity raises MIR34AHG's level | lines that do not express TP53INP1 (7) vs lines expressing it (43) | 3.09× lower at baseline in the lines without TP53INP1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379; maybe low, not absent |
| [[ABCA12]] | B | ABCA12 activity raises MIR34AHG's level | lines that do not express ABCA12 (10) vs lines expressing it (40) | 2.43× lower at baseline in the lines without ABCA12 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000226640, ZPLD1, ANKRD7; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHLDA3]] | B | MIR34AHG activity raises PHLDA3's level | lines that do not express MIR34AHG (15) vs lines expressing it (35) | 1.64× lower at baseline in the lines without MIR34AHG | 0.046 | ⚠ within organs, on part of the lines; also absent: SPATA18, LINC01876 |
| [[TP53INP1]] | B | MIR34AHG activity raises TP53INP1's level | lines that do not express MIR34AHG (15) vs lines expressing it (35) | 1.44× lower at baseline in the lines without MIR34AHG | 0.071 | ⚠ within organs, on part of the lines; also absent: SPATA18, LINC01876 |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.9, 35.9); signed map (41.7, -24.7). **Vector** length 113, 32.2% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *p53 targets up* (control, mean cos +0.54 to 26); *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.51 to 6); *apoptosis* (hallmark, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.8 | -0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +5.5 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.0 | +1.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +4.7 | +7.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.9 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | -1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.6 | +1.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | -3.3 | -9.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.0 | -11.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.7 | -6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.6 | -3.9 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.5 | -5.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -3.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -0.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -0.6 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | MIR34A host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p36.22 — chr1:9,148,011-9,198,906 (-) |
| Ensembl biotype | lncRNA |
| Also known as | lnc34a |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [106614088](https://www.ncbi.nlm.nih.gov/gene/106614088):

> Predicted to be involved in miRNA-mediated post-transcriptional gene silencing. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:51913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51913) · Entrez [106614088](https://www.ncbi.nlm.nih.gov/gene/106614088) · Ensembl [ENSG00000228526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228526)

## Data

Gene col 13654: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13654); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13654, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13654]; `tensor/DDL_lfc|DDL_z.npy` [13654]; `embed/gene_vectors.npy` [13654]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13654 or target_col == 13654). Every well: [[MIR34AHG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR34AHG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
