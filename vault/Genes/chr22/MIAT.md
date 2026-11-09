---
symbol: "MIAT"
type: "gene"
col: 13485
ensembl_id: "ENSG00000225783"
name: "myocardial infarction associated transcript"
location: "22q12.1"
module: 90
arm: "+"
pooled_cpm: 4.66
n_lines_expressing: 45
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# MIAT

*myocardial infarction associated transcript* — 22q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.43× (z +11.4, q 2e-27, up in 23 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Medroxyprogesterone acetate (drug)]] 5 µM: 0.700× (z -4.5, q 0.003, down in 17 of 38 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HS3ST5]] (+0.62, fdr 1e-05), [[LINC02223]] (+0.62, fdr 1e-05), [[PSD2]] (+0.60, fdr 2e-05).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[JAKMIP2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13485.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.43×** | +11.4 | 2e-27 | 23/41 (MIA PaCa-2, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.66×** | +8.9 | 2e-16 | 19/33 (MIA PaCa-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +8.4 | 1e-14 | 1/7 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.21×** | +7.2 | 9e-11 | 0/13 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +6.2 | 6e-08 | 12/29 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +6.0 | 1e-07 | 1/4 (SHP-77) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +5.0 | 4e-05 | 7/42 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +4.2 | 0.002 | 9/34 (SHP-77, A-172, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.60×** | +4.0 | 0.004 | 6/23 (SHP-77, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.56×** | +3.7 | 0.011 | 3/24 (SK-MEL-2, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.10×** | +3.5 | 0.022 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.47×** | +3.5 | 0.022 | 5/21 (SHP-77, SW1417, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.66×** | +3.3 | 0.045 | 2/9 (SW 900, SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.073 | 4/30 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.074 | 11/32 (SW 900, RPMI-7951, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13485.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.700×** | -4.5 | 0.003 | 17/38 (Panc 03.27, SW1417, …) | inconsistent across doses | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.638×** | -3.9 | 0.022 | 4/40 (SHP-77, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.652×** | -3.9 | 0.022 | 13/38 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.675×** | -3.4 | 0.097 | 10/35 (hTERT-HPNE, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM |  | 0.691× | -3.3 | 0.11 | 6/38 (NCI-H1792, COLO 205, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.709× | -3.1 | 0.19 | 8/27 (RPMI-7951, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13485. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 21.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0223× (z -14.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SHP-77 (line)]] | alt | 99.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -16.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0657× (z -12.3) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 3.56 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.77× (z +9.7) ⚠ position not correctable | — |
| [[A-427 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.638 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.764 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13485), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HS3ST5]] | +0.62 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[LINC02223]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[PSD2]] | +0.60 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[ADAMTS19]] | +0.59 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[CNTNAP2]] | +0.58 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[ENTPD1]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[GPM6A]] | +0.58 | +0.42 / +0.68 | both halves | 4e-05 |  |
| [[LINC01226]] | +0.57 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[LINC01980]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ARHGAP25]] | +0.54 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[LINC02466]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[VENTXP1]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAKMIP2-AS1]] | B | JAKMIP2-AS1 activity raises MIAT's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 2.68× lower at baseline in the lines without JAKMIP2-AS1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[LINC01611]] | B | LINC01611 activity raises MIAT's level | lines that do not express LINC01611 (34) vs lines expressing it (16) | 2.44× lower at baseline in the lines without LINC01611 | 0.012 | ⚠ within organs, on part of the lines; also absent: CDH13, ENSG00000248973, LINC02377 |
| [[SLC25A24P1]] | B | SLC25A24P1 activity raises MIAT's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 2.84× lower at baseline in the lines without SLC25A24P1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2 |
| [[GAP43]] | B | GAP43 activity raises MIAT's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 1.88× lower at baseline in the lines without GAP43 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent |
| [[PCSK1]] | B | PCSK1 activity raises MIAT's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 2.65× lower at baseline in the lines without PCSK1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2 |
| [[ASCL1]] | B | ASCL1 activity raises MIAT's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.55× lower at baseline in the lines without ASCL1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[CALCA]] | B | CALCA activity raises MIAT's level | lines that do not express CALCA (45) vs lines expressing it (5) | 3.48× lower at baseline in the lines without CALCA | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[ST18]] | B | ST18 activity raises MIAT's level | lines that do not express ST18 (39) vs lines expressing it (11) | 1.95× lower at baseline in the lines without ST18 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent |
| [[HS3ST5]] | B | HS3ST5 activity raises MIAT's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.68× lower at baseline in the lines without HS3ST5 | 0.098 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.1, 37.9); signed map (35.7, 17.7). **Vector** length 51.7, 7.00% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +3.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.0 | -3.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -3.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | +0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -0.1 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | myocardial infarction associated transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q12.1 — chr22:26,646,411-26,676,475 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ25967, Rncr2, gomafu, NCRNA00066, LINC00066, lncRNA-MIAT; previously C22orf35 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [440823](https://www.ncbi.nlm.nih.gov/gene/440823):

> This gene encodes a spliced long non-coding RNA that may constitute a component of the nuclear matrix. Altered expression of this locus has been reported to be associated with a susceptibility to myocardial infarction. It has also been proposed that pathways involving this transcript may contribute to the pathophysiology of schizophrenia. A similar gene in mouse has been associated with retinal cell fate determination. Alternatively spliced transcript variants have been identified. [provided by …

**Accessions** — [HGNC:33425](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33425) · Entrez [440823](https://www.ncbi.nlm.nih.gov/gene/440823) · Ensembl [ENSG00000225783](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225783)

## Data

Gene col 13485: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13485); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13485, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13485]; `tensor/DDL_lfc|DDL_z.npy` [13485]; `embed/gene_vectors.npy` [13485]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13485 or target_col == 13485). Every well: [[MIAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
