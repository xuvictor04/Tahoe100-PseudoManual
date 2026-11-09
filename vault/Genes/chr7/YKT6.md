---
symbol: "YKT6"
type: "gene"
col: 2789
ensembl_id: "ENSG00000106636"
name: "YKT6 vesicular SNARE protein"
location: "7p13"
module: 52
arm: "+"
pooled_cpm: 45.61
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# YKT6

*YKT6 vesicular SNARE protein* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.46× (z +15.0, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 0.422×, A-427 0.420×; ⚠ cell-cycle shift, explains ~40% of this change); [[Levobupivacaine (hydrochloride) (drug)]] 5 µM in 1 line (SW 1088 0.0917×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPP9]] (+0.74, fdr 7e-06), [[SEC13]] (+0.73, fdr 7e-06), [[GOLGA3]] (+0.72, fdr 7e-06); moves opposite to [[TGIF2]] (-0.58, fdr 1e-05), [[BAZ2B]] (-0.58, fdr 5e-05), [[UNK]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[DAP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2789.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.46×** | +15.0 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.45×** | +14.9 | 0e+00 | 45/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.37×** | +14.4 | 2e-44 | 45/48 (SW480, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.08×** | +12.2 | 4e-32 | 46/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.84×** | +10.1 | 5e-22 | 45/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.70×** | +8.8 | 1e-16 | 41/48 (PANC-1, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.73×** | +8.6 | 1e-15 | 40/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +8.3 | 8e-15 | 33/47 (SK-MEL-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.61×** | +7.9 | 1e-13 | 32/44 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.42×** | +7.7 | 1e-12 | 43/49 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.57×** | +7.2 | 2e-11 | 28/38 (SW480, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +6.3 | 2e-08 | 33/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.48×** | +6.3 | 2e-08 | 30/47 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.48×** | +6.0 | 8e-08 | 26/41 (SNU-423, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +5.6 | 8e-07 | 29/47 (NCI-H2030, SHP-77, …) | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +5.4 | 2e-06 | 25/48 (MIA PaCa-2, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 5e-06 | 29/48 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.9 | 3e-05 | 22/48 (SNU-423, A-427, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.001 | 20/47 (NCI-H23, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.002 | 18/48 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.005 | 15/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2789.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 0.422×, A-427 0.420×; ⚠ cell-cycle shift, explains ~40% of this change); [[Levobupivacaine (hydrochloride) (drug)]] 5 µM in 1 line (SW 1088 0.0917×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.813× | -3.5 | 0.27 | 15/48 (KATO III, HEC-1-A, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.822× | -3.2 | 0.27 | 16/47 (AsPC-1, SW 900, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.880× | -3.1 | 0.27 | 7/48 (SNU-1, BT-474, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.843× | -3.1 | 0.27 | 8/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2789. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 60.4 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.52× (z +10.0) | — |
| [[SW480 (line)]] | alt | 40.2 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.70× (z +15.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 33.9 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.71× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 36.3 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.37× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 23.2 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.93× (z +10.5) | — |
| [[A-427 (line)]] | wt | 33.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.79× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -10.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HEC-1-A (line)]] | alt | 34.4 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.15× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 35.5 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.40× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 50.5 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.37× (z +10.7) | — |
| [[A-172 (line)]] | wt | 64.9 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.70× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 37.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.85× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 24.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.74× (z +11.6) | — |
| [[LS 180 (line)]] | wt | 28.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.17× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 29.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.28× (z +10.1) | — |
| [[C32 (line)]] | wt | 26.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.04× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 47.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.73× (z +9.2) | — |
| [[J82 (line)]] | alt | 58.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -12.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[KATO III (line)]] | alt | 50.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +8.6) | — |
| [[LoVo (line)]] | wt | 40.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.3) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2347 (line)]] | alt | 43.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.27× (z +8.7) | — |
| [[RKO (line)]] | wt | 37.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.05× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 55.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.11× (z +9.6) | — |
| [[SW 1088 (line)]] | alt | 79.1 | 0 | 1 | — | [[Levobupivacaine (hydrochloride) (drug)]] 5 µM 0.0917× (z -8.5) |
| [[SW 900 (line)]] | alt | 41.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.48× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 60.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.36× (z +8.6) | — |
| [[A498 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 82.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2789), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPP9]] | +0.74 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[SEC13]] | +0.73 | +0.71 / +0.60 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 730 |
| [[GOLGA3]] | +0.72 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[RER1]] | +0.72 | +0.64 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[TPD52L2]] | +0.71 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[DPH7]] | +0.71 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[CHFR]] | +0.70 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[SEC61A1]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[SEC22B]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 | same gene group; pathway: HALLMARK_PROTEIN_SECRETION; STRING 995 |
| [[PCYT1A]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[LINC02693]] | +0.69 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[MED8]] | +0.67 | +0.77 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGIF2]] | -0.58 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.58 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[UNK]] | -0.58 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ARID2]] | -0.57 | -0.36 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAP]] | C | YKT6's natural level strengthens DAP's drug response | YKT6's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.10; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | YKT6's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | YKT6's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.478 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.759). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.3, -28.2); signed map (-50.4, 3.5). **Vector** length 98.3, 27.8% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.6 | +14.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +15.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +14.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +8.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.4 | +12.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.3 | +5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +8.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.7 | +4.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | +0.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | -5.2 | +2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -0.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.5 | +5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.2 | -3.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | YKT6 vesicular SNARE protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:44,200,959-44,214,294 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SNAREs |
| Hallmark sets | PROTEIN_SECRETION, UV_RESPONSE_UP, MTORC1_SIGNALING |
| Reactome | 17 pathways, smallest: Intra-Golgi traffic; COPII-mediated vesicle transport; RHOG GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O15498](https://www.uniprot.org/uniprotkb/O15498) (Synaptobrevin homolog YKT6):

> Vesicular soluble NSF attachment protein receptor (v-SNARE) mediating vesicle docking and fusion to a specific acceptor cellular compartment. Functions in endoplasmic reticulum to Golgi transport; as part of a SNARE complex composed of GOSR1, GOSR2 and STX5 (By similarity). Functions in early/recycling endosome to TGN transport; as part of a SNARE complex composed of BET1L, GOSR1 and STX5. Has a S-palmitoyl transferase activity. Essential for the structural and functional organization of the …

**Summary**, from NCBI Gene [10652](https://www.ncbi.nlm.nih.gov/gene/10652):

> This gene product is one of the SNARE recognition molecules implicated in vesicular transport between secretory compartments. It is a membrane associated, isoprenylated protein that functions at the endoplasmic reticulum-Golgi transport step. This protein is highly conserved from yeast to human and can functionally complement the loss of the yeast homolog in the yeast secretory pathway. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16959](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16959) · Entrez [10652](https://www.ncbi.nlm.nih.gov/gene/10652) · UniProt [O15498](https://www.uniprot.org/uniprotkb/O15498) · Ensembl [ENSG00000106636](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106636)

## Data

Gene col 2789: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2789); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2789, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2789]; `tensor/DDL_lfc|DDL_z.npy` [2789]; `embed/gene_vectors.npy` [2789]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2789 or target_col == 2789). Every well: [[YKT6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YKT6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
