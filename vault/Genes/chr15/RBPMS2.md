---
symbol: "RBPMS2"
type: "gene"
col: 9366
ensembl_id: "ENSG00000166831"
name: "RNA binding protein, mRNA processing factor 2"
location: "15q22.31"
module: 102
arm: "+"
pooled_cpm: 2.93
n_lines_expressing: 36
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 17
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# RBPMS2

*RNA binding protein, mRNA processing factor 2* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.09× (z +18.0, q 0e+00, up in 17 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.619× (z -5.4, q 3e-05, down in 14 of 32 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MEGF11]] (+0.68, fdr 1e-05), [[MSI1]] (+0.67, fdr 1e-05), [[ADAM23]] (+0.64, fdr 1e-05); moves opposite to [[IFT172]] (-0.55, fdr 3e-05), [[NPHP1]] (-0.53, fdr 5e-05), [[INIP]] (-0.53, fdr 2e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MSI1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GBX1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9366.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +18.0 | 0e+00 | 17/23 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.64×** | +10.5 | 2e-23 | 4/6 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +9.6 | 1e-19 | 5/7 (A498, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +7.3 | 5e-11 | 6/17 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +6.1 | 2e-07 | 8/22 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +5.9 | 3e-07 | 11/28 (HOP62, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.4 | 6e-06 | 11/33 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.61×** | +5.3 | 7e-06 | 9/32 (AN3 CA, HT-29, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +4.8 | 8e-05 | 7/27 (A-172, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +4.7 | 1e-04 | 8/29 (HT-29, AN3 CA, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +4.5 | 4e-04 | 5/26 (MIA PaCa-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +4.4 | 6e-04 | 1/14 (LoVo) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.14×** | +4.3 | 7e-04 | 1/10 (A-172) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.004 | 5/30 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.42×** | +3.8 | 0.006 | 6/15 (A-172, PANC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.015 | 5/31 (SW480, NCI-H1792, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +3.4 | 0.019 | 1/12 (PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.019 | 2/32 (A-172, SW 900) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 0.05 µM |  | **1.35×** | +3.4 | 0.023 | 0/28 | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.023 | 5/23 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.064 | 0/30 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9366.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.619×** | -5.4 | 3e-05 | 14/32 (A-427, AN3 CA, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.672×** | -4.5 | 0.002 | 14/33 (J82, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.710×** | -3.9 | 0.019 | 7/32 (HEC-1-A, A-172, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.717×** | -3.8 | 0.022 | 13/33 (A-427, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.526×** | -3.7 | 0.029 | 6/27 (A-427, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.05 µM |  | 0.733× | -3.3 | 0.11 | 3/30 (A-172, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.748× | -3.2 | 0.11 | 7/30 (LoVo, A-172, …) | two highest doses | composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.757× | -3.2 | 0.11 | 5/28 (HS-578T, AN3 CA, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.581× | -3.1 | 0.13 | 8/30 (LoVo, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9366. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.12 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -13.2) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 6.23 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.20× (z +12.8) | [[Harringtonine (drug)]] 5 µM 0.154× (z -9.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 10.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -10.1) |
| [[A549 (line)]] | wt | 3.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +10.8) | — |
| [[C-33 A (line)]] | alt | 21.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -8.5) |
| [[J82 (line)]] | alt | 7.21 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 1.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +11.7) | — |
| [[A498 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.321 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.221 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.258 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.249 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.291 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.904 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9366), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEGF11]] | +0.68 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[MSI1]] | +0.67 | +0.56 / +0.56 | both halves | 1e-05 | same gene group |
| [[ADAM23]] | +0.64 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ZNF423]] | +0.61 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[LRRN2]] | +0.59 | +0.63 / +0.40 | both halves | 4e-05 |  |
| [[TEAD3]] | +0.58 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[CDH23]] | +0.57 | +0.33 / +0.60 | both halves | 1e-04 | same gene group |
| [[HDGFL3]] | +0.57 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[SRC]] | +0.57 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[ADCY3]] | +0.57 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[MICALL1]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PHF21B]] | +0.57 | +0.44 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT172]] | -0.55 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[NPHP1]] | -0.53 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[INIP]] | -0.53 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[ABITRAM]] | -0.51 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[ASB8]] | -0.50 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[SPEF2]] | -0.49 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[PKN2]] | -0.49 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[ARL4A]] | -0.48 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[TTC23]] | -0.47 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[TTC26]] | -0.47 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[PTCD3]] | -0.47 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[TOGARAM1]] | -0.47 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSI1]] | B | MSI1 activity raises RBPMS2's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.11× lower at baseline in the lines without MSI1 | 0.037 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[HDAC6]] | B | HDAC6 activity raises RBPMS2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[KCNG3]] | C | KCNG3 activity raises RBPMS2's level | lines that do not express KCNG3 (20) vs lines expressing it (30) | 2.35× lower at baseline in the lines without KCNG3 | 0.010 | ⚠ within organs, on part of the lines; also absent: ELOVL2, LHX2, MAPK8IP2; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBX1]] | B | RBPMS2 activity raises GBX1's level | lines that do not express RBPMS2 (14) vs lines expressing it (36) | 1.98× lower at baseline in the lines without RBPMS2 | 0.006 | ⚠ within organs, on part of the lines; also absent: STOX2, KCNG3, WIPF3 |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.5, 35.8); signed map (26.8, 24.3). **Vector** length 45.9, 7.14% of its response variance represented; |z| ≥ 3 in 701 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +18.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +9.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +5.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +2.9 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -1.9 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.5 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.4 | -3.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.9 | +0.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding protein, mRNA processing factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:64,739,891-64,775,589 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RNA binding motif containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZRY4](https://www.uniprot.org/uniprotkb/Q6ZRY4) (RNA-binding protein with multiple splicing 2):

> RNA-binding protein involved in the regulation of smooth muscle cell differentiation and proliferation in the gastrointestinal system. Binds NOG mRNA, the major inhibitor of the bone morphogenetic protein (BMP) pathway. Mediates an increase of NOG mRNA levels, thereby contributing to the negative regulation of BMP signaling pathway and promoting reversible dedifferentiation and proliferation of smooth muscle cells (By similarity). Acts as a pre-mRNA alternative splicing regulator (By …

**Summary**, from NCBI Gene [348093](https://www.ncbi.nlm.nih.gov/gene/348093):

> The protein encoded by this gene is a member of the RNA recognition motif (RRM)-containing protein family and is involved in the development and dedifferentiation of digestive smooth muscle cells. The encoded protein functions as a homodimer and indirectly inhibits the bone morphogenetic protein pathway. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:19098](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19098) · Entrez [348093](https://www.ncbi.nlm.nih.gov/gene/348093) · UniProt [Q6ZRY4](https://www.uniprot.org/uniprotkb/Q6ZRY4) · Ensembl [ENSG00000166831](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166831)

## Data

Gene col 9366: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9366); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9366, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9366]; `tensor/DDL_lfc|DDL_z.npy` [9366]; `embed/gene_vectors.npy` [9366]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9366 or target_col == 9366). Every well: [[RBPMS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBPMS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
