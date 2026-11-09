---
symbol: "SPTSSA"
type: "gene"
col: 9113
ensembl_id: "ENSG00000165389"
name: "serine palmitoyltransferase small subunit A"
location: "14q13.1"
module: 139
arm: "+"
pooled_cpm: 55.01
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# SPTSSA

*serine palmitoyltransferase small subunit A* — 14q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.83× (z +9.8, q 5e-20, up in 38 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.53× (z +5.9, q 7e-07, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.376× (z -5.0, q 3e-04, down in 41 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.327×; ⚠ cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H1573 0.205×; ⚠ cell-cycle shift, explains ~21% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (A-427 0.126×).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIFR]] (+0.58, fdr 3e-05), [[PHF20]] (+0.56, fdr 2e-05), [[RIC1]] (+0.55, fdr 6e-05); moves opposite to [[ALKBH6]] (-0.52, fdr 4e-05), [[EAF1]] (-0.50, fdr 8e-05), [[VPS52]] (-0.49, fdr 2e-04).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9113.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.83×** | +9.8 | 5e-20 | 38/40 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.89×** | +8.6 | 2e-15 | 45/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +5.9 | 7e-07 | 41/48 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.81×** | +5.4 | 1e-05 | 33/43 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.68×** | +5.1 | 4e-05 | 38/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +5.0 | 5e-05 | 35/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.60×** | +4.6 | 3e-04 | 35/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.55×** | +4.3 | 0.001 | 37/48 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.53×** | +4.2 | 0.002 | 34/46 (NCI-H2030, SW1417, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.028 | 23/48 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **1.42×** | +3.5 | 0.028 | 26/47 (HT-29, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.044 | 35/48 (SNU-423, HepG2/C3A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.38×** | +3.2 | 0.066 | 29/48 (BT-474, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9113.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.327×; ⚠ cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H1573 0.205×; ⚠ cell-cycle shift, explains ~21% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (A-427 0.126×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.376×** | -5.0 | 3e-04 | 41/49 (A-427, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.546× | -3.1 | 0.40 | 27/48 (LS 180, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9113. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 61.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.63× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.44× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 155 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.73× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.205× (z -10.7) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A-427 (line)]] | wt | 118 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -12.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.126× (z -8.5) |
| [[BT-474 (line)]] | alt | 144 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.57× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 90.4 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.13× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 34.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RPMI-7951 (line)]] | alt | 50.1 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.60× (z +8.9) | — |
| [[SW480 (line)]] | alt | 39.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A-172 (line)]] | wt | 42.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[C32 (line)]] | wt | 115 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[CFPAC-1 (line)]] | alt | 52.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.27× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 33.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HepG2_C3A (line)]] | wt | 79.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.69× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 47.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HT-29 (line)]] | alt | 35.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.62× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.55× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LS 180 (line)]] | wt | 63.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW 900 (line)]] | alt | 44.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.61× (z +9.1) | — |
| [[A498 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9113), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIFR]] | +0.58 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[PHF20]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[RIC1]] | +0.55 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[COX5A]] ⚠ | +0.53 | +0.61 / +0.39 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SAA1]] | +0.52 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[BIRC3]] | +0.52 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[SLC25A4]] | +0.52 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[SAA2]] | +0.51 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[COX7B]] | +0.50 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[EGLN3]] | +0.49 | +0.41 / +0.50 | both halves | 4e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PAG1]] | +0.49 | +0.30 / +0.43 | both halves | 2e-04 |  |
| [[TXNIP]] | +0.48 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[CCDC88A]] | +0.48 | +0.45 / +0.37 | both halves | 7e-05 |  |
| [[CCL20]] | +0.48 | +0.42 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH6]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[EAF1]] | -0.50 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[VPS52]] | -0.49 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[SETD4]] | -0.48 | -0.24 / -0.45 | both halves | 4e-04 |  |
| [[PLXNB3-AS1]] | -0.47 | -0.19 / -0.50 | ⚠ not reproduced | 8e-04 |  |
| [[PRR3]] | -0.47 | -0.24 / -0.27 | both halves | 4e-04 |  |
| [[EIF3F]] | -0.47 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[SMARCAL1]] | -0.47 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[RAE1]] | -0.47 | -0.29 / -0.36 | both halves | 2e-04 |  |
| [[EXOC7]] | -0.47 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[GATB]] | -0.46 | -0.20 / -0.48 | both halves | 7e-04 |  |
| [[TCTN1]] | -0.46 | -0.12 / -0.53 | ⚠ one half (not replicated) | 0.002 |  |
| [[UROD]] | -0.46 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[C1D]] | -0.45 | -0.40 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.5, 3.1); signed map (-10.4, 18.6). **Vector** length 92.7, 28.6% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.2 | +0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +1.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.9 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.9 | -2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.3 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -4.1 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | serine palmitoyltransferase small subunit A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.1 — chr14:34,432,788-34,462,240 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ssSPTa; previously C14orf147 |
| Gene groups (HGNC) | Serine palmitoyltransferase small subunits |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969W0](https://www.uniprot.org/uniprotkb/Q969W0) (Serine palmitoyltransferase small subunit A):

> Component of the serine palmitoyltransferase multisubunit enzyme (SPT) that catalyzes the initial and rate-limiting step in sphingolipid biosynthesis by condensing L-serine and activated acyl-CoA (most commonly palmitoyl-CoA) to form long-chain bases. The SPT complex is composed of SPTLC1, SPTLC2 or SPTLC3 and SPTSSA or SPTSSB. Within this complex, the heterodimer consisting of SPTLC1 and SPTLC2/SPTLC3 forms the catalytic core. Within the SPT complex, SPTSSA stimulates the catalytic activity …

**Summary**, from NCBI Gene [171546](https://www.ncbi.nlm.nih.gov/gene/171546):

> Serine palmitoyltransferase (SPT; EC 2.3.1.50) catalyzes the first committed and rate-limiting step in sphingolipid biosynthesis. SSSPTA is a small SPT subunit that stimulates SPT activity and confers acyl-CoA preference to the SPT catalytic heterodimer of SPTLC1 (MIM 605712) and either SPTLC2 (MIM 605713) or SPTLC3 (MIM 611120) (Han et al., 2009 [PubMed 19416851]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:20361](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20361) · Entrez [171546](https://www.ncbi.nlm.nih.gov/gene/171546) · UniProt [Q969W0](https://www.uniprot.org/uniprotkb/Q969W0) · Ensembl [ENSG00000165389](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165389)

## Data

Gene col 9113: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9113); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9113, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9113]; `tensor/DDL_lfc|DDL_z.npy` [9113]; `embed/gene_vectors.npy` [9113]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9113 or target_col == 9113). Every well: [[SPTSSA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPTSSA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
