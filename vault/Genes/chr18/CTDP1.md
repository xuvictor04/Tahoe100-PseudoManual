---
symbol: "CTDP1"
type: "gene"
col: 682
ensembl_id: "ENSG00000060069"
name: "CTD phosphatase 1"
location: "18q23"
module: 105
arm: "+"
pooled_cpm: 35.22
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# CTDP1

*CTD phosphatase 1* — 18q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.40× (z +10.4, q 9e-23, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.351× (z -11.3, q 6e-27, down in 44 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.730× (z -4.9, q 2e-04, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMM10B]] (+0.68, fdr 7e-06), [[LONP1]] (+0.67, fdr 7e-06), [[BMT2]] (+0.67, fdr 7e-06); moves opposite to [[AGL]] (-0.59, fdr 9e-06), [[ZNF518A]] (-0.58, fdr 1e-05), [[FAM200B]] (-0.57, fdr 2e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NRIP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 682.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.40×** | +10.4 | 9e-23 | 47/48 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.58×** | +10.2 | 8e-22 | 43/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.34×** | +9.1 | 2e-17 | 46/47 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.22×** | +8.6 | 1e-15 | 43/47 (MIA PaCa-2, HEC-1-A, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.10×** | +7.9 | 2e-13 | 40/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.09×** | +7.9 | 3e-13 | 41/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.16×** | +7.8 | 5e-13 | 44/48 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.42×** | +6.9 | 4e-10 | 38/47 (LS 180, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.89×** | +6.8 | 7e-10 | 39/48 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +6.4 | 1e-08 | 27/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.49×** | +5.1 | 2e-05 | 39/47 (SHP-77, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.19×** | +4.4 | 5e-04 | 28/43 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.87×** | +4.3 | 8e-04 | 30/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.31×** | +4.1 | 0.002 | 25/48 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.42×** | +3.8 | 0.006 | 23/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.42×** | +3.7 | 0.007 | 21/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.079 | 19/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 682.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.351×** | -11.3 | 6e-27 | 44/45 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.381×** | -10.1 | 2e-21 | 36/40 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.512×** | -6.7 | 3e-09 | 32/43 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.730×** | -4.9 | 2e-04 | 29/48 (HS-578T, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.766×** | -4.1 | 0.004 | 28/48 (C32, SK-MEL-2, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.690×** | -3.9 | 0.009 | 30/48 (C32, NCI-H460, …) | top dose only | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.779×** | -3.9 | 0.009 | 25/48 (NCI-H2347, A498, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.746×** | -3.2 | 0.096 | 19/47 (hTERT-HPNE, HT-29, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.759× | -3.0 | 0.14 | 19/48 (Panc 03.27, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.760× | -3.0 | 0.14 | 15/48 (NCI-H460, SW48, …) | inconsistent across doses | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.760× | -3.0 | 0.14 | 18/48 (LOX-IMVI, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 682. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.8 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.41× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -11.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 56.6 | 6 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.14× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -9.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 15.9 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.48× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 24.4 | 3 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.79× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0864× (z -18.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 39.3 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.66× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -10.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 63.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -13.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 15.5 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.16× (z +12.2) | — |
| [[LoVo (line)]] | wt | 34.3 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.14× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -11.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 46.1 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.66× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.135× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 51.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.34× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.224× (z -10.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 24.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +8.6) ⚠ cell-cycle shift, explains ~18% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -9.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[C-33 A (line)]] | alt | 75.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -11.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 55.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -10.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 64.6 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.18× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 46.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.41× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -10.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 78.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -11.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 45.4 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.28× (z +9.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -10.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SW 900 (line)]] | alt | 25.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -12.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -10.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 42.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.19× (z +8.7) | — |
| [[A498 (line)]] | wt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -9.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -10.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 16.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 10.1× (z +10.6) | — |
| [[H4 (line)]] | wt | 40.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0929× (z -10.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -9.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -9.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -9.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -10.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 34.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.95× (z +9.0) | — |
| [[A549 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 682), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM10B]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[LONP1]] | +0.67 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[BMT2]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[CRYBB2P1-1]] | +0.67 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[POM121]] | +0.66 | +0.75 / +0.55 | both halves | 1e-05 | pathway: HIV Infection |
| [[RNF4]] | +0.65 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[GID4]] | +0.65 | +0.66 / +0.57 | both halves | 8e-06 |  |
| [[VPS53]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[AK2]] | +0.62 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[PLEKHA8]] | +0.62 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[SPINDOC]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[EIF1AD]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGL]] | -0.59 | -0.57 / -0.62 | both halves | 9e-06 |  |
| [[ZNF518A]] | -0.58 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[FAM200B]] | -0.57 | -0.72 / -0.47 | both halves | 2e-05 |  |
| [[BRAF]] | -0.55 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[DZIP3]] | -0.55 | -0.67 / -0.44 | both halves | 3e-05 |  |
| [[NBPF26]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[KPNA5]] | -0.54 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[SUGT1P3-1]] | -0.54 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[CX3CL1]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[POGZ]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[GORAB]] | -0.53 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[SOCS2]] | -0.53 | -0.58 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRIP1]] | B | NRIP1 activity lowers CTDP1's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 1.49× higher at baseline in the lines without NRIP1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.4, -20.9); signed map (-40.9, 23.6). **Vector** length 101, 30.5% of its response variance represented; |z| ≥ 3 in 1,169 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.3 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +6.8 | +4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.8 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.6 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +0.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +5.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -11.0 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -10.8 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -8.0 | -2.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.4 | -4.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -0.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.6 | -2.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | CTD phosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q23 — chr18:79,679,803-79,754,503 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FCP1 |
| Gene groups (HGNC) | CTD family phosphatases |
| Reactome | 25 pathways, smallest: Abortive elongation of HIV-1 transcript in the absence of Tat; Pausing and recovery of Tat-mediated HIV elongation; Tat-mediated HIV elongation arrest and recovery |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5B0](https://www.uniprot.org/uniprotkb/Q9Y5B0) (RNA polymerase II subunit A C-terminal domain phosphatase):

> Processively dephosphorylates 'Ser-2' and 'Ser-5' of the heptad repeats YSPTSPS in the C-terminal domain of the largest RNA polymerase II subunit. This promotes the activity of RNA polymerase II. Plays a role in the exit from mitosis by dephosphorylating crucial mitotic substrates (USP44, CDC20 and WEE1) that are required for M-phase-promoting factor (MPF)/CDK1 inactivation.

**Summary**, from NCBI Gene [9150](https://www.ncbi.nlm.nih.gov/gene/9150):

> This gene encodes a protein which interacts with the carboxy-terminus of the RAP74 subunit of transcription initiation factor TFIIF, and functions as a phosphatase that processively dephosphorylates the C-terminus of POLR2A (a subunit of RNA polymerase II), making it available for initiation of gene expression. Mutations in this gene are associated with congenital cataracts, facial dysmorphism and neuropathy syndrome (CCFDN). Alternatively spliced transcript variants encoding different isoforms …

**Accessions** — [HGNC:2498](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2498) · Entrez [9150](https://www.ncbi.nlm.nih.gov/gene/9150) · UniProt [Q9Y5B0](https://www.uniprot.org/uniprotkb/Q9Y5B0) · Ensembl [ENSG00000060069](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000060069)

## Data

Gene col 682: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 682); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 682, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 682]; `tensor/DDL_lfc|DDL_z.npy` [682]; `embed/gene_vectors.npy` [682]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 682 or target_col == 682). Every well: [[CTDP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTDP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
