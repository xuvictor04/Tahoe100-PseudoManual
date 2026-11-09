---
symbol: "PSG9"
type: "gene"
col: 11433
ensembl_id: "ENSG00000183668"
name: "pregnancy specific beta-1-glycoprotein 9"
location: "19q13.31"
module: 125
arm: "+"
pooled_cpm: 6.5
n_lines_expressing: 5
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 9
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# PSG9

*pregnancy specific beta-1-glycoprotein 9* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.13× (z +14.5, q 1e-44, up in 1 of 3 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (SNU-423 0.203×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSG4]] (+0.80, fdr 7e-06, ⚠ same locus), [[SLAMF7]] (+0.65, fdr 1e-05), [[ANKRD30B]] (+0.63, fdr 2e-05), [[LINC02154]] (+0.61, fdr 1e-05); moves opposite to [[ANGPTL4]] (-0.53, fdr 2e-04), [[FOXC2]] (-0.52, fdr 3e-05), [[MT2A]] (-0.49, fdr 1e-04).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSG5]] → it (grade C ⚠); 9 go from it, the strongest it → [[SLC25A48]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11433.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.13×** | +14.5 | 1e-44 | 1/3 (A-172) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **10.7×** | +14.3 | 8e-44 | 2/3 (J82, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **9.09×** | +13.8 | 4e-41 | 3/3 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.33×** | +10.7 | 2e-24 | 2/3 (J82, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.26×** | +9.1 | 1e-17 | 1/3 (A-172) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +7.9 | 2e-13 | 2/3 (J82, SNU-423) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.86×** | +6.6 | 4e-09 | 1/3 (A-172) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.87×** | +6.3 | 2e-08 | 1/3 (A-172) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +6.0 | 1e-07 | 1/3 (J82) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.26×** | +5.1 | 2e-05 | 1/3 (A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.31×** | +5.0 | 3e-05 | 0/3 | top dose only | cell-cycle shift (explains ~7% here) |
| [[vincristine (drug)]] 0.5 µM |  | **2.53×** | +4.1 | 0.002 | 0/3 | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.52×** | +4.1 | 0.002 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.002 | 2/3 (SNU-423, A-172) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +4.0 | 0.003 | 3/3 (A-172, SNU-423, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.27×** | +3.7 | 0.009 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.75×** | +3.5 | 0.015 | 0/3 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.18×** | +3.5 | 0.016 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Almonertinib (hydrochloride) (drug)]] 0.5 µM |  | **1.72×** | +3.4 | 0.021 | 0/3 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.71×** | +3.4 | 0.022 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.040 | 0/3 | rises with dose |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.69×** | +3.0 | 0.057 | 0/3 | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +3.0 | 0.057 | 2/3 (J82, SNU-423) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11433.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (SNU-423 0.203×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.596× | -3.3 | 0.37 | 0/3 | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.600× | -3.2 | 0.37 | 2/3 (SNU-423, A-172) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.616× | -3.0 | 0.43 | 2/3 (SNU-423, A-172) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11433. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 128 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 11.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 25.1× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 113 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -10.2) |
| [[A-427 (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.377 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.928 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.574 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.714 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.791 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.964 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.981 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.434 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.406 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.590 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11433), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSG4]] | +0.80 | +0.68 / +0.80 | both halves | 7e-06 | same gene group; pathway: Cell surface interactions at the vascular wall; STRING 778; ⚠ same locus (4.5 kb, same strand: neighbours can correlate without regulation) |
| [[SLAMF7]] | +0.65 | +0.59 / +0.57 | both halves | 1e-05 | same gene group |
| [[ANKRD30B]] | +0.63 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[PSG5]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 | same gene group; pathway: Cell surface interactions at the vascular wall; STRING 636; ⚠ same locus (25.3 kb, same strand: neighbours can correlate without regulation) |
| [[LINC02154]] | +0.61 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[IGFN1]] | +0.57 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[GPNMB]] | +0.53 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[LINC00536]] | +0.53 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[ATP6V1C1]] | +0.52 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[LY96]] | +0.51 | +0.27 / +0.50 | both halves | 3e-04 |  |
| [[PKD1L2]] | +0.50 | +0.38 / +0.44 | both halves | 6e-05 |  |
| [[GNPDA1]] | +0.50 | +0.41 / +0.35 | both halves | 1e-04 |  |
| [[KCP]] | +0.49 | +0.35 / +0.38 | both halves | 1e-04 |  |
| [[MSR1]] | +0.49 | +0.46 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANGPTL4]] | -0.53 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[FOXC2]] | -0.52 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[MT2A]] | -0.49 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[SH3RF3]] | -0.48 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[MT1X]] | -0.47 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[ITGA10]] | -0.46 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[ZMYND8]] | -0.45 | -0.29 / -0.38 | both halves | 3e-04 |  |
| [[ID1]] | -0.44 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[PLXNA2]] | -0.44 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[TBC1D8]] | -0.43 | -0.39 / -0.29 | both halves | 2e-04 |  |
| [[PLAT]] | -0.43 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[AKAP12]] | -0.43 | -0.33 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSG5]] | C | PSG5 activity raises PSG9's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 3.98× lower at baseline in the lines without PSG5 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A48]] | B | PSG9 activity raises SLC25A48's level | lines that do not express PSG9 (45) vs lines expressing it (5) | 1.44× lower at baseline in the lines without PSG9 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, PSG1, NPPB; its own permutation p |
| [[LINC00504]] | C | PSG9 activity raises LINC00504's level | lines that do not express PSG9 (45) vs lines expressing it (5) | 2.37× lower at baseline in the lines without PSG9 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, PSG1, NPPB; co-absent with the target; its own permutation p |
| [[SPINK1]] | C | PSG9 activity raises SPINK1's level | lines that do not express PSG9 (45) vs lines expressing it (5) | 2.31× lower at baseline in the lines without PSG9 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, PSG1, NPPB; co-absent with the target; its own permutation p |
| [[PSG4]] | C | PSG9 activity raises PSG4's level | lines that do not express PSG9 (45) vs lines expressing it (5) | 8.05× lower at baseline in the lines without PSG9 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, PSG1, NPPB; co-absent with the target |
| [[LINC02154]] | C | PSG9 activity raises LINC02154's level | lines that do not express PSG9 (45) vs lines expressing it (5) | 3.03× lower at baseline in the lines without PSG9 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, PSG1, NPPB; co-absent with the target |
| [[LINC01435]] | C | PSG9 activity raises LINC01435's level | lines that do not express PSG9 (45) vs lines expressing it (5) | 5.50× lower at baseline in the lines without PSG9 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, PSG1, NPPB; co-absent with the target |
| [[ANKRD30B]] | C | PSG9 activity raises ANKRD30B's level | lines that do not express PSG9 (45) vs lines expressing it (5) | 6.85× lower at baseline in the lines without PSG9 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, PSG1, NPPB; co-absent with the target; its own permutation p |
| [[ENTHD1]] | C | PSG9 activity raises ENTHD1's level | lines that do not express PSG9 (45) vs lines expressing it (5) | 2.28× lower at baseline in the lines without PSG9 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, PSG1, NPPB; co-absent with the target; its own permutation p |
| [[MARCOL]] | C | PSG9 activity raises MARCOL's level | lines that do not express PSG9 (45) vs lines expressing it (5) | 2.03× lower at baseline in the lines without PSG9 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, PSG1, NPPB; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.1, 21.9); signed map (38.5, 23.7). **Vector** length 15.1, 5.86% of its response variance represented; |z| ≥ 3 in 100 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +13.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.5 | +10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.3 | +7.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.0 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +9.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.6 | +2.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +0.6 | +1.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.6 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.6 | +0.7 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -0.6 | -3.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.5 | -0.8 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.5 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.5 | -2.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | pregnancy specific beta-1-glycoprotein 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.31 — chr19:43,211,791-43,269,530 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PSGII; previously PSG11 |
| Gene groups (HGNC) | V-set domain containing; Pregnancy specific glycoproteins |
| Reactome | 2 pathways, smallest: Cell surface interactions at the vascular wall; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00887](https://www.uniprot.org/uniprotkb/Q00887) (Pregnancy-specific beta-1-glycoprotein 9):

> Binds to the small latent transforming growth factor-beta complex, consisting of the N-terminal TGFB1 latency-associated peptide (LAP) and the mature form of TGFB1, thereby leading to the activation of TGFB1. The activation of TGFB1 leads to stimulation of naive CD4(+) T-cells to increase FoxP3 expression and to an increase in the number of FoxP3(+) regulatory T-cells. Induces the differentiation of a suppressive CD4(+)LAP(+)FoxP3(-) T-cell subset. Induces the secretion of TGFB1 in macrophages, …

**Summary**, from NCBI Gene [5678](https://www.ncbi.nlm.nih.gov/gene/5678):

> The protein encoded by this gene is a member of the pregnancy-specific glycoprotein (PSG) family. This protein family and the closely related carcinoembryonic antigen cell adhesion molecule (CEACAM) gene family are both members of the immunoglobulin superfamily, and are organized as a large gene cluster. This protein is thought to inhibit platelet-fibrinogen interactions. Several studies suggest that reduced serum concentrations of PSGs are associated with fetal growth restrictions, while …

**Accessions** — [HGNC:9526](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9526) · Entrez [5678](https://www.ncbi.nlm.nih.gov/gene/5678) · UniProt [Q00887](https://www.uniprot.org/uniprotkb/Q00887) · Ensembl [ENSG00000183668](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183668)

## Data

Gene col 11433: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11433); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11433, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11433]; `tensor/DDL_lfc|DDL_z.npy` [11433]; `embed/gene_vectors.npy` [11433]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11433 or target_col == 11433). Every well: [[PSG9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSG9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
