---
symbol: "DDX19B"
type: "gene"
col: 8061
ensembl_id: "ENSG00000157349"
name: "DEAD-box helicase 19B"
location: "16q22.1"
module: 17
arm: "+"
pooled_cpm: 33.8
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 5
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# DDX19B

*DEAD-box helicase 19B* — 16q22.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 2.98×, NCI-H23 2.56×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.463× (z -21.7, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF45]] (+0.74, fdr 1e-05), [[MRPS31P4]] (+0.72, fdr 1e-05), [[THOC1]] (+0.66, fdr 1e-05); moves opposite to [[ATP11C]] (-0.66, fdr 1e-05), [[ARSB]] (-0.62, fdr 1e-05), [[EIF4G2]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8061.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 2.98×, NCI-H23 2.56×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.14× | +3.6 | 0.17 | 13/47 (HS-578T, HOP62, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.38 | 13/47 (HEC-1-A, C-33 A, …) | inconsistent across doses |  |
| [[Resveratrol (drug)]] 5 µM |  | 1.11× | +3.1 | 0.38 | 6/47 (J82, A549, …) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.23× | +3.0 | 0.38 | 6/47 (Hs 766T, NCI-H460, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8061.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.463×** | -21.7 | 0e+00 | 46/47 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.575×** | -10.6 | 7e-24 | 38/46 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.582×** | -10.4 | 6e-23 | 39/47 (NCI-H23, LS 180, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.842× | -4.8 | 2e-04 | 24/47 (HOP62, SNU-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.806×** | -4.3 | 0.002 | 18/47 (SNU-423, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.807×** | -4.3 | 0.002 | 22/44 (SNU-1, SW1417, …) | inconsistent across doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.836× | -3.6 | 0.030 | 18/47 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.846× | -3.3 | 0.065 | 13/47 (LS 180, COLO 205, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | 0.844× | -3.2 | 0.074 | 17/46 (LS 180, NCI-H23, …) | top dose only |  |
| [[Gefitinib (drug)]] 5 µM |  | 0.855× | -3.1 | 0.10 | 4/47 (PANC-1, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8061. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 41.5 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 38.2 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -14.9) |
| [[LoVo (line)]] | wt | 37.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -12.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 27.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.2) |
| [[HCT15 (line)]] | alt | 38.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -8.7) |
| [[HOP62 (line)]] | alt | 23.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -9.4) |
| [[Hs 766T (line)]] | wt | 41.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -12.1) |
| [[HS-578T (line)]] | alt | 21.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -10.6) |
| [[LS 180 (line)]] | wt | 28.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 65.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -17.4) |
| [[NCI-H1573 (line)]] | alt | 35.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -10.9) |
| [[RKO (line)]] | wt | 32.7 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -14.1) |
| [[SNU-423 (line)]] | alt | 31.7 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -9.3) |
| [[A498 (line)]] | wt | 39.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -14.0) |
| [[AN3 CA (line)]] | alt | 48.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 28.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -21.6) |
| [[CHP-212 (line)]] | wt | 51.1 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.128× (z -9.6) |
| [[H4 (line)]] | wt | 18.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 34.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -8.6) |
| [[HT-29 (line)]] | alt | 36.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -12.2) |
| [[hTERT-HPNE (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 31.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.1) |
| [[KATO III (line)]] | alt | 35.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -9.9) |
| [[NCI-H2122 (line)]] | alt | 30.0 | 0 | 1 | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.205× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 22.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -12.7) |
| [[PANC-1 (line)]] | alt | 26.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 30.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.149× (z -8.6) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 34.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -11.2) |
| [[SW1417 (line)]] | alt | 35.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -12.5) |
| [[SW480 (line)]] | alt | 63.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -9.3) |
| [[A-172 (line)]] | wt | 7.83 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8061), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF45]] | +0.74 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[MRPS31P4]] | +0.72 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[THOC1]] | +0.66 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[GGT7]] | +0.66 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[CNKSR1]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[DPY30]] | +0.64 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[POLR2I]] | +0.64 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[ZNF461]] | +0.64 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[CRTC1]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[BBS5]] | +0.61 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[MRPS31P5-1]] | +0.61 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[TTC38]] | +0.61 | +0.44 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP11C]] | -0.66 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[ARSB]] | -0.62 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.61 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[HCFC1]] | -0.60 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[CRPPA]] | -0.60 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[PRDM10]] | -0.59 | -0.26 / -0.54 | both halves | 4e-04 |  |
| [[DDX5]] | -0.58 | -0.48 / -0.55 | both halves | 2e-05 | same gene group |
| [[SIAH2-AS1]] | -0.58 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[CCDC200]] | -0.58 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[RNF217-AS1]] | -0.57 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[CFL1]] | -0.57 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[CDK2AP1]] | -0.57 | -0.35 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DDX19B's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[EXO5-DT]] | B | EXO5-DT activity raises DDX19B's level | lines that do not express EXO5-DT (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without EXO5-DT | 0.092 | ⚠ within organs, on part of the lines; also absent: EXO5, LARP6, ENSG00000290399 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.668). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-27.8, -2.7); signed map (-22.2, -14.8). **Vector** length 88.9, 18.1% of its response variance represented; |z| ≥ 3 in 704 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.9 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +1.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.3 | +3.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -0.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.7 | +2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.5 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -21.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -10.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | -2.8 | -3.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 19B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:70,289,663-70,335,305 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DBP5; previously DDX19 |
| Gene groups (HGNC) | DEAD-box helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMR2](https://www.uniprot.org/uniprotkb/Q9UMR2) (ATP-dependent RNA helicase DDX19B):

> ATP-dependent RNA helicase involved in mRNA export from the nucleus. Rather than unwinding RNA duplexes, DDX19B functions as a remodeler of ribonucleoprotein particles, whereby proteins bound to nuclear mRNA are dissociated and replaced by cytoplasmic mRNA binding proteins.

**Summary**, from NCBI Gene [11269](https://www.ncbi.nlm.nih.gov/gene/11269):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. This gene encodes a …

**Accessions** — [HGNC:2742](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2742) · Entrez [11269](https://www.ncbi.nlm.nih.gov/gene/11269) · UniProt [Q9UMR2](https://www.uniprot.org/uniprotkb/Q9UMR2) · Ensembl [ENSG00000157349](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157349)

## Data

Gene col 8061: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8061); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8061, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8061]; `tensor/DDL_lfc|DDL_z.npy` [8061]; `embed/gene_vectors.npy` [8061]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8061 or target_col == 8061). Every well: [[DDX19B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX19B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
