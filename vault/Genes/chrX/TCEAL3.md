---
symbol: "TCEAL3"
type: "gene"
col: 12225
ensembl_id: "ENSG00000196507"
name: "transcription elongation factor A like 3"
location: "Xq22.2"
module: 59
arm: "+"
pooled_cpm: 18.43
n_lines_expressing: 43
n_dd_up: 9
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# TCEAL3

*transcription elongation factor A like 3* — Xq22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.42× (z +7.2, q 4e-10, up in 39 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.540× (z -5.0, q 3e-04, down in 32 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 1 line (AN3 CA 0.0506×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (H4 0.156×; ⚠ toxic; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARMCX3]] (+0.75, fdr 7e-06), [[TCEAL9]] (+0.72, fdr 7e-06), [[TCEAL1]] (+0.66, fdr 7e-06, ⚠ same locus), [[APBA3]] (+0.65, fdr 1e-05); moves opposite to [[URB1]] (-0.66, fdr 7e-06), [[PRKDC]] (-0.65, fdr 1e-05), [[EFTUD2]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF563]] → it (grade B ⚠); 5 go from it, the strongest it → cells under [[Sodium Salicylate (drug)]] 0.5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12225.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.42×** | +7.2 | 4e-10 | 39/41 (HT-29, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.37×** | +6.7 | 4e-09 | 29/35 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +5.7 | 2e-06 | 15/25 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +5.7 | 2e-06 | 26/36 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.69×** | +4.3 | 0.002 | 26/37 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.66×** | +4.0 | 0.007 | 22/40 (NCI-H2030, SNU-423, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.020 | 25/40 (A498, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.37×** | +3.6 | 0.023 | 17/39 (NCI-H460, A-172, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.098 | 19/41 (A498, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.1 | 0.11 | 2/41 (MIA PaCa-2, HOP62) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12225.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 1 line (AN3 CA 0.0506×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (H4 0.156×; ⚠ toxic; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.540×** | -5.0 | 3e-04 | 32/41 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.567×** | -4.4 | 0.004 | 22/40 (Panc 03.27, C32, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.448× | -3.4 | 0.12 | 23/39 (CFPAC-1, HCT15, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.681× | -3.1 | 0.26 | 18/40 (A549, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.691× | -3.0 | 0.30 | 12/41 (NCI-H2030, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12225. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.14 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 12.3× (z +12.8) | — |
| [[A-172 (line)]] | wt | 21.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 5.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +10.4) | — |
| [[AN3 CA (line)]] | alt | 20.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0506× (z -8.8) |
| [[H4 (line)]] | wt | 31.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.156× (z -8.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 28.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 6.49 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.4× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 30.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12225), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMCX3]] | +0.75 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[TCEAL9]] | +0.72 | +0.68 / +0.75 | both halves | 7e-06 | same gene group; STRING 461 |
| [[TCEAL1]] | +0.66 | +0.68 / +0.62 | both halves | 7e-06 | same gene group; STRING 731; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[APBA3]] | +0.65 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[MITD1]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[SELENOM]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[SNRNP27]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ABCA5]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[MFAP1]] | +0.61 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[ZMYM5]] | +0.60 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[PIGP]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ZNF563]] | +0.60 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[EMP3]] | +0.60 | +0.63 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[URB1]] | -0.66 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[PRKDC]] | -0.65 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.65 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[TUFM]] | -0.64 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[NUP93]] | -0.63 | -0.58 / -0.61 | both halves | 8e-06 |  |
| [[MRPS27]] | -0.62 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[HERC2]] | -0.61 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[SPATA5]] | -0.60 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[CHID1]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ELAC2]] | -0.60 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[C1QBP]] | -0.59 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[DROSHA]] | -0.58 | -0.46 / -0.62 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF563]] | B | ZNF563 activity raises TCEAL3's level | lines that do not express ZNF563 (9) vs lines expressing it (41) | 2.12× lower at baseline in the lines without ZNF563 | 0.013 | ⚠ within organs, on part of the lines; also absent: ZNF442, ZNF433, ENSG00000269755 |
| [[ARMCX1]] | B | ARMCX1 activity raises TCEAL3's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 2.74× lower at baseline in the lines without ARMCX1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1 |
| [[IFI27L2]] | B | IFI27L2 activity raises TCEAL3's level | lines that do not express IFI27L2 (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without IFI27L2 | 0.097 | ⚠ within organs, on part of the lines |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Sodium Salicylate (drug)]] 0.5 µM | B | TCEAL3 activity lowers the cells' numbers under Sodium Salicylate 0.5 µM (makes them more sensitive) | lines that do not express TCEAL3 (7) vs lines expressing it (41) | the lines without TCEAL3: 1.23× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, TTLL7, ENSG00000234405 |
| [[PIGP]] | B | TCEAL3 activity lowers PIGP's level | lines that do not express TCEAL3 (7) vs lines expressing it (43) | 1.30× higher at baseline in the lines without TCEAL3 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, TTLL7, ENSG00000234405 |
| [[MED18]] | B | TCEAL3 activity lowers MED18's level | lines that do not express TCEAL3 (7) vs lines expressing it (43) | 1.32× higher at baseline in the lines without TCEAL3 | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, TTLL7, ENSG00000234405 |
| [[TCEAL9]] | B | TCEAL3 activity raises TCEAL9's level | lines that do not express TCEAL3 (7) vs lines expressing it (43) | 1.75× lower at baseline in the lines without TCEAL3 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, TTLL7, ENSG00000234405 |
| [[UAP1L1]] | B | TCEAL3 activity raises UAP1L1's level | lines that do not express TCEAL3 (7) vs lines expressing it (43) | 2.41× lower at baseline in the lines without TCEAL3 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, TTLL7, ENSG00000234405 |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.676). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-35.0, -31.0); signed map (-10.7, -0.6). **Vector** length 75.8, 19.7% of its response variance represented; |z| ≥ 3 in 557 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.1 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +7.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +4.5 | +4.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.8 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +0.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -3.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -4.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.2 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | transcription elongation factor A like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.2 — chrX:103,607,451-103,629,690 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15737, WEX8 |
| Gene groups (HGNC) | Transcription elongation factor A like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969E4](https://www.uniprot.org/uniprotkb/Q969E4) (Transcription elongation factor A protein-like 3):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [85012](https://www.ncbi.nlm.nih.gov/gene/85012):

> This gene encodes a member of the transcription elongation factor A (SII)-like (TCEAL) gene family. Members of this family contain TFA domains and may function as nuclear phosphoproteins that modulate transcription in a promoter context-dependent manner. Multiple family members are located on the X chromosome. Alternative splicing results in multiple transcript variants encoding a single isoform. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:28247](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28247) · Entrez [85012](https://www.ncbi.nlm.nih.gov/gene/85012) · UniProt [Q969E4](https://www.uniprot.org/uniprotkb/Q969E4) · Ensembl [ENSG00000196507](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196507)

## Data

Gene col 12225: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12225); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12225, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12225]; `tensor/DDL_lfc|DDL_z.npy` [12225]; `embed/gene_vectors.npy` [12225]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12225 or target_col == 12225). Every well: [[TCEAL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCEAL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
