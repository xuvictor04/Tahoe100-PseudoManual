---
symbol: "RSL24D1"
type: "gene"
col: 6089
ensembl_id: "ENSG00000137876"
name: "ribosomal L24 domain containing 1"
location: "15q21.3"
module: 63
arm: "+"
pooled_cpm: 88.72
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# RSL24D1

*ribosomal L24 domain containing 1* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.89× (z +9.6, q 5e-19, up in 42 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.68× (z +8.5, q 5e-15, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Folic acid (drug)]] 5 µM: 0.837× (z -4.1, q 0.028, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.406×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (PANC-1 0.489×; ⚠ cell-cycle shift, explains ~1% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCEA1]] (+0.79, fdr 7e-06), [[EPRS1]] (+0.78, fdr 7e-06), [[TARS1]] (+0.77, fdr 7e-06); moves opposite to [[POLR2L]] (-0.57, fdr 1e-05), [[TUBB4B]] (-0.51, fdr 3e-05), [[RBX1]] (-0.47, fdr 2e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC00662]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6089.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +9.6 | 5e-19 | 42/45 (A498, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +8.7 | 1e-15 | 40/47 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +8.5 | 5e-15 | 44/48 (C32, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +7.6 | 3e-12 | 38/49 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +5.4 | 8e-06 | 25/44 (HepG2/C3A, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +5.1 | 3e-05 | 37/49 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +4.9 | 6e-05 | 30/48 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +4.9 | 8e-05 | 28/49 (C32, H4, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.34×** | +4.8 | 1e-04 | 29/48 (J82, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +4.8 | 1e-04 | 30/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.33×** | +4.7 | 1e-04 | 29/48 (NCI-H2030, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +4.3 | 6e-04 | 31/48 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +4.3 | 6e-04 | 35/48 (HT-29, PANC-1, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.3 | 6e-04 | 31/45 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.2 | 0.001 | 33/48 (MIA PaCa-2, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.003 | 26/48 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.006 | 28/48 (LOX-IMVI, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.009 | 21/47 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.010 | 23/47 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.053 | 19/48 (Hs 766T, NCI-H2030, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.061 | 14/48 (LOX-IMVI, NCI-H2030, …) | two highest doses |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.061 | 13/48 (SW1417, A-427, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6089.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.406×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (PANC-1 0.489×; ⚠ cell-cycle shift, explains ~1% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | 0.837× | -4.1 | 0.028 | 20/48 (HT-29, A498, …) | inconsistent across doses | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.791×** | -3.8 | 0.040 | 32/49 (NCI-H23, Panc 03.27, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.738×** | -3.5 | 0.063 | 24/48 (HT-29, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.798×** | -3.5 | 0.063 | 25/47 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.830× | -3.0 | 0.28 | 23/48 (NCI-H23, COLO 205, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6089. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 65.5 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.99× (z +10.7) ⚠ toxic | — |
| [[LoVo (line)]] | wt | 176 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.64× (z +11.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 2.26× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 92.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 63.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +11.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 99.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.10× (z +9.2) | — |
| [[A498 (line)]] | wt | 79.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.43× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 116 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +10.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 47.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.11× (z +10.9) | — |
| [[COLO 205 (line)]] | alt | 79.4 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.05× (z +9.7) ⚠ toxic | — |
| [[HepG2_C3A (line)]] | wt | 79.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 133 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.20× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 84.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.28× (z +8.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[PANC-1 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.489× (z -9.6) ⚠ cell-cycle shift, explains ~1% of this change |
| [[RKO (line)]] | wt | 117 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +8.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 139 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 126 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6089), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEA1]] | +0.79 | +0.79 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[EPRS1]] | +0.78 | +0.82 / +0.78 | both halves | 7e-06 | STRING 636 |
| [[TARS1]] | +0.77 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[NARS1]] | +0.76 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[IARS1]] | +0.75 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[SARS1]] | +0.74 | +0.81 / +0.64 | both halves | 7e-06 |  |
| [[HSPA9]] | +0.74 | +0.75 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[XPOT]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[ZFAND1]] | +0.71 | +0.70 / +0.65 | both halves | 7e-06 | STRING 434 |
| [[TRIB3]] | +0.70 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[MTHFD2]] | +0.69 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[GARS1]] | +0.69 | +0.72 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2L]] | -0.57 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[TUBB4B]] | -0.51 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[RBX1]] | -0.47 | -0.46 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00662]] | C | LINC00662 activity lowers RSL24D1's level | lines that do not express LINC00662 (3) vs lines expressing it (47) | 1.79× higher at baseline in the lines without LINC00662 | 0.023 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221 |
| [[SEL1L]] | C | SEL1L's natural level weakens RSL24D1's drug response | SEL1L's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.36; direction not clear | 0.038 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SLC38A1]] | C | SLC38A1 activity raises RSL24D1's level | lines that do not express SLC38A1 (3) vs lines expressing it (47) | 1.25× lower at baseline in the lines without SLC38A1 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ALPK3, TRIB3, SAMHD1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.768). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.8, 47.2); signed map (-14.3, 24.0). **Vector** length 105, 31.3% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.60 to 16); *mTORC1 signaling* (hallmark, mean cos +0.59 to 20); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.71 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.9 | +8.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.0 | +3.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +3.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.4 | +8.7 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +4.2 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.9 | +1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.6 | +3.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.2 | +1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | +1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | +2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | +1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.7 | -3.0 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal L24 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:55,180,806-55,197,049 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HRP-L30-iso, L30, RPL24L, RPL24; previously C15orf15 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHA3](https://www.uniprot.org/uniprotkb/Q9UHA3) (Probable ribosome biogenesis protein RLP24):

> Involved in the biogenesis of the 60S ribosomal subunit. Ensures the docking of GTPBP4/NOG1 to pre-60S particles (By similarity).

**Summary**, from NCBI Gene [51187](https://www.ncbi.nlm.nih.gov/gene/51187):

> This gene encodes a protein sharing a low level of sequence similarity with human ribosomal protein L24. Although this gene has been referred to as RPL24, L30, and 60S ribosomal protein L30 isolog in the sequence databases, it is distinct from the human genes officially named RPL24 (which itself has been referred to as ribosomal protein L30) and RPL30. The protein encoded by this gene localizes to the nucleolus and is thought to play a role in the biogenesis of the 60S ribosomal subunit. The …

**Accessions** — [HGNC:18479](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18479) · Entrez [51187](https://www.ncbi.nlm.nih.gov/gene/51187) · UniProt [Q9UHA3](https://www.uniprot.org/uniprotkb/Q9UHA3) · Ensembl [ENSG00000137876](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137876)

## Data

Gene col 6089: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6089); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6089, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6089]; `tensor/DDL_lfc|DDL_z.npy` [6089]; `embed/gene_vectors.npy` [6089]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6089 or target_col == 6089). Every well: [[RSL24D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSL24D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
