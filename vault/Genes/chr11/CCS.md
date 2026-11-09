---
symbol: "CCS"
type: "gene"
col: 10451
ensembl_id: "ENSG00000173992"
name: "copper chaperone for superoxide dismutase"
location: "11q13.2"
module: 4
arm: "-"
pooled_cpm: 17.81
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CCS

*copper chaperone for superoxide dismutase* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.48× (z +15.2, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.529× (z -5.6, q 1e-05, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NKAP]] (+0.69, fdr 7e-06), [[TULP3]] (+0.69, fdr 1e-05), [[SIRT2]] (+0.68, fdr 7e-06); moves opposite to [[NAA15]] (-0.68, fdr 7e-06), [[PRKDC]] (-0.66, fdr 7e-06), [[TMEM33]] (-0.66, fdr 1e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10451.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.48×** | +15.2 | 0e+00 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.48×** | +15.1 | 0e+00 | 43/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.93×** | +10.9 | 1e-25 | 38/48 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +10.4 | 3e-23 | 27/47 (AsPC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +8.3 | 2e-14 | 27/47 (NCI-H2030, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +7.2 | 4e-11 | 27/43 (SW 900, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +7.0 | 2e-10 | 32/47 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.29×** | +6.0 | 2e-07 | 23/48 (A-427, LoVo, …) | rises with dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.9 | 2e-07 | 27/48 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +4.7 | 1e-04 | 16/48 (PANC-1, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.25×** | +3.7 | 0.010 | 17/47 (A-427, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.7 | 0.012 | 16/48 (LS 180, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.22×** | +3.3 | 0.041 | 11/48 (A-427, SW480, …) | rises with dose |  |
| [[Ciclopirox (drug)]] 5 µM |  | 1.15× | +3.3 | 0.042 | 6/48 (A549, NCI-H1573, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.056 | 10/48 (A-427, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.082 | 4/46 (LS 180, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10451.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.529×** | -5.6 | 1e-05 | 27/48 (HS-578T, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.723×** | -5.2 | 4e-05 | 24/46 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.551×** | -5.2 | 4e-05 | 23/46 (A-427, SW1417, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.774×** | -4.3 | 0.002 | 15/48 (LS 180, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.775×** | -4.3 | 0.002 | 19/40 (Panc 03.27, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.768×** | -4.3 | 0.002 | 15/33 (LOX-IMVI, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10451. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 26.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +11.6) | — |
| [[Panc 03.27 (line)]] | alt | 22.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 17.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.48× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 14.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.18× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.153× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 11.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +8.6) | — |
| [[SW480 (line)]] | alt | 18.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.11× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.163× (z -10.5) ⚠ toxic |
| [[A549 (line)]] | wt | 14.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +11.5) | — |
| [[C32 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0617× (z -13.8) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 13.4 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.05 µM 0.0709× (z -10.7) |
| [[HS-578T (line)]] | alt | 20.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +8.5) | — |
| [[J82 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0956× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~51% of this change |
| [[MIA PaCa-2 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0628× (z -10.1) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 21.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +10.3) | — |
| [[RKO (line)]] | wt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -8.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10451), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAP]] | +0.69 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[TULP3]] | +0.69 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[SIRT2]] | +0.68 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[SEC22A]] | +0.68 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[SPATA7]] | +0.67 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[RANBP10]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SAT2]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[HMGCL]] | +0.65 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[ADPRM]] | +0.65 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.64 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[SUGP1]] | +0.64 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[OGA]] | +0.64 | +0.62 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA15]] | -0.68 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[PRKDC]] | -0.66 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[TMEM33]] | -0.66 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.65 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[XRCC5]] | -0.64 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[SRFBP1]] | -0.63 | -0.42 / -0.66 | both halves | 4e-05 |  |
| [[MTHFD1]] | -0.62 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[ATIC]] | -0.62 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[TMX3]] | -0.62 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[CCT5]] | -0.62 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[C1QBP]] | -0.62 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[XRN2]] | -0.61 | -0.58 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCS's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.651). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-25.7, -32.0); signed map (-14.9, 4.2). **Vector** length 75.4, 13.5% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +7.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +4.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +1.9 | +6.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +0.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.1 | -0.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.0 | -5.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.0 | -5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.7 | -4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.7 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | copper chaperone for superoxide dismutase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,593,153-66,606,019 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 4 pathways, smallest: Detoxification of Reactive Oxygen Species; Cellular response to chemical stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [O14618](https://www.uniprot.org/uniprotkb/O14618) (Copper chaperone for superoxide dismutase):

> Delivers copper to copper zinc superoxide dismutase (SOD1).

**Summary**, from NCBI Gene [9973](https://www.ncbi.nlm.nih.gov/gene/9973):

> Copper chaperone for superoxide dismutase specifically delivers Cu to copper/zinc superoxide dismutase and may activate copper/zinc superoxide dismutase through direct insertion of the Cu cofactor. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1613](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1613) · Entrez [9973](https://www.ncbi.nlm.nih.gov/gene/9973) · UniProt [O14618](https://www.uniprot.org/uniprotkb/O14618) · Ensembl [ENSG00000173992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173992)

## Data

Gene col 10451: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10451); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10451, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10451]; `tensor/DDL_lfc|DDL_z.npy` [10451]; `embed/gene_vectors.npy` [10451]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10451 or target_col == 10451). Every well: [[CCS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
