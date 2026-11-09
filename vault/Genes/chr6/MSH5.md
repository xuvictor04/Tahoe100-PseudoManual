---
symbol: "MSH5"
type: "gene"
col: 12870
ensembl_id: "ENSG00000204410"
name: "mutS homolog 5"
location: "6p21.33"
module: 6
arm: "+"
pooled_cpm: 27.47
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 28
n_dd_up_clean: 3
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MSH5

*mutS homolog 5* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.46× (z +11.9, q 6e-30, up in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.66× (z +6.7, q 4e-09, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.433× (z -14.9, q 0e+00, down in 40 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.413× (z -11.7, q 4e-29, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX11]] (+0.75, fdr 7e-06), [[CENPI]] (+0.74, fdr 7e-06), [[POLA1]] (+0.73, fdr 7e-06); moves opposite to [[ATP6V1G1]] (-0.64, fdr 7e-06), [[CCDC59]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12870.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.46×** | +11.9 | 6e-30 | 43/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.21×** | +10.5 | 4e-23 | 42/46 (SW480, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.13×** | +10.0 | 3e-21 | 39/47 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +6.7 | 4e-09 | 33/47 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.14×** | +5.3 | 2e-05 | 27/47 (SW480, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +5.1 | 3e-05 | 26/46 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12870.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.433×** | -14.9 | 0e+00 | 40/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.413×** | -11.7 | 4e-29 | 41/46 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.421×** | -11.5 | 4e-28 | 45/46 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.446×** | -10.1 | 8e-22 | 36/47 (SK-MEL-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.511×** | -8.9 | 7e-17 | 35/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.631×** | -8.2 | 2e-14 | 37/46 (MIA PaCa-2, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.531×** | -8.1 | 6e-14 | 33/47 (PANC-1, SK-MEL-2, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.550×** | -7.9 | 2e-13 | 37/47 (KATO III, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.347×** | -7.3 | 2e-11 | 30/39 (HEC-1-A, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.576×** | -7.3 | 2e-11 | 27/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.629×** | -6.1 | 5e-08 | 26/47 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.737×** | -5.5 | 2e-06 | 32/47 (J82, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.667×** | -5.4 | 4e-06 | 24/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.704×** | -4.6 | 1e-04 | 23/46 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.513×** | -4.6 | 1e-04 | 23/45 (AN3 CA, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.515×** | -4.6 | 2e-04 | 25/47 (SHP-77, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.542×** | -4.2 | 7e-04 | 21/46 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.740×** | -4.0 | 0.002 | 19/47 (Panc 03.27, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.752×** | -3.8 | 0.005 | 20/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.692×** | -3.5 | 0.015 | 17/47 (HOP62, SW 1271, …) | all doses, flat | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.616×** | -3.4 | 0.022 | 19/45 (C32, COLO 205, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12870. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 61.2 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -13.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.306× (z -10.1) |
| [[PANC-1 (line)]] | alt | 55.9 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -17.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.191× (z -14.3) |
| [[SW480 (line)]] | alt | 26.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -14.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.311× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 24.9 | 0 | 6 (4 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0501× (z -17.7) |
| [[LS 180 (line)]] | wt | 24.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -10.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.229× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 31.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0756× (z -16.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -14.9) |
| [[A-427 (line)]] | wt | 37.0 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.226× (z -11.9) |
| [[J82 (line)]] | alt | 69.2 | 0 | 4 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.286× (z -9.7) |
| [[A549 (line)]] | wt | 23.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -11.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 44.0 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0895× (z -10.5) ⚠ toxic · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.328× (z -8.7) |
| [[HOP62 (line)]] | alt | 34.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -14.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 25.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -10.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.256× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 17.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -14.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.293× (z -8.7) |
| [[H4 (line)]] | wt | 25.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -9.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -9.1) |
| [[KATO III (line)]] | alt | 29.2 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.189× (z -10.7) |
| [[SHP-77 (line)]] | alt | 46.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.233× (z -10.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 42.2 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.297× (z -9.0) |
| [[SW48 (line)]] | wt | 26.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -8.8) |
| [[AN3 CA (line)]] | alt | 47.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0880× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -10.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HS-578T (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.241× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.236× (z -9.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 19.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.234× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 29.9 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.236× (z -9.2) |
| [[RKO (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -9.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -13.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12870), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX11]] | +0.75 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[CENPI]] | +0.74 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[POLA1]] | +0.73 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[CENPK]] | +0.73 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[DDX12P]] | +0.73 | +0.64 / +0.77 | both halves | 7e-06 |  |
| [[BLM]] | +0.72 | +0.61 / +0.74 | both halves | 7e-06 | pathway: Meiosis; STRING 718 |
| [[FANCA]] | +0.72 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[NCAPG2]] | +0.72 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[MELK]] | +0.71 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[SPC24]] | +0.71 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.71 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[FANCB]] | +0.71 | +0.62 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1G1]] | -0.64 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[CCDC59]] | -0.62 | -0.52 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MSH5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TCF19]] | B | TCF19 activity raises MSH5's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.13× lower at baseline in the lines without TCF19 | 0.045 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDCA7L]] | B | CDCA7L activity raises MSH5's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.29× lower at baseline in the lines without CDCA7L | 0.051 | ⚠ within organs, on part of the lines |
| [[TERT]] | B | TERT activity raises MSH5's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.49× lower at baseline in the lines without TERT | 0.097 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[PBK]] | C | PBK activity raises MSH5's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.24× lower at baseline in the lines without PBK | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises MSH5's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.49× lower at baseline in the lines without AURKB | 0.058 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[MELK]] | C | MELK activity raises MSH5's level | lines that do not express MELK (3) vs lines expressing it (47) | 2.66× lower at baseline in the lines without MELK | 0.075 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent |
| [[MCM3]] | C | MCM3 activity raises MSH5's level | lines that do not express MCM3 (3) vs lines expressing it (47) | 2.52× lower at baseline in the lines without MCM3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.721). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-29.5, -44.9); signed map (-36.1, -39.5). **Vector** length 111, 31.9% of its response variance represented; |z| ≥ 3 in 1,179 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.52 to 65); *DNA strand elongation* (reactome, mean cos +0.54 to 28); *DNA Replication* (reactome, mean cos +0.53 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.8 | +10.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.7 | +11.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.3 | +10.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +6.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.0 | +5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.4 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.1 | -8.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -7.8 | -10.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -7.3 | -8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.3 | -11.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.8 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | mutS homolog 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,739,677-31,762,676 (+) |
| Ensembl biotype | protein_coding |
| Also known as | G7 |
| Gene groups (HGNC) | MutS homologs |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 4 pathways, smallest: Meiotic recombination; Meiosis; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [O43196](https://www.uniprot.org/uniprotkb/O43196) (MutS protein homolog 5):

> Involved in DNA mismatch repair and meiotic recombination processes. Facilitates crossovers between homologs during meiosis (By similarity).

**Summary**, from NCBI Gene [4439](https://www.ncbi.nlm.nih.gov/gene/4439):

> This gene encodes a member of the mutS family of proteins that are involved in DNA mismatch repair and meiotic recombination. This protein is similar to a Saccharomyces cerevisiae protein that participates in segregation fidelity and crossing-over events during meiosis. This protein plays a role in promoting ionizing radiation-induced apoptosis. This protein forms hetero-oligomers with another member of this family, mutS homolog 4. Polymorphisms in this gene have been linked to various human …

**Accessions** — [HGNC:7328](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7328) · Entrez [4439](https://www.ncbi.nlm.nih.gov/gene/4439) · UniProt [O43196](https://www.uniprot.org/uniprotkb/O43196) · Ensembl [ENSG00000204410](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204410)

## Data

Gene col 12870: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12870); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12870, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12870]; `tensor/DDL_lfc|DDL_z.npy` [12870]; `embed/gene_vectors.npy` [12870]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12870 or target_col == 12870). Every well: [[MSH5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSH5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
