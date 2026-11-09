---
symbol: "TRMT2B"
type: "gene"
col: 12066
ensembl_id: "ENSG00000188917"
name: "tRNA methyltransferase 2B"
location: "Xq22.1"
module: 14
arm: "+"
pooled_cpm: 31.14
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 25
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TRMT2B

*tRNA methyltransferase 2B* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.42× (z +5.8, q 4e-06, up in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~61% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.31× (z +4.6, q 6e-04, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.258× (z -33.1, q 0e+00, down in 44 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.312× (z -20.1, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THOC5]] (+0.57, fdr 9e-06), [[BABAM1]] (+0.53, fdr 5e-05), [[ZCCHC4]] (+0.52, fdr 3e-05); moves opposite to [[KLF10]] (-0.60, fdr 1e-05), [[BHLHE41]] (-0.58, fdr 1e-05), [[CAV1]] (-0.56, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); 2 go from it, the strongest it → [[IPP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12066.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.42×** | +5.8 | 4e-06 | 28/48 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.33×** | +4.9 | 3e-04 | 22/47 (SW480, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 6e-04 | 20/48 (HOP62, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12066.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.258×** | -33.1 | 0e+00 | 44/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.312×** | -20.1 | 0e+00 | 46/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.394×** | -15.5 | 0e+00 | 42/47 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.551×** | -14.6 | 0e+00 | 37/47 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.446×** | -14.0 | 2e-42 | 41/47 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.462×** | -13.4 | 9e-39 | 44/48 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.504×** | -11.8 | 2e-30 | 39/48 (COLO 205, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.295×** | -11.0 | 2e-26 | 42/48 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.597×** | -8.9 | 3e-17 | 36/48 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.624×** | -8.1 | 2e-14 | 33/47 (J82, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.628×** | -8.0 | 4e-14 | 29/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.647×** | -7.5 | 3e-12 | 31/47 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.438×** | -7.5 | 4e-12 | 31/45 (Panc 03.27, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.710×** | -5.9 | 1e-07 | 21/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **0.710×** | -5.5 | 2e-06 | 24/38 (NCI-H460, NCI-H23, …) | inconsistent across doses | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.606×** | -4.5 | 2e-04 | 19/48 (Panc 03.27, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.843× | -4.2 | 8e-04 | 20/48 (Hs 766T, SW480, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.778×** | -3.1 | 0.045 | 17/44 (A-427, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[ERK5-IN-2 (drug)]] 0.5 µM |  | **0.782×** | -3.0 | 0.052 | 6/47 (Panc 03.27, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.890× | -2.8 | 0.089 | 12/48 (HOP62, Panc 03.27, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.843× | -2.8 | 0.089 | 13/47 (A498, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12066. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 115 | 0 | 17 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -29.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -20.4) |
| [[A549 (line)]] | wt | 34.5 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -18.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 34.0 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -24.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -17.8) |
| [[SW480 (line)]] | alt | 37.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -14.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.448× (z -8.9) |
| [[COLO 205 (line)]] | alt | 41.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -13.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.166× (z -10.7) |
| [[HOP62 (line)]] | alt | 24.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -16.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.449× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 28.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0801× (z -26.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.259× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 36.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -18.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -16.6) |
| [[Panc 03.27 (line)]] | alt | 30.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -14.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -9.9) |
| [[PANC-1 (line)]] | alt | 54.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -29.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -15.3) |
| [[SNU-423 (line)]] | alt | 43.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -19.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -10.5) |
| [[H4 (line)]] | wt | 31.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -13.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 24.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -22.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -12.4) |
| [[HCT15 (line)]] | alt | 25.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0647× (z -15.3) |
| [[HEC-1-A (line)]] | alt | 25.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -14.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -12.9) |
| [[J82 (line)]] | alt | 25.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -15.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.298× (z -9.7) |
| [[KATO III (line)]] | alt | 33.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -11.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.328× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 32.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -18.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.302× (z -9.9) |
| [[A-172 (line)]] | wt | 13.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -13.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 25.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -15.3) |
| [[A498 (line)]] | wt | 21.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -13.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -12.9) |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -11.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0716× (z -10.7) |
| [[LoVo (line)]] | wt | 15.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -14.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.295× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 36.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -15.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 23.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -12.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 2 (1 ⚠) | — | [[Saquinavir (drug)]] 0.05 µM 0.139× (z -10.5) |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -10.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -10.2) |
| [[SW1417 (line)]] | alt | 23.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 22.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -8.5) |
| [[BT-474 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -9.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -10.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -10.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 30.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 14.9 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.229× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -13.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -13.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -17.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12066), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC5]] | +0.57 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[BABAM1]] | +0.53 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[ZCCHC4]] | +0.52 | +0.56 / +0.46 | both halves | 3e-05 | same gene group |
| [[ANKRD39]] | +0.52 | +0.67 / +0.39 | both halves | 5e-05 |  |
| [[SMG5]] | +0.52 | +0.65 / +0.35 | both halves | 1e-04 |  |
| [[TOM1L1]] | +0.51 | +0.62 / +0.38 | both halves | 7e-05 |  |
| [[SLC30A6]] | +0.51 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[ANKRD23]] | +0.50 | +0.48 / +0.43 | both halves | 4e-05 |  |
| [[FLYWCH1]] | +0.50 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[TMEM161A]] | +0.49 | +0.60 / +0.38 | both halves | 6e-05 |  |
| [[CROCCP2]] | +0.49 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[RCC1L]] | +0.49 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF10]] | -0.60 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[BHLHE41]] | -0.58 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[CAV1]] | -0.56 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[HERPUD2-AS1]] | -0.55 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[LMNA]] | -0.54 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[NR3C1]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[BCL9L]] | -0.51 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[CCDC148]] | -0.49 | -0.66 / -0.34 | both halves | 1e-04 |  |
| [[FIBP]] | -0.49 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[BCOR]] | -0.49 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[CPEB2]] | -0.49 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[TAGLN2]] | -0.48 | -0.39 / -0.57 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers TRMT2B's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IPP]] | C | TRMT2B's natural level strengthens IPP's drug response | TRMT2B's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.15; direction not clear | 0.071 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | TRMT2B's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | TRMT2B's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.435 over the table, 0.085 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction -0.357). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-25.2, 36.6); signed map (-26.2, -26.0). **Vector** length 81.9, 18.5% of its response variance represented; |z| ≥ 3 in 1,248 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +7.6 | +4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | +7.3 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.5 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Afatinib (drug)]] 5 µM |  | +1.6 | +2.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.1 | -11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.8 | -33.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -20.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -7.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.3 | -15.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -7.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | tRNA methyltransferase 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:101,009,346-101,052,116 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12687; previously CXorf34 |
| Gene groups (HGNC) | 7BS C5-uridine RNA methyltransferases; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GJ1](https://www.uniprot.org/uniprotkb/Q96GJ1) (tRNA):

> Mitochondrial S-adenosyl-L-methionine-dependent methyltransferase that catalyzes the formation of 5-methyl-uridine in tRNAs and 12S rRNA. Catalyzes the methylation of uridine at position 54 (m5U54) in all tRNAs. Specifically methylates the uridine in position 429 of 12S rRNA (m5U429). Does not affect RNA stability or mitochondrial translation.

**Summary**, from NCBI Gene [79979](https://www.ncbi.nlm.nih.gov/gene/79979):

> This gene encodes a homolog of the TRM2 gene in S. cerevisiae. The yeast gene encodes a tRNA methyltransferase that plays a role in tRNA maturation. The yeast protein also has endo-exonuclease activity and may be involved in DNA double strand break repair. Alternative splicing results in multiple transcripts encoding different isoforms. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:25748](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25748) · Entrez [79979](https://www.ncbi.nlm.nih.gov/gene/79979) · UniProt [Q96GJ1](https://www.uniprot.org/uniprotkb/Q96GJ1) · Ensembl [ENSG00000188917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188917)

## Data

Gene col 12066: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12066); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12066, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12066]; `tensor/DDL_lfc|DDL_z.npy` [12066]; `embed/gene_vectors.npy` [12066]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12066 or target_col == 12066). Every well: [[TRMT2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMT2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
