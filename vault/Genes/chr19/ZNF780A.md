---
symbol: "ZNF780A"
type: "gene"
col: 12464
ensembl_id: "ENSG00000197782"
name: "zinc finger protein 780A"
location: "19q13.2"
module: 16
arm: "+"
pooled_cpm: 18.81
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZNF780A

*zinc finger protein 780A* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.11× (z +15.7, q 0e+00, up in 40 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.620× (z -10.1, q 5e-21, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF776]] (+0.77, fdr 7e-06), [[VPS72]] (+0.77, fdr 7e-06), [[ZSCAN12]] (+0.77, fdr 7e-06); moves opposite to [[MFN1]] (-0.65, fdr 1e-05), [[RABGEF1]] (-0.62, fdr 1e-05), [[SENP5]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TSPYL5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12464.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +15.7 | 0e+00 | 40/45 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +9.4 | 1e-18 | 31/48 (HT-29, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +7.5 | 2e-11 | 26/45 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.21×** | +6.2 | 1e-07 | 25/47 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +5.4 | 7e-06 | 22/45 (A-427, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.40×** | +4.9 | 7e-05 | 14/46 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +4.3 | 0.001 | 12/47 (PANC-1, KATO III, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.003 | 12/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.060 | 10/47 (A-427, SNU-1, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.23× | +3.1 | 0.12 | 7/48 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Vismodegib (drug)]] 0.05 µM |  | 1.23× | +3.0 | 0.13 | 6/47 (NCI-H2347, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12464.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.620×** | -10.1 | 5e-21 | 37/45 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -5.5 | 1e-05 | 20/45 (SK-MEL-2, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.690×** | -5.3 | 2e-05 | 18/43 (PANC-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.756×** | -4.2 | 0.005 | 18/45 (PANC-1, SNU-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.772×** | -3.7 | 0.024 | 22/46 (SNU-1, HT-29, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.845× | -3.5 | 0.039 | 12/47 (J82, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.799×** | -3.3 | 0.068 | 8/47 (PANC-1, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12464. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 143 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.378× (z -11.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -11.1) |
| [[A549 (line)]] | wt | 20.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 8.98 | 0 | 2 | — | [[Radotinib (drug)]] 0.5 µM 0.0916× (z -10.8) |
| [[A-172 (line)]] | wt | 7.03 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 5.25 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0709× (z -8.6) |
| [[H4 (line)]] | wt | 6.50 | 0 | 1 | — | [[Orlistat (drug)]] 5 µM 0.0501× (z -8.7) |
| [[HCT15 (line)]] | alt | 18.4 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.171× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 24.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.143× (z -8.6) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 9.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +11.7) | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 8.45 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -8.5) |
| [[SHP-77 (line)]] | alt | 30.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 16.6 | 0 | 1 | — | [[vincristine (drug)]] 0.5 µM 0.0540× (z -11.6) |
| [[SNU-1 (line)]] | wt | 17.3 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.154× (z -8.7) |
| [[SNU-423 (line)]] | alt | 9.52 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.133× (z -9.1) ⚠ toxic |
| [[SW480 (line)]] | alt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.8) | — |
| [[A-427 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12464), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF776]] | +0.77 | +0.80 / +0.71 | both halves | 7e-06 | same gene group |
| [[VPS72]] | +0.77 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[ZSCAN12]] | +0.77 | +0.78 / +0.74 | both halves | 7e-06 | same gene group |
| [[ZNF221]] | +0.76 | +0.75 / +0.77 | both halves | 7e-06 | same gene group |
| [[ZNF260]] | +0.76 | +0.74 / +0.74 | both halves | 7e-06 | same gene group |
| [[ZNF268]] | +0.75 | +0.81 / +0.67 | both halves | 7e-06 | same gene group |
| [[ZNF480]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 | same gene group |
| [[MRPL47]] | +0.72 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[ZNF502]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 | same gene group |
| [[ZNF155]] | +0.71 | +0.83 / +0.60 | both halves | 7e-06 | same gene group |
| [[CSTF2T]] | +0.71 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[ZNF606]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFN1]] | -0.65 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[RABGEF1]] | -0.62 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[SENP5]] | -0.62 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[TAF5]] | -0.60 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[SLC37A3]] | -0.60 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[KDELR1]] | -0.59 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[EEF1AKMT4]] | -0.59 | -0.62 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPYL5]] | B | TSPYL5 activity raises ZNF780A's level | lines that do not express TSPYL5 (36) vs lines expressing it (14) | 1.64× lower at baseline in the lines without TSPYL5 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000241168, LINC02999, LINC01205 |
| [[TOP2A]] | B | TOP2A activity raises ZNF780A's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.857). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-32.1, 10.6); signed map (2.0, -27.5). **Vector** length 74.8, 13.4% of its response variance represented; |z| ≥ 3 in 821 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.6 | +9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +15.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +7.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +5.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.5 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +1.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -10.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -5.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -1.9 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.7 | -3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.2 | -2.4 |
|  | [[Rucaparib (phosphate) (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 780A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,069,152-40,090,943 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF780 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O75290](https://www.uniprot.org/uniprotkb/O75290) (Zinc finger protein 780A):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [284323](https://www.ncbi.nlm.nih.gov/gene/284323):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleoplasm. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27603](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27603) · Entrez [284323](https://www.ncbi.nlm.nih.gov/gene/284323) · UniProt [O75290](https://www.uniprot.org/uniprotkb/O75290) · Ensembl [ENSG00000197782](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197782)

## Data

Gene col 12464: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12464); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12464, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12464]; `tensor/DDL_lfc|DDL_z.npy` [12464]; `embed/gene_vectors.npy` [12464]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12464 or target_col == 12464). Every well: [[ZNF780A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF780A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
