---
symbol: "HSPB11"
type: "gene"
col: 1328
ensembl_id: "ENSG00000081870"
name: "intraflagellar transport 25"
location: "1p32.3"
module: 40
arm: "+"
pooled_cpm: 43.36
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# HSPB11

*intraflagellar transport 25* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.65× (z +8.7, q 3e-15, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.522× (z -15.9, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHAP1]] (+0.79, fdr 7e-06), [[GMCL1]] (+0.77, fdr 7e-06), [[SDHAP2]] (+0.72, fdr 7e-06); moves opposite to [[MED1]] (-0.71, fdr 7e-06), [[ZC3H4]] (-0.69, fdr 1e-05), [[ST7L]] (-0.68, fdr 2e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1328.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +8.7 | 3e-15 | 31/48 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +7.7 | 4e-12 | 32/48 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +6.9 | 9e-10 | 29/48 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Verteporfin (drug)]] 5 µM |  | 1.20× | +3.1 | 0.29 | 18/48 (HT-29, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1328.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.522×** | -15.9 | 0e+00 | 39/47 (A-427, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.427×** | -14.7 | 0e+00 | 41/47 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.440×** | -13.6 | 4e-40 | 41/48 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.563×** | -9.9 | 5e-21 | 39/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.439×** | -7.4 | 1e-11 | 37/48 (HOP62, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.468×** | -6.9 | 6e-10 | 37/49 (NCI-H1792, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.677×** | -6.7 | 1e-09 | 32/48 (HOP62, SW 900, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -5.9 | 2e-07 | 26/47 (HCT15, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.723×** | -5.6 | 1e-06 | 30/48 (Hs 766T, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.724×** | -5.4 | 4e-06 | 27/48 (NCI-H1792, HS-578T, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.734×** | -5.4 | 4e-06 | 27/48 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.754×** | -4.9 | 5e-05 | 25/48 (hTERT-HPNE, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.825×** | -4.7 | 1e-04 | 25/48 (A498, NCI-H2347, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.787×** | -4.1 | 0.001 | 23/48 (hTERT-HPNE, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.807×** | -3.7 | 0.008 | 12/48 (LoVo, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.808×** | -3.5 | 0.018 | 19/47 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1328. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 52.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -15.1) |
| [[A498 (line)]] | wt | 66.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.377× (z -11.4) |
| [[HCT15 (line)]] | alt | 76.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -15.1) |
| [[HOP62 (line)]] | alt | 58.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -13.3) |
| [[HS-578T (line)]] | alt | 106 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -14.8) |
| [[CFPAC-1 (line)]] | alt | 48.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.362× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 46.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -17.6) |
| [[NCI-H2347 (line)]] | alt | 35.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -13.5) |
| [[SW480 (line)]] | alt | 52.1 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.298× (z -12.2) |
| [[A549 (line)]] | wt | 28.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 53.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -15.2) |
| [[H4 (line)]] | wt | 107 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.173× (z -12.4) |
| [[Hs 766T (line)]] | wt | 64.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -10.1) |
| [[KATO III (line)]] | alt | 23.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.317× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 30.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -11.6) |
| [[PANC-1 (line)]] | alt | 34.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.368× (z -10.9) |
| [[SNU-1 (line)]] | wt | 45.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -11.1) |
| [[A-427 (line)]] | wt | 33.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -18.0) |
| [[COLO 205 (line)]] | alt | 35.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 31.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -12.9) |
| [[HT-29 (line)]] | alt | 25.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -9.1) |
| [[J82 (line)]] | alt | 60.4 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.88× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 29.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.264× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 29.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -9.0) |
| [[LS 180 (line)]] | wt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 34.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -8.9) |
| [[RKO (line)]] | wt | 31.6 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0824× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 58.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.251× (z -11.0) |
| [[SHP-77 (line)]] | alt | 41.5 | 0 | 1 | — | [[Sonidegib (drug)]] 5 µM 0.103× (z -9.4) |
| [[SNU-423 (line)]] | alt | 53.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.351× (z -9.5) |
| [[SW1417 (line)]] | alt | 48.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +8.5) | — |
| [[SW48 (line)]] | wt | 28.5 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.142× (z -10.5) |
| [[AN3 CA (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 58.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1328), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP1]] | +0.79 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.77 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.72 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[HACE1]] | +0.72 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[CBFA2T2]] | +0.70 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[NTAN1]] | +0.70 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[ANKMY2]] | +0.70 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[SEC11A]] | +0.70 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[KCTD7]] | +0.70 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[SDHAP4]] | +0.69 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[SCAI]] | +0.69 | +0.69 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED1]] | -0.71 | -0.70 / -0.62 | both halves | 7e-06 | pathway: Organelle biogenesis and maintenance |
| [[ZC3H4]] | -0.69 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[ST7L]] | -0.68 | -0.68 / -0.46 | both halves | 2e-05 |  |
| [[ZNF462]] | -0.68 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.67 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[ZSCAN29]] | -0.67 | -0.68 / -0.44 | both halves | 3e-05 |  |
| [[TCF12]] | -0.67 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.67 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[ZNF629]] | -0.66 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[FEM1A]] | -0.65 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[BMPR1B]] | -0.65 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[SON]] | -0.65 | -0.64 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers HSPB11's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[EDN1]] | B | EDN1 activity strengthens HSPB11's drug response | lines that do not express EDN1 (27) vs lines expressing it (22) | the lines without EDN1 respond 0.84× as strongly (z diff +0.58); strongest at Panobinostat 5 µM: 1.27x vs 1.83x (z diff +3.0) | 0.068 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC; target measured in part of the lines; artifact flags |
| [[PCSK6]] | B | PCSK6 activity lowers HSPB11's level | lines that do not express PCSK6 (21) vs lines expressing it (29) | 1.39× higher at baseline in the lines without PCSK6 | 0.081 | ⚠ within organs, on part of the lines; also absent: BTNL9, CYP4F12, LINC02964 |
| [[LINC00857]] | B | LINC00857 activity lowers HSPB11's level | lines that do not express LINC00857 (17) vs lines expressing it (33) | 1.16× higher at baseline in the lines without LINC00857 | 0.082 | ⚠ within organs, on part of the lines; also absent: KRT18, C19orf33, OCLN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.744). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (3.1, -13.9); signed map (-35.3, 15.4). **Vector** length 123, 33.5% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.0 | +8.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.4 | +7.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.4 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | +2.3 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +1.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.6 | -9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.6 | -14.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.8 | -13.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.3 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.1 | -15.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.0 | -5.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.1 | -3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.8 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -7.4 |

