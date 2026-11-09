---
symbol: "POLR2I"
type: "gene"
col: 2573
ensembl_id: "ENSG00000105258"
name: "RNA polymerase II subunit I"
location: "19q13.12"
module: 24
arm: "+"
pooled_cpm: 13.22
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# POLR2I

*RNA polymerase II subunit I* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.48× (z +6.8, q 8e-09, up in 36 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 7.17×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.590× (z -4.0, q 0.028, down in 33 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (H4 0.0447×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.0988×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPP21]] (+0.84, fdr 7e-06), [[NDUFB10]] (+0.78, fdr 1e-05), [[SSNA1]] (+0.77, fdr 1e-05); moves opposite to [[EIF4G2]] (-0.69, fdr 4e-05), [[HCFC1]] (-0.68, fdr 3e-05), [[TUG1]] (-0.68, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RAC3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NDUFC2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2573.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 7.17×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.48×** | +6.8 | 8e-09 | 36/36 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.24×** | +6.1 | 3e-07 | 24/24 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +4.2 | 0.005 | 30/41 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.99×** | +3.7 | 0.029 | 32/43 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | 1.94× | +3.3 | 0.10 | 19/29 (A549, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2573.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (H4 0.0447×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.0988×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.590×** | -4.0 | 0.028 | 33/46 (C-33 A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -3.9 | 0.028 | 28/46 (LS 180, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.540× | -3.3 | 0.16 | 30/47 (LoVo, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.547× | -3.2 | 0.16 | 28/47 (SW 900, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | 0.323× | -3.2 | 0.16 | 27/43 (NCI-H2030, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2573. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0447× (z -11.1) |
| [[Hs 766T (line)]] | wt | 11.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0988× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 8.97 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.17× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2573), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 20 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP21]] | +0.84 | +0.65 / +0.86 | both halves | 7e-06 |  |
| [[NDUFB10]] | +0.78 | +0.54 / +0.78 | both halves | 1e-05 | STRING 432 |
| [[SSNA1]] | +0.77 | +0.51 / +0.76 | both halves | 1e-05 |  |
| [[RBIS]] | +0.77 | +0.45 / +0.80 | both halves | 3e-05 |  |
| [[TMEM256]] | +0.77 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[ATP5MJ]] | +0.77 | +0.46 / +0.78 | both halves | 3e-05 |  |
| [[NOL7]] ⚠ | +0.76 | +0.64 / +0.73 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SMIM26]] ⚠ | +0.76 | +0.59 / +0.86 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[TRAPPC5]] | +0.76 | +0.46 / +0.78 | both halves | 3e-05 |  |
| [[POLR2J]] ⚠ | +0.75 | +0.29 / +0.79 | both halves | 3e-04 | same gene group; pathway: HALLMARK_DNA_REPAIR; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[MRPL41]] ⚠ | +0.75 | +0.36 / +0.80 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CHCHD5]] | +0.75 | +0.60 / +0.82 | both halves | 7e-06 |  |
| [[MRPL43]] | +0.74 | +0.44 / +0.75 | both halves | 3e-05 |  |
| [[GADD45GIP1]] | +0.74 | +0.55 / +0.78 | both halves | 1e-05 |  |
| [[RPS26]] | +0.73 | +0.59 / +0.64 | both halves | 7e-06 | pathway: Influenza Infection |
| [[ATP5ME]] | +0.73 | +0.55 / +0.74 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.69 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[HCFC1]] | -0.68 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[TUG1]] | -0.68 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[SECISBP2]] | -0.66 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[MOB1A]] | -0.66 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[DDX3X]] | -0.65 | -0.46 / -0.59 | both halves | 3e-05 | pathway: Dengue Virus-Host Interactions |
| [[SLC39A10]] | -0.64 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[MAPRE1]] | -0.63 | -0.43 / -0.70 | both halves | 3e-05 |  |
| [[FGD5-AS1]] | -0.63 | -0.48 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAC3]] | B | RAC3 activity raises POLR2I's level | lines that do not express RAC3 (7) vs lines expressing it (43) | 1.32× lower at baseline in the lines without RAC3 | 0.052 | ⚠ within organs, on part of the lines; also absent: FKBP10; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDUFC2]] | C | POLR2I's natural level strengthens NDUFC2's drug response | POLR2I's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse -0.04; direction not clear | 0.057 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.754). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-44.9, -14.2); signed map (-18.1, -6.8). **Vector** length 61.1, 16.3% of its response variance represented; |z| ≥ 3 in 456 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.53 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +0.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -4.1 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -4.0 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -3.5 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.3 | -0.4 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase II subunit I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:36,113,709-36,115,213 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPB9, hRPB14.5 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 75 pathways, smallest: Signaling by FGFR2 IIIa TM; PIWI-interacting RNA (piRNA) biogenesis; Abortive elongation of HIV-1 transcript in the absence of Tat |
| Matched by | ensembl_id |

**Function**, from UniProt [P36954](https://www.uniprot.org/uniprotkb/P36954) (DNA-directed RNA polymerase II subunit RPB9):

> Core component of RNA polymerase II (Pol II), a DNA-dependent RNA polymerase which synthesizes mRNA precursors and many functional non-coding RNAs using the four ribonucleoside triphosphates as substrates. Pol II is the central component of the basal RNA polymerase II transcription machinery. It is composed of mobile elements that move relative to each other. POLR2I/RPB9 is part of the upper jaw surrounding the central large cleft and thought to grab the incoming DNA template.

**Summary**, from NCBI Gene [5438](https://www.ncbi.nlm.nih.gov/gene/5438):

> This gene encodes a subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. This subunit, in combination with two other polymerase subunits, forms the DNA binding domain of the polymerase, a groove in which the DNA template is transcribed into RNA. The product of this gene has two zinc finger motifs with conserved cysteines and the subunit does possess zinc binding activity. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9196](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9196) · Entrez [5438](https://www.ncbi.nlm.nih.gov/gene/5438) · UniProt [P36954](https://www.uniprot.org/uniprotkb/P36954) · Ensembl [ENSG00000105258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105258)

## Data

Gene col 2573: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2573); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2573, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2573]; `tensor/DDL_lfc|DDL_z.npy` [2573]; `embed/gene_vectors.npy` [2573]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2573 or target_col == 2573). Every well: [[POLR2I — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR2I.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
