---
symbol: "ARHGEF9"
type: "gene"
col: 5168
ensembl_id: "ENSG00000131089"
name: "Cdc42 guanine nucleotide exchange factor 9"
location: "Xq11.1"
module: 3
arm: "-"
pooled_cpm: 28.09
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 39
n_dd_up_clean: 1
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# ARHGEF9

*Cdc42 guanine nucleotide exchange factor 9* — Xq11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.92× (z +9.6, q 4e-19, up in 31 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.33× (z +4.2, q 0.004, up in 24 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 3.48×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (16 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.320× (z -17.4, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPD]] (+0.68, fdr 9e-06), [[YWHAE]] (+0.59, fdr 2e-05), [[EWSR1]] (+0.59, fdr 5e-05); moves opposite to [[VRK3]] (-0.60, fdr 1e-05), [[CDC34]] (-0.60, fdr 2e-05), [[IL17RA]] (-0.59, fdr 2e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF611]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5168.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 3.48×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +9.6 | 4e-19 | 31/38 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.81×** | +7.6 | 6e-12 | 30/43 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +6.8 | 3e-09 | 27/41 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.004 | 24/46 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.17× | +3.4 | 0.090 | 14/47 (C-33 A, KATO III, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.15× | +3.1 | 0.16 | 8/47 (RPMI-7951, H4, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.18 | 13/47 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.05 µM |  | 1.22× | +3.0 | 0.18 | 8/47 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5168.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.320×** | -17.4 | 0e+00 | 45/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.346×** | -16.2 | 0e+00 | 44/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.379×** | -14.8 | 0e+00 | 42/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.399×** | -14.0 | 2e-42 | 42/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.421×** | -13.2 | 1e-37 | 40/46 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.522×** | -9.4 | 7e-19 | 35/47 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.574×** | -8.5 | 2e-15 | 33/47 (KATO III, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.678×** | -8.4 | 5e-15 | 27/46 (NCI-H1573, HEC-1-A, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.605×** | -7.4 | 1e-11 | 29/44 (SW1417, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.624×** | -7.2 | 4e-11 | 32/47 (BT-474, SW480, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.649×** | -6.6 | 2e-09 | 27/46 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.658×** | -6.4 | 9e-09 | 29/47 (A-427, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.485×** | -5.8 | 4e-07 | 26/40 (MIA PaCa-2, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.695×** | -5.5 | 1e-06 | 22/46 (KATO III, HCT15, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.698×** | -5.5 | 2e-06 | 22/47 (COLO 205, SW480, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.669×** | -5.1 | 1e-05 | 25/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.795×** | -4.9 | 3e-05 | 27/47 (CFPAC-1, KATO III, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.800×** | -4.8 | 5e-05 | 22/47 (Hs 766T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.729×** | -4.6 | 9e-05 | 21/47 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.699×** | -4.6 | 1e-04 | 19/46 (NCI-H23, RPMI-7951, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5168. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 50.9 | 0 | 9 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.198× (z -14.6) |
| [[PANC-1 (line)]] | alt | 26.6 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.185× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.199× (z -15.0) |
| [[SW480 (line)]] | alt | 33.7 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -17.3) |
| [[A-427 (line)]] | wt | 36.1 | 0 | 5 | — | [[Auranofin (drug)]] 5 µM 0.227× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 35.9 | 0 | 5 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.161× (z -12.2) |
| [[BT-474 (line)]] | alt | 39.0 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.158× (z -12.4) |
| [[COLO 205 (line)]] | alt | 43.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.5) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.238× (z -9.8) |
| [[Hs 766T (line)]] | wt | 36.8 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.228× (z -10.7) |
| [[J82 (line)]] | alt | 22.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -9.7) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -9.0) |
| [[LS 180 (line)]] | wt | 32.2 | 0 | 4 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.300× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 44.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -14.3) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.193× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 31.3 | 0 | 4 | — | [[Ixazomib citrate (drug)]] 5 µM 0.231× (z -13.7) |
| [[SNU-1 (line)]] | wt | 46.1 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0602× (z -16.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.119× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 50.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -13.0) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.406× (z -9.0) |
| [[LoVo (line)]] | wt | 17.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.48× (z +9.3) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.243× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 17.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -10.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 32.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.241× (z -10.3) |
| [[RKO (line)]] | wt | 24.8 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -9.5) |
| [[SNU-423 (line)]] | alt | 51.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.308× (z -9.6) |
| [[C32 (line)]] | wt | 24.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.210× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 19.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -9.0) |
| [[HOP62 (line)]] | alt | 28.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.278× (z -9.8) |
| [[HT-29 (line)]] | alt | 17.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 21.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -11.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 41.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -11.3) |
| [[SHP-77 (line)]] | alt | 33.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[vincristine (drug)]] 5 µM 0.0933× (z -8.9) |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.190× (z -10.5) |
| [[SW1417 (line)]] | alt | 22.2 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0629× (z -18.0) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.281× (z -8.6) |
| [[A-172 (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.346× (z -8.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -9.7) ⚠ cell-cycle shift, explains ~66% of this change |
| [[C-33 A (line)]] | alt | 49.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.197× (z -10.8) |
| [[H4 (line)]] | wt | 29.7 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.191× (z -8.9) |
| [[HCT15 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -10.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5168), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPD]] | +0.68 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[YWHAE]] | +0.59 | +0.48 / +0.55 | both halves | 2e-05 | pathway: Cell death signalling via NRAGE, NRIF and NADE |
| [[EWSR1]] | +0.59 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[FUBP1]] | +0.57 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[PUS7L]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[SRSF1]] | +0.57 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[BCLAF1]] | +0.56 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[HMGN1]] | +0.56 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[ACADM]] | +0.55 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[HNRNPA3]] | +0.55 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[DHX9]] | +0.55 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[AGL]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 5 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VRK3]] | -0.60 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[CDC34]] | -0.60 | -0.46 / -0.60 | both halves | 2e-05 |  |
| [[IL17RA]] | -0.59 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[PLIN3]] | -0.57 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[ZNF611]] | -0.57 | -0.37 / -0.62 | both halves | 7e-05 |  |
| [[RPL36AL]] ⚠ | -0.56 | -0.29 / -0.61 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[NOP10]] ⚠ | -0.54 | -0.33 / -0.55 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[EMC6]] | -0.54 | -0.17 / -0.56 | ⚠ one half (not replicated) | 0.001 |  |
| [[ARID3A]] | -0.53 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[CAMLG]] | -0.53 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[CIAO2B]] | -0.53 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[MED10]] | -0.53 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[TM2D2]] | -0.53 | -0.24 / -0.62 | both halves | 5e-04 |  |
| [[POLR2J4]] | -0.52 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[TRAPPC4]] | -0.52 | -0.26 / -0.53 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF611]] | C | ZNF611 activity raises ARHGEF9's level | lines that do not express ZNF611 (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without ZNF611 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF468, ZNF845, ZNF14; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.593). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.5, -24.2); signed map (14.9, -38.5). **Vector** length 77.0, 18.5% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.50 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +9.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.8 | -4.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +3.1 | -5.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -4.2 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +1.5 | +2.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.9 | -7.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -13.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.3 | -9.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.6 | -7.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -2.5 | -5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -4.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.3 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | Cdc42 guanine nucleotide exchange factor 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq11.1 — chrX:63,634,967-63,809,274 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0424, PEM-2 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; SH3 domain containing |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 16 pathways, smallest: GABA receptor activation; NRAGE signals death through JNK; RHOQ GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O43307](https://www.uniprot.org/uniprotkb/O43307) (Rho guanine nucleotide exchange factor 9):

> Acts as a guanine nucleotide exchange factor (GEF) for CDC42. Promotes formation of GPHN clusters (By similarity).

**Summary**, from NCBI Gene [23229](https://www.ncbi.nlm.nih.gov/gene/23229):

> The protein encoded by this gene is a Rho-like GTPase that switches between the active (GTP-bound) state and inactive (GDP-bound) state to regulate CDC42 and other genes. This brain-specific protein also acts as an adaptor protein for the recruitment of gephyrin and together these proteins facilitate receceptor recruitement in GABAnergic and glycinergic synapses. Defects in this gene are the cause of startle disease with epilepsy (STHEE), also known as hyperekplexia with epilepsy, as well as …

**Accessions** — [HGNC:14561](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14561) · Entrez [23229](https://www.ncbi.nlm.nih.gov/gene/23229) · UniProt [O43307](https://www.uniprot.org/uniprotkb/O43307) · Ensembl [ENSG00000131089](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131089)

## Data

Gene col 5168: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5168); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5168, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5168]; `tensor/DDL_lfc|DDL_z.npy` [5168]; `embed/gene_vectors.npy` [5168]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5168 or target_col == 5168). Every well: [[ARHGEF9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
