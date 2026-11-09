---
symbol: "ALDOC"
type: "gene"
col: 3029
ensembl_id: "ENSG00000109107"
name: "aldolase, fructose-bisphosphate C"
location: "17q11.2"
module: 79
arm: "+"
pooled_cpm: 39.63
n_lines_expressing: 43
n_dd_up: 5
n_dd_down: 40
n_dd_up_clean: 5
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# ALDOC

*aldolase, fructose-bisphosphate C* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Berbamine (drug)]] 5 µM: 1.55× (z +6.3, q 2e-07, up in 35 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.227× (z -21.0, q 0e+00, down in 40 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFNA4]] (+0.74, fdr 7e-06), [[EFNA3]] (+0.74, fdr 7e-06), [[ABCB9]] (+0.71, fdr 7e-06); moves opposite to [[AVEN]] (-0.66, fdr 1e-05), [[ZMYND11]] (-0.63, fdr 3e-05), [[ZMPSTE24]] (-0.62, fdr 3e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[AKR7A2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3029.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berbamine (drug)]] 5 µM |  | **1.55×** | +6.3 | 2e-07 | 35/42 (LoVo, A549, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.48×** | +5.6 | 6e-06 | 34/41 (LoVo, HT-29, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.60×** | +4.7 | 4e-04 | 28/41 (A549, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +4.1 | 0.005 | 21/41 (A498, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +4.0 | 0.009 | 23/41 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 1.40× | +3.2 | 0.12 | 21/41 (A549, C32, …) | top dose only | plate-row cell shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.35× | +3.0 | 0.20 | 18/41 (SW480, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3029.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.227×** | -21.0 | 0e+00 | 40/41 (LOX-IMVI, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.176×** | -16.8 | 0e+00 | 37/41 (LOX-IMVI, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.195×** | -16.4 | 0e+00 | 41/41 (KATO III, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.242×** | -13.7 | 1e-40 | 35/38 (LOX-IMVI, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.346×** | -9.9 | 6e-21 | 31/36 (SW1417, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.413×** | -8.6 | 1e-15 | 29/34 (SW1417, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.553×** | -8.4 | 3e-15 | 34/40 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.438×** | -8.3 | 7e-15 | 25/38 (SW1417, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.453×** | -7.9 | 1e-13 | 32/41 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.492×** | -7.1 | 6e-11 | 34/41 (MIA PaCa-2, HCT15, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.492×** | -6.9 | 4e-10 | 33/41 (KATO III, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.625×** | -6.7 | 1e-09 | 37/41 (NCI-H460, SNU-1, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.223×** | -6.5 | 4e-09 | 32/41 (RKO, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.523×** | -6.3 | 1e-08 | 29/41 (H4, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.247×** | -6.0 | 6e-08 | 31/42 (SNU-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.566×** | -5.4 | 2e-06 | 30/41 (LOX-IMVI, SW1417, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.597×** | -5.2 | 7e-06 | 31/41 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.604×** | -5.1 | 1e-05 | 30/41 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.645×** | -4.4 | 3e-04 | 24/41 (SW 900, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3029. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 155 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -24.2) |
| [[LOX-IMVI (line)]] | wt | 74.3 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0763× (z -28.9) |
| [[NCI-H460 (line)]] | wt | 55.4 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -15.8) |
| [[SNU-1 (line)]] | wt | 105 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0584× (z -26.3) |
| [[SW1417 (line)]] | alt | 49.1 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0951× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.301× (z -12.7) |
| [[HCT15 (line)]] | alt | 37.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0514× (z -14.6) |
| [[Hs 766T (line)]] | wt | 50.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 32.9 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.128× (z -11.8) |
| [[RKO (line)]] | wt | 61.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0845× (z -23.7) |
| [[RPMI-7951 (line)]] | alt | 47.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -16.4) |
| [[SW480 (line)]] | alt | 19.7 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0822× (z -16.1) |
| [[A549 (line)]] | wt | 26.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -16.7) |
| [[CFPAC-1 (line)]] | alt | 77.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -12.3) |
| [[HT-29 (line)]] | alt | 57.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -18.0) |
| [[LoVo (line)]] | wt | 27.3 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0365× (z -20.9) |
| [[NCI-H1792 (line)]] | alt | 103 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -13.7) |
| [[PANC-1 (line)]] | alt | 25.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.125× (z -13.7) |
| [[SNU-423 (line)]] | alt | 40.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -16.7) |
| [[SW 900 (line)]] | alt | 44.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -20.2) |
| [[NCI-H1573 (line)]] | alt | 32.4 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.176× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 82.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -13.0) |
| [[C32 (line)]] | wt | 66.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 52.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -18.3) |
| [[LS 180 (line)]] | wt | 78.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -14.7) |
| [[Panc 03.27 (line)]] | alt | 33.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -12.3) |
| [[SW48 (line)]] | wt | 49.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0365× (z -26.7) |
| [[A-172 (line)]] | wt | 10.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 30.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -8.7) |
| [[COLO 205 (line)]] | alt | 70.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.115× (z -13.1) |
| [[H4 (line)]] | wt | 16.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 28.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0674× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.179× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 20.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -13.9) |
| [[A498 (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -11.2) ⚠ toxic |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0784× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 13.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -9.4) |
| [[SHP-77 (line)]] | alt | 49.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -16.2) |
| [[SW 1088 (line)]] | alt | 56.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0633× (z -11.9) |
| [[A-427 (line)]] | wt | 4.57 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.73 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.79 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 36.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3029), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFNA4]] | +0.74 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[EFNA3]] | +0.74 | +0.67 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[ABCB9]] | +0.71 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[HILPDA]] | +0.70 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[VKORC1]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[PDK3]] | +0.68 | +0.70 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 419 |
| [[CNOT8]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ENO2]] | +0.67 | +0.69 / +0.57 | both halves | 9e-06 | pathway: HALLMARK_HYPOXIA; STRING 957 |
| [[PFKFB4]] | +0.67 | +0.67 / +0.54 | both halves | 1e-05 | pathway: Glucose metabolism; STRING 578 |
| [[ZNF511]] | +0.66 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[C4orf3]] | +0.66 | +0.68 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVEN]] | -0.66 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.63 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[ZMPSTE24]] | -0.62 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[PSME3IP1]] | -0.61 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[DPH5-DT]] | -0.60 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[ITPA]] | -0.60 | -0.56 / -0.35 | both halves | 1e-04 | STRING 401 |
| [[MAPKAPK5]] | -0.60 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[LTO1]] | -0.59 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[ARRDC3-AS1]] | -0.58 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[FAIM]] | -0.58 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[ST7L]] | -0.58 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[PIEZO1]] | -0.57 | -0.35 / -0.58 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ALDOC's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR7A2]] | B | ALDOC activity lowers AKR7A2's level | lines that do not express ALDOC (7) vs lines expressing it (43) | 1.61× higher at baseline in the lines without ALDOC | 0.084 | ⚠ within organs, on part of the lines |
| [[CFLAR]] | B | ALDOC activity raises CFLAR's level | lines that do not express ALDOC (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without ALDOC | 0.095 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.724). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.5, -14.3); signed map (-34.2, 21.6). **Vector** length 136, 44.5% of its response variance represented; |z| ≥ 3 in 1,193 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.55 to 5); *glycolysis* (hallmark, mean cos +0.55 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +8.7 | +4.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +8.2 | +4.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +7.3 | +3.0 |
|  | [[Berbamine (drug)]] 5 µM |  | +4.8 | +6.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.9 | +5.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.9 | +4.7 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.2 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -10.0 | -8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.6 | -9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.3 | -8.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.4 | -6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.3 | -6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.2 | -7.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.2 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | aldolase, fructose-bisphosphate C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,573,115-28,576,948 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Endoribonucleases; Aldolase, fructose-bisphosphate family |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, HYPOXIA |
| Reactome | 6 pathways, smallest: Gluconeogenesis; Glycolysis; Glucose metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P09972](https://www.uniprot.org/uniprotkb/P09972) (Fructose-bisphosphate aldolase C):

> Catalyzes the reversible conversion of beta-D-fructose 1,6-bisphosphate (FBP) into two triose phosphate and plays a key role in glycolysis and gluconeogenesis.

**Summary**, from NCBI Gene [230](https://www.ncbi.nlm.nih.gov/gene/230):

> This gene encodes a member of the class I fructose-biphosphate aldolase gene family. Expressed specifically in the hippocampus and Purkinje cells of the brain, the encoded protein is a glycolytic enzyme that catalyzes the reversible aldol cleavage of fructose-1,6-biphosphate and fructose 1-phosphate to dihydroxyacetone phosphate and either glyceraldehyde-3-phosphate or glyceraldehyde, respectively. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:418](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:418) · Entrez [230](https://www.ncbi.nlm.nih.gov/gene/230) · UniProt [P09972](https://www.uniprot.org/uniprotkb/P09972) · Ensembl [ENSG00000109107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109107)

## Data

Gene col 3029: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3029); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3029, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3029]; `tensor/DDL_lfc|DDL_z.npy` [3029]; `embed/gene_vectors.npy` [3029]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3029 or target_col == 3029). Every well: [[ALDOC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDOC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
