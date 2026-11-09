---
symbol: "RRN3P1"
type: "gene"
col: 14520
ensembl_id: "ENSG00000248124"
name: "RRN3 pseudogene 1"
location: "16p12.2"
module: 1
arm: "+"
pooled_cpm: 4.05
n_lines_expressing: 41
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RRN3P1

*RRN3 pseudogene 1* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.66× (z +6.6, q 2e-08, up in 13 of 37 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 3.01× (z +5.3, q 3e-05, up in 11 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.551× (z -5.5, q 2e-05, down in 13 of 21 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Thymol (drug)]] 5 µM: 0.723× (z -4.2, q 0.007, down in 15 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPRYD4]] (+0.68, fdr 1e-05), [[TIGD1]] (+0.66, fdr 1e-05), [[ZNF783]] (+0.64, fdr 1e-05, ⚠ ZNF783 in the vector space only through flagged drug-doses), [[ZNF225]] (+0.61, fdr 1e-05); moves opposite to [[FRYL]] (-0.56, fdr 2e-05), [[RAPGEF2]] (-0.55, fdr 3e-05), [[NBEAL1]] (-0.54, fdr 8e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GPRASP1]] → it (grade C ⚠); 2 go from it, the strongest it → [[C3orf33]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14520.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.66×** | +6.6 | 2e-08 | 13/37 (CFPAC-1, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **3.01×** | +5.3 | 3e-05 | 11/26 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.98×** | +5.2 | 3e-05 | 16/35 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.75×** | +5.1 | 4e-05 | 12/36 (PANC-1, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +5.0 | 8e-05 | 15/32 (Panc 03.27, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +4.9 | 1e-04 | 13/32 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.074 | 0/37 | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.074 | 3/37 (CFPAC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.43× | +3.1 | 0.12 | 5/36 (J82, KATO III, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.39× | +3.0 | 0.14 | 9/35 (NCI-H460, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14520.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.551×** | -5.5 | 2e-05 | 13/21 (NCI-H1792, RPMI-7951, …) | inconsistent across doses | composition shift; position effect removed |
| [[Thymol (drug)]] 5 µM |  | **0.723×** | -4.2 | 0.007 | 15/37 (LOX-IMVI, HEC-1-A, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.549×** | -3.9 | 0.016 | 14/27 (NCI-H1792, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | **0.690×** | -3.4 | 0.091 | 10/36 (CHP-212, SW48, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.685×** | -3.4 | 0.091 | 6/30 (LOX-IMVI, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -3.3 | 0.095 | 11/32 (LS 180, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.710× | -3.0 | 0.20 | 8/36 (SW48, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14520. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 12.8 | 0 | 2 | — | [[Flutamide (drug)]] 0.5 µM 0.121× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 4.27 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0765× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 5.56 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0878× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.575 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.511 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.43 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14520), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRYD4]] | +0.68 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[TIGD1]] | +0.66 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[ZNF783]] ⚠ | +0.64 | +0.58 / +0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF225]] | +0.61 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ZNF256]] | +0.59 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[ZNF202]] | +0.58 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ZNF502]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[SPIN3]] | +0.56 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[SETD4]] | +0.56 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[PIGC]] | +0.55 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[ZNF485]] | +0.55 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[ZNF283]] | +0.55 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[PGBD2]] | +0.55 | +0.54 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRYL]] | -0.56 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[RAPGEF2]] | -0.55 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[NBEAL1]] | -0.54 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[RASSF7]] | -0.52 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[MPC2]] | -0.52 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[GNB2]] | -0.51 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[ARIH1]] | -0.50 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[FNBP1]] | -0.50 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[TSEN34]] | -0.49 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[PCSK1N]] | -0.49 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[HECTD4]] | -0.49 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[TOM1L2]] | -0.48 | -0.30 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRASP1]] | C | GPRASP1's natural level weakens RRN3P1's drug response | GPRASP1's natural level across 38 lines (lineage-adjusted; a glimpse) | r -0.73, reverse +0.11; direction not clear | 0.059 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C3orf33]] | B | RRN3P1 activity lowers C3orf33's level | lines that do not express RRN3P1 (9) vs lines expressing it (41) | 1.27× higher at baseline in the lines without RRN3P1 | 0.080 | ⚠ within organs, on part of the lines; co-absent genes |
| [[ATXN7L2]] | B | RRN3P1 activity lowers ATXN7L2's level | lines that do not express RRN3P1 (9) vs lines expressing it (41) | 1.15× higher at baseline in the lines without RRN3P1 | 0.088 | ⚠ within organs, on part of the lines; co-absent genes |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.5, -3.7); signed map (4.2, -41.6). **Vector** length 41.7, 5.08% of its response variance represented; |z| ≥ 3 in 801 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.2 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.2 | +2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.0 | +0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.0 | +1.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +0.9 | +0.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | RRN3 pseudogene 1 |
| Locus type | pseudogene |
| Location | 16p12.2 — chr16:21,797,750-21,820,384 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

UniProt [Q2M238](https://www.uniprot.org/uniprotkb/Q2M238) carries no function annotation.

**Summary**, from NCBI Gene [730092](https://www.ncbi.nlm.nih.gov/gene/730092):

> Predicted to enable RNA polymerase I general transcription initiation factor activity. Predicted to be involved in SRP-dependent cotranslational protein targeting to membrane, signal sequence recognition and transcription initiation at RNA polymerase I promoter. Predicted to be part of signal recognition particle, endoplasmic reticulum targeting. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30548](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30548) · Entrez [730092](https://www.ncbi.nlm.nih.gov/gene/730092) · UniProt [Q2M238](https://www.uniprot.org/uniprotkb/Q2M238) · Ensembl [ENSG00000248124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248124)

## Data

Gene col 14520: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14520); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14520, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14520]; `tensor/DDL_lfc|DDL_z.npy` [14520]; `embed/gene_vectors.npy` [14520]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14520 or target_col == 14520). Every well: [[RRN3P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRN3P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
