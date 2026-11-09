---
symbol: "IPO9"
type: "gene"
col: 12646
ensembl_id: "ENSG00000198700"
name: "importin 9"
location: "1q32.1"
module: 6
arm: "+"
pooled_cpm: 104.97
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# IPO9

*importin 9* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.48× (z +7.1, q 9e-10, up in 35 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.22× (z +3.6, q 0.023, up in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 2.59×, NCI-H23 2.16×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1573 2.75×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 2.27×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.705× (z -9.3, q 8e-18, down in 36 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INTS7]] (+0.76, fdr 7e-06), [[XRCC2]] (+0.72, fdr 7e-06), [[SAE1]] (+0.70, fdr 7e-06); moves opposite to [[DNAJC4]] (-0.67, fdr 7e-06), [[CDK7]] (-0.65, fdr 7e-06), [[KDM5B]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[POLR1D]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12646.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 2.59×, NCI-H23 2.16×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1573 2.75×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 2.27×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.48×** | +7.1 | 9e-10 | 35/44 (NCI-H1573, NCI-H23, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +6.0 | 5e-07 | 39/48 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.29×** | +4.7 | 3e-04 | 28/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.28×** | +4.7 | 3e-04 | 32/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.25×** | +4.2 | 0.002 | 26/49 (C32, A498, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.21×** | +3.7 | 0.023 | 23/48 (LoVo, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.023 | 23/48 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | 1.20× | +3.4 | 0.051 | 22/48 (LoVo, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12646.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.705×** | -9.3 | 8e-18 | 36/49 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.702×** | -6.7 | 8e-09 | 33/48 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.616×** | -4.8 | 4e-04 | 32/49 (SK-MEL-2, HCT15, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.699×** | -3.5 | 0.061 | 19/48 (RPMI-7951, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.827×** | -3.4 | 0.066 | 23/47 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.848× | -3.1 | 0.17 | 15/48 (HCT15, RKO, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | 0.849× | -3.1 | 0.17 | 22/48 (AsPC-1, A498, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12646. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 75.1 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.75× (z +11.8) | — |
| [[NCI-H23 (line)]] | alt | 121 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.16× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Auranofin (drug)]] 5 µM 0.538× (z -8.6) |
| [[A-172 (line)]] | wt | 213 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 54.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -10.2) |
| [[C-33 A (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[H4 (line)]] | wt | 113 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 71.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.27× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 138 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -9.5) |
| [[RKO (line)]] | wt | 118 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -13.1) |
| [[RPMI-7951 (line)]] | alt | 118 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 98.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.251× (z -8.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 93.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 103 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 201 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 144 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 76.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 129 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 81.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 99.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 89.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 99.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12646), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS7]] | +0.76 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[XRCC2]] | +0.72 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[SAE1]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[NUP188]] | +0.70 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[ANAPC7]] | +0.69 | +0.60 / +0.75 | both halves | 7e-06 | STRING 443 |
| [[SMC1A]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 | same gene group |
| [[NUP155]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[DNMT1]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[FARSB]] | +0.68 | +0.51 / +0.78 | both halves | 1e-05 |  |
| [[EFTUD2]] | +0.67 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[MTHFD1]] | +0.67 | +0.52 / +0.73 | both halves | 1e-05 |  |
| [[TFDP1]] | +0.66 | +0.52 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC4]] | -0.67 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[CDK7]] | -0.65 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[KDM5B]] | -0.64 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[CLK1]] | -0.63 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[ZMAT5]] | -0.63 | -0.40 / -0.66 | both halves | 5e-05 |  |
| [[RSBN1]] | -0.62 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[RIOK3]] | -0.62 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[DNAJC3-DT]] | -0.62 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[IFT20]] | -0.61 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[STX5-DT]] | -0.61 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[SYF2]] | -0.61 | -0.44 / -0.67 | both halves | 3e-05 |  |
| [[VPS37D]] | -0.60 | -0.50 / -0.68 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POLR1D]] | C | IPO9's natural level strengthens POLR1D's drug response | IPO9's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.12; direction not clear | 0.049 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-37.1, -41.4); signed map (-34.8, -48.4). **Vector** length 126, 37.3% of its response variance represented; |z| ≥ 3 in 748 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.53 to 28); *DNA Replication* (reactome, mean cos +0.51 to 40); *Synthesis of DNA* (reactome, mean cos +0.50 to 37).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.6 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +5.4 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +5.4 | +4.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.0 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +4.9 | +4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.7 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +2.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +0.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.0 | -9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -6.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -2.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -1.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.7 | -2.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.5 | -0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | importin 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:201,829,149-201,884,291 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Imp9, FLJ10402 |
| Gene groups (HGNC) | Importins; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96P70](https://www.uniprot.org/uniprotkb/Q96P70) (Importin-9):

> Nuclear transport receptor that mediates nuclear import of proteins, such as histones, proteasome and actin. Serves as receptor for nuclear localization signals (NLS) in cargo substrates. Is thought to mediate docking of the importin/substrate complex to the nuclear pore complex (NPC) through binding to nucleoporin and the complex is subsequently translocated through the pore by an energy requiring, Ran-dependent mechanism. At the nucleoplasmic side of the NPC, Ran binds to the importin, the …

**Summary**, from NCBI Gene [55705](https://www.ncbi.nlm.nih.gov/gene/55705):

> Enables histone binding activity; histone chaperone activity; and nuclear import signal receptor activity. Involved in proteasome localization and protein import into nucleus. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19425](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19425) · Entrez [55705](https://www.ncbi.nlm.nih.gov/gene/55705) · UniProt [Q96P70](https://www.uniprot.org/uniprotkb/Q96P70) · Ensembl [ENSG00000198700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198700)

## Data

Gene col 12646: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12646); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12646, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12646]; `tensor/DDL_lfc|DDL_z.npy` [12646]; `embed/gene_vectors.npy` [12646]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12646 or target_col == 12646). Every well: [[IPO9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IPO9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
