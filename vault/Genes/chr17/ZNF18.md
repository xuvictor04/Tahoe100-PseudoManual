---
symbol: "ZNF18"
type: "gene"
col: 7858
ensembl_id: "ENSG00000154957"
name: "zinc finger protein 18"
location: "17p12"
module: 17
arm: "+"
pooled_cpm: 6.14
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ZNF18

*zinc finger protein 18* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.52× (z +5.4, q 3e-05, up in 21 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.397× (z -11.9, q 4e-30, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD18]] (+0.75, fdr 7e-06), [[FAM114A2]] (+0.70, fdr 2e-05), [[ZNF571]] (+0.67, fdr 7e-06); moves opposite to [[CDK14]] (-0.49, fdr 4e-05), [[CDKN2B-AS1]] (-0.49, fdr 5e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7858.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +5.4 | 3e-05 | 21/46 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +5.3 | 3e-05 | 17/46 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.24×** | +4.0 | 0.012 | 11/46 (SW480, KATO III, …) | top dose only | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.041 | 8/46 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.15 | 5/47 (Hs 766T, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.15 | 14/41 (NCI-H2030, SW480, …) | inconsistent across doses | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.27× | +3.1 | 0.15 | 2/45 (SW48, SW480) | rises with dose | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.26× | +3.0 | 0.18 | 3/38 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7858.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.397×** | -11.9 | 4e-30 | 34/46 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.483×** | -9.4 | 1e-18 | 33/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.497×** | -9.1 | 2e-17 | 24/40 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.519×** | -8.5 | 3e-15 | 27/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.518×** | -8.2 | 3e-14 | 22/32 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.604×** | -6.5 | 6e-09 | 21/46 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.618×** | -6.2 | 4e-08 | 21/43 (A498, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.630×** | -6.0 | 2e-07 | 17/27 (LOX-IMVI, LoVo, …) | inconsistent across doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.726×** | -5.9 | 3e-07 | 18/46 (HS-578T, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.641×** | -5.8 | 5e-07 | 17/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.662×** | -5.3 | 5e-06 | 21/44 (NCI-H460, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.706×** | -4.5 | 3e-04 | 17/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.705×** | -4.4 | 6e-04 | 7/46 (NCI-H460, A-172, …) | top dose only | position effect removed |
| [[Pentoxifylline (drug)]] 0.05 µM | ⚠ transcription drop | **0.742×** | -3.9 | 0.005 | 7/43 (PANC-1, A549, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.823×** | -3.6 | 0.014 | 11/40 (Hs 766T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.841× | -3.2 | 0.052 | 2/45 (SHP-77, A-427) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7858. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.58 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0933× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0972× (z -14.0) |
| [[SW480 (line)]] | alt | 8.45 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.138× (z -13.1) |
| [[Hs 766T (line)]] | wt | 5.84 | 0 | 3 (1 ⚠) | — | [[Trifluridine (drug)]] 0.5 µM 0.0902× (z -8.9) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0948× (z -8.7) |
| [[PANC-1 (line)]] | alt | 8.86 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 5.93 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.130× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 2.61 | 0 | 1 | — | [[Busulfan (drug)]] 0.05 µM 0.0607× (z -8.5) |
| [[COLO 205 (line)]] | alt | 5.66 | 0 | 1 | — | [[Sunitinib (drug)]] 0.05 µM 0.0603× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 3.88 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0553× (z -11.5) |
| [[HOP62 (line)]] | alt | 5.55 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0756× (z -10.9) |
| [[HS-578T (line)]] | alt | 7.25 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.193× (z -10.5) |
| [[KATO III (line)]] | alt | 7.90 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0873× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 7.25 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0842× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 7.83 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0710× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.159× (z -9.2) ⚠ toxic |
| [[SW1417 (line)]] | alt | 5.05 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.1000× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7858), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD18]] | +0.75 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[FAM114A2]] | +0.70 | +0.83 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[ZNF571]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 | same gene group |
| [[GEMIN2]] | +0.66 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[SUGT1P4-STRA6LP]] | +0.63 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[STRA6LP]] | +0.62 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[TUT1]] | +0.62 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[TRAPPC11]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[SUPT20H]] | +0.60 | +0.68 / +0.40 | both halves | 5e-05 |  |
| [[MRPS31P4]] | +0.60 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ZNF25]] | +0.59 | +0.59 / +0.57 | both halves | 9e-06 | same gene group |
| [[C17orf58]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK14]] | -0.49 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[CDKN2B-AS1]] | -0.49 | -0.40 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ZNF18's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[C3orf18]] | B | C3orf18 activity raises ZNF18's level | lines that do not express C3orf18 (10) vs lines expressing it (40) | 1.37× lower at baseline in the lines without C3orf18 | 0.079 | ⚠ within organs, on part of the lines; also absent: TMCC2, SELENOM; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-28.8, -0.5); signed map (-20.0, -15.2). **Vector** length 56.5, 7.52% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +1.7 | +3.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.7 | +1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.4 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | -1.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[Bexarotene (drug)]] 5 µM |  | +1.1 | +0.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.8 | -11.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | -8.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -6.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.1 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p12 — chr17:11,977,439-11,997,475 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZKSCAN6, KOX11, HDSG1, Zfp535, ZNF535, ZSCAN38 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17022](https://www.uniprot.org/uniprotkb/P17022) (Zinc finger protein 18):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7566](https://www.ncbi.nlm.nih.gov/gene/7566):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:12969](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12969) · Entrez [7566](https://www.ncbi.nlm.nih.gov/gene/7566) · UniProt [P17022](https://www.uniprot.org/uniprotkb/P17022) · Ensembl [ENSG00000154957](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154957)

## Data

Gene col 7858: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7858); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7858, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7858]; `tensor/DDL_lfc|DDL_z.npy` [7858]; `embed/gene_vectors.npy` [7858]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7858 or target_col == 7858). Every well: [[ZNF18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
