---
symbol: "MRPL14"
type: "gene"
col: 11153
ensembl_id: "ENSG00000180992"
name: "mitochondrial ribosomal protein L14"
location: "6p21.1"
module: 54
arm: "+"
pooled_cpm: 24.77
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# MRPL14

*mitochondrial ribosomal protein L14* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.70× (z +6.2, q 4e-07, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.552× (z -10.8, q 2e-24, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5F1D]] (+0.70, fdr 7e-05, ⚠ ATP5F1D in the vector space only through flagged drug-doses), [[UQCR10]] (+0.69, fdr 1e-04, ⚠ UQCR10 in the vector space only through flagged drug-doses), [[ANTKMT]] (+0.68, fdr 3e-04), [[LSM2]] (+0.67, fdr 1e-04), [[MRPL57]] (+0.67, fdr 4e-04); moves opposite to [[PRKAR1A]] (-0.62, fdr 7e-05), [[LHFPL3]] (-0.61, fdr 2e-04), [[CROCC]] (-0.61, fdr 3e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11153.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.70×** | +6.2 | 4e-07 | 40/48 (HT-29, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.53×** | +5.5 | 1e-05 | 29/46 (PANC-1, NCI-H1792, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.55×** | +5.4 | 1e-05 | 25/48 (PANC-1, HEC-1-A, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.43×** | +4.7 | 5e-04 | 25/47 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.42×** | +4.6 | 6e-04 | 27/46 (HS-578T, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **1.40×** | +4.2 | 0.003 | 26/47 (NCI-H23, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.37×** | +4.1 | 0.004 | 24/48 (Panc 03.27, NCI-H2347, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.35×** | +3.9 | 0.007 | 20/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.34×** | +3.8 | 0.011 | 19/47 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.39× | +3.1 | 0.12 | 13/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11153.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.552×** | -10.8 | 2e-24 | 42/48 (LOX-IMVI, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -4.6 | 0.001 | 27/47 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.722×** | -4.0 | 0.011 | 21/48 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.758×** | -3.6 | 0.054 | 22/48 (SW 1088, NCI-H1573, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.779× | -3.2 | 0.16 | 18/47 (NCI-H2030, HCT15, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.782× | -3.0 | 0.24 | 17/35 (Panc 03.27, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11153. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 27.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -15.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 26.9 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -9.5) |
| [[A498 (line)]] | wt | 23.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 16.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 27.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 33.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -9.2) |
| [[HOP62 (line)]] | alt | 21.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -8.8) |
| [[HS-578T (line)]] | alt | 25.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -10.0) |
| [[KATO III (line)]] | alt | 35.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -9.3) |
| [[LoVo (line)]] | wt | 26.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 31.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -15.8) |
| [[NCI-H2030 (line)]] | alt | 33.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.458× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -10.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -14.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 31.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -10.6) |
| [[RKO (line)]] | wt | 33.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -11.6) |
| [[SW 900 (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0709× (z -15.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11153), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 20 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1D]] ⚠ | +0.70 | +0.38 / +0.64 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UQCR10]] ⚠ | +0.69 | +0.35 / +0.71 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ANTKMT]] | +0.68 | +0.28 / +0.62 | both halves | 3e-04 |  |
| [[LSM2]] | +0.67 | +0.33 / +0.68 | both halves | 1e-04 |  |
| [[MRPL57]] | +0.67 | +0.25 / +0.73 | both halves | 4e-04 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 835 |
| [[MRPL12]] | +0.66 | +0.22 / +0.66 | both halves | 6e-04 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 932 |
| [[POP7]] | +0.66 | +0.38 / +0.65 | both halves | 6e-05 |  |
| [[NDUFC2]] | +0.66 | +0.39 / +0.62 | both halves | 5e-05 |  |
| [[RPL22L1]] ⚠ | +0.65 | +0.41 / +0.65 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LAGE3]] | +0.65 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[NDUFA8]] | +0.64 | +0.39 / +0.66 | both halves | 6e-05 |  |
| [[WRAP73]] | +0.63 | +0.31 / +0.59 | both halves | 2e-04 |  |
| [[POLR2I]] | +0.63 | +0.23 / +0.57 | both halves | 5e-04 |  |
| [[EMC6]] | +0.63 | +0.40 / +0.67 | both halves | 5e-05 |  |
| [[PAFAH1B3]] | +0.62 | +0.31 / +0.54 | both halves | 2e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKAR1A]] | -0.62 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[LHFPL3]] | -0.61 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[CROCC]] | -0.61 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[DVL3]] | -0.60 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[AP2B1]] | -0.60 | -0.30 / -0.66 | both halves | 2e-04 |  |
| [[ATXN1L]] | -0.59 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[PAPOLA]] | -0.59 | -0.27 / -0.57 | both halves | 3e-04 |  |
| [[UBE2A]] | -0.59 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[MSL3]] | -0.59 | -0.32 / -0.53 | both halves | 1e-04 |  |
| [[N4BP2]] | -0.58 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[SNHG22]] | -0.58 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[LRP2BP]] | -0.58 | -0.38 / -0.45 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MRPL14's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.686). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-47.2, -14.7); signed map (-32.6, 4.1). **Vector** length 90.7, 21.8% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +4.0 | +4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.9 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +3.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | +6.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.5 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | -0.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.9 | -10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.0 | -2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.9 | -3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.7 | -1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | +0.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:44,113,451-44,127,452 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPML32, MRP-L32, uL14m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P1L8](https://www.uniprot.org/uniprotkb/Q6P1L8) (Large ribosomal subunit protein uL14m):

> Forms part of 2 intersubunit bridges in the assembled ribosome. Upon binding to MALSU1 intersubunit bridge formation is blocked, preventing ribosome formation and repressing translation (Probable).

**Summary**, from NCBI Gene [64928](https://www.ncbi.nlm.nih.gov/gene/64928):

> This nuclear gene encodes a protein component of the 39S subunit of the mitochondrial ribosome. A pseudogene of this gene is found on chromosome 17. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:14279](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14279) · Entrez [64928](https://www.ncbi.nlm.nih.gov/gene/64928) · UniProt [Q6P1L8](https://www.uniprot.org/uniprotkb/Q6P1L8) · Ensembl [ENSG00000180992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180992)

## Data

Gene col 11153: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11153); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11153, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11153]; `tensor/DDL_lfc|DDL_z.npy` [11153]; `embed/gene_vectors.npy` [11153]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11153 or target_col == 11153). Every well: [[MRPL14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
