---
symbol: "SLC10A3"
type: "gene"
col: 4778
ensembl_id: "ENSG00000126903"
name: "solute carrier family 10 member 3"
location: "Xq28"
module: 52
arm: "+"
pooled_cpm: 7.22
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# SLC10A3

*solute carrier family 10 member 3* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.34× (z +11.2, q 3e-26, up in 35 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.271× (z -6.3, q 1e-07, down in 30 of 42 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOB2]] (+0.66, fdr 1e-05), [[TPRN]] (+0.59, fdr 1e-04), [[RIC8A]] (+0.59, fdr 4e-05); moves opposite to [[PPA2]] (-0.61, fdr 1e-05), [[MRPL42]] (-0.59, fdr 1e-04), [[RAD23B]] (-0.58, fdr 6e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4778.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +11.2 | 3e-26 | 35/40 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +5.6 | 8e-06 | 19/32 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +4.9 | 2e-04 | 21/38 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +4.8 | 3e-04 | 20/38 (NCI-H460, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.029 | 16/47 (Hs 766T, NCI-H2347, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +3.6 | 0.029 | 13/32 (AsPC-1, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.45×** | +3.5 | 0.040 | 12/46 (SW1417, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.40× | +3.1 | 0.13 | 10/46 (KATO III, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4778.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.271×** | -6.3 | 1e-07 | 30/42 (LoVo, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.364×** | -4.9 | 3e-04 | 22/38 (HOP62, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.628×** | -4.3 | 0.003 | 23/46 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.625×** | -4.2 | 0.004 | 21/41 (NCI-H23, PANC-1, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.627×** | -4.1 | 0.005 | 22/42 (hTERT-HPNE, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.655×** | -3.9 | 0.008 | 21/46 (hTERT-HPNE, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.678×** | -3.6 | 0.025 | 15/45 (H4, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.672×** | -3.5 | 0.029 | 18/43 (HCT15, H4, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.689×** | -3.4 | 0.033 | 18/39 (AsPC-1, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.690×** | -3.4 | 0.033 | 17/44 (RPMI-7951, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.784×** | -3.2 | 0.076 | 11/46 (LoVo, A-172, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.717×** | -3.1 | 0.099 | 17/43 (LS 180, PANC-1, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4778. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 15.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.250× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0431× (z -15.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0698× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0851× (z -8.9) |
| [[A549 (line)]] | wt | 5.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 5.61 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0633× (z -9.7) |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0906× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 7.16 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0866× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 5.55 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 4.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +10.8) | — |
| [[A-427 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4778), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOB2]] | +0.66 | +0.50 / +0.74 | both halves | 1e-05 |  |
| [[TPRN]] | +0.59 | +0.36 / +0.66 | both halves | 1e-04 |  |
| [[RIC8A]] | +0.59 | +0.41 / +0.70 | both halves | 4e-05 |  |
| [[SHPK]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ZNF324]] | +0.58 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[FBXL12]] | +0.57 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[ELOVL1]] | +0.57 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[POLG]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SLC52A2]] | +0.57 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[ACD]] | +0.56 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[LRWD1]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[KCTD5]] | +0.55 | +0.44 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPA2]] | -0.61 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[MRPL42]] | -0.59 | -0.35 / -0.67 | both halves | 1e-04 |  |
| [[RAD23B]] | -0.58 | -0.39 / -0.67 | both halves | 6e-05 |  |
| [[DTWD2]] | -0.56 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[FUT10]] | -0.55 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[CEBPZOS]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[SCP2]] | -0.52 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[KPNA5]] | -0.51 | -0.24 / -0.61 | both halves | 4e-04 |  |
| [[SMG7]] | -0.50 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[HSD17B4]] | -0.50 | -0.36 / -0.59 | both halves | 9e-05 |  |
| [[MAP2K6]] | -0.50 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[G3BP1]] | -0.49 | -0.17 / -0.63 | ⚠ one half (not replicated) | 0.001 |  |
| [[DLD]] | -0.49 | -0.26 / -0.60 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC10A3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers SLC10A3's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | SLC10A3's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | SLC10A3's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.59 | 0.491 over the table, 0.078 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | SLC10A3's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | SLC10A3's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.56 | 0.530 over the table, 0.099 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.401). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-28.3, -14.1); signed map (-21.9, 41.5). **Vector** length 77.0, 15.1% of its response variance represented; |z| ≥ 3 in 818 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +11.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +5.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +4.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.0 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.6 | -3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | -1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 10 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,487,306-154,490,690 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P3, DXS253E |
| Gene groups (HGNC) | Solute carrier family 10 |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [P09131](https://www.uniprot.org/uniprotkb/P09131) (P3 protein):

> The ubiquitous expression and the conservation of the sequence in distant animal species suggest that the gene codes for a protein with housekeeping functions.

**Summary**, from NCBI Gene [8273](https://www.ncbi.nlm.nih.gov/gene/8273):

> This gene maps to a GC-rich region of the X chromosome and was identified by its proximity to a CpG island. It is thought to be a housekeeping gene. Alternative splicing results in multiple transcript variants encoding distinct isoforms.[provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:22979](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22979) · Entrez [8273](https://www.ncbi.nlm.nih.gov/gene/8273) · UniProt [P09131](https://www.uniprot.org/uniprotkb/P09131) · Ensembl [ENSG00000126903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126903)

## Data

Gene col 4778: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4778); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4778, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4778]; `tensor/DDL_lfc|DDL_z.npy` [4778]; `embed/gene_vectors.npy` [4778]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4778 or target_col == 4778). Every well: [[SLC10A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC10A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
