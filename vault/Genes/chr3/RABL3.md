---
symbol: "RABL3"
type: "gene"
col: 6936
ensembl_id: "ENSG00000144840"
name: "RAB, member of RAS oncogene family like 3"
location: "3q13.33"
module: 83
arm: "+"
pooled_cpm: 32.49
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# RABL3

*RAB, member of RAS oncogene family like 3* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.82× (z +11.3, q 1e-26, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.515× (z -12.5, q 5e-33, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP16]] (+0.78, fdr 7e-06), [[TRMO]] (+0.74, fdr 7e-06), [[LANCL2]] (+0.70, fdr 1e-05); moves opposite to [[TBC1D12]] (-0.62, fdr 7e-06), [[MMS19]] (-0.61, fdr 2e-05), [[TSEN54]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6936.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +11.3 | 1e-26 | 41/48 (NCI-H2347, Panc 03.27, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +9.7 | 9e-20 | 32/47 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +8.7 | 8e-16 | 33/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.1 | 1e-07 | 26/48 (A-427, SNU-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +5.8 | 1e-06 | 26/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +5.6 | 2e-06 | 20/40 (NCI-H23, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +5.3 | 9e-06 | 28/48 (LoVo, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +5.1 | 2e-05 | 20/49 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +4.8 | 1e-04 | 24/48 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +4.7 | 1e-04 | 22/48 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.5 | 3e-04 | 16/34 (Hs 766T, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.25×** | +4.2 | 0.001 | 20/47 (NCI-H1573, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.010 | 22/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.3 | 0.042 | 14/42 (A-427, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.059 | 9/48 (C32, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6936.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.515×** | -12.5 | 5e-33 | 47/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.571×** | -10.5 | 1e-23 | 42/48 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.617×** | -8.7 | 4e-16 | 35/47 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.658×** | -7.9 | 5e-13 | 38/48 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.681×** | -7.2 | 5e-11 | 35/48 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -7.1 | 1e-10 | 30/47 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.710×** | -6.4 | 9e-09 | 30/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.780×** | -4.5 | 5e-04 | 23/48 (LS 180, SW480, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.620×** | -4.3 | 9e-04 | 17/48 (RPMI-7951, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.797×** | -4.1 | 0.002 | 20/47 (HS-578T, SW 1271, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6936. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 31.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.338× (z -10.2) ⚠ toxic |
| [[SW480 (line)]] | alt | 37.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.495× (z -8.7) |
| [[HT-29 (line)]] | alt | 47.4 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.117× (z -9.9) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 28.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 29.0 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.1) |
| [[A-172 (line)]] | wt | 36.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.191× (z -9.3) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 58.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.306× (z -9.6) |
| [[HOP62 (line)]] | alt | 30.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -9.2) |
| [[LoVo (line)]] | wt | 41.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 20.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 50.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[NCI-H1573 (line)]] | alt | 22.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +12.8) | — |
| [[NCI-H1792 (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -8.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 35.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.251× (z -10.4) ⚠ toxic |
| [[SW 900 (line)]] | alt | 26.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +8.6) | — |
| [[A-427 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6936), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP16]] | +0.78 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[TRMO]] | +0.74 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[LANCL2]] | +0.70 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[TAF2]] | +0.68 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[DNAJB12]] | +0.68 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[PPP4R3B]] | +0.66 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[NUBP1]] | +0.66 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[TRMT10A]] | +0.64 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[UBE2D3-AS1]] | +0.63 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ZNF546]] | +0.63 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[COQ7]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[SNAPC5]] | +0.63 | +0.56 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D12]] | -0.62 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[MMS19]] | -0.61 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[TSEN54]] | -0.60 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[FLYWCH2]] | -0.59 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[METAP1]] | -0.57 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[ORC4]] | -0.57 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[PXK]] | -0.57 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[OSTF1]] | -0.57 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[KIF3A]] | -0.56 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[LPCAT4]] | -0.56 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[FBXO31]] | -0.56 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[SLC9A6]] | -0.56 | -0.50 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises RABL3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.569). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-23.2, 11.1); signed map (12.6, -29.7). **Vector** length 105, 24.6% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.6 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +6.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +0.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.6 | +2.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.0 | -8.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.3 | -12.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.2 | -7.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.6 | -6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -7.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Tomivosertib (drug)]] 5 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | RAB, member of RAS oncogene family like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:120,684,938-120,742,993 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC23920 |
| Gene groups (HGNC) | RAB like GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5HYI8](https://www.uniprot.org/uniprotkb/Q5HYI8) (Rab-like protein 3):

> Small GTPase required for KRAS signaling regulation and modulation of cell proliferation. Regulator of KRAS prenylation, and probably prenylation of other small GTPases. Required for lymphocyte development and function (By similarity). Not required for myeloid cell development (By similarity). Interacts with Rab11 to promote ciliary vesicle formation at the mother centriole, thereby regulating early ciliogenesis. The GTP-binding capacity of RABL3 is essential for ciliogenesis.

**Summary**, from NCBI Gene [285282](https://www.ncbi.nlm.nih.gov/gene/285282):

> Enables G protein activity. Involved in positive regulation of cilium assembly; regulation of Ras protein signal transduction; and regulation of protein lipidation. Predicted to be located in Golgi apparatus and centrosome. Predicted to be active in endomembrane system. Implicated in pancreatic cancer. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18072](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18072) · Entrez [285282](https://www.ncbi.nlm.nih.gov/gene/285282) · UniProt [Q5HYI8](https://www.uniprot.org/uniprotkb/Q5HYI8) · Ensembl [ENSG00000144840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144840)

## Data

Gene col 6936: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6936); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6936, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6936]; `tensor/DDL_lfc|DDL_z.npy` [6936]; `embed/gene_vectors.npy` [6936]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6936 or target_col == 6936). Every well: [[RABL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RABL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
