---
symbol: "LRRCC1"
type: "gene"
col: 5471
ensembl_id: "ENSG00000133739"
name: "leucine rich repeat and coiled-coil centrosomal protein 1"
location: "8q21.2"
module: 6
arm: "+"
pooled_cpm: 15.36
n_lines_expressing: 46
n_dd_up: 13
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 31
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# LRRCC1

*leucine rich repeat and coiled-coil centrosomal protein 1* — 8q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.21× (z +15.4, q 0e+00, up in 34 of 34 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.46× (z +3.9, q 0.008, up in 13 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.461× (z -8.3, q 3e-14, down in 30 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MNS1]] (+0.72, fdr 7e-06), [[HLTF]] (+0.72, fdr 7e-06), [[PRIM1]] (+0.70, fdr 7e-06); moves opposite to [[NOXRED1]] (-0.62, fdr 3e-05), [[ZNF778]] (-0.61, fdr 2e-05), [[ZNF547]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DDX11]] → it (grade C ⚠); 31 go from it, the strongest it → cells under [[Homoharringtonine (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5471.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **4.21×** | +15.4 | 0e+00 | 34/34 (A498, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.96×** | +14.2 | 2e-43 | 24/25 (A498, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.01×** | +11.0 | 1e-25 | 29/30 (A498, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.59×** | +5.0 | 8e-05 | 23/43 (A498, NCI-H2030, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.58×** | +4.9 | 1e-04 | 19/43 (A498, A549, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.50×** | +4.3 | 0.001 | 24/44 (A498, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.008 | 13/42 (J82, LoVo, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.42×** | +3.8 | 0.010 | 15/42 (NCI-H1573, SW 900, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.42×** | +3.7 | 0.012 | 17/44 (A498, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.41×** | +3.7 | 0.014 | 15/38 (CFPAC-1, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.26×** | +3.6 | 0.020 | 13/43 (Hs 766T, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.058 | 15/43 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.096 | 9/42 (J82, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5471.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.461×** | -8.3 | 3e-14 | 30/42 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.461×** | -8.3 | 3e-14 | 32/42 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.469×** | -8.1 | 9e-14 | 29/44 (A498, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -6.9 | 9e-10 | 28/42 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.553×** | -6.3 | 2e-08 | 24/41 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.329×** | -6.2 | 4e-08 | 27/41 (SW1417, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.583×** | -5.8 | 5e-07 | 26/43 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.597×** | -5.2 | 1e-05 | 25/42 (PANC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.676×** | -4.2 | 0.002 | 24/42 (SW48, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.491×** | -4.0 | 0.004 | 19/43 (SHP-77, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.770×** | -4.0 | 0.004 | 21/43 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.552×** | -4.0 | 0.004 | 14/43 (KATO III, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.695×** | -3.9 | 0.004 | 21/43 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.698×** | -3.8 | 0.005 | 17/42 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.731×** | -3.4 | 0.030 | 16/44 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5471. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.3 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.234× (z -10.8) |
| [[A498 (line)]] | wt | 44.5 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -10.4) |
| [[SHP-77 (line)]] | alt | 77.3 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.312× (z -9.4) |
| [[HOP62 (line)]] | alt | 14.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.3) |
| [[KATO III (line)]] | alt | 23.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.28× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -8.9) |
| [[A-427 (line)]] | wt | 32.1 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.189× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 16.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[TAK-901 (drug)]] 0.05 µM 0.224× (z -9.4) |
| [[J82 (line)]] | alt | 18.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.42× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Digitoxin (drug)]] 5 µM 0.252× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 9.71 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.64× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 23.5 | 0 | 2 | — | [[TAK-901 (drug)]] 0.05 µM 0.131× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0700× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 10.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 0.05 µM 0.167× (z -9.9) |
| [[A549 (line)]] | wt | 7.34 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.146× (z -8.5) |
| [[BT-474 (line)]] | alt | 13.4 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.141× (z -8.7) |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -9.0) |
| [[LS 180 (line)]] | wt | 23.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 7.58 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.2× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[RKO (line)]] | wt | 23.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.146× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~83% of this change |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -8.9) |
| [[SW48 (line)]] | wt | 12.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0651× (z -9.1) |
| [[SW480 (line)]] | alt | 13.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5471), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MNS1]] | +0.72 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[HLTF]] | +0.72 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[PRIM1]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ALDH7A1]] | +0.68 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SSX2IP]] | +0.67 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[CENPS]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[MSH5]] | +0.63 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[CDCA7L]] | +0.62 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[CENPU]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[DNMT1]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[PHF6]] | +0.61 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[DHX9]] | +0.61 | +0.48 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOXRED1]] | -0.62 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[ZNF778]] | -0.61 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ZNF547]] | -0.58 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[TMEM11-DT]] | -0.57 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[ZNF586]] | -0.56 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[LRRC41]] | -0.56 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[MON1B]] | -0.54 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[C9orf153]] | -0.54 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[BORCS7-ASMT]] | -0.54 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[GUCA1B]] | -0.53 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[TMEM101]] | -0.53 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[TNXB]] | -0.53 | -0.46 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDX11]] | C | DDX11's natural level strengthens LRRCC1's drug response | DDX11's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.01; direction clear | 0.061 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 0, C 31. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Homoharringtonine (drug)]] 0.05 µM | C | LRRCC1, [[OXR1]] activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.55× the cells of the other lines | 0.008 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| cells under [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM | C | LRRCC1, [[OXR1]] activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.74× the cells of the other lines | 0.008 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| cells under [[Homoharringtonine (drug)]] 0.5 µM | C | LRRCC1, [[OXR1]] activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.22× the cells of the other lines | 0.012 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | LRRCC1, [[OXR1]] activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.76× the cells of the other lines | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| [[ALDH7A1]] | C | LRRCC1 activity lowers ALDH7A1's level | lines that do not express LRRCC1 (4) vs lines expressing it (46) | 3.18× higher at baseline in the lines without LRRCC1 | 0.023 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent |
| cells under [[Sulfatinib (drug)]] 5 µM | C | LRRCC1, [[OXR1]] activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.72× the cells of the other lines | 0.025 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| cells under [[Harringtonine (drug)]] 0.5 µM | C | LRRCC1, [[OXR1]] activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.38× the cells of the other lines | 0.032 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| cells under [[Entrectinib (drug)]] 5 µM | C | LRRCC1, [[OXR1]] activity lowers the cells' numbers under Entrectinib 5 µM (makes them more sensitive) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 1.28× the cells of the other lines | 0.038 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| cells under [[Rimonabant (drug)]] 5 µM | C | LRRCC1, [[OXR1]] activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 1.20× the cells of the other lines | 0.039 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| cells under [[Entecavir (monohydrate) (drug)]] 0.5 µM | C | LRRCC1, [[OXR1]] activity raises the cells' numbers under Entecavir (monohydrate) 0.5 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.72× the cells of the other lines | 0.039 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| [[HAUS1]] | C | LRRCC1 activity lowers HAUS1's level | lines that do not express LRRCC1 (4) vs lines expressing it (46) | 2.07× higher at baseline in the lines without LRRCC1 | 0.040 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | LRRCC1, [[OXR1]] activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.79× the cells of the other lines | 0.042 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.526). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-27.1, -37.5); signed map (-34.0, -35.4). **Vector** length 81.9, 18.7% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +7.6 | +15.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +6.8 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +6.2 | +11.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.8 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.7 | +3.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.5 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +3.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -6.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.7 | -5.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.6 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -8.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat and coiled-coil centrosomal protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.2 — chr8:85,107,215-85,146,080 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1764, CLERC, VFL1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C099](https://www.uniprot.org/uniprotkb/Q9C099) (Leucine-rich repeat and coiled-coil domain-containing protein 1):

> Required for the organization of the mitotic spindle. Maintains the structural integrity of centrosomes during mitosis.

**Summary**, from NCBI Gene [85444](https://www.ncbi.nlm.nih.gov/gene/85444):

> This gene encodes a centrosomal protein that maintains the structural integrity of the centrosome and plays a key role in mitotic spindle formation. The encoded protein contains an N-terminal leucine-rich repeat domain and a C-terminal coiled-coil domain. It associates with the centrosome throughout the cell cycle and accumulates on the mitotic centrosome. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:29373](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29373) · Entrez [85444](https://www.ncbi.nlm.nih.gov/gene/85444) · UniProt [Q9C099](https://www.uniprot.org/uniprotkb/Q9C099) · Ensembl [ENSG00000133739](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133739)

## Data

Gene col 5471: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5471); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5471, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5471]; `tensor/DDL_lfc|DDL_z.npy` [5471]; `embed/gene_vectors.npy` [5471]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5471 or target_col == 5471). Every well: [[LRRCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
