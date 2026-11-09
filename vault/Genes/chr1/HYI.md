---
symbol: "HYI"
type: "gene"
col: 10974
ensembl_id: "ENSG00000178922"
name: "hydroxypyruvate isomerase (putative)"
location: "1p34.2"
module: 96
arm: "+"
pooled_cpm: 6.01
n_lines_expressing: 41
n_dd_up: 17
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# HYI

*hydroxypyruvate isomerase (putative)* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.84× (z +14.0, q 9e-42, up in 21 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.51× (z +6.0, q 2e-07, up in 14 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.326× (z -11.7, q 5e-29, down in 31 of 38 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCED1A]] (+0.68, fdr 2e-05), [[ACP2]] (+0.59, fdr 3e-05), [[GTF3C6]] (+0.58, fdr 2e-04); moves opposite to [[ACTR6]] (-0.51, fdr 3e-04), [[TBC1D20]] (-0.50, fdr 1e-04), [[GFPT1]] (-0.49, fdr 1e-04).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GALC]] → it (grade B ⚠); 3 go from it, the strongest it → [[RNF207]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10974.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.84×** | +14.0 | 9e-42 | 21/21 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.29×** | +11.9 | 3e-30 | 11/11 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.91×** | +10.3 | 2e-22 | 16/16 (NCI-H2030, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +6.0 | 2e-07 | 14/39 (RKO, hTERT-HPNE, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +5.6 | 3e-06 | 12/29 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.81×** | +4.4 | 0.001 | 11/25 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.78×** | +4.3 | 0.002 | 7/34 (RPMI-7951, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.45×** | +3.8 | 0.009 | 10/35 (COLO 205, LS 180, …) | two highest doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.66×** | +3.8 | 0.010 | 12/34 (A498, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +3.8 | 0.010 | 3/11 (NCI-H2347, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.43×** | +3.7 | 0.012 | 11/27 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.6 | 0.017 | 4/39 (RPMI-7951, AsPC-1, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.92×** | +3.5 | 0.017 | 7/25 (HOP62, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.5 | 0.019 | 9/26 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.032 | 9/34 (HOP62, NCI-H2030, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.38×** | +3.1 | 0.070 | 5/32 (A498, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.070 | 6/35 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.49×** | +3.0 | 0.097 | 8/35 (NCI-H460, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10974.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.326×** | -11.7 | 5e-29 | 31/38 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.349×** | -11.0 | 9e-26 | 32/36 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.412×** | -9.3 | 3e-18 | 31/37 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.552×** | -6.2 | 6e-08 | 22/38 (RPMI-7951, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.429×** | -4.6 | 4e-04 | 16/37 (LS 180, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.677×** | -4.1 | 0.004 | 16/33 (RKO, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.676×** | -3.9 | 0.008 | 13/34 (J82, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.707×** | -3.7 | 0.017 | 9/38 (AsPC-1, HCT15, …) | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 5 µM |  | **0.784×** | -3.6 | 0.017 | 8/35 (NCI-H460, COLO 205, …) | rises with dose | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.745×** | -3.1 | 0.096 | 4/37 (AsPC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.746×** | -3.1 | 0.096 | 6/39 (SW 1271, HOP62, …) | two highest doses | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.571×** | -3.1 | 0.096 | 7/32 (SW480, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.749×** | -3.1 | 0.096 | 3/39 (NCI-H460, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10974. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.227× (z -9.0) |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0937× (z -8.8) |
| [[RKO (line)]] | wt | 6.11 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0812× (z -8.6) |
| [[A-172 (line)]] | wt | 0.637 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.953 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.643 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.707 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10974), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCED1A]] | +0.68 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[ACP2]] | +0.59 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[GTF3C6]] | +0.58 | +0.30 / +0.48 | both halves | 2e-04 |  |
| [[EME2]] | +0.58 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[CCDC9B]] | +0.58 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[MYL5]] | +0.58 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[TAF9B]] | +0.57 | +0.37 / +0.51 | both halves | 9e-05 |  |
| [[AP1G2-AS1]] | +0.57 | +0.48 / +0.30 | both halves | 2e-04 |  |
| [[SPTY2D1OS]] | +0.57 | +0.33 / +0.33 | both halves | 1e-04 |  |
| [[WIZ]] | +0.57 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[CYB561A3]] | +0.57 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[IDUA]] | +0.56 | +0.51 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR6]] | -0.51 | -0.48 / -0.29 | both halves | 3e-04 |  |
| [[TBC1D20]] | -0.50 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[GFPT1]] | -0.49 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[SLC27A1]] | -0.49 | -0.38 / -0.26 | both halves | 4e-04 |  |
| [[SLC31A1]] | -0.48 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[EFCAB14]] | -0.48 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[PHKA2]] | -0.46 | -0.28 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALC]] | B | GALC activity raises HYI's level | lines that do not express GALC (17) vs lines expressing it (33) | 1.95× lower at baseline in the lines without GALC | 0.092 | ⚠ within organs, on part of the lines; also absent: HERC5, TNFRSF1B, ZNF354C |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF207]] | B | HYI activity lowers RNF207's level | lines that do not express HYI (9) vs lines expressing it (41) | 1.58× higher at baseline in the lines without HYI | 0.042 | ⚠ within organs, on part of the lines; also absent: HEIH |
| [[FBXW4]] | B | HYI activity lowers FBXW4's level | lines that do not express HYI (9) vs lines expressing it (41) | 1.42× higher at baseline in the lines without HYI | 0.046 | ⚠ within organs, on part of the lines; also absent: HEIH |
| [[GALC]] | B | HYI activity raises GALC's level | lines that do not express HYI (9) vs lines expressing it (41) | 2.96× lower at baseline in the lines without HYI | 0.095 | ⚠ within organs, on part of the lines; also absent: HEIH |

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.0, 22.2); signed map (31.9, -21.0). **Vector** length 46.5, 6.80% of its response variance represented; |z| ≥ 3 in 704 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +10.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.3 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +3.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -1.8 | -4.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.7 | -9.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -0.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | hydroxypyruvate isomerase (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:43,450,989-43,453,989 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HT036 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T013](https://www.uniprot.org/uniprotkb/Q5T013) (Putative hydroxypyruvate isomerase):

> May catalyzes the reversible isomerization between hydroxypyruvate and 2-hydroxy-3-oxopropanoate (also termed tartronate semialdehyde).

**Summary**, from NCBI Gene [81888](https://www.ncbi.nlm.nih.gov/gene/81888):

> This gene encodes a putative hydroxypyruvate isomerase, which likely catalyzes the conversion of hydroxypyruvate to 2-hydroxy-3-oxopropanoate, and may be involved in carbohydrate transport and metabolism. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:26948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26948) · Entrez [81888](https://www.ncbi.nlm.nih.gov/gene/81888) · UniProt [Q5T013](https://www.uniprot.org/uniprotkb/Q5T013) · Ensembl [ENSG00000178922](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178922)

## Data

Gene col 10974: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10974); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10974, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10974]; `tensor/DDL_lfc|DDL_z.npy` [10974]; `embed/gene_vectors.npy` [10974]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10974 or target_col == 10974). Every well: [[HYI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HYI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
