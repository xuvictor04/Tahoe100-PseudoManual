---
symbol: "SPRING1"
type: "gene"
col: 3231
ensembl_id: "ENSG00000111412"
name: "SREBF pathway regulator in golgi 1"
location: "12q24.22"
module: 50
arm: "+"
pooled_cpm: 21.16
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# SPRING1

*SREBF pathway regulator in golgi 1* — 12q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.31× (z +21.4, q 0e+00, up in 46 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A549 0.165×, A-172 0.214×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (HT-29 0.335×, SW 900 0.256×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.212×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0744×); [[Triamcinolone (drug)]] 0.5 µM in 1 line (H4 0.0699×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLB1]] (+0.61, fdr 1e-05), [[TMEM127]] (+0.60, fdr 1e-05), [[GNPTG]] (+0.60, fdr 2e-05); moves opposite to [[ANKRD26]] (-0.57, fdr 5e-05), [[LRRC37A2]] (-0.50, fdr 2e-04), [[HIRIP3]] (-0.49, fdr 4e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3231.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.31×** | +21.4 | 0e+00 | 46/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.85×** | +18.8 | 0e+00 | 43/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.47×** | +16.2 | 0e+00 | 42/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +11.7 | 3e-29 | 40/47 (HT-29, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.80×** | +10.5 | 1e-23 | 37/47 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +9.2 | 5e-18 | 27/46 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +8.9 | 6e-17 | 30/46 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +8.4 | 2e-15 | 33/47 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +7.8 | 5e-13 | 31/47 (CFPAC-1, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +7.7 | 1e-12 | 28/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +7.5 | 3e-12 | 30/47 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +7.5 | 4e-12 | 30/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +7.4 | 7e-12 | 29/48 (NCI-H2347, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +7.0 | 9e-11 | 25/44 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.01×** | +6.5 | 2e-09 | 28/48 (COLO 205, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.2 | 2e-08 | 25/46 (SNU-423, LS 180, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +5.3 | 4e-06 | 22/47 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.74×** | +5.2 | 6e-06 | 19/45 (NCI-H2347, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3231.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A549 0.165×, A-172 0.214×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (HT-29 0.335×, SW 900 0.256×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.212×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0744×); [[Triamcinolone (drug)]] 0.5 µM in 1 line (H4 0.0699×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.847× | -3.0 | 0.75 | 2/47 (NCI-H23, HT-29) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3231. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 20.4 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.01× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 21.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.53× (z +13.3) | — |
| [[A549 (line)]] | wt | 15.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.36× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[NCI-H460 (line)]] | wt | 13.3 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.12× (z +10.0) | — |
| [[SW480 (line)]] | alt | 14.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.01× (z +14.7) | — |
| [[A-427 (line)]] | wt | 27.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A498 (line)]] | wt | 7.65 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 55.1 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.53× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 50.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.69× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 18.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.33× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 12.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.66× (z +9.6) | — |
| [[A-172 (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[AsPC-1 (line)]] | alt | 16.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.82× (z +9.2) | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0699× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 17.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.36× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 10.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 27.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.85× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.31× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0744× (z -11.6) |
| [[SW 900 (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 25.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3231), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLB1]] | +0.61 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[TMEM127]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[GNPTG]] | +0.60 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[ILRUN]] | +0.59 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ASAH1]] | +0.56 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[GM2A]] | +0.56 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[ZDHHC16]] | +0.56 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[CIPC]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[CPSF4]] | +0.54 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[SNN]] | +0.54 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[ESYT1]] | +0.53 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[SPNS1]] | +0.53 | +0.55 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD26]] | -0.57 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[LRRC37A2]] | -0.50 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[HIRIP3]] | -0.49 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[HMGXB4]] | -0.49 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[DZIP3]] | -0.49 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[H3-3B]] | -0.47 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[CETN3]] | -0.46 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[NBPF10]] | -0.46 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[FAN1]] | -0.46 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[HELQ]] | -0.45 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[NEPRO-AS1]] | -0.45 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[C1orf131]] | -0.45 | -0.41 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.521). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.6, -17.5); signed map (-49.4, -9.6). **Vector** length 69.2, 12.4% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.8 | +11.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.4 | +7.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.8 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +2.9 | +5.9 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.4 | +1.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +3.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | -1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | +1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.1 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | SREBF pathway regulator in golgi 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.22 — chr12:116,710,171-116,738,070 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21415, SPRING, POST1, LUR1; previously C12orf49 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H741](https://www.uniprot.org/uniprotkb/Q9H741) (SREBP regulating gene protein):

> Positively regulates hepatic SREBP signaling pathway by modulating the proper localization of SCAP (SREBP cleavage-activating protein) to the endoplasmic reticulum, thereby controlling the level of functional SCAP.

**Summary**, from NCBI Gene [79794](https://www.ncbi.nlm.nih.gov/gene/79794):

> Involved in positive regulation of SREBP signaling pathway. Located in Golgi membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26128](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26128) · Entrez [79794](https://www.ncbi.nlm.nih.gov/gene/79794) · UniProt [Q9H741](https://www.uniprot.org/uniprotkb/Q9H741) · Ensembl [ENSG00000111412](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111412)

## Data

Gene col 3231: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3231); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3231, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3231]; `tensor/DDL_lfc|DDL_z.npy` [3231]; `embed/gene_vectors.npy` [3231]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3231 or target_col == 3231). Every well: [[SPRING1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPRING1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
