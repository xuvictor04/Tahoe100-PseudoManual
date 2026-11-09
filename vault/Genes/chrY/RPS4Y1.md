---
symbol: "RPS4Y1"
type: "gene"
col: 5004
ensembl_id: "ENSG00000129824"
name: "ribosomal protein S4 Y-linked 1"
location: "Yp11.2"
module: 125
arm: "+"
pooled_cpm: 68.85
n_lines_expressing: 20
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# RPS4Y1

*ribosomal protein S4 Y-linked 1* — Yp11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 4.10× (z +13.4, q 2e-38, up in 14 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.58× (z +6.7, q 4e-09, up in 9 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Trametinib (drug)]] 0.05 µM: 0.763× (z -3.9, q 0.058, down in 0 of 18 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02154]] (+0.52, fdr 3e-05), [[RINL]] (+0.50, fdr 7e-05), [[DISC1FP1]] (+0.47, fdr 1e-04); moves opposite to [[VPS45]] (-0.40, fdr 2e-04), [[NPLOC4]] (-0.39, fdr 3e-04), [[ORC6]] (-0.38, fdr 6e-04).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RAMP1]] → it (grade B ⚠); 3 go from it, the strongest it → [[C12orf50]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5004.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.10×** | +13.4 | 2e-38 | 14/17 (NCI-H460, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.55×** | +13.1 | 2e-36 | 9/18 (A-427, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +9.7 | 4e-20 | 9/17 (A-427, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +6.7 | 4e-09 | 9/18 (A-172, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.36×** | +6.5 | 7e-09 | 16/16 (A-172, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.68×** | +5.3 | 1e-05 | 11/18 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +5.3 | 1e-05 | 6/19 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.61×** | +4.9 | 7e-05 | 14/18 (NCI-H460, NCI-H2030, …) | rises with dose | composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.002 | 0/18 | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.77×** | +4.1 | 0.002 | 8/17 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.32×** | +4.0 | 0.003 | 13/18 (A-172, NCI-H460, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.8 | 0.007 | 7/17 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.009 | 9/18 (LoVo, CHP-212, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.59×** | +3.4 | 0.031 | 8/18 (A-427, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.85×** | +3.3 | 0.037 | 17/19 (SNU-1, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.045 | 13/18 (SK-MEL-2, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.56×** | +3.2 | 0.046 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.046 | 1/18 (NCI-H460) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.048 | 14/18 (LoVo, A-427, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.51×** | +3.0 | 0.080 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.50×** | +2.9 | 0.084 | 0/18 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5004.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | **0.763×** | -3.9 | 0.058 | 0/18 | inconsistent across doses |  |
| [[Fingolimod (hydrochloride) (drug)]] 0.05 µM |  | 0.730× | -3.3 | 0.24 | 0/18 | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.733× | -3.2 | 0.24 | 0/18 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.727× | -3.0 | 0.30 | 1/18 (LoVo) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5004. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 224 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.04× (z +16.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 103 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.5) ⚠ cell-cycle shift, explains ~94% of this change | — |
| [[A-427 (line)]] | wt | 73.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.17× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 98.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.95× (z +10.9) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 111 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +8.9) ⚠ cell-cycle shift, explains ~94% of this change | — |
| [[H4 (line)]] | wt | 142 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.42× (z +10.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 120 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.7) ⚠ cell-cycle shift, explains ~94% of this change | — |
| [[LoVo (line)]] | wt | 142 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.30× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 137 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.10× (z +12.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 231 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.37× (z +9.4) | — |
| [[A498 (line)]] | wt | 4.67 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.00 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.02 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.20 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 99.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 222 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 153 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.90 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.94 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.89 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 94.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.23 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.94 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.36 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.26 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 797 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.57 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.58 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.95 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.34 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.44 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.60 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.84 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5004), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02154]] | +0.52 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[RINL]] | +0.50 | +0.43 / +0.38 | both halves | 7e-05 |  |
| [[DISC1FP1]] | +0.47 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[FSTL5]] | +0.47 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[DDX3Y]] | +0.47 | +0.52 / +0.46 | both halves | 3e-05 | same gene group; STRING 963 |
| [[LINC01876]] | +0.46 | +0.44 / +0.35 | both halves | 1e-04 |  |
| [[DNAJC12]] | +0.46 | +0.47 / +0.39 | both halves | 6e-05 |  |
| [[DNAH6]] | +0.45 | +0.54 / +0.29 | both halves | 3e-04 |  |
| [[PLCH2]] | +0.45 | +0.39 / +0.34 | both halves | 1e-04 |  |
| [[ENTHD1]] | +0.45 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[ATP6V1B2]] | +0.45 | +0.36 / +0.44 | both halves | 1e-04 | pathway: Cellular response to starvation |
| [[PNLIPRP3]] | +0.45 | +0.52 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS45]] | -0.40 | -0.30 / -0.41 | both halves | 2e-04 | pathway: SARS-CoV-2 Infection |
| [[NPLOC4]] | -0.39 | -0.28 / -0.46 | both halves | 3e-04 | pathway: Ribosome-associated quality control |
| [[ORC6]] | -0.38 | -0.22 / -0.37 | both halves | 6e-04 |  |
| [[UBN1]] | -0.38 | -0.22 / -0.42 | both halves | 6e-04 |  |
| [[AP4E1]] | -0.37 | -0.21 / -0.41 | both halves | 7e-04 |  |
| [[NFATC2IP]] | -0.37 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[UBE2K]] | -0.37 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[GLYR1]] | -0.37 | -0.21 / -0.42 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAMP1]] | B | RAMP1 activity lowers RPS4Y1's level | lines that do not express RAMP1 (16) vs lines expressing it (34) | 3.13× higher at baseline in the lines without RAMP1 | 0.017 | ⚠ within organs, on part of the lines; also absent: IGFBP6, TRHDE, SDCBP2; maybe low, not absent |
| [[DDX3Y]] | C | DDX3Y activity raises RPS4Y1's level | lines that do not express DDX3Y (30) vs lines expressing it (20) | 10.78× lower at baseline in the lines without DDX3Y | 5e-04 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C12orf50]] | B | RPS4Y1 activity raises C12orf50's level | lines that do not express RPS4Y1 (30) vs lines expressing it (20) | 1.79× lower at baseline in the lines without RPS4Y1 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZFY, PRKY, LINC00278 |
| [[DDX3Y]] | C | RPS4Y1 activity raises DDX3Y's level | lines that do not express RPS4Y1 (30) vs lines expressing it (20) | 12.57× lower at baseline in the lines without RPS4Y1 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZFY, PRKY, LINC00278; co-absent with the target |
| [[ENTHD1]] | C | RPS4Y1 activity raises ENTHD1's level | lines that do not express RPS4Y1 (30) vs lines expressing it (20) | 2.47× lower at baseline in the lines without RPS4Y1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZFY, PRKY, LINC00278; co-absent with the target |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.424). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.0, 38.9); signed map (56.5, 14.8). **Vector** length 44.1, 10.9% of its response variance represented; |z| ≥ 3 in 460 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +3.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +13.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -1.0 | +4.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | +1.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.7 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.7 | +0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -1.6 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -0.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S4 Y-linked 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Yp11.2 — chrY:2,841,602-2,932,000 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5070, MGC119100, S4; previously RPS4Y |
| Gene groups (HGNC) | S ribosomal proteins; Minor histocompatibility antigens |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

UniProt [P22090](https://www.uniprot.org/uniprotkb/P22090) carries no function annotation.

**Summary**, from NCBI Gene [6192](https://www.ncbi.nlm.nih.gov/gene/6192):

> Cytoplasmic ribosomes, organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes ribosomal protein S4, a component of the 40S subunit. Ribosomal protein S4 is the only ribosomal protein known to be encoded by more than one gene, namely this gene and ribosomal protein S4, X-linked (RPS4X). The 2 isoforms encoded by these genes are …

**Accessions** — [HGNC:10425](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10425) · Entrez [6192](https://www.ncbi.nlm.nih.gov/gene/6192) · UniProt [P22090](https://www.uniprot.org/uniprotkb/P22090) · Ensembl [ENSG00000129824](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129824)

## Data

Gene col 5004: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5004); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5004, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5004]; `tensor/DDL_lfc|DDL_z.npy` [5004]; `embed/gene_vectors.npy` [5004]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5004 or target_col == 5004). Every well: [[RPS4Y1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS4Y1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
