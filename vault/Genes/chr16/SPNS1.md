---
symbol: "SPNS1"
type: "gene"
col: 9834
ensembl_id: "ENSG00000169682"
name: "SPNS lysolipid transporter 1, lysophospholipid"
location: "16p11.2"
module: 122
arm: "+"
pooled_cpm: 13.93
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 4
n_dd_up_clean: 27
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# SPNS1

*SPNS lysolipid transporter 1, lysophospholipid* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.34× (z +13.9, q 3e-41, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.689× (z -8.6, q 3e-15, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEXA]] (+0.78, fdr 7e-06), [[GNPTG]] (+0.78, fdr 7e-06), [[GET3]] (+0.70, fdr 7e-06); moves opposite to [[SPDL1]] (-0.50, fdr 3e-05), [[ZNF217]] (-0.47, fdr 1e-04).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC26A11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9834.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.34×** | +13.9 | 3e-41 | 40/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.26×** | +13.4 | 2e-38 | 42/47 (SW480, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +11.4 | 1e-27 | 35/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +9.3 | 2e-18 | 33/46 (NCI-H2030, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.75×** | +9.1 | 9e-18 | 31/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +8.0 | 1e-13 | 32/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +7.4 | 1e-11 | 21/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +7.1 | 7e-11 | 27/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +7.1 | 8e-11 | 28/48 (J82, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +7.0 | 1e-10 | 23/43 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +7.0 | 1e-10 | 26/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.50×** | +6.6 | 2e-09 | 24/47 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +5.8 | 3e-07 | 21/48 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +5.7 | 4e-07 | 18/47 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +5.3 | 5e-06 | 22/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +5.1 | 1e-05 | 18/47 (PANC-1, LoVo, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.68×** | +4.4 | 3e-04 | 13/43 (A-427, SW480, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.67×** | +4.4 | 3e-04 | 11/47 (NCI-H1573, A549, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.62×** | +4.1 | 1e-03 | 14/48 (NCI-H1573, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9834.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.689×** | -8.6 | 3e-15 | 31/48 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.691×** | -6.1 | 4e-07 | 23/47 (SHP-77, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.660×** | -3.6 | 0.067 | 8/46 (HEC-1-A, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.805×** | -3.4 | 0.083 | 9/47 (C32, KATO III, …) | top dose only |  |
| [[Busulfan (drug)]] 5 µM |  | 0.874× | -3.1 | 0.20 | 8/48 (SNU-1, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9834. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +14.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.77× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 18.0 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +13.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.75× (z +13.0) | — |
| [[PANC-1 (line)]] | alt | 13.7 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.90× (z +12.9) | — |
| [[SW480 (line)]] | alt | 10.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.64× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 14.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.21× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 16.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.50× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 13.0 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0945× (z -10.5) |
| [[J82 (line)]] | alt | 16.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 12.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.45× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.154× (z -8.6) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 21.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +10.0) | — |
| [[SW48 (line)]] | wt | 9.98 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0740× (z -9.2) |
| [[A-172 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9834), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEXA]] | +0.78 | +0.73 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[GNPTG]] | +0.78 | +0.80 / +0.81 | both halves | 7e-06 |  |
| [[GET3]] | +0.70 | +0.60 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[MCOLN1]] | +0.69 | +0.54 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[GLMP]] | +0.66 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[CTSA]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[COMMD9]] | +0.65 | +0.53 / +0.77 | both halves | 1e-05 |  |
| [[CLN3]] | +0.64 | +0.66 / +0.65 | both halves | 7e-06 | STRING 413 |
| [[NAGPA]] | +0.63 | +0.42 / +0.72 | both halves | 4e-05 |  |
| [[AP5Z1]] | +0.63 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[MYL6B]] | +0.62 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[TSC1]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPDL1]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ZNF217]] | -0.47 | -0.36 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC26A11]] | B | SLC26A11 activity raises SPNS1's level | lines that do not express SLC26A11 (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without SLC26A11 | 0.089 | ⚠ within organs, on part of the lines; also absent: DENND5B, SMAD4, MINAR1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.9, -17.4); signed map (-10.1, -20.4). **Vector** length 74.2, 13.4% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.2 | +13.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.1 | +7.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +11.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.1 | +13.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.1 | +4.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.5 | -6.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | +0.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -0.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -0.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | SPNS lysolipid transporter 1, lysophospholipid |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:28,974,221-28,984,548 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSpin1, nrs, SPINL, PP2030, SPIN1, LAT, SLC63A1 |
| Gene groups (HGNC) | Solute carrier family 63, sphingosine phosphate transporters |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2V7](https://www.uniprot.org/uniprotkb/Q9H2V7) (Protein spinster homolog 1):

> Plays a critical role in the phospholipid salvage pathway from lysosomes to the cytosol. Mediates the rate-limiting, proton-dependent, lysosomal efflux of lysophospholipids, which can then be reacylated by acyltransferases in the endoplasmic reticulum to form phospholipids. Selective for zwitterionic headgroups such as lysophosphatidylcholine (LPC) and lysophosphatidylethanolamine (LPE), can also transport lysophosphatidylglycerol (LPG), but not other anionic lysophospholipids, sphingosine, nor …

**Summary**, from NCBI Gene [83985](https://www.ncbi.nlm.nih.gov/gene/83985):

> Enables lysophospholipid:sodium symporter activity. Involved in lysophospholipid transport. Located in lysosomal membrane. Is active in lysosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30621](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30621) · Entrez [83985](https://www.ncbi.nlm.nih.gov/gene/83985) · UniProt [Q9H2V7](https://www.uniprot.org/uniprotkb/Q9H2V7) · Ensembl [ENSG00000169682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169682)

## Data

Gene col 9834: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9834); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9834, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9834]; `tensor/DDL_lfc|DDL_z.npy` [9834]; `embed/gene_vectors.npy` [9834]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9834 or target_col == 9834). Every well: [[SPNS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPNS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
