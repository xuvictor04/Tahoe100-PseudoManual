---
symbol: "FLVCR2"
type: "gene"
col: 4099
ensembl_id: "ENSG00000119686"
name: "FLVCR choline and putative heme transporter 2"
location: "14q24.3"
module: 106
arm: "+"
pooled_cpm: 9.24
n_lines_expressing: 45
n_dd_up: 48
n_dd_down: 3
n_dd_up_clean: 44
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# FLVCR2

*FLVCR choline and putative heme transporter 2* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.80× (z +11.9, q 4e-30, up in 29 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.530× (z -5.4, q 5e-05, down in 13 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 0.648× (z -3.8, q 0.028, down in 15 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0490×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.151×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (LS 180 0.0885×; ⚠ transcription drop; cell-cycle shift, explains ~22% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EDN2]] (+0.70, fdr 7e-06), [[MT1M]] (+0.65, fdr 1e-05), [[TSC22D3]] (+0.65, fdr 7e-06); moves opposite to [[ANXA10]] (-0.64, fdr 7e-06), [[DCBLD2]] (-0.61, fdr 7e-06), [[LINC02798]] (-0.57, fdr 1e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC5A4-AS1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[AVPI1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4099.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.80×** | +11.9 | 4e-30 | 29/38 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.31×** | +10.1 | 2e-21 | 31/40 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **6.03×** | +8.2 | 4e-14 | 31/39 (PANC-1, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **2.43×** | +7.8 | 1e-12 | 27/41 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.35×** | +7.5 | 8e-12 | 30/41 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.11×** | +6.5 | 7e-09 | 25/41 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.72×** | +6.2 | 3e-08 | 17/41 (A-427, RKO, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.69×** | +6.1 | 6e-08 | 22/40 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.68×** | +5.9 | 2e-07 | 22/41 (SNU-1, SW480, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.95×** | +5.6 | 1e-06 | 21/40 (AsPC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +5.5 | 2e-06 | 16/41 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +5.3 | 6e-06 | 20/41 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 0.05 µM |  | **1.83×** | +5.3 | 6e-06 | 18/39 (AsPC-1, HS-578T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.78×** | +5.0 | 2e-05 | 20/40 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +5.0 | 3e-05 | 16/37 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.76×** | +4.9 | 3e-05 | 19/42 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4099.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0490×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.151×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (LS 180 0.0885×; ⚠ transcription drop; cell-cycle shift, explains ~22% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.530×** | -5.4 | 5e-05 | 13/19 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.599×** | -4.5 | 0.002 | 17/31 (NCI-H2347, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.648×** | -3.8 | 0.028 | 15/42 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.682× | -3.4 | 0.11 | 10/41 (NCI-H2030, MIA PaCa-2, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.701× | -3.1 | 0.13 | 10/41 (J82, H4, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.766× | -3.1 | 0.13 | 11/41 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.701× | -3.1 | 0.13 | 9/43 (SW 1088, A-172, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.702× | -3.1 | 0.13 | 9/42 (NCI-H661, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4099. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 9.93 | 13 | 0 | [[Triamcinolone (drug)]] 5 µM 10.0× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 35.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0490× (z -15.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 3.95 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 6.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.68× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 7.31 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0885× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~22% of this change |
| [[Panc 03.27 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.32× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 13.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 24.6× (z +8.5) | — |
| [[A-172 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4099), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDN2]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[MT1M]] | +0.65 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[TSC22D3]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[PER1]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 | same gene group |
| [[RRAGD]] | +0.64 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[KLF9]] | +0.63 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[TLR2]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[SLC25A12]] | +0.63 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[MAOA]] | +0.62 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[UBE2E1]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[PRKAG2]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CYB5A]] | +0.60 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA10]] | -0.64 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[DCBLD2]] | -0.61 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[LINC02798]] | -0.57 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[NEK10]] | -0.57 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[SLC4A7]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[AADAC]] | -0.56 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[MANCR]] | -0.55 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[ANTXR2]] | -0.55 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[LUCAT1]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[AADACP1]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ITGA2]] | -0.51 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[TBILA]] | -0.51 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC5A4-AS1]] | B | SLC5A4-AS1 activity lowers FLVCR2's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.75× higher at baseline in the lines without SLC5A4-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AVPI1]] | B | FLVCR2 activity raises AVPI1's level | lines that do not express FLVCR2 (5) vs lines expressing it (45) | 2.03× lower at baseline in the lines without FLVCR2 | 0.089 | ⚠ within organs, on part of the lines; also absent: AIFM2, CTSD, ERAP2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.737). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.4, 14.7); signed map (16.2, 29.8). **Vector** length 105, 27.2% of its response variance represented; |z| ≥ 3 in 1,118 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +4.6 | +5.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.3 | +5.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +4.2 | +4.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.2 | +5.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.1 | +5.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.5 | -1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -1.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | FLVCR choline and putative heme transporter 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:75,578,620-75,663,214 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20371, MFSD7C, SLC49A2, CCT; previously C14orf58 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Solute carrier family 49 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPI3](https://www.uniprot.org/uniprotkb/Q9UPI3) (Choline/ethanolamine transporter FLVCR2):

> Choline uniporter that specifically mediates choline uptake at the blood-brain-barrier. Responsible for the majority of choline uptake across the blood-brain-barrier from the circulation into the brain (By similarity). Choline, a nutrient critical for brain development, is a precursor of phosphatidylcholine, as well as betaine (By similarity). Also mediates transport of ethanolamine. Choline and ethanolamine transport is not coupled with proton transport and is exclusively driven by the choline …

**Summary**, from NCBI Gene [55640](https://www.ncbi.nlm.nih.gov/gene/55640):

> This gene encodes a member of the major facilitator superfamily. The encoded transmembrane protein is a calcium transporter. Unlike the related protein feline leukemia virus subgroup C receptor 1, the protein encoded by this locus does not bind to feline leukemia virus subgroup C envelope protein. The encoded protein may play a role in development of brain vascular endothelial cells, as mutations at this locus have been associated with proliferative vasculopathy and hydranencephaly-hydrocephaly …

**Accessions** — [HGNC:20105](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20105) · Entrez [55640](https://www.ncbi.nlm.nih.gov/gene/55640) · UniProt [Q9UPI3](https://www.uniprot.org/uniprotkb/Q9UPI3) · Ensembl [ENSG00000119686](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119686)

## Data

Gene col 4099: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4099); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4099, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4099]; `tensor/DDL_lfc|DDL_z.npy` [4099]; `embed/gene_vectors.npy` [4099]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4099 or target_col == 4099). Every well: [[FLVCR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLVCR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
