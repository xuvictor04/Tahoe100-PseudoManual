---
symbol: "MRPL9"
type: "gene"
col: 6743
ensembl_id: "ENSG00000143436"
name: "mitochondrial ribosomal protein L9"
location: "1q21.3"
module: 7
arm: "+"
pooled_cpm: 18.91
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# MRPL9

*mitochondrial ribosomal protein L9* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.88× (z +9.8, q 6e-20, up in 30 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.66× (z +7.9, q 7e-13, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.713× (z -7.4, q 9e-11, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTR8]] (+0.74, fdr 7e-06), [[TRUB1]] (+0.71, fdr 7e-06), [[PSMD6]] (+0.71, fdr 7e-06); moves opposite to [[PPP1R14B]] (-0.57, fdr 1e-04), [[SH3GL1]] (-0.57, fdr 3e-05), [[MYL12B]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6743.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.88×** | +9.8 | 6e-20 | 30/40 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +8.8 | 5e-16 | 23/30 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.66×** | +7.9 | 7e-13 | 37/47 (HOP62, NCI-H2030, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +7.8 | 8e-13 | 36/47 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.49×** | +6.2 | 5e-08 | 26/44 (RPMI-7951, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +6.1 | 1e-07 | 28/47 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.47×** | +5.9 | 3e-07 | 25/46 (LS 180, NCI-H1573, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +5.9 | 3e-07 | 22/35 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +5.8 | 4e-07 | 28/46 (CFPAC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.42×** | +5.3 | 8e-06 | 25/44 (NCI-H23, Panc 03.27, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +5.1 | 2e-05 | 24/47 (A498, NCI-H460, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +4.9 | 4e-05 | 20/48 (NCI-H2347, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.38×** | +4.8 | 7e-05 | 21/46 (COLO 205, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +4.7 | 1e-04 | 17/38 (NCI-H1573, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +4.4 | 4e-04 | 17/47 (LS 180, NCI-H1573, …) | all doses, flat | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.009 | 18/47 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.54×** | +3.5 | 0.015 | 11/45 (NCI-H23, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Erdafitinib (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.053 | 8/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6743.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.713×** | -7.4 | 9e-11 | 35/48 (H4, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.657×** | -6.5 | 3e-08 | 28/47 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.692×** | -5.7 | 3e-06 | 25/47 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.712×** | -5.2 | 2e-05 | 28/47 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.746×** | -4.5 | 9e-04 | 22/47 (SW 900, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.783×** | -3.8 | 0.016 | 17/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.635×** | -3.7 | 0.020 | 13/48 (SW480, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trimetrexate (drug)]] 5 µM |  | 0.866× | -3.1 | 0.13 | 11/47 (MIA PaCa-2, SW480, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.759× | -3.0 | 0.16 | 17/46 (hTERT-HPNE, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6743. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 11.3 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0558× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +12.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -10.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[A-172 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6743), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR8]] | +0.74 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[TRUB1]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 | STRING 462 |
| [[PSMD6]] | +0.71 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[ERAL1]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 | pathway: Mitochondrial ribosome-associated quality control; STRING 581 |
| [[RNF6]] | +0.67 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[TCTN1]] | +0.67 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[FECH]] | +0.67 | +0.72 / +0.45 | both halves | 3e-05 |  |
| [[GPN1]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[DNAJA2]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[SMARCE1]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[ZXDB]] | +0.65 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[FUNDC1]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R14B]] | -0.57 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[SH3GL1]] | -0.57 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[MYL12B]] | -0.56 | -0.47 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises MRPL9's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises MRPL9's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.527). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-22.3, 5.0); signed map (6.0, -32.0). **Vector** length 71.6, 13.1% of its response variance represented; |z| ≥ 3 in 847 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.9 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +3.9 | +9.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +2.6 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.7 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.2 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -2.0 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -1.4 | -3.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,759,647-151,763,496 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bL9m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9BYD2](https://www.uniprot.org/uniprotkb/Q9BYD2) carries no function annotation.

**Summary**, from NCBI Gene [65005](https://www.ncbi.nlm.nih.gov/gene/65005):

> This is a nuclear gene encoding a protein component of the 39S subunit of the mitochondrial ribosome. Alternative splicing results in multiple transcript variants. A pseudogene of this gene is found on chromosome 8. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:14277](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14277) · Entrez [65005](https://www.ncbi.nlm.nih.gov/gene/65005) · UniProt [Q9BYD2](https://www.uniprot.org/uniprotkb/Q9BYD2) · Ensembl [ENSG00000143436](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143436)

## Data

Gene col 6743: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6743); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6743, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6743]; `tensor/DDL_lfc|DDL_z.npy` [6743]; `embed/gene_vectors.npy` [6743]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6743 or target_col == 6743). Every well: [[MRPL9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
