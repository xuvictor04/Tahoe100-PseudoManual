---
symbol: "ZBTB6"
type: "gene"
col: 11780
ensembl_id: "ENSG00000186130"
name: "zinc finger and BTB domain containing 6"
location: "9q33.2"
module: 7
arm: "+"
pooled_cpm: 12.41
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ZBTB6

*zinc finger and BTB domain containing 6* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.01× (z +17.0, q 0e+00, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.677× (z -6.7, q 2e-08, down in 20 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 0.808× (z -3.5, q 0.071, down in 5 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (PANC-1 0.103×, NCI-H460 0.196×, HEC-1-A 0.200×, J82 0.233×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HEC-1-A 0.172×, Hs 766T 0.168×, J82 0.241×, A-172 0.285×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-172 0.178×, LoVo 0.199×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Aprepitant (drug)]] 0.5 µM in 1 line (AsPC-1 0.0491×); [[Silodosin (drug)]] 5 µM in 1 line (SW 900 0.0681×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (C32 0.121×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBLL1]] (+0.89, fdr 7e-06), [[SMG8]] (+0.83, fdr 7e-06), [[THUMPD3]] (+0.82, fdr 7e-06); moves opposite to [[CBFA2T2]] (-0.63, fdr 1e-05), [[CD81]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZFP30]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11780.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +17.0 | 0e+00 | 40/46 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.80×** | +15.8 | 0e+00 | 41/48 (SW480, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.38×** | +14.4 | 6e-45 | 37/44 (RKO, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.26×** | +14.0 | 2e-42 | 42/46 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.24×** | +13.3 | 2e-38 | 41/46 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.01×** | +12.0 | 3e-31 | 39/46 (SW480, HEC-1-A, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.67×** | +11.7 | 2e-29 | 33/44 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +9.2 | 2e-18 | 25/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.64×** | +8.5 | 1e-15 | 32/46 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +7.3 | 1e-11 | 26/48 (SK-MEL-2, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +7.3 | 2e-11 | 25/41 (NCI-H1573, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.54×** | +6.8 | 4e-10 | 24/45 (NCI-H460, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +4.8 | 6e-05 | 12/44 (HOP62, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +4.3 | 8e-04 | 12/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.1 | 0.001 | 13/47 (HOP62, BT-474, …) | top dose only |  |
| [[Malotilate (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.066 | 4/46 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11780.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (PANC-1 0.103×, NCI-H460 0.196×, HEC-1-A 0.200×, J82 0.233×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HEC-1-A 0.172×, Hs 766T 0.168×, J82 0.241×, A-172 0.285×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-172 0.178×, LoVo 0.199×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Aprepitant (drug)]] 0.5 µM in 1 line (AsPC-1 0.0491×); [[Silodosin (drug)]] 5 µM in 1 line (SW 900 0.0681×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (C32 0.121×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.677×** | -6.7 | 2e-08 | 20/37 (HEC-1-A, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.773×** | -4.2 | 0.007 | 18/42 (A-427, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.777×** | -4.1 | 0.007 | 13/22 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.808×** | -3.5 | 0.071 | 5/46 (C-33 A, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11780. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 18.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 16.7 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.90× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 17.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -13.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 17.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -9.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 11.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.1× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 8.10 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.169× (z -8.8) ⚠ toxic |
| [[A549 (line)]] | wt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 5.63 | 0 | 1 | — | [[Aprepitant (drug)]] 0.5 µM 0.0491× (z -11.8) |
| [[C32 (line)]] | wt | 9.45 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.121× (z -9.3) |
| [[H4 (line)]] | wt | 12.9 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0984× (z -8.7) |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.158× (z -9.0) |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -10.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 9.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 9.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -13.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 8.62 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -15.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 7.91 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0681× (z -10.6) |
| [[SW1417 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11780), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBLL1]] | +0.89 | +0.85 / +0.86 | both halves | 7e-06 |  |
| [[SMG8]] | +0.83 | +0.82 / +0.76 | both halves | 7e-06 |  |
| [[THUMPD3]] | +0.82 | +0.84 / +0.76 | both halves | 7e-06 |  |
| [[ZNF543]] | +0.81 | +0.85 / +0.64 | both halves | 7e-06 | same gene group |
| [[ZNF268]] | +0.81 | +0.88 / +0.69 | both halves | 7e-06 | same gene group |
| [[GTF3C4]] | +0.79 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[ZNF614]] | +0.78 | +0.77 / +0.69 | both halves | 7e-06 | same gene group |
| [[NAIF1]] | +0.77 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.77 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.77 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[ZNF845]] | +0.76 | +0.79 / +0.69 | both halves | 7e-06 | same gene group |
| [[CSTF2T]] | +0.75 | +0.76 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T2]] | -0.63 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[CD81]] | -0.63 | -0.58 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFP30]] | B | ZFP30 activity raises ZBTB6's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 1.37× lower at baseline in the lines without ZFP30 | 0.038 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |
| [[ZNF613]] | B | ZNF613 activity raises ZBTB6's level | lines that do not express ZNF613 (7) vs lines expressing it (43) | 1.28× lower at baseline in the lines without ZNF613 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF850, ENSG00000283201, ZNF571 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.829). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-35.5, 11.2); signed map (-0.3, -27.0). **Vector** length 89.7, 17.7% of its response variance represented; |z| ≥ 3 in 1,050 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.2 | +15.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.6 | +14.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.0 | +14.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.1 | +11.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +13.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +8.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +4.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.2 | -6.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.0 | -4.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.5 | -2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +0.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:122,908,056-122,913,323 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZID; previously ZNF482 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15916](https://www.uniprot.org/uniprotkb/Q15916) (Zinc finger and BTB domain-containing protein 6):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [10773](https://www.ncbi.nlm.nih.gov/gene/10773):

> Predicted to enable DNA-binding transcription repressor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in negative regulation of transcription by RNA polymerase II; regulation of cytokine production; and regulation of immune system process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16764](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16764) · Entrez [10773](https://www.ncbi.nlm.nih.gov/gene/10773) · UniProt [Q15916](https://www.uniprot.org/uniprotkb/Q15916) · Ensembl [ENSG00000186130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186130)

## Data

Gene col 11780: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11780); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11780, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11780]; `tensor/DDL_lfc|DDL_z.npy` [11780]; `embed/gene_vectors.npy` [11780]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11780 or target_col == 11780). Every well: [[ZBTB6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
