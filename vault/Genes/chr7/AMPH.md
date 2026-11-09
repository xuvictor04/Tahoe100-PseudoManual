---
symbol: "AMPH"
type: "gene"
col: 1204
ensembl_id: "ENSG00000078053"
name: "amphiphysin"
location: "7p14.1"
module: 104
arm: "+"
pooled_cpm: 5.32
n_lines_expressing: 14
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# AMPH

*amphiphysin* — 7p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.49× (z +16.0, q 0e+00, up in 1 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0544×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.289×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMTC1]] (+0.62, fdr 8e-06), [[PID1]] (+0.59, fdr 4e-05), [[LINC02930]] (+0.58, fdr 1e-05); moves opposite to [[RHCE]] (-0.46, fdr 1e-04), [[NMNAT1]] (-0.42, fdr 4e-04), [[CATSPER2P1]] (-0.39, fdr 9e-04, ⚠ not reproduced).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NAALADL2-AS2]] → it (grade C ⚠); 4 go from it, the strongest it → [[CACNA1C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1204.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.49×** | +16.0 | 0e+00 | 1/11 (C32) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.82×** | +14.2 | 2e-43 | 1/8 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.66×** | +12.5 | 1e-33 | 12/12 (HS-578T, SW 900, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.19×** | +12.5 | 2e-33 | 1/5 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.48×** | +10.4 | 2e-23 | 2/7 (J82, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +9.0 | 2e-17 | 9/11 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.34×** | +7.7 | 1e-12 | 4/12 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.24×** | +7.3 | 2e-11 | 8/11 (SW 900, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.02×** | +6.4 | 1e-08 | 8/11 (SW 900, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.99×** | +6.2 | 3e-08 | 8/11 (BT-474, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +5.8 | 3e-07 | 3/12 (hTERT-HPNE, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +5.2 | 1e-05 | 9/11 (HS-578T, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.9 | 5e-05 | 6/7 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.78×** | +4.8 | 5e-05 | 5/6 (SW 900, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.70×** | +4.8 | 7e-05 | 6/11 (SW 900, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +4.6 | 1e-04 | 4/11 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.6 | 1e-04 | 1/12 (SW 900) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +4.4 | 3e-04 | 0/11 | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.62×** | +4.2 | 8e-04 | 3/11 (C32, HS-578T, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.75×** | +3.6 | 0.008 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sodium Salicylate (drug)]] 0.5 µM |  | **1.47×** | +3.5 | 0.013 | 0/11 | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.99×** | +3.3 | 0.025 | 5/12 (HS-578T, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1204.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0544×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.289×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.676× | -3.6 | 0.11 | 0/11 | inconsistent across doses |  |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | 0.684× | -3.5 | 0.11 | 1/12 (RPMI-7951) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.670× | -3.4 | 0.11 | 0/11 | inconsistent across doses |  |
| [[Finasteride (drug)]] 5 µM |  | 0.682× | -3.4 | 0.11 | 1/11 (SK-MEL-2) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.699× | -3.1 | 0.23 | 0/12 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1204. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 23.6 | 9 | 0 | [[Clobetasol propionate (drug)]] 5 µM 6.67× (z +9.9) | — |
| [[A-172 (line)]] | wt | 75.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 23.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0544× (z -12.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.605 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.827 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.996 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.623 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.922 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.816 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.680 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.682 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.611 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.587 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.690 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.567 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.971 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.936 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.539 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.645 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.822 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.588 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1204), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMTC1]] | +0.62 | +0.58 / +0.63 | both halves | 8e-06 | **novel candidate** |
| [[PID1]] | +0.59 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[LINC02930]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[JCAD]] | +0.54 | +0.32 / +0.62 | both halves | 2e-04 |  |
| [[SLC7A2]] | +0.53 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[FZD4]] | +0.52 | +0.38 / +0.53 | both halves | 7e-05 | pathway: Clathrin-mediated endocytosis |
| [[ENPP2]] | +0.52 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[SLC1A3]] | +0.50 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[TOX2]] | +0.50 | +0.29 / +0.51 | both halves | 3e-04 |  |
| [[SNAI2]] | +0.49 | +0.36 / +0.53 | both halves | 9e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[DNER]] | +0.49 | +0.44 / +0.46 | both halves | 3e-05 | STRING 791 |
| [[IL1R1]] | +0.49 | +0.40 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHCE]] | -0.46 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[NMNAT1]] | -0.42 | -0.35 / -0.26 | both halves | 4e-04 |  |
| [[CATSPER2P1]] | -0.39 | -0.18 / -0.34 | ⚠ not reproduced | 9e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAALADL2-AS2]] | C | NAALADL2-AS2 activity raises AMPH's level | lines that do not express NAALADL2-AS2 (36) vs lines expressing it (14) | 2.93× lower at baseline in the lines without NAALADL2-AS2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RNF17, ENSG00000287598, SSX1; co-absent with the target |
| [[LINC02930]] | C | LINC02930 activity raises AMPH's level | lines that do not express LINC02930 (33) vs lines expressing it (17) | 3.57× lower at baseline in the lines without LINC02930 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000232053, GYPC, PLPP4; co-absent with the target |
| [[PLPP4]] | C | PLPP4 activity raises AMPH's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 3.36× lower at baseline in the lines without PLPP4 | 0.035 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6; co-absent with the target |
| [[FSTL5]] | C | FSTL5 activity raises AMPH's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 2.23× lower at baseline in the lines without FSTL5 | 0.077 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2; co-absent with the target |
| [[LINC01320]] | C | LINC01320 activity raises AMPH's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 1.98× lower at baseline in the lines without LINC01320 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA1C]] | B | AMPH activity raises CACNA1C's level | lines that do not express AMPH (36) vs lines expressing it (14) | 3.95× lower at baseline in the lines without AMPH | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ANKRD30B, GRIN2A, GYPC |
| [[ENPP2]] | C | AMPH activity raises ENPP2's level | lines that do not express AMPH (36) vs lines expressing it (14) | 3.52× lower at baseline in the lines without AMPH | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ANKRD30B, GRIN2A, GYPC; co-absent with the target |
| [[LINC01320]] | C | AMPH activity raises LINC01320's level | lines that do not express AMPH (36) vs lines expressing it (14) | 4.27× lower at baseline in the lines without AMPH | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ANKRD30B, GRIN2A, GYPC; co-absent with the target |
| [[PLPP4]] | C | AMPH activity raises PLPP4's level | lines that do not express AMPH (36) vs lines expressing it (14) | 5.13× lower at baseline in the lines without AMPH | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ANKRD30B, GRIN2A, GYPC; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.6, 15.7); signed map (18.2, 36.0). **Vector** length 34.3, 8.87% of its response variance represented; |z| ≥ 3 in 337 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +14.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +12.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.4 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +10.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.2 | +1.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.1 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +4.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.1 | +2.6 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.8 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.7 | -2.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -0.9 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | amphiphysin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.1 — chr7:38,383,704-38,631,420 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | N-BAR domain containing; SH3 domain containing |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 3 pathways, smallest: Clathrin-mediated endocytosis; Membrane Trafficking; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P49418](https://www.uniprot.org/uniprotkb/P49418) (Amphiphysin):

> May participate in mechanisms of regulated exocytosis in synapses and certain endocrine cell types. May control the properties of the membrane associated cytoskeleton.

**Summary**, from NCBI Gene [273](https://www.ncbi.nlm.nih.gov/gene/273):

> This gene encodes a protein associated with the cytoplasmic surface of synaptic vesicles. A subset of patients with stiff-man syndrome who were also affected by breast cancer are positive for autoantibodies against this protein. Alternate splicing of this gene results in two transcript variants encoding different isoforms. Additional splice variants have been described, but their full length sequences have not been determined. A pseudogene of this gene is found on chromosome 11.[provided by …

**Accessions** — [HGNC:471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:471) · Entrez [273](https://www.ncbi.nlm.nih.gov/gene/273) · UniProt [P49418](https://www.uniprot.org/uniprotkb/P49418) · Ensembl [ENSG00000078053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078053)

## Data

Gene col 1204: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1204); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1204, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1204]; `tensor/DDL_lfc|DDL_z.npy` [1204]; `embed/gene_vectors.npy` [1204]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1204 or target_col == 1204). Every well: [[AMPH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMPH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
