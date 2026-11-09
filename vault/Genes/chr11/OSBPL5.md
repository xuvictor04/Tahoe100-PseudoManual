---
symbol: "OSBPL5"
type: "gene"
col: 329
ensembl_id: "ENSG00000021762"
name: "oxysterol binding protein like 5"
location: "11p15.4"
module: 97
arm: "+"
pooled_cpm: 42.02
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 50
n_dd_up_clean: 2
n_dd_down_clean: 37
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# OSBPL5

*oxysterol binding protein like 5* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 1.32× (z +4.6, q 0.002, up in 20 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (A498 2.88×); [[Budesonide (drug)]] 0.5 µM in 1 line (A498 2.66×); [[Phenylephrine (hydrochloride) (drug)]] 5 µM in 1 line (A498 2.52×).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.303× (z -19.5, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT2A]] (+0.64, fdr 7e-06), [[C16orf74]] (+0.64, fdr 7e-06), [[SPRY4]] (+0.64, fdr 7e-06); moves opposite to [[BBOX1-AS1]] (-0.52, fdr 2e-05), [[ZSCAN31]] (-0.52, fdr 3e-05), [[HINT3]] (-0.51, fdr 1e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ITPRIP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 329.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (A498 2.88×); [[Budesonide (drug)]] 0.5 µM in 1 line (A498 2.66×); [[Phenylephrine (hydrochloride) (drug)]] 5 µM in 1 line (A498 2.52×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.32×** | +4.6 | 0.002 | 20/46 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.053 | 17/46 (A498, SNU-423, …) | two highest doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.22× | +3.3 | 0.14 | 6/46 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.22× | +3.3 | 0.14 | 18/46 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.22× | +3.2 | 0.14 | 13/46 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 329.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.303×** | -19.5 | 0e+00 | 45/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.454×** | -18.2 | 0e+00 | 41/46 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.466×** | -17.6 | 0e+00 | 35/45 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.419×** | -14.2 | 2e-43 | 37/45 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.421×** | -14.1 | 3e-43 | 41/46 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.443×** | -13.3 | 2e-38 | 42/46 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.446×** | -13.2 | 9e-38 | 36/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.473×** | -12.2 | 2e-32 | 40/46 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.474×** | -12.2 | 3e-32 | 42/46 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.450×** | -11.9 | 4e-31 | 34/46 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.262×** | -11.4 | 2e-28 | 35/47 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.498×** | -11.4 | 3e-28 | 41/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.470×** | -11.3 | 6e-28 | 37/44 (HOP62, COLO 205, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.475×** | -11.1 | 3e-27 | 39/46 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.650×** | -9.9 | 1e-21 | 30/46 (HOP62, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.577×** | -9.0 | 1e-17 | 32/46 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.370×** | -8.5 | 7e-16 | 31/45 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 329. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 59.1 | 0 | 21 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -25.9) |
| [[HOP62 (line)]] | alt | 94.8 | 0 | 16 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -16.4) |
| [[LoVo (line)]] | wt | 35.2 | 0 | 15 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0740× (z -25.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -17.2) |
| [[SW480 (line)]] | alt | 41.6 | 0 | 15 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.197× (z -15.8) |
| [[LOX-IMVI (line)]] | wt | 57.4 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -21.4) |
| [[PANC-1 (line)]] | alt | 48.7 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -19.8) |
| [[NCI-H23 (line)]] | alt | 36.3 | 0 | 12 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0633× (z -18.7) |
| [[HEC-1-A (line)]] | alt | 31.5 | 0 | 11 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.265× (z -16.6) |
| [[A498 (line)]] | wt | 40.9 | 5 | 5 | [[Clobetasol propionate (drug)]] 0.5 µM 2.88× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 91.2 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -19.8) |
| [[Hs 766T (line)]] | wt | 71.9 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -16.2) |
| [[MIA PaCa-2 (line)]] | alt | 31.2 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -12.7) |
| [[A549 (line)]] | wt | 32.1 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -17.7) |
| [[J82 (line)]] | alt | 51.2 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -14.2) |
| [[NCI-H2030 (line)]] | alt | 30.7 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -22.6) |
| [[RPMI-7951 (line)]] | alt | 71.3 | 0 | 7 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -11.5) |
| [[RKO (line)]] | wt | 36.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -10.3) |
| [[COLO 205 (line)]] | alt | 37.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -19.6) |
| [[LS 180 (line)]] | wt | 70.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 21.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -14.5) |
| [[SNU-423 (line)]] | alt | 35.7 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -11.2) |
| [[SW1417 (line)]] | alt | 32.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -13.8) |
| [[A-172 (line)]] | wt | 58.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.464× (z -10.7) |
| [[A-427 (line)]] | wt | 21.5 | 0 | 3 | — | [[TAK-901 (drug)]] 5 µM 0.0531× (z -9.6) |
| [[C-33 A (line)]] | alt | 30.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.236× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 52.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0942× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -11.4) |
| [[KATO III (line)]] | alt | 22.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -14.2) |
| [[SW48 (line)]] | wt | 44.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -11.2) |
| [[H4 (line)]] | wt | 76.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -10.0) |
| [[HCT15 (line)]] | alt | 45.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -10.5) |
| [[HS-578T (line)]] | alt | 26.3 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.293× (z -9.2) |
| [[HT-29 (line)]] | alt | 56.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -13.9) |
| [[SNU-1 (line)]] | wt | 37.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0787× (z -14.6) |
| [[BT-474 (line)]] | alt | 18.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 33.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.244× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.17 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 329), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT2A]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[C16orf74]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[MT1X]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[MT1A]] | +0.63 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[HMGA2]] | +0.60 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[PHC2]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[TOX2]] | +0.59 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ERGIC1]] | +0.58 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[AKAP12]] | +0.57 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[MLKL]] | +0.57 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[ASAP2]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBOX1-AS1]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[ZSCAN31]] | -0.52 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[HINT3]] | -0.51 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[EDIL3]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[IFT57]] | -0.51 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[LURAP1L]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[ITM2B]] | -0.50 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[GALNT7]] | -0.49 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[ERAP1]] | -0.49 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[SCARB2]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ATXN1-AS1]] | -0.49 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[IDO1]] | -0.49 | -0.50 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITPRIP]] | B | ITPRIP activity raises OSBPL5's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 1.67× lower at baseline in the lines without ITPRIP | 0.009 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[C13orf46]] | B | C13orf46 activity raises OSBPL5's level | lines that do not express C13orf46 (11) vs lines expressing it (39) | 2.17× lower at baseline in the lines without C13orf46 | 0.022 | ⚠ within organs, on part of the lines; also absent: RASA3, COL27A1, PRR5L |
| [[LDLRAD3]] | B | LDLRAD3 activity raises OSBPL5's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 2.56× lower at baseline in the lines without LDLRAD3 | 0.037 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CLMP]] | B | CLMP activity raises OSBPL5's level | lines that do not express CLMP (25) vs lines expressing it (25) | 1.52× lower at baseline in the lines without CLMP | 0.052 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[SERPINE1]] | B | SERPINE1 activity raises OSBPL5's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 1.43× lower at baseline in the lines without SERPINE1 | 0.075 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[TOP2A]] | B | TOP2A activity raises OSBPL5's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.0% of all compounds | 0.089 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SPRY4-AS1]] | C | SPRY4-AS1 activity raises OSBPL5's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 2.25× lower at baseline in the lines without SPRY4-AS1 | 0.064 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent |
| [[ARHGEF19]] | C | ARHGEF19 activity strengthens OSBPL5's drug response | lines that do not express ARHGEF19 (3) vs lines expressing it (43) | the lines without ARHGEF19 respond 0.33× as strongly (z diff +3.78); strongest at Homoharringtonine 5 µM: 1.21x vs 0.41x (z diff +9.2) | 0.064 | ⚠ few lines (3 vs 47); across organs; also absent: SLC35F2, ENSG00000274213; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.4, 12.6); signed map (10.1, 35.5). **Vector** length 91.2, 26.5% of its response variance represented; |z| ≥ 3 in 1,617 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | -17.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.3 | +4.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.2 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +1.2 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | +3.0 | +2.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.0 | +2.5 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -5.8 | -2.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.7 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.5 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.2 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.1 | -2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | oxysterol binding protein like 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:3,087,107-3,166,739 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1534, ORP5, OBPH1 |
| Gene groups (HGNC) | Oxysterol binding proteins; Pleckstrin homology domain containing |
| Reactome | 4 pathways, smallest: Acyl chain remodelling of PS; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0X9](https://www.uniprot.org/uniprotkb/Q9H0X9) (Oxysterol-binding protein-related protein 5):

> Lipid transporter involved in lipid countertransport between the endoplasmic reticulum and the plasma membrane: specifically exchanges phosphatidylserine with phosphatidylinositol 4-phosphate (PI4P), delivering phosphatidylserine to the plasma membrane in exchange for PI4P, which is degraded by the SAC1/SACM1L phosphatase in the endoplasmic reticulum. Binds phosphatidylserine and PI4P in a mutually exclusive manner. May cooperate with NPC1 to mediate the exit of cholesterol from …

**Summary**, from NCBI Gene [114879](https://www.ncbi.nlm.nih.gov/gene/114879):

> This gene encodes a member of the oxysterol-binding protein (OSBP) family, a group of intracellular lipid receptors that play a key role in the maintenance of cholesterol balance in the body. Most members contain an N-terminal pleckstrin homology domain and a highly conserved C-terminal OSBP-like sterol-binding domain. This gene has been shown to be imprinted, with preferential expression from the maternal allele only in placenta. Transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:16392](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16392) · Entrez [114879](https://www.ncbi.nlm.nih.gov/gene/114879) · UniProt [Q9H0X9](https://www.uniprot.org/uniprotkb/Q9H0X9) · Ensembl [ENSG00000021762](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000021762)

## Data

Gene col 329: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 329); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 329, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 329]; `tensor/DDL_lfc|DDL_z.npy` [329]; `embed/gene_vectors.npy` [329]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 329 or target_col == 329). Every well: [[OSBPL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSBPL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
