---
symbol: "TMEM266"
type: "gene"
col: 9852
ensembl_id: "ENSG00000169758"
name: "transmembrane protein 266"
location: "15q24.2"
module: 100
arm: "+"
pooled_cpm: 3.12
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# TMEM266

*transmembrane protein 266* — 15q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.96× (z +17.8, q 0e+00, up in 29 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (C-33 A 0.0703×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (SW480 0.0922×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTBN4]] (+0.72, fdr 7e-06), [[SGCZ]] (+0.68, fdr 7e-06), [[EFHD1]] (+0.66, fdr 7e-06).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[POU3F3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9852.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.96×** | +17.8 | 0e+00 | 29/33 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.80×** | +17.0 | 0e+00 | 34/44 (NCI-H460, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.72×** | +15.3 | 0e+00 | 36/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.56×** | +14.2 | 1e-43 | 2/3 (NCI-H2347, HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.87×** | +12.3 | 2e-32 | 30/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.79×** | +11.9 | 8e-31 | 11/15 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.90×** | +10.5 | 4e-24 | 19/34 (LoVo, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.29×** | +9.6 | 4e-20 | 27/38 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.05×** | +8.4 | 4e-15 | 22/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +8.3 | 6e-15 | 24/44 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +7.8 | 3e-13 | 2/4 (PANC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.64×** | +5.9 | 2e-07 | 9/38 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +5.7 | 6e-07 | 10/40 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.7 | 6e-07 | 4/35 (SW480, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +4.6 | 2e-04 | 2/43 (NCI-H23, HCT15) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Procainamide (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.2 | 9e-04 | 3/38 (A498, Panc 03.27, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.013 | 11/45 (NCI-H23, A549, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.013 | 2/41 (NCI-H2030, SK-MEL-2) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9852.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (C-33 A 0.0703×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (SW480 0.0922×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | 0.739× | -3.5 | 0.17 | 10/39 (C-33 A, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -3.4 | 0.17 | 10/48 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Ivermectin (drug)]] 5 µM |  | 0.763× | -3.2 | 0.30 | 2/46 (HepG2/C3A, NCI-H1792) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.772× | -3.0 | 0.34 | 14/41 (C-33 A, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9852. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0703× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 2.25 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0922× (z -8.8) |
| [[A-172 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9852), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTBN4]] | +0.72 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.68 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[EFHD1]] | +0.66 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[CDH23]] | +0.65 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[SLC26A5]] | +0.65 | +0.46 / +0.77 | both halves | 3e-05 |  |
| [[KANK3]] | +0.65 | +0.50 / +0.77 | both halves | 1e-05 |  |
| [[SLC38A4]] | +0.65 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[KCNB1]] | +0.64 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[NME9]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[CAMK2B]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[GALNT17]] | +0.63 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[ST8SIA1]] | +0.63 | +0.51 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POU3F3]] | B | POU3F3 activity raises TMEM266's level | lines that do not express POU3F3 (34) vs lines expressing it (16) | 1.39× lower at baseline in the lines without POU3F3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PANTR1, EPGN, ENSG00000244468 |
| [[PANTR1]] | B | PANTR1 activity raises TMEM266's level | lines that do not express PANTR1 (37) vs lines expressing it (13) | 1.35× lower at baseline in the lines without PANTR1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: POU3F3, LINC01508, TIMD4 |
| [[ABCA17P]] | B | ABCA17P activity raises TMEM266's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.42× lower at baseline in the lines without ABCA17P | 0.039 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers TMEM266's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAM78B]] | B | FAM78B activity raises TMEM266's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.33× lower at baseline in the lines without FAM78B | 0.099 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.665). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.5, 34.7); signed map (27.4, 20.4). **Vector** length 50.4, 6.23% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +17.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.0 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +11.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | +2.3 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -3.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -2.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.1 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.8 | -1.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 266 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2 — chr15:76,059,958-76,229,121 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38190; previously C15orf27 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2M3C6](https://www.uniprot.org/uniprotkb/Q2M3C6) (Transmembrane protein 266):

> Voltage-sensor protein present on the post-synaptic side of glutamatergic mossy fibers and granule cells in the cerebellum. Despite the presence of a voltage-sensor segment, does not form a functional ion channel and its precise role remains unclear. Undergoes both rapid and slow structural rearrangements in response to changes in voltage. Contains a zinc-binding site that can regulate the slow conformational transition.

**Summary**, from NCBI Gene [123591](https://www.ncbi.nlm.nih.gov/gene/123591):

> Enables protein homodimerization activity. Predicted to be involved in monoatomic ion transport and transmembrane transport. Located in cytosol; dendrite; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26763](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26763) · Entrez [123591](https://www.ncbi.nlm.nih.gov/gene/123591) · UniProt [Q2M3C6](https://www.uniprot.org/uniprotkb/Q2M3C6) · Ensembl [ENSG00000169758](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169758)

## Data

Gene col 9852: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9852); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9852, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9852]; `tensor/DDL_lfc|DDL_z.npy` [9852]; `embed/gene_vectors.npy` [9852]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9852 or target_col == 9852). Every well: [[TMEM266 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM266.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
