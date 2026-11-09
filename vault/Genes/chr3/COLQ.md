---
symbol: "COLQ"
type: "gene"
col: 13051
ensembl_id: "ENSG00000206561"
name: "collagen like tail subunit of asymmetric acetylcholinesterase"
location: "3p25.1"
module: 26
arm: "+"
pooled_cpm: 4.55
n_lines_expressing: 48
n_dd_up: 37
n_dd_down: 8
n_dd_up_clean: 29
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# COLQ

*collagen like tail subunit of asymmetric acetylcholinesterase* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.43× (z +17.8, q 0e+00, up in 34 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.460× (z -8.0, q 8e-13, down in 28 of 44 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 0.5 µM: 0.534× (z -4.6, q 0.001, down in 13 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESRRB]] (+0.71, fdr 8e-06), [[SLC26A7]] (+0.70, fdr 1e-05), [[ST8SIA5]] (+0.68, fdr 3e-05); moves opposite to [[L2HGDH]] (-0.56, fdr 3e-04), [[MTERF3]] (-0.56, fdr 3e-05), [[POMGNT2]] (-0.55, fdr 7e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LINC02641]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13051.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.43×** | +17.8 | 0e+00 | 34/38 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.81×** | +13.7 | 4e-40 | 41/44 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.56×** | +12.5 | 1e-33 | 28/33 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.16×** | +11.8 | 8e-30 | 35/43 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +11.3 | 1e-27 | 34/37 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.77×** | +10.0 | 1e-21 | 28/38 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.98×** | +9.9 | 3e-21 | 33/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.89×** | +9.2 | 2e-18 | 28/45 (HOP62, BT-474, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.61×** | +9.1 | 7e-18 | 4/8 (HS-578T, BT-474, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.37×** | +8.8 | 6e-17 | 26/37 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +8.8 | 1e-16 | 5/7 (CFPAC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.31×** | +8.5 | 6e-16 | 28/44 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.07×** | +6.7 | 7e-10 | 20/44 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +6.6 | 2e-09 | 17/45 (LS 180, NCI-H2030, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +6.6 | 2e-09 | 8/22 (MIA PaCa-2, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +6.3 | 1e-08 | 20/42 (NCI-H23, RPMI-7951, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.86×** | +5.6 | 6e-07 | 13/41 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.72×** | +5.3 | 5e-06 | 12/38 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13051.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.460×** | -8.0 | 8e-13 | 28/44 (A-172, LoVo, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.534×** | -4.6 | 0.001 | 13/45 (CFPAC-1, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -4.1 | 0.007 | 11/46 (RKO, Panc 03.27, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.470×** | -4.0 | 0.007 | 12/33 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.492×** | -3.8 | 0.016 | 7/37 (RKO, SHP-77, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.509×** | -3.6 | 0.025 | 9/37 (HEC-1-A, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.510×** | -3.6 | 0.025 | 12/29 (HEC-1-A, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.712×** | -3.3 | 0.069 | 11/43 (KATO III, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13051. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.43 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +10.9) | — |
| [[C32 (line)]] | wt | 7.86 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.67× (z +10.4) | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0806× (z -9.1) |
| [[LoVo (line)]] | wt | 5.98 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.53× (z +14.2) | — |
| [[A-172 (line)]] | wt | 5.38 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0743× (z -9.5) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 4.29 | 0 | 1 | — | [[Idoxuridine (drug)]] 0.5 µM 0.0664× (z -8.6) |
| [[BT-474 (line)]] | alt | 10.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 21.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 7.73 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 2.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 3.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.29× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0960× (z -8.6) |
| [[SW48 (line)]] | wt | 5.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +9.5) | — |
| [[A-427 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13051), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESRRB]] | +0.71 | +0.81 / +0.58 | both halves | 8e-06 |  |
| [[SLC26A7]] | +0.70 | +0.81 / +0.53 | both halves | 1e-05 |  |
| [[ST8SIA5]] | +0.68 | +0.79 / +0.46 | both halves | 3e-05 |  |
| [[NEB]] | +0.67 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[BAALC-AS1]] | +0.67 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[TPTE2]] | +0.67 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[CMYA5]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[LINC01208]] | +0.66 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[CFAP70]] | +0.65 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[CHODL]] | +0.65 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[LINC02763]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[HSD17B3]] | +0.64 | +0.67 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L2HGDH]] | -0.56 | -0.54 / -0.28 | both halves | 3e-04 | same gene group |
| [[MTERF3]] | -0.56 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[POMGNT2]] | -0.55 | -0.64 / -0.21 | both halves | 7e-04 |  |
| [[GK5]] | -0.54 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[COPG2]] | -0.54 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[PDSS1]] | -0.53 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[WASF3]] | -0.53 | -0.69 / -0.07 | ⚠ one half (not replicated) | 0.004 |  |
| [[TAF5L]] | -0.53 | -0.63 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02641]] | B | LINC02641 activity raises COLQ's level | lines that do not express LINC02641 (14) vs lines expressing it (36) | 1.73× lower at baseline in the lines without LINC02641 | 0.032 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers COLQ's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[WASF3]] | B | WASF3 activity raises COLQ's level | lines that do not express WASF3 (21) vs lines expressing it (29) | 1.49× lower at baseline in the lines without WASF3 | 0.076 | ⚠ within organs, on part of the lines; also absent: SDC2, COL4A4, IGF2BP1 |
| [[IGSF11]] | B | IGSF11 activity raises COLQ's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.69× lower at baseline in the lines without IGSF11 | 0.077 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises COLQ's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.86× lower at baseline in the lines without FSIP2-AS1 | 0.088 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[LINC01762]] | B | LINC01762 activity raises COLQ's level | lines that do not express LINC01762 (5) vs lines expressing it (45) | 1.92× lower at baseline in the lines without LINC01762 | 0.094 | ⚠ within organs, on part of the lines; also absent: MPP4, LINC01429, DNAH6; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.688). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (13.5, 16.8); signed map (22.8, 1.0). **Vector** length 63.8, 9.81% of its response variance represented; |z| ≥ 3 in 1,158 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.0 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +17.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +9.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +9.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.3 | +5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +4.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -8.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | -4.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | collagen like tail subunit of asymmetric acetylcholinesterase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:15,450,133-15,521,751 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EAD |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y215](https://www.uniprot.org/uniprotkb/Q9Y215) (Acetylcholinesterase collagenic tail peptide):

> Anchors the catalytic subunits of asymmetric AChE to the synaptic basal membrane, and is therefore involved in the down-regulation of colinergic synaptic transmission.

**Summary**, from NCBI Gene [8292](https://www.ncbi.nlm.nih.gov/gene/8292):

> This gene encodes the subunit of a collagen-like molecule associated with acetylcholinesterase in skeletal muscle. Each molecule is composed of three identical subunits. Each subunit contains a proline-rich attachment domain (PRAD) that binds an acetylcholinesterase tetramer to anchor the catalytic subunit of the enzyme to the basal lamina. Mutations in this gene are associated with endplate acetylcholinesterase deficiency. Multiple transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:2226](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2226) · Entrez [8292](https://www.ncbi.nlm.nih.gov/gene/8292) · UniProt [Q9Y215](https://www.uniprot.org/uniprotkb/Q9Y215) · Ensembl [ENSG00000206561](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206561)

## Data

Gene col 13051: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13051); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13051, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13051]; `tensor/DDL_lfc|DDL_z.npy` [13051]; `embed/gene_vectors.npy` [13051]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13051 or target_col == 13051). Every well: [[COLQ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COLQ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
