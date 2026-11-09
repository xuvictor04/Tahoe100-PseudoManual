---
symbol: "MLF1"
type: "gene"
col: 10891
ensembl_id: "ENSG00000178053"
name: "myeloid leukemia factor 1"
location: "3q25.32"
module: 83
arm: "-"
pooled_cpm: 59.68
n_lines_expressing: 45
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# MLF1

*myeloid leukemia factor 1* — 3q25.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.22× (z +12.0, q 2e-30, up in 43 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.265×, SK-MEL-2 0.322×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.266×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Belzutifan (drug)]] 5 µM in 1 line (C32 0.0387×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP210]] (+0.76, fdr 7e-06), [[RFX2]] (+0.71, fdr 7e-06), [[USP2]] (+0.67, fdr 1e-05); moves opposite to [[DNAJC11]] (-0.66, fdr 1e-05), [[MAPKAPK5]] (-0.60, fdr 1e-05), [[DNAJB14]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TRMT12]] → it (grade C ⚠); 4 go from it, the strongest it → [[GABPB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10891.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.22×** | +12.0 | 2e-30 | 43/43 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.15×** | +9.6 | 3e-19 | 43/43 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.55×** | +7.4 | 2e-11 | 43/43 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.10×** | +6.2 | 8e-08 | 40/43 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.99×** | +5.7 | 1e-06 | 34/43 (NCI-H460, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.85×** | +5.2 | 2e-05 | 33/43 (NCI-H460, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +4.8 | 1e-04 | 30/43 (SW1417, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +4.2 | 0.002 | 30/43 (SW1417, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.49×** | +4.0 | 0.004 | 36/43 (SW1417, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM |  | **1.81×** | +3.5 | 0.022 | 25/43 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.52×** | +3.5 | 0.022 | 22/43 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +3.5 | 0.025 | 25/43 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artemether (drug)]] 0.05 µM |  | **1.49×** | +3.3 | 0.040 | 26/43 (LS 180, PANC-1, …) | inconsistent across doses |  |
| [[Allopurinol (drug)]] 0.05 µM |  | **1.46×** | +3.2 | 0.057 | 25/43 (LS 180, PANC-1, …) | inconsistent across doses |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **1.45×** | +3.1 | 0.078 | 24/43 (NCI-H1573, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10891.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.265×, SK-MEL-2 0.322×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.266×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Belzutifan (drug)]] 5 µM in 1 line (C32 0.0387×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lonafarnib (drug)]] 0.05 µM |  | 0.647× | -3.4 | 0.36 | 20/43 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.765× | -3.1 | 0.37 | 27/43 (AsPC-1, HS-578T, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.770× | -3.1 | 0.37 | 22/43 (H4, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10891. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 21.9 | 8 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.80× (z +14.3) | — |
| [[SW1417 (line)]] | alt | 32.9 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 9.66× (z +15.8) | — |
| [[SW480 (line)]] | alt | 20.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.16× (z +15.2) | — |
| [[A-172 (line)]] | wt | 38.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.85× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 65.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.33× (z +10.3) | — |
| [[KATO III (line)]] | alt | 43.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.06× (z +11.1) | — |
| [[LoVo (line)]] | wt | 21.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.74× (z +11.1) | — |
| [[C32 (line)]] | wt | 28.5 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 5.00× (z +9.4) | [[Belzutifan (drug)]] 5 µM 0.0387× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 102 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.88× (z +8.7) | — |
| [[H4 (line)]] | wt | 60.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.95× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 25.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.34× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 80.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.20× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 68.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.15× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 58.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.70× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 71.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.05× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 69.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.18× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 76.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.27× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 56.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.28× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 68.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.08× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A498 (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.38 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 177 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.73 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.83 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.91 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10891), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP210]] | +0.76 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[RFX2]] | +0.71 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[USP2]] | +0.67 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[OSR2]] | +0.66 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[NUP62CL]] | +0.66 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[MAK]] | +0.62 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[STARD5]] | +0.61 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[EFHC1]] | +0.60 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[BZW2]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[AFMID]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[PPP1R2]] | +0.57 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[WDR47]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC11]] | -0.66 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[MAPKAPK5]] | -0.60 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[DNAJB14]] | -0.60 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[RRP36]] | -0.59 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[LTO1]] | -0.58 | -0.51 / -0.43 | both halves | 4e-05 |  |
| [[ZNF629]] | -0.57 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[WDR33]] | -0.57 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[NACC1]] | -0.56 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[MTG2]] | -0.56 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[SCO1]] | -0.56 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[GTF2E1]] | -0.55 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[TRMT12]] | -0.55 | -0.52 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRMT12]] | C | TRMT12 activity raises MLF1's level | lines that do not express TRMT12 (3) vs lines expressing it (47) | 3.84× lower at baseline in the lines without TRMT12 | 0.051 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000283491, MBOAT2, TRIM68 |
| [[CDON]] | C | CDON activity raises MLF1's level | lines that do not express CDON (3) vs lines expressing it (47) | 2.28× lower at baseline in the lines without CDON | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ATP6V0E2, DBNDD1, NAT14; maybe low, not absent; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABPB1]] | B | MLF1 activity lowers GABPB1's level | lines that do not express MLF1 (5) vs lines expressing it (45) | 1.45× higher at baseline in the lines without MLF1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CCDC110, MLH1, ITGA3; its own permutation p |
| [[DPP8]] | B | MLF1 activity raises DPP8's level | lines that do not express MLF1 (5) vs lines expressing it (45) | 1.18× lower at baseline in the lines without MLF1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CCDC110, MLH1, ITGA3; its own permutation p |
| [[YTHDF2]] | B | MLF1 activity lowers YTHDF2's level | lines that do not express MLF1 (5) vs lines expressing it (45) | 1.34× higher at baseline in the lines without MLF1 | 0.077 | ⚠ within organs, on part of the lines; also absent: CCDC110, MLH1, ITGA3 |
| [[PPDPF]] | B | MLF1 activity raises PPDPF's level | lines that do not express MLF1 (5) vs lines expressing it (45) | 1.80× lower at baseline in the lines without MLF1 | 0.095 | ⚠ within organs, on part of the lines; also absent: CCDC110, MLH1, ITGA3 |

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (12.5, -9.9); signed map (-0.6, 19.1). **Vector** length 120, 41.1% of its response variance represented; |z| ≥ 3 in 729 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +3.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +6.2 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +2.9 | +3.1 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.7 | +2.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +2.6 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.5 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.8 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | +0.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | -3.4 | -2.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | myeloid leukemia factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.32 — chr3:158,571,163-158,607,252 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Myeloid leukemia factor family |
| Hallmark sets | SPERMATOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [P58340](https://www.uniprot.org/uniprotkb/P58340) (Myeloid leukemia factor 1):

> Involved in lineage commitment of primary hemopoietic progenitors by restricting erythroid formation and enhancing myeloid formation. Interferes with erythropoietin-induced erythroid terminal differentiation by preventing cells from exiting the cell cycle through suppression of CDKN1B/p27Kip1 levels. Suppresses COP1 activity via CSN3 which activates p53 and induces cell cycle arrest. Binds DNA and affects the expression of a number of genes so may function as a transcription factor in the …

**Summary**, from NCBI Gene [4291](https://www.ncbi.nlm.nih.gov/gene/4291):

> This gene encodes an oncoprotein which is thought to play a role in the phenotypic determination of hemopoetic cells. Translocations between this gene and nucleophosmin have been associated with myelodysplastic syndrome and acute myeloid leukemia. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:7125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7125) · Entrez [4291](https://www.ncbi.nlm.nih.gov/gene/4291) · UniProt [P58340](https://www.uniprot.org/uniprotkb/P58340) · Ensembl [ENSG00000178053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178053)

## Data

Gene col 10891: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10891); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10891, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10891]; `tensor/DDL_lfc|DDL_z.npy` [10891]; `embed/gene_vectors.npy` [10891]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10891 or target_col == 10891). Every well: [[MLF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
