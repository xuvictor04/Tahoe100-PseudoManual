---
symbol: "STIP1"
type: "gene"
col: 9652
ensembl_id: "ENSG00000168439"
name: "stress induced phosphoprotein 1"
location: "11q13.1"
module: 60
arm: "+"
pooled_cpm: 87.98
n_lines_expressing: 50
n_dd_up: 54
n_dd_down: 1
n_dd_up_clean: 23
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# STIP1

*stress induced phosphoprotein 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 54 drug-doses (31 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 6.09× (z +28.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.783× (z -3.9, q 0.049, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCT5]] (+0.76, fdr 7e-06), [[TCP1]] (+0.76, fdr 7e-06), [[NUDC]] (+0.75, fdr 7e-06); moves opposite to [[SNHG9]] (-0.69, fdr 7e-06), [[TERF2IP]] (-0.66, fdr 1e-05), [[ABCA5]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DGKG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 31 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 54 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 31 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9652.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **6.09×** | +28.6 | 0e+00 | 48/48 (LoVo, BT-474, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **4.29×** | +23.0 | 0e+00 | 48/48 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.91×** | +21.6 | 0e+00 | 48/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.34×** | +18.3 | 0e+00 | 44/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.01×** | +16.5 | 0e+00 | 48/48 (CFPAC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.69×** | +15.6 | 0e+00 | 47/49 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.34×** | +13.4 | 4e-39 | 47/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.37×** | +13.1 | 2e-37 | 43/44 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.21×** | +12.6 | 2e-34 | 48/48 (SW480, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.19×** | +12.4 | 1e-33 | 45/48 (KATO III, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **4.40×** | +12.3 | 6e-33 | 43/44 (CFPAC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **2.13×** | +11.5 | 7e-29 | 45/47 (COLO 205, SHP-77, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.88×** | +11.2 | 1e-27 | 48/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.09×** | +10.8 | 2e-25 | 39/45 (A498, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.95×** | +10.6 | 1e-24 | 45/48 (SW480, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +9.2 | 1e-18 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.26×** | +9.2 | 1e-18 | 45/49 (CFPAC-1, SW1417, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.03×** | +9.2 | 2e-18 | 43/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +7.9 | 6e-14 | 42/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Infigratinib (drug)]] 5 µM |  | **2.23×** | +6.6 | 8e-10 | 42/48 (A498, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **2.16×** | +6.4 | 4e-09 | 41/47 (KATO III, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~25% here); noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.44×** | +5.7 | 2e-07 | 36/47 (HOP62, H4, …) | all doses, flat | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.75×** | +4.6 | 6e-05 | 33/48 (CFPAC-1, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.31×** | +4.1 | 6e-04 | 28/47 (NCI-H460, HOP62, …) | all doses, flat | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.002 | 25/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9652.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.783×** | -3.9 | 0.049 | 29/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 0.851× | -3.5 | 0.11 | 17/48 (LS 180, RKO, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.807× | -3.4 | 0.11 | 22/48 (KATO III, C-33 A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.861× | -3.3 | 0.11 | 17/49 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.815× | -3.3 | 0.11 | 21/49 (RKO, PANC-1, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.826× | -3.1 | 0.19 | 19/48 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 0.827× | -3.0 | 0.19 | 15/48 (hTERT-HPNE, SHP-77, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9652. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 113 | 17 (11 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.35× (z +21.1) | — |
| [[KATO III (line)]] | alt | 93.5 | 15 (11 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.30× (z +19.3) | — |
| [[NCI-H460 (line)]] | wt | 58.2 | 15 (11 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +16.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.22× (z +14.3) | — |
| [[PANC-1 (line)]] | alt | 89.8 | 15 (8 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.34× (z +16.7) | — |
| [[A549 (line)]] | wt | 61.9 | 14 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +15.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.62× (z +13.5) | — |
| [[HOP62 (line)]] | alt | 55.4 | 13 (8 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.95× (z +19.5) | — |
| [[Hs 766T (line)]] | wt | 78.8 | 13 (9 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.68× (z +17.1) | — |
| [[LoVo (line)]] | wt | 82.1 | 13 (9 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.8× (z +26.0) | — |
| [[SNU-423 (line)]] | alt | 58.0 | 11 (7 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 11.6× (z +21.0) | — |
| [[SW1417 (line)]] | alt | 129 | 11 (7 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.67× (z +18.4) | — |
| [[COLO 205 (line)]] | alt | 44.8 | 10 (6 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 15.7× (z +16.8) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 7.06× (z +12.4) | — |
| [[HS-578T (line)]] | alt | 75.5 | 10 (6 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.14× (z +18.3) | — |
| [[HT-29 (line)]] | alt | 96.4 | 10 (6 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.7× (z +24.2) | — |
| [[LS 180 (line)]] | wt | 72.7 | 10 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.61× (z +15.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 98.3 | 10 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.72× (z +19.1) | — |
| [[Panc 03.27 (line)]] | alt | 81.4 | 10 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.09× (z +19.3) | — |
| [[SW 900 (line)]] | alt | 88.5 | 10 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.72× (z +17.6) | — |
| [[A-172 (line)]] | wt | 72.0 | 9 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.51× (z +20.2) | — |
| [[HEC-1-A (line)]] | alt | 87.1 | 9 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.36× (z +20.2) | — |
| [[hTERT-HPNE (line)]] | wt | 47.6 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +14.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 7.18× (z +14.0) | — |
| [[NCI-H1573 (line)]] | alt | 58.7 | 9 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.62× (z +14.5) | — |
| [[NCI-H1792 (line)]] | alt | 40.7 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.91× (z +17.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.65× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 79.1 | 9 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.07× (z +17.6) | — |
| [[A498 (line)]] | wt | 59.4 | 8 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.97× (z +18.8) | — |
| [[CFPAC-1 (line)]] | alt | 61.5 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.28× (z +17.9) | — |
| [[NCI-H2030 (line)]] | alt | 106 | 8 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.27× (z +13.6) | — |
| [[AsPC-1 (line)]] | alt | 91.2 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.69× (z +13.6) | — |
| [[H4 (line)]] | wt | 51.0 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.83× (z +14.0) | — |
| [[J82 (line)]] | alt | 141 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.33× (z +12.4) | — |
| [[LOX-IMVI (line)]] | wt | 93.4 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.19× (z +18.2) | — |
| [[C32 (line)]] | wt | 69.2 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 14.2× (z +21.4) | — |
| [[RKO (line)]] | wt | 123 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.95× (z +21.1) | — |
| [[A-427 (line)]] | wt | 172 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.06× (z +15.3) | — |
| [[NCI-H2347 (line)]] | alt | 92.5 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.56× (z +14.3) | — |
| [[BT-474 (line)]] | alt | 224 | 4 | 0 | [[Auranofin (drug)]] 5 µM 10.7× (z +24.8) | — |
| [[C-33 A (line)]] | alt | 117 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.32× (z +13.7) | — |
| [[HCT15 (line)]] | alt | 133 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.45× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 110 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.75× (z +12.9) | — |
| [[SHP-77 (line)]] | alt | 95.5 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.34× (z +13.0) | — |
| [[SK-MEL-2 (line)]] | alt | 58.4 | 3 | 0 | [[Auranofin (drug)]] 5 µM 5.24× (z +14.6) | — |
| [[SW48 (line)]] | wt | 103 | 3 | 0 | [[Auranofin (drug)]] 5 µM 5.98× (z +14.5) | — |
| [[HepG2_C3A (line)]] | wt | 74.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.36× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 89.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 8.67× (z +15.8) | — |
| [[AN3 CA (line)]] | alt | 112 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.63× (z +12.9) | — |
| [[SW 1271 (line)]] | alt | 103 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.45× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 81.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9652), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT5]] | +0.76 | +0.75 / +0.76 | both halves | 7e-06 | STRING 978 |
| [[TCP1]] | +0.76 | +0.71 / +0.78 | both halves | 7e-06 | STRING 968 |
| [[NUDC]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 | STRING 553 |
| [[FKBP4]] | +0.75 | +0.70 / +0.79 | both halves | 7e-06 | same gene group; pathway: HALLMARK_UV_RESPONSE_UP; STRING 979 |
| [[PSMD2]] | +0.74 | +0.75 / +0.68 | both halves | 7e-06 | STRING 509 |
| [[PTGES3]] | +0.74 | +0.67 / +0.77 | both halves | 7e-06 | pathway: HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; STRING 996 |
| [[CCT3]] | +0.74 | +0.72 / +0.74 | both halves | 7e-06 | STRING 976 |
| [[HSP90AA1]] | +0.73 | +0.79 / +0.70 | both halves | 7e-06 | pathway: HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; STRING 999 |
| [[GPN1]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[CCT6A]] | +0.71 | +0.69 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 931 |
| [[HSPA8]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 | pathway: HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; STRING 999 |
| [[HSP90AA2P]] | +0.70 | +0.72 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG9]] | -0.69 | -0.62 / -0.71 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.66 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.65 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[POLR1H]] | -0.64 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[DPM3]] | -0.63 | -0.57 / -0.70 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.62 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[SELENOH]] | -0.62 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[TRAPPC6A]] | -0.62 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[TMEM258]] | -0.62 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[PHPT1]] | -0.60 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[CUTA]] | -0.60 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[SAT2]] | -0.60 | -0.60 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DGKG]] | B | DGKG activity lowers STIP1's level | lines that do not express DGKG (14) vs lines expressing it (36) | 1.28× higher at baseline in the lines without DGKG | 0.046 | ⚠ within organs, on part of the lines; also absent: CADPS2, RBPMS, SHC4; maybe low, not absent |
| [[SRPX2]] | B | SRPX2 activity lowers STIP1's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 1.37× higher at baseline in the lines without SRPX2 | 0.064 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.726). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-20.4, -12.1); signed map (-26.7, -29.7). **Vector** length 90.7, 34.5% of its response variance represented; |z| ≥ 3 in 1,771 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *The role of GTSE1 in G2/M progression after G2 checkpoint* (reactome, mean cos +0.52 to 8); *Formation of tubulin folding intermediates by CCT/TriC* (reactome, mean cos +0.59 to 5); *Hh mutants are degraded by ERAD* (reactome, mean cos +0.57 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.5 | +28.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +8.1 | +13.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.5 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +6.6 | +15.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.5 | +12.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.2 | +21.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +9.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +9.2 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | -4.5 | +9.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | -3.2 | +2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -3.0 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | +9.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.9 | +12.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -1.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.1 | -0.3 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.0 | -0.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.9 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | stress induced phosphoprotein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,185,272-64,204,543 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HOP, STI1 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Hallmark sets | UV_RESPONSE_UP, MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: RND1 GTPase cycle; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P31948](https://www.uniprot.org/uniprotkb/P31948) (Stress-induced-phosphoprotein 1):

> Acts as a co-chaperone for HSP90AA1. Mediates the association of the molecular chaperones HSPA8/HSC70 and HSP90 (By similarity).

**Summary**, from NCBI Gene [10963](https://www.ncbi.nlm.nih.gov/gene/10963):

> STIP1 is an adaptor protein that coordinates the functions of HSP70 (see HSPA1A; MIM 140550) and HSP90 (see HSP90AA1; MIM 140571) in protein folding. It is thought to assist in the transfer of proteins from HSP70 to HSP90 by binding both HSP90 and substrate-bound HSP70. STIP1 also stimulates the ATPase activity of HSP70 and inhibits the ATPase activity of HSP90, suggesting that it regulates both the conformations and ATPase cycles of these chaperones (Song and Masison, 2005 [PubMed …

**Accessions** — [HGNC:11387](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11387) · Entrez [10963](https://www.ncbi.nlm.nih.gov/gene/10963) · UniProt [P31948](https://www.uniprot.org/uniprotkb/P31948) · Ensembl [ENSG00000168439](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168439)

## Data

Gene col 9652: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9652); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9652, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9652]; `tensor/DDL_lfc|DDL_z.npy` [9652]; `embed/gene_vectors.npy` [9652]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9652 or target_col == 9652). Every well: [[STIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
