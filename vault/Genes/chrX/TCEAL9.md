---
symbol: "TCEAL9"
type: "gene"
col: 11642
ensembl_id: "ENSG00000185222"
name: "transcription elongation factor A like 9"
location: "Xq22.2"
module: 12
arm: "+"
pooled_cpm: 76.65
n_lines_expressing: 46
n_dd_up: 3
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# TCEAL9

*transcription elongation factor A like 9* — Xq22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.36× (z +8.6, q 4e-15, up in 42 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 8 lines (A-172 3.68×, SNU-423 3.65×, C32 5.48×, HEC-1-A 3.23×, …); [[Homoharringtonine (drug)]] 5 µM in 6 lines (SNU-423 2.99×, Hs 766T 3.47×, NCI-H460 3.06×, NCI-H2030 2.42×, …; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 3.57×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.565× (z -5.7, q 7e-06, down in 36 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCEAL8]] (+0.76, fdr 7e-06), [[TCEAL3]] (+0.72, fdr 7e-06), [[ARMCX3]] (+0.69, fdr 7e-06); moves opposite to [[SLC25A39]] (-0.65, fdr 7e-06), [[PRKDC]] (-0.61, fdr 7e-06), [[NUP93]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Tomivosertib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11642.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 8 lines (A-172 3.68×, SNU-423 3.65×, C32 5.48×, HEC-1-A 3.23×, …); [[Homoharringtonine (drug)]] 5 µM in 6 lines (SNU-423 2.99×, Hs 766T 3.47×, NCI-H460 3.06×, NCI-H2030 2.42×, …; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 3.57×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.36×** | +8.6 | 4e-15 | 42/44 (A-172, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.58×** | +4.6 | 0.001 | 32/44 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.6 | 0.068 | 29/43 (SW480, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.26× | +3.3 | 0.13 | 22/44 (SNU-423, Hs 766T, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | 1.38× | +3.3 | 0.13 | 24/43 (HS-578T, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.37× | +3.2 | 0.14 | 27/44 (HEC-1-A, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11642.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.565×** | -5.7 | 7e-06 | 36/44 (hTERT-HPNE, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.587×** | -5.3 | 3e-05 | 31/44 (hTERT-HPNE, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.594×** | -5.2 | 4e-05 | 32/44 (hTERT-HPNE, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.796× | -3.2 | 0.19 | 23/45 (hTERT-HPNE, AsPC-1, …) | top dose only | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.805× | -3.1 | 0.26 | 18/44 (LoVo, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11642. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 208 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.272× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 104 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +12.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-423 (line)]] | alt | 202 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.65× (z +11.2) | — |
| [[A-172 (line)]] | wt | 72.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.68× (z +11.7) | — |
| [[AsPC-1 (line)]] | alt | 81.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -9.1) ⚠ cell-cycle shift, explains ~16% of this change |
| [[C32 (line)]] | wt | 51.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.48× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 62.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 60.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.23× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 117 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Hs 766T (line)]] | wt | 102 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +13.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 34.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.96× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 56.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.34× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 66.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 126 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 104 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.28× (z +9.2) | — |
| [[SW 1088 (line)]] | alt | 141 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.0607× (z -10.8) |
| [[SW480 (line)]] | alt | 65.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.96× (z +9.1) | — |
| [[A-427 (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 169 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 137 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.43 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.90 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.99 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.23 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 46.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 73.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11642), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEAL8]] | +0.76 | +0.67 / +0.80 | both halves | 7e-06 | same gene group; STRING 533 |
| [[TCEAL3]] | +0.72 | +0.68 / +0.75 | both halves | 7e-06 | same gene group; STRING 461 |
| [[ARMCX3]] | +0.69 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[KRT10]] ⚠ | +0.69 | +0.61 / +0.70 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS18C]] | +0.67 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[SMIM26]] ⚠ | +0.64 | +0.52 / +0.68 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TRAPPC2B]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[NKAP]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[TMF1]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[DCP1A]] | +0.62 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[SEC62]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[IFI27L2]] | +0.62 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[ZNF503]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[MFAP1]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A39]] | -0.65 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[PRKDC]] | -0.61 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[NUP93]] | -0.61 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[RPSA]] | -0.60 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[CHID1]] | -0.60 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[IPO5]] | -0.60 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[JPT2]] | -0.58 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[SIGMAR1]] | -0.58 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.58 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[PSME3]] | -0.57 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[RNPS1]] | -0.57 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[MTHFD1]] | -0.57 | -0.53 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TCEAL9's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TCEAL3]] | B | TCEAL3 activity raises TCEAL9's level | lines that do not express TCEAL3 (7) vs lines expressing it (43) | 1.75× lower at baseline in the lines without TCEAL3 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, TTLL7, ENSG00000234405 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tomivosertib (drug)]] 5 µM | C | TCEAL9 activity raises the cells' numbers under Tomivosertib 5 µM (protects the cells) | lines that do not express TCEAL9 (4) vs lines expressing it (44) | the lines without TCEAL9: 0.80× the cells of the other lines | 0.040 | ⚠ few lines (4 vs 46); tissue-confounded; across organs |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.536). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-35.0, -31.2); signed map (-10.8, -0.8). **Vector** length 97.6, 33.7% of its response variance represented; |z| ≥ 3 in 564 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.2 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.8 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +0.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.1 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +0.0 |
|  | [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | +2.2 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.9 | -0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.9 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.8 | +2.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -3.4 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -0.6 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | transcription elongation factor A like 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.2 — chrX:103,356,489-103,358,462 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp313K1940, WEX6; previously WBP5 |
| Gene groups (HGNC) | Transcription elongation factor A like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHQ7](https://www.uniprot.org/uniprotkb/Q9UHQ7) (Transcription elongation factor A protein-like 9):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [51186](https://www.ncbi.nlm.nih.gov/gene/51186):

> The globular WW domain is composed of 38 to 40 semiconserved amino acids shared by proteins of diverse functions including structural, regulatory, and signaling proteins. The domain is involved in mediating protein-protein interactions through the binding of polyproline ligands. This gene encodes a WW domain binding protein. This gene also encodes a domain with similarity to the transcription elongation factor A, SII-related family. Alternative splicing results in multiple transcript variants …

**Accessions** — [HGNC:30084](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30084) · Entrez [51186](https://www.ncbi.nlm.nih.gov/gene/51186) · UniProt [Q9UHQ7](https://www.uniprot.org/uniprotkb/Q9UHQ7) · Ensembl [ENSG00000185222](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185222)

## Data

Gene col 11642: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11642); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11642, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11642]; `tensor/DDL_lfc|DDL_z.npy` [11642]; `embed/gene_vectors.npy` [11642]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11642 or target_col == 11642). Every well: [[TCEAL9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCEAL9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
