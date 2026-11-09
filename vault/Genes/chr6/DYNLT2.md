---
symbol: "DYNLT2"
type: "gene"
col: 11575
ensembl_id: "ENSG00000184786"
name: "dynein light chain Tctex-type 2"
location: "6q27"
module: 15
arm: "+"
pooled_cpm: 2.66
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# DYNLT2

*dynein light chain Tctex-type 2* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 5.28× (z +14.3, q 7e-44, up in 13 of 15 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 4.93× (z +14.3, q 7e-44, up in 36 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bicalutamide (drug)]] 5 µM in 1 line (NCI-H661 0.736×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00115]] (+0.76, fdr 7e-06), [[ZBTB26]] (+0.72, fdr 1e-05), [[HSPE1-MOB4]] (+0.71, fdr 1e-05); moves opposite to [[CLEC16A]] (-0.52, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC01139]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11575.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **5.28×** | +14.3 | 7e-44 | 13/15 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **4.93×** | +14.3 | 7e-44 | 36/40 (A-427, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.04×** | +13.4 | 1e-38 | 4/4 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **2.54×** | +11.8 | 6e-30 | 30/44 (PANC-1, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.63×** | +8.7 | 5e-16 | 31/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.29×** | +7.4 | 1e-11 | 6/15 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +6.9 | 4e-10 | 15/31 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.8 | 7e-10 | 17/33 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +6.4 | 9e-09 | 15/22 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +5.2 | 1e-05 | 1/3 (PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.05×** | +5.2 | 1e-05 | 13/39 (KATO III, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +5.1 | 2e-05 | 10/34 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.65×** | +4.6 | 2e-04 | 0/4 | top dose only | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.64×** | +4.4 | 4e-04 | 13/41 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +4.1 | 0.002 | 13/41 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +4.0 | 0.002 | 10/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.09×** | +3.4 | 0.019 | 8/32 (LS 180, KATO III, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.019 | 3/38 (J82, SW480, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.023 | 4/38 (PANC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.050 | 3/39 (A-172, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.051 | 10/42 (KATO III, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.056 | 9/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11575.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bicalutamide (drug)]] 5 µM in 1 line (NCI-H661 0.736×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.661× | -3.7 | 0.10 | 11/45 (LS 180, PANC-1, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | 0.478× | -3.5 | 0.14 | 7/39 (RKO, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (maleate) (drug)]] 0.05 µM |  | 0.677× | -3.3 | 0.21 | 10/35 (HS-578T, CFPAC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11575. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.95 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 10.8× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 3.73 | 1 | 0 | [[Auranofin (drug)]] 5 µM 16.2× (z +9.5) | — |
| [[A-172 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11575), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00115]] | +0.76 | +0.61 / +0.77 | both halves | 7e-06 |  |
| [[ZBTB26]] | +0.72 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[HSPE1-MOB4]] | +0.71 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[ZNF117]] | +0.70 | +0.30 / +0.76 | both halves | 2e-04 |  |
| [[ZNF596]] | +0.68 | +0.31 / +0.75 | both halves | 2e-04 |  |
| [[GTF3C2-AS2]] | +0.67 | +0.39 / +0.62 | both halves | 6e-05 |  |
| [[ANKRD42-DT]] | +0.66 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[CTTN-DT]] | +0.66 | +0.32 / +0.63 | both halves | 2e-04 |  |
| [[CAPN10-DT]] | +0.65 | +0.41 / +0.67 | both halves | 4e-05 |  |
| [[CCNY-AS1]] | +0.65 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[RAD51-AS1]] | +0.63 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[GOT1-DT]] | +0.62 | +0.38 / +0.59 | both halves | 7e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLEC16A]] | -0.52 | -0.28 / -0.59 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01139]] | B | LINC01139 activity raises DYNLT2's level | lines that do not express LINC01139 (24) vs lines expressing it (26) | 1.11× lower at baseline in the lines without LINC01139 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000260289, NTRK3, CTNNA2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.634). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-7.0, 23.0); signed map (31.1, -17.3). **Vector** length 54.8, 7.40% of its response variance represented; |z| ≥ 3 in 1,036 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.4 | +14.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.3 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +13.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +14.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.3 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -1.1 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -3.5 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.0 | -1.3 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | dynein light chain Tctex-type 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:169,740,109-169,751,587 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TCTEX1D3, TCTEX2, Tctex4, oda12; previously TCTE3 |
| Gene groups (HGNC) | Dyneins, axonemal outer arm complex subunits; Dynein light chain Tctex-type family |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZS6](https://www.uniprot.org/uniprotkb/Q8IZS6) (Dynein light chain Tctex-type protein 2):

> Component of dynein, a family of motor proteins essential for movement along microtubules. Required for structural and functional integrity of cilia (By similarity). Candidate for involvement in male sterility (By similarity).

**Summary**, from NCBI Gene [6991](https://www.ncbi.nlm.nih.gov/gene/6991):

> Predicted to enable dynein intermediate chain binding activity. Predicted to be involved in microtubule-based movement. Predicted to be located in membrane and microtubule. Predicted to be part of cytoplasmic dynein complex. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11695](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11695) · Entrez [6991](https://www.ncbi.nlm.nih.gov/gene/6991) · UniProt [Q8IZS6](https://www.uniprot.org/uniprotkb/Q8IZS6) · Ensembl [ENSG00000184786](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184786)

## Data

Gene col 11575: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11575); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11575, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11575]; `tensor/DDL_lfc|DDL_z.npy` [11575]; `embed/gene_vectors.npy` [11575]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11575 or target_col == 11575). Every well: [[DYNLT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYNLT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
