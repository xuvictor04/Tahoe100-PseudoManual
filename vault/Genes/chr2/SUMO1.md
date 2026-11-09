---
symbol: "SUMO1"
type: "gene"
col: 3753
ensembl_id: "ENSG00000116030"
name: "small ubiquitin like modifier 1"
location: "2q33.1"
module: 20
arm: "+"
pooled_cpm: 54.48
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# SUMO1

*small ubiquitin like modifier 1* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.74× (z +10.8, q 1e-24, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.682× (z -8.5, q 9e-15, down in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.396×, SW480 0.532×, AsPC-1 0.429×, NCI-H2347 0.605×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.154×; ⚠ cell-cycle shift, explains ~0% of this change); [[Monocrotaline (drug)]] 0.05 µM in 1 line (AN3 CA 0.0618×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (CHP-212 0.0682×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPS7B]] (+0.73, fdr 7e-06), [[RPL6]] (+0.69, fdr 7e-06), [[POLR2B]] (+0.68, fdr 7e-06); moves opposite to [[TRIM47]] (-0.61, fdr 7e-06), [[AK6]] (-0.60, fdr 7e-06), [[NBPF10]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MRPS30-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3753.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.74×** | +10.8 | 1e-24 | 46/49 (NCI-H1573, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.94×** | +8.9 | 2e-16 | 42/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +7.0 | 6e-10 | 33/49 (SW480, A549, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +6.7 | 3e-09 | 38/47 (LoVo, AsPC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +6.5 | 1e-08 | 33/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +6.0 | 1e-07 | 28/45 (SW480, RKO, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +6.0 | 1e-07 | 22/35 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +5.2 | 2e-05 | 32/48 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.0 | 4e-05 | 30/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +4.9 | 7e-05 | 30/48 (NCI-H1573, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +4.7 | 1e-04 | 25/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.6 | 2e-04 | 25/45 (MIA PaCa-2, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.5 | 4e-04 | 22/43 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.002 | 27/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.9 | 0.003 | 0/49 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.006 | 24/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3753.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.396×, SW480 0.532×, AsPC-1 0.429×, NCI-H2347 0.605×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.154×; ⚠ cell-cycle shift, explains ~0% of this change); [[Monocrotaline (drug)]] 0.05 µM in 1 line (AN3 CA 0.0618×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (CHP-212 0.0682×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.682×** | -8.5 | 9e-15 | 40/48 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.786×** | -3.8 | 0.043 | 24/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.807× | -3.4 | 0.14 | 19/48 (AsPC-1, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.742× | -3.2 | 0.20 | 19/48 (SW 1271, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.748× | -3.1 | 0.22 | 19/47 (NCI-H460, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | 0.691× | -3.0 | 0.22 | 14/48 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3753. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 50.2 | 6 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.24× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 62.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.396× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 51.0 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.89× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 46.1 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.28× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 57.7 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 60.8 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0618× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 73.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -10.8) |
| [[C-33 A (line)]] | alt | 59.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -13.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 59.0 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0682× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 52.9 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 5.12× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 33.6 | 0 | 1 (1 ⚠) | — | [[Torkinib (drug)]] 5 µM 0.110× (z -8.9) ⚠ toxic |
| [[LoVo (line)]] | wt | 31.8 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.87× (z +9.4) ⚠ toxic | — |
| [[NCI-H2347 (line)]] | alt | 74.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.605× (z -8.5) |
| [[RKO (line)]] | wt | 50.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.07× (z +8.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 61.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.82× (z +8.9) | — |
| [[A-172 (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3753), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS7B]] | +0.73 | +0.74 / +0.68 | both halves | 7e-06 | pathway: Global Genome Nucleotide Excision Repair (GG-NER) |
| [[RPL6]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[POLR2B]] | +0.68 | +0.61 / +0.69 | both halves | 7e-06 | pathway: Nucleotide Excision Repair |
| [[NUDT21]] | +0.67 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[RPS3A]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[ILRUN]] | +0.65 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[CNPY3]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[NPEPPSP1]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[C1D]] | +0.63 | +0.57 / +0.70 | both halves | 9e-06 |  |
| [[RAD23B]] | +0.63 | +0.71 / +0.59 | both halves | 7e-06 | pathway: Formation of Incision Complex in GG-NER; STRING 715 |
| [[SDHAP4]] | +0.63 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[TSFM]] | +0.63 | +0.64 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM47]] | -0.61 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[AK6]] | -0.60 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[NBPF10]] | -0.59 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[YIF1A]] | -0.59 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[TUBB4B]] | -0.58 | -0.62 / -0.55 | both halves | 1e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[LCAT]] | -0.58 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[FBXL6]] | -0.57 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.57 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[METTL23]] | -0.56 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[NBPF19]] | -0.56 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[HMGXB4]] | -0.56 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[LIME1]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MRPS30-DT]] | B | MRPS30-DT activity raises SUMO1's level | lines that do not express MRPS30-DT (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without MRPS30-DT | 0.093 | ⚠ within organs, on part of the lines; also absent: PIP4P2, ENSG00000277611 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.622). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-10.5, -14.8); signed map (-25.2, -33.1). **Vector** length 113, 31.0% of its response variance represented; |z| ≥ 3 in 879 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *L13a-mediated translational silencing of Ceruloplasmin expression* (reactome, mean cos +0.51 to 11); *GTP hydrolysis and joining of the 60S ribosomal subunit* (reactome, mean cos +0.51 to 11); *Eukaryotic Translation Elongation* (reactome, mean cos +0.51 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.2 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +4.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.6 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | -0.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.2 | -8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.4 | -1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.4 | -2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.1 | -2.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.1 | -2.1 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | small ubiquitin like modifier 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:202,206,182-202,238,599 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PIC1, GMP1, SMT3C, SUMO-1, SMT3H3, OFC10; previously UBL1 |
| Gene groups (HGNC) | Small ubiquitin like modifier family |
| Reactome | 59 pathways, smallest: SUMOylation of nuclear envelope proteins; SUMO is conjugated to E1 (UBA2:SAE1); SUMO is proteolytically processed |
| Matched by | ensembl_id |

