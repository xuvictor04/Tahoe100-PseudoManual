---
symbol: "CHTF8"
type: "gene"
col: 9702
ensembl_id: "ENSG00000168802"
name: "chromosome transmission fidelity factor 8"
location: "16q22.1"
module: 11
arm: "+"
pooled_cpm: 23.21
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# CHTF8

*chromosome transmission fidelity factor 8* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +10.8, q 3e-24, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.699× (z -5.8, q 5e-06, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMG8]] (+0.71, fdr 7e-06), [[TMEM199]] (+0.71, fdr 1e-05), [[ZNF629]] (+0.69, fdr 1e-05); moves opposite to [[NDRG3]] (-0.64, fdr 2e-05), [[CAMK2G]] (-0.61, fdr 5e-05), [[MPP1]] (-0.60, fdr 6e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PNISR-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9702.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +10.8 | 3e-24 | 41/47 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +10.1 | 3e-21 | 20/48 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +7.5 | 1e-11 | 38/48 (SW480, HT-29, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +7.3 | 3e-11 | 33/48 (SW1417, A-427, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +6.1 | 1e-07 | 26/45 (HT-29, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +5.5 | 3e-06 | 23/43 (NCI-H2030, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +4.9 | 7e-05 | 20/48 (A498, NCI-H2030, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.005 | 19/47 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.007 | 13/48 (SW 900, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.012 | 19/48 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.029 | 9/46 (H4, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.054 | 11/47 (AsPC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9702.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.699×** | -5.8 | 5e-06 | 26/48 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.725×** | -5.2 | 7e-05 | 28/48 (NCI-H2030, HEC-1-A, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.753×** | -4.6 | 9e-04 | 21/48 (A-172, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.747×** | -4.5 | 9e-04 | 21/45 (NCI-H23, SNU-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.762×** | -4.4 | 0.001 | 21/48 (SK-MEL-2, LS 180, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.773×** | -4.1 | 0.003 | 19/46 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.796×** | -3.7 | 0.020 | 20/47 (SK-MEL-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.799×** | -3.4 | 0.045 | 17/48 (Hs 766T, H4, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.675×** | -3.3 | 0.061 | 12/48 (SNU-1, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.811×** | -3.2 | 0.070 | 13/32 (MIA PaCa-2, HCT15, …) | rises with dose | composition shift |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.873× | -3.0 | 0.12 | 7/48 (SW1417, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9702. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 22.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +8.9) | [[AZD2858 (drug)]] 5 µM 0.0792× (z -9.0) ⚠ toxic |
| [[SW48 (line)]] | wt | 19.1 | 0 | 2 | — | [[Silodosin (drug)]] 5 µM 0.0795× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 22.0 | 0 | 1 | — | [[Altretamine (drug)]] 0.05 µM 0.135× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 16.4 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.121× (z -9.0) |
| [[HOP62 (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.402× (z -8.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 32.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H2030 (line)]] | alt | 24.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0938× (z -16.7) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 23.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 23.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.167× (z -8.5) ⚠ toxic |
| [[SW1417 (line)]] | alt | 20.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.8) | — |
| [[SW480 (line)]] | alt | 37.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +11.1) | — |
| [[A-172 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9702), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG8]] | +0.71 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[TMEM199]] | +0.71 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[ZNF629]] | +0.69 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[UBE3B]] | +0.67 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[ZNF101]] | +0.67 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[FAM200A]] | +0.66 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[THBS4]] | +0.65 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[TMEM186]] | +0.65 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[PBLD]] | +0.65 | +0.60 / +0.31 | both halves | 2e-04 |  |
| [[TIGD6]] | +0.64 | +0.64 / +0.40 | both halves | 4e-05 |  |
| [[ZNF407-AS1]] | +0.64 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[LINS1]] | +0.64 | +0.69 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | -0.64 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[CAMK2G]] | -0.61 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[MPP1]] | -0.60 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[INPP5F]] | -0.59 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[MGAT4A]] | -0.57 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[ATP8A1]] | -0.57 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[PPP1CC]] | -0.57 | -0.34 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CHTF8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises CHTF8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PNISR-AS1]] | C | CHTF8's natural level strengthens PNISR-AS1's drug response | CHTF8's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.05; direction not clear | 0.068 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.543). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.4, 11.3); signed map (16.4, -12.2). **Vector** length 84.2, 16.5% of its response variance represented; |z| ≥ 3 in 783 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +7.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +4.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.8 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +1.8 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -4.4 | -4.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.6 | -5.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.4 | -4.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.1 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | chromosome transmission fidelity factor 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:69,118,010-69,132,588 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20400, CTF8 |
| Reactome | 6 pathways, smallest: Polymerase switching on the C-strand of the telomere; Telomere C-strand (Lagging Strand) Synthesis; Extension of Telomeres |
| Matched by | ensembl_id |

**Function**, from UniProt [P0CG13](https://www.uniprot.org/uniprotkb/P0CG13) (Chromosome transmission fidelity protein 8 homolog):

> Chromosome cohesion factor involved in sister chromatid cohesion and fidelity of chromosome transmission. Component of one of the cell nuclear antigen loader complexes, CTF18-replication factor C (CTF18-RFC), which consists of CTF18, CTF8, DSCC1, RFC2, RFC3, RFC4 and RFC5. The CTF18-RFC complex binds to single-stranded and primed DNAs and has weak ATPase activity that is stimulated the presence of primed DNA, replication protein A (RPA) and proliferating cell nuclear antigen (PCNA). The …

**Summary**, from NCBI Gene [54921](https://www.ncbi.nlm.nih.gov/gene/54921):

> This gene encodes a short protein that forms part of the Ctf18 replication factor C (RFC) complex that occurs in both yeast and mammals. The heteroheptameric RFC complex plays a role in sister chromatid cohesion and may load the replication clamp PCNA (proliferating cell nuclear antigen) onto DNA during DNA replication and repair. This gene is ubiquitously expressed and has been shown to have reduced expression in renal and prostate tumors. Alternatively spliced transcript variants have been …

**Accessions** — [HGNC:24353](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24353) · Entrez [54921](https://www.ncbi.nlm.nih.gov/gene/54921) · UniProt [P0CG13](https://www.uniprot.org/uniprotkb/P0CG13) · Ensembl [ENSG00000168802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168802)

## Data

Gene col 9702: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9702); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9702, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9702]; `tensor/DDL_lfc|DDL_z.npy` [9702]; `embed/gene_vectors.npy` [9702]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9702 or target_col == 9702). Every well: [[CHTF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHTF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
