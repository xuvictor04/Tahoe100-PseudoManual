---
symbol: "OAZ1"
type: "gene"
col: 2522
ensembl_id: "ENSG00000104904"
name: "ornithine decarboxylase antizyme 1"
location: "19p13.3"
module: 5
arm: "-"
pooled_cpm: 116.46
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# OAZ1

*ornithine decarboxylase antizyme 1* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.67× (z +10.6, q 2e-23, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.00× (z +5.6, q 3e-06, up in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 14 lines (C32 6.34×, NCI-H460 6.00×, HOP62 5.10×, SW480 4.30×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (C32 4.15×, LoVo 3.44×); [[Dinaciclib (drug)]] 5 µM in 1 line (C32 4.75×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (79 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2B]] (+0.64, fdr 3e-05), [[HDAC5]] (+0.61, fdr 2e-05), [[MKNK2]] (+0.60, fdr 2e-04); moves opposite to [[ALG8]] (-0.69, fdr 4e-05), [[PIGW]] (-0.63, fdr 2e-04), [[MCM3AP]] (-0.62, fdr 9e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2522.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 14 lines (C32 6.34×, NCI-H460 6.00×, HOP62 5.10×, SW480 4.30×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (C32 4.15×, LoVo 3.44×); [[Dinaciclib (drug)]] 5 µM in 1 line (C32 4.75×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.67×** | +10.6 | 2e-23 | 49/49 (C32, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.81×** | +8.1 | 2e-13 | 43/44 (C32, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.26×** | +5.7 | 2e-06 | 42/45 (C32, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.00×** | +5.6 | 3e-06 | 41/48 (C32, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +5.4 | 7e-06 | 45/47 (NCI-H2030, C32, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.93×** | +5.2 | 2e-05 | 40/47 (SHP-77, COLO 205, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.88×** | +5.1 | 2e-05 | 46/48 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.85×** | +5.0 | 4e-05 | 46/48 (SHP-77, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.67×** | +4.2 | 0.002 | 35/48 (NCI-H460, SW48, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **1.61×** | +3.9 | 0.006 | 40/48 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.51×** | +3.3 | 0.041 | 34/48 (AN3 CA, C-33 A, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +3.3 | 0.041 | 31/48 (C32, NCI-H1792, …) | rises with dose | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.041 | 34/48 (LOX-IMVI, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2522.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Hydroxyurea (drug)]] 5 µM |  | 0.661× | -3.3 | 0.32 | 41/48 (CHP-212, RKO, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.757× | -3.2 | 0.32 | 35/48 (RPMI-7951, hTERT-HPNE, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.478× | -3.1 | 0.32 | 41/49 (RKO, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2522. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 97.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.34× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.15× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 58.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HOP62 (line)]] | alt | 100 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LoVo (line)]] | wt | 116 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.44× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 79.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1792 (line)]] | alt | 60.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW480 (line)]] | alt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 154 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A498 (line)]] | wt | 168 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A549 (line)]] | wt | 48.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.87× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[C-33 A (line)]] | alt | 73.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HEC-1-A (line)]] | alt | 117 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Hs 766T (line)]] | wt | 98.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HS-578T (line)]] | alt | 197 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HT-29 (line)]] | alt | 132 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[KATO III (line)]] | alt | 93.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 168 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 127 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RPMI-7951 (line)]] | alt | 140 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 128 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-427 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 96.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 86.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 146 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 120 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 184 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 129 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 99.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 152 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2522), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*27 of its nearest partners move with it, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2B]] | +0.64 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[HDAC5]] | +0.61 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[MKNK2]] | +0.60 | +0.29 / +0.58 | both halves | 2e-04 |  |
| [[CAMSAP3]] | +0.59 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[SYP]] | +0.59 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[RNF114]] | +0.59 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[CCDC88B]] | +0.58 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[KBTBD3]] | +0.58 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[GABARAPL2]] | +0.58 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[KRT10]] ⚠ | +0.56 | +0.36 / +0.56 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[JUND]] | +0.56 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[GPX4]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CDKN2D]] | +0.55 | +0.42 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*73 of its nearest partners move opposite, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG8]] | -0.69 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[PIGW]] | -0.63 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[MCM3AP]] | -0.62 | -0.37 / -0.63 | both halves | 9e-05 |  |
| [[SUV39H2]] | -0.62 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[MAPKAPK5]] | -0.61 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[UTP4]] | -0.61 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[E2F3]] | -0.60 | -0.36 / -0.57 | both halves | 9e-05 |  |
| [[QTRT1]] | -0.60 | -0.17 / -0.67 | ⚠ one half (not replicated) | 0.001 |  |
| [[ECHDC1]] | -0.59 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[CPSF3]] | -0.59 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[EIF2S1]] | -0.58 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[TOMM40]] | -0.57 | -0.48 / -0.67 | both halves | 2e-05 |  |
| [[ARMC6]] | -0.57 | -0.31 / -0.64 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.594). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (2.0, -48.7); signed map (-25.4, 18.8). **Vector** length 63.7, 23.0% of its response variance represented; |z| ≥ 3 in 653 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +1.9 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +1.8 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +1.8 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.6 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -3.5 | +10.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -3.3 | +8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | +0.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -0.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.5 | +0.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | ornithine decarboxylase antizyme 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,269,509-2,273,490 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AZI, MGC138338, AZ1; previously OAZ |
| Gene groups (HGNC) | Ornithine decarboxylase antizyme family |
| Reactome | 3 pathways, smallest: Regulation of ornithine decarboxylase (ODC); Metabolism of polyamines; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P54368](https://www.uniprot.org/uniprotkb/P54368) (Ornithine decarboxylase antizyme 1):

> Ornithine decarboxylase (ODC) antizyme protein that negatively regulates ODC activity and intracellular polyamine biosynthesis and uptake in response to increased intracellular polyamine levels. Binds to ODC monomers, inhibiting the assembly of the functional ODC homodimer, and targets the monomers for ubiquitin-independent proteolytic destruction by the 26S proteasome. Triggers ODC degradation by inducing the exposure of a cryptic proteasome-interacting surface of ODC. Stabilizes AZIN2 by …

**Summary**, from NCBI Gene [4946](https://www.ncbi.nlm.nih.gov/gene/4946):

> The protein encoded by this gene belongs to the ornithine decarboxylase antizyme family, which plays a role in cell growth and proliferation by regulating intracellular polyamine levels. Expression of antizymes requires +1 ribosomal frameshifting, which is enhanced by high levels of polyamines. Antizymes in turn bind to and inhibit ornithine decarboxylase (ODC), the key enzyme in polyamine biosynthesis; thus, completing the auto-regulatory circuit. This gene encodes antizyme 1, the first member …

**Accessions** — [HGNC:8095](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8095) · Entrez [4946](https://www.ncbi.nlm.nih.gov/gene/4946) · UniProt [P54368](https://www.uniprot.org/uniprotkb/P54368) · Ensembl [ENSG00000104904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104904)

## Data

Gene col 2522: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2522); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2522, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2522]; `tensor/DDL_lfc|DDL_z.npy` [2522]; `embed/gene_vectors.npy` [2522]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2522 or target_col == 2522). Every well: [[OAZ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OAZ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
