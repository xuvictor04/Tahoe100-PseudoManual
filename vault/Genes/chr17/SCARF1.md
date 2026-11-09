---
symbol: "SCARF1"
type: "gene"
col: 1087
ensembl_id: "ENSG00000074660"
name: "scavenger receptor class F member 1"
location: "17p13.3"
module: 181
arm: "+"
pooled_cpm: 3.5
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# SCARF1

*scavenger receptor class F member 1* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.23× (z +11.9, q 9e-30, up in 18 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.601× (z -5.3, q 6e-05, down in 13 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL34]] (+0.67, fdr 7e-06), [[ABR]] (+0.62, fdr 2e-05), [[MMRN2]] (+0.62, fdr 3e-05); moves opposite to [[CLASP1]] (-0.51, fdr 1e-05), [[ADAM15]] (-0.50, fdr 7e-05), [[VDAC2]] (-0.49, fdr 3e-05).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC01629]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1087.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +11.9 | 9e-30 | 18/32 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.33×** | +8.9 | 2e-16 | 14/31 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +7.7 | 3e-12 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +6.4 | 2e-08 | 1/7 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +5.4 | 8e-06 | 5/13 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.7 | 2e-04 | 5/29 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.69×** | +3.9 | 0.008 | 1/20 (PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.3 | 0.069 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Allantoin (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +3.2 | 0.069 | 0/32 | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +3.2 | 0.069 | 1/6 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.069 | 5/43 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.078 | 14/38 (A-172, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1087.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.601×** | -5.3 | 6e-05 | 13/44 (PANC-1, H4, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.635×** | -4.8 | 6e-04 | 13/41 (RKO, SW 900, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.649×** | -4.5 | 0.001 | 17/41 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.654×** | -4.3 | 0.002 | 11/31 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.665×** | -4.3 | 0.002 | 19/36 (PANC-1, LS 180, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.522×** | -3.6 | 0.035 | 5/23 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.772×** | -3.3 | 0.078 | 9/44 (SW 900, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.740× | -3.1 | 0.12 | 15/41 (RKO, A-172, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.734× | -3.1 | 0.14 | 6/37 (LOX-IMVI, COLO 205, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.750× | -3.0 | 0.15 | 9/40 (NCI-H23, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1087. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 9.74 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +17.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0666× (z -12.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 21.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.25× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 32.9 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0871× (z -14.6) ⚠ cell-cycle shift, explains ~93% of this change |
| [[HT-29 (line)]] | alt | 4.98 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0858× (z -8.8) ⚠ cell-cycle shift, explains ~93% of this change |
| [[MIA PaCa-2 (line)]] | alt | 9.11 | 0 | 2 (1 ⚠) | — | [[Belumosudil (drug)]] 5 µM 0.0723× (z -11.6) |
| [[PANC-1 (line)]] | alt | 6.10 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +9.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 3.61 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +12.0) | [[Panobinostat (drug)]] 0.05 µM 0.0407× (z -10.0) ⚠ cell-cycle shift, explains ~18% of this change |
| [[A549 (line)]] | wt | 2.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 1.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 2.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +12.5) | — |
| [[A-427 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.902 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1087), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL34]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[ABR]] | +0.62 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[MMRN2]] | +0.62 | +0.71 / +0.45 | both halves | 3e-05 |  |
| [[NANOS3]] | +0.61 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[KCNQ4]] | +0.60 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[COL11A2]] | +0.58 | +0.63 / +0.43 | both halves | 4e-05 |  |
| [[LIME1]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[WNK4]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[TRAF1]] | +0.58 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[PIK3IP1-DT]] | +0.57 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[TGIF2-RAB5IF]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[NEPRO-AS1]] | +0.56 | +0.61 / +0.37 | both halves | 9e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLASP1]] | -0.51 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ADAM15]] | -0.50 | -0.55 / -0.37 | both halves | 7e-05 |  |
| [[VDAC2]] | -0.49 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[XPR1]] | -0.48 | -0.49 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01629]] | B | LINC01629 activity raises SCARF1's level | lines that do not express LINC01629 (30) vs lines expressing it (20) | 1.59× lower at baseline in the lines without LINC01629 | 0.015 | ⚠ within organs, on part of the lines; also absent: XIST, ENSG00000262198, RHEX |
| [[LINC02509]] | B | LINC02509 activity raises SCARF1's level | lines that do not express LINC02509 (35) vs lines expressing it (15) | 1.46× lower at baseline in the lines without LINC02509 | 0.018 | ⚠ within organs, on part of the lines; also absent: POSTN, ITGA11, IRAG2 |
| [[AFF3]] | B | AFF3 activity raises SCARF1's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 1.30× lower at baseline in the lines without AFF3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[TRPM2]] | B | TRPM2 activity lowers SCARF1's level | lines that do not express TRPM2 (11) vs lines expressing it (39) | 1.67× higher at baseline in the lines without TRPM2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.9, -5.3); signed map (24.5, 6.7). **Vector** length 63.0, 9.74% of its response variance represented; |z| ≥ 3 in 1,104 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.1 | +3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.4 | +6.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +1.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.1 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | +1.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.0 | +1.0 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -4.3 |
|  | [[NG25 (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | scavenger receptor class F member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:1,633,858-1,645,744 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SREC, KIAA0149, SREC1 |
| Gene groups (HGNC) | Scavenger receptors |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 3 pathways, smallest: Scavenging by Class F Receptors; Binding and Uptake of Ligands by Scavenger Receptors; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14162](https://www.uniprot.org/uniprotkb/Q14162) (Scavenger receptor class F member 1):

> Mediates the binding and degradation of acetylated low density lipoprotein (Ac-LDL). Mediates heterophilic interactions, suggesting a function as adhesion protein. Plays a role in the regulation of neurite-like outgrowth (By similarity).

**Summary**, from NCBI Gene [8578](https://www.ncbi.nlm.nih.gov/gene/8578):

> The protein encoded by this gene is a scavenger receptor that is expressed in endothelial cells. It regulates the uptake of chemically modified low density lipoproteins, including acetylated low density lipoprotein (Ac-LDL), and it may be involved in atherogenesis. This gene is regulated by the transcription factors ZNF444/EZF-2 and SP1. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2013]

**Accessions** — [HGNC:16820](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16820) · Entrez [8578](https://www.ncbi.nlm.nih.gov/gene/8578) · UniProt [Q14162](https://www.uniprot.org/uniprotkb/Q14162) · Ensembl [ENSG00000074660](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074660)

## Data

Gene col 1087: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1087); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1087, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1087]; `tensor/DDL_lfc|DDL_z.npy` [1087]; `embed/gene_vectors.npy` [1087]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1087 or target_col == 1087). Every well: [[SCARF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCARF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
