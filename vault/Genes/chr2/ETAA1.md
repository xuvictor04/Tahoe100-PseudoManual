---
symbol: "ETAA1"
type: "gene"
col: 6829
ensembl_id: "ENSG00000143971"
name: "ETAA1 activator of ATR kinase"
location: "2p14"
module: 11
arm: "+"
pooled_cpm: 22.82
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 23
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ETAA1

*ETAA1 activator of ATR kinase* — 2p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.29× (z +5.9, q 2e-06, up in 20 of 48 measured lines) ⚠ cell-cycle shift, explains ~19% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.33× (z +4.8, q 5e-04, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.421× (z -14.3, q 1e-43, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OBI1]] (+0.68, fdr 7e-06), [[CSTF1]] (+0.67, fdr 7e-06), [[KIAA1586]] (+0.62, fdr 7e-06); moves opposite to [[PRKCZ]] (-0.55, fdr 3e-05), [[INPP5A]] (-0.54, fdr 1e-05), [[MBOAT7]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6829.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.29×** | +5.9 | 2e-06 | 20/48 (SK-MEL-2, A498, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +4.8 | 5e-04 | 24/48 (CFPAC-1, hTERT-HPNE, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.2 | 0.006 | 18/48 (A-427, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 0.007 | 14/48 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.8 | 0.019 | 13/48 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.089 | 10/48 (SK-MEL-2, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.21× | +3.1 | 0.16 | 12/47 (A-172, HOP62, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.16 | 6/48 (COLO 205, LOX-IMVI, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6829.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.421×** | -14.3 | 1e-43 | 44/48 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.459×** | -12.9 | 2e-35 | 28/43 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.539×** | -10.2 | 3e-22 | 34/47 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.565×** | -9.4 | 6e-19 | 31/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.569×** | -9.3 | 1e-18 | 34/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.587×** | -8.5 | 2e-15 | 30/45 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.587×** | -8.3 | 8e-15 | 34/48 (Hs 766T, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.612×** | -8.1 | 3e-14 | 28/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.616×** | -7.7 | 8e-13 | 21/31 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.640×** | -7.4 | 1e-11 | 32/48 (PANC-1, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.681×** | -6.3 | 1e-08 | 22/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.582×** | -4.7 | 1e-04 | 16/41 (NCI-H1573, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.739×** | -4.6 | 2e-04 | 18/38 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.685×** | -4.5 | 3e-04 | 22/48 (HCT15, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.702×** | -4.2 | 0.001 | 17/46 (CHP-212, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 0.5 µM |  | **0.799×** | -3.7 | 0.007 | 14/48 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.810×** | -3.5 | 0.014 | 14/48 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.699×** | -3.1 | 0.051 | 17/45 (RPMI-7951, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.700×** | -3.1 | 0.051 | 6/47 (NCI-H1792, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 5 µM |  | **0.829×** | -3.0 | 0.073 | 5/48 (PANC-1, HepG2/C3A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6829. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 27.9 | 0 | 14 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -17.9) |
| [[NCI-H1792 (line)]] | alt | 42.9 | 0 | 8 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.119× (z -13.9) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H460 (line)]] | wt | 19.5 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -13.4) |
| [[A-427 (line)]] | wt | 44.9 | 0 | 5 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -12.4) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.351× (z -10.2) |
| [[A498 (line)]] | wt | 47.1 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -17.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 29.2 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.182× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.324× (z -11.7) |
| [[A-172 (line)]] | wt | 28.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0928× (z -18.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 24.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0822× (z -20.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 18.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -13.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.183× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 28.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0773× (z -21.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 24.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.278× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 33.1 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -9.3) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.367× (z -9.1) |
| [[A549 (line)]] | wt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -10.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 7.88 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0881× (z -8.9) |
| [[C-33 A (line)]] | alt | 23.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -9.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 19.9 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.191× (z -9.5) |
| [[J82 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.205× (z -9.3) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.189× (z -9.9) |
| [[SW48 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0688× (z -10.2) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6829), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OBI1]] | +0.68 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[CSTF1]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[KIAA1586]] | +0.62 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[COIL]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[UQCRFS1]] | +0.59 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[PPP4R2]] | +0.58 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[MRFAP1L1]] | +0.58 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[DDX20]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MRPL44]] | +0.57 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[RDH14]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NUDT6]] | +0.56 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[KLHL9]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKCZ]] | -0.55 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[INPP5A]] | -0.54 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[MBOAT7]] | -0.53 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[FBRSL1]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[TCF3]] | -0.52 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[GAK]] | -0.51 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[TPD52L2]] | -0.51 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[TPST2]] | -0.50 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[BAIAP2]] | -0.49 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[CTBP2]] | -0.49 | -0.65 / -0.38 | both halves | 6e-05 |  |
| [[PPP1R12C]] | -0.49 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[UFD1]] | -0.49 | -0.38 / -0.53 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.536). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.5, 5.3); signed map (2.4, -19.8). **Vector** length 77.0, 15.2% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | -1.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +4.4 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | +0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +4.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.0 | -14.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.8 | -12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -7.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -10.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.2 | -8.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.5 | -4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -7.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ETAA1 activator of ATR kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p14 — chr2:67,397,322-67,412,089 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ETAA16 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NY74](https://www.uniprot.org/uniprotkb/Q9NY74) (Ewing's tumor-associated antigen 1):

> Replication stress response protein that accumulates at DNA damage sites and promotes replication fork progression and integrity. Recruited to stalled replication forks via interaction with the RPA complex and directly stimulates ATR kinase activity independently of TOPBP1. Probably only regulates a subset of ATR targets.

**Summary**, from NCBI Gene [54465](https://www.ncbi.nlm.nih.gov/gene/54465):

> Enables protein serine/threonine kinase activator activity. Involved in several processes, including positive regulation of protein serine/threonine kinase activity; regulation of cell cycle phase transition; and replication fork processing. Located in nuclear replication fork and nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24648](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24648) · Entrez [54465](https://www.ncbi.nlm.nih.gov/gene/54465) · UniProt [Q9NY74](https://www.uniprot.org/uniprotkb/Q9NY74) · Ensembl [ENSG00000143971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143971)

## Data

Gene col 6829: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6829); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6829, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6829]; `tensor/DDL_lfc|DDL_z.npy` [6829]; `embed/gene_vectors.npy` [6829]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6829 or target_col == 6829). Every well: [[ETAA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETAA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
