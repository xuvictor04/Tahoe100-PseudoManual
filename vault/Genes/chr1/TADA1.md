---
symbol: "TADA1"
type: "gene"
col: 7620
ensembl_id: "ENSG00000152382"
name: "transcriptional adaptor 1"
location: "1q24.1"
module: 146
arm: "+"
pooled_cpm: 17.75
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# TADA1

*transcriptional adaptor 1* — 1q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 1.97× (z +5.2, q 1e-04, up in 24 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.493× (z -10.4, q 2e-22, down in 35 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.582× (z -7.9, q 2e-13, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEATR6]] (+0.73, fdr 7e-06), [[C6orf136]] (+0.73, fdr 7e-06), [[MRPL34]] (+0.71, fdr 7e-06); moves opposite to [[LINC00641]] (-0.65, fdr 1e-05), [[OSTM1]] (-0.65, fdr 1e-05), [[BACH1]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[KPNA4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7620.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.97×** | +5.2 | 1e-04 | 24/45 (A-427, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.005 | 18/48 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.2 | 0.005 | 17/46 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.086 | 12/48 (NCI-H460, SW480, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.53× | +3.3 | 0.13 | 6/44 (C32, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 1.23× | +3.0 | 0.23 | 17/48 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7620.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.493×** | -10.4 | 2e-22 | 35/41 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.485×** | -10.2 | 7e-22 | 19/30 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.569×** | -8.3 | 3e-14 | 31/48 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.549×** | -8.1 | 6e-14 | 26/36 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.582×** | -7.9 | 2e-13 | 31/47 (C32, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.654×** | -6.2 | 5e-08 | 22/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.656×** | -6.0 | 2e-07 | 27/47 (SW 900, A-172, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.771×** | -5.4 | 5e-06 | 30/48 (AsPC-1, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.692×** | -5.2 | 1e-05 | 23/46 (HS-578T, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.713×** | -5.0 | 4e-05 | 22/47 (A498, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.803×** | -4.6 | 3e-04 | 21/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | **0.828×** | -3.9 | 0.004 | 14/48 (NCI-H661, CFPAC-1, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.832×** | -3.8 | 0.006 | 22/47 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.7 | 0.010 | 15/48 (CFPAC-1, A-172, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.804×** | -3.2 | 0.051 | 11/48 (RPMI-7951, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **0.806×** | -3.2 | 0.053 | 4/47 (SW 900, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7620. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 38.6 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0709× (z -16.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 19.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 25.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -15.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 23.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -13.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 18.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -13.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 13.3 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.102× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 26.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -9.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 15.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -14.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -11.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 31.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0831× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -9.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 9.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -10.0) |
| [[HS-578T (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -9.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[J82 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -9.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -9.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -8.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -10.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -10.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0717× (z -22.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7620), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEATR6]] | +0.73 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[C6orf136]] | +0.73 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[MRPL34]] | +0.71 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ALG9]] | +0.70 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[PRMT9]] | +0.70 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[FHIP2A]] | +0.68 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[METTL17]] | +0.68 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[ATG4C]] | +0.67 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[LRIG2]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[MLLT10]] | +0.67 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[ANAPC4]] | +0.67 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[NOD1]] | +0.67 | +0.69 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00641]] | -0.65 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[OSTM1]] | -0.65 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[BACH1]] | -0.62 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[DDX5]] | -0.62 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[KPNA4]] | -0.61 | -0.46 / -0.62 | both halves | 2e-05 |  |
| [[SECISBP2]] | -0.60 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[TBILA]] | -0.60 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[SSUH2]] | -0.59 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.59 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[NABP1]] | -0.59 | -0.62 / -0.58 | both halves | 8e-06 |  |
| [[RNF32-AS1]] | -0.59 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[NOP14-AS1]] | -0.59 | -0.58 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TADA1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KPNA4]] | C | TADA1's natural level strengthens KPNA4's drug response | TADA1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.74, reverse -0.38; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.817). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-6.3, -7.8); signed map (-28.9, -12.0). **Vector** length 82.5, 16.5% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +1.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.3 | +3.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.5 | +1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.6 | -7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.1 | -10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.1 | -8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -4.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.9 | -2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | +0.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | transcriptional adaptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.1 — chr1:166,856,510-166,876,264 (-) |
| Ensembl biotype | protein_coding |
| Also known as | STAF42, ADA1, hADA1, HFI1; previously TADA1L |
| Gene groups (HGNC) | SAGA complex |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BN2](https://www.uniprot.org/uniprotkb/Q96BN2) (Transcriptional adapter 1):

> Probably involved in transcriptional regulation.

**Summary**, from NCBI Gene [117143](https://www.ncbi.nlm.nih.gov/gene/117143):

> TADA1L is a protein subunit of the human STAGA complex (SPT3; (MIM 602947)/TAF9 (MIM 600822)/GCN5 (MIM 602301) acetyltransferase complex), which is a chromatin-modifying multiprotein complex (Martinez et al., 2001 [PubMed 11564863]).[supplied by OMIM, Apr 2009]

**Accessions** — [HGNC:30631](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30631) · Entrez [117143](https://www.ncbi.nlm.nih.gov/gene/117143) · UniProt [Q96BN2](https://www.uniprot.org/uniprotkb/Q96BN2) · Ensembl [ENSG00000152382](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152382)

## Data

Gene col 7620: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7620); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7620, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7620]; `tensor/DDL_lfc|DDL_z.npy` [7620]; `embed/gene_vectors.npy` [7620]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7620 or target_col == 7620). Every well: [[TADA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TADA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
