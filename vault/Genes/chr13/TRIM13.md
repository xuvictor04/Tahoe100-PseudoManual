---
symbol: "TRIM13"
type: "gene"
col: 12942
ensembl_id: "ENSG00000204977"
name: "tripartite motif containing 13"
location: "13q14.2"
module: 114
arm: "+"
pooled_cpm: 24.03
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# TRIM13

*tripartite motif containing 13* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.62× (z +8.6, q 6e-15, up in 33 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.30× (z +4.8, q 2e-04, up in 22 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW480 2.08×; ⚠ toxic).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.499× (z -12.9, q 4e-35, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTFMT]] (+0.65, fdr 7e-06), [[TEFM]] (+0.63, fdr 7e-06), [[SETDB1]] (+0.63, fdr 1e-05); moves opposite to [[COL20A1]] (-0.52, fdr 2e-05), [[FOSB]] (-0.51, fdr 3e-05), [[LRRC59]] (-0.51, fdr 2e-05).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12942.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW480 2.08×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +8.6 | 6e-15 | 33/45 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.21×** | +5.0 | 2e-04 | 21/47 (HOP62, A498, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 2e-04 | 22/46 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +3.8 | 0.021 | 17/46 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12942.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.499×** | -12.9 | 4e-35 | 43/47 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.592×** | -9.7 | 7e-20 | 39/47 (HepG2/C3A, RKO, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.605×** | -9.3 | 3e-18 | 40/47 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.687×** | -6.9 | 6e-10 | 28/46 (HCT15, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.718×** | -6.1 | 9e-08 | 25/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.829×** | -4.9 | 9e-05 | 23/47 (SK-MEL-2, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **0.787×** | -4.4 | 7e-04 | 21/43 (COLO 205, KATO III, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.790×** | -4.2 | 0.002 | 20/47 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.855× | -4.1 | 0.003 | 18/47 (SW1417, A-172, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.829×** | -3.3 | 0.049 | 9/47 (SK-MEL-2, RKO, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | 0.839× | -3.1 | 0.089 | 15/46 (AN3 CA, SW48, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | 0.834× | -3.1 | 0.089 | 18/41 (NCI-H23, NCI-H2347, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12942. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 42.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.08× (z +9.3) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.342× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.471× (z -9.9) |
| [[A-172 (line)]] | wt | 24.7 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.331× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 27.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.217× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 30.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[AN3 CA (line)]] | alt | 43.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.106× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~41% of this change |
| [[C-33 A (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[CHP-212 (line)]] | wt | 34.1 | 0 | 1 | — | [[Osimertinib (mesylate) (drug)]] 5 µM 0.0886× (z -10.1) |
| [[COLO 205 (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[HOP62 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.334× (z -8.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[LOX-IMVI (line)]] | wt | 26.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -9.8) ⚠ cell-cycle shift, explains ~67% of this change |
| [[NCI-H2347 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[RKO (line)]] | wt | 36.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.337× (z -8.9) |
| [[SNU-423 (line)]] | alt | 15.7 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.210× (z -9.4) |
| [[SW48 (line)]] | wt | 34.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[A-427 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.88 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12942), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTFMT]] | +0.65 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[TEFM]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[SETDB1]] | +0.63 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[RWDD3]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[THUMPD2]] | +0.62 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[SNRNP35]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[TATDN3]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ZCCHC10]] | +0.60 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[STARD7-AS1]] | +0.60 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ZC3HC1]] | +0.60 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[POLR3C]] | +0.59 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[MTHFS]] | +0.58 | +0.37 / +0.60 | both halves | 9e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL20A1]] | -0.52 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[FOSB]] | -0.51 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[LRRC59]] | -0.51 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[SPTBN5]] | -0.50 | -0.51 / -0.51 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[SPAG9]] | -0.50 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[GOLGA3]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[ZDHHC11]] | -0.48 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[HDLBP]] | -0.48 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[IQGAP1]] | -0.48 | -0.34 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TRIM13's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.616). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.2, 7.8); signed map (-8.9, -14.8). **Vector** length 80.1, 15.0% of its response variance represented; |z| ≥ 3 in 744 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.9 | +8.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.8 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.9 | +4.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.1 | +1.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +1.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | -4.0 | -4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.0 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | -3.1 | -3.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.0 | -12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -6.9 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Uridine (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:49,995,888-50,020,481 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Leu5, RNF77, DLEU5; previously RFP2 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 4 pathways, smallest: ER Quality Control Compartment (ERQC); Calnexin/calreticulin cycle; N-glycan trimming in the ER and Calnexin/Calreticulin cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O60858](https://www.uniprot.org/uniprotkb/O60858) (E3 ubiquitin-protein ligase TRIM13):

> Endoplasmic reticulum (ER) membrane anchored E3 ligase involved in the retrotranslocation and turnover of membrane and secretory proteins from the ER through a set of processes named ER-associated degradation (ERAD). This process acts on misfolded proteins as well as in the regulated degradation of correctly folded proteins. Enhances ionizing radiation-induced p53/TP53 stability and apoptosis via ubiquitinating MDM2 and AKT1 and decreasing AKT1 kinase activity through MDM2 and AKT1 proteasomal …

**Summary**, from NCBI Gene [10206](https://www.ncbi.nlm.nih.gov/gene/10206):

> This gene encodes a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. This gene is located on chromosome 13 within the minimal deletion region for B-cell chronic lymphocytic leukemia. Multiple alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9976](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9976) · Entrez [10206](https://www.ncbi.nlm.nih.gov/gene/10206) · UniProt [O60858](https://www.uniprot.org/uniprotkb/O60858) · Ensembl [ENSG00000204977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204977)

## Data

Gene col 12942: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12942); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12942, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12942]; `tensor/DDL_lfc|DDL_z.npy` [12942]; `embed/gene_vectors.npy` [12942]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12942 or target_col == 12942). Every well: [[TRIM13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