**Function**, from UniProt [P63165](https://www.uniprot.org/uniprotkb/P63165) (Small ubiquitin-related modifier 1):

> Ubiquitin-like protein that can be covalently attached to proteins as a monomer or a lysine-linked polymer. Covalent attachment via an isopeptide bond to its substrates requires prior activation by the E1 complex SAE1-SAE2 and linkage to the E2 enzyme UBE2I, and can be promoted by E3 ligases such as PIAS1-4, RANBP2 or CBX4. This post-translational modification on lysine residues of proteins plays a crucial role in a number of cellular processes such as nuclear transport, DNA replication and …

**Summary**, from NCBI Gene [7341](https://www.ncbi.nlm.nih.gov/gene/7341):

> This gene encodes a protein that is a member of the SUMO (small ubiquitin-like modifier) protein family. It functions in a manner similar to ubiquitin in that it is bound to target proteins as part of a post-translational modification system. However, unlike ubiquitin which targets proteins for degradation, this protein is involved in a variety of cellular processes, such as nuclear transport, transcriptional regulation, apoptosis, and protein stability. It is not active until the last four …

**Accessions** — [HGNC:12502](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12502) · Entrez [7341](https://www.ncbi.nlm.nih.gov/gene/7341) · UniProt [P63165](https://www.uniprot.org/uniprotkb/P63165) · Ensembl [ENSG00000116030](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116030)

## Data

Gene col 3753: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3753); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3753, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3753]; `tensor/DDL_lfc|DDL_z.npy` [3753]; `embed/gene_vectors.npy` [3753]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3753 or target_col == 3753). Every well: [[SUMO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUMO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
