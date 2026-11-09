---
symbol: "TM7SF2"
type: "gene"
col: 7412
ensembl_id: "ENSG00000149809"
name: "transmembrane 7 superfamily member 2"
location: "11q13.1"
module: 59
arm: "+"
pooled_cpm: 5.54
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 8
n_dd_up_clean: 25
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# TM7SF2

*transmembrane 7 superfamily member 2* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.28× (z +12.0, q 2e-30, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.567× (z -5.7, q 6e-06, down in 24 of 44 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEU1]] (+0.55, fdr 2e-05), [[SLC9A3R1]] (+0.53, fdr 1e-05), [[TNFSF9]] (+0.53, fdr 3e-05); moves opposite to [[NAA50]] (-0.51, fdr 4e-05), [[NAE1]] (-0.47, fdr 1e-04), [[NUP107]] (-0.47, fdr 4e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HES6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7412.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.28×** | +12.0 | 2e-30 | 38/46 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.99×** | +11.1 | 4e-26 | 35/47 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +7.7 | 3e-12 | 15/24 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.13×** | +7.6 | 3e-12 | 27/47 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +6.1 | 2e-07 | 12/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.78×** | +5.8 | 6e-07 | 20/44 (LS 180, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.73×** | +5.5 | 3e-06 | 22/46 (KATO III, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.4 | 4e-06 | 16/38 (LS 180, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +4.7 | 2e-04 | 14/41 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.5 | 3e-04 | 13/32 (LS 180, A549, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.4 | 6e-04 | 11/46 (HEC-1-A, A549, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.52×** | +4.2 | 0.001 | 14/44 (SW1417, LS 180, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +4.2 | 0.001 | 6/13 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.004 | 12/45 (BT-474, SW 900, …) | rises with dose | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.09×** | +3.9 | 0.004 | 9/31 (SW1417, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.006 | 13/37 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.57×** | +3.6 | 0.013 | 9/37 (NCI-H23, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.58×** | +3.3 | 0.027 | 10/40 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7412.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.567×** | -5.7 | 6e-06 | 24/44 (HCT15, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.578×** | -5.5 | 9e-06 | 20/43 (HCT15, HepG2/C3A, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.565×** | -5.0 | 9e-05 | 20/45 (RPMI-7951, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.623×** | -4.8 | 3e-04 | 20/46 (A-427, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.682×** | -3.9 | 0.012 | 15/47 (LoVo, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.654×** | -3.8 | 0.016 | 11/47 (RPMI-7951, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.713×** | -3.4 | 0.047 | 19/47 (NCI-H2030, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pyridoxine (drug)]] 5 µM |  | **0.788×** | -3.4 | 0.047 | 7/45 (SNU-1, HS-578T, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.726× | -3.1 | 0.12 | 6/45 (SK-MEL-2, SW 1271, …) | top dose only | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | 0.730× | -3.0 | 0.13 | 5/46 (NCI-H460, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7412. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 14.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.83× (z +9.2) | — |
| [[A-427 (line)]] | wt | 10.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -8.7) |
| [[LS 180 (line)]] | wt | 8.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.33× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 3.20 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.5 µM 0.0654× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 10.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0302× (z -15.6) |
| [[RKO (line)]] | wt | 5.73 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0378× (z -10.9) |
| [[SHP-77 (line)]] | alt | 4.04 | 0 | 1 | — | [[Folic acid (drug)]] 0.05 µM 0.0570× (z -8.9) |
| [[A-172 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.43 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7412), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 7 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEU1]] | +0.55 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[SLC9A3R1]] | +0.53 | +0.59 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[TNFSF9]] | +0.53 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[PIM2]] | +0.53 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[PNPLA2]] | +0.53 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[NUDT14]] | +0.53 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[INSIG1]] | +0.52 | +0.39 / +0.43 | both halves | 6e-05 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 414 |
| [[ECH1]] | +0.50 | +0.57 / +0.46 | both halves | 2e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[DCXR]] | +0.50 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[TP53INP2]] | +0.49 | +0.59 / +0.34 | both halves | 1e-04 |  |
| [[JUND]] | +0.48 | +0.57 / +0.37 | both halves | 8e-05 |  |
| [[ROGDI]] | +0.47 | +0.38 / +0.51 | both halves | 6e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA50]] | -0.51 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[NAE1]] | -0.47 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[NUP107]] | -0.47 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[ADAT2]] | -0.44 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[METTL3]] | -0.44 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[UCHL5]] | -0.43 | -0.27 / -0.37 | both halves | 3e-04 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[PCGF6]] | -0.43 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[ZNF595]] | -0.42 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[TUBGCP4]] | -0.42 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[ADCY3]] | -0.42 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[CACYBP]] | -0.41 | -0.50 / -0.31 | both halves | 2e-04 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[CBX3]] | -0.41 | -0.47 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES6]] | B | HES6 activity raises TM7SF2's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.71× lower at baseline in the lines without HES6 | 0.030 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers TM7SF2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.449). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (31.9, -30.0); signed map (-6.0, 20.1). **Vector** length 52.5, 6.82% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +2.2 | +4.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.1 | +6.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.1 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +1.9 | +3.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.8 | +11.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.7 | +3.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -5.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.7 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane 7 superfamily member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,111,845-65,116,384 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C14SR, ANG1, DHCR14A, NET47 |
| Gene groups (HGNC) | Dehydrocholesterol reductases |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway); Cholesterol biosynthesis via desmosterol (Bloch pathway); Cholesterol biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O76062](https://www.uniprot.org/uniprotkb/O76062) (Delta(14)-sterol reductase TM7SF2):

> Catalyzes the reduction of the C14-unsaturated bond of lanosterol, as part of the metabolic pathway leading to cholesterol biosynthesis.

**Summary**, from NCBI Gene [7108](https://www.ncbi.nlm.nih.gov/gene/7108):

> Enables Delta14-sterol reductase activity. Involved in cholesterol biosynthetic process. Located in endoplasmic reticulum. Part of signaling receptor complex. Is active in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11863](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11863) · Entrez [7108](https://www.ncbi.nlm.nih.gov/gene/7108) · UniProt [O76062](https://www.uniprot.org/uniprotkb/O76062) · Ensembl [ENSG00000149809](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149809)

## Data

Gene col 7412: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7412); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7412, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7412]; `tensor/DDL_lfc|DDL_z.npy` [7412]; `embed/gene_vectors.npy` [7412]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7412 or target_col == 7412). Every well: [[TM7SF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TM7SF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
