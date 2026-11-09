---
symbol: "CHMP2A"
type: "gene"
col: 5107
ensembl_id: "ENSG00000130724"
name: "charged multivesicular body protein 2A"
location: "19q13.43"
module: 48
arm: "+"
pooled_cpm: 39.91
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# CHMP2A

*charged multivesicular body protein 2A* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.22× (z +10.3, q 5e-22, up in 42 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (HEC-1-A 4.50×, NCI-H460 4.51×, A549 4.83×, PANC-1 3.43×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 3.94×, HEC-1-A 3.43×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.307×, NCI-H2030 0.386×); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.237×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Elimusertib hydrochloride (drug)]] 5 µM in 1 line (SK-MEL-2 0.0605×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL20]] (+0.70, fdr 1e-05), [[NDUFB11]] (+0.69, fdr 7e-06, ⚠ NDUFB11 in the vector space only through flagged drug-doses), [[COX6A1]] (+0.68, fdr 7e-06), [[SF3B6]] (+0.67, fdr 7e-06); moves opposite to [[CCT5]] (-0.60, fdr 1e-05), [[ADSS2]] (-0.59, fdr 1e-05), [[HNRNPAB]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5107.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (HEC-1-A 4.50×, NCI-H460 4.51×, A549 4.83×, PANC-1 3.43×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 3.94×, HEC-1-A 3.43×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.22×** | +10.3 | 5e-22 | 42/44 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.34×** | +7.2 | 2e-10 | 33/37 (SW480, HEC-1-A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.22×** | +6.5 | 2e-08 | 35/40 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.83×** | +5.3 | 1e-05 | 35/47 (SW1417, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.5 | 0.063 | 25/45 (RKO, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.12×** | +3.4 | 0.076 | 25/49 (A549, NCI-H460, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5107.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.307×, NCI-H2030 0.386×); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.237×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Elimusertib hydrochloride (drug)]] 5 µM in 1 line (SK-MEL-2 0.0605×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.763× | -3.4 | 0.24 | 26/47 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.684× | -3.3 | 0.24 | 25/48 (A498, A-427, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.505× | -3.0 | 0.44 | 29/48 (NCI-H1792, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5107. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 43.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 49.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.50× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 35.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +9.4) ⚠ toxic; transcription drop | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0605× (z -8.9) ⚠ toxic |
| [[SW480 (line)]] | alt | 37.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.94× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 79.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 48.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +9.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 47.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.115× (z -8.6) ⚠ toxic |
| [[HOP62 (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 56.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 27.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +10.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 67.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5107), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 14 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL20]] | +0.70 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[NDUFB11]] ⚠ | +0.69 | +0.59 / +0.75 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[COX6A1]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[SF3B6]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[TOMM7]] | +0.67 | +0.58 / +0.69 | both halves | 8e-06 | pathway: Autophagy |
| [[ETFB]] | +0.67 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[NDUFA2]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.66 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[ELOB]] | +0.66 | +0.51 / +0.69 | both halves | 1e-05 | pathway: HIV Infection |
| [[COX7C]] | +0.66 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[COX6B1]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[NDUFA11]] ⚠ | +0.66 | +0.52 / +0.66 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5ME]] | +0.66 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[ATP5MJ]] | +0.66 | +0.57 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT5]] | -0.60 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[ADSS2]] | -0.59 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[HNRNPAB]] | -0.57 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[ELK4]] | -0.56 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[FBXO30]] | -0.56 | -0.56 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.730). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-47.3, -20.4); signed map (-35.2, 7.5). **Vector** length 60.1, 15.7% of its response variance represented; |z| ≥ 3 in 430 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.56 to 31); *Respiratory electron transport* (reactome, mean cos +0.56 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.57 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.4 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +0.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.7 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +0.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.0 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.0 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | +0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | +0.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.6 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | charged multivesicular body protein 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:58,551,452-58,555,105 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BC-2, CHMP2, VPS2, VPS2A |
| Gene groups (HGNC) | Charged multivesicular body proteins; ESCRT-III |
| Reactome | 31 pathways, smallest: Translation of Replicase and Assembly of the Replication Transcription Complex_9679504; Translation of Replicase and Assembly of the Replication Transcription Complex_9694676; Pyroptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [O43633](https://www.uniprot.org/uniprotkb/O43633) (Charged multivesicular body protein 2a):

> Probable core component of the endosomal sorting required for transport complex III (ESCRT-III) which is involved in multivesicular bodies (MVBs) formation and sorting of endosomal cargo proteins into MVBs. MVBs contain intraluminal vesicles (ILVs) that are generated by invagination and scission from the limiting membrane of the endosome and mostly are delivered to lysosomes enabling degradation of membrane proteins, such as stimulated growth factor receptors, lysosomal enzymes and lipids. The …

**Summary**, from NCBI Gene [27243](https://www.ncbi.nlm.nih.gov/gene/27243):

> CHMP2A belongs to the chromatin-modifying protein/charged multivesicular body protein (CHMP) family. These proteins are components of ESCRT-III (endosomal sorting complex required for transport III), a complex involved in degradation of surface receptor proteins and formation of endocytic multivesicular bodies (MVBs). Some CHMPs have both nuclear and cytoplasmic/vesicular distributions, and one such CHMP, CHMP1A (MIM 164010), is required for both MVB formation and regulation of cell cycle …

**Accessions** — [HGNC:30216](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30216) · Entrez [27243](https://www.ncbi.nlm.nih.gov/gene/27243) · UniProt [O43633](https://www.uniprot.org/uniprotkb/O43633) · Ensembl [ENSG00000130724](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130724)

## Data

Gene col 5107: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5107); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5107, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5107]; `tensor/DDL_lfc|DDL_z.npy` [5107]; `embed/gene_vectors.npy` [5107]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5107 or target_col == 5107). Every well: [[CHMP2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHMP2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
