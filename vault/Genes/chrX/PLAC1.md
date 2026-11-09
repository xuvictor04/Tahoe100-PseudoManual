---
symbol: "PLAC1"
type: "gene"
col: 10037
ensembl_id: "ENSG00000170965"
name: "placenta associated 1"
location: "Xq26.3"
module: 37
arm: "+"
pooled_cpm: 2.88
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 1
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# PLAC1

*placenta associated 1* — Xq26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.20× (z +24.4, q 0e+00, up in 31 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.682× (z -3.9, q 0.060, down in 12 of 39 measured lines) ⚠ cell-cycle shift, explains ~67% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.194×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD200R1]] (+0.70, fdr 7e-06), [[CD247]] (+0.66, fdr 7e-06), [[CELF5]] (+0.63, fdr 1e-04); moves opposite to [[MDM1]] (-0.55, fdr 2e-04), [[ZNF512B]] (-0.51, fdr 1e-04), [[PEX1]] (-0.50, fdr 2e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10037.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.20×** | +24.4 | 0e+00 | 31/31 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **6.46×** | +19.5 | 0e+00 | 45/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **6.40×** | +19.4 | 0e+00 | 37/41 (HEC-1-A, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **3.52×** | +18.6 | 0e+00 | 41/46 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.25×** | +17.3 | 0e+00 | 42/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.17×** | +14.4 | 1e-44 | 14/23 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.41×** | +13.0 | 2e-36 | 30/46 (KATO III, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.44×** | +12.9 | 3e-36 | 34/40 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.23×** | +11.8 | 4e-30 | 24/34 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.97×** | +11.4 | 3e-28 | 33/45 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.00×** | +11.0 | 1e-26 | 11/15 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.15×** | +8.0 | 7e-14 | 20/46 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +7.6 | 1e-12 | 1/5 (SW480) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.67×** | +7.6 | 2e-12 | 9/47 (SW1417, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.94×** | +6.9 | 2e-10 | 15/39 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.72×** | +5.5 | 2e-06 | 5/39 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.18×** | +4.2 | 6e-04 | 6/42 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.46×** | +3.9 | 0.002 | 6/45 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10037.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.194×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.682×** | -3.9 | 0.060 | 12/39 (NCI-H1573, NCI-H2030, …) | rises with dose | composition shift |
| [[8-Hydroxyquinoline (drug)]] 5 µM |  | 0.806× | -3.2 | 0.36 | 5/46 (A549, MIA PaCa-2, …) | top dose only |  |
| [[Quinestrol (drug)]] 5 µM |  | 0.813× | -3.1 | 0.36 | 3/46 (SW 900, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10037. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 4.49 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 5.69× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 4.24 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.75× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 2.26 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.75× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 11.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 7.27× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -8.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 1.63 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +10.2) | — |
| [[A498 (line)]] | wt | 2.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +12.1) | — |
| [[A549 (line)]] | wt | 1.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.6× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 3.14 | 1 | 0 | [[Auranofin (drug)]] 5 µM 23.8× (z +8.7) | — |
| [[A-172 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.833 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10037), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD200R1]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[CD247]] | +0.66 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[CELF5]] | +0.63 | +0.35 / +0.83 | both halves | 1e-04 |  |
| [[C9orf153]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[SNX31]] | +0.62 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[GRK3]] | +0.61 | +0.33 / +0.65 | both halves | 1e-04 |  |
| [[PHKG1]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ANKFN1]] | +0.59 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[CDC26]] | +0.59 | +0.32 / +0.55 | both halves | 2e-04 |  |
| [[HYPK]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[DDN-AS1]] | +0.58 | +0.34 / +0.62 | both halves | 1e-04 |  |
| [[RBM44]] | +0.58 | +0.33 / +0.60 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDM1]] | -0.55 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[ZNF512B]] | -0.51 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[PEX1]] | -0.50 | -0.29 / -0.33 | both halves | 2e-04 |  |
| [[YTHDC2]] | -0.49 | -0.33 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PLAC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01234]] | B | LINC01234 activity raises PLAC1's level | lines that do not express LINC01234 (12) vs lines expressing it (38) | 1.50× lower at baseline in the lines without LINC01234 | 0.058 | ⚠ within organs, on part of the lines; also absent: NXPH4, COP1-DT, LINC00276; maybe low, not absent |
| [[LSP1P5-1]] | B | LSP1P5-1 activity lowers PLAC1's level | lines that do not express LSP1P5-1 (6) vs lines expressing it (44) | 1.28× higher at baseline in the lines without LSP1P5-1 | 0.069 | ⚠ within organs, on part of the lines; also absent: LSP1P4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.0, -19.2); signed map (7.4, 7.5). **Vector** length 58.5, 8.04% of its response variance represented; |z| ≥ 3 in 1,377 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.4 | +19.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +18.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +6.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.8 | +13.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +7.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +0.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -3.0 | -3.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.2 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | placenta associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.3 — chrX:134,565,838-134,764,322 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CT92, OOSP2L, OOSP2B |
| Gene groups (HGNC) | OOSP family |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBJ0](https://www.uniprot.org/uniprotkb/Q9HBJ0) (Placenta-specific protein 1):

> May play a role in placental development.

**Summary**, from NCBI Gene [10761](https://www.ncbi.nlm.nih.gov/gene/10761):

> Involved in placenta development. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9044](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9044) · Entrez [10761](https://www.ncbi.nlm.nih.gov/gene/10761) · UniProt [Q9HBJ0](https://www.uniprot.org/uniprotkb/Q9HBJ0) · Ensembl [ENSG00000170965](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170965)

## Data

Gene col 10037: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10037); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10037, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10037]; `tensor/DDL_lfc|DDL_z.npy` [10037]; `embed/gene_vectors.npy` [10037]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10037 or target_col == 10037). Every well: [[PLAC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLAC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
