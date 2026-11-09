---
symbol: "SDHAF1"
type: "gene"
col: 12951
ensembl_id: "ENSG00000205138"
name: "succinate dehydrogenase complex assembly factor 1"
location: "19q13.12"
module: 54
arm: "+"
pooled_cpm: 3.2
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# SDHAF1

*succinate dehydrogenase complex assembly factor 1* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.93× (z +4.9, q 5e-04, up in 8 of 17 measured lines) ⚠ toxic. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.28× (z +3.5, q 0.057, up in 3 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.428× (z -9.4, q 3e-18, down in 27 of 33 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (C32 0.0682×, HOP62 0.158×, NCI-H460 0.139×, NCI-H2030 0.135×, …); [[Harringtonine (drug)]] 5 µM in 1 line (A498 0.0868×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.0917×; ⚠ toxic; transcription drop); [[Bergenin (drug)]] 0.5 µM in 1 line (NCI-H460 0.0641×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POP7]] (+0.77, fdr 7e-06), [[MRPL55]] (+0.75, fdr 1e-05), [[NCBP2AS2]] (+0.71, fdr 1e-05); moves opposite to [[TAF9B]] (-0.68, fdr 1e-05), [[CCDC50]] (-0.67, fdr 5e-05), [[CROCC]] (-0.67, fdr 2e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MYLK]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12951.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +4.9 | 5e-04 | 8/17 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.84×** | +4.7 | 6e-04 | 12/17 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.66×** | +3.9 | 0.016 | 11/46 (A549, LOX-IMVI, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.28×** | +3.5 | 0.057 | 3/17 (HOP62, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.56×** | +3.4 | 0.066 | 15/44 (A549, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | 1.51× | +3.2 | 0.14 | 8/35 (HEC-1-A, SNU-423, …) | two highest doses | cell-cycle shift (explains ~19% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12951.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (C32 0.0682×, HOP62 0.158×, NCI-H460 0.139×, NCI-H2030 0.135×, …); [[Harringtonine (drug)]] 5 µM in 1 line (A498 0.0868×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.0917×; ⚠ toxic; transcription drop); [[Bergenin (drug)]] 0.5 µM in 1 line (NCI-H460 0.0641×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.428×** | -9.4 | 3e-18 | 27/33 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.659× | -3.3 | 0.29 | 10/33 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | 0.663× | -3.1 | 0.29 | 15/41 (A498, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.653× | -3.1 | 0.29 | 8/44 (SW 900, Hs 766T, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12951. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 5.08 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0868× (z -10.3) |
| [[HOP62 (line)]] | alt | 3.67 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 2.49 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -9.7) |
| [[C32 (line)]] | wt | 2.79 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0682× (z -10.4) |
| [[HS-578T (line)]] | alt | 4.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0597× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 3.31 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -8.9) |
| [[PANC-1 (line)]] | alt | 3.53 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0917× (z -9.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 3.67 | 0 | 1 | — | [[Ferulic acid (drug)]] 5 µM 0.0687× (z -8.5) |
| [[A-172 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12951), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP7]] | +0.77 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[MRPL55]] | +0.75 | +0.55 / +0.80 | both halves | 1e-05 |  |
| [[NCBP2AS2]] | +0.71 | +0.49 / +0.77 | both halves | 1e-05 |  |
| [[MPG]] | +0.70 | +0.44 / +0.71 | both halves | 3e-05 |  |
| [[TMEM11]] | +0.70 | +0.50 / +0.81 | both halves | 1e-05 |  |
| [[MALSU1]] | +0.70 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[NR2F6]] | +0.70 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[NUDT22]] | +0.69 | +0.39 / +0.75 | both halves | 6e-05 |  |
| [[SF3B5]] ⚠ | +0.69 | +0.41 / +0.70 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SMYD4]] | +0.69 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[XYLT2]] | +0.69 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[CCDC107]] | +0.68 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[DEXI]] | +0.67 | +0.54 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF9B]] | -0.68 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[CCDC50]] | -0.67 | -0.40 / -0.67 | both halves | 5e-05 |  |
| [[CROCC]] | -0.67 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[GMFB]] | -0.66 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[EWSR1]] | -0.65 | -0.29 / -0.70 | both halves | 2e-04 |  |
| [[ZNF655]] | -0.64 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[GALC]] | -0.64 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[CLASP1-AS1]] | -0.64 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[SDCBP2-AS1]] | -0.64 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[PIEZO1]] | -0.62 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[HDHD2]] | -0.62 | -0.30 / -0.61 | both halves | 2e-04 |  |
| [[LIN7C]] | -0.61 | -0.32 / -0.69 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYLK]] | B | MYLK activity raises SDHAF1's level | lines that do not express MYLK (20) vs lines expressing it (30) | 1.09× lower at baseline in the lines without MYLK | 0.093 | ⚠ within organs, on part of the lines; also absent: ADAMTS2, COL4A1, CPEB1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.786). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-43.3, -12.6); signed map (-35.2, 3.7). **Vector** length 56.4, 8.99% of its response variance represented; |z| ≥ 3 in 707 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial ribosome-associated quality control* (reactome, mean cos +0.57 to 9); *Mitochondrial translation* (reactome, mean cos +0.57 to 9); *Mitochondrial translation elongation* (reactome, mean cos +0.56 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +2.4 | +3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +2.0 | +3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | -0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.8 | +0.7 |
|  | [[TAK-901 (drug)]] 0.5 µM |  | +0.8 | +1.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +0.7 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.7 | -1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.5 | +2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | -9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.4 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | +0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | succinate dehydrogenase complex assembly factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,995,188-35,996,312 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LYRM8 |
| Gene groups (HGNC) | LYR motif containing; Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Maturation of TCA enzymes and regulation of TCA cycle; Citric acid cycle (TCA cycle); Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NFY7](https://www.uniprot.org/uniprotkb/A6NFY7) (Succinate dehydrogenase assembly factor 1, mitochondrial):

> Plays an essential role in the assembly of succinate dehydrogenase (SDH), an enzyme complex (also referred to as respiratory complex II) that is a component of both the tricarboxylic acid (TCA) cycle and the mitochondrial electron transport chain, and which couples the oxidation of succinate to fumarate with the reduction of ubiquinone (coenzyme Q) to ubiquinol. Promotes maturation of the iron-sulfur protein subunit SDHB of the SDH catalytic dimer, protecting it from the deleterious effects of …

**Summary**, from NCBI Gene [644096](https://www.ncbi.nlm.nih.gov/gene/644096):

> The succinate dehydrogenase (SDH) complex (or complex II) of the mitochondrial respiratory chain is composed of 4 individual subunits. The protein encoded by this gene resides in the mitochondria, and is essential for SDH assembly, but does not physically associate with the complex in vivo. Mutations in this gene are associated with SDH-defective infantile leukoencephalopathy (mitochondrial complex II deficiency).[provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:33867](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33867) · Entrez [644096](https://www.ncbi.nlm.nih.gov/gene/644096) · UniProt [A6NFY7](https://www.uniprot.org/uniprotkb/A6NFY7) · Ensembl [ENSG00000205138](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205138)

## Data

Gene col 12951: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12951); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12951, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12951]; `tensor/DDL_lfc|DDL_z.npy` [12951]; `embed/gene_vectors.npy` [12951]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12951 or target_col == 12951). Every well: [[SDHAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDHAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
