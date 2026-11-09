---
symbol: "FAM241B"
type: "gene"
col: 10077
ensembl_id: "ENSG00000171224"
name: "family with sequence similarity 241 member B"
location: "10q22.1"
module: 12
arm: "+"
pooled_cpm: 3.15
n_lines_expressing: 46
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# FAM241B

*family with sequence similarity 241 member B* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 4.03× (z +11.0, q 1e-25, up in 35 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.554× (z -6.6, q 3e-08, down in 24 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (PANC-1 0.193×, J82 0.124×, NCI-H460 0.178×); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.0656×); [[Clofarabine (drug)]] 5 µM in 1 line (A-172 0.0772×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYB5R1]] (+0.71, fdr 7e-06), [[LSM10]] (+0.70, fdr 7e-06), [[ANKRD39]] (+0.69, fdr 9e-06); moves opposite to [[PTBP1]] (-0.56, fdr 2e-05), [[GPAA1]] (-0.56, fdr 2e-05), [[ILF2]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[TOM1L1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10077.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **4.03×** | +11.0 | 1e-25 | 35/38 (SW480, HOP62, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.90×** | +10.8 | 1e-24 | 36/39 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.90×** | +10.2 | 4e-22 | 32/36 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.30×** | +6.6 | 6e-09 | 23/39 (A-427, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.88×** | +5.0 | 6e-05 | 13/20 (SW480, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +5.0 | 6e-05 | 2/4 (A498, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +4.6 | 3e-04 | 12/19 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.22×** | +4.5 | 4e-04 | 14/38 (SW480, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.016 | 5/41 (NCI-H1573, RKO, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +3.6 | 0.018 | 11/41 (HOP62, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.57×** | +3.6 | 0.018 | 11/39 (AsPC-1, C-33 A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +3.5 | 0.021 | 14/40 (A-427, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.26×** | +3.4 | 0.031 | 4/13 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.52×** | +3.3 | 0.038 | 2/17 (PANC-1, A498) | all doses, stronger at high dose | composition shift |
| [[Radotinib (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.046 | 7/40 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.085 | 3/35 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10077.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (PANC-1 0.193×, J82 0.124×, NCI-H460 0.178×); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.0656×); [[Clofarabine (drug)]] 5 µM in 1 line (A-172 0.0772×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.554×** | -6.6 | 3e-08 | 24/31 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.746× | -3.2 | 0.34 | 16/40 (HEC-1-A, SW 900, …) | top dose only |  |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.756× | -3.1 | 0.38 | 4/43 (SW480, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10077. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.15 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0656× (z -9.7) |
| [[SW480 (line)]] | alt | 3.54 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.64× (z +9.2) | — |
| [[A-172 (line)]] | wt | 5.40 | 0 | 1 | — | [[Clofarabine (drug)]] 5 µM 0.0772× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 3.85 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.172× (z -8.9) |
| [[J82 (line)]] | alt | 3.92 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -10.0) |
| [[PANC-1 (line)]] | alt | 5.42 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -11.4) |
| [[A-427 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.919 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.557 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.351 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10077), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5R1]] | +0.71 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[LSM10]] | +0.70 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ANKRD39]] | +0.69 | +0.71 / +0.57 | both halves | 9e-06 |  |
| [[TMEM161A]] | +0.68 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[BLVRA]] | +0.65 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[METTL5]] | +0.65 | +0.41 / +0.70 | both halves | 4e-05 |  |
| [[MRGBP]] | +0.65 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[PUS3]] | +0.64 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[HIBCH]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[BRF2]] | +0.64 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[JOSD2]] | +0.64 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[FLYWCH1]] | +0.64 | +0.69 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTBP1]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[GPAA1]] | -0.56 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ILF2]] | -0.55 | -0.38 / -0.65 | both halves | 6e-05 |  |
| [[HNRNPUL1]] | -0.54 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[RNF170]] | -0.53 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[CFL1]] | -0.53 | -0.43 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOM1L1]] | C | FAM241B activity raises TOM1L1's level | lines that do not express FAM241B (4) vs lines expressing it (46) | 2.48× lower at baseline in the lines without FAM241B | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP8, EPHB2, LRP5; maybe low, not absent; its own permutation p |
| [[PCBD1]] | C | FAM241B activity raises PCBD1's level | lines that do not express FAM241B (4) vs lines expressing it (46) | 2.16× lower at baseline in the lines without FAM241B | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP8, EPHB2, LRP5; maybe low, not absent; its own permutation p |
| [[VEZT]] | C | FAM241B activity raises VEZT's level | lines that do not express FAM241B (4) vs lines expressing it (46) | 2.03× lower at baseline in the lines without FAM241B | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP8, EPHB2, LRP5; maybe low, not absent |
| [[RPP21]] | C | FAM241B activity raises RPP21's level | lines that do not express FAM241B (4) vs lines expressing it (46) | 1.41× lower at baseline in the lines without FAM241B | 0.0997 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP8, EPHB2, LRP5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.427). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-17.6, -8.0); signed map (-19.2, -6.2). **Vector** length 60.3, 10.3% of its response variance represented; |z| ≥ 3 in 771 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.3 | +10.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.8 | +10.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +11.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.4 | +3.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +4.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.9 | -2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 241 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:69,630,247-69,633,596 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C10orf35 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96D05](https://www.uniprot.org/uniprotkb/Q96D05) (Protein FAM241B):

> May play a role in lysosome homeostasis.

**Summary**, from NCBI Gene [219738](https://www.ncbi.nlm.nih.gov/gene/219738):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23519](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23519) · Entrez [219738](https://www.ncbi.nlm.nih.gov/gene/219738) · UniProt [Q96D05](https://www.uniprot.org/uniprotkb/Q96D05) · Ensembl [ENSG00000171224](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171224)

## Data

Gene col 10077: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10077); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10077, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10077]; `tensor/DDL_lfc|DDL_z.npy` [10077]; `embed/gene_vectors.npy` [10077]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10077 or target_col == 10077). Every well: [[FAM241B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM241B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
