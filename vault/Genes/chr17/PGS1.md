---
symbol: "PGS1"
type: "gene"
col: 1488
ensembl_id: "ENSG00000087157"
name: "phosphatidylglycerophosphate synthase 1"
location: "17q25.3"
module: 15
arm: "+"
pooled_cpm: 30.03
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PGS1

*phosphatidylglycerophosphate synthase 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.96× (z +13.0, q 8e-36, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.537× (z -8.5, q 1e-14, down in 30 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Aliskiren (drug)]] 0.5 µM: 0.773× (z -3.5, q 0.050, down in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SW1417 0.0803×, SHP-77 0.144×, NCI-H460 0.234×, A498 0.271×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 0.154×, SW480 0.264×, SW 900 0.237×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 0.367×, NCI-H23 0.442×; ⚠ cell-cycle shift, explains ~93% of this change); [[Tetracycline (hydrochloride) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0537×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STARD3]] (+0.69, fdr 7e-06), [[GLUD1P3]] (+0.69, fdr 7e-06), [[RNF4]] (+0.67, fdr 7e-06); moves opposite to [[LGALS3]] (-0.59, fdr 1e-05), [[SFR1]] (-0.58, fdr 1e-05), [[MAPRE2]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1488.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +13.0 | 8e-36 | 43/48 (CFPAC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.91×** | +7.6 | 8e-12 | 40/48 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.31×** | +6.0 | 4e-07 | 35/46 (A-427, HOP62, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.8 | 6e-07 | 30/47 (SNU-423, C32, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +5.8 | 6e-07 | 32/47 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +5.2 | 2e-05 | 29/48 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +5.2 | 2e-05 | 30/48 (HEC-1-A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.44×** | +5.0 | 5e-05 | 28/47 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.003 | 23/48 (SK-MEL-2, NCI-H2347, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.54× | +3.1 | 0.12 | 12/32 (A549, HS-578T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1488.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SW1417 0.0803×, SHP-77 0.144×, NCI-H460 0.234×, A498 0.271×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 0.154×, SW480 0.264×, SW 900 0.237×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 0.367×, NCI-H23 0.442×; ⚠ cell-cycle shift, explains ~93% of this change); [[Tetracycline (hydrochloride) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0537×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.537×** | -8.5 | 1e-14 | 30/44 (SW1417, SHP-77, …) | two highest doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.606×** | -6.6 | 2e-08 | 26/36 (A-172, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.763×** | -5.2 | 3e-05 | 27/47 (J82, NCI-H23, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.704×** | -4.6 | 6e-04 | 21/48 (PANC-1, A498, …) | rises with dose | composition shift; position effect removed |
| [[Aliskiren (drug)]] 0.5 µM |  | **0.773×** | -3.5 | 0.050 | 17/48 (HEC-1-A, Hs 766T, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 0.5 µM |  | 0.802× | -3.0 | 0.24 | 15/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1488. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 32.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -12.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 31.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -11.6) ⚠ cell-cycle shift, explains ~93% of this change |
| [[NCI-H460 (line)]] | wt | 36.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -13.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 40.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.2) | [[Harringtonine (drug)]] 5 µM 0.367× (z -9.2) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SHP-77 (line)]] | alt | 61.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -17.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 39.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -9.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 38.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -12.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -13.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 26.0 | 0 | 1 | — | [[Tetracycline (hydrochloride) (drug)]] 0.5 µM 0.0537× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 15.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +11.9) | — |
| [[C32 (line)]] | wt | 30.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 16.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +12.7) | — |
| [[COLO 205 (line)]] | alt | 29.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 32.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -9.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 42.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 29.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 23.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 39.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -9.4) ⚠ cell-cycle shift, explains ~93% of this change |
| [[RKO (line)]] | wt | 36.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -12.7) ⚠ cell-cycle shift, explains ~91% of this change |
| [[SW1417 (line)]] | alt | 28.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0803× (z -21.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1488), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STARD3]] | +0.69 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[GLUD1P3]] | +0.69 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[RNF4]] | +0.67 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[UBOX5]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[C8orf76]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[SH3BP5L]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[STX16-NPEPL1]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[EIF4ENIF1]] | +0.63 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[CTC-338M12.4]] | +0.62 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ZNF250]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[PIK3R4]] | +0.61 | +0.63 / +0.50 | both halves | 1e-05 | pathway: Phospholipid metabolism |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LGALS3]] | -0.59 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[SFR1]] | -0.58 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[MAPRE2]] | -0.58 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[IQCN]] | -0.57 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[KLF4]] | -0.56 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[SPTAN1]] | -0.55 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[RASEF]] | -0.54 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[OSR2]] | -0.54 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[TENT5C]] | -0.54 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[FAM222A]] | -0.53 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[JUN]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[TOB1]] | -0.53 | -0.53 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PGS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.590). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.1, 21.3); signed map (-44.7, 1.3). **Vector** length 104, 25.3% of its response variance represented; |z| ≥ 3 in 882 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +13.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -8.4 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -7.8 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | -4.5 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.1 | -2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.9 | -8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -0.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -2.2 | -2.1 |
|  | [[Aliskiren (drug)]] 0.5 µM |  | -2.2 | -3.5 |
|  | [[Adagrasib (drug)]] 5 µM |  | -2.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylglycerophosphate synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:78,378,649-78,425,114 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP762M186 |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 4 pathways, smallest: Synthesis of PG; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q32NB8](https://www.uniprot.org/uniprotkb/Q32NB8) (CDP-diacylglycerol--glycerol-3-phosphate 3-phosphatidyltransferase, mitochondrial):

> Functions in the biosynthesis of the anionic phospholipids phosphatidylglycerol and cardiolipin.

**Summary**, from NCBI Gene [9489](https://www.ncbi.nlm.nih.gov/gene/9489):

> Predicted to enable CDP-diacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity and calcium ion binding activity. Predicted to be involved in cardiolipin biosynthetic process and diacylglycerol metabolic process. Located in endoplasmic reticulum. Is active in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30029](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30029) · Entrez [9489](https://www.ncbi.nlm.nih.gov/gene/9489) · UniProt [Q32NB8](https://www.uniprot.org/uniprotkb/Q32NB8) · Ensembl [ENSG00000087157](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087157)

## Data

Gene col 1488: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1488); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1488, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1488]; `tensor/DDL_lfc|DDL_z.npy` [1488]; `embed/gene_vectors.npy` [1488]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1488 or target_col == 1488). Every well: [[PGS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
