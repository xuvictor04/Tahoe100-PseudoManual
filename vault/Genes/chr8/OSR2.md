---
symbol: "OSR2"
type: "gene"
col: 9030
ensembl_id: "ENSG00000164920"
name: "odd-skipped related transciption factor 2"
location: "8q22.2"
module: 123
arm: "+"
pooled_cpm: 2.71
n_lines_expressing: 45
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 6
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# OSR2

*odd-skipped related transciption factor 2* — 8q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.20× (z +10.7, q 5e-24, up in 24 of 32 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.05 µM in 1 line (SW480 0.0590×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP210]] (+0.75, fdr 7e-06), [[MYLIP]] (+0.71, fdr 7e-06), [[KLF4]] (+0.67, fdr 7e-06); moves opposite to [[SDHC]] (-0.54, fdr 3e-05), [[FUBP3]] (-0.54, fdr 1e-05), [[PGS1]] (-0.54, fdr 1e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BCAR3]] → it (grade B ⚠); 6 go from it, the strongest it → cells under [[Elimusertib hydrochloride (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9030.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.20×** | +10.7 | 5e-24 | 24/32 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.57×** | +8.3 | 3e-14 | 30/41 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.62×** | +8.0 | 2e-13 | 14/19 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.83×** | +6.8 | 2e-09 | 26/41 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +6.7 | 2e-09 | 18/32 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.47×** | +5.9 | 4e-07 | 25/41 (RKO, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.31×** | +5.2 | 1e-05 | 15/36 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +4.5 | 4e-04 | 13/30 (LS 180, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.51×** | +4.4 | 7e-04 | 13/41 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.93×** | +4.1 | 0.002 | 1/5 (PANC-1) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.80×** | +3.8 | 0.007 | 13/41 (J82, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.75×** | +3.6 | 0.014 | 11/42 (C-33 A, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.016 | 9/40 (NCI-H2347, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.01×** | +3.2 | 0.051 | 1/9 (SW1417) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.64×** | +3.1 | 0.071 | 4/29 (HEC-1-A, KATO III, …) | top dose only | position effect removed |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **1.61×** | +3.1 | 0.071 | 2/41 (NCI-H2347, SNU-1) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.59×** | +3.1 | 0.071 | 7/39 (SW480, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM |  | **1.64×** | +3.0 | 0.094 | 7/38 (SW480, AsPC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9030.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.05 µM in 1 line (SW480 0.0590×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pralsetinib (drug)]] 0.05 µM |  | 0.597× | -3.2 | 0.33 | 7/39 (PANC-1, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 0.602× | -3.1 | 0.33 | 8/39 (A-427, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.522× | -3.1 | 0.33 | 7/41 (SW 900, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9030. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.84 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0590× (z -10.7) |
| [[A-172 (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.613 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.692 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.801 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9030), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP210]] | +0.75 | +0.71 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[MYLIP]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[KLF4]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 | same gene group |
| [[MLF1]] | +0.66 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[TENT5C]] | +0.62 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[BCL2L11]] | +0.61 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[MAK]] | +0.59 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[GATA6]] | +0.59 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[FAM222A]] | +0.58 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[SIRT1]] | +0.58 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[NFATC2]] | +0.57 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[MAPRE2]] | +0.55 | +0.55 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHC]] | -0.54 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[FUBP3]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[PGS1]] | -0.54 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[STX16-NPEPL1]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[MAP3K7]] | -0.51 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[ARPC5L]] | -0.50 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[IKBKG]] | -0.50 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[STARD3]] | -0.50 | -0.58 / -0.43 | both halves | 4e-05 |  |
| [[SZT2]] | -0.50 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[TRAPPC10]] | -0.49 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[HARS1]] | -0.48 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[BCAR3]] | -0.48 | -0.52 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAR3]] | B | BCAR3 activity lowers OSR2's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 2.12× higher at baseline in the lines without BCAR3 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Elimusertib hydrochloride (drug)]] 5 µM | C | OSR2 activity raises the cells' numbers under Elimusertib hydrochloride 5 µM (protects the cells) | lines that do not express OSR2 (5) vs lines expressing it (43) | the lines without OSR2: 0.64× the cells of the other lines | 0.004 | ⚠ tissue-confounded; across organs; also absent: ZC3HAV1L, TACC2, VRK2; maybe low, not absent |
| cells under [[Belinostat (drug)]] 5 µM | C | OSR2 activity raises the cells' numbers under Belinostat 5 µM (protects the cells) | lines that do not express OSR2 (5) vs lines expressing it (43) | the lines without OSR2: 0.69× the cells of the other lines | 0.022 | ⚠ tissue-confounded; across organs; also absent: ZC3HAV1L, TACC2, VRK2; maybe low, not absent |
| cells under [[Topotecan (hydrochloride) (drug)]] 0.5 µM | C | OSR2 activity raises the cells' numbers under Topotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express OSR2 (5) vs lines expressing it (43) | the lines without OSR2: 0.75× the cells of the other lines | 0.028 | ⚠ tissue-confounded; across organs; also absent: ZC3HAV1L, TACC2, VRK2; maybe low, not absent |
| cells under [[5-Azacytidine (drug)]] 5 µM | C | OSR2 activity raises the cells' numbers under 5-Azacytidine 5 µM (protects the cells) | lines that do not express OSR2 (5) vs lines expressing it (43) | the lines without OSR2: 0.75× the cells of the other lines | 0.028 | ⚠ tissue-confounded; across organs; also absent: ZC3HAV1L, TACC2, VRK2; maybe low, not absent |
| cells under [[Tucidinostat (drug)]] 5 µM | C | OSR2 activity raises the cells' numbers under Tucidinostat 5 µM (protects the cells) | lines that do not express OSR2 (5) vs lines expressing it (43) | the lines without OSR2: 0.88× the cells of the other lines | 0.093 | ⚠ tissue-confounded; across organs; also absent: ZC3HAV1L, TACC2, VRK2; maybe low, not absent |
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | OSR2's natural level lowers the cells' numbers under Lapatinib ditosylate 0.5 µM (makes them more sensitive) | OSR2's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.437 over the table, 0.072 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.442). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.8, -29.2); signed map (0.1, 18.4). **Vector** length 61.1, 11.3% of its response variance represented; |z| ≥ 3 in 812 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.4 | +10.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +3.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.7 | +3.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +1.6 | +1.1 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +1.5 | +3.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.2 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -0.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.0 | -2.5 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Lonafarnib (drug)]] 0.05 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | odd-skipped related transciption factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.2 — chr8:98,944,403-98,952,104 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90037 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Odd-skipped related transcription factor family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N2R0](https://www.uniprot.org/uniprotkb/Q8N2R0) (Protein odd-skipped-related 2):

> May be involved in the development of the mandibular molar tooth germ at the bud stage.

**Summary**, from NCBI Gene [116039](https://www.ncbi.nlm.nih.gov/gene/116039):

> OSR2 is a mammalian homolog of the Drosophila odd-skipped family of transcription factors (Lan et al., 2004 [PubMed 15175245]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:15830](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15830) · Entrez [116039](https://www.ncbi.nlm.nih.gov/gene/116039) · UniProt [Q8N2R0](https://www.uniprot.org/uniprotkb/Q8N2R0) · Ensembl [ENSG00000164920](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164920)

## Data

Gene col 9030: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9030); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9030, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9030]; `tensor/DDL_lfc|DDL_z.npy` [9030]; `embed/gene_vectors.npy` [9030]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9030 or target_col == 9030). Every well: [[OSR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