## What is on record

|  |  |
|---|---|
| Name | intraflagellar transport 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:53,916,574-53,945,699 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPCO34, PP25, FAP232, CFAP232; previously C1orf41, HSPB11 |
| Gene groups (HGNC) | Small heat shock proteins; IFT-B1 complex |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y547](https://www.uniprot.org/uniprotkb/Q9Y547) (Intraflagellar transport protein 25 homolog):

> Component of the IFT complex B required for sonic hedgehog/SHH signaling. May mediate transport of SHH components: required for the export of SMO and PTCH1 receptors out of the cilium and the accumulation of GLI2 at the ciliary tip in response to activation of the SHH pathway, suggesting it is involved in the dynamic transport of SHH signaling molecules within the cilium. Not required for ciliary assembly. Its role in intraflagellar transport is mainly seen in tissues rich in ciliated cells …

**Summary**, from NCBI Gene [51668](https://www.ncbi.nlm.nih.gov/gene/51668):

> Predicted to enable metal ion binding activity. Predicted to be involved in kidney development; smoothened signaling pathway; and spermatogenesis. Predicted to act upstream of or within several processes, including left/right axis specification; lung development; and skeletal system development. Part of intraciliary transport particle A. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25019](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25019) · Entrez [51668](https://www.ncbi.nlm.nih.gov/gene/51668) · UniProt [Q9Y547](https://www.uniprot.org/uniprotkb/Q9Y547) · Ensembl [ENSG00000081870](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081870)

## Data

Gene col 1328: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1328); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1328, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1328]; `tensor/DDL_lfc|DDL_z.npy` [1328]; `embed/gene_vectors.npy` [1328]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1328 or target_col == 1328). Every well: [[HSPB11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPB11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
